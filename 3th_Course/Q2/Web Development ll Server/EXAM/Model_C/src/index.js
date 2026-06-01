require('dotenv').config();
const express = require('express');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const bcrypt = require('bcryptjs');
const sequelize = require('./config/database');
const swaggerSpec = require('./config/swagger');
const User = require('./models/User');
const Event = require('./models/Event');
const userRoutes = require('./routes/userRoutes');
const eventRoutes = require('./routes/eventRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec, { explorer: true, customSiteTitle: 'Events API - Documentación' }));
app.get('/api-docs.json', (req, res) => { res.setHeader('Content-Type', 'application/json'); res.send(swaggerSpec); });
app.use('/api/users', userRoutes);
app.use('/api/events', eventRoutes);
app.get('/', (req, res) => {
  res.json({
    message: 'Events API funcionando correctamente.',
    version: '1.0.0',
    documentation: `http://localhost:${PORT}/api-docs`,
    endpoints: { users: `http://localhost:${PORT}/api/users`, events: `http://localhost:${PORT}/api/events` },
  });
});
app.use((req, res) => res.status(404).json({ error: `Ruta ${req.method} ${req.originalUrl} no encontrada.` }));
app.use((err, req, res, next) => { console.error('Error:', err.stack); res.status(500).json({ error: 'Error interno del servidor.', details: err.message }); });

const startServer = async () => {
  try {
    await sequelize.sync({ alter: true });
    console.log('✅ Base de datos sincronizada.');
    const adminExists = await User.findOne({ where: { email: 'admin@events.com' } });
    if (!adminExists) {
      const hashedPassword = await bcrypt.hash('admin123', 10);
      await User.create({ username: 'admin_events', email: 'admin@events.com', fullName: 'Administrador Eventos', password: hashedPassword, isAdmin: true });
      console.log('✅ Usuario administrador creado: admin@events.com / admin123');
    }
    const eventCount = await Event.count();
    if (eventCount === 0) {
      const admin = await User.findOne({ where: { email: 'admin@events.com' } });
      await Event.bulkCreate([
        { name: 'Festival de Música Verano', eventDate: '2024-07-15 20:00', city: 'Madrid', address: 'Plaza Mayor, 5', maxCapacity: 5000, availableSpots: 5000, ticketPrice: 45, category: 'concierto', description: 'Gran festival de música en vivo.', organizerId: admin.id },
        { name: 'Partida de Fútbol Amistosa', eventDate: '2024-06-20 19:00', city: 'Barcelona', address: 'Estadio Olimpico, s/n', maxCapacity: 60000, availableSpots: 45000, ticketPrice: 25, category: 'deporte', description: 'Amistoso entre equipos locales.', organizerId: admin.id },
      ]);
      console.log('✅ Eventos de ejemplo creados.');
    }
    app.listen(PORT, () => {
      console.log(`\n🚀 Servidor arrancado en http://localhost:${PORT}`);
      console.log(`📚 Documentación: http://localhost:${PORT}/api-docs\n`);
    });
  } catch (error) {
    console.error('❌ Error:', error);
    process.exit(1);
  }
};

startServer();
