# 🔐 AUTENTICACIÓN JWT - COPIA Y PEGA

## LOGIN Y GENERACIÓN DE TOKENS

```javascript
// ─── src/controllers/userController.js ────────────────────────

const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const User = require('../models/User');
const { validationResult } = require('express-validator');

// Generar JWT
const generateToken = (user) => {
  return jwt.sign(
    { id: user.id, email: user.email, isAdmin: user.isAdmin },
    process.env.JWT_SECRET,
    { expiresIn: '8h' }  // Token válido 8 horas
  );
};

// REGISTRO: Crear usuario nuevo
const registerUser = async (req, res) => {
  const { username, email, password, fullName } = req.body;

  try {
    // Buscar si existe
    const existingUser = await User.findOne({ where: { email } });
    if (existingUser) {
      return res.status(400).json({ error: 'Este email ya está registrado.' });
    }

    // Hash de password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Crear usuario
    const newUser = await User.create({
      username,
      email,
      password: hashedPassword,
      fullName,
      isAdmin: false,  // Por defecto no es admin
    });

    // Generar token
    const token = generateToken(newUser);

    return res.status(201).json({
      message: 'Usuario registrado correctamente.',
      token,
      user: {
        id: newUser.id,
        username: newUser.username,
        email: newUser.email,
        fullName: newUser.fullName,
        isAdmin: newUser.isAdmin,
      },
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

// LOGIN: Autenticar usuario
const loginUser = async (req, res) => {
  const { email, password } = req.body;

  try {
    // Buscar usuario por email
    const user = await User.findOne({ where: { email } });
    if (!user) {
      return res.status(400).json({ error: 'Email o contraseña incorrectos.' });
    }

    // Verificar contraseña
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(400).json({ error: 'Email o contraseña incorrectos.' });
    }

    // Generar token
    const token = generateToken(user);

    return res.status(200).json({
      message: 'Login exitoso.',
      token,
      user: {
        id: user.id,
        username: user.username,
        email: user.email,
        fullName: user.fullName,
        isAdmin: user.isAdmin,
      },
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

// GET PROFILE: Obtener perfil del usuario autenticado
const getUserProfile = async (req, res) => {
  try {
    const user = await User.findByPk(req.user.id, {
      attributes: { exclude: ['password'] },
    });

    return res.status(200).json({
      message: 'Perfil obtenido correctamente.',
      user,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

// GET ALL USERS (solo admin)
const getAllUsers = async (req, res) => {
  try {
    const users = await User.findAll({
      attributes: { exclude: ['password'] },
      order: [['createdAt', 'DESC']],
    });

    return res.status(200).json({
      total: users.length,
      users,
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

// UPDATE PROFILE: Actualizar perfil del usuario autenticado
const updateUserProfile = async (req, res) => {
  const { fullName, username } = req.body;

  try {
    const user = await User.findByPk(req.user.id);

    if (fullName) user.fullName = fullName;
    if (username) {
      // Verificar que no exista otro usuario con ese username
      const existingUser = await User.findOne({
        where: { username, id: { [sequelize.Op.ne]: user.id } },
      });
      if (existingUser) {
        return res.status(400).json({ error: 'Este username ya existe.' });
      }
      user.username = username;
    }

    await user.save();

    return res.status(200).json({
      message: 'Perfil actualizado correctamente.',
      user: {
        id: user.id,
        username: user.username,
        email: user.email,
        fullName: user.fullName,
        isAdmin: user.isAdmin,
      },
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

// CHANGE PASSWORD: Cambiar contraseña
const changePassword = async (req, res) => {
  const { oldPassword, newPassword } = req.body;

  try {
    const user = await User.findByPk(req.user.id);

    // Verificar contraseña antigua
    const isPasswordValid = await bcrypt.compare(oldPassword, user.password);
    if (!isPasswordValid) {
      return res.status(400).json({ error: 'Contraseña antigua incorrecta.' });
    }

    // Hash de nueva contraseña
    const hashedPassword = await bcrypt.hash(newPassword, 10);
    user.password = hashedPassword;
    await user.save();

    return res.status(200).json({
      message: 'Contraseña actualizada correctamente.',
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

// DELETE ACCOUNT: Eliminar cuenta del usuario
const deleteUserAccount = async (req, res) => {
  const { password } = req.body;

  try {
    const user = await User.findByPk(req.user.id);

    // Verificar contraseña
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(400).json({ error: 'Contraseña incorrecta.' });
    }

    await user.destroy();

    return res.status(200).json({
      message: 'Cuenta eliminada correctamente.',
    });
  } catch (error) {
    return res.status(500).json({ error: 'Error interno del servidor.' });
  }
};

module.exports = {
  registerUser,
  loginUser,
  getUserProfile,
  getAllUsers,
  updateUserProfile,
  changePassword,
  deleteUserAccount,
};
```

---

## RUTAS DE AUTENTICACIÓN

```javascript
// ─── src/routes/userRoutes.js ────────────────────┬──────────

const express = require('express');
const router = express.Router();
const { body, validationResult } = require('express-validator');

const { verifyToken, verifyAdmin } = require('../middleware/auth');
const { handleValidationErrors } = require('../middleware/validationHandler');

const {
  registerUser,
  loginUser,
  getUserProfile,
  getAllUsers,
  updateUserProfile,
  changePassword,
  deleteUserAccount,
} = require('../controllers/userController');

// ─── VALIDADORES ──────────────────────────────────
const registerValidators = [
  body('username')
    .trim()
    .notEmpty().withMessage('Username es obligatorio.')
    .isLength({ min: 3, max: 50 }).withMessage('Entre 3 y 50 caracteres.'),
  body('email')
    .isEmail().withMessage('Email no válido.')
    .normalizeEmail(),
  body('password')
    .isLength({ min: 6 }).withMessage('Mínimo 6 caracteres.'),
  body('fullName')
    .trim()
    .notEmpty().withMessage('Nombre completo es obligatorio.')
    .isLength({ min: 3, max: 100 }).withMessage('Entre 3 y 100 caracteres.'),
];

const loginValidators = [
  body('email')
    .isEmail().withMessage('Email no válido.')
    .normalizeEmail(),
  body('password')
    .notEmpty().withMessage('Contraseña es obligatoria.'),
];

const changePasswordValidators = [
  body('oldPassword')
    .notEmpty().withMessage('Contraseña antigua es obligatoria.'),
  body('newPassword')
    .isLength({ min: 6 }).withMessage('Nueva contraseña mínimo 6 caracteres.'),
];

// ─── RUTAS PÚBLICAS ───────────────────────────────

/**
 * @swagger
 * /users/register:
 *   post:
 *     summary: Registrar nuevo usuario
 *     tags: [Auth]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             properties:
 *               username: { type: string, example: "usuario1" }
 *               email: { type: string, example: "user@example.com" }
 *               password: { type: string, example: "password123" }
 *               fullName: { type: string, example: "Usuario Uno" }
 *     responses:
 *       201: { description: "Usuario registrado, devuelve token JWT" }
 *       400: { description: "Email ya registrado o datos inválidos" }
 */
router.post('/register', registerValidators, handleValidationErrors, registerUser);

/**
 * @swagger
 * /users/login:
 *   post:
 *     summary: Login de usuario (obtener token JWT)
 *     tags: [Auth]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             properties:
 *               email: { type: string, example: "user@example.com" }
 *               password: { type: string, example: "password123" }
 *     responses:
 *       200: { description: "Login exitoso, devuelve token JWT" }
 *       400: { description: "Email o contraseña incorrectos" }
 */
router.post('/login', loginValidators, handleValidationErrors, loginUser);

// ─── RUTAS PROTEGIDAS (requieren token) ───────────

/**
 * @swagger
 * /users/profile:
 *   get:
 *     summary: Obtener perfil del usuario autenticado
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200: { description: "Perfil del usuario" }
 *       401: { description: "Token no proporcionado o inválido" }
 */
router.get('/profile', verifyToken, getUserProfile);

/**
 * @swagger
 * /users/profile:
 *   put:
 *     summary: Actualizar perfil del usuario
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       content:
 *         application/json:
 *           schema:
 *             properties:
 *               fullName: { type: string }
 *               username: { type: string }
 */
router.put('/profile', verifyToken, updateUserProfile);

/**
 * @swagger
 * /users/change-password:
 *   post:
 *     summary: Cambiar contraseña del usuario
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             properties:
 *               oldPassword: { type: string }
 *               newPassword: { type: string }
 */
router.post('/change-password', verifyToken, changePasswordValidators, handleValidationErrors, changePassword);

/**
 * @swagger
 * /users/delete-account:
 *   delete:
 *     summary: Eliminar cuenta del usuario
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             properties:
 *               password: { type: string, description: "Contraseña para confirmar" }
 */
router.delete('/delete-account', verifyToken, deleteUserAccount);

// ─── RUTAS ADMIN ──────────────────────────────────

/**
 * @swagger
 * /users:
 *   get:
 *     summary: Obtener todos los usuarios (solo admin)
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200: { description: "Lista de usuarios" }
 *       403: { description: "No es administrador" }
 */
router.get('/', verifyToken, verifyAdmin, getAllUsers);

module.exports = router;
```

---

## .ENV REQUERIDO

```
PORT=3000
DATABASE=database.sqlite
JWT_SECRET=tu_secreto_super_seguro_aqui_1234567890
NODE_ENV=development
```

---

## FLUJO DE AUTENTICACIÓN COMPLETO

```
1. USUARIO SE REGISTRA
   POST /api/users/register
   Body: { username, email, password, fullName }
   ↓
   Response: { token: "JWT...", user: {...} }

2. USUARIO HACE LOGIN
   POST /api/users/login
   Body: { email, password }
   ↓
   Response: { token: "JWT...", user: {...} }

3. USUARIO ACCEDE A RECURSO PROTEGIDO
   PUT/POST/DELETE /api/books
   Header: Authorization: Bearer JWT...
   ↓
   Middleware verifyToken extraerá el token

4. MIDDLEWARE VERIFICA TOKEN
   - Lee "Bearer JWT..." del header
   - Verifica validez con JWT_SECRET
   - Si válido, extrae { id, email, isAdmin }
   - Si invalid/expired, devuelve 401

5. SI ES ADMIN, CONTINÚA
   verifyAdmin chequea req.user.isAdmin === true
   ↓
   Si no es admin → 403 Forbidden
   Si es admin → Ejecuta controlador
```

---

## ERRORES COMUNES EN AUTENTICACIÓN

1. ❌ **Token sin Bearer**: 
   - ❌ Header: `Authorization: EYJABC...`
   - ✅ Header: `Authorization: Bearer EYJABC...`

2. ❌ **JWT_SECRET no definitido**:
   - Resultado: `Cannot read property 'verify' of undefined`
   - Solución: Verificar `.env` tiene `JWT_SECRET=algo`

3. ❌ **Password sin hash en BD**:
   - ❌ `user.password = req.body.password;`
   - ✅ `user.password = await bcrypt.hash(req.body.password, 10);`

4. ❌ **Devolviendo password en JSON**:
   - ❌ `return res.json(user);` // Incluye password!!
   - ✅ `attributes: { exclude: ['password'] }` en findAll()

5. ❌ **Token enviado sin Bearer en cliente**:
   ```javascript
   // ❌ INCORRECTO
   headers: { 'Authorization': token }
   
   // ✅ CORRECTO
   headers: { 'Authorization': 'Bearer ' + token }
   ```

---

## TESTING CON CURL

```bash
# 1. REGISTRAR
curl -X POST http://localhost:3000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username":"admin_yourapi",
    "email":"admin@example.com",
    "password":"admin123",
    "fullName":"Administrador Sistema"
  }'

# Response:
# {
#   "message": "Usuario registrado correctamente.",
#   "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#   "user": { ... }
# }

# 2. LOGIN (sin existencia previa, si usas los mismos datos)
curl -X POST http://localhost:3000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "email":"admin@example.com",
    "password":"admin123"
  }'

# Copiar el token de la respuesta

# 3. USAR TOKEN PARA ACCEDER A RECURSO PROTEGIDO
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

curl -X GET http://localhost:3000/api/users/profile \
  -H "Authorization: Bearer $TOKEN"

# 4. CAMBIAR CONTRASEÑA
curl -X POST http://localhost:3000/api/users/change-password \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "oldPassword":"admin123",
    "newPassword":"newPassword456"
  }'

# 5. ACTUALIZAR PERFIL
curl -X PUT http://localhost:3000/api/users/profile \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "fullName":"Nuevo Nombre",
    "username":"new_username"
  }'

# 6. DELETE (requiere password)
curl -X DELETE http://localhost:3000/api/users/delete-account \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"password":"newPassword456"}'
```

---

## VERSIÓN SIMPLIFICADA PARA EL EXAMEN

Si en el examen necesitas copiar todo súper rápido:

```javascript
// LOGIN RÁPIDO
const loginUser = async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await User.findOne({ where: { email } });
    if (!user || !(await bcrypt.compare(password, user.password))) {
      return res.status(400).json({ error: 'Credenciales inválidas' });
    }
    const token = jwt.sign(
      { id: user.id, isAdmin: user.isAdmin },
      process.env.JWT_SECRET,
      { expiresIn: '8h' }
    );
    return res.json({ token, user: { id: user.id, email: user.email, isAdmin: user.isAdmin } });
  } catch (error) {
    return res.status(500).json({ error: 'Error' });
  }
};

// MIDDLEWARE VERIFICACIÓN
const verifyToken = async (req, res, next) => {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = await User.findByPk(decoded.id);
    next();
  } catch {
    return res.status(401).json({ error: 'Invalid token' });
  }
};

const verifyAdmin = (req, res, next) => {
  if (!req.user?.isAdmin) return res.status(403).json({ error: 'Forbidden' });
  next();
};
```
