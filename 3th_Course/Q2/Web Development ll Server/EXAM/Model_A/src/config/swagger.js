const swaggerJsdoc = require('swagger-jsdoc');

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Weather API',
      version: '1.0.0',
      description: `
API para la publicación y gestión de datos meteorológicos.

## Autenticación
Esta API usa **JWT Bearer Token**. Para acceder a los endpoints protegidos:
1. Haz login en \`POST /users/login\` con tus credenciales.
2. Copia el \`token\` de la respuesta.
3. Haz clic en **Authorize** (arriba a la derecha) e introduce: \`Bearer <tu_token>\`.

## Permisos
- **Público**: Lectura de datos meteorológicos (\`GET /data\`, \`GET /data/:id\`).
- **Admin**: Todas las demás operaciones requieren un usuario autenticado con \`isAdmin: true\`.

## Usuario administrador inicial
- Email: \`admin@weather.com\`
- Password: \`admin123\`
      `,
      contact: {
        name: 'Soporte Weather API',
        email: 'soporte@weatherapi.com',
      },
    },
    servers: [
      {
        url: 'http://localhost:3000/api',
        description: 'Servidor de desarrollo',
      },
    ],
    components: {
      securitySchemes: {
        bearerAuth: {
          type: 'http',
          scheme: 'bearer',
          bearerFormat: 'JWT',
          description: 'Introduce tu JWT token obtenido del endpoint de login.',
        },
      },
      schemas: {
        User: {
          type: 'object',
          properties: {
            id: { type: 'integer', example: 1 },
            username: { type: 'string', example: 'admin_weather' },
            email: { type: 'string', format: 'email', example: 'admin@weather.com' },
            fullName: { type: 'string', example: 'Administrador Sistema' },
            isAdmin: { type: 'boolean', example: true },
            createdAt: { type: 'string', format: 'date-time' },
            updatedAt: { type: 'string', format: 'date-time' },
          },
        },
        WeatherData: {
          type: 'object',
          properties: {
            id: { type: 'integer', example: 1 },
            date: { type: 'string', format: 'date', example: '2024-03-15' },
            userId: { type: 'integer', example: 1 },
            latitude: { type: 'number', example: 40.4168 },
            longitude: { type: 'number', example: -3.7038 },
            rainProbability: { type: 'number', example: 75.5 },
            precipitation: { type: 'number', example: 12.3 },
            windSpeed: { type: 'number', example: 45.2 },
            tempMin: { type: 'number', example: 8.5 },
            tempMax: { type: 'number', example: 18.2 },
            tempCurrent: { type: 'number', example: 13.4 },
            createdAt: { type: 'string', format: 'date-time' },
            updatedAt: { type: 'string', format: 'date-time' },
          },
        },
        Error: {
          type: 'object',
          properties: {
            error: { type: 'string', example: 'Mensaje de error.' },
            details: {
              type: 'array',
              items: {
                type: 'object',
                properties: {
                  field: { type: 'string' },
                  message: { type: 'string' },
                },
              },
            },
          },
        },
      },
    },
  },
  apis: ['./src/routes/*.js'],
};

const swaggerSpec = swaggerJsdoc(options);

module.exports = swaggerSpec;
