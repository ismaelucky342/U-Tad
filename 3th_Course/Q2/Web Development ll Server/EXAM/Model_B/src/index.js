require('dotenv').config();
const express = require('express');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const bcrypt = require('bcryptjs');

const sequelize = require('./config/database');
const swaggerSpec = require('./config/swagger');

// Importar modelos
const User = require('./models/User');
const Book = require('./models/Book');

// Importar rutas
const userRoutes = require('./routes/userRoutes');
const bookRoutes = require('./routes/bookRoutes');

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
    customSiteTitle: 'Library API - Documentación',
    customCss: '.swagger-ui .topbar { background-color: #d32f2f; }',
  })
);

// Endpoint para obtener el JSON de Swagger
app.get('/api-docs.json', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.send(swaggerSpec);
});

// ─── Rutas de la API ──────────────────────────────────────────────────────────
app.use('/api/users', userRoutes);
app.use('/api/books', bookRoutes);

// ─── Ruta raíz ────────────────────────────────────────────────────────────────
app.get('/', (req, res) => {
  res.json({
    message: 'Library API funcionando correctamente.',
    version: '1.0.0',
    documentation: `http://localhost:${PORT}/api-docs`,
    endpoints: {
      users: `http://localhost:${PORT}/api/users`,
      books: `http://localhost:${PORT}/api/books`,
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
    await sequelize.sync({ alter: true });
    console.log('✅ Base de datos sincronizada correctamente.');

    const adminExists = await User.findOne({ where: { email: 'admin@library.com' } });
    if (!adminExists) {
      const hashedPassword = await bcrypt.hash('admin123', 10);
      await User.create({
        username: 'admin_library',
        email: 'admin@library.com',
        fullName: 'Administrador Biblioteca',
        password: hashedPassword,
        isAdmin: true,
      });
      console.log('✅ Usuario administrador creado: admin@library.com / admin123');
    }

    const bookCount = await Book.count();
    if (bookCount === 0) {
      const admin = await User.findOne({ where: { email: 'admin@library.com' } });
      await Book.bulkCreate([
        {
          title: '1984',
          author: 'George Orwell',
          isbn: '978-0451524935',
          genre: 'Distopía',
          publicationYear: 1949,
          pages: 328,
          available: true,
          synopsis: 'Una novela sobre un régimen totalitario donde la libertad es suprimida.',
          userId: admin.id,
        },
        {
          title: 'Don Quijote',
          author: 'Miguel de Cervantes',
          isbn: '978-8420412498',
          genre: 'Novela',
          publicationYear: 1605,
          pages: 1072,
          available: true,
          synopsis: 'Las aventuras de un hidalgo español que se vuelve loco leyendo libros de caballerías.',
          userId: admin.id,
        },
      ]);
      console.log('✅ Libros de ejemplo creados.');
    }

    app.listen(PORT, () => {
      console.log(`\n🚀 Servidor arrancado en http://localhost:${PORT}`);
      console.log(`📚 Documentación Swagger: http://localhost:${PORT}/api-docs`);
      console.log(`\n🔑 Credenciales de administrador:`);
      console.log(`   Email: admin@library.com`);
      console.log(`   Password: admin123\n`);
    });
  } catch (error) {
    console.error('❌ Error al iniciar el servidor:', error);
    process.exit(1);
  }
};

startServer();
