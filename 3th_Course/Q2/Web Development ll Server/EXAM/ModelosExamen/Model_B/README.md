# 📚 Library API

API REST para la gestión de una biblioteca digital, desarrollada con **Node.js**, **Express**, **Sequelize (SQLite)**, **JWT**, **bcrypt** y documentada con **Swagger**.

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
cd library-api

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

## 🔐 Autenticación

Para acceder a los endpoints protegidos:

1. **Login**: `POST /api/users/login`
   ```json
   {
     "email": "admin@library.com",
     "password": "admin123"
   }
   ```

2. Copia el `token` de la respuesta.

3. Haz clic en el botón **Authorize** en Swagger e introduce:
   ```
   Bearer <tu_token>
   ```

---

## 📊 Estructura de la API

### Usuarios (`/users`)
- `POST /users/login` — Login (público)
- `GET /users` — Listar todos los usuarios (solo admin)
- `GET /users/:id` — Obtener usuario por ID (solo admin)
- `POST /users` — Crear nuevo usuario (solo admin)
- `PUT /users/:id` — Actualizar usuario (solo admin)
- `DELETE /users/:id` — Eliminar usuario (solo admin)

### Libros (`/books`)
- `GET /books` — Listar todos los libros (público)
- `GET /books/:id` — Obtener libro por ID (público)
- `POST /books` — Crear nuevo libro (solo admin)
- `PUT /books/:id` — Actualizar libro (solo admin)
- `DELETE /books/:id` — Eliminar libro (solo admin)

---

## 👤 Usuario administrador inicial

- **Email**: `admin@library.com`
- **Password**: `admin123`

---

## 📝 Ejemplos de uso

### Login
```bash
curl -X POST http://localhost:3000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@library.com","password":"admin123"}'
```

### Crear libro (requiere token admin)
```bash
curl -X POST http://localhost:3000/api/books \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <tu_token>" \
  -d '{
    "title": "El Quijote",
    "author": "Miguel de Cervantes",
    "isbn": "978-8420412498",
    "genre": "Novela",
    "publicationYear": 1605,
    "pages": 1072,
    "available": true,
    "synopsis": "Aventuras de un hidalgo español."
  }'
```

### Obtener todos los libros
```bash
curl http://localhost:3000/api/books
```

---

## 🛠️ Notas de desarrollo

- La base de datos se sincroniza automáticamente al arrancar.
- Los datos de ejemplo se crean si la tabla está vacía.
- El hash de contraseñas se realiza con `bcryptjs` (salt rounds: 10).
- Los tokens JWT expiran en **8 horas**.

