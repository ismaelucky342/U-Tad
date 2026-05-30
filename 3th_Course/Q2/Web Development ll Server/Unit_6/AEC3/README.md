# BurgerPrince API - AEC3

## Introducción personal

He desarrollado esta API REST para una hamburguesería como continuacion de las AEC1 y AEC2. La BurgerPrince API continua la tarea de crear un sistema completo que permitiera gestionar todos los aspectos operativos de un restaurante: desde la administración de usuarios con roles diferenciados hasta la gestión integral de pedidos con métodos de pago variados. A través del desarrollo de este proyecto, he aprendido no solo a escribir código funcional, sino a estructurarlo de manera profesional y escalable, separando responsabilidades entre controladores, modelos y rutas.

Lo que hace especial este proyecto es que implementa características que van más allá del CRUD básico. He incluido un sistema de autenticación robusto con JWT, validaciones exhaustivas en todos los endpoints, una documentación interactiva con Swagger, y un suite completo de pruebas unitarias con Jest. Cada decisión técnica ha sido pensada para reflejar las mejores prácticas que estoy aprendiendo.

## Características implementadas

He desarrollado una API REST de hamburguesería que incluye:

- Base de datos persistente utilizando MongoDB, que permite almacenar y recuperar información de manera confiable
- Autenticación y autorización mediante JWT (JSON Web Tokens), lo que me permitió entender cómo proteger rutas y gestionar sesiones sin estado
- Sistema de validaciones completo con express-validator, asegurando que todos los datos que entra en la API sean válidos antes de procesarlos
- CRUD completo de Productos, permitiendo crear, leer, actualizar y eliminar productos del catálogo
- CRUD de Usuarios con sistema de roles y permisos, donde implementé diferentes niveles de acceso según la posición del usuario
- Sistema de Pedidos mejorado con seguimiento de estado y múltiples métodos de pago
- Documentación automática con Swagger, facilitando que otros desarrolladores entiendan cómo usar la API
- Unit Tests con Jest, lo que me ha permitido verificar que cada componente funciona según lo esperado

## Cómo instalar y ejecutar el proyecto

Para poder trabajar con esta API, necesito asegurarme de que tengo todos los requisitos previos instalados. He elegido Node.js como entorno de ejecución porque permite escribir JavaScript en el servidor de manera muy natural. MongoDB es la base de datos que utilizo, puede ser una instancia local o en la nube usando MongoDB Atlas.

Antes de empezar, necesito tener instalado:
- Node.js versión 14 o superior, que es donde ejecutará el código de mi servidor
- MongoDB, ya sea instalado localmente o una cuenta en Atlas para usar en la nube
- npm o yarn para gestionar los paquetes que necesita el proyecto

Una vez tengo todo listo, el proceso de instalación es bastante directo. Primero instalo todas las dependencias que necesito, luego configuro las variables de entorno con mis parámetros específicos, y finalmente puedo empezar a ejecutar la API.

```bash
# Paso 1: Instalar todas las dependencias necesarias del proyecto
npm install

# Paso 2: Crear el archivo de variables de entorno basándome en el ejemplo
cp .env.example .env

# Paso 3: Configurar MongoDB en el archivo .env con mi conexión específica
MONGODB_URI=mongodb://localhost:27017/burgerprince
MONGODB_URI_TEST=mongodb://localhost:27017/burgerprince-test
JWT_SECRET=tu_super_secreto_jwt
```

## Ejecutando la aplicación

Tengo tres formas distintas de ejecutar la aplicación dependiendo de lo que necesite hacer:

Para desarrollo, donde necesito ver cambios en tiempo real mientras escribo código:
```bash
npm run dev
```

Para simular el entorno de producción donde se ejecutaría en un servidor real:
```bash
npm start
```

Para ejecutar la suite de pruebas y verificar que todo funciona correctamente:
```bash
npm test
```

## Cómo organicé la estructura del proyecto

He organizado el proyecto siguiendo el patrón MVC (Modelo-Vista-Controlador) adaptado para una API REST. Esta estructura me permite mantener el código limpio, modular y fácil de mantener conforme crezca el proyecto.

En la carpeta `src` coloco todo el código de mi aplicación. Los modelos en Mongoose definen la estructura de las bases de datos y las reglas de validación a nivel de base de datos. He creado tres modelos principales: uno para usuarios que incluye roles y permisos, otro para productos del menú con precios e ingredientes, y otro para pedidos con seguimiento de estado.

Los controladores son donde implemento toda la lógica empresarial. Son funciones que reciben las peticiones HTTP, consultan los modelos, aplican la lógica necesaria y envían las respuestas. Tengo un controlador para cada recurso principal: autenticación, usuarios, productos y pedidos.

Las rutas definen los endpoints de mi API, conectando cada petición HTTP con el controlador correspondiente. He organizado las rutas por recurso, manteniendo cada conjunto de rutas en su propio archivo para mantener todo organizado.

Los middlewares son funciones que se ejecutan antes de llegar al controlador. He creado middlewares para autenticación que verifican tokens, para validaciones que usan express-validator, para manejo de errores centralizado, y para logging de peticiones importantes.

```
src/
├── models/              # Defino aquí la estructura de mis datos
│   ├── User.js          # Modelo de usuarios con roles
│   ├── Product.js       # Modelo de productos del catálogo
│   └── Order.js         # Modelo de pedidos con estado
├── controllers/         # Lógica empresarial de cada recurso
│   ├── authController.js
│   ├── usersController.js
│   ├── productsController.js
│   └── ordersController.js
├── routes/              # Definición de endpoints
│   ├── auth.js
│   ├── users.js
│   ├── products.js
│   └── orders.js
├── middlewares/         # Funciones que procesan peticiones
│   ├── auth.js          # Verifica autenticación
│   ├── validators.js    # Valida datos de entrada
│   ├── errorHandler.js  # Maneja errores consistentemente
│   └── logger.js        # Registra peticiones importantes
└── index.js             # Punto de entrada de la aplicación
tests/
├── auth.test.js
├── users.test.js
├── products.test.js
└── orders.test.js
```

## Los endpoints que he desarrollado

He organizado mi API en cuatro grupos principales de endpoints, cada uno responsable de un aspecto diferente de la aplicación.

### Autenticación - rutas bajo `/auth`

El sistema de autenticación es donde todo comienza. Aquí permito que los nuevos usuarios se registren en el sistema, aunque con una protección especial: solamente el primer usuario puede registrarse directamente. Los usuarios posteriores deben ser creados por un administrador. Esto asegura que siempre haya control sobre quiénes tienen acceso al sistema.

- `POST /auth/register` - Permite al primer usuario registrarse en el sistema
- `POST /auth/login` - Un usuario existente inicia sesión y recibe un token JWT
- `POST /auth/logout` - El usuario cierra su sesión actual
- `GET /auth/me` - Obtiene los datos del usuario autenticado actualmente

### Usuarios - rutas bajo `/users`

La gestión de usuarios es fundamental para un sistema multiusuario. Aquí implementé un sistema de roles donde diferentes usuarios pueden tener diferentes permisos. Solamente administradores pueden crear nuevos usuarios o ver la lista completa. He incluido también la capacidad de cambiar contraseña de manera segura.

Todos estos endpoints requieren que el usuario esté autenticado:
- `POST /users` - Crear un nuevo usuario (solo administradores)
- `GET /users` - Ver todos los usuarios (solo administradores)
- `GET /users/:id` - Obtener datos de un usuario específico
- `PUT /users/:id` - Actualizar información de un usuario
- `PUT /users/:id/change-password` - Cambiar la contraseña de forma segura
- `DELETE /users/:id` - Eliminar un usuario (solo administradores)

### Productos - rutas bajo `/products`

El catálogo de productos es lo que los clientes verán y pedirán. He diseñado estos endpoints para que el listado público sea accesible sin autenticación, pero cualquier modificación requiera estar autenticado. También implementé la capacidad de filtrar productos disponibles.

- `POST /products` - Crear un nuevo producto (requiere autenticación)
- `GET /products` - Ver todos los productos del catálogo
- `GET /products?available=true` - Filtrar para ver solo productos disponibles
- `GET /products/:id` - Obtener detalles completos de un producto específico
- `PUT /products/:id` - Actualizar información de un producto (requiere autenticación)
- `DELETE /products/:id` - Remover un producto del catálogo (requiere autenticación)

### Pedidos - rutas bajo `/orders`

El sistema de pedidos es el corazón de la aplicación. Aquí manejo todo el ciclo de vida de un pedido, desde su creación hasta su entrega. Implementé múltiples estados para rastrear en qué fase está cada pedido, y permito diferentes métodos de pago.

- `POST /orders` - Crear un nuevo pedido
- `GET /orders` - Listar todos los pedidos (requiere autenticación)
- `GET /orders/:id` - Obtener detalles de un pedido específico
- `PUT /orders/:id/status` - Actualizar el estado de un pedido
- `DELETE /orders/:id` - Cancelar o eliminar un pedido

## La estructura de datos que utilizo

Cada recurso en mi API tiene un modelo que define su estructura y algunas reglas de validación a nivel de base de datos. He diseñado cuidadosamente estas estructuras para que capturen toda la información necesaria mientras se mantienen simples y eficientes.

### El modelo de Usuario

Un usuario en mi sistema tiene varios campos que lo definen. Necesito su nombre completo para saber a quién corresponde la cuenta, un nombre de usuario para efectos de login, su email que uso para comunicaciones y recuperación de contraseña, un teléfono para contacto, y una posición que determina qué permisos tiene en el sistema. Las posiciones varían desde administrador que tiene acceso total, hasta manager que gestiona operaciones, staff que atiende clientes, chef que prepara alimentos, y delivery que entrega pedidos.

Crucialmente, la contraseña se almacena de forma encriptada usando bcrypt, nunca en texto plano. Esto asegura que incluso si alguien accede a la base de datos, las contraseñas están protegidas.

```javascript
{
  fullName: String,
  username: String,
  email: String,
  phone: String,
  position: String, // Admin, Manager, Staff, Chef, Delivery
  password: String, // Encriptada con bcrypt para seguridad
  isFirstUser: Boolean
}
```

### El modelo de Producto

Cada producto en mi catálogo tiene un nombre descriptivo, una descripción que ayuda al cliente a entender qué es, un precio, una lista de ingredientes, y un estado que indica si está disponible o no. También registro quién creó el producto y cuándo, lo que es útil para auditoría y debugging.

```javascript
{
  name: String,
  description: String,
  price: Number,
  ingredients: String,
  available: Boolean,
  createdBy: ObjectId, // Referencia a qué usuario lo creó
  timestamps: true     // Registra cuándo se creó y modificó
}
```

### El modelo de Pedido

Un pedido es la parte más compleja. Cada pedido tiene un número único para referencia rápida, un método de pago que el cliente eligió, una dirección de entrega, y una lista de productos con cantidades y precios. Registro el precio total, el estado actual del pedido en su ciclo de vida, e información del cliente para saber a quién entregar.

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

## Cómo funciona la autenticación en mi API

He implementado un sistema de autenticación basado en JWT (JSON Web Tokens), que es lo que se usa en prácticamente todas las APIs modernas. La idea es que el usuario se autentica una sola vez con sus credenciales, recibe un token, y luego usa ese token para acceder a recursos protegidos sin necesidad de enviar su contraseña constantemente.

El flujo es relativamente simple. Cuando el usuario proporciona sus credenciales en el login, verifico que sean correctas, genero un token JWT y lo devuelvo. Este token contiene información codificada sobre el usuario y tiene una fecha de expiración. Cada vez que el usuario quiere acceder a un recurso protegido, envía este token en el encabezado de autorización.

Para obtener un token, el usuario inicia sesión con sus credenciales:

```bash
curl -X POST http://localhost:3000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"password123"}'
```

Una vez que tengo el token, lo uso en peticiones posteriores incluyéndolo en el encabezado de Autorización:

```bash
curl -X GET http://localhost:3000/auth/me \
  -H "Authorization: Bearer <token>"
```

El token en sí es verificado por un middleware en cada petición. Si es válido y no ha expirado, permito que la petición continúe. Si es inválido o ha expirado, devuelvo un error 401 indicando que el usuario no está autorizado.

## Cómo valido todos los datos que recibo

Una de las lecciones más importantes que aprendí es que nunca debo confiar en los datos que me envía el cliente. Cualquiera podría enviarme datos inválidos, incompletos o maliciosos. Por esa razón, implementé un sistema exhaustivo de validaciones usando express-validator.

Para los usuarios, verifico que el email sea realmente un email válido usando expresiones regulares, que el nombre tenga al menos 3 caracteres para ser significativo, y que el teléfono tenga un formato válido. 

Para los productos, valido que el nombre tenga entre 3 y 100 caracteres, que la descripción sea lo suficientemente larga y detallada (entre 10 y 500 caracteres), y que el precio sea un número positivo mayor a cero. No tiene sentido permitir productos gratis accidentalmente.

Para los pedidos, valido que el método de pago sea uno de los permitidos, que haya al menos un producto en el pedido, que las cantidades sean números positivos, y que los datos del cliente sean suficientes para completar la entrega.

Todas estas validaciones se ejecutan antes de que el controlador procese la petición. Si algo no es válido, devuelvo un error 400 con mensajes claros explicando qué está mal, para que el cliente pueda corregir su petición.

## La documentación interactiva de mi API

He integrado Swagger en mi API para que otros desarrolladores puedan entender y probar qué hace cada endpoint. Esta documentación es especialmente útil porque es interactiva: puedo ver exactamente qué parámetros tiene cada petición, qué respuesta esperar, y puedo incluso hacer peticiones de prueba directamente desde la documentación.

Acceder a la documentación es tan simple como visitar esta URL en el navegador:

```
http://localhost:3000/api-docs
```

Aquí veré una interfaz amigable que lista todos mis endpoints, explica qué hace cada uno, y me permite hacer peticiones de prueba directamente. Esto es invaluable para desarrollo y para que otros entiendan cómo usar mi API.

## Las pruebas automáticas que implementé

He creído profundamente en la importancia de las pruebas automáticas. Cuando escribo código nuevo, es común que funcione bien en pruebas manuales pero tenga comportamientos inesperados en casos especiales. Las pruebas automáticas me permiten verificar que mi código hace lo que espero y detectar problemas antes de que lleguen a usuarios reales.

He utilizado Jest como framework de testing por su simplicidad y potencia. Ejecuto todas las pruebas con un simple comando:

```bash
npm test
```

He incluido pruebas para cada componente importante de mi API:

Para la autenticación, verifico que el registro funciona correctamente, que el login rechaza credenciales incorrectas pero acepta las correctas, que puedo obtener mis datos de usuario actual, y que el logout funciona como se espera. Esto me da 15 o más casos de prueba.

Para usuarios, pruebo que pueda crear nuevos usuarios pero solo si tengo permisos de administrador, que pueda actualizar mi propia información, que el cambio de contraseña funciona correctamente, que los usuarios sin permisos no puedan realizar ciertas acciones. Esto me da aproximadamente 16 casos de prueba.

Para productos, verifico que puedo crear productos nuevos, que el filtrado de productos disponibles funciona, que puedo actualizar y eliminar productos, y que los datos inválidos son rechazados. Esto suma unos 17 casos de prueba.

Para pedidos, pruebo el ciclo completo: crear pedidos, cambiar su estado conforme avanzan, calcular precios totales correctamente, y rechazar pedidos con datos inválidos. Esto me da otros 17 casos de prueba.

En total, tengo más de 65 casos de prueba que verifican que mi API funciona correctamente. Cuando ejecuto las pruebas, espero que todas pasen sin excepciones.

## Las medidas de seguridad que implementé

La seguridad es algo que tomo muy en serio. He implementado varias capas de protección para asegurar que los datos de usuarios y la integridad del sistema estén protegidos.

Primero, las contraseñas nunca se almacenan en texto plano. Utilizo bcryptjs para encriptarlas con 10 rondas de salt, lo que hace que aunque alguien acceda a la base de datos, no pueda ver las contraseñas. Incluso si dos usuarios tienen la misma contraseña, se almacenan de manera diferente debido al salt.

Los tokens JWT están firmados con un secreto seguro y tienen un tiempo de expiración. Esto significa que incluso si alguien intercepta un token, solo tendrá validez durante un período limitado, después del cual será rechazado automáticamente. El usuario deberá hacer login nuevamente para obtener un token fresco.

He implementado validaciones en el cliente y servidor para asegurar que los datos sean realmente lo que dicen ser. Esto previene muchos tipos de ataques comunes.

El sistema de autorización verifica que cada usuario solo pueda acceder a lo que le corresponde según su rol. Un usuario regular no puede crear otros usuarios, ver información de otros usuarios, o eliminar productos. Solamente los administradores tienen estos permisos.

He configurado CORS de manera segura, permitiendo solo los orígenes que establezco explícitamente. Esto previene que scripts maliciosos desde otros sitios accedan a mi API.

También implementé límite de rapidez en las peticiones (rate limiting) para proteger contra ataques de fuerza bruta donde alguien intenta constantemente romper contraseñas.

## Las configuraciones que necesito

Mi aplicación se configura a través de variables de entorno, que es la manera moderna de hacer esto. Me permite cambiar la configuración sin modificar el código, lo que es especialmente importante cuando paso de desarrollo a producción.

Necesito configurar el puerto en el que escucha mi servidor, normalmente 3000 en desarrollo. Establezco el entorno (desarrollo, pruebas o producción) para que la aplicación se comporte diferente según donde esté.

Para persistencia de datos, configuro la URI de MongoDB. En desarrollo uso una instancia local, pero en producción podría usar MongoDB Atlas en la nube. Also tengo una URI separada para las pruebas para que las pruebas no afecten mis datos reales.

Para seguridad, establezco un secreto JWT que se usa para firmar y verificar los tokens. Este debe ser una cadena aleatoria larga y segura. También configuro cuánto tiempo dura un token antes de expirar.

```env
# Configuración del servidor
PORT=3000
NODE_ENV=development

# Base de datos
MONGODB_URI=mongodb://localhost:27017/burgerprince
MONGODB_URI_TEST=mongodb://localhost:27017/burgerprince-test

# Seguridad JWT
JWT_SECRET=tu_super_secreto_jwt_aec3_2026
JWT_EXPIRE=7d

# URL base de la API
API_URL=http://localhost:3000
```

## Ejemplos prácticos de cómo usar mi API

Aquí muestro algunos ejemplos reales de cómo interactuar con mi API. El primero es siempre registrar el primer usuario.

### Registrar el primer usuario del sistema

Para que la aplicación sea útil, necesito crear al menos un usuario. El primer usuario debe ser creado a través del endpoint de registro, que es la única vez que cualquiera puede registrarse sin ser administrador:

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

Una vez tengo este usuario, todos los demás usuarios deben ser creados por un administrador a través de una petición autenticada.

### Crear un nuevo producto

Después de autenticarme e incluir mi token JWT, puedo crear nuevos productos para el catálogo. Esta información será lo que mis clientes verán cuando hagan un pedido:

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

Este producto ahora estará disponible en el catálogo para que todos lo vean.

### Crear un pedido de cliente

Un cliente quiere hacer un pedido. Este cliente no necesita estar autenticado; cualquiera puede crear un pedido. Especifico qué productos quiere comprar, cómo piensa pagar, y a dónde desea que se le entregue:

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

El sistema calcula automáticamente el precio total y asigna un número de pedido único para seguimiento.

## Cómo manejo los errores

He diseñado mi sistema de errores para que sea consistente y útil. Cada error deviene en un formato JSON estándar que permite al cliente entender qué salió mal y por qué.

Cuando ocurre un error, mi API devuelve un objeto JSON con un campo de éxito establecido a falso, un mensaje que explica el problema en lenguaje natural, y opcionalmente detalles técnicos si son relevantes:

```javascript
{
  "success": false,
  "message": "Descripción clara del error",
  "error": "Detalles técnicos opcionales"
}
```

Los códigos HTTP que utilizo siguen los estándares REST, lo que hace que sea fácil para cualquier cliente entender qué pasó:

- 200: La petición fue exitosa y estoy devolviendo datos
- 201: La petición fue exitosa y he creado un nuevo recurso
- 400: La petición tiene datos inválidos o incompletos que no puedo procesar
- 401: El usuario no está autenticado, necesita hacer login
- 403: El usuario está autenticado pero no tiene permisos para acceder a esto
- 404: El recurso que está buscando no existe
- 500: Algo salió mal en mi servidor, no es culpa del cliente

Este sistema consistente de errores hace que sea mucho más fácil para el cliente entender y manejar problemas.


## Demostraciones en Video

He grabado dos videos demostrando que todo funciona correctamente:

### Video 1: Ejecución de Tests Automáticos

En este video muestro cómo todos mis tests unitarios se ejecutan exitosamente. He creado una suite de pruebas exhaustiva que valida cada componente de mi API. El video comienza navegando a la carpeta del proyecto, mostrando los archivos de test disponibles, y luego ejecuto el comando `npm test`.

Lo que se ve en el video es:
- La ejecución de los tests de autenticación, verificando que el registro, login y logout funcionan correctamente
- Los tests de usuarios pasando, demostrando que solo administradores pueden crear usuarios y que los permisos se respetan
- Los tests de productos pasando, mostrando que la creación, lectura, actualización y eliminación funcionan con validaciones correctas
- Los tests de pedidos pasando, incluyendo la creación de pedidos con múltiples productos y cambios de estado
- Un resumen final mostrando que más de 50 tests pasaron exitosamente en aproximadamente 3-4 segundos

Este video es importante porque prueba de manera automática y reproducible que toda mi lógica de negocio funciona como se espera.

### Video 2: Servidor en Vivo con Peticiones HTTP

En este segundo video muestro la API ejecutándose en tiempo real, recibiendo peticiones HTTP y devolviendo respuestas correctas. Este video es especialmente útil porque demuestra que la API está lista para ser usada por clientes reales.

En el video puedo ver:

**Autenticación y Usuarios:**
- Me registro como el primer usuario administrador, recibiendo un JWT token
- Hago login con mis credenciales y obtengo un nuevo token
- Obtengo mis datos de usuario autenticado usando el token

**Productos:**
- Creo un producto nuevo "Hamburguesa Clásica" con descripción, precio e ingredientes
- Listo todos los productos disponibles sin necesidad de autenticación
- El servidor responde correctamente en cada caso

**Pedidos:**
- Creo un pedido con el producto que acabo de crear, especificando cantidad, método de pago y dirección de entrega
- El pedido se crea exitosamente con un estado "Pending"
- Listo todos los pedidos de mi cuenta usando autenticación
