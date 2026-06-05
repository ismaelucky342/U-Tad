// src/controllers/userController.js
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');

// ── Helper: excluye la contraseña del objeto devuelto ────────
const sanitize = (user) => {
  const { password, ...safe } = user.toJSON ? user.toJSON() : user;
  return safe;
};

/** POST /users/login */
const login = async (req, res) => {
  try {
    const { email, password } = req.body;
    const user = await User.findOne({ where: { email, isActive: true } });

    if (!user || !(await bcrypt.compare(password, user.password))) {
      return res.status(401).json({ success: false, message: 'Credenciales incorrectas' });
    }

    const token = jwt.sign(
      { id: user.id, email: user.email, role: user.role },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN || '24h' }
    );

    return res.status(200).json({
      success: true,
      message: 'Login exitoso',
      token,
      user: sanitize(user),
    });
  } catch (error) {
    console.error('Error en login:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** POST /users/register — Registro público (crea cliente) */
const register = async (req, res) => {
  try {
    const { username, email, fullName, password, phone, address } = req.body;

    const existing = await User.findOne({ where: { email } });
    if (existing) {
      return res.status(409).json({ success: false, message: 'El email ya está registrado' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = await User.create({
      username, email, fullName,
      password: hashedPassword,
      phone, address,
      role: 'client',   // El registro público siempre crea clientes
    });

    return res.status(201).json({
      success: true,
      message: 'Usuario registrado correctamente',
      data: sanitize(newUser),
    });
  } catch (error) {
    console.error('Error en registro:', error);
    if (error.name === 'SequelizeUniqueConstraintError') {
      return res.status(409).json({ success: false, message: 'El username o email ya existe' });
    }
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** GET /users — Solo admin: lista todos los usuarios */
const getAllUsers = async (req, res) => {
  try {
    const users = await User.findAll({ attributes: { exclude: ['password'] } });
    return res.status(200).json({ success: true, count: users.length, data: users });
  } catch (error) {
    console.error('Error al obtener usuarios:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** GET /users/:id
 *  - Admin: puede ver cualquier usuario
 *  - Client: solo puede ver su propio perfil (controlado en ruta con isOwnerOrAdmin)
 */
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

/** POST /users — Solo admin: crear usuario con cualquier rol */
const createUser = async (req, res) => {
  try {
    const { username, email, fullName, password, phone, address, role } = req.body;

    const existing = await User.findOne({ where: { email } });
    if (existing) {
      return res.status(409).json({ success: false, message: 'El email ya está registrado' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = await User.create({
      username, email, fullName,
      password: hashedPassword,
      phone, address,
      role: role || 'client',
    });

    return res.status(201).json({
      success: true,
      message: 'Usuario creado correctamente',
      data: sanitize(newUser),
    });
  } catch (error) {
    console.error('Error al crear usuario:', error);
    if (error.name === 'SequelizeUniqueConstraintError') {
      return res.status(409).json({ success: false, message: 'El username o email ya existe' });
    }
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** PUT /users/:id
 *  - Admin: puede actualizar cualquier campo de cualquier usuario
 *  - Client: puede actualizar solo su propio perfil (controlado en ruta)
 */
const updateUser = async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id);
    if (!user) {
      return res.status(404).json({ success: false, message: 'Usuario no encontrado' });
    }

    const { email, fullName, password, phone, address, role, isActive } = req.body;
    const updateData = {};

    if (email !== undefined) updateData.email = email;
    if (fullName !== undefined) updateData.fullName = fullName;
    if (phone !== undefined) updateData.phone = phone;
    if (address !== undefined) updateData.address = address;
    if (password !== undefined) updateData.password = await bcrypt.hash(password, 10);

    // Solo el admin puede cambiar rol y estado activo
    if (req.user.role === 'admin') {
      if (role !== undefined) updateData.role = role;
      if (isActive !== undefined) updateData.isActive = isActive;
    }

    await user.update(updateData);
    return res.status(200).json({
      success: true,
      message: 'Usuario actualizado correctamente',
      data: sanitize(user),
    });
  } catch (error) {
    console.error('Error al actualizar usuario:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** DELETE /users/:id — Solo admin */
const deleteUser = async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id);
    if (!user) {
      return res.status(404).json({ success: false, message: 'Usuario no encontrado' });
    }
    // Soft delete: desactivar en lugar de borrar para no romper FK de pedidos
    await user.update({ isActive: false });
    return res.status(200).json({ success: true, message: 'Usuario desactivado correctamente' });
  } catch (error) {
    console.error('Error al eliminar usuario:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

module.exports = { login, register, getAllUsers, getUserById, createUser, updateUser, deleteUser };
