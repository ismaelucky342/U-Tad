// src/validators/orderValidators.js
const { body } = require('express-validator');

const validateCreateOrder = [
  body('items')
    .notEmpty().withMessage('Los items del pedido son obligatorios')
    .isArray({ min: 1 }).withMessage('Debe incluir al menos un producto'),

  body('items.*.productName')
    .notEmpty().withMessage('El nombre del producto es obligatorio')
    .isString().withMessage('El nombre debe ser texto'),

  body('items.*.quantity')
    .notEmpty().withMessage('La cantidad es obligatoria')
    .isInt({ min: 1 }).withMessage('La cantidad debe ser un entero mayor que 0'),

  body('items.*.unitPrice')
    .notEmpty().withMessage('El precio unitario es obligatorio')
    .isFloat({ min: 0 }).withMessage('El precio no puede ser negativo'),

  body('shippingAddress')
    .trim()
    .notEmpty().withMessage('La dirección de envío es obligatoria')
    .isLength({ min: 5, max: 200 }).withMessage('Entre 5 y 200 caracteres'),

  body('notes')
    .optional()
    .trim()
    .isLength({ max: 500 }).withMessage('Las notas no pueden superar 500 caracteres'),
];

const validateUpdateOrder = [
  body('status')
    .optional()
    .isIn(['pending', 'confirmed', 'shipped', 'delivered', 'cancelled'])
    .withMessage('Estado no válido. Valores permitidos: pending, confirmed, shipped, delivered, cancelled'),

  body('shippingAddress')
    .optional()
    .trim()
    .isLength({ min: 5, max: 200 }).withMessage('Entre 5 y 200 caracteres'),

  body('notes')
    .optional()
    .trim()
    .isLength({ max: 500 }).withMessage('Las notas no pueden superar 500 caracteres'),
];

module.exports = { validateCreateOrder, validateUpdateOrder };
