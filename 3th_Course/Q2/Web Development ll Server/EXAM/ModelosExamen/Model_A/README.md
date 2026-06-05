# 🌤️ Weather API

API REST para la publicación y gestión de datos meteorológicos, desarrollada con **Node.js**, **Express**, **Sequelize (SQLite)**, **JWT**, **bcrypt** y documentada con **Swagger**.

---

## 📋 Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Node.js + Express | Servidor y enrutado |
| Sequelize + SQLite | ORM y almacenamiento |
| JWT (jsonwebtoken) | Autenticación |
| bcryptjs | Hash de contraseñas |
| express-validator | Validación de entradas |
| swagger-jsdoc + swagger-ui-express | Documentación |
| dotenv | Variables de entorno |
| cors | Cross-Origin Resource Sharing |

---

## 🚀 Instalación y arranque

```bash
# 1. Clonar/descomprimir el proyecto
cd weather-api

# 2. Instalar dependencias
npm install

# 3. Iniciar el servidor
npm start

# O en modo desarrollo (con nodemon)
npm run dev
```

El servidor arrancará en `http://localhost:3000`.

---

## 📚 Documentación

Una vez arrancado el servidor, accede a la documentación Swagger en:

```
http://localhost:3000/api-docs
```

---

## 🔑 Credenciales iniciales

Al arrancar por primera vez, se crea automáticamente un usuario administrador:

- **Email**: `admin@weather.com`
- **Password**: `admin123`

---

## 📡 Endpoints

### `/api/users` — Gestión de usuarios

| Método | Endpoint | Descripción | Auth requerida |
|---|---|---|---|
| `POST` | `/api/users/login` | Iniciar sesión | ❌ |
| `GET` | `/api/users` | Obtener todos los usuarios | ✅ Admin |
| `GET` | `/api/users/:id` | Obtener usuario por ID | ✅ Admin |
| `POST` | `/api/users` | Crear nuevo usuario | ✅ Admin |
| `PUT` | `/api/users/:id` | Actualizar usuario | ✅ Admin |
| `DELETE` | `/api/users/:id` | Eliminar usuario | ✅ Admin |

### `/api/data` — Datos meteorológicos

| Método | Endpoint | Descripción | Auth requerida |
|---|---|---|---|
| `GET` | `/api/data` | Obtener todos los registros | ❌ Público |
| `GET` | `/api/data/:id` | Obtener registro por ID | ❌ Público |
| `POST` | `/api/data` | Crear nuevo registro | ✅ Admin |
| `PUT` | `/api/data/:id` | Actualizar registro | ✅ Admin |
| `DELETE` | `/api/data/:id` | Eliminar registro | ✅ Admin |

---

## 🔐 Autenticación

La API usa **JWT Bearer Token**:

1. Haz `POST /api/users/login` con email y password.
2. Copia el `token` de la respuesta.
3. En las peticiones protegidas, añade la cabecera:
   ```
   Authorization: Bearer <tu_token>
   ```

---

## 📝 Ejemplos de uso

### Login
```bash
curl -X POST http://localhost:3000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@weather.com", "password": "admin123"}'
```

### Crear registro meteorológico
```bash
curl -X POST http://localhost:3000/api/data \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{
    "date": "2024-03-20",
    "latitude": 40.4168,
    "longitude": -3.7038,
    "rainProbability": 60,
    "precipitation": 8.5,
    "windSpeed": 30,
    "tempMin": 10,
    "tempMax": 20,
    "tempCurrent": 15
  }'
```

---

## 📁 Estructura del proyecto

```
weather-api/
├── src/
│   ├── config/
│   │   ├── database.js      # Configuración de Sequelize
│   │   └── swagger.js       # Configuración de Swagger
│   ├── controllers/
│   │   ├── userController.js      # Lógica de usuarios
│   │   └── weatherController.js   # Lógica de datos meteorológicos
│   ├── middleware/
│   │   ├── auth.js                # Verificación JWT y admin
│   │   └── validationHandler.js   # Manejo de errores de validación
│   ├── models/
│   │   ├── User.js           # Modelo de usuario
│   │   └── Pedidos.js    # Modelo de datos meteorológicos
│   ├── routes/
│   │   ├── userRoutes.js     # Rutas de usuarios
│   │   └── weatherRoutes.js  # Rutas de datos meteorológicos
│   ├── validators/
│   │   ├── userValidators.js    # Validaciones de usuarios
│   │   └── weatherValidators.js # Validaciones de datos meteorológicos
│   └── index.js             # Punto de entrada principal
├── .env                     # Variables de entorno
├── .gitignore
├── package.json
└── README.md
```
