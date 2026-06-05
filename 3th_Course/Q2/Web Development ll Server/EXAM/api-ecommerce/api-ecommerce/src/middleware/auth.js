// src/middleware/auth.js
const jwt = require('jsonwebtoken');

/**
 * Verifica que el token JWT es válido.
 * Inyecta req.user = { id, email, role }
 */
const verifyToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ success: false, message: 'Acceso denegado. Token no proporcionado.' });
  }

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    return res.status(403).json({ success: false, message: 'Token inválido o expirado.' });
  }
};

/**
 * Solo admins pueden pasar.
 */
const isAdmin = (req, res, next) => {
  if (!req.user || req.user.role !== 'admin') {
    return res.status(403).json({ success: false, message: 'Acceso denegado. Se requieren permisos de administrador.' });
  }
  next();
};

/**
 * Admins y clients autenticados pueden pasar.
 * Uso: rutas que requieren login pero no necesariamente ser admin.
 */
const isAuthenticated = (req, res, next) => {
  if (!req.user) {
    return res.status(401).json({ success: false, message: 'Debes iniciar sesión.' });
  }
  next();
};

/**
 * Verifica que el usuario autenticado es dueño del recurso O es admin.
 * Se usa para que un cliente solo vea/edite SUS pedidos.
 * Requiere que la ruta tenga :userId o que el controlador compruebe req.user.id.
 */
const isOwnerOrAdmin = (req, res, next) => {
  const requestedUserId = parseInt(req.params.userId || req.params.id);
  if (req.user.role === 'admin' || req.user.id === requestedUserId) {
    return next();
  }
  return res.status(403).json({ success: false, message: 'No tienes permiso para acceder a este recurso.' });
};

module.exports = { verifyToken, isAdmin, isAuthenticated, isOwnerOrAdmin };
