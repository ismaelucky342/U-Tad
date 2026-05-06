# BurgerPrince API - AEC3

## Descripción

API REST completa de hamburguesería con las siguientes características:

✅ **Base de datos persistente** con MongoDB
✅ **Autenticación y autorización** con JWT
✅ **Validaciones** con express-validator
✅ **CRUD de Productos** con modelo completo
✅ **CRUD de Usuarios** con roles y permisos
✅ **Sistema de Pedidos** mejorado
✅ **Documentación Swagger** automática
✅ **Unit Tests** con Jest

## Instalación

### Requisitos previos
- Node.js (v14 o superior)
- MongoDB (local o Atlas)
- npm o yarn

### Pasos de instalación

```bash
# 1. Instalar dependencias
npm install

# 2. Configurar variables de entorno
cp .env.example .env

# 3. Configurar MongoDB en .env
MONGODB_URI=mongodb://localhost:27017/burgerprince
MONGODB_URI_TEST=mongodb://localhost:27017/burgerprince-test
JWT_SECRET=tu_super_secreto_jwt
```

## Uso

### Desarrollo
```bash
npm run dev
```

### Producción
```bash
npm start
```

### Tests
```bash
npm test
```

## Estructura del Proyecto

```
src/
├── models/              # Modelos Mongoose
│   ├── User.js
│   ├── Product.js
│   └── Order.js
├── controllers/         # Controladores
│   ├── authController.js
│   ├── usersController.js
│   ├── productsController.js
│   └── ordersController.js
├── routes/             # Rutas API
│   ├── auth.js
│   ├── users.js
│   ├── products.js
│   └── orders.js
├── middlewares/        # Middlewares
│   ├── auth.js
│   ├── validators.js
│   ├── errorHandler.js
│   └── logger.js
└── index.js           # Entrada principal
tests/
├── auth.test.js
├── users.test.js
├── products.test.js
└── orders.test.js
```

## API Endpoints

### Autenticación (`/auth`)
- `POST /auth/register` - Registrar primer usuario
- `POST /auth/login` - Iniciar sesión
- `POST /auth/logout` - Cerrar sesión
- `GET /auth/me` - Obtener usuario actual

### Usuarios (`/users`) - Requiere autenticación
- `POST /users` - Crear usuario (solo Admin)
- `GET /users` - Listar todos (solo Admin)
- `GET /users/:id` - Obtener usuario
- `PUT /users/:id` - Actualizar usuario
- `PUT /users/:id/change-password` - Cambiar contraseña
- `DELETE /users/:id` - Eliminar usuario (solo Admin)

### Productos (`/products`)
- `POST /products` - Crear producto (requiere autenticación)
- `GET /products` - Listar todos
- `GET /products?available=true` - Filtrar disponibles
- `GET /products/:id` - Obtener producto
- `PUT /products/:id` - Actualizar (requiere autenticación)
- `DELETE /products/:id` - Eliminar producto (requiere autenticación)

### Pedidos (`/orders`)
- `POST /orders` - Crear pedido
- `GET /orders` - Listar todos (requiere autenticación)
- `GET /orders/:id` - Obtener pedido
- `PUT /orders/:id/status` - Actualizar estado
- `DELETE /orders/:id` - Eliminar pedido

## Modelos de Datos

### User
```javascript
{
  fullName: String,
  username: String,
  email: String,
  phone: String,
  position: String, // Admin, Manager, Staff, Chef, Delivery
  password: String, // Encriptada con bcrypt
  isFirstUser: Boolean
}
```

### Product
```javascript
{
  name: String,
  description: String,
  price: Number,
  ingredients: String,
  available: Boolean,
  createdBy: ObjectId, // Referencia a User
  timestamps: true
}
```

### Order
```javascript
{
  orderNumber: String,
  paymentMethod: String, // Credit Card, Debit Card, Cash, PayPal, Transfer
  deliveryAddress: String,
  products: [
    {
      productId: ObjectId,
      quantity: Number,
      price: Number
    }
  ],
  totalPrice: Number,
  status: String, // Pending, Confirmed, Preparing, Ready, Delivered, Cancelled
  customer: {
    name: String,
    email: String,
    phone: String
  },
  timestamps: true
}
```

## Autenticación

La API utiliza JWT (JSON Web Tokens) para autenticación. 

### Obtener Token
```bash
curl -X POST http://localhost:3000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"password123"}'
```

### Usar Token
```bash
curl -X GET http://localhost:3000/auth/me \
  -H "Authorization: Bearer <token>"
```

## Validaciones

### express-validator
La API implementa validaciones automáticas en todos los endpoints:

- **Usuarios**: Email válido, nombre mínimo 3 caracteres, teléfono formato válido
- **Productos**: Nombre 3-100 caracteres, descripción 10-500 caracteres, precio > 0
- **Pedidos**: Método de pago válido, al menos 1 producto, cantidad > 0

## Documentación Swagger

Accede a la documentación interactiva en:
```
http://localhost:3000/api-docs
```

## Tests

### Ejecutar todos los tests
```bash
npm test
```

### Cobertura de tests
- ✅ Auth: Registro, Login, Obtener usuario, Logout
- ✅ Usuarios: CRUD completo, cambio de contraseña, control de permisos
- ✅ Productos: CRUD completo, filtrados
- ✅ Pedidos: CRUD completo, actualización de estado

### Resultados esperados
Todos los tests deberían pasar:
- `auth.test.js` - 15+ tests
- `users.test.js` - 16+ tests
- `products.test.js` - 17+ tests
- `orders.test.js` - 17+ tests

## Seguridad

### Implementaciones
1. **Contraseñas**: Encriptadas con bcryptjs (10 rondas de salt)
2. **JWT**: Tokens seguros con vencimiento configurable
3. **Validaciones**: Validación en cliente y servidor
4. **Autorización**: Control de roles y permisos
5. **CORS**: Configuración segura
6. **Rate Limiting**: Protección contra ataques

## Variables de Entorno

```env
# Servidor
PORT=3000
NODE_ENV=development

# Base de datos
MONGODB_URI=mongodb://localhost:27017/burgerprince
MONGODB_URI_TEST=mongodb://localhost:27017/burgerprince-test

# JWT
JWT_SECRET=tu_super_secreto_jwt_aec3_2026
JWT_EXPIRE=7d

# API
API_URL=http://localhost:3000
```

## Ejemplos de Uso

### 1. Registrar primer usuario
```bash
POST /auth/register
{
  "fullName": "Admin User",
  "username": "admin",
  "email": "admin@example.com",
  "phone": "+34666666666",
  "position": "Admin",
  "password": "password123"
}
```

### 2. Crear producto
```bash
POST /products
Headers: Authorization: Bearer {token}
{
  "name": "Hamburguesa Clásica",
  "description": "Deliciosa hamburguesa con queso y lechuga",
  "price": 9.99,
  "ingredients": "Pan, carne, queso, lechuga, tomate"
}
```

### 3. Crear pedido
```bash
POST /orders
{
  "paymentMethod": "Cash",
  "deliveryAddress": "123 Main St",
  "products": [
    {
      "productId": "60f7b1c1e1e1e1e1e1e1e1e1",
      "quantity": 2
    }
  ],
  "customer": {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+34666666666"
  }
}
```

## Manejo de Errores

La API devuelve errores en formato JSON:

```javascript
{
  "success": false,
  "message": "Descripción del error",
  "error": "Detalles técnicos (opcional)"
}
```

### Códigos HTTP
- `200`: OK
- `201`: Created
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Server Error

## Troubleshooting

### Conexión MongoDB
```bash
# Verificar conexión
mongosh "mongodb://localhost:27017"

# Si usar MongoDB Atlas, actualizar .env
MONGODB_URI=mongodb+srv://usuario:contraseña@cluster.mongodb.net/burgerprince
```

### Tests fallando
```bash
# Limpiar y reinstalar
rm -rf node_modules package-lock.json
npm install

# Reconstruir JEST
npm test -- --clearCache
```

### JWT expirado
```
Token expirado → Hacer login nuevamente para obtener nuevo token
```

## Contributing

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## Rúbrica de Evaluación

| Criterio | Puntuación |
|----------|-----------|
| Cambios en estructura API | 4 puntos |
| Validaciones express-validator | 1 punto |
| Autenticación JWT + bcrypt | 2 puntos |
| Documentación Swagger | 1 punto |
| Unit Testing JEST | 1 punto |
| Gestión de errores | 1 punto |
| **TOTAL** | **10 puntos** |

## Autor

Ismael Hernandez Clemente
- Email: ismael.hernandez@live.u-tad.com
- GitHub: https://github.com/ismaelucky342

## Licencia

MIT License - Ver LICENSE para más detalles
curl -sS http://localhost:3000/orders | jq
```

Crear un pedido:

```bash
curl -sS -X POST http://localhost:3000/orders \
  -H 'Content-Type: application/json' \
  -d '{"paymentMethod":"cash","price":8.5,"ingredients":{"bun":"sesame","patty":"beef","cheese":true}}' | jq
```

Ver un pedido por ID:

```bash
curl -sS http://localhost:3000/orders/1 | jq
```

Actualizar un pedido:

```bash
curl -sS -X PUT http://localhost:3000/orders/1 \
  -H 'Content-Type: application/json' \
  -d '{"paymentMethod":"card","price":9.5,"ingredients":{"bun":"sesame","patty":"veggie","cheese":false}}' | jq
```

Eliminar un pedido:

```bash
curl -sS -X DELETE http://localhost:3000/orders/1 | jq
```

## Errores que he probado

Probé el caso de enviar datos inválidos y la API devuelve un 400 con un mensaje claro.

Ejemplo:

```bash
curl -sS -X POST http://localhost:3000/orders \
  -H 'Content-Type: application/json' \
  -d '{"price":-5,"ingredients":{}}' | jq
```

La respuesta:

```json
{
  "success": false,
  "message": "Validation failed",
  "errors": [
    "paymentMethod is required and must be a non-empty string",
    "price is required and must be a non-negative number",
    "ingredients object must include at least one ingredient"
  ]
}
```

También comprobé que un ID inválido devuelve un 400:

```bash
curl -sS http://localhost:3000/orders/abc | jq
```

Y que un pedido no existente devuelve un 404.

## Pruebas manuales realizadas

- `GET /orders` para ver la lista inicial
- `POST /orders` para crear un pedido
- `GET /orders/:id` para recuperar ese pedido
- `PUT /orders/:id` para actualizarlo
- `DELETE /orders/:id` para borrarlo
- respuestas 400 cuando envío datos malos
- respuestas 404 cuando no existe el pedido

## Tests automáticos

he añadido unos tests automáticos que se ejecutan con:

```bash
npm test
```

donde se cubre: 

- listado de pedidos
- creación de pedido válido
- lectura por ID
- actualización
- eliminación
- errores de validación
- IDs inválidos
- pedidos inexistentes

## Extras

Siendo mi primera vez con express (muy necesario actualmente en otra asignatura) este proyecto me ha servido para practicar cómo estructurar una API pequeña con rutas claras, validaciones y manejo de errores sin usar base de datos. Me ha permitido ver lo útil que es separar rutas, controladores y middlewares, y confirmar que incluso un proyecto sencillo gana calidad con pruebas automáticas y una documentación clara.

![alt text](image.png)