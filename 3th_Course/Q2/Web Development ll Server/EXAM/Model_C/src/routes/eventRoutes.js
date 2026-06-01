const express = require('express');
const router = express.Router();
const { verifyToken, verifyAdmin } = require('../middleware/auth');
const { handleValidationErrors } = require('../middleware/validationHandler');
const { getAllEvents, getEventById, createEvent, updateEvent, deleteEvent } = require('../controllers/eventController');
const { createEventValidators, updateEventValidators, idParamValidator } = require('../validators/eventValidators');

/**
 * @swagger
 * /events:
 *   get:
 *     summary: Obtener todos los eventos
 *     tags: [Events]
 *     responses:
 *       200: { description: "Lista de eventos" }
 */
router.get('/', getAllEvents);
router.get('/:id', idParamValidator, handleValidationErrors, getEventById);
router.post('/', verifyToken, verifyAdmin, createEventValidators, handleValidationErrors, createEvent);
router.put('/:id', verifyToken, verifyAdmin, updateEventValidators, handleValidationErrors, updateEvent);
router.delete('/:id', verifyToken, verifyAdmin, idParamValidator, handleValidationErrors, deleteEvent);

module.exports = router;
