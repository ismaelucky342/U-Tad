// src/routes/userRoutes.js
const express = require('express');
const router = express.Router();
const { verifyToken, isAdmin, isOwnerOrAdmin } = require('../middleware/auth');
const handleValidation = require('../middleware/handleValidation');
const { validateRegister, validateUpdateUser, validateLogin } = require('../validators/userValidators');
const {
  login, register, getAllUsers, getUserById, createUser, updateUser, deleteUser,
} = require('../controllers/userController');

/**
 * @swagger
 * tags:
 *   name: Users
 *   description: Gestión de usuarios y autenticación
 */

/**
 * @swagger
 * /users/login:
 *   post:
 *     summary: Login (admin y client)
 *     tags: [Users]
 *     security: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required: [email, password]
 *             properties:
 *               email:
 *                 type: string
 *                 example: admin@shop.com
 *               password:
 *                 type: string
 *                 example: password123
 *     responses:
 *       200:
 *         description: Login exitoso, devuelve JWT
 *       401:
 *         description: Credenciales incorrectas
 */
router.post('/login', validateLogin, handleValidation, login);

/**
 * @swagger
 * /users/register:
 *   post:
 *     summary: Registro público (crea cuenta de cliente)
 *     tags: [Users]
 *     security: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required: [username, email, fullName, password]
 *             properties:
 *               username:
 *                 type: string
 *               email:
 *                 type: string
 *               fullName:
 *                 type: string
 *               password:
 *                 type: string
 *               phone:
 *                 type: string
 *               address:
 *                 type: string
 *     responses:
 *       201:
 *         description: Cuenta de cliente creada
 *       409:
 *         description: Email ya registrado
 */
router.post('/register', validateRegister, handleValidation, register);

/**
 * @swagger
 * /users:
 *   get:
 *     summary: Listar todos los usuarios (solo admin)
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Lista de usuarios
 *       403:
 *         description: Solo administradores
 */
router.get('/', verifyToken, isAdmin, getAllUsers);

/**
 * @swagger
 * /users/{id}:
 *   get:
 *     summary: Ver usuario por ID (admin ve cualquiera; cliente solo el suyo)
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Datos del usuario
 *       403:
 *         description: No autorizado
 *       404:
 *         description: Usuario no encontrado
 */
router.get('/:id', verifyToken, isOwnerOrAdmin, getUserById);

/**
 * @swagger
 * /users:
 *   post:
 *     summary: Crear usuario con cualquier rol (solo admin)
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required: [username, email, fullName, password]
 *             properties:
 *               username:
 *                 type: string
 *               email:
 *                 type: string
 *               fullName:
 *                 type: string
 *               password:
 *                 type: string
 *               phone:
 *                 type: string
 *               address:
 *                 type: string
 *               role:
 *                 type: string
 *                 enum: [admin, client]
 *     responses:
 *       201:
 *         description: Usuario creado
 */
router.post('/', verifyToken, isAdmin, validateRegister, handleValidation, createUser);

/**
 * @swagger
 * /users/{id}:
 *   put:
 *     summary: Actualizar usuario (admin cualquiera; cliente solo el suyo)
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     requestBody:
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               fullName:
 *                 type: string
 *               phone:
 *                 type: string
 *               address:
 *                 type: string
 *               password:
 *                 type: string
 *     responses:
 *       200:
 *         description: Usuario actualizado
 */
router.put('/:id', verifyToken, isOwnerOrAdmin, validateUpdateUser, handleValidation, updateUser);

/**
 * @swagger
 * /users/{id}:
 *   delete:
 *     summary: Desactivar usuario (solo admin)
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Usuario desactivado
 */
router.delete('/:id', verifyToken, isAdmin, deleteUser);

module.exports = router;
