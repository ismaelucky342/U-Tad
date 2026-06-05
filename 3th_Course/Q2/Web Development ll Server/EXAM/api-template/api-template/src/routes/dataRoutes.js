// src/routes/dataRoutes.js
const express = require('express');
const router = express.Router();
const { verifyToken, isAdmin } = require('../middleware/auth');
const handleValidation = require('../middleware/handleValidation');
const { validateCreateData, validateUpdateData } = require('../validators/dataValidators');
const {
  getAllData, getDataById, createData, updateData, deleteData,
} = require('../controllers/dataController');

// ============================================================
// CAMBIA POCO: Ajusta los validators y el nombre de la sección Swagger.
// La estructura de permisos (público vs admin) no cambia.
// ============================================================

/**
 * @swagger
 * tags:
 *   name: WeatherData
 *   description: Gestión de registros meteorológicos
 */

/**
 * @swagger
 * /data:
 *   get:
 *     summary: Obtener todos los registros meteorológicos (público)
 *     tags: [WeatherData]
 *     security: []
 *     responses:
 *       200:
 *         description: Lista de registros
 */
router.get('/', getAllData);

/**
 * @swagger
 * /data/{id}:
 *   get:
 *     summary: Obtener registro por ID (público)
 *     tags: [WeatherData]
 *     security: []
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Registro encontrado
 *       404:
 *         description: Registro no encontrado
 */
router.get('/:id', getDataById);

/**
 * @swagger
 * /data:
 *   post:
 *     summary: Crear nuevo registro meteorológico (solo admins)
 *     tags: [WeatherData]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required: [latitude, longitude, rainProbability, tempMin, tempMax, tempCurrent]
 *             properties:
 *               recordDate:
 *                 type: string
 *                 format: date-time
 *               latitude:
 *                 type: number
 *                 example: 40.4168
 *               longitude:
 *                 type: number
 *                 example: -3.7038
 *               rainProbability:
 *                 type: number
 *                 example: 75
 *               precipitation:
 *                 type: number
 *                 example: 12.5
 *               windSpeed:
 *                 type: number
 *                 example: 30
 *               tempMin:
 *                 type: number
 *                 example: 10
 *               tempMax:
 *                 type: number
 *                 example: 22
 *               tempCurrent:
 *                 type: number
 *                 example: 16
 *     responses:
 *       201:
 *         description: Registro creado
 *       400:
 *         description: Error de validación
 *       401:
 *         description: No autorizado
 */
router.post('/', verifyToken, isAdmin, validateCreateData, handleValidation, createData);

/**
 * @swagger
 * /data/{id}:
 *   put:
 *     summary: Actualizar registro meteorológico (solo admins)
 *     tags: [WeatherData]
 *     security:
 *       - bearerAuth: []
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     requestBody:
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               rainProbability:
 *                 type: number
 *               tempCurrent:
 *                 type: number
 *     responses:
 *       200:
 *         description: Registro actualizado
 *       404:
 *         description: Registro no encontrado
 */
router.put('/:id', verifyToken, isAdmin, validateUpdateData, handleValidation, updateData);

/**
 * @swagger
 * /data/{id}:
 *   delete:
 *     summary: Eliminar registro meteorológico (solo admins)
 *     tags: [WeatherData]
 *     security:
 *       - bearerAuth: []
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Registro eliminado
 *       404:
 *         description: Registro no encontrado
 */
router.delete('/:id', verifyToken, isAdmin, deleteData);

module.exports = router;
