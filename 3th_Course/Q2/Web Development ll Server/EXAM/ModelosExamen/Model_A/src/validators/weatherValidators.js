const { body, param } = require('express-validator');

const createWeatherValidators = [
  body('date')
    .notEmpty().withMessage('La fecha es obligatoria.')
    .isDate({ format: 'YYYY-MM-DD' }).withMessage('La fecha debe tener el formato YYYY-MM-DD.'),
  body('latitude')
    .notEmpty().withMessage('La latitud es obligatoria.')
    .isFloat({ min: -90, max: 90 }).withMessage('La latitud debe estar entre -90 y 90.'),
  body('longitude')
    .notEmpty().withMessage('La longitud es obligatoria.')
    .isFloat({ min: -180, max: 180 }).withMessage('La longitud debe estar entre -180 y 180.'),
  body('rainProbability')
    .notEmpty().withMessage('La probabilidad de lluvia es obligatoria.')
    .isFloat({ min: 0, max: 100 }).withMessage('La probabilidad de lluvia debe estar entre 0 y 100.'),
  body('precipitation')
    .notEmpty().withMessage('La precipitación es obligatoria.')
    .isFloat({ min: 0 }).withMessage('La precipitación no puede ser negativa.'),
  body('windSpeed')
    .notEmpty().withMessage('La velocidad del viento es obligatoria.')
    .isFloat({ min: 0 }).withMessage('La velocidad del viento no puede ser negativa.'),
  body('tempMin')
    .notEmpty().withMessage('La temperatura mínima es obligatoria.')
    .isFloat().withMessage('La temperatura mínima debe ser un número.'),
  body('tempMax')
    .notEmpty().withMessage('La temperatura máxima es obligatoria.')
    .isFloat().withMessage('La temperatura máxima debe ser un número.')
    .custom((value, { req }) => {
      if (parseFloat(value) < parseFloat(req.body.tempMin)) {
        throw new Error('La temperatura máxima no puede ser menor que la mínima.');
      }
      return true;
    }),
  body('tempCurrent')
    .notEmpty().withMessage('La temperatura actual es obligatoria.')
    .isFloat().withMessage('La temperatura actual debe ser un número.'),
];

const updateWeatherValidators = [
  param('id')
    .isInt({ min: 1 }).withMessage('El ID debe ser un número entero positivo.'),
  body('date')
    .optional()
    .isDate({ format: 'YYYY-MM-DD' }).withMessage('La fecha debe tener el formato YYYY-MM-DD.'),
  body('latitude')
    .optional()
    .isFloat({ min: -90, max: 90 }).withMessage('La latitud debe estar entre -90 y 90.'),
  body('longitude')
    .optional()
    .isFloat({ min: -180, max: 180 }).withMessage('La longitud debe estar entre -180 y 180.'),
  body('rainProbability')
    .optional()
    .isFloat({ min: 0, max: 100 }).withMessage('La probabilidad de lluvia debe estar entre 0 y 100.'),
  body('precipitation')
    .optional()
    .isFloat({ min: 0 }).withMessage('La precipitación no puede ser negativa.'),
  body('windSpeed')
    .optional()
    .isFloat({ min: 0 }).withMessage('La velocidad del viento no puede ser negativa.'),
  body('tempMin')
    .optional()
    .isFloat().withMessage('La temperatura mínima debe ser un número.'),
  body('tempMax')
    .optional()
    .isFloat().withMessage('La temperatura máxima debe ser un número.'),
  body('tempCurrent')
    .optional()
    .isFloat().withMessage('La temperatura actual debe ser un número.'),
];

const idParamValidator = [
  param('id')
    .isInt({ min: 1 }).withMessage('El ID debe ser un número entero positivo.'),
];

module.exports = {
  createWeatherValidators,
  updateWeatherValidators,
  idParamValidator,
};
