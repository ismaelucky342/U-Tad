// src/index.js
require('dotenv').config();
const express = require('express');
const swaggerUi = require('swagger-ui-express');
const swaggerSpec = require('./config/swagger');
const sequelize = require('./config/database');

// Registrar modelos (el orden importa: User antes que Order por la FK)
require('./models/User');
require('./models/Order');

const userRoutes = require('./routes/userRoutes');
const orderRoutes = require('./routes/orderRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

// ─── Middlewares globales ────────────────────────────────────
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ─── Swagger ─────────────────────────────────────────────────
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec, {
  customSiteTitle: 'E-Commerce API Docs',
}));

// ─── Rutas ───────────────────────────────────────────────────
app.use('/users', userRoutes);
app.use('/orders', orderRoutes);

// ─── Info raíz ───────────────────────────────────────────────
app.get('/', (req, res) => {
  res.json({
    message: '🛒 E-Commerce API en funcionamiento',
    docs: `http://localhost:${PORT}/api-docs`,
    endpoints: {
      users: `http://localhost:${PORT}/users`,
      orders: `http://localhost:${PORT}/orders`,
    },
    roles: {
      admin: 'Acceso total: gestiona usuarios, ve todos los pedidos, cambia estados',
      client: 'Registro público, crea y cancela sus propios pedidos, edita su perfil',
    },
  });
});

// ─── 404 ─────────────────────────────────────────────────────
app.use((req, res) => {
  res.status(404).json({ success: false, message: `Ruta ${req.originalUrl} no encontrada` });
});

// ─── Error global ────────────────────────────────────────────
app.use((err, req, res, next) => {
  console.error('Error no controlado:', err.stack);
  res.status(500).json({ success: false, message: 'Error interno del servidor' });
});

// ─── Arrancar ────────────────────────────────────────────────
sequelize.sync({ alter: true })
  .then(() => {
    console.log('✅ Base de datos sincronizada');
    app.listen(PORT, () => {
      console.log(`🚀 Servidor en http://localhost:${PORT}`);
      console.log(`📚 Swagger en http://localhost:${PORT}/api-docs`);
    });
  })
  .catch(err => {
    console.error('❌ Error al sincronizar BD:', err);
    process.exit(1);
  });

module.exports = app;
