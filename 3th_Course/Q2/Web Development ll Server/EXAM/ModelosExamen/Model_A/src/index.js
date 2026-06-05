require('dotenv').config();
const express = require('express');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const bcrypt = require('bcryptjs');

const sequelize = require('./config/database');
const swaggerSpec = require('./config/swagger');

// Importar modelos (el orden importa para las asociaciones)
const User = require('./models/User');
const Pedidos = require('./models/Pedidos');

// Importar rutas
const userRoutes = require('./routes/userRoutes');
const weatherRoutes = require('./routes/weatherRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

// ─── Middlewares globales ─────────────────────────────────────────────────────
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ─── Documentación Swagger ────────────────────────────────────────────────────
app.use(
  '/api-docs',
  swaggerUi.serve,
  swaggerUi.setup(swaggerSpec, {
    explorer: true,
    customSiteTitle: 'Weather API - Documentación',
    customCss: '.swagger-ui .topbar { background-color: #1a73e8; }',
  })
);

// Endpoint para obtener el JSON de Swagger
app.get('/api-docs.json', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.send(swaggerSpec);
});

// ─── Rutas de la API ──────────────────────────────────────────────────────────
app.use('/api/users', userRoutes);
app.use('/api/data', weatherRoutes);

// ─── Ruta raíz ────────────────────────────────────────────────────────────────
app.get('/', (req, res) => {
  res.json({
    message: 'Weather API funcionando correctamente.',
    version: '1.0.0',
    documentation: `http://localhost:${PORT}/api-docs`,
    endpoints: {
      users: `http://localhost:${PORT}/api/users`,
      data: `http://localhost:${PORT}/api/data`,
    },
  });
});

// ─── Manejo de rutas no encontradas ──────────────────────────────────────────
app.use((req, res) => {
  res.status(404).json({ error: `Ruta ${req.method} ${req.originalUrl} no encontrada.` });
});

// ─── Manejo global de errores ─────────────────────────────────────────────────
app.use((err, req, res, next) => {
  console.error('Error no controlado:', err.stack);
  res.status(500).json({ error: 'Error interno del servidor.', details: err.message });
});

// ─── Sincronización de BD y arranque ─────────────────────────────────────────
const startServer = async () => {
  try {
    // Sincronizar base de datos (crea tablas si no existen)
    await sequelize.sync({ alter: true });
    console.log('✅ Base de datos sincronizada correctamente.');

    // Crear usuario administrador inicial si no existe
    const adminExists = await User.findOne({ where: { email: 'admin@weather.com' } });
    if (!adminExists) {
      const hashedPassword = await bcrypt.hash('admin123', 10);
      await User.create({
        username: 'admin_weather',
        email: 'admin@weather.com',
        fullName: 'Administrador Sistema',
        password: hashedPassword,
        isAdmin: true,
      });
      console.log('✅ Usuario administrador creado: admin@weather.com / admin123');
    }

    // Crear datos meteorológicos de ejemplo si no existen
    const dataCount = await Pedidos.count();
    if (dataCount === 0) {
      const admin = await User.findOne({ where: { email: 'admin@weather.com' } });
      await Pedidos.bulkCreate([
        {
          date: '2024-03-15',
          userId: admin.id,
          latitude: 40.4168,
          longitude: -3.7038,
          rainProbability: 75.5,
          precipitation: 12.3,
          windSpeed: 45.2,
          tempMin: 8.5,
          tempMax: 18.2,
          tempCurrent: 13.4,
        },
        {
          date: '2024-03-16',
          userId: admin.id,
          latitude: 41.3851,
          longitude: 2.1734,
          rainProbability: 20.0,
          precipitation: 0.0,
          windSpeed: 15.8,
          tempMin: 12.1,
          tempMax: 22.5,
          tempCurrent: 19.3,
        },
      ]);
      console.log('✅ Datos meteorológicos de ejemplo creados.');
    }

    app.listen(PORT, () => {
      console.log(`\n🚀 Servidor arrancado en http://localhost:${PORT}`);
      console.log(`📚 Documentación Swagger: http://localhost:${PORT}/api-docs`);
      console.log(`\n🔑 Credenciales de administrador:`);
      console.log(`   Email: admin@weather.com`);
      console.log(`   Password: admin123\n`);
    });
  } catch (error) {
    console.error('❌ Error al iniciar el servidor:', error);
    process.exit(1);
  }
};

startServer();
