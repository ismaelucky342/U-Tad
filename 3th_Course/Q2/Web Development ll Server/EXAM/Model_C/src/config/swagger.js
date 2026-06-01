const swaggerJsdoc = require('swagger-jsdoc');

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Events API',
      version: '1.0.0',
      description: 'API para la gestión de eventos culturales y de ocio.\n\n## Autenticación\nUsa JWT Bearer Token. Email: admin@events.com / Password: admin123',
    },
    servers: [{ url: 'http://localhost:3000/api', description: 'Servidor de desarrollo' }],
    components: {
      securitySchemes: {
        bearerAuth: { type: 'http', scheme: 'bearer', bearerFormat: 'JWT' },
      },
    },
  },
  apis: ['./src/routes/*.js'],
};

module.exports = swaggerJsdoc(options);
