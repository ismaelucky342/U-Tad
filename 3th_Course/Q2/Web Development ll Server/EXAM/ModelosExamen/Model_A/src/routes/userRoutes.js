const express = require('express');
const router = express.Router();

const { verifyToken, verifyAdmin } = require('../middleware/auth');
const { handleValidationErrors } = require('../middleware/validationHandler');
const {
  login,
  getAllUsers,
  getUserById,
  createUser,
  updateUser,
  deleteUser,
} = require('../controllers/userController');
const {
  loginValidators,
  createUserValidators,
  updateUserValidators,
  idParamValidator,
} = require('../validators/userValidators');

/**
 * @swagger
 * tags:
 *   name: Users
 *   description: Gestión de usuarios
 */

/**
 * @swagger
 * /users/login:
 *   post:
 *     summary: Iniciar sesión
 *     tags: [Users]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required:
 *               - email
 *               - password
 *             properties:
 *               email:
 *                 type: string
 *                 format: email
 *                 example: admin@weather.com
 *               password:
 *                 type: string
 *                 example: admin123
 *     responses:
 *       200:
 *         description: Login correcto. Retorna JWT.
 *       400:
 *         description: Datos de entrada inválidos.
 *       401:
 *         description: Credenciales incorrectas.
 */
router.post('/login', loginValidators, handleValidationErrors, login);

/**
 * @swagger
 * /users:
 *   get:
 *     summary: Obtener todos los usuarios
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     responses:
 *       200:
 *         description: Lista de usuarios.
 *       401:
 *         description: Token no proporcionado o inválido.
 *       403:
 *         description: Se requieren permisos de administrador.
 */
router.get('/', verifyToken, verifyAdmin, getAllUsers);

/**
 * @swagger
 * /users/{id}:
 *   get:
 *     summary: Obtener usuario por ID
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *         description: ID del usuario
 *     responses:
 *       200:
 *         description: Datos del usuario.
 *       401:
 *         description: Token no proporcionado o inválido.
 *       403:
 *         description: Se requieren permisos de administrador.
 *       404:
 *         description: Usuario no encontrado.
 */
router.get('/:id', verifyToken, verifyAdmin, idParamValidator, handleValidationErrors, getUserById);

/**
 * @swagger
 * /users:
 *   post:
 *     summary: Crear nuevo usuario
 *     tags: [Users]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required:
 *               - username
 *               - email
 *               - fullName
 *               - password
 *             properties:
 *               username:
 *                 type: string
 *                 example: juan_garcia
 *               email:
 *                 type: string
 *                 format: email
 *                 example: juan@example.com
 *               fullName:
 *                 type: string
 *                 example: Juan García López
 *               password:
 *                 type: string
 *                 example: miPassword123
 *               isAdmin:
 *                 type: boolean
 *                 example: false
 *     responses:
 *       201:
 *         description: Usuario creado correctamente.
 *       400:
 *         description: Datos de entrada inválidos.
 *       401:
 *         description: Token no proporcionado o inválido.
 *       403:
 *         description: Se requieren permisos de administrador.
 *       409:
 *         description: El usuario ya existe.
 */
router.post('/', verifyToken, verifyAdmin, createUserValidators, handleValidationErrors, createUser);

/**
 * @swagger
 * /users/{id}:
 *   put:
 *     summary: Actualizar usuario
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
 *               username:
 *                 type: string
 *               email:
 *                 type: string
 *               fullName:
 *                 type: string
 *               password:
 *                 type: string
 *               isAdmin:
 *                 type: boolean
 *     responses:
 *       200:
 *         description: Usuario actualizado correctamente.
 *       400:
 *         description: Datos inválidos.
 *       401:
 *         description: Token inválido.
 *       403:
 *         description: Sin permisos de administrador.
 *       404:
 *         description: Usuario no encontrado.
 */
router.put('/:id', verifyToken, verifyAdmin, updateUserValidators, handleValidationErrors, updateUser);

/**
 * @swagger
 * /users/{id}:
 *   delete:
 *     summary: Eliminar usuario
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
 *         description: Usuario eliminado correctamente.
 *       401:
 *         description: Token inválido.
 *       403:
 *         description: Sin permisos de administrador.
 *       404:
 *         description: Usuario no encontrado.
 */
router.delete('/:id', verifyToken, verifyAdmin, idParamValidator, handleValidationErrors, deleteUser);

module.exports = router;
