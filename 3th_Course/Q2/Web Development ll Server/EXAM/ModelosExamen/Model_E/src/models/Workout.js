const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');
const User = require('./User');
const Workout = sequelize.define('Workout', {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  date: { type: DataTypes.DATE, allowNull: false },
  activityType: { type: DataTypes.ENUM('carrera', 'ciclismo', 'natación', 'pesas', 'otro'), allowNull: false },
  duration: { type: DataTypes.INTEGER, allowNull: false, validate: { min: 1 } },
  distance: { type: DataTypes.FLOAT, allowNull: true, validate: { min: 0 } },
  caloriesBurned: { type: DataTypes.FLOAT, allowNull: false, validate: { min: 0 } },
  avgHeartRate: { type: DataTypes.INTEGER, allowNull: false, validate: { min: 0 } },
  notes: { type: DataTypes.TEXT, allowNull: true },
  recordedBy: { type: DataTypes.INTEGER, allowNull: false, references: { model: User, key: 'id' } },
}, { tableName: 'workouts', timestamps: true });
User.hasMany(Workout, { foreignKey: 'recordedBy', as: 'workouts' });
Workout.belongsTo(User, { foreignKey: 'recordedBy', as: 'athlete' });
module.exports = Workout;
