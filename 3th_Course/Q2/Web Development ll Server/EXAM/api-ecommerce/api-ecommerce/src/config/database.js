// src/config/database.js
const { Sequelize } = require('sequelize');

// ============================================================
// CAMBIA ESTO: Configuración de base de datos
// Por defecto usa SQLite (fichero local, sin instalar nada).
// Para MySQL/PostgreSQL cambia el dialecto y credenciales.
// ============================================================
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: './database.sqlite',       // Archivo local de SQLite
  logging: false,                      // Pon true para ver las queries SQL
});

// Para MySQL sería así:
// const sequelize = new Sequelize(
//   process.env.DB_NAME,
//   process.env.DB_USER,
//   process.env.DB_PASSWORD,
//   { host: process.env.DB_HOST, dialect: 'mysql', logging: false }
// );

module.exports = sequelize;
