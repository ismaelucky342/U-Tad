const { body, validationResult } = require('express-validator');

// Middleware para manejar errores de validación
const handleValidationErrors = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({
      success: false,
      message: 'Errores de validación',
      errors: errors.array().map(err => ({
        field: err.param,
        message: err.msg
      }))
    });
  }
  next();
};

// Reglas de validación para usuarios
const validateUserRegistration = [
  body('fullName')
    .notEmpty().withMessage('El nombre completo es requerido')
    .isLength({ min: 3 }).withMessage('El nombre debe tener al menos 3 caracteres'),
  body('username')
    .notEmpty().withMessage('El username es requerido')
    .isLength({ min: 3 }).withMessage('El username debe tener al menos 3 caracteres')
    .matches(/^[a-zA-Z0-9_]+$/).withMessage('El username solo puede contener letras, números y guiones bajos'),
  body('email')
    .notEmpty().withMessage('El correo es requerido')
    .isEmail().withMessage('Ingrese un correo válido'),
  body('phone')
    .notEmpty().withMessage('El teléfono es requerido')
    .matches(/^[\d\s\-\+\(\)]+$/).withMessage('El teléfono debe ser válido'),
  body('position')
    .notEmpty().withMessage('El cargo es requerido')
    .isIn(['Admin', 'Manager', 'Staff', 'Chef', 'Delivery']).withMessage('Cargo no válido'),
  body('password')
    .notEmpty().withMessage('La contraseña es requerida')
    .isLength({ min: 6 }).withMessage('La contraseña debe tener al menos 6 caracteres')
];

const validateUserLogin = [
  body('email')
    .notEmpty().withMessage('El correo es requerido')
    .isEmail().withMessage('Ingrese un correo válido'),
  body('password')
    .notEmpty().withMessage('La contraseña es requerida')
];

// Reglas de validación para productos
const validateProductCreation = [
  body('name')
    .notEmpty().withMessage('El nombre del producto es requerido')
    .isLength({ min: 3, max: 100 }).withMessage('El nombre debe tener entre 3 y 100 caracteres'),
  body('description')
    .notEmpty().withMessage('La descripción es requerida')
    .isLength({ min: 10, max: 500 }).withMessage('La descripción debe tener entre 10 y 500 caracteres'),
  body('price')
    .notEmpty().withMessage('El precio es requerido')
    .isFloat({ min: 0 }).withMessage('El precio debe ser un número positivo'),
  body('ingredients')
    .notEmpty().withMessage('Los ingredientes son requeridos')
    .isLength({ min: 3 }).withMessage('Los ingredientes deben tener al menos 3 caracteres')
];

// Reglas de validación para pedidos
const validateOrderCreation = [
  body('paymentMethod')
    .notEmpty().withMessage('El método de pago es requerido')
    .isIn(['Credit Card', 'Debit Card', 'Cash', 'PayPal', 'Transfer']).withMessage('Método de pago no válido'),
  body('products')
    .isArray({ min: 1 }).withMessage('Debe contener al menos un producto'),
  body('products.*.productId')
    .notEmpty().withMessage('El ID del producto es requerido'),
  body('products.*.quantity')
    .notEmpty().withMessage('La cantidad es requerida')
    .isInt({ min: 1 }).withMessage('La cantidad debe ser un número entero positivo'),
  body('customer.name')
    .optional()
    .isLength({ min: 3 }).withMessage('El nombre debe tener al menos 3 caracteres'),
  body('customer.email')
    .optional()
    .isEmail().withMessage('Ingrese un correo válido'),
  body('customer.phone')
    .optional()
    .matches(/^[\d\s\-\+\(\)]+$/).withMessage('El teléfono debe ser válido')
];

module.exports = {
  handleValidationErrors,
  validateUserRegistration,
  validateUserLogin,
  validateProductCreation,
  validateOrderCreation
};
