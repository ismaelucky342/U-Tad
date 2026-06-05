// src/routes/orderRoutes.js
const express = require('express');
const router = express.Router();
const { verifyToken, isAdmin, isAuthenticated } = require('../middleware/auth');
const handleValidation = require('../middleware/handleValidation');
const { validateCreateOrder, validateUpdateOrder } = require('../validators/orderValidators');
const {
  getAllOrders, getOrderById, createOrder, updateOrder, deleteOrder,
} = require('../controllers/orderController');

/**
 * @swagger
 * tags:
 *   name: Orders
 *   description: Gestión de pedidos
 */

/**
 * @swagger
 * /orders:
 *   get:
 *     summary: >
 *       Listar pedidos.
 *       Admin obtiene todos; cliente obtiene solo los suyos.
 *     tags: [Orders]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Lista de pedidos
 *       401:
 *         description: No autenticado
 */
router.get('/', verifyToken, isAuthenticated, getAllOrders);

/**
 * @swagger
 * /orders/{id}:
 *   get:
 *     summary: Ver pedido por ID (admin cualquiera; cliente solo el suyo)
 *     tags: [Orders]
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
 *         description: Pedido encontrado
 *       403:
 *         description: No autorizado para ver este pedido
 *       404:
 *         description: Pedido no encontrado
 */
router.get('/:id', verifyToken, isAuthenticated, getOrderById);

/**
 * @swagger
 * /orders:
 *   post:
 *     summary: Crear pedido (admin y cliente autenticado)
 *     tags: [Orders]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required: [items, shippingAddress]
 *             properties:
 *               items:
 *                 type: array
 *                 items:
 *                   type: object
 *                   required: [productName, quantity, unitPrice]
 *                   properties:
 *                     productName:
 *                       type: string
 *                       example: Camiseta básica
 *                     quantity:
 *                       type: integer
 *                       example: 2
 *                     unitPrice:
 *                       type: number
 *                       example: 19.99
 *               shippingAddress:
 *                 type: string
 *                 example: Calle Mayor 1, Madrid
 *               notes:
 *                 type: string
 *               userId:
 *                 type: integer
 *                 description: Solo para admins, para crear pedidos en nombre de otro usuario
 *     responses:
 *       201:
 *         description: Pedido creado
 *       400:
 *         description: Error de validación
 */
router.post('/', verifyToken, isAuthenticated, validateCreateOrder, handleValidation, createOrder);

/**
 * @swagger
 * /orders/{id}:
 *   put:
 *     summary: >
 *       Actualizar pedido.
 *       Admin puede cambiar cualquier campo.
 *       Cliente solo puede cancelar su pedido si está en estado 'pending'.
 *     tags: [Orders]
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
 *               status:
 *                 type: string
 *                 enum: [pending, confirmed, shipped, delivered, cancelled]
 *               shippingAddress:
 *                 type: string
 *               notes:
 *                 type: string
 *     responses:
 *       200:
 *         description: Pedido actualizado
 *       403:
 *         description: Sin permiso para esta operación
 */
router.put('/:id', verifyToken, isAuthenticated, validateUpdateOrder, handleValidation, updateOrder);

/**
 * @swagger
 * /orders/{id}:
 *   delete:
 *     summary: Eliminar pedido definitivamente (solo admin)
 *     tags: [Orders]
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
 */
router.delete('/:id', verifyToken, isAdmin, deleteOrder);

module.exports = router;
