const Workout = require('../models/Workout');
const User = require('../models/User');
const getAllWorkouts = async (req, res) => {
  try {
    const workouts = await Workout.findAll({ include: [{ model: User, as: 'athlete', attributes: ['id', 'username', 'fullName'] }], order: [['date', 'DESC']] });
    return res.status(200).json(workouts);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno.' });
  }
};
const getWorkoutById = async (req, res) => {
  const { id } = req.params;
  try {
    const workout = await Workout.findByPk(id, { include: [{ model: User, as: 'athlete', attributes: ['id', 'username', 'fullName'] }] });
    if (!workout) return res.status(404).json({ error: 'No encontrado.' });
    return res.status(200).json(workout);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno.' });
  }
};
const createWorkout = async (req, res) => {
  const { date, activityType, duration, distance, caloriesBurned, avgHeartRate, notes } = req.body;
  try {
    const newWorkout = await Workout.create({ date, activityType, duration, distance, caloriesBurned, avgHeartRate, notes, recordedBy: req.user.id });
    return res.status(201).json({ message: 'Entrenamiento creado.', data: newWorkout });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno.' });
  }
};
const updateWorkout = async (req, res) => {
  const { id } = req.params;
  const { date, activityType, duration, distance, caloriesBurned, avgHeartRate, notes } = req.body;
  try {
    const workout = await Workout.findByPk(id);
    if (!workout) return res.status(404).json({ error: 'No encontrado.' });
    const updateData = {};
    if (date !== undefined) updateData.date = date;
    if (activityType !== undefined) updateData.activityType = activityType;
    if (duration !== undefined) updateData.duration = duration;
    if (distance !== undefined) updateData.distance = distance;
    if (caloriesBurned !== undefined) updateData.caloriesBurned = caloriesBurned;
    if (avgHeartRate !== undefined) updateData.avgHeartRate = avgHeartRate;
    if (notes !== undefined) updateData.notes = notes;
    await workout.update(updateData);
    return res.status(200).json({ message: 'Actualizado.', data: workout });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno.' });
  }
};
const deleteWorkout = async (req, res) => {
  const { id } = req.params;
  try {
    const workout = await Workout.findByPk(id);
    if (!workout) return res.status(404).json({ error: 'No encontrado.' });
    await workout.destroy();
    return res.status(200).json({ message: 'Eliminado.' });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno.' });
  }
};
module.exports = { getAllWorkouts, getWorkoutById, createWorkout, updateWorkout, deleteWorkout };
