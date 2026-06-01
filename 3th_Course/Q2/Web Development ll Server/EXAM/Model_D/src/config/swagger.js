const swaggerJsdoc = require('swagger-jsdoc');
const options = {
  definition: {
    openapi: '3.0.0',
    info: { title: 'Products API', version: '1.0.0', description: 'API de gestión de productos e-commerce. Email: admin@products.com / Pass: admin123' },
    servers: [{ url: 'http://localhost:3000/api', description: 'Servidor de desarrollo' }],
    components: { securitySchemes: { bearerAuth: { type: 'http', scheme: 'bearer', bearerFormat: 'JWT' } } },
  },
  apis: ['./src/routes/*.js'],
};
module.exports = swaggerJsdoc(options);
