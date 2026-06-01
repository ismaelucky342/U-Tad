require('dotenv').config();
const express = require('express');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const bcrypt = require('bcryptjs');
const sequelize = require('./config/database');
const swaggerSpec = require('./config/swagger');
const User = require('./models/User');
const Product = require('./models/Product');
const userRoutes = require('./routes/userRoutes');
const productRoutes = require('./routes/productRoutes');
const app = express();
const PORT = process.env.PORT || 3000;
app.use(cors());
app.use(express.json());
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec, { explorer: true, customSiteTitle: 'Products API' }));
app.get('/api-docs.json', (req, res) => { res.send(swaggerSpec); });
app.use('/api/users', userRoutes);
app.use('/api/products', productRoutes);
app.get('/', (req, res) => res.json({
  message: 'Products API funcionando.',
  version: '1.0.0',
  documentation: `http://localhost:${PORT}/api-docs`,
  endpoints: { users: `http://localhost:${PORT}/api/users`, products: `http://localhost:${PORT}/api/products` },
}));
app.use((req, res) => res.status(404).json({ error: 'Ruta no encontrada.' }));
app.use((err, req, res, next) => { console.error(err.stack); res.status(500).json({ error: 'Error interno.' }); });
const startServer = async () => {
  try {
    await sequelize.sync({ alter: true });
    const adminExists = await User.findOne({ where: { email: 'admin@products.com' } });
    if (!adminExists) {
      const hashedPassword = await bcrypt.hash('admin123', 10);
      await User.create({ username: 'admin_products', email: 'admin@products.com', fullName: 'Admin Productos', password: hashedPassword, isAdmin: true });
      console.log('✅ Admin created: admin@products.com / admin123');
    }
    const productCount = await Product.count();
    if (productCount === 0) {
      const admin = await User.findOne({ where: { email: 'admin@products.com' } });
      await Product.bulkCreate([
        { name: 'Laptop HP 15', description: 'Laptop 15 pulgadas', price: 799.99, stock: 50, category: 'Electrónica', brand: 'HP', weight: 1800, registeredDate: '2024-01-01', registeredBy: admin.id },
        { name: 'Mouse Logitech MX', description: 'Mouse inalámbrico', price: 99.99, stock: 200, category: 'Accesorios', brand: 'Logitech', weight: 100, registeredDate: '2024-01-05', registeredBy: admin.id },
      ]);
    }
    app.listen(PORT, () => console.log(`🚀 Servidor en http://localhost:${PORT}`));
  } catch (error) {
    console.error('❌ Error:', error);
    process.exit(1);
  }
};
startServer();
