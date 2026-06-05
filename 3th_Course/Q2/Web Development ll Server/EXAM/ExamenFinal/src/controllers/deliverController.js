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

// src/controllers/deliveryController.js
const Delivery = require('../models/Delivery');
const User = require('../models/User');

/** GET /data - Obtener todos los pedidos (público) */
const getAllDelivery = async (req, res) => {
  try {
    const records = await Delivery.findAll({
      include: [{
        model: User,
        as: 'uploader',
        attributes: ['id', 'username', 'fullName'],   // Solo datos públicos del usuario
      }],
      order: [['recordDate', 'DESC']],
    });

    return res.status(200).json({ success: true, count: records.length, data: records });
  } catch (error) {
    console.error('Error al obtener datos:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** GET /data/:id - Obtener pedidos por ID (público) */
const getDeliveryById = async (req, res) => {
  try {
    const record = await Delivery.findByPk(req.params.id, {
      include: [{
        model: User,
        as: 'uploader',
        attributes: ['id', 'username'],
      }],
    });

    if (!record) {
      return res.status(404).json({ success: false, message: 'Registro no encontrado' });
    }

    return res.status(200).json({ success: true, data: record });
  } catch (error) {
    console.error('Error al obtener registro:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** POST /data - Crear nuevo pedido (solo admins) */
const createDelivery = async (req, res) => {
  try {
    const {
      id_paquete,
      shipment_name,
      delivery_name,
      DeliveryDate,
    } = req.body;

    // El userId viene del token JWT
    const newRecord = await Delivery.create({
      DeliveryDate: DeliveryDate || new Date(),
      id_paquete,
      shipment_name,
      delivery_name,
      DeliveryDate,
      userId: req.user.id,
    });

    return res.status(201).json({
      success: true,
      message: 'Pedido creado correctamente',
      data: newRecord,
    });
  } catch (error) {
    console.error('Error al crear Pedido:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** PUT /data/:id - Actualizar Pedidos (solo admins) */
const updateDelivery = async (req, res) => {
  try {
    const record = await Delivery.findByPk(req.params.id);
    if (!record) {
      return res.status(404).json({ success: false, message: 'Pedido no encontrado' });
    }
    const updateFields = [
      'id_paquete', 'shipment_name', 'delivery_name', 'DeliveryDate',
    ];

    const updateDelivery = {};
    updateFields.forEach(field => {
      if (req.body[field] !== undefined) updateDelivery[field] = req.body[field];
    });

    await record.update(updateDelivery);

    return res.status(200).json({
      success: true,
      message: 'Pedido actualizado correctamente',
      data: record,
    });
  } catch (error) {
    console.error('Error al actualizar pedido:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** DELETE /data/:id - Eliminar pedido (solo admins) */
const deleteData = async (req, res) => {
  try {
    const record = await Delivery.findByPk(req.params.id);
    if (!record) {
      return res.status(404).json({ success: false, message: 'Pedido no encontrado' });
    }

    await record.destroy();
    return res.status(200).json({ success: true, message: 'Pedido eliminado correctamente' });
  } catch (error) {
    console.error('Error al eliminar Pedido:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

module.exports = { getAllDelivery, getDeliveryById, createDelivery, updateDelivery, deleteData };
