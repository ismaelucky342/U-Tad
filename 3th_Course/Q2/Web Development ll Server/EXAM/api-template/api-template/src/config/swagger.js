// src/config/swagger.js
const swaggerJsdoc = require('swagger-jsdoc');

// ============================================================
// CAMBIA ESTO: Título, descripción y versión de tu API
// ============================================================
const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'API de Datos Meteorológicos',   // <-- Cambia el título
      version: '1.0.0',
      description: 'API REST para gestión de datos meteorológicos y usuarios',
    },
    servers: [
      { url: 'http://localhost:3000', description: 'Servidor de desarrollo' },
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
  // Escanea estos archivos en busca de comentarios JSDoc con @swagger
  apis: ['./src/routes/*.js'],
};

module.exports = swaggerJsdoc(options);
