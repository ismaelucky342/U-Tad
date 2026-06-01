# ⚙️ MIDDLEWARE Y PATRONES COMUNES

## VALIDACIÓN DE ERRORES

```javascript
// ─── src/middleware/validationHandler.js ─────────────────────

const { validationResult } = require('express-validator');

const handleValidationErrors = (req, res, next) => {
  const errors = validationResult(req);
  
  if (!errors.isEmpty()) {
    const formattedErrors = errors.array().map(error => ({
      field: error.param,
      message: error.msg,
      value: error.value,
    }));

    return res.status(400).json({
      error: 'Validación fallida.',
      details: formattedErrors,
    });
  }

  next();
};

module.exports = { handleValidationErrors };
```

---

## CORS Y SEGURIDAD

```javascript
// ─── En src/index.js ────────────────────────────────────────

const cors = require('cors');

// Opción 1: Permitir todos los orígenes (desarrollo)
app.use(cors());

// Opción 2: Permitir orígenes específicos (producción)
const allowedOrigins = [
  'http://localhost:3000',
  'http://localhost:3001',
  'https://example.com'
];

app.use(cors({
  origin: (origin, callback) => {
    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('CORS no permitido'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
}));
```

---

## MANEJO GLOBAL DE ERRORES

```javascript
// ─── Error handler en src/index.js ─────────────────────────

// Rutas normales aquí...

// Manejo 404 - Debe estar DESPUÉS de todas las rutas
app.use((req, res) => {
  res.status(404).json({
    error: `Ruta ${req.method} ${req.originalUrl} no encontrada.`,
    availableEndpoints: {
      users: 'GET /api/users',
      resources: 'GET /api/resources',
      docs: 'GET /api-docs',
    },
  });
});

// Error handler global - Debe estar ÚLTIMO
app.use((err, req, res, next) => {
  console.error(err);

  // Errores de Sequelize
  if (err.name === 'SequelizeValidationError') {
    return res.status(400).json({
      error: 'Error de validación en base de datos.',
      details: err.errors.map(e => e.message),
    });
  }

  if (err.name === 'SequelizeUniqueConstraintError') {
    return res.status(400).json({
      error: 'Valor duplicado en campo único.',
      field: err.errors[0]?.path || 'unknown',
    });
  }

  // Errores de JWT
  if (err.name === 'JsonWebTokenError') {
    return res.status(401).json({ error: 'Token inválido.' });
  }

  // Errores genéricos
  res.status(err.status || 500).json({
    error: err.message || 'Error interno del servidor.',
    ...(process.env.NODE_ENV === 'development' && { stack: err.stack }),
  });
});
```

---

## MIDDLEWARE DE LOGGING

```javascript
// ─── Logging simple ────────────────────────────────────────

const loggingMiddleware = (req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = Date.now() - start;
    const timestamp = new Date().toISOString();
    
    console.log(
      `[${timestamp}] ${req.method} ${req.originalUrl} - ${res.statusCode} (${duration}ms)`
    );
  });
  
  next();
};

// En src/index.js, ANTES de otras rutas:
app.use(loggingMiddleware);
```

---

## MIDDLEWARE DE RATE LIMITING (opcional)

```javascript
// npm install express-rate-limit

const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutos
  max: 100,                  // Máximo 100 requests
  message: 'Demasiadas peticiones, intenta más tarde.',
});

// Aplicar a rutas específicas
app.use('/api/users/login', limiter);
app.use('/api/users/register', limiter);

// O aplicar globalmente
app.use(limiter);
```

---

## PATRÓN DE CONTROLADOR CON ERROR HANDLING

```javascript
// Template robusto para copiar

const createResource = async (req, res) => {
  try {
    const { campo1, campo2 } = req.body;
    
    // Validaciones adicionales si es necesario
    if (!campo1 || !campo2) {
      return res.status(400).json({ error: 'Campos obligatorios.' });
    }

    // Crear objeto
    const resource = await Resource.create({
      campo1,
      campo2,
      userId: req.user.id, // Usuario autenticado
    });

    // Respuesta exitosa
    return res.status(201).json({
      message: 'Recurso creado correctamente.',
      data: resource,
    });
  } catch (error) {
    // Logging
    console.error('Error en createResource:', error.message);

    // Respuesta de error
    return res.status(500).json({
      error: 'Error al crear recurso.',
      details: error.message,
    });
  }
};

// Con relaciones (include)
const getResourcesWithRelations = async (req, res) => {
  try {
    const resources = await Resource.findAll({
      include: [
        {
          model: User,
          as: 'creator',
          attributes: ['id', 'username', 'fullName'],
        },
      ],
      order: [['createdAt', 'DESC']],
    });

    return res.status(200).json({
      total: resources.length,
      data: resources,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error al obtener recursos.' });
  }
};

// Actualización con validación
const updateResource = async (req, res) => {
  try {
    const { id } = req.params;
    const { campo1, campo2 } = req.body;

    // Buscar recurso
    const resource = await Resource.findByPk(id);
    if (!resource) {
      return res.status(404).json({ error: 'Recurso no encontrado.' });
    }

    // Actualizar solo campos enviados
    if (campo1 !== undefined) resource.campo1 = campo1;
    if (campo2 !== undefined) resource.campo2 = campo2;

    await resource.save();

    return res.status(200).json({
      message: 'Recurso actualizado correctamente.',
      data: resource,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error al actualizar recurso.' });
  }
};

// Delete con confirmación
const deleteResource = async (req, res) => {
  try {
    const { id } = req.params;

    const resource = await Resource.findByPk(id);
    if (!resource) {
      return res.status(404).json({ error: 'Recurso no encontrado.' });
    }

    await resource.destroy();

    return res.status(200).json({
      message: `Recurso ${id} eliminado correctamente.`,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error al eliminar recurso.' });
  }
};
```

---

## PATRÓN DE MODELO COMPLETO

```javascript
// ─── src/models/Resource.js ────────────────────────────────

const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const Resource = sequelize.define('Resource', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  name: {
    type: DataTypes.STRING(100),
    allowNull: false,
  },
  description: {
    type: DataTypes.TEXT,
  },
  status: {
    type: DataTypes.ENUM('activo', 'inactivo', 'archivado'),
    defaultValue: 'activo',
  },
  priority: {
    type: DataTypes.ENUM('baja', 'media', 'alta'),
    defaultValue: 'media',
  },
  dueDate: {
    type: DataTypes.DATEONLY,
  },
  value: {
    type: DataTypes.FLOAT,
    validate: { min: 0 },
  },
  tags: {
    type: DataTypes.JSON,
    defaultValue: [],
  },
  userId: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: { model: 'Users', key: 'id' },
    onDelete: 'CASCADE',
  },
}, {
  tableName: 'resources',
  timestamps: true,
  createdAt: 'createdAt',
  updatedAt: 'updatedAt',
});

module.exports = Resource;
```

---

## RELACIONES EN MODELS

```javascript
// ─── En User.js ────────────────────────────────────────────
const User = sequelize.define('User', { /* ... */ });
const Book = require('./Book');
const Event = require('./Event');
// etc.

User.hasMany(Book, { foreignKey: 'userId', as: 'books' });
User.hasMany(Event, { foreignKey: 'userId', as: 'events' });

// ─── En Book.js ────────────────────────────────────────────
const Book = sequelize.define('Book', { /* ... */ });
const User = require('./User');

Book.belongsTo(User, { foreignKey: 'userId', as: 'creator' });

module.exports = Book;
```

---

## DATABASE CONFIGURATION

```javascript
// ─── src/config/database.js ────────────────────────────────

const { Sequelize } = require('sequelize');
const path = require('path');

const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, '../../database.sqlite'),
  logging: process.env.NODE_ENV === 'development' ? console.log : false,
  define: {
    timestamps: true,
    charset: 'utf8mb4',
    collate: 'utf8mb4_unicode_ci',
  },
});

// Verificar conexión
sequelize.authenticate()
  .then(() => console.log('✅ Base de datos conectada.'))
  .catch(err => console.error('❌ Error BD:', err));

module.exports = sequelize;
```

---

## SWAGGER BÁSICO

```javascript
// ─── src/config/swagger.js ────────────────────────────────

const swaggerJsdoc = require('swagger-jsdoc');

const swaggerSpec = swaggerJsdoc({
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Your API',
      version: '1.0.0',
      description: 'Documentación de Your API',
    },
    servers: [
      {
        url: 'http://localhost:3000',
        description: 'Development server',
      },
      {
        url: 'http://localhost:3001',
        description: 'Testing server',
      },
    ],
    components: {
      securitySchemes: {
        bearerAuth: {
          type: 'http',
          scheme: 'bearer',
          bearerFormat: 'JWT',
        },
      },
    },
    security: [{ bearerAuth: [] }],
  },
  apis: [
    './src/routes/*.js',
  ],
});

module.exports = swaggerSpec;
```

---

## .ENV SEGURO

```
# .env
PORT=3000
DATABASE=database.sqlite
JWT_SECRET=cambiar_esto_en_produccion_a_algo_seguro_1234567890
NODE_ENV=development

# Opcional para CORS
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3001

# Opcional para logs
DEBUG=false
