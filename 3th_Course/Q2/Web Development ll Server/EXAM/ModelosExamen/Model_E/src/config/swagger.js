const swaggerJsdoc = require('swagger-jsdoc');
const options = {
  definition: {
    openapi: '3.0.0',
    info: { title: 'Workouts API', version: '1.0.0', description: 'API de actividad física. Email: admin@workouts.com / Pass: admin123' },
    servers: [{ url: 'http://localhost:3000/api' }],
    components: { securitySchemes: { bearerAuth: { type: 'http', scheme: 'bearer', bearerFormat: 'JWT' } } },
  },
  apis: ['./src/routes/*.js'],
};
module.exports = swaggerJsdoc(options);
