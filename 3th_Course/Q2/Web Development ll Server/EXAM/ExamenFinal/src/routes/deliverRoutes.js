/*====================================================================================================*/
/*                                                                                                    */
/*                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      Examen Final - PW2S                               ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                                        ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        05/06/2026  -  17:30:13           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    05/06/2026  -  18:40:00           ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                                    */
/*      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             */
/*                                                                                                    */
/*      Github:                                           https://github.com/ismaelucky342            */
/*                                                                                                    */
/*====================================================================================================*/

// src/routes/deliverRoutes.js
const express = require('express');
const router = express.Router();
const { verifyToken, isAdmin } = require('../middleware/auth');
const handleValidation = require('../middleware/handleValidation');
const { validatecreateDelivery, validateupdateDelivery } = require('../validators/deliveryValidator');
const {
  getAllDelivery, getDeliveryById, createDelivery, updateDelivery, deleteData,
} = require('../controllers/deliverController');

/**
 * @swagger
 * tags:
 *   name: Delivery
 *   description: Gestión de Delivery
 */

/**
 * @swagger
 * /data:
 *   get:
 *     summary: Obtener todos los Pedido del delivery (público)
 *     tags: [Delivery]
 *     security: []
 *     responses:
 *       200:
 *         description: Lista de Pedido
 */
router.get('/', getAllDelivery);

/**
 * @swagger
 * /data/{id}:
 *   get:
 *     summary: Obtener Pedido por ID (público)
 *     tags: [Delivery]
 *     security: []
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Pedido encontrado
 *       404:
 *         description: Pedido no encontrado
 */
router.get('/:id', getDeliveryById);

/**
 * @swagger
 * /data:
 *   post:
 *     summary: Crear nuevo delivery(solo admins)
 *     tags: [Delivery]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required: [DeliveryDate, delivery_name, shipment_name, id_paquete]
 *             properties:
 *               DeliveryDate:
 *                 type: string
 *                 format: date-time
 *               delivery_name:
 *                 type: string
 *                 example: Manolo
 *               shipment_name:
 *                 type: string
 *                 example: Amazon
 *               id_paquete:
 *                 type: integer
 *                 example: 98784567
 *     responses:
 *       201:
 *         description: Pedido creado
 *       400:
 *         description: Error de validación
 *       401:
 *         description: No autorizado
 */
router.post('/', verifyToken, isAdmin, validatecreateDelivery, handleValidation, createDelivery);

/**
 * @swagger
 * /data/{id}:
 *   put:
 *     summary: Actualizar registro Pedidos (solo admins)
 *     tags: [Delivery]
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
 *         description: Pedido actualizado
 *       404:
 *         description: Pedido no encontrado
 */
router.put('/:id', verifyToken, isAdmin, validateupdateDelivery, handleValidation, updateDelivery);

/**
 * @swagger
 * /data/{id}:
 *   delete:
 *     summary: Eliminar Pedido (solo admins)
 *     tags: [Delivery]
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
 *         description: Pedido eliminado
 *       404:
 *         description: Pedido no encontrado
 */
router.delete('/:id', verifyToken, isAdmin, deleteData);

module.exports = router;
