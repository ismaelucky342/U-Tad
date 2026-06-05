// src/models/WeatherData.js
const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');
const User = require('./User');

// ============================================================
// CAMBIA ESTO: Este es el modelo de datos del dominio.
// Es lo que más varía entre enunciados.
// Renombra el modelo y cambia TODOS los campos por los del tuyo.
// Ejemplos: Producto, Libro, Pelicula, Sensor, Evento...
// ============================================================
const WeatherData = sequelize.define('WeatherData', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  // --- CAMPOS DEL DOMINIO (meteorología en este caso) ---
  recordDate: {
    type: DataTypes.DATE,
    allowNull: false,
    defaultValue: DataTypes.NOW,
  },
  latitude: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
  longitude: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
  rainProbability: {
    type: DataTypes.FLOAT,        // Porcentaje 0-100
    allowNull: false,
    validate: { min: 0, max: 100 },
  },
  precipitation: {
    type: DataTypes.FLOAT,        // Litros por m²
    allowNull: false,
    defaultValue: 0,
  },
  windSpeed: {
    type: DataTypes.FLOAT,        // km/h
    allowNull: false,
    defaultValue: 0,
  },
  tempMin: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
  tempMax: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
  tempCurrent: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
  // Foreign key: quién subió el registro
  userId: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: { model: 'users', key: 'id' },
  },
}, {
  tableName: 'weather_data',
  timestamps: true,
});

// Relación: Un usuario puede tener muchos registros
User.hasMany(WeatherData, { foreignKey: 'userId', as: 'weatherData' });
WeatherData.belongsTo(User, { foreignKey: 'userId', as: 'uploader' });

module.exports = WeatherData;
