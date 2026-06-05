# 🗺️ GUÍA DE ADAPTACIÓN — API REST Template

Esta plantilla funciona tal cual para el enunciado de meteorología.
Para adaptarla a **cualquier otro enunciado** solo tienes que tocar **4 archivos**.

---

## ✅ LAS 4 COSAS QUE CAMBIAS (y nada más)

### 1. 📦 `src/models/WeatherData.js` → Tu modelo de dominio
**Renombra el archivo** y cambia los campos del `DataTypes` por los de tu enunciado.

| Enunciado dice... | Tú pones en el modelo |
|---|---|
| "título del libro (string)" | `title: { type: DataTypes.STRING, allowNull: false }` |
| "precio (decimal)" | `price: { type: DataTypes.FLOAT, allowNull: false }` |
| "fecha de publicación" | `publishedAt: { type: DataTypes.DATE }` |
| "stock (número entero)" | `stock: { type: DataTypes.INTEGER, defaultValue: 0 }` |
| "activo (booleano)" | `isActive: { type: DataTypes.BOOLEAN, defaultValue: true }` |

**Mantén siempre** el campo `userId` (la FK al autor/creador del registro) y los `timestamps`.

```js
// Ejemplo para una API de Libros
const Book = sequelize.define('Book', {
  id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
  title: { type: DataTypes.STRING, allowNull: false },
  author: { type: DataTypes.STRING, allowNull: false },
  isbn: { type: DataTypes.STRING, unique: true },
  price: { type: DataTypes.FLOAT, allowNull: false },
  stock: { type: DataTypes.INTEGER, defaultValue: 0 },
  userId: { type: DataTypes.INTEGER, allowNull: false },
}, { tableName: 'books', timestamps: true });
```

---

### 2. ✅ `src/validators/dataValidators.js` → Tus validaciones
Cambia los `body('campo')` por los campos de TU modelo.

**Reglas básicas de express-validator:**
```js
body('campo').notEmpty().withMessage('Es obligatorio')
body('campo').isString().withMessage('Debe ser texto')
body('campo').isFloat({ min: 0 }).withMessage('Debe ser número positivo')
body('campo').isInt().withMessage('Debe ser entero')
body('campo').isBoolean().withMessage('Debe ser true/false')
body('campo').isISO8601().withMessage('Fecha inválida')
body('campo').isIn(['val1','val2']).withMessage('Valor no permitido')
body('campo').isLength({ min: 3, max: 100 }).withMessage('Longitud inválida')
body('campo').optional()   // <-- lo hace opcional en PUT/PATCH
```

---

### 3. 🎮 `src/controllers/dataController.js` → Tus campos
Solo hay que cambiar **dos funciones**:

**En `createData`**: Desestructura los campos de TU modelo:
```js
// Antes (meteorología):
const { recordDate, latitude, longitude, rainProbability, ... } = req.body;

// Después (libros):
const { title, author, isbn, price, stock } = req.body;

// Y en el create():
const newRecord = await Book.create({ title, author, isbn, price, stock, userId: req.user.id });
```

**En `updateData`**: Cambia el array `updateFields`:
```js
// Antes:
const updateFields = ['recordDate', 'latitude', 'longitude', ...];

// Después:
const updateFields = ['title', 'author', 'isbn', 'price', 'stock'];
```

---

### 4. 🛣️ `src/index.js` → Nombre de tu ruta
Cambia el prefijo de la ruta y las importaciones:

```js
// Antes:
require('./models/WeatherData');
const dataRoutes = require('./routes/dataRoutes');
app.use('/data', dataRoutes);

// Después (para libros):
require('./models/Book');
const bookRoutes = require('./routes/bookRoutes');
app.use('/books', bookRoutes);
```

Y en `src/routes/dataRoutes.js` actualiza el nombre del tag de Swagger:
```js
// @swagger tags:  name: Books  (en lugar de WeatherData)
```

---

## 🔒 LO QUE NO TOCAS NUNCA

Estos archivos son 100% genéricos. **Copiarlos tal cual** da todos los puntos de:

| Archivo | Puntos cubiertos |
|---|---|
| `src/middleware/auth.js` | Pregunta 5 (JWT), Pregunta 6 (permisos) |
| `src/middleware/handleValidation.js` | Pregunta 4 (validación) |
| `src/validators/userValidators.js` | Pregunta 4, Pregunta 5 |
| `src/controllers/userController.js` | Pregunta 3, Pregunta 5 |
| `src/routes/userRoutes.js` | Pregunta 1, Pregunta 7 (Swagger) |
| `src/config/swagger.js` | Pregunta 7 |
| `src/config/database.js` | Pregunta 2 |
| `src/models/User.js` | Pregunta 2 |

---

## 🚀 ARRANCAR EL PROYECTO

```bash
# 1. Instalar dependencias
npm install

# 2. Crear el .env (copia el ejemplo)
cp .env.example .env

# 3. Arrancar en modo desarrollo
npm run dev

# 4. Abrir Swagger en el navegador
# http://localhost:3000/api-docs
```

---

## 🧪 FLUJO DE PRUEBA (orden correcto)

1. **Crear primer usuario admin** via `POST /users/login` — espera, primero...
2. Necesitas un admin. En producción se haría con un seed script, pero en el examen:
   - Llama a `POST /users` sin token (el primer usuario se puede crear sin auth si lo configuras)
   - O cambia temporalmente la ruta para que no requiera `isAdmin` al crear el primer usuario

3. **Login**: `POST /users/login` → copia el token
4. **Usar el token**: En Swagger, clic en "Authorize" → `Bearer <token>`
5. **Probar rutas protegidas**: crear datos, ver usuarios, etc.

---

## 📁 ESTRUCTURA DEL ZIP DE ENTREGA

```
mi-api/
├── src/
│   ├── config/
│   ├── controllers/
│   ├── middleware/
│   ├── models/
│   ├── routes/
│   ├── validators/
│   └── index.js
├── .env.example
├── .gitignore
└── package.json

❌ NO incluir: node_modules/, .env, *.sqlite
```

---

## 💡 TABLA RÁPIDA DE TIPOS SEQUELIZE

| Tipo de dato | Sequelize |
|---|---|
| Texto corto | `DataTypes.STRING` |
| Texto largo | `DataTypes.TEXT` |
| Número entero | `DataTypes.INTEGER` |
| Número decimal | `DataTypes.FLOAT` o `DataTypes.DECIMAL(10,2)` |
| Booleano | `DataTypes.BOOLEAN` |
| Fecha+hora | `DataTypes.DATE` |
| Solo fecha | `DataTypes.DATEONLY` |
| Enum | `DataTypes.ENUM('opcion1', 'opcion2')` |
| JSON | `DataTypes.JSON` |
