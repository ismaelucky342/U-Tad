# 📚 GUÍA DE ESTUDIO - WEB DEVELOPMENT II EXAM

## 🎯 ESTRUCTURA DEL MATERIAL

Este directorio contiene **5 archivos de referencia rápida** diseñados para el examen. Cada archivo está optimizado para ser consultado rápidamente durante la prueba.

---

## 📋 ARCHIVOS DE ESTUDIO

### 1. **CHULETA_COMPLETA.md** ⭐ COMIENZA AQUÍ
- **Propósito**: Resumen general de todo
- **Contenido**:
  - Field types de Sequelize (STRING, INTEGER, FLOAT, ENUM, JSON, DATE)
  - Validadores de express-validator (notEmpty, isEmail, isLength, etc.)
  - Middleware de autenticación (verifyToken, verifyAdmin)
  - Plantilla de controlador (CRUD completo)
  - Plantilla de rutas con Swagger
  - Plantilla de index.js
  - Checklist del examen
  - Errores comunes (versión corta)
- **Tiempo de lectura**: 10-15 minutos
- **Cuándo usar**: Primera revisión, repaso rápido

---

### 2. **CAMPOS_POR_MODELO.md** 🔧 REFERENCIA DE MODELOS
- **Propósito**: Comparación de campos entre los 5 modelos
- **Contenido**:
  - **Model_B (Library)**: Book con genre ENUM, ISBN, páginas
  - **Model_C (Events)**: Event con DateTime, category ENUM, ubicación
  - **Model_D (Products)**: Product con FLOAT (price, weight), stock INTEGER
  - **Model_E (Workouts)**: Workout con ENUM (activityType), campos opcionales
  - **Model_F (Articles)**: Article con JSON (tags), status ENUM, public filter
  - Tabla comparativa de características
  - Patrones de validación
  - Relaciones entre modelos
  - Test rápido con curl
- **Tiempo de lectura**: 5-10 minutos
- **Cuándo usar**: Cuando necesitas recordar campos específicos de un modelo

---

### 3. **AUTENTICACION_JWT.md** 🔐 AUTENTICACIÓN Y LOGIN
- **Propósito**: Completar sistema de login/registro
- **Contenido**:
  - `registerUser` controlador completo
  - `loginUser` controlador completo
  - `getUserProfile`, UpdateProfile, changePassword, deleteAccount
  - Rutas uteando /login, /register con esquemas swagger
  - Generación de JWT
  - Verificación de JWT
  - Flujo completo de autenticación
  - .env requerido
  - Testing con CURL
  - Versión simplificada para copiar rápido
  - Errores comunes en auth
- **Tiempo de lectura**: 8-12 minutos
- **Cuándo usar**: Implementar endpoints de usuarios, need generar tokens

---

### 4. **MIDDLEWARE_Y_PATRONES.md** ⚙️ CONFIGURACIÓN Y HELPERS
- **Propósito**: Componentes reutilizables en todas las APIs
- **Contenido**:
  - Validación de errores (handleValidationErrors)
  - CORS (desarrollo y producción)
  - Error handler global
  - Rating limiting (opcional)
  - Patrón de controlador robusto con try-catch
  - Patrón de controlador con relaciones
  - Patrón de actualización parcial
  - Patrón de delete con confirmación
  - Modelo completo con timestamp
  - Relaciones (hasMany, belongsTo)
  - Database.js (SQLite)
  - Swagger config
  - .env seguro
- **Tiempo de lectura**: 10-15 minutos
- **Cuándo usar**: Setup inicial, cuando copias middleware

---

### 5. **ERRORES_Y_TROUBLESHOOTING.md** 🚨 DEBUGGING RÁPIDO
- **Propósito**: Solucionar problemas en el examen
- **Contenido**:
  - Top 20 errores comunes (Token, JWT_SECRET, password, CORS, etc.)
  - Problema ↔️ Solución para cada error
  - Diagnóstico rápido (para error X → causa Y → solución Z)
  - Checklist final antes de entregar
  - Tips para ganar tiempo
  - Respuestas rápidas (snippets de 1 línea)
- **Tiempo de lectura**: 5-10 minutos
- **Cuándo usar**: Cuando algo no funciona en el examen

---

## 🚀 FLUJO RECOMENDADO

**Al empezar el examen (0-5 min):**
1. Abre este README
2. Lee la estructura
3. Revisa ERRORES_Y_TROUBLESHOOTING.md → Checklist

**Desarrollo (5-50 min):**
1. Copiar estructura de Model_A (o uno de los 5 modelos)
2. Cambiar nombres de entidades (Book → Tu_Entidad)
3. Consultar CAMPOS_POR_MODELO.md → Adaptar campos
4. Consultar MIDDLEWARE_Y_PATRONES.md → Copiar validadores/controladores
5. Consultar AUTENTICACION_JWT.md → Login/registro si aplica

**Testing (50-60 min):**
1. Probar endpoints con curl (en ERRORES_Y_TROUBLESHOOTING.md)
2. Si falla → ir a Sección correspondiente
3. Consultar ERRORES_Y_TROUBLESHOOTING.md → Diagnosticar

**Revisión (60-65 min):**
1. Ejecutar ERRORES_Y_TROUBLESHOOTING.md → Checklist
2. Verificar no olvidó nada crítico

---

## 🔑 CONCEPTOS CLAVE

### Autenticación
- **JWT**: Token con expiración (8h)
- **Bearer**: Formato `Authorization: Bearer TOKEN`
- **Roles**: Solo admins pueden POST/PUT/DELETE recurso secundario

### Modelos
- **Siempre 2**: User + Entidad secundaria (Book, Event, Product, etc.)
- **Relación**: User.hasMany(Entity), Entity.belongsTo(User)
- **Exclusión**: Nunca devolver password en JSON

### Validadores
- **express-validator**: body(), param() chaining
- **withMessage()**: Mensajes claros
- **handleValidationErrors**: Middleware siempre

### Seguridad
- Passwords con bcryptjs (hash)
- CORS habilitado
- Error handling global
- Validación en todas partes

---

## 📐 ESTRUCTURA DE UN MODELO

```
Model_X/
├── package.json (deps: express, sequelize, sqlite3, bcryptjs, jsonwebtoken, express-validator)
├── .env (PORT, DATABASE, JWT_SECRET)
├── database.sqlite (auto-creada)
└── src/
    ├── config/
    │   ├── database.js (SQLite)
    │   └── swagger.js (OpenAPI)
    ├── middleware/
    │   ├── auth.js (verifyToken, verifyAdmin)
    │   └── validationHandler.js (handleValidationErrors)
    ├── models/
    │   ├── User.js (id, username, email, password, fullName, isAdmin)
    │   └── Entity.js (Vary by domain)
    ├── controllers/
    │   ├── userController.js (register, login, profile)
    │   └── entityController.js (CRUD)
    ├── validators/
    │   ├── userValidators.js (email, password)
    │   └── entityValidators.js (domain-specific)
    ├── routes/
    │   ├── userRoutes.js (/register, /login, /profile)
    │   └── entityRoutes.js (CRUD + access control)
    ├── index.js (servidor, middlewares, DB sync)
    └── README.md (documentación rápida)
```

---

## 🧪 ENDPOINTS MÍNIMOS

**Endpoint usuarios:**
```
POST   /api/users/register         → Crear usuario
POST   /api/users/login            → Obtener token
GET    /api/users/profile          → Perfil autenticado
```

**Endpoint recursos:**
```
GET    /api/books                  → Listar todos (público)
GET    /api/books/:id              → Obtener uno (público)
POST   /api/books                  → Crear (admin only)
PUT    /api/books/:id              → Actualizar (admin only)
DELETE /api/books/:id              → Eliminar (admin only)
```

---

## 💡 QUICK TIPS

| Tarea | Archivo | Líneas |
|-------|---------|--------|
| Tipos de datos Sequelize | CHULETA_COMPLETA | 30-80 |
| Validadores express-validator | CHULETA_COMPLETA | 85-150 |
| GenerarToken JWT | AUTENTICACION_JWT | 5-15 |
| VerifyToken middleware | AUTENTICACION_JWT | 30-50 |
| Plantilla controlador CRUD | MIDDLEWARE_Y_PATRONES | 80-150 |
| Relaciones Sequelize | CAMPOS_POR_MODELO | 150-180 |
| Error Handler Global | MIDDLEWARE_Y_PATRONES | 20-60 |
| Solución problema X | ERRORES_Y_TROUBLESHOOTING | Busca por nombre |

---

## 🎓 MODELS DE REFERENCIA

Los 5 modelos disponibles en `/3th_Course/Q2/Web Development ll Server/EXAM/`:

1. **Model_A** (Weather API) - Referencia original
2. **Model_B** (Library API) - Books + Users
3. **Model_C** (Events API) - Events + Users
4. **Model_D** (Products API) - Products + Users
5. **Model_E** (Workouts API) - Workouts + Users
6. **Model_F** (Articles API) - Articles + Users

**Estrategia examen**: Copiar estructura de uno, cambiar nombres, adaptar campos.

---

## ⏱️ TIMING ESPERADO

- **Copia estructura + cambios**: 5-10 minutos
- **Implementar controlers/validadores**: 20-30 minutos
- **Rutas + middleware**: 10-15 minutos
- **Testing/debugging**: 10-15 minutos
- **Buffer/revisión**: 5-10 minutos

**Total**: 50-80 minutos (según complejidad)

---

## ✅ ÚLTIMA REVISIÓN

Antes de entregar:
- [ ] TODO funciona sin errores
- [ ] GET devuelve datos
- [ ] POST sólo admin
- [ ] PUT/DELETE sólo admin
- [ ] Password hasheado y excluído
- [ ] JWT verificable
- [ ] CORS funciona
- [ ] Swagger actualizado
- [ ] Base datos sincronizada

---

## 📞 AYUDA RÁPIDA

**"Mi token no funciona"** → Ver AUTENTICACION_JWT + ERRORES_Y_TROUBLESHOOTING

**"Validadores no trabajan"** → Ver CHULETA_COMPLETA + MIDDLEWARE_Y_PATRONES

**"No puedo crear usuario"** → Ver CAMPOS_POR_MODELO (Model_B) + AUTENTICACION_JWT

**"Quiero copiar controlador"** → Ver MIDDLEWARE_Y_PATRONES

**"Error X no entiendo"** → Ver ERRORES_Y_TROUBLESHOOTING → Busca error

---

**Buena suerte en el examen! 🍀**

*Última actualización: Exam prep 2024*
*Versión: 1.0 (Complete - Todos los 5 modelos disponibles)*
