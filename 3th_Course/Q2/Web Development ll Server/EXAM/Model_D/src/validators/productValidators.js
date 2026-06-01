const { body, param } = require('express-validator');
const createProductValidators = [
  body('name').trim().notEmpty().isLength({ min: 3, max: 200 }),
  body('description').optional().isString(),
  body('price').notEmpty().isFloat({ min: 0 }),
  body('stock').notEmpty().isInt({ min: 0 }),
  body('category').trim().notEmpty().isLength({ min: 2, max: 100 }),
  body('brand').trim().notEmpty().isLength({ min: 2, max: 100 }),
  body('imageUrl').optional().isURL(),
  body('weight').notEmpty().isFloat({ min: 0 }),
  body('registeredDate').notEmpty().isDate({ format: 'YYYY-MM-DD' }),
];
const updateProductValidators = [
  param('id').isInt({ min: 1 }),
  body('name').optional().trim().isLength({ min: 3, max: 200 }),
  body('description').optional().isString(),
  body('price').optional().isFloat({ min: 0 }),
  body('stock').optional().isInt({ min: 0 }),
  body('category').optional().trim().isLength({ min: 2, max: 100 }),
  body('brand').optional().trim().isLength({ min: 2, max: 100 }),
  body('imageUrl').optional().isURL(),
  body('weight').optional().isFloat({ min: 0 }),
  body('registeredDate').optional().isDate({ format: 'YYYY-MM-DD' }),
];
const idParamValidator = [param('id').isInt({ min: 1 })];
module.exports = { createProductValidators, updateProductValidators, idParamValidator };
