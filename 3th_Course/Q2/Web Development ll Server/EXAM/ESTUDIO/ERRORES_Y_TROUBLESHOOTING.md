# 🚨 ERRORES COMUNES Y TROUBLESHOOTING

## TOP 20 ERRORES EN EL EXAMEN

### 1. ❌ Token Bearer Mal Formado

**Problema:**
```javascript
// ❌ INCORRECTO
Header: Authorization: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
// Resultado: Token no proporcionado. Acceso denegado.
```

**Solución:**
```javascript
// ✅ CORRECTO
Header: Authorization: "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
// En código:
const token = authHeader.split(' ')[1];
```

---

### 2. ❌ JWT_SECRET No Definido

**Problema:**
```
Unable to verify token: Cannot read property 'verify' of undefined
```

**Solución:**
```env
# .env
JWT_SECRET=mi_secreto_super_seguro_1234567890
```

```javascript
// En auth.js, asegurarse de:
const decoded = jwt.verify(token, process.env.JWT_SECRET);
```

---

### 3. ❌ Password Devuelto en Responses

**Problema:**
```javascript
// ❌ INCORRECTO - Expone passwords
const user = await User.findByPk(id);
return res.json(user); // ¡Incluye password!
```

**Solución:**
```javascript
// ✅ CORRECTO
const user = await User.findByPk(id, {
  attributes: { exclude: ['password'] }
});
return res.json(user);

// O en findAll:
const users = await User.findAll({
  attributes: { exclude: ['password'] }
});
```

---

### 4. ❌ Contraseña Sin Hash

**Problema:**
```javascript
// ❌ INCORRECTO - Almacena en texto plano!
const user = await User.create({
  email: req.body.email,
  password: req.body.password // ¡SIN HASH!
});
```

**Solución:**
```javascript
// ✅ CORRECTO - Usar bcryptjs
const bcrypt = require('bcryptjs');

const hashedPassword = await bcrypt.hash(req.body.password, 10);
const user = await User.create({
  email: req.body.email,
  password: hashedPassword
});

// Y verificar en login:
const isValid = await bcrypt.compare(req.body.password, user.password);
```

---

### 5. ❌ Falta body() en Validadores

**Problema:**
```javascript
// ❌ INCORRECTO - No valida nada
const loginValidators = [
  'email' // ¡Falta body()!
    .isEmail()
];
router.post('/login', loginValidators, handler);
```

**Solución:**
```javascript
// ✅ CORRECTO
const { body } = require('express-validator');

const loginValidators = [
  body('email').isEmail().withMessage('Email inválido'),
  body('password').notEmpty().withMessage('Password obligatorio')
];
router.post('/login', loginValidators, handleValidationErrors, handler);
```

---

### 6. ❌ Olvidar handleValidationErrors

**Problema:**
```javascript
// ❌ INCORRECTO - Validadores de express-validator se ignorarán
router.post('/login', loginValidators, loginHandler);
```

**Solución:**
```javascript
// ✅ CORRECTO
const { handleValidationErrors } = require('../middleware/validationHandler');

router.post('/login', 
  loginValidators,           // Validadores
  handleValidationErrors,    // IMPORTANTE: Verifica errores
  loginHandler               // Handler
);
```

---

### 7. ❌ Email Duplicado Sin Verificación

**Problema:**
```javascript
// ❌ INCORRECTO - No chequea duplicados
const registerUser = async (req, res) => {
  const user = await User.create({
    email: req.body.email,
    // ...
  });
};

// Segundo registro con mismo email → ERROR no controlado
```

**Solución:**
```javascript
// ✅ CORRECTO
const registerUser = async (req, res) => {
  const existing = await User.findOne({ where: { email: req.body.email } });
  if (existing) {
    return res.status(400).json({ error: 'Email ya registrado.' });
  }
  
  const user = await User.create({...});
};
```

---

### 8. ❌ Falta await en Promises

**Problema:**
```javascript
// ❌ INCORRECTO - No espera la promesa
const user = sequelize.sync();
console.log(user); // Promise {}
```

**Solución:**
```javascript
// ✅ CORRECTO
const startServer = async () => {
  await sequelize.sync({ alter: true });
  console.log('BD sincronizada');
};
```

---

### 9. ❌ Rutas Aún No Registradas

**Problema:**
```javascript
// En routers/bookRoutes.js
router.get('/top', getTopBooks);

// Pero en index.js NO se registra la ruta
app.use('/api/books', bookRoutes); // ✗ Falta esta línea
```

**Solución:**
```javascript
// ✅ En index.js, registrar todas las rutas
const bookRoutes = require('./routes/bookRoutes');
const eventRoutes = require('./routes/eventRoutes');
// etc.

app.use('/api/books', bookRoutes);
app.use('/api/events', eventRoutes);
```

---

### 10. ❌ CORS No Habilitado

**Problema:**
```
Cross-Origin Request Blocked: The Same Origin Policy disallows reading 
the remote resource at http://localhost:3000/api/...
```

**Solución:**
```javascript
// ✅ En index.js, ANTES de router
const cors = require('cors');
app.use(cors());
```

---

### 11. ❌ Olvidar Relaciones Entre Modelos

**Problema:**
```javascript
// ✅ Modelos creados
const User = require('./User');
const Book = require('./Book');

// ❌ Pero sin relaciones!
// Result: No podré hacer include en queries
```

**Solución:**
```javascript
// ✅ En models/User.js
User.hasMany(Book, { foreignKey: 'userId', as: 'books' });

// En models/Book.js
Book.belongsTo(User, { foreignKey: 'userId', as: 'creator' });

// Luego en controller:
const book = await Book.findByPk(id, {
  include: [{ model: User, as: 'creator' }]
});
```

---

### 12. ❌ Middleware Order Incorrecto

**Problema:**
```javascript
// ❌ INCORRECTO - routes ANTES de middlewares
app.use('/api', routes);
app.use(express.json()); // Muy tarde!
```

**Solución:**
```javascript
// ✅ CORRECTO
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/api', userRoutes);
app.use('/api', bookRoutes);
```

---

### 13. ❌ Error Handler Mal Posicionado

**Problema:**
```javascript
// ❌ INCORRECTO - Error handler ANTES de rutas
app.use((err, req, res, next) => { /* ... */ });
app.use('/api', routes); // Nunca llegará

// Error nunca se maneja
```

**Solución:**
```javascript
// ✅ CORRECTO - Error handler ÚLTIMO
app.use('/api/users', userRoutes);
app.use('/api/books', bookRoutes);

app.use((req, res) => { // 404 handler
  res.status(404).json({ error: 'Not found' });
});

app.use((err, req, res, next) => { // Error handler
  res.status(500).json({ error: 'Server error' });
});
```

---

### 14. ❌ Olvidar Timestamps en Modelos

**Problema:**
```javascript
// ❌ Sin timestamps
const User = sequelize.define('User', { 
  name: STRING 
});
// Resultado: No puedo usar order: [['createdAt', 'DESC']]
```

**Solución:**
```javascript
// ✅ CON timestamps (por defecto enableados)
const User = sequelize.define('User', { 
  name: STRING 
}, { 
  timestamps: true,  // Explícito (por defecto já está puesto)
  createdAt: 'createdAt',
  updatedAt: 'updatedAt'
});

// Luego:
const users = await User.findAll({
  order: [['createdAt', 'DESC']]
});
```

---

### 15. ❌ Env Variables En Desarrollo

**Problema:**
```javascript
const port = process.env.PORT || 3000;
// Funciona, pero sin .env archivo → undefined
```

**Solución:**
```bash
# Crear .env en raíz del proyecto
npm install dotenv

# .env
PORT=3000
DATABASE=database.sqlite
JWT_SECRET=abc123def456

# En src/index.js (PRIMERA línea)
require('dotenv').config();
```

---

### 16. ❌ Relaciones Con Foreign Key Mal

**Problema:**
```javascript
// ❌ INCORRECTO
const Book = sequelize.define('Book', {
  userId: INTEGER
  // Pero sin especificar foreignKey bien
});
```

**Solución:**
```javascript
// ✅ CORRECTO
const Book = sequelize.define('Book', {
  userId: {
    type: INTEGER,
    allowNull: false,
    references: { model: 'Users', key: 'id' },
    onDelete: 'CASCADE'
  }
});

Book.belongsTo(User, { foreignKey: 'userId', as: 'creator' });
```

---

### 17. ❌ Validadores Con Mensajes Confusos

**Problema:**
```javascript
// ❌ Sin mensajes claros
body('email').isEmail();
// Response: [{ param: 'email', msg: 'Invalid value' }]
// El usuario no sabe qué está mal
```

**Solución:**
```javascript
// ✅ Con mensajes claros
body('email')
  .isEmail()
  .withMessage('El email no es válido. Ejemplo: user@example.com')
  
body('password')
  .isLength({ min: 6 })
  .withMessage('La contraseña debe tener mínimo 6 caracteres.')

body('age')
  .isInt({ min: 0, max: 150 })
  .withMessage('La edad debe estar entre 0 y 150 años.')
```

---

### 18. ❌ Falta `updatedAt` en PUT

**Problema:**
```javascript
// ❌ Actualiza pero updatedAt no cambia
const book = await Book.findByPk(id);
book.title = 'Nuevo título';
book.save(); // updateAt se actualiza alone (sequelize)
```

**Solución:**
```javascript
// ✅ CORRECTO (secuelize actualiza automáticamente)
const book = await Book.findByPk(id);
book.title = 'Nuevo título';
await book.save(); // Automáticamente actualiza updatedAt

// O directo:
await Book.update(
  { title: 'Nuevo título' },
  { where: { id } }
);
```

---

### 19. ❌ Olvidar Extraer ID del Parámetro

**Problema:**
```javascript
// ❌ INCORRECTO
const getBook = async (req, res) => {
  const book = await Book.findByPk(params.id); // undefined!
};
```

**Solución:**
```javascript
// ✅ CORRECTO
const getBook = async (req, res) => {
  const { id } = req.params;
  const book = await Book.findByPk(id);
};

// En las rutas:
router.get('/:id', getBook); // :id → req.params.id
```

---

### 20. ❌ Permisos Admin Sin Verificación

**Problema:**
```javascript
// ❌ Sin verificar permisos
router.post('/books', createBook);
// Cualquiera puede crear libros
```

**Solución:**
```javascript
// ✅ CON verificación admin
const { verifyToken, verifyAdmin } = require('../middleware/auth');

router.post('/books', 
  verifyToken,  // Debe estar autenticado
  verifyAdmin,  // Debe ser admin
  createBook
);
```

---

## DIAGNÓSTICO RÁPIDO

### Error: "Cannot read property 'findByPk' of undefined"
```
Causa: Sequelize no está importado o BD no sincronizada
Solución: 
  1. await sequelize.sync()
  2. const Model = require('./models/Model')
```

### Error: "Token inválido o expirado"
```
Causa: Token mal formateado, expirado, o JWT_SECRET diferente
Solución:
  1. Verificar formato "Bearer ..."
  2. Verificar JWT_SECRET en .env
  3. Regenerar token
```

### Error: "CORS error"
```
Causa: Falta middlewares CORS
Solución: app.use(cors()) ANTES de rutas
```

### Error: "Email already exists"
```
Causa: Intentar crear usuario con email duplicado
Solución: Siempre verificar unique: true en modelo +
          validar antes de create()
```

### Error: "TypeError: res.json is not a function"
```
Causa: Falta app.use(express.json())
Solución: Añadir middlewares ANTES de rutas
```

---

## CHECKLIST DEL EXAMEN 🎯

Antes de entregar:

- [ ] ✅ `.env` existe con `JWT_SECRET`, `DATABASE`, `PORT`
- [ ] ✅ `sequelize.sync({ alter: true })` llamado en startup
- [ ] ✅ Passwords con hash (bcryptjs)
- [ ] ✅ Passwords excluidas en responses
- [ ] ✅ Validadores están en rutas
- [ ] ✅ `handleValidationErrors` middleware presente
- [ ] ✅ Tokens con Bearer format
- [ ] ✅ CORS habilitado
- [ ] ✅ Error handler global a final de index.js
- [ ] ✅ Rutas registradas con `app.use()`
- [ ] ✅ Relaciones Usuario-Recurso definidas
- [ ] ✅ Admin requiere `verifyToken` + `verifyAdmin`
- [ ] ✅ Documentación Swagger funcionando
- [ ] ✅ GET públicos, POST/PUT/DELETE admin
- [ ] ✅ Datos de ejemplo en startup

---

## TIPS GANAR TIEMPO

1. **Copiar estructura de Model_A**: Primera 10 min, ganadas.

2. **Plantillas en ESTUDIO**: Copiar validadores, middleware, controladores base.

3. **Diferencias clave a cambiar**:
   - Campo en modelo (type, datatype)
   - Nombre entidad (Book, Event, Product)
   - Datos de ejemplo
   - Validadores específicos

4. **No reinventar la rueda**:
   ```javascript
   // Todas usan este mismo patrón:
   const entityController = async (req, res) => {
     try {
       const data = await Entity.findAll({ include: [...] });
       return res.json(data);
     } catch (error) {
       return res.status(500).json({ error: 'Error' });
     }
   };
   ```

5. **Swagger**: Copiar spec base, cambiar título + descripción.

6. **Primero que funcione, luego refactoriza**:
   - Endpoints GET/POST/PUT/DELETE básicos
   - Luego validaciones avanzadas
   - Luego documentación bonita

---

## RESPUESTAS RÁPIDAS

**¿Cómo genero un token?**
```javascript
const token = jwt.sign(
  { id: user.id, isAdmin: user.isAdmin },
  process.env.JWT_SECRET,
  { expiresIn: '8h' }
);
```

**¿Cómo verifico un token?**
```javascript
const decoded = jwt.verify(token, process.env.JWT_SECRET);
```

**¿Cómo hago hash de password?**
```javascript
const hashedPassword = await bcrypt.hash(password, 10);
```

**¿Cómo valido email?**
```javascript
body('email').isEmail().withMessage('Email no válido')
```

**¿Cómo hago relación One-to-Many?**
```javascript
User.hasMany(Book);
Book.belongsTo(User);
```

**¿Cómo excluyo password en query?**
```javascript
attributes: { exclude: ['password'] }
```

**¿Cómo filtro por enum?**
```javascript
where: { status: 'publicado' }
```

**¿Cómo ordeno por fecha?**
```javascript
order: [['createdAt', 'DESC']]
```

**¿Cómo actualizo solo algunos campos?**
```javascript
const updateData = {};
if (field1) updateData.field1 = field1;
await user.update(updateData);
```

**¿Cómo valido que sea admin?**
```javascript
if (!req.user.isAdmin) return res.status(403).json({ error: 'Forbidden' });
```
