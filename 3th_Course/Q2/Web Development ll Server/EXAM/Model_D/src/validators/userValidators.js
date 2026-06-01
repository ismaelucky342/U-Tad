const { body, param } = require('express-validator');
const loginValidators = [
  body('email').isEmail().withMessage('El correo electrónico no es válido.').normalizeEmail(),
  body('password').notEmpty().withMessage('La contraseña es obligatoria.'),
];
const createUserValidators = [
  body('username').trim().notEmpty().withMessage('El nombre de usuario es obligatorio.').isLength({ min: 3, max: 50 }).withMessage('Entre 3 y 50 caracteres.')
    .matches(/^[a-zA-Z0-9_]+$/).withMessage('Solo letras, números y guiones bajos.'),
  body('email').isEmail().withMessage('Correo no válido.').normalizeEmail(),
  body('fullName').trim().notEmpty().withMessage('El nombre completo es obligatorio.').isLength({ min: 2, max: 100 }).withMessage('Entre 2 y 100 caracteres.'),
  body('password').isLength({ min: 6 }).withMessage('Mínimo 6 caracteres.'),
  body('isAdmin').optional().isBoolean().withMessage('Debe ser un booleano.'),
];
const updateUserValidators = [
  param('id').isInt({ min: 1 }).withMessage('ID debe ser entero positivo.'),
  body('username').optional().trim().isLength({ min: 3, max: 50 }),
  body('email').optional().isEmail().normalizeEmail(),
  body('fullName').optional().trim().isLength({ min: 2, max: 100 }),
  body('password').optional().isLength({ min: 6 }),
  body('isAdmin').optional().isBoolean(),
];
const idParamValidator = [param('id').isInt({ min: 1 }).withMessage('ID debe ser entero positivo.')];
module.exports = { loginValidators, createUserValidators, updateUserValidators, idParamValidator };
