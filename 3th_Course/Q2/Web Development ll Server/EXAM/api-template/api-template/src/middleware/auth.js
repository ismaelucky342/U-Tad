// src/middleware/auth.js
const jwt = require('jsonwebtoken');

// ============================================================
// NO CAMBIAR: Este middleware es genérico y reutilizable tal cual
// ============================================================

/**
 * Middleware: verifica que el token JWT es válido.
 * Uso: añadir como segundo argumento en cualquier ruta protegida.
 * Ejemplo: router.get('/ruta', verifyToken, controlador)
 */
const verifyToken = (req, res, next) => {
  // El token llega en el header: Authorization: Bearer <token>
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({
      success: false,
      message: 'Acceso denegado. Token no proporcionado.',
    });
  }

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;   // Guarda el payload del token en req.user
    next();
  } catch (error) {
    return res.status(403).json({
      success: false,
      message: 'Token inválido o expirado.',
    });
  }
};

/**
 * Middleware: verifica que el usuario tiene rol de administrador.
 * SIEMPRE se usa después de verifyToken.
 * Ejemplo: router.delete('/ruta', verifyToken, isAdmin, controlador)
 */
const isAdmin = (req, res, next) => {
  if (!req.user || req.user.role !== 'admin') {
    return res.status(403).json({
      success: false,
      message: 'Acceso denegado. Se requieren permisos de administrador.',
    });
  }
  next();
};

module.exports = { verifyToken, isAdmin };
