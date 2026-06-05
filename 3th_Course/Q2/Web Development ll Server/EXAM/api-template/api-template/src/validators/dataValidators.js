// src/validators/dataValidators.js
const { body } = require('express-validator');

// ============================================================
// CAMBIA ESTO: Este archivo es el que MÁS cambiarás entre enunciados.
// Sustituye todos estos campos por los campos de tu modelo de dominio.
// ============================================================

/** Validaciones para crear un nuevo registro meteorológico */
const validateCreateData = [
  body('recordDate')
    .optional()
    .isISO8601().withMessage('La fecha debe tener formato ISO 8601 (ej: 2024-01-15T10:00:00Z)'),

  body('latitude')
    .notEmpty().withMessage('La latitud es obligatoria')
    .isFloat({ min: -90, max: 90 }).withMessage('La latitud debe estar entre -90 y 90'),

  body('longitude')
    .notEmpty().withMessage('La longitud es obligatoria')
    .isFloat({ min: -180, max: 180 }).withMessage('La longitud debe estar entre -180 y 180'),

  body('rainProbability')
    .notEmpty().withMessage('La probabilidad de lluvia es obligatoria')
    .isFloat({ min: 0, max: 100 }).withMessage('La probabilidad debe estar entre 0 y 100'),

  body('precipitation')
    .optional()
    .isFloat({ min: 0 }).withMessage('La precipitación no puede ser negativa'),

  body('windSpeed')
    .optional()
    .isFloat({ min: 0 }).withMessage('La velocidad del viento no puede ser negativa'),

  body('tempMin')
    .notEmpty().withMessage('La temperatura mínima es obligatoria')
    .isFloat().withMessage('La temperatura mínima debe ser un número'),

  body('tempMax')
    .notEmpty().withMessage('La temperatura máxima es obligatoria')
    .isFloat().withMessage('La temperatura máxima debe ser un número'),

  body('tempCurrent')
    .notEmpty().withMessage('La temperatura actual es obligatoria')
    .isFloat().withMessage('La temperatura actual debe ser un número'),
];

/** Validaciones para actualizar un registro (todos opcionales) */
const validateUpdateData = [
  body('recordDate')
    .optional()
    .isISO8601().withMessage('La fecha debe tener formato ISO 8601'),

  body('latitude')
    .optional()
    .isFloat({ min: -90, max: 90 }).withMessage('La latitud debe estar entre -90 y 90'),

  body('longitude')
    .optional()
    .isFloat({ min: -180, max: 180 }).withMessage('La longitud debe estar entre -180 y 180'),

  body('rainProbability')
    .optional()
    .isFloat({ min: 0, max: 100 }).withMessage('La probabilidad debe estar entre 0 y 100'),

  body('precipitation')
    .optional()
    .isFloat({ min: 0 }).withMessage('La precipitación no puede ser negativa'),

  body('windSpeed')
    .optional()
    .isFloat({ min: 0 }).withMessage('La velocidad del viento no puede ser negativa'),

  body('tempMin').optional().isFloat().withMessage('Debe ser un número'),
  body('tempMax').optional().isFloat().withMessage('Debe ser un número'),
  body('tempCurrent').optional().isFloat().withMessage('Debe ser un número'),
];

module.exports = { validateCreateData, validateUpdateData };
