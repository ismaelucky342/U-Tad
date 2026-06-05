// src/controllers/userController.js
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');

// ============================================================
// CAMBIA POCO: La estructura de este controlador es genérica.
// Solo ajusta los campos al crear/actualizar según tu modelo.
// ============================================================

/** POST /users/login - Login de usuario */
const login = async (req, res) => {
  try {
    const { email, password } = req.body;

    // Buscar usuario por email
    const user = await User.findOne({ where: { email } });
    if (!user) {
      return res.status(401).json({ success: false, message: 'Credenciales incorrectas' });
    }

    // Verificar contraseña con bcrypt
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(401).json({ success: false, message: 'Credenciales incorrectas' });
    }

    // Generar token JWT con id, email y rol del usuario
    const token = jwt.sign(
      { id: user.id, email: user.email, role: user.role },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN || '24h' }
    );

    return res.status(200).json({
      success: true,
      message: 'Login exitoso',
      token,
      user: {
        id: user.id,
        username: user.username,
        email: user.email,
        fullName: user.fullName,
        role: user.role,
      },
    });
  } catch (error) {
    console.error('Error en login:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** GET /users - Obtener todos los usuarios */
const getAllUsers = async (req, res) => {
  try {
    const users = await User.findAll({
      attributes: { exclude: ['password'] },   // Nunca devolver la contraseña
    });
    return res.status(200).json({ success: true, data: users });
  } catch (error) {
    console.error('Error al obtener usuarios:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** GET /users/:id - Obtener usuario por ID */
const getUserById = async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id, {
      attributes: { exclude: ['password'] },
    });

    if (!user) {
      return res.status(404).json({ success: false, message: 'Usuario no encontrado' });
    }

    return res.status(200).json({ success: true, data: user });
  } catch (error) {
    console.error('Error al obtener usuario:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** POST /users - Crear nuevo usuario */
const createUser = async (req, res) => {
  try {
    const { username, email, fullName, password, role } = req.body;

    // Verificar si el email ya existe
    const existingUser = await User.findOne({ where: { email } });
    if (existingUser) {
      return res.status(409).json({ success: false, message: 'El email ya está registrado' });
    }

    // Hashear la contraseña con bcrypt (salt rounds = 10)
    const hashedPassword = await bcrypt.hash(password, 10);

    const newUser = await User.create({
      username,
      email,
      fullName,
      password: hashedPassword,
      role: role || 'user',
    });

    // Devolver el usuario sin la contraseña
    const { password: _, ...userWithoutPassword } = newUser.toJSON();
    return res.status(201).json({
      success: true,
      message: 'Usuario creado correctamente',
      data: userWithoutPassword,
    });
  } catch (error) {
    console.error('Error al crear usuario:', error);
    if (error.name === 'SequelizeUniqueConstraintError') {
      return res.status(409).json({ success: false, message: 'El username o email ya existe' });
    }
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** PUT /users/:id - Actualizar usuario */
const updateUser = async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id);
    if (!user) {
      return res.status(404).json({ success: false, message: 'Usuario no encontrado' });
    }

    const { username, email, fullName, password, role } = req.body;
    const updateData = {};

    if (username !== undefined) updateData.username = username;
    if (email !== undefined) updateData.email = email;
    if (fullName !== undefined) updateData.fullName = fullName;
    if (role !== undefined) updateData.role = role;
    if (password !== undefined) {
      updateData.password = await bcrypt.hash(password, 10);
    }

    await user.update(updateData);

    const { password: _, ...updated } = user.toJSON();
    return res.status(200).json({
      success: true,
      message: 'Usuario actualizado correctamente',
      data: updated,
    });
  } catch (error) {
    console.error('Error al actualizar usuario:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** DELETE /users/:id - Eliminar usuario */
const deleteUser = async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id);
    if (!user) {
      return res.status(404).json({ success: false, message: 'Usuario no encontrado' });
    }

    await user.destroy();
    return res.status(200).json({ success: true, message: 'Usuario eliminado correctamente' });
  } catch (error) {
    console.error('Error al eliminar usuario:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

module.exports = { login, getAllUsers, getUserById, createUser, updateUser, deleteUser };
