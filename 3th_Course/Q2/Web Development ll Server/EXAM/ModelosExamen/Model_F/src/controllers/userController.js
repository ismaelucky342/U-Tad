const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const login = async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await User.findOne({ where: { email } });
    if (!user || !(await bcrypt.compare(password, user.password))) return res.status(401).json({ error: 'Credenciales incorrectas.' });
    const token = jwt.sign({ id: user.id, email: user.email, isAdmin: user.isAdmin }, process.env.JWT_SECRET, { expiresIn: '8h' });
    return res.status(200).json({ message: 'Login correcto.', token });
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
const getAllUsers = async (req, res) => {
  try {
    const users = await User.findAll({ attributes: { exclude: ['password'] } });
    return res.status(200).json(users);
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
const getUserById = async (req, res) => {
  const { id } = req.params;
  try {
    const user = await User.findByPk(id, { attributes: { exclude: ['password'] } });
    if (!user) return res.status(404).json({ error: 'No encontrado.' });
    return res.status(200).json(user);
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
const createUser = async (req, res) => {
  const { username, email, fullName, password, isAdmin } = req.body;
  try {
    if (await User.findOne({ where: { email } })) return res.status(409).json({ error: 'Email ya existe.' });
    if (await User.findOne({ where: { username } })) return res.status(409).json({ error: 'Usuario ya existe.' });
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = await User.create({ username, email, fullName, password: hashedPassword, isAdmin: isAdmin || false });
    return res.status(201).json({ message: 'Usuario creado.', user: { id: newUser.id } });
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
const updateUser = async (req, res) => {
  const { id } = req.params;
  const { username, email, fullName, password, isAdmin } = req.body;
  try {
    const user = await User.findByPk(id);
    if (!user) return res.status(404).json({ error: 'No encontrado.' });
    const updateData = {};
    if (username) updateData.username = username;
    if (email) updateData.email = email;
    if (fullName) updateData.fullName = fullName;
    if (password) updateData.password = await bcrypt.hash(password, 10);
    if (isAdmin !== undefined) updateData.isAdmin = isAdmin;
    await user.update(updateData);
    return res.status(200).json({ message: 'Actualizado.' });
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
const deleteUser = async (req, res) => {
  const { id } = req.params;
  try {
    const user = await User.findByPk(id);
    if (!user) return res.status(404).json({ error: 'No encontrado.' });
    await user.destroy();
    return res.status(200).json({ message: 'Eliminado.' });
  } catch (error) { return res.status(500).json({ error: 'Error interno.' }); }
};
module.exports = { login, getAllUsers, getUserById, createUser, updateUser, deleteUser };
