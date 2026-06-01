const Event = require('../models/Event');
const User = require('../models/User');

const getAllEvents = async (req, res) => {
  try {
    const events = await Event.findAll({
      include: [{ model: User, as: 'organizer', attributes: ['id', 'username', 'fullName'] }],
      order: [['eventDate', 'ASC']],
    });
    return res.status(200).json(events);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

const getEventById = async (req, res) => {
  const { id } = req.params;
  try {
    const event = await Event.findByPk(id, {
      include: [{ model: User, as: 'organizer', attributes: ['id', 'username', 'fullName'] }],
    });
    if (!event) return res.status(404).json({ error: `Evento con ID ${id} no encontrado.` });
    return res.status(200).json(event);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

const createEvent = async (req, res) => {
  const { name, eventDate, city, address, maxCapacity, availableSpots, ticketPrice, category, description } = req.body;
  try {
    const newEvent = await Event.create({
      name, eventDate, city, address, maxCapacity, availableSpots, ticketPrice, category, description, organizerId: req.user.id,
    });
    return res.status(201).json({ message: 'Evento creado correctamente.', data: newEvent });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

const updateEvent = async (req, res) => {
  const { id } = req.params;
  const { name, eventDate, city, address, maxCapacity, availableSpots, ticketPrice, category, description } = req.body;
  try {
    const event = await Event.findByPk(id);
    if (!event) return res.status(404).json({ error: `Evento con ID ${id} no encontrado.` });
    const updateData = {};
    if (name !== undefined) updateData.name = name;
    if (eventDate !== undefined) updateData.eventDate = eventDate;
    if (city !== undefined) updateData.city = city;
    if (address !== undefined) updateData.address = address;
    if (maxCapacity !== undefined) updateData.maxCapacity = maxCapacity;
    if (availableSpots !== undefined) updateData.availableSpots = availableSpots;
    if (ticketPrice !== undefined) updateData.ticketPrice = ticketPrice;
    if (category !== undefined) updateData.category = category;
    if (description !== undefined) updateData.description = description;
    await event.update(updateData);
    return res.status(200).json({ message: 'Evento actualizado correctamente.', data: event });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

const deleteEvent = async (req, res) => {
  const { id } = req.params;
  try {
    const event = await Event.findByPk(id);
    if (!event) return res.status(404).json({ error: `Evento con ID ${id} no encontrado.` });
    await event.destroy();
    return res.status(200).json({ message: `Evento con ID ${id} eliminado correctamente.` });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

module.exports = { getAllEvents, getEventById, createEvent, updateEvent, deleteEvent };
