const { body, param } = require('express-validator');

const createEventValidators = [
  body('name')
    .trim()
    .notEmpty().withMessage('El nombre del evento es obligatorio.')
    .isLength({ min: 3, max: 200 }).withMessage('El nombre debe tener entre 3 y 200 caracteres.'),
  body('eventDate')
    .notEmpty().withMessage('La fecha del evento es obligatoria.')
    .isISO8601().withMessage('La fecha debe ser válida (ISO 8601).'),
  body('city')
    .trim()
    .notEmpty().withMessage('La ciudad es obligatoria.')
    .isLength({ min: 2, max: 100 }).withMessage('La ciudad debe tener entre 2 y 100 caracteres.'),
  body('address')
    .trim()
    .notEmpty().withMessage('La dirección es obligatoria.')
    .isLength({ min: 5, max: 250 }).withMessage('La dirección debe tener entre 5 y 250 caracteres.'),
  body('maxCapacity')
    .notEmpty().withMessage('El aforo máximo es obligatorio.')
    .isInt({ min: 1 }).withMessage('El aforo máximo debe ser al menos 1.'),
  body('availableSpots')
    .notEmpty().withMessage('Las plazas disponibles son obligatorias.')
    .isInt({ min: 0 }).withMessage('Las plazas disponibles no pueden ser negativas.'),
  body('ticketPrice')
    .notEmpty().withMessage('El precio de entrada es obligatorio.')
    .isFloat({ min: 0 }).withMessage('El precio no puede ser negativo.'),
  body('category')
    .notEmpty().withMessage('La categoría es obligatoria.')
    .isIn(['concierto', 'teatro', 'deporte', 'otro']).withMessage('Categoría no válida.'),
  body('description')
    .optional()
    .isString().withMessage('La descripción debe ser un texto.'),
];

const updateEventValidators = [
  param('id')
    .isInt({ min: 1 }).withMessage('El ID debe ser un número entero positivo.'),
  body('name')
    .optional()
    .trim()
    .isLength({ min: 3, max: 200 }).withMessage('El nombre debe tener entre 3 y 200 caracteres.'),
  body('eventDate')
    .optional()
    .isISO8601().withMessage('La fecha debe ser válida (ISO 8601).'),
  body('city')
    .optional()
    .trim()
    .isLength({ min: 2, max: 100 }).withMessage('La ciudad debe tener entre 2 y 100 caracteres.'),
  body('address')
    .optional()
    .trim()
    .isLength({ min: 5, max: 250 }).withMessage('La dirección debe tener entre 5 y 250 caracteres.'),
  body('maxCapacity')
    .optional()
    .isInt({ min: 1 }).withMessage('El aforo máximo debe ser al menos 1.'),
  body('availableSpots')
    .optional()
    .isInt({ min: 0 }).withMessage('Las plazas disponibles no pueden ser negativas.'),
  body('ticketPrice')
    .optional()
    .isFloat({ min: 0 }).withMessage('El precio no puede ser negativo.'),
  body('category')
    .optional()
    .isIn(['concierto', 'teatro', 'deporte', 'otro']).withMessage('Categoría no válida.'),
  body('description')
    .optional()
    .isString().withMessage('La descripción debe ser un texto.'),
];

const idParamValidator = [
  param('id')
    .isInt({ min: 1 }).withMessage('El ID debe ser un número entero positivo.'),
];

module.exports = {
  createEventValidators,
  updateEventValidators,
  idParamValidator,
};
