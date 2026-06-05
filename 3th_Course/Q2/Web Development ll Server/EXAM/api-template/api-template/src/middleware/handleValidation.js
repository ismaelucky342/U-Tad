// src/middleware/handleValidation.js
const { validationResult } = require('express-validator');

// ============================================================
// NO CAMBIAR: Middleware genérico para gestionar errores de validación.
// Se usa después de los arrays de validación de express-validator.
// ============================================================

/**
 * Middleware que recoge los errores de express-validator y devuelve 400
 * si hay algún campo inválido. Si todo está bien, pasa al controlador.
 */
const handleValidation = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({
      success: false,
      message: 'Error de validación',
      errors: errors.array().map(err => ({
        field: err.path,
        message: err.msg,
      })),
    });
  }
  next();
};

module.exports = handleValidation;
