// src/controllers/dataController.js
const WeatherData = require('../models/WeatherData');
const User = require('../models/User');

// ============================================================
// CAMBIA ESTO: Importa tu modelo de dominio en lugar de WeatherData.
// Ajusta los campos en createData y updateData según tu modelo.
// El resto de la estructura (getAll, getById, delete) es genérica.
// ============================================================

/** GET /data - Obtener todos los registros (público) */
const getAllData = async (req, res) => {
  try {
    const records = await WeatherData.findAll({
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

/** GET /data/:id - Obtener registro por ID (público) */
const getDataById = async (req, res) => {
  try {
    const record = await WeatherData.findByPk(req.params.id, {
      include: [{
        model: User,
        as: 'uploader',
        attributes: ['id', 'username', 'fullName'],
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

/** POST /data - Crear nuevo registro (solo admins) */
const createData = async (req, res) => {
  try {
    // ============================================================
    // CAMBIA ESTO: Desestructura los campos de TU modelo aquí
    // ============================================================
    const {
      recordDate,
      latitude,
      longitude,
      rainProbability,
      precipitation,
      windSpeed,
      tempMin,
      tempMax,
      tempCurrent,
    } = req.body;

    // El userId viene del token JWT (req.user.id)
    const newRecord = await WeatherData.create({
      recordDate: recordDate || new Date(),
      latitude,
      longitude,
      rainProbability,
      precipitation: precipitation || 0,
      windSpeed: windSpeed || 0,
      tempMin,
      tempMax,
      tempCurrent,
      userId: req.user.id,   // Usuario autenticado como autor
    });

    return res.status(201).json({
      success: true,
      message: 'Registro creado correctamente',
      data: newRecord,
    });
  } catch (error) {
    console.error('Error al crear registro:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** PUT /data/:id - Actualizar registro (solo admins) */
const updateData = async (req, res) => {
  try {
    const record = await WeatherData.findByPk(req.params.id);
    if (!record) {
      return res.status(404).json({ success: false, message: 'Registro no encontrado' });
    }

    // ============================================================
    // CAMBIA ESTO: Ajusta los campos de actualización a tu modelo
    // ============================================================
    const updateFields = [
      'recordDate', 'latitude', 'longitude', 'rainProbability',
      'precipitation', 'windSpeed', 'tempMin', 'tempMax', 'tempCurrent',
    ];

    const updateData = {};
    updateFields.forEach(field => {
      if (req.body[field] !== undefined) updateData[field] = req.body[field];
    });

    await record.update(updateData);

    return res.status(200).json({
      success: true,
      message: 'Registro actualizado correctamente',
      data: record,
    });
  } catch (error) {
    console.error('Error al actualizar registro:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

/** DELETE /data/:id - Eliminar registro (solo admins) */
const deleteData = async (req, res) => {
  try {
    const record = await WeatherData.findByPk(req.params.id);
    if (!record) {
      return res.status(404).json({ success: false, message: 'Registro no encontrado' });
    }

    await record.destroy();
    return res.status(200).json({ success: true, message: 'Registro eliminado correctamente' });
  } catch (error) {
    console.error('Error al eliminar registro:', error);
    return res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
};

module.exports = { getAllData, getDataById, createData, updateData, deleteData };
