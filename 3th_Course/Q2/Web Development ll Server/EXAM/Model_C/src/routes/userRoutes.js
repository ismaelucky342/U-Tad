const express = require('express');
const router = express.Router();
const { verifyToken, verifyAdmin } = require('../middleware/auth');
const { handleValidationErrors } = require('../middleware/validationHandler');
const { login, getAllUsers, getUserById, createUser, updateUser, deleteUser } = require('../controllers/userController');
const { loginValidators, createUserValidators, updateUserValidators, idParamValidator } = require('../validators/userValidators');

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
 *             required: [email, password]
 *             properties:
 *               email: { type: string, format: email, example: "admin@events.com" }
 *               password: { type: string, example: "admin123" }
 *     responses:
 *       200: { description: "Login correcto" }
 *       401: { description: "Credenciales incorrectas" }
 */
router.post('/login', loginValidators, handleValidationErrors, login);
router.get('/', verifyToken, verifyAdmin, getAllUsers);
router.get('/:id', verifyToken, verifyAdmin, idParamValidator, handleValidationErrors, getUserById);
router.post('/', verifyToken, verifyAdmin, createUserValidators, handleValidationErrors, createUser);
router.put('/:id', verifyToken, verifyAdmin, updateUserValidators, handleValidationErrors, updateUser);
router.delete('/:id', verifyToken, verifyAdmin, idParamValidator, handleValidationErrors, deleteUser);

module.exports = router;
