const { body, param } = require('express-validator');

const loginValidators = [
  body('email')
    .isEmail().withMessage('El correo electrónico no es válido.')
    .normalizeEmail(),
  body('password')
    .notEmpty().withMessage('La contraseña es obligatoria.'),
];

const createUserValidators = [
  body('username')
    .trim()
    .notEmpty().withMessage('El nombre de usuario es obligatorio.')
    .isLength({ min: 3, max: 50 }).withMessage('El nombre de usuario debe tener entre 3 y 50 caracteres.')
    .matches(/^[a-zA-Z0-9_]+$/).withMessage('El nombre de usuario solo puede contener letras, números y guiones bajos.'),
  body('email')
    .isEmail().withMessage('El correo electrónico no es válido.')
    .normalizeEmail(),
  body('fullName')
    .trim()
    .notEmpty().withMessage('El nombre completo es obligatorio.')
    .isLength({ min: 2, max: 100 }).withMessage('El nombre completo debe tener entre 2 y 100 caracteres.'),
  body('password')
    .isLength({ min: 6 }).withMessage('La contraseña debe tener al menos 6 caracteres.'),
  body('isAdmin')
    .optional()
    .isBoolean().withMessage('El campo isAdmin debe ser un booleano.'),
];

const updateUserValidators = [
  param('id')
    .isInt({ min: 1 }).withMessage('El ID debe ser un número entero positivo.'),
  body('username')
    .optional()
    .trim()
    .isLength({ min: 3, max: 50 }).withMessage('El nombre de usuario debe tener entre 3 y 50 caracteres.')
    .matches(/^[a-zA-Z0-9_]+$/).withMessage('El nombre de usuario solo puede contener letras, números y guiones bajos.'),
  body('email')
    .optional()
    .isEmail().withMessage('El correo electrónico no es válido.')
    .normalizeEmail(),
  body('fullName')
    .optional()
    .trim()
    .isLength({ min: 2, max: 100 }).withMessage('El nombre completo debe tener entre 2 y 100 caracteres.'),
  body('password')
    .optional()
    .isLength({ min: 6 }).withMessage('La contraseña debe tener al menos 6 caracteres.'),
  body('isAdmin')
    .optional()
    .isBoolean().withMessage('El campo isAdmin debe ser un booleano.'),
];

const idParamValidator = [
  param('id')
    .isInt({ min: 1 }).withMessage('El ID debe ser un número entero positivo.'),
];

module.exports = {
  loginValidators,
  createUserValidators,
  updateUserValidators,
  idParamValidator,
};
