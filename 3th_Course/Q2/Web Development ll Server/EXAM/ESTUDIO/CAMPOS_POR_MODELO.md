# 📋 CAMPO POR CAMPO - GUÍA RÁPIDA

## TABLA COMPARATIVA DE CAMPOS POR MODELO

| Campo | Model_B (Library) | Model_C (Events) | Model_D (Products) | Model_E (Workouts) | Model_F (Articles) |
|-------|---|---|---|---|---|
| **TABLA SECUNDARIA** | Book | Event | Product | Workout | Article |
| --- | --- | --- | --- | --- | --- |

### 📚 MODEL_B: LIBRARY API - BOOK

```javascript
Book.init({
  id: { type: INTEGER, primaryKey: true, autoIncrement: true },
  title: { type: STRING(100), allowNull: false },                // Nombre del libro
  author: { type: STRING(100), allowNull: false },               // Autor
  ISBN: { type: STRING(13), allowNull: false, unique: true },    // ISBN único
  genre: { type: ENUM('ficción','no-ficción','ciencia','historia','otros'), allowNull: false },
  publicationYear: { type: INTEGER, validate: { min: 1000, max: 2100 } },
  pages: { type: INTEGER, validate: { min: 1 } },                // Número de páginas
  available: { type: BOOLEAN, defaultValue: true },              // ¿Está disponible?
  synopsis: { type: TEXT },                                      // Describción
  userId: { type: INTEGER, allowNull: false, foreignKey: true }, // Quién lo registró
  createdAt: { type: DATE, defaultValue: NOW() },
  updatedAt: { type: DATE, defaultValue: NOW() },
});
```

**Validadores Clave:**
```javascript
body('ISBN')
  .matches(/^[0-9]{13}$/).withMessage('ISBN debe tener 13 dígitos'),
body('publicationYear')
  .isInt({ min: 1000, max: 2100 }).withMessage('Año entre 1000-2100'),
body('pages')
  .isInt({ min: 1 }).withMessage('Páginas debe ser > 0'),
body('genre')
  .isIn(['ficción','no-ficción','ciencia','historia','otros']).withMessage('Género no válido'),
```

---

### 🎭 MODEL_C: EVENTS API - EVENT

```javascript
Event.init({
  id: { type: INTEGER, primaryKey: true, autoIncrement: true },
  name: { type: STRING(100), allowNull: false },                          // Nombre evento
  eventDate: { type: DATE, allowNull: false },                            // Fecha/hora del evento
  city: { type: STRING(50), allowNull: false },                           // Ciudad
  address: { type: STRING(200), allowNull: false },                       // Dirección completa
  category: { type: ENUM('concierto','teatro','deporte','otro'), allowNull: false },
  maxCapacity: { type: INTEGER, allowNull: false, validate: { min: 1 } },
  availableSpots: { type: INTEGER, allowNull: false },                   // Entradas disponibles
  ticketPrice: { type: FLOAT, allowNull: false, validate: { min: 0 } },  // Precio en €
  description: { type: TEXT },                                            // Descripción larga
  organizerId: { type: INTEGER, allowNull: false, foreignKey: true },    // Usuario organizador
  createdAt: { type: DATE, defaultValue: NOW() },
  updatedAt: { type: DATE, defaultValue: NOW() },
});
```

**Validadores Clave:**
```javascript
body('eventDate')
  .isISO8601().withMessage('Fecha debe ser formato ISO'),
body('category')
  .isIn(['concierto','teatro','deporte','otro']).withMessage('Categoría no válida'),
body('ticketPrice')
  .isFloat({ min: 0 }).withMessage('Precio debe ser ≥ 0'),
body('maxCapacity')
  .isInt({ min: 1 }).withMessage('Capacidad debe ser > 0'),
```

---

### 🛍️  MODEL_D: PRODUCTS API - PRODUCT

```javascript
Product.init({
  id: { type: INTEGER, primaryKey: true, autoIncrement: true },
  name: { type: STRING(100), allowNull: false },                   // Nombre producto
  description: { type: TEXT },                                     // Descripción
  price: { type: FLOAT, allowNull: false, validate: { min: 0 } }, // Precio en €
  stock: { type: INTEGER, allowNull: false, validate: { min: 0 } }, // Unidades disponibles
  category: { type: STRING(50), allowNull: false },                // Categoría
  brand: { type: STRING(50) },                                     // Marca fabricante
  imageUrl: { type: STRING(500) },                                 // URL de imagen
  weight: { type: FLOAT, validate: { min: 0 } },                   // Peso en gramos
  registeredDate: { type: DATEONLY, defaultValue: NOW() },         // Solo fecha (no hora)
  registeredBy: { type: INTEGER, allowNull: false, foreignKey: true }, // Usuario que registró
  createdAt: { type: DATE, defaultValue: NOW() },
  updatedAt: { type: DATE, defaultValue: NOW() },
});
```

**Validadores Clave:**
```javascript
body('price')
  .isFloat({ min: 0 }).withMessage('Precio debe ser ≥ 0'),
body('stock')
  .isInt({ min: 0 }).withMessage('Stock debe ser ≥ 0'),
body('weight')
  .optional()
  .isFloat({ min: 0 }).withMessage('Peso debe ser ≥ 0'),
body('imageUrl')
  .optional()
  .isURL().withMessage('URL inválida'),
```

---

### 🏋️ MODEL_E: WORKOUTS API - WORKOUT

```javascript
Workout.init({
  id: { type: INTEGER, primaryKey: true, autoIncrement: true },
  date: { type: DATE, allowNull: false },                           // Fecha/hora
  activityType: { type: ENUM('carrera','ciclismo','natación','pesas','otro'), allowNull: false },
  duration: { type: INTEGER, allowNull: false, validate: { min: 1 } }, // Duración en minutos
  distance: { type: FLOAT, validate: { min: 0 } },                  // Distancia en km (opcional)
  caloriesBurned: { type: FLOAT, allowNull: false, validate: { min: 0 } }, // Calorías quemadas
  avgHeartRate: { type: INTEGER, validate: { min: 40, max: 220 } }, // Promedio de FC (pulsaciones)
  notes: { type: TEXT },                                             // Notas adicionales
  recordedBy: { type: INTEGER, allowNull: false, foreignKey: true }, // Usuario que registró
  createdAt: { type: DATE, defaultValue: NOW() },
  updatedAt: { type: DATE, defaultValue: NOW() },
});
```

**Validadores Clave:**
```javascript
body('activityType')
  .isIn(['carrera','ciclismo','natación','pesas','otro']).withMessage('Actividad no válida'),
body('duration')
  .isInt({ min: 1 }).withMessage('Duración debe ser > 0'),
body('distance')
  .optional()
  .isFloat({ min: 0 }).withMessage('Distancia debe ser ≥ 0'),
body('caloriesBurned')
  .isFloat({ min: 0 }).withMessage('Calorías deben ser ≥ 0'),
body('avgHeartRate')
  .optional()
  .isInt({ min: 40, max: 220 }).withMessage('Frecuencia cardíaca entre 40-220'),
```

---

### 📰 MODEL_F: ARTICLES API - ARTICLE

```javascript
Article.init({
  id: { type: INTEGER, primaryKey: true, autoIncrement: true },
  title: { type: STRING(200), allowNull: false },                   // Título artículo
  subtitle: { type: STRING(300) },                                  // Subtítulo (opcional)
  body: { type: TEXT, allowNull: false },                           // Contenido principal
  category: { type: STRING(50), allowNull: false },                 // Categoría
  publishedDate: { type: DATE },                                    // Fecha de publicación
  authorId: { type: INTEGER, allowNull: false, foreignKey: true },  // Usuario autor
  featuredImageUrl: { type: STRING(500) },                          // Imagen destacada (opcional)
  tags: { type: JSON, defaultValue: [] },                           // Array de etiquetas
  status: { type: ENUM('borrador','publicado'), defaultValue: 'borrador' },
  createdAt: { type: DATE, defaultValue: NOW() },
  updatedAt: { type: DATE, defaultValue: NOW() },
});
```

**Validadores Clave:**
```javascript
body('title')
  .notEmpty().withMessage('Título obligatorio')
  .isLength({ min: 5, max: 200 }).withMessage('Entre 5 y 200 caracteres'),
body('body')
  .notEmpty().withMessage('Contenido obligatorio'),
body('tags')
  .optional()
  .isArray().withMessage('Tags debe ser array'),
body('status')
  .isIn(['borrador','publicado']).withMessage('Estado no válido'),
body('category')
  .notEmpty().withMessage('Categoría obligatoria'),
```

---

## TABLA RESUMEN

| Característica | Model_B | Model_C | Model_D | Model_E | Model_F |
|---|---|---|---|---|---|
| **Uso de DATE** | No (only year) | ✅ eventDate | Registrada | ✅ date | ✅ publishedDate |
| **Uso de DATEONLY** | No | No | ✅ registeredDate | No | No |
| **Uso de FLOAT** | No | ✅ ticketPrice | ✅ price, weight | ✅ distance, caloriesBurned | No |
| **Uso de INTEGER** | ✅ pages | ✅ maxCapacity | ✅ stock | ✅ duration, avgHeartRate | No |
| **Uso de ENUM** | ✅ genre | ✅ category | No | ✅ activityType | ✅ status, category (string) |
| **Uso de JSON** | No | No | No | No | ✅ tags (array) |
| **Uso de TEXT** | ✅ synopsis | ✅ description | ✅ description | ✅ notes | ✅ body |
| **Campos opcionales** | 3 (publicationYear, pages, synopsis) | 1 (description) | 4 (brand, imageUrl, weight) | 2 (distance, notes) | 2 (subtitle, featuredImageUrl) |
| **Relación con User** | userId (creator) | organizerId | registeredBy | recordedBy | authorId |

---

## PATRONES DE VALIDACIÓN SEGURO

### Patrón 1: Campo Required + Email
```javascript
body('email')
  .notEmpty().withMessage('Email requerido')
  .isEmail().withMessage('Email no válido')
  .normalizeEmail()
```

### Patrón 2: Campo Optional + Número
```javascript
body('age')
  .optional()
  .isInt({ min: 0, max: 150 }).withMessage('Edad entre 0-150')
```

### Patrón 3: Campo Required + Enum
```javascript
body('status')
  .isIn(['activo','inactivo','suspendido']).withMessage('Status no válido')
```

### Patrón 4: Campo Required + Rango de Caracteres
```javascript
body('title')
  .notEmpty()
  .isLength({ min: 5, max: 100 }).withMessage('Entre 5 y 100 caracteres')
```

### Patrón 5: Campo Optional + URL
```javascript
body('website')
  .optional()
  .isURL().withMessage('URL no válida')
```

---

## RELACIONES ENTRE MODELOS

```javascript
// Todos los modelos (Book, Event, Product, Workout, Article)
// tienen la misma relación con User:

User.hasMany(Book, { foreignKey: 'userId', as: 'books' });
Book.belongsTo(User, { foreignKey: 'userId', as: 'creator' });

// Luego en controladores:
const book = await Book.findByPk(id, {
  include: [{
    model: User,
    as: 'creator',
    attributes: ['id', 'username', 'fullName'],
  }],
});
```

---

## TEST RÁPIDO DE RUTAS

```bash
# 1. Registrar usuario
curl -X POST http://localhost:3000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{"username":"user1","email":"user1@example.com","password":"123456","fullName":"User One"}'

# 2. Login (obtener token)
curl -X POST http://localhost:3000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user1@example.com","password":"123456"}'

# Copiar el "token" de la respuesta

# 3. Crear recurso (requiere token y ser admin)
curl -X POST http://localhost:3000/api/books \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer COPIAR_TOKEN_AQUI" \
  -d '{"title":"1984","author":"Orwell","ISBN":"1234567890123","genre":"ficción","pages":328,"synopsis":"Novela distópica"}'

# 4. Obtener todos (sin autenticación)
curl -X GET http://localhost:3000/api/books

# 5. Obtener por ID
curl -X GET http://localhost:3000/api/books/1
```
