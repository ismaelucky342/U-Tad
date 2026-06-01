require('dotenv').config();
const express = require('express');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const bcrypt = require('bcryptjs');
const sequelize = require('./config/database');
const swaggerSpec = require('./config/swagger');
const User = require('./models/User');
const Article = require('./models/Article');
const userRoutes = require('./routes/userRoutes');
const articleRoutes = require('./routes/articleRoutes');
const app = express();
const PORT = process.env.PORT || 3000;
app.use(cors());
app.use(express.json());
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec, { explorer: true }));
app.use('/api/users', userRoutes);
app.use('/api/articles', articleRoutes);
app.get('/', (req, res) => res.json({ message: 'Articles API funcionando.', version: '1.0.0' }));
app.use((req, res) => res.status(404).json({ error: 'No encontrado.' }));
app.use((err, req, res) => res.status(500).json({ error: 'Error interno.' }));
const startServer = async () => {
  try {
    await sequelize.sync({ alter: true });
    const adminExists = await User.findOne({ where: { email: 'admin@articles.com' } });
    if (!adminExists) {
      const hashedPassword = await bcrypt.hash('admin123', 10);
      await User.create({ username: 'admin_articles', email: 'admin@articles.com', fullName: 'Admin Artículos', password: hashedPassword, isAdmin: true });
    }
    app.listen(PORT, () => console.log(`🚀 Servidor en http://localhost:${PORT}`));
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
};
startServer();
