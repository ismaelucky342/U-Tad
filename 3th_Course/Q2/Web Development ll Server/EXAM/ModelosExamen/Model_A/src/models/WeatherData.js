const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');
const User = require('./User');

const WeatherData = sequelize.define('WeatherData', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  date: {
    type: DataTypes.DATEONLY,
    allowNull: false,
  },
  userId: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: {
      model: User,
      key: 'id',
    },
  },
  latitude: {
    type: DataTypes.FLOAT,
    allowNull: false,
    validate: {
      min: -90,
      max: 90,
    },
  },
  longitude: {
    type: DataTypes.FLOAT,
    allowNull: false,
    validate: {
      min: -180,
      max: 180,
    },
  },
  rainProbability: {
    type: DataTypes.FLOAT,
    allowNull: false,
    validate: {
      min: 0,
      max: 100,
    },
  },
  precipitation: {
    type: DataTypes.FLOAT,
    allowNull: false,
    validate: {
      min: 0,
    },
  },
  windSpeed: {
    type: DataTypes.FLOAT,
    allowNull: false,
    validate: {
      min: 0,
    },
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
}, {
  tableName: 'weather_data',
  timestamps: true,
});

// Asociaciones
User.hasMany(WeatherData, { foreignKey: 'userId', as: 'weatherRecords' });
WeatherData.belongsTo(User, { foreignKey: 'userId', as: 'uploader' });

module.exports = WeatherData;
