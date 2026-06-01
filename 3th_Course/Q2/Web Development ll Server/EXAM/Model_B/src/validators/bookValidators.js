const { body, param } = require('express-validator');

const createBookValidators = [
  body('title')
    .trim()
    .notEmpty().withMessage('El título es obligatorio.')
    .isLength({ min: 3, max: 200 }).withMessage('El título debe tener entre 3 y 200 caracteres.'),
  body('author')
    .trim()
    .notEmpty().withMessage('El autor es obligatorio.')
    .isLength({ min: 2, max: 150 }).withMessage('El autor debe tener entre 2 y 150 caracteres.'),
  body('isbn')
    .trim()
    .notEmpty().withMessage('El ISBN es obligatorio.')
    .isLength({ min: 10, max: 20 }).withMessage('El ISBN debe tener entre 10 y 20 caracteres.'),
  body('genre')
    .trim()
    .notEmpty().withMessage('El género es obligatorio.')
    .isLength({ min: 2, max: 100 }).withMessage('El género debe tener entre 2 y 100 caracteres.'),
  body('publicationYear')
    .notEmpty().withMessage('El año de publicación es obligatorio.')
    .isInt({ min: 1000, max: new Date().getFullYear() })
    .withMessage(`El año de publicación debe estar entre 1000 y ${new Date().getFullYear()}.`),
  body('pages')
    .notEmpty().withMessage('El número de páginas es obligatorio.')
    .isInt({ min: 1 }).withMessage('El número de páginas debe ser al menos 1.'),
  body('available')
    .optional()
    .isBoolean().withMessage('El campo disponible debe ser un booleano.'),
  body('synopsis')
    .optional()
    .isString().withMessage('La sinopsis debe ser un texto.'),
];

const updateBookValidators = [
  param('id')
    .isInt({ min: 1 }).withMessage('El ID debe ser un número entero positivo.'),
  body('title')
    .optional()
    .trim()
    .isLength({ min: 3, max: 200 }).withMessage('El título debe tener entre 3 y 200 caracteres.'),
  body('author')
    .optional()
    .trim()
    .isLength({ min: 2, max: 150 }).withMessage('El autor debe tener entre 2 y 150 caracteres.'),
  body('isbn')
    .optional()
    .trim()
    .isLength({ min: 10, max: 20 }).withMessage('El ISBN debe tener entre 10 y 20 caracteres.'),
  body('genre')
    .optional()
    .trim()
    .isLength({ min: 2, max: 100 }).withMessage('El género debe tener entre 2 y 100 caracteres.'),
  body('publicationYear')
    .optional()
    .isInt({ min: 1000, max: new Date().getFullYear() })
    .withMessage(`El año de publicación debe estar entre 1000 y ${new Date().getFullYear()}.`),
  body('pages')
    .optional()
    .isInt({ min: 1 }).withMessage('El número de páginas debe ser al menos 1.'),
  body('available')
    .optional()
    .isBoolean().withMessage('El campo disponible debe ser un booleano.'),
  body('synopsis')
    .optional()
    .isString().withMessage('La sinopsis debe ser un texto.'),
];

const idParamValidator = [
  param('id')
    .isInt({ min: 1 }).withMessage('El ID debe ser un número entero positivo.'),
];

module.exports = {
  createBookValidators,
  updateBookValidators,
  idParamValidator,
};
