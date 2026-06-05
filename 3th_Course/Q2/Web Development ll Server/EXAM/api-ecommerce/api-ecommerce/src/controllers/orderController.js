// src/controllers/orderController.js
const Order = require('../models/Order');
const User = require('../models/User');

// ── Helper: calcula el total de un array de items ────────────
const calcTotal = (items) =>
  items.reduce((sum, item) => sum + item.quantity * item.unitPrice, 0);

/** GET /orders
 *  - Admin: devuelve TODOS los pedidos
 *  - Client: devuelve SOLO sus propios pedidos
 */
const getAllOrders = async (req, res) => {
  try {
    const whereClause = req.user.role === 'admin' ? {} : { userId: req.user.id };

    const orders = await Order.findAll({
      where: whereClause,
      include: [{
        model: User,
        as: 'client',
        attributes: ['id', 'username', 'fullName', 'email'],
      }],
      order: [['orderDate', 'DESC']],
    });

    return res.status(200).json({ success: true, count: orders.length, data: orders });
  } catch (error) {
    console.error('Error al obtener pedidos:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** GET /orders/:id
 *  - Admin: puede ver cualquier pedido
 *  - Client: solo puede ver sus propios pedidos
 */
const getOrderById = async (req, res) => {
  try {
    const order = await Order.findByPk(req.params.id, {
      include: [{
        model: User,
        as: 'client',
        attributes: ['id', 'username', 'fullName', 'email'],
      }],
    });

    if (!order) {
      return res.status(404).json({ success: false, message: 'Pedido no encontrado' });
    }

    // Un cliente solo puede ver sus propios pedidos
    if (req.user.role !== 'admin' && order.userId !== req.user.id) {
      return res.status(403).json({ success: false, message: 'No tienes permiso para ver este pedido' });
    }

    return res.status(200).json({ success: true, data: order });
  } catch (error) {
    console.error('Error al obtener pedido:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** POST /orders
 *  - Admin y Client autenticados pueden crear pedidos
 *  - El userId siempre se toma del token (el cliente no puede crear pedidos para otros)
 *  - Admin puede especificar un userId diferente en el body
 */
const createOrder = async (req, res) => {
  try {
    const { items, shippingAddress, notes } = req.body;

    // Admin puede crear pedidos en nombre de otro usuario; cliente solo en el suyo
    const targetUserId = (req.user.role === 'admin' && req.body.userId)
      ? req.body.userId
      : req.user.id;

    // Verificar que el usuario destinatario existe
    const targetUser = await User.findByPk(targetUserId);
    if (!targetUser) {
      return res.status(404).json({ success: false, message: 'Usuario destino no encontrado' });
    }

    const totalAmount = calcTotal(items);

    const newOrder = await Order.create({
      userId: targetUserId,
      items,
      totalAmount,
      shippingAddress,
      notes,
      status: 'pending',
    });

    return res.status(201).json({
      success: true,
      message: 'Pedido creado correctamente',
      data: newOrder,
    });
  } catch (error) {
    console.error('Error al crear pedido:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** PUT /orders/:id
 *  - Admin: puede cambiar cualquier campo, incluido el status
 *  - Client: solo puede cancelar su propio pedido si está en 'pending'
 */
const updateOrder = async (req, res) => {
  try {
    const order = await Order.findByPk(req.params.id);
    if (!order) {
      return res.status(404).json({ success: false, message: 'Pedido no encontrado' });
    }

    // Permisos para clientes
    if (req.user.role !== 'admin') {
      if (order.userId !== req.user.id) {
        return res.status(403).json({ success: false, message: 'No tienes permiso para modificar este pedido' });
      }
      // Cliente solo puede cancelar si está pendiente
      if (req.body.status && req.body.status !== 'cancelled') {
        return res.status(403).json({ success: false, message: 'Solo puedes cancelar tu pedido' });
      }
      if (order.status !== 'pending') {
        return res.status(400).json({ success: false, message: 'Solo puedes cancelar pedidos en estado pendiente' });
      }
    }

    const { status, shippingAddress, notes, items } = req.body;
    const updateData = {};

    if (status !== undefined) updateData.status = status;
    if (shippingAddress !== undefined) updateData.shippingAddress = shippingAddress;
    if (notes !== undefined) updateData.notes = notes;

    // Admin puede modificar items y recalcular total
    if (req.user.role === 'admin' && items !== undefined) {
      updateData.items = items;
      updateData.totalAmount = calcTotal(items);
    }

    await order.update(updateData);
    return res.status(200).json({
      success: true,
      message: 'Pedido actualizado correctamente',
      data: order,
    });
  } catch (error) {
    console.error('Error al actualizar pedido:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** DELETE /orders/:id — Solo admin */
const deleteOrder = async (req, res) => {
  try {
    const order = await Order.findByPk(req.params.id);
    if (!order) {
      return res.status(404).json({ success: false, message: 'Pedido no encontrado' });
    }

    await order.destroy();
    return res.status(200).json({ success: true, message: 'Pedido eliminado correctamente' });
  } catch (error) {
    console.error('Error al eliminar pedido:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

module.exports = { getAllOrders, getOrderById, createOrder, updateOrder, deleteOrder };
