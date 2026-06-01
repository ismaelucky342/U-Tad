const { body, param } = require('express-validator');
const loginValidators = [body('email').isEmail(), body('password').notEmpty()];
const createUserValidators = [body('username').trim().notEmpty().isLength({ min: 3, max: 50 }).matches(/^[a-zA-Z0-9_]+$/), body('email').isEmail(), body('fullName').trim().notEmpty().isLength({ min: 2, max: 100 }), body('password').isLength({ min: 6 }), body('isAdmin').optional().isBoolean()];
const updateUserValidators = [param('id').isInt({ min: 1 }), body('username').optional().trim(), body('email').optional().isEmail(), body('fullName').optional().trim(), body('password').optional().isLength({ min: 6 }), body('isAdmin').optional().isBoolean()];
const idParamValidator = [param('id').isInt({ min: 1 })];
module.exports = { loginValidators, createUserValidators, updateUserValidators, idParamValidator };
