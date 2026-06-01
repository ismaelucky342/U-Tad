const jwt = require('jsonwebtoken');
const User = require('../models/User');
const verifyToken = async (req, res, next) => {
  const authHeader = req.headers['authorization'];
  if (!authHeader || !authHeader.startsWith('Bearer ')) return res.status(401).json({ error: 'Token no proporcionado.' });
  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    const user = await User.findByPk(decoded.id);
    if (!user) return res.status(401).json({ error: 'Usuario no encontrado.' });
    req.user = user;
    next();
  } catch { return res.status(401).json({ error: 'Token inválido.' }); }
};
const verifyAdmin = (req, res, next) => {
  if (!req.user || !req.user.isAdmin) return res.status(403).json({ error: 'Se requieren permisos de administrador.' });
  next();
};
module.exports = { verifyToken, verifyAdmin };
