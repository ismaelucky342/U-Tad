const express = require('express');
const router = express.Router();

const { verifyToken, verifyAdmin } = require('../middleware/auth');
const { handleValidationErrors } = require('../middleware/validationHandler');
const {
  getAllBooks,
  getBookById,
  createBook,
  updateBook,
  deleteBook,
} = require('../controllers/bookController');
const {
  createBookValidators,
  updateBookValidators,
  idParamValidator,
} = require('../validators/bookValidators');

/**
 * @swagger
 * tags:
 *   name: Books
 *   description: Gestión de libros
 */

/**
 * @swagger
 * /books:
 *   get:
 *     summary: Obtener todos los libros
 *     tags: [Books]
 *     responses:
 *       200:
 *         description: Lista de libros.
 */
router.get('/', getAllBooks);

/**
 * @swagger
 * /books/{id}:
 *   get:
 *     summary: Obtener libro por ID
 *     tags: [Books]
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *         description: ID del libro
 *     responses:
 *       200:
 *         description: Datos del libro.
 *       404:
 *         description: Libro no encontrado.
 */
router.get('/:id', idParamValidator, handleValidationErrors, getBookById);

/**
 * @swagger
 * /books:
 *   post:
 *     summary: Crear nuevo libro (solo admin)
 *     tags: [Books]
 *     security:
 *       - bearerAuth: []
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required:
 *               - title
 *               - author
 *               - isbn
 *               - genre
 *               - publicationYear
 *               - pages
 *             properties:
 *               title:
 *                 type: string
 *                 example: "1984"
 *               author:
 *                 type: string
 *                 example: "George Orwell"
 *               isbn:
 *                 type: string
 *                 example: "978-0451524935"
 *               genre:
 *                 type: string
 *                 example: "Distopía"
 *               publicationYear:
 *                 type: integer
 *                 example: 1949
 *               pages:
 *                 type: integer
 *                 example: 328
 *               available:
 *                 type: boolean
 *                 example: true
 *               synopsis:
 *                 type: string
 *                 example: "Una novela sobre un régimen totalitario."
 *     responses:
 *       201:
 *         description: Libro creado correctamente.
 *       401:
 *         description: Token no proporcionado o inválido.
 *       403:
 *         description: Se requieren permisos de administrador.
 */
router.post('/', verifyToken, verifyAdmin, createBookValidators, handleValidationErrors, createBook);

/**
 * @swagger
 * /books/{id}:
 *   put:
 *     summary: Actualizar libro (solo admin)
 *     tags: [Books]
 *     security:
 *       - bearerAuth: []
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *         description: ID del libro
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               title:
 *                 type: string
 *               author:
 *                 type: string
 *               isbn:
 *                 type: string
 *               genre:
 *                 type: string
 *               publicationYear:
 *                 type: integer
 *               pages:
 *                 type: integer
 *               available:
 *                 type: boolean
 *               synopsis:
 *                 type: string
 *     responses:
 *       200:
 *         description: Libro actualizado correctamente.
 *       401:
 *         description: Token no proporcionado o inválido.
 *       403:
 *         description: Se requieren permisos de administrador.
 *       404:
 *         description: Libro no encontrado.
 */
router.put('/:id', verifyToken, verifyAdmin, updateBookValidators, handleValidationErrors, updateBook);

/**
 * @swagger
 * /books/{id}:
 *   delete:
 *     summary: Eliminar libro (solo admin)
 *     tags: [Books]
 *     security:
 *       - bearerAuth: []
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *         description: ID del libro
 *     responses:
 *       200:
 *         description: Libro eliminado correctamente.
 *       401:
 *         description: Token no proporcionado o inválido.
 *       403:
 *         description: Se requieren permisos de administrador.
 *       404:
 *         description: Libro no encontrado.
 */
router.delete('/:id', verifyToken, verifyAdmin, idParamValidator, handleValidationErrors, deleteBook);

module.exports = router;
