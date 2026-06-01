const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const login = async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await User.findOne({ where: { email } });
    if (!user) return res.status(401).json({ error: 'Credenciales incorrectas.' });
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) return res.status(401).json({ error: 'Credenciales incorrectas.' });
    const token = jwt.sign({ id: user.id, email: user.email, isAdmin: user.isAdmin }, process.env.JWT_SECRET, { expiresIn: '8h' });
    return res.status(200).json({ message: 'Login correcto.', token, user: { id: user.id, username: user.username, email: user.email, fullName: user.fullName, isAdmin: user.isAdmin } });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
const getAllUsers = async (req, res) => {
  try {
    const users = await User.findAll({ attributes: { exclude: ['password'] } });
    return res.status(200).json(users);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
const getUserById = async (req, res) => {
  const { id } = req.params;
  try {
    const user = await User.findByPk(id, { attributes: { exclude: ['password'] } });
    if (!user) return res.status(404).json({ error: `Usuario con ID ${id} no encontrado.` });
    return res.status(200).json(user);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
const createUser = async (req, res) => {
  const { username, email, fullName, password, isAdmin } = req.body;
  try {
    let existing = await User.findOne({ where: { email } });
    if (existing) return res.status(409).json({ error: 'Ya existe un usuario con ese correo electrónico.' });
    existing = await User.findOne({ where: { username } });
    if (existing) return res.status(409).json({ error: 'Ya existe un usuario con ese nombre de usuario.' });
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = await User.create({ username, email, fullName, password: hashedPassword, isAdmin: isAdmin || false });
    return res.status(201).json({ message: 'Usuario creado correctamente.', user: { id: newUser.id, username: newUser.username, email: newUser.email, fullName: newUser.fullName, isAdmin: newUser.isAdmin } });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
const updateUser = async (req, res) => {
  const { id } = req.params;
  const { username, email, fullName, password, isAdmin } = req.body;
  try {
    const user = await User.findByPk(id);
    if (!user) return res.status(404).json({ error: `Usuario con ID ${id} no encontrado.` });
    if (email && email !== user.email) {
      const existing = await User.findOne({ where: { email } });
      if (existing) return res.status(409).json({ error: 'Ya existe un usuario con ese correo electrónico.' });
    }
    if (username && username !== user.username) {
      const existing = await User.findOne({ where: { username } });
      if (existing) return res.status(409).json({ error: 'Ya existe un usuario con ese nombre de usuario.' });
    }
    const updateData = {};
    if (username) updateData.username = username;
    if (email) updateData.email = email;
    if (fullName) updateData.fullName = fullName;
    if (password) updateData.password = await bcrypt.hash(password, 10);
    if (isAdmin !== undefined) updateData.isAdmin = isAdmin;
    await user.update(updateData);
    return res.status(200).json({ message: 'Usuario actualizado correctamente.', user: { id: user.id, username: user.username, email: user.email, fullName: user.fullName, isAdmin: user.isAdmin } });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
const deleteUser = async (req, res) => {
  const { id } = req.params;
  try {
    const user = await User.findByPk(id);
    if (!user) return res.status(404).json({ error: `Usuario con ID ${id} no encontrado.` });
    await user.destroy();
    return res.status(200).json({ message: `Usuario con ID ${id} eliminado correctamente.` });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};
module.exports = { login, getAllUsers, getUserById, createUser, updateUser, deleteUser };
