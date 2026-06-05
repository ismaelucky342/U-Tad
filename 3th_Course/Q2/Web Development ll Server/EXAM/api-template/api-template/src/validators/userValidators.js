// src/validators/userValidators.js
const { body } = require('express-validator');

// ============================================================
// CAMBIA ESTO: Ajusta las validaciones según los campos de tu modelo
// ============================================================

/** Validaciones para el registro/creación de usuario */
const validateCreateUser = [
  body('username')
    .trim()
    .notEmpty().withMessage('El nombre de usuario es obligatorio')
    .isLength({ min: 3, max: 30 }).withMessage('El username debe tener entre 3 y 30 caracteres'),

  body('email')
    .trim()
    .notEmpty().withMessage('El correo electrónico es obligatorio')
    .isEmail().withMessage('Debe ser un correo electrónico válido')
    .normalizeEmail(),

  body('fullName')
    .trim()
    .notEmpty().withMessage('El nombre completo es obligatorio')
    .isLength({ min: 2, max: 100 }).withMessage('El nombre debe tener entre 2 y 100 caracteres'),

  body('password')
    .notEmpty().withMessage('La contraseña es obligatoria')
    .isLength({ min: 6 }).withMessage('La contraseña debe tener al menos 6 caracteres'),

  body('role')
    .optional()
    .isIn(['admin', 'user']).withMessage('El rol debe ser "admin" o "user"'),
];

/** Validaciones para actualización (todos opcionales) */
const validateUpdateUser = [
  body('email')
    .optional()
    .trim()
    .isEmail().withMessage('Debe ser un correo electrónico válido')
    .normalizeEmail(),

  body('fullName')
    .optional()
    .trim()
    .isLength({ min: 2, max: 100 }).withMessage('El nombre debe tener entre 2 y 100 caracteres'),

  body('password')
    .optional()
    .isLength({ min: 6 }).withMessage('La contraseña debe tener al menos 6 caracteres'),
];

/** Validaciones para el login */
const validateLogin = [
  body('email')
    .trim()
    .notEmpty().withMessage('El correo es obligatorio')
    .isEmail().withMessage('Debe ser un correo válido'),

  body('password')
    .notEmpty().withMessage('La contraseña es obligatoria'),
];

module.exports = { validateCreateUser, validateUpdateUser, validateLogin };
