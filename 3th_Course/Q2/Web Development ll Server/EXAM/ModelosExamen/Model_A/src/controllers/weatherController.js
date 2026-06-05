const Pedidos = require('../models/Pedidos');
const User = require('../models/User');

// GET /data — Obtener todos los registros meteorológicos (público)
const getAllData = async (req, res) => {
  try {
    const records = await Pedidos.findAll({
      include: [{
        model: User,
        as: 'uploader',
        attributes: ['id', 'username', 'fullName'],
      }],
      order: [['date', 'DESC']],
    });
    return res.status(200).json(records);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

// GET /data/:id — Obtener registro meteorológico por ID (público)
const getDataById = async (req, res) => {
  const { id } = req.params;
  try {
    const record = await Pedidos.findByPk(id, {
      include: [{
        model: User,
        as: 'uploader',
        attributes: ['id', 'username', 'fullName'],
      }],
    });
    if (!record) {
      return res.status(404).json({ error: `Registro meteorológico con ID ${id} no encontrado.` });
    }
    return res.status(200).json(record);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

// POST /data — Crear nuevo registro meteorológico (solo admin)
const createData = async (req, res) => {
  const {
    date, latitude, longitude,
    rainProbability, precipitation, windSpeed,
    tempMin, tempMax, tempCurrent,
  } = req.body;

  try {
    const newRecord = await Pedidos.create({
      date,
      userId: req.user.id,
      latitude,
      longitude,
      rainProbability,
      precipitation,
      windSpeed,
      tempMin,
      tempMax,
      tempCurrent,
    });

    return res.status(201).json({
      message: 'Registro meteorológico creado correctamente.',
      data: newRecord,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

// PUT /data/:id — Actualizar registro meteorológico (solo admin)
const updateData = async (req, res) => {
  const { id } = req.params;
  const {
    date, latitude, longitude,
    rainProbability, precipitation, windSpeed,
    tempMin, tempMax, tempCurrent,
  } = req.body;

  try {
    const record = await Pedidos.findByPk(id);
    if (!record) {
      return res.status(404).json({ error: `Registro meteorológico con ID ${id} no encontrado.` });
    }

    const updateData = {};
    if (date !== undefined) updateData.date = date;
    if (latitude !== undefined) updateData.latitude = latitude;
    if (longitude !== undefined) updateData.longitude = longitude;
    if (rainProbability !== undefined) updateData.rainProbability = rainProbability;
    if (precipitation !== undefined) updateData.precipitation = precipitation;
    if (windSpeed !== undefined) updateData.windSpeed = windSpeed;
    if (tempMin !== undefined) updateData.tempMin = tempMin;
    if (tempMax !== undefined) updateData.tempMax = tempMax;
    if (tempCurrent !== undefined) updateData.tempCurrent = tempCurrent;

    await record.update(updateData);

    return res.status(200).json({
      message: 'Registro meteorológico actualizado correctamente.',
      data: record,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

// DELETE /data/:id — Eliminar registro meteorológico (solo admin)
const deleteData = async (req, res) => {
  const { id } = req.params;

  try {
    const record = await Pedidos.findByPk(id);
    if (!record) {
      return res.status(404).json({ error: `Registro meteorológico con ID ${id} no encontrado.` });
    }

    await record.destroy();
    return res.status(200).json({ message: `Registro meteorológico con ID ${id} eliminado correctamente.` });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

module.exports = {
  getAllData,
  getDataById,
  createData,
  updateData,
  deleteData,
};
