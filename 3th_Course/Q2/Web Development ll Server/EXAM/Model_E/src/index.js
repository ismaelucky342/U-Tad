require('dotenv').config();
const express = require('express');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const bcrypt = require('bcryptjs');
const sequelize = require('./config/database');
const swaggerSpec = require('./config/swagger');
const User = require('./models/User');
const Workout = require('./models/Workout');
const userRoutes = require('./routes/userRoutes');
const workoutRoutes = require('./routes/workoutRoutes');
const app = express();
const PORT = process.env.PORT || 3000;
app.use(cors());
app.use(express.json());
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec, { explorer: true }));
app.use('/api/users', userRoutes);
app.use('/api/workouts', workoutRoutes);
app.get('/', (req, res) => res.json({ message: 'Workouts API funcionando.', version: '1.0.0' }));
app.use((req, res) => res.status(404).json({ error: 'No encontrado.' }));
app.use((err, req, res) => res.status(500).json({ error: 'Error interno.' }));
const startServer = async () => {
  try {
    await sequelize.sync({ alter: true });
    const adminExists = await User.findOne({ where: { email: 'admin@workouts.com' } });
    if (!adminExists) {
      const hashedPassword = await bcrypt.hash('admin123', 10);
      await User.create({ username: 'admin_workouts', email: 'admin@workouts.com', fullName: 'Admin Entrenamientos', password: hashedPassword, isAdmin: true });
    }
    app.listen(PORT, () => console.log(`🚀 Servidor en http://localhost:${PORT}`));
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
};
startServer();
