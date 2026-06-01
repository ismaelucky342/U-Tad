# 🎓 MATERIAL DE ESTUDIO - REFERENCIA RÁPIDA

Este documento contiene todas las chuletas que necesitas para el examen.

---

## 1️⃣  FIELD TYPES DE SEQUELIZE

Los tipos de datos más usados en modelos Sequelize:

```javascript
const { DataTypes } = require('sequelize');

// ─── TIPOS BÁSICOS ────────────────────────────────────
DataTypes.STRING(100)         // Texto corto (hasta 100 caracteres)
DataTypes.TEXT                // Texto largo
DataTypes.INTEGER             // Números enteros
DataTypes.FLOAT               // Números decimales
DataTypes.BOOLEAN             // Verdadero/Falso
DataTypes.DATE                // Fecha y hora (2024-03-15 14:30:00)
DataTypes.DATEONLY            // Solo fecha (2024-03-15)

// ─── TIPOS ESPECIALES ────────────────────────────────
DataTypes.ENUM('valor1', 'valor2', 'valor3')  // Lista cerrada de opciones
DataTypes.JSON                // Datos en formato JSON
DataTypes.UUID                // Identificador único universal
DataTypes.ARRAY(DataTypes.STRING)             // Array (solo PostgreSQL)

// ─── CONFIGURACIÓN DE COLUMNAS ──────────────────────
{
  type: DataTypes.STRING(100),
  allowNull: false,            // No puede ser vacío
  unique: true,                // Valor único en la tabla
  defaultValue: 'valor',       // Valor por defecto
  validate: {
    min: 0,                    // Mínimo para números
    max: 100,                  // Máximo para números
    isEmail: true,             // Verifica que sea email
    isIn: ['opcion1', 'opcion2'],  // Debe estar en la lista
    len: [3, 50],              // Longitud entre 3 y 50
  },
}

// ─── EJEMPLO COMPLETO ──────────────────────────────
const User = sequelize.define('User', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  email: {
    type: DataTypes.STRING(100),
    allowNull: false,
    unique: true,
    validate: { isEmail: true },
  },
  age: {
    type: DataTypes.INTEGER,
    validate: { min: 0, max: 150 },
  },
  status: {
    type: DataTypes.ENUM('active', 'inactive', 'suspended'),
    defaultValue: 'active',
  },
  isAdmin: {
    type: DataTypes.BOOLEAN,
    defaultValue: false,
  },
}, { tableName: 'users', timestamps: true });
```

---

## 2️⃣  VALIDADORES DE EXPRESS-VALIDATOR

Todos los validadores que necesitas en una hoja rápida:

```javascript
const { body, param } = require('express-validator');

// ═════════════════════════════════════════════════════════════════
// VALIDADORES PARA BODY (JSON)
// ═════════════════════════════════════════════════════════════════

// ─── BÁSICOS ──────────────────────────────────────────────────
body('campo').notEmpty()                    // No vacío
body('campo').trim()                        // Elimina espacios
body('campo').isString()                    // Debe ser string
body('campo').isInt()                       // Debe ser entero
body('campo').isFloat()                     // Debe ser decimal
body('campo').isBoolean()                   // Debe ser boolean

// ─── STRINGS ──────────────────────────────────────────────────
body('campo').isEmail()                     // Validar email
body('campo').isLength({ min: 3, max: 50 }) // Rango de caracteres
body('campo').matches(/regex/)              // Validar con regex
body('campo').isAlphanumeric()              // Solo letras y números
body('campo').isMobilePhone()               // Número de teléfono
body('campo').isURL()                       // URL válida

// ─── NÚMEROS ──────────────────────────────────────────────────
body('campo').isFloat({ min: 0, max: 100 }) // Rango numérico
body('campo').isInt({ min: 1 })             // Entero con mínimo

// ─── FECHAS ───────────────────────────────────────────────────
body('campo').isDate()                      // Fecha válida
body('campo').isISO8601()                   // Formato ISO (2024-03-15)
body('campo').isDate({ format: 'YYYY-MM-DD' })

// ─── LISTAS ───────────────────────────────────────────────────
body('campo').isIn(['opcion1', 'opcion2'])  // Valor en lista
body('campo').isArray()                     // Debe ser array

// ─── OPCIONALES ───────────────────────────────────────────────
body('campo').optional()                    // Campo no obligatorio
body('campo').optional().isEmail()          // Email si se envía

// ─── NORMALIZACIÓN ────────────────────────────────────────────
body('campo').normalizeEmail()              // Normalizar email
body('campo').escape()                      // Escapar caracteres especiales

// ─── MENSAJES DE ERROR ────────────────────────────────────────
body('email')
  .isEmail()
  .withMessage('El email no es válido.')

// ═════════════════════════════════════════════════════════════════
// VALIDADORES PARA PARÁMETROS (URL)
// ═════════════════════════════════════════════════════════════════

param('id').isInt({ min: 1 })               // ID debe ser entero > 0
param('slug').isAlphanumeric()              // Slug sin caracteres especiales

// ═════════════════════════════════════════════════════════════════
// EJEMPLO DE USO COMPLETO
// ═════════════════════════════════════════════════════════════════

const createUserValidators = [
  body('username')
    .trim()
    .notEmpty().withMessage('El nombre de usuario es obligatorio.')
    .isLength({ min: 3, max: 50 }).withMessage('Entre 3 y 50 caracteres.')
    .matches(/^[a-zA-Z0-9_]+$/).withMessage('Solo letras, números y guiones bajos.'),
  
  body('email')
    .isEmail().withMessage('Email no válido.')
    .normalizeEmail(),
  
  body('password')
    .isLength({ min: 6 }).withMessage('Mínimo 6 caracteres.'),
  
  body('age')
    .optional()
    .isInt({ min: 0, max: 120 }).withMessage('Edad entre 0 y 120.'),
  
  body('role')
    .isIn(['user', 'admin']).withMessage('Rol no válido.'),
];

// Usar en ruta:
router.post('/users', createUserValidators, handleValidationErrors, createUser);
```

---

## 3️⃣  MIDDLEWARE DE AUTENTICACIÓN

Copiar tal cual, sin cambios:

```javascript
// ─── src/middleware/auth.js ──────────────────────────────────

const jwt = require('jsonwebtoken');
const User = require('../models/User');

// Middleware: verifica que el token JWT sea válido
const verifyToken = async (req, res, next) => {
  const authHeader = req.headers['authorization'];

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Token no proporcionado. Acceso denegado.' });
  }

  const token = authHeader.split(' ')[1];

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    const user = await User.findByPk(decoded.id);

    if (!user) {
      return res.status(401).json({ error: 'Usuario no encontrado. Token inválido.' });
    }

    req.user = user;  // Guardar usuario en req para usarlo después
    next();
  } catch (error) {
    return res.status(401).json({ error: 'Token inválido o expirado.' });
  }
};

// Middleware: verifica que el usuario sea administrador
const verifyAdmin = (req, res, next) => {
  if (!req.user || !req.user.isAdmin) {
    return res.status(403).json({ error: 'Acceso denegado. Se requieren permisos de administrador.' });
  }
  next();
};

module.exports = { verifyToken, verifyAdmin };
```

---

## 4️⃣  PLANTILLA DE VALIDADORES

Copia esta plantilla y adapta los campos:

```javascript
// ─── src/validators/resourceValidators.js ─────────────────────

const { body, param } = require('express-validator');

const createResourceValidators = [
  body('campo1')
    .notEmpty().withMessage('Campo1 es obligatorio.')
    .isLength({ min: X, max: Y }).withMessage('Entre X y Y caracteres.'),
  
  body('campo2')
    .notEmpty().withMessage('Campo2 es obligatorio.')
    .isEmail().withMessage('Email no válido.')
    .normalizeEmail(),
  
  body('campo3')
    .optional()
    .isInt({ min: 0 }).withMessage('Debe ser número positivo.'),
];

const updateResourceValidators = [
  param('id')
    .isInt({ min: 1 }).withMessage('ID debe ser entero positivo.'),
  
  body('campo1')
    .optional()
    .isLength({ min: X, max: Y }).withMessage('Entre X y Y caracteres.'),
  
  body('campo2')
    .optional()
    .isEmail().normalizeEmail(),
];

const idParamValidator = [
  param('id')
    .isInt({ min: 1 }).withMessage('ID debe ser entero positivo.'),
];

module.exports = {
  createResourceValidators,
  updateResourceValidators,
  idParamValidator,
};
```

---

## 5️⃣  PLANTILLA DE CONTROLADOR

Estructura base para CRUD:

```javascript
// ─── src/controllers/resourceController.js ────────────────────

const Resource = require('../models/Resource');
const User = require('../models/User');

// GET - Obtener todos (público o admin)
const getAllResources = async (req, res) => {
  try {
    const resources = await Resource.findAll({
      include: [{
        model: User,
        as: 'creator',
        attributes: ['id', 'username', 'fullName'],
      }],
      order: [['createdAt', 'DESC']],
    });
    return res.status(200).json(resources);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.', details: error.message });
  }
};

// GET - Obtener por ID
const getResourceById = async (req, res) => {
  const { id } = req.params;
  try {
    const resource = await Resource.findByPk(id, {
      include: [{
        model: User,
        as: 'creator',
        attributes: ['id', 'username', 'fullName'],
      }],
    });
    if (!resource) {
      return res.status(404).json({ error: `Recurso con ID ${id} no encontrado.` });
    }
    return res.status(200).json(resource);
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

// POST - Crear nuevo (admin)
const createResource = async (req, res) => {
  const { campo1, campo2, campo3 } = req.body;
  try {
    const newResource = await Resource.create({
      campo1,
      campo2,
      campo3,
      userId: req.user.id,  // Usuario autenticado
    });
    return res.status(201).json({
      message: 'Recurso creado correctamente.',
      data: newResource,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

// PUT - Actualizar (admin)
const updateResource = async (req, res) => {
  const { id } = req.params;
  const { campo1, campo2, campo3 } = req.body;
  try {
    const resource = await Resource.findByPk(id);
    if (!resource) {
      return res.status(404).json({ error: `Recurso con ID ${id} no encontrado.` });
    }
    const updateData = {};
    if (campo1 !== undefined) updateData.campo1 = campo1;
    if (campo2 !== undefined) updateData.campo2 = campo2;
    if (campo3 !== undefined) updateData.campo3 = campo3;
    await resource.update(updateData);
    return res.status(200).json({
      message: 'Recurso actualizado correctamente.',
      data: resource,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

// DELETE - Eliminar (admin)
const deleteResource = async (req, res) => {
  const { id } = req.params;
  try {
    const resource = await Resource.findByPk(id);
    if (!resource) {
      return res.status(404).json({ error: `Recurso con ID ${id} no encontrado.` });
    }
    await resource.destroy();
    return res.status(200).json({
      message: `Recurso con ID ${id} eliminado correctamente.`,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

module.exports = {
  getAllResources,
  getResourceById,
  createResource,
  updateResource,
  deleteResource,
};
```

---

## 6️⃣  PLANTILLA DE RUTAS

Estructura base para endpoints:

```javascript
// ─── src/routes/resourceRoutes.js ─────────────────────────────

const express = require('express');
const router = express.Router();

const { verifyToken, verifyAdmin } = require('../middleware/auth');
const { handleValidationErrors } = require('../middleware/validationHandler');
const {
  getAllResources,
  getResourceById,
  createResource,
  updateResource,
  deleteResource,
} = require('../controllers/resourceController');
const {
  createResourceValidators,
  updateResourceValidators,
  idParamValidator,
} = require('../validators/resourceValidators');

/**
 * @swagger
 * /resources:
 *   get:
 *     summary: Obtener todos los recursos
 *     tags: [Resources]
 *     responses:
 *       200: { description: "Lista de recursos" }
 */
router.get('/', getAllResources);

/**
 * @swagger
 * /resources/{id}:
 *   get:
 *     summary: Obtener recurso por ID
 */
router.get('/:id', idParamValidator, handleValidationErrors, getResourceById);

/**
 * @swagger
 * /resources:
 *   post:
 *     summary: Crear nuevo recurso (solo admin)
 *     security:
 *       - bearerAuth: []
 */
router.post('/', verifyToken, verifyAdmin, createResourceValidators, handleValidationErrors, createResource);

/**
 * @swagger
 * /resources/{id}:
 *   put:
 *     summary: Actualizar recurso (solo admin)
 *     security:
 *       - bearerAuth: []
 */
router.put('/:id', verifyToken, verifyAdmin, updateResourceValidators, handleValidationErrors, updateResource);

/**
 * @swagger
 * /resources/{id}:
 *   delete:
 *     summary: Eliminar recurso (solo admin)
 *     security:
 *       - bearerAuth: []
 */
router.delete('/:id', verifyToken, verifyAdmin, idParamValidator, handleValidationErrors, deleteResource);

module.exports = router;
```

---

## 7️⃣  PLANTILLA INDEX.JS

Estructura del servidor principal:

```javascript
// ─── src/index.js ────────────────────────────────────────────

require('dotenv').config();
const express = require('express');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const bcrypt = require('bcryptjs');

const sequelize = require('./config/database');
const swaggerSpec = require('./config/swagger');

// Importar modelos
const User = require('./models/User');
const Resource1 = require('./models/Resource1');
const Resource2 = require('./models/Resource2');

// Importar rutas
const userRoutes = require('./routes/userRoutes');
const resource1Routes = require('./routes/resource1Routes');
const resource2Routes = require('./routes/resource2Routes');

const app = express();
const PORT = process.env.PORT || 3000;

// ─── MIDDLEWARES ──────────────────────────────────────────────
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ─── SWAGGER ──────────────────────────────────────────────────
app.use(
  '/api-docs',
  swaggerUi.serve,
  swaggerUi.setup(swaggerSpec, {
    explorer: true,
    customSiteTitle: 'Your API - Documentación',
    customCss: '.swagger-ui .topbar { background-color: #1a73e8; }',
  })
);

app.get('/api-docs.json', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.send(swaggerSpec);
});

// ─── RUTAS ───────────────────────────────────────────────────
app.use('/api/users', userRoutes);
app.use('/api/resource1', resource1Routes);
app.use('/api/resource2', resource2Routes);

// ─── RAÍZ ────────────────────────────────────────────────────
app.get('/', (req, res) => {
  res.json({
    message: 'Your API funcionando correctamente.',
    version: '1.0.0',
    documentation: `http://localhost:${PORT}/api-docs`,
    endpoints: {
      users: `http://localhost:${PORT}/api/users`,
      resource1: `http://localhost:${PORT}/api/resource1`,
      resource2: `http://localhost:${PORT}/api/resource2`,
    },
  });
});

// ─── ERROR 404 ───────────────────────────────────────────────
app.use((req, res) => {
  res.status(404).json({ error: `Ruta ${req.method} ${req.originalUrl} no encontrada.` });
});

// ─── ERROR GLOBAL ────────────────────────────────────────────
app.use((err, req, res, next) => {
  console.error('Error no controlado:', err.stack);
  res.status(500).json({ error: 'Error interno del servidor.', details: err.message });
});

// ─── INICIAR SERVIDOR ────────────────────────────────────────
const startServer = async () => {
  try {
    // Sincronizar BD
    await sequelize.sync({ alter: true });
    console.log('✅ Base de datos sincronizada correctamente.');

    // Crear admin inicial
    const adminExists = await User.findOne({ where: { email: 'admin@yourapi.com' } });
    if (!adminExists) {
      const hashedPassword = await bcrypt.hash('admin123', 10);
      await User.create({
        username: 'admin_yourapi',
        email: 'admin@yourapi.com',
        fullName: 'Administrador Sistema',
        password: hashedPassword,
        isAdmin: true,
      });
      console.log('✅ Usuario administrador creado: admin@yourapi.com / admin123');
    }

    // Crear datos de ejemplo
    const resourceCount = await Resource1.count();
    if (resourceCount === 0) {
      const admin = await User.findOne({ where: { email: 'admin@yourapi.com' } });
      await Resource1.bulkCreate([
        {
          // datos de ejemplo
        },
      ]);
      console.log('✅ Datos de ejemplo creados.');
    }

    // Arrancar servidor
    app.listen(PORT, () => {
      console.log(`\n🚀 Servidor arrancado en http://localhost:${PORT}`);
      console.log(`📚 Documentación Swagger: http://localhost:${PORT}/api-docs`);
      console.log(`\n🔑 Credenciales de administrador:`);
      console.log(`   Email: admin@yourapi.com`);
      console.log(`   Password: admin123\n`);
    });
  } catch (error) {
    console.error('❌ Error al iniciar el servidor:', error);
    process.exit(1);
  }
};

startServer();
```

---

## 8️⃣  CHECKLIST DEL EXAMEN

☐ **Modelos** (User + 1 recurso)
  - [ ] Fields correctos con tipos
  - [ ] Validaciones
  - [ ] Relaciones (hasMany/belongsTo)

☐ **Validadores**
  - [ ] Login validators
  - [ ] Create validators
  - [ ] Update validators
  - [ ] ID param validator

☐ **Controladores**
  - [ ] Login (generar JWT)
  - [ ] CRUD completo (GET, GET/:id, POST, PUT, DELETE)
  - [ ] Manejo de errores
  - [ ] Inclusión de relaciones

☐ **Rutas**
  - [ ] Swagger docs
  - [ ] Middleware de autenticación
  - [ ] Middleware de validación
  - [ ] Puntos de acceso correctos

☐ **Config**
  - [ ] database.js
  - [ ] swagger.js
  - [ ] .env

☐ **index.js**
  - [ ] Middlewares
  - [ ] Rutas
  - [ ] Manejo de errores
  - [ ] Sync de BD
  - [ ] Datos iniciales

☐ **package.json**
  - [ ] Dependencias necesarias

---

## 9️⃣  ERRORES COMUNES

1. ❌ **Token no incluido en rutas protegidas**: Usar `verifyToken` antes de `verifyAdmin`
2. ❌ **Validadores no funcionar**: Olvidar `handleValidationErrors`
3. ❌ **CORS errors**: Falta `app.use(cors())`
4. ❌ **Rutas no encontradas**: Olvidar `app.use('/api/resource', routes)`
5. ❌ **JWT_SECRET undefined**: Falta `.env` o cargar `dotenv`
6. ❌ **Modelo no sincronizado**: Olvidar `await sequelize.sync()`
7. ❌ **Email duplicado**: No verificar unicidad antes de crear
8. ❌ **Contraseña sin hash**: Usar `bcryptjs` siempre
9. ❌ **Passwords devueltas en API**: Usar `{ exclude: ['password'] }`
10. ❌ **Relaciones no working**: Olvidar `hasMany/belongsTo` en ambos modelos
