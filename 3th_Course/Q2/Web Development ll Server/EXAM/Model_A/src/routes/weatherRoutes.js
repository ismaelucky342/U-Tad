const express = require('express');
const router = express.Router();

const { verifyToken, verifyAdmin } = require('../middleware/auth');
const { handleValidationErrors } = require('../middleware/validationHandler');
const {
  getAllData,
  getDataById,
  createData,
  updateData,
  deleteData,
} = require('../controllers/weatherController');
const {
  createWeatherValidators,
  updateWeatherValidators,
  idParamValidator,
} = require('../validators/weatherValidators');

/**
 * @swagger
 * tags:
 *   name: WeatherData
 *   description: Gestión de datos meteorológicos
 */

/**
 * @swagger
 * /data:
 *   get:
 *     summary: Obtener todos los registros meteorológicos
 *     tags: [WeatherData]
 *     responses:
 *       200:
 *         description: Lista de registros meteorológicos.
 */
router.get('/', getAllData);

/**
 * @swagger
 * /data/{id}:
 *   get:
 *     summary: Obtener registro meteorológico por ID
 *     tags: [WeatherData]
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *         description: ID del registro
 *     responses:
 *       200:
 *         description: Datos del registro meteorológico.
 *       404:
 *         description: Registro no encontrado.
 */
router.get('/:id', idParamValidator, handleValidationErrors, getDataById);

/**
 * @swagger
 * /data:
 *   post:
 *     summary: Crear nuevo registro meteorológico
 *     tags: [WeatherData]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required:
 *               - date
 *               - latitude
 *               - longitude
 *               - rainProbability
 *               - precipitation
 *               - windSpeed
 *               - tempMin
 *               - tempMax
 *               - tempCurrent
 *             properties:
 *               date:
 *                 type: string
 *                 format: date
 *                 example: "2024-03-15"
 *               latitude:
 *                 type: number
 *                 example: 40.4168
 *               longitude:
 *                 type: number
 *                 example: -3.7038
 *               rainProbability:
 *                 type: number
 *                 example: 75.5
 *               precipitation:
 *                 type: number
 *                 example: 12.3
 *               windSpeed:
 *                 type: number
 *                 example: 45.2
 *               tempMin:
 *                 type: number
 *                 example: 8.5
 *               tempMax:
 *                 type: number
 *                 example: 18.2
 *               tempCurrent:
 *                 type: number
 *                 example: 13.4
 *     responses:
 *       201:
 *         description: Registro creado correctamente.
 *       400:
 *         description: Datos de entrada inválidos.
 *       401:
 *         description: Token no proporcionado o inválido.
 *       403:
 *         description: Se requieren permisos de administrador.
 */
router.post('/', verifyToken, verifyAdmin, createWeatherValidators, handleValidationErrors, createData);

/**
 * @swagger
 * /data/{id}:
 *   put:
 *     summary: Actualizar registro meteorológico
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
 *               date:
 *                 type: string
 *                 format: date
 *               latitude:
 *                 type: number
 *               longitude:
 *                 type: number
 *               rainProbability:
 *                 type: number
 *               precipitation:
 *                 type: number
 *               windSpeed:
 *                 type: number
 *               tempMin:
 *                 type: number
 *               tempMax:
 *                 type: number
 *               tempCurrent:
 *                 type: number
 *     responses:
 *       200:
 *         description: Registro actualizado correctamente.
 *       400:
 *         description: Datos inválidos.
 *       401:
 *         description: Token inválido.
 *       403:
 *         description: Sin permisos de administrador.
 *       404:
 *         description: Registro no encontrado.
 */
router.put('/:id', verifyToken, verifyAdmin, updateWeatherValidators, handleValidationErrors, updateData);

/**
 * @swagger
 * /data/{id}:
 *   delete:
 *     summary: Eliminar registro meteorológico
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
 *         description: Registro eliminado correctamente.
 *       401:
 *         description: Token inválido.
 *       403:
 *         description: Sin permisos de administrador.
 *       404:
 *         description: Registro no encontrado.
 */
router.delete('/:id', verifyToken, verifyAdmin, idParamValidator, handleValidationErrors, deleteData);

module.exports = router;
