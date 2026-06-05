// src/models/User.js
const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

// ============================================================
// CAMBIA ESTO: Campos del modelo de Usuario
// Añade o quita campos según el enunciado de tu examen
// ============================================================
const User = sequelize.define('User', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  username: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  email: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
    validate: { isEmail: true },
  },
  fullName: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  password: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  // CAMPO CLAVE: rol para el sistema de permisos
  role: {
    type: DataTypes.ENUM('admin', 'user'),
    defaultValue: 'user',
  },
}, {
  tableName: 'users',
  timestamps: true,             // Añade createdAt y updatedAt automáticamente
});

module.exports = User;
