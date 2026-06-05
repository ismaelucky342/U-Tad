// src/validators/userValidators.js
const { body } = require('express-validator');

const validateRegister = [
  body('username')
    .trim()
    .notEmpty().withMessage('El nombre de usuario es obligatorio')
    .isLength({ min: 3, max: 30 }).withMessage('Entre 3 y 30 caracteres'),

  body('email')
    .trim()
    .notEmpty().withMessage('El email es obligatorio')
    .isEmail().withMessage('Email no válido')
    .normalizeEmail(),

  body('fullName')
    .trim()
    .notEmpty().withMessage('El nombre completo es obligatorio')
    .isLength({ min: 2, max: 100 }).withMessage('Entre 2 y 100 caracteres'),

  body('password')
    .notEmpty().withMessage('La contraseña es obligatoria')
    .isLength({ min: 6 }).withMessage('Mínimo 6 caracteres'),

  body('phone')
    .optional()
    .isMobilePhone().withMessage('Número de teléfono no válido'),

  body('address')
    .optional()
    .trim()
    .isLength({ max: 200 }).withMessage('Dirección demasiado larga'),

  body('role')
    .optional()
    .isIn(['admin', 'client']).withMessage('El rol debe ser "admin" o "client"'),
];

const validateUpdateUser = [
  body('email')
    .optional().trim().isEmail().withMessage('Email no válido').normalizeEmail(),

  body('fullName')
    .optional().trim().isLength({ min: 2, max: 100 }).withMessage('Entre 2 y 100 caracteres'),

  body('password')
    .optional().isLength({ min: 6 }).withMessage('Mínimo 6 caracteres'),

  body('phone')
    .optional().isMobilePhone().withMessage('Número de teléfono no válido'),

  body('address')
    .optional().trim().isLength({ max: 200 }).withMessage('Dirección demasiado larga'),
];

const validateLogin = [
  body('email')
    .trim().notEmpty().withMessage('El email es obligatorio')
    .isEmail().withMessage('Email no válido'),

  body('password')
    .notEmpty().withMessage('La contraseña es obligatoria'),
];

module.exports = { validateRegister, validateUpdateUser, validateLogin };
