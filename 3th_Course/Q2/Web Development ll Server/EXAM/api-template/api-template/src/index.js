// src/index.js
require('dotenv').config();
const express = require('express');
const swaggerUi = require('swagger-ui-express');
const swaggerSpec = require('./config/swagger');
const sequelize = require('./config/database');

// Importar modelos para que Sequelize los registre y cree las tablas
require('./models/User');
require('./models/WeatherData');     // CAMBIA ESTO: importa tu modelo de dominio

// Importar rutas
const userRoutes = require('./routes/userRoutes');
const dataRoutes = require('./routes/dataRoutes');   // CAMBIA ESTO: importa tus rutas

const app = express();
const PORT = process.env.PORT || 3000;

// ─── Middlewares globales ────────────────────────────────────
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ─── Documentación Swagger ───────────────────────────────────
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec, {
  customSiteTitle: 'API Meteorológica - Docs',
}));

// ─── Rutas ───────────────────────────────────────────────────
// CAMBIA ESTO: Ajusta los prefijos de ruta según el enunciado
app.use('/users', userRoutes);
app.use('/data', dataRoutes);   // CAMBIA ESTO: cambia '/data' por tu ruta

// ─── Ruta raíz informativa ───────────────────────────────────
app.get('/', (req, res) => {
  res.json({
    message: 'API Meteorológica en funcionamiento',
    docs: `http://localhost:${PORT}/api-docs`,
    endpoints: {
      users: `http://localhost:${PORT}/users`,
      data: `http://localhost:${PORT}/data`,
    },
  });
});

// ─── Manejo de rutas no encontradas ─────────────────────────
app.use((req, res) => {
  res.status(404).json({ success: false, message: `Ruta ${req.originalUrl} no encontrada` });
});

// ─── Manejo global de errores ────────────────────────────────
app.use((err, req, res, next) => {
  console.error('Error no controlado:', err.stack);
  res.status(500).json({ success: false, message: 'Error interno del servidor' });
});

// ─── Sincronizar BD y arrancar servidor ─────────────────────
sequelize.sync({ alter: true })     // alter:true actualiza tablas sin borrar datos
  .then(() => {
    console.log('✅ Base de datos sincronizada');
    app.listen(PORT, () => {
      console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`);
      console.log(`📚 Documentación en http://localhost:${PORT}/api-docs`);
    });
  })
  .catch(err => {
    console.error('❌ Error al sincronizar la base de datos:', err);
    process.exit(1);
  });

module.exports = app;
