const swaggerJsdoc = require('swagger-jsdoc');

const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Library API',
      version: '1.0.0',
      description: `
API para la gestión de una biblioteca digital.

## Autenticación
Esta API usa **JWT Bearer Token**. Para acceder a los endpoints protegidos:
1. Haz login en \`POST /users/login\` con tus credenciales.
2. Copia el \`token\` de la respuesta.
3. Haz clic en **Authorize** (arriba a la derecha) e introduce: \`Bearer <tu_token>\`.

## Permisos
- **Público**: Lectura de libros (\`GET /books\`, \`GET /books/:id\`).
- **Admin**: Todas las demás operaciones requieren un usuario autenticado con \`isAdmin: true\`.

## Usuario administrador inicial
- Email: \`admin@library.com\`
- Password: \`admin123\`
      `,
      contact: {
        name: 'Soporte Library API',
        email: 'soporte@libraryapi.com',
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
            username: { type: 'string', example: 'admin_library' },
            email: { type: 'string', format: 'email', example: 'admin@library.com' },
            fullName: { type: 'string', example: 'Administrador Biblioteca' },
            isAdmin: { type: 'boolean', example: true },
            createdAt: { type: 'string', format: 'date-time' },
            updatedAt: { type: 'string', format: 'date-time' },
          },
        },
        Book: {
          type: 'object',
          properties: {
            id: { type: 'integer', example: 1 },
            title: { type: 'string', example: '1984' },
            author: { type: 'string', example: 'George Orwell' },
            isbn: { type: 'string', example: '978-0451524935' },
            genre: { type: 'string', example: 'Distopía' },
            publicationYear: { type: 'integer', example: 1949 },
            pages: { type: 'integer', example: 328 },
            available: { type: 'boolean', example: true },
            synopsis: { type: 'string', example: 'Una novela sobre un régimen totalitario.' },
            userId: { type: 'integer', example: 1 },
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
