# AEC2 - Consultas y Agregaciones en MongoDB

---

## Introducción

Esta actividad práctica comienza con un dataset de **120 librerías de Madrid** distribuidas uniformemente en 8 distritos (Centro, Salamanca, Retiro..etc). Cada documento incluye:

- Nombre y ubicación completa (distrito, barrio, dirección con coordenadas)
- Categorías de libros que tienen (array)
- Idiomas disponibles (array)
- Nivel de precios, año de apertura y las valoraciones de usuarios
- Capacidad y superficie del local
- Eventos programados con tipo, fecha y asistencia esperada
- Si pertenecen a alguna cadena de librerías

El objetivo es sacarle información útil a través de consultas básicas y agregaciones más complejas en la base de datos `bookstores_db`, todo en la colección `bookstores`.

---

## Desarrollo e información técnica

Inicialmente hice esta práctica con otro enunciado y dataset (restaurantes de Nueva York, que está en la carpeta `AEC2A`). Las fechas de creación de los archivos `queries.js` (23/10/2025) y `run_queries.sh` (03/11/2025) vienen de ahí, pero he reutilizado y adaptado bastante código para esta versión con las librerías madrileñas.

El nuevo enunciado pedía entregarlo en PDF, pero me pareció mejor ampliar la entrega con:
- Un script JavaScript (`queries.js`) con las 20 consultas bien comentadas
- Un script bash (`run_queries.sh`) que automatiza la importación y ejecución
- El txt con los resultados reales de las queries

Me parece más práctico y reproducible, además de demostrar mejor cómo uso MongoDB y cómo puedo automatizar procesos.

---

## Tareas

He dividido la práctica en dos bloques bien diferenciados:

**Consultas básicas (1-10):**
1. Contar el total de librerías
2. Librerías abiertas desde 2018 (ordenadas por año)
3. Librerías que ofrecen libros en francés
4. Librerías con capacidad ≥ 80 y superficie ≥ 200 (top 10)
5. Librerías pertenecientes a cadenas
6. En Chamberí, librerías con libros en inglés
7. Librerías con categorías "academic" y "art" simultáneamente
8. Librerías baratas ($) con buena valoración (≥ 4.5)
9. Librerías con eventos programados
10. En Salamanca, librerías con workshops

**Agregaciones (11-20):**
11. Número de librerías por distrito
12. Valoración media por distrito
13. Top 5 barrios por rating (con 3+ librerías)
14. Recuento de librerías por categoría
15. Superficie y capacidad media por categoría
16. Densidad media (personas/m²) por distrito
17. Número de eventos por mes en 2025
18. Proporción de librerías con inglés por distrito
19. Top 5 librerías mejor valoradas
20. Asistencia esperada por tipo de evento (Q2 2025)

---

## Configuración Inicial

### Importación de datos

```bash
mongoimport --db bookstores_db --collection bookstores --file bookstores.json --jsonArray --drop
```

### Ejecución de consultas

**Opción 1: Script automático (recomendado)**
```bash
./run_queries.sh
```

**Opción 2: Manual**
```bash
# 1. Importar datos
mongoimport --db bookstores_db --collection bookstores --file bookstores.json --jsonArray --drop

# 2. Ejecutar consultas y guardar resultados
mongosh bookstores_db < queries.js > query_results.txt
```

---

## Estructura del Proyecto

```
AEC2B/
├── bookstores.json                   # Dataset de 120 librerías
├── queries.js                        # 20 consultas con comentarios
├── run_queries.sh                    # Script de automatización
├── query_results.txt                 # Salida completa de ejecución
└── README.md                         # Esta documentación
```

---

## Instrucciones de Uso

**Setup rápido:**
```bash
chmod +x run_queries.sh
./run_queries.sh
```

Este script realiza automáticamente:
1. Importación del JSON a MongoDB (con `--drop` para limpiar datos previos)
2. Ejecución de todas las consultas
3. Guardado de resultados en `query_results.txt`

**Uso manual:**
```bash
# Importar datos
mongoimport --db bookstores_db --collection bookstores --file bookstores.json --jsonArray --drop

# Ejecutar consultas
mongosh bookstores_db < queries.js > query_results.txt
```

**Verificar importación:**
```javascript
mongosh bookstores_db
db.bookstores.countDocuments()  // Debe devolver 120
db.bookstores.findOne()         // Ver documento de ejemplo
```

---

## CONSULTAS BÁSICAS

### 1. Número total de librerías

Cuento todos los documentos en la colección usando `countDocuments()` sin filtros.

```javascript
db.bookstores.countDocuments();
```

**Salida:**
```
120
```

---

### 2. Librerías abiertas desde 2018 ordenadas de más nuevas a más antiguas

Filtro por `year_opened >= 2018` y ordeno descendentemente. Proyecto solo nombre y año.

```javascript
db.bookstores.find(
  { year_opened: { $gte: 2018 } },  // Filtro: año >= 2018
  { name: 1, year_opened: 1, _id: 0 }  // Proyección: solo nombre y año, sin _id
).sort({ year_opened: -1 });  // Orden descendente (-1) por año
```

**Salida:**
```json
{ "name": "Book&Beans - Bellas Vistas", "year_opened": 2025 }
{ "name": "Estudios y Manuales - Goya", "year_opened": 2024 }
{ "name": "Arapiles Anticuaria - Cuatro Caminos", "year_opened": 2024 }
{ "name": "Recoletos Books - Castillejos", "year_opened": 2024 }
{ "name": "Rincón del Lector - Goya", "year_opened": 2024 }
{ "name": "Rincón del Lector - Ibiza", "year_opened": 2023 }
{ "name": "Cómic Central - Jerónimos", "year_opened": 2023 }
{ "name": "Anticuaria - Pacífico", "year_opened": 2023 }
...
```
_Total: 27 librerías abiertas desde 2018_

---

### 3. Librerías que ofrecen libros en francés

Busco en el array `languages` si contiene "fr".

```javascript
db.bookstores.find(
  { languages: "fr" },  // MongoDB busca "fr" dentro del array languages
  { name: 1, borough: 1, _id: 0 }  // Solo muestro nombre y distrito
);
```

**Salida:**
```json
{ "name": "Anticuaria - Recoletos", "borough": "Salamanca" }
{ "name": "El Atril - Guindalera", "borough": "Salamanca" }
{ "name": "Anticuaria - Lista", "borough": "Salamanca" }
{ "name": "Rincón del Lector - Lista", "borough": "Salamanca" }
{ "name": "Arapiles Anticuaria - Adelfas", "borough": "Retiro" }
{ "name": "Rincón del Lector - Ibiza", "borough": "Retiro" }
...
```
_Total: 31 librerías ofrecen francés_

---

### 4. Librerías con capacidad ≥ 80 y superficie ≥ 200 (Top 10)

Filtro por ambas condiciones a la vez y ordeno por capacidad descendente, limitando a 10 resultados.

```javascript
db.bookstores.find(
  { 
    capacity: { $gte: 80 },  // Capacidad mayor o igual a 80 personas
    area_sqm: { $gte: 200 }  // Superficie mayor o igual a 200 m²
  },
  { name: 1, capacity: 1, area_sqm: 1, _id: 0 }  // Proyecto los tres campos relevantes
).sort({ capacity: -1 })  // Orden por capacidad descendente
 .limit(10);  // Solo los 10 primeros
```

**Salida:**
```json
{ "name": "El Atril - Almenara", "capacity": 178, "area_sqm": 693 }
{ "name": "Arapiles Anticuaria - Recoletos", "capacity": 177, "area_sqm": 591 }
{ "name": "Savia de Tinta - Delicias", "capacity": 177, "area_sqm": 401 }
{ "name": "Arte y Ensayo - Guindalera", "capacity": 177, "area_sqm": 622 }
{ "name": "Estudios y Manuales - Canillas", "capacity": 176, "area_sqm": 687 }
{ "name": "Comicverse - Pacífico", "capacity": 169, "area_sqm": 430 }
{ "name": "Cómic Central - Arapiles", "capacity": 167, "area_sqm": 479 }
{ "name": "Cómic Central - Imperial", "capacity": 166, "area_sqm": 466 }
{ "name": "Estudios y Manuales - Valdezarza", "capacity": 166, "area_sqm": 589 }
{ "name": "Cómic Central - Malasaña", "capacity": 164, "area_sqm": 575 }
```

---

### 5. Librerías que pertenecen a una cadena

Uso `$exists: true` para verificar que tienen el campo `chain`.

```javascript
db.bookstores.find(
  { chain: { $exists: true } },  // Solo documentos que tienen el campo chain
  { name: 1, "chain.name": 1, "chain.branch_id": 1, _id: 0 }  // Accedo a subcampos con notación de punto
);
```

**Salida:**
```json
{ "name": "Recoletos Books - Sol", "chain": { "name": "PageTurners", "branch_id": "PT-216" } }
{ "name": "Anticuaria - Cortes", "chain": { "name": "LibroMundo", "branch_id": "LM-251" } }
{ "name": "Estudios y Manuales - Lavapiés", "chain": { "name": "Paper&Co", "branch_id": "PCO-688" } }
{ "name": "Arapiles Anticuaria - Chueca", "chain": { "name": "LibroMundo", "branch_id": "LM-374" } }
{ "name": "Estudios y Manuales - Chueca", "chain": { "name": "Paper&Co", "branch_id": "PCO-409" } }
...
```
_Total: 37 librerías pertenecen a una cadena_

---

### 6. En Chamberí, librerías que ofrecen libros en inglés

Doble condición: `borough = "Chamberí"` AND "en" en `languages`.

```javascript
db.bookstores.find(
  { 
    borough: "Chamberí",  // Primera condición: distrito específico
    languages: "en"  // Segunda condición: "en" presente en el array
  },
  { name: 1, languages: 1, _id: 0 }  // Muestro nombre y todos los idiomas disponibles
);
```

**Salida:**
```json
{ "name": "Lectores Unidos - Vallehermoso", "languages": [ "de", "en", "es" ] }
{ "name": "El Lomo Verde - Trafalgar", "languages": [ "en", "es", "fr" ] }
{ "name": "Arte y Ensayo - Trafalgar", "languages": [ "en", "es" ] }
{ "name": "Book&Beans - Trafalgar", "languages": [ "de", "en", "es" ] }
{ "name": "Luz de Papel - Trafalgar", "languages": [ "en", "es" ] }
{ "name": "El Atril - Arapiles", "languages": [ "en", "es" ] }
{ "name": "Comicverse - Ríos Rosas", "languages": [ "en", "es" ] }
{ "name": "Cómic Central - Arapiles", "languages": [ "en", "es" ] }
{ "name": "Arapiles Anticuaria - Arapiles", "languages": [ "de", "en", "es" ] }
```

---

### 7. Librerías cuya categoría incluya a la vez "academic" y "art"

Uso `$all` para asegurarme de que el array contenga AMBAS categorías.

```javascript
db.bookstores.find(
  { 
    categories: { $all: ["academic", "art"] }  // $all: el array debe contener AMBOS elementos
  },
  { name: 1, borough: 1, neighborhood: 1, _id: 0 }  // Ubicación completa
);
```

**Salida:**
```json
{ "name": "Anticuaria - Malasaña", "borough": "Centro", "neighborhood": "Malasaña" }
{ "name": "Arte y Ensayo - Guindalera", "borough": "Salamanca", "neighborhood": "Guindalera" }
{ "name": "Luz de Papel - Jerónimos", "borough": "Retiro", "neighborhood": "Jerónimos" }
{ "name": "Arte y Ensayo - Trafalgar", "borough": "Chamberí", "neighborhood": "Trafalgar" }
```

---

### 8. Librerías de precio "$" y valoración media ≥ 4.5

Combino `price_level = "$"` con `rating.avg >= 4.5`.

```javascript
db.bookstores.find(
  { 
    price_level: "$",  // Precio bajo
    "rating.avg": { $gte: 4.5 }  // Valoración alta (notación de punto para subcampos)
  },
  { name: 1, neighborhood: 1, "rating.avg": 1, _id: 0 }  // Proyecto rating.avg específicamente
);
```

**Salida:**
```json
{ "name": "Arapiles Anticuaria - Chueca", "neighborhood": "Chueca", "rating": { "avg": 4.8 } }
{ "name": "Libromanía - Guindalera", "neighborhood": "Guindalera", "rating": { "avg": 4.9 } }
{ "name": "Book&Beans - Ibiza", "neighborhood": "Ibiza", "rating": { "avg": 4.8 } }
{ "name": "Lectores Unidos - Vallehermoso", "neighborhood": "Vallehermoso", "rating": { "avg": 4.6 } }
{ "name": "Rincón del Lector - Imperial", "neighborhood": "Imperial", "rating": { "avg": 4.9 } }
{ "name": "Arte y Ensayo - Argüelles", "neighborhood": "Argüelles", "rating": { "avg": 4.5 } }
{ "name": "Estudios y Manuales - Valdezarza", "neighborhood": "Valdezarza", "rating": { "avg": 4.8 } }
{ "name": "Estudios y Manuales - Canillas", "neighborhood": "Canillas", "rating": { "avg": 4.6 } }
{ "name": "Arte y Ensayo - Palomas", "neighborhood": "Palomas", "rating": { "avg": 4.7 } }
```

---

### 9. Librerías con algún evento planificado

El campo `events` debe existir Y no ser un array vacío.

```javascript
db.bookstores.find(
  { 
    events: { $exists: true, $ne: [] }  // $exists verifica que existe, $ne: [] que no está vacío
  },
  { name: 1, borough: 1, _id: 0 }
);
```

**Salida:** _(muestra algunas)_
```json
{ "name": "Recoletos Books - Sol", "borough": "Centro" }
{ "name": "Anticuaria - Cortes", "borough": "Centro" }
{ "name": "Estudios y Manuales - Lavapiés", "borough": "Centro" }
{ "name": "Arapiles Anticuaria - Chueca", "borough": "Centro" }
{ "name": "Anticuaria - Recoletos", "borough": "Salamanca" }
...
```
_Total: 102 librerías tienen eventos programados_

---

### 10. En el distrito de Salamanca, librerías con eventos tipo "workshop"

Busco dentro del array `events` algún elemento con `type = "workshop"`.

```javascript
db.bookstores.find(
  { 
    borough: "Salamanca",  // Filtro de distrito
    "events.type": "workshop"  // Busca en array de objetos: algún evento con type="workshop"
  },
  { name: 1, _id: 0 }
);
```

**Salida:**
```json
{ "name": "Arte y Ensayo - Guindalera" }
{ "name": "Anticuaria - Lista" }
{ "name": "Arte y Ensayo - Guindalera" }
{ "name": "Rincón del Lector - Goya" }
```

---

## AGREGACIONES

### Índice sobre fechas de eventos

Antes de empezar con las agregaciones, creo un índice sobre las fechas para mejorar el rendimiento.

```javascript
db.bookstores.createIndex({ "events.date": 1 });  // Índice ascendente en el campo date dentro del array events
```

**Salida:**
```
events.date_1
```

---

### 11. Número de librerías por distrito

Simple: agrupo por `borough` y sumo 1 para contar.

```javascript
db.bookstores.aggregate([
  { $group: { 
      _id: "$borough",  // Agrupo por el campo borough
      count: { $sum: 1 }  // Cuento: sumo 1 por cada documento
    } 
  },
  { $sort: { count: -1 } }  // Ordeno por cantidad descendente
]);
```

**Salida:**
```json
{ "_id": "Hortaleza", "count": 15 }
{ "_id": "Chamberí", "count": 15 }
{ "_id": "Salamanca", "count": 15 }
{ "_id": "Centro", "count": 15 }
{ "_id": "Retiro", "count": 15 }
{ "_id": "Arganzuela", "count": 15 }
{ "_id": "Moncloa-Aravaca", "count": 15 }
{ "_id": "Tetuán", "count": 15 }
```

**Análisis:** La distribución es perfectamente uniforme (15 librerías por distrito).

---

### 12. Valoración media por distrito (orden descendente)

Calculo `$avg` sobre `rating.avg` y ordeno de mejor a peor.

```javascript
db.bookstores.aggregate([
  { $group: { 
      _id: "$borough",  // Agrupo por distrito
      avg_rating: { $avg: "$rating.avg" }  // Promedio del campo rating.avg
    } 
  },
  { $sort: { avg_rating: -1 } }  // Ordeno por rating descendente
]);
```

**Salida:**
```json
{ "_id": "Moncloa-Aravaca", "avg_rating": 4.193333333333333 }
{ "_id": "Chamberí", "avg_rating": 4.04 }
{ "_id": "Salamanca", "avg_rating": 4.02 }
{ "_id": "Retiro", "avg_rating": 4.02 }
{ "_id": "Centro", "avg_rating": 3.94 }
{ "_id": "Tetuán", "avg_rating": 3.8866666666666663 }
{ "_id": "Hortaleza", "avg_rating": 3.8333333333333335 }
{ "_id": "Arganzuela", "avg_rating": 3.7733333333333334 }
```

**Análisis:** Moncloa-Aravaca tiene la mejor valoración media (4.19).

---

### 13. Top 5 barrios por rating medio (solo barrios con 3+ librerías)

Agrupo por barrio, cuento, filtro con `$match` los que tengan >= 3 librerías y me quedo con el top 5.

```javascript
db.bookstores.aggregate([
  {
    $group: {
      _id: "$neighborhood",  // Agrupo por barrio
      avg_rating: { $avg: "$rating.avg" },  // Calculo el promedio de ratings
      count: { $sum: 1 }  // Cuento cuántas librerías hay en cada barrio
    }
  },
  { $match: { count: { $gte: 3 } } },  // Filtro: solo barrios con 3 o más librerías
  { $sort: { avg_rating: -1 } },  // Ordeno por rating descendente
  { $limit: 5 }  // Me quedo con los 5 mejores
]);
```

**Salida:**
```json
{ "_id": "Argüelles", "avg_rating": 4.4, "count": 5 }
{ "_id": "Guindalera", "avg_rating": 4.375, "count": 4 }
{ "_id": "Niño Jesús", "avg_rating": 4.266666666666667, "count": 3 }
{ "_id": "Cortes", "avg_rating": 4.233333333333333, "count": 3 }
{ "_id": "Castillejos", "avg_rating": 4.233333333333333, "count": 3 }
```

**Análisis:** Argüelles es el barrio mejor valorado con 4.4 de media.

---

### 14. Recuento por categoría

Como `categories` es un array, uso `$unwind` para "desplegar" cada valor y luego agrupar.

```javascript
db.bookstores.aggregate([
  { $unwind: "$categories" },  // Descompongo el array: un documento por cada categoría
  { $group: { 
      _id: "$categories",  // Agrupo por cada categoría
      count: { $sum: 1 }  // Cuento cuántas veces aparece cada una
    } 
  },
  { $sort: { count: -1 } }  // Ordeno de mayor a menor
]);
```

**Salida:**
```json
{ "_id": "academic", "count": 37 }
{ "_id": "children", "count": 27 }
{ "_id": "general", "count": 27 }
{ "_id": "comics", "count": 26 }
{ "_id": "art", "count": 24 }
{ "_id": "second_hand", "count": 23 }
```

**Análisis:** "Academic" es la categoría más común (37 librerías).

---

### 15. Media de superficie y aforo por categoría

Mismo truco: unwind para separar las categorías y luego agrupar calculando medias.

```javascript
db.bookstores.aggregate([
  { $unwind: "$categories" },  // Descompongo el array categories
  {
    $group: {
      _id: "$categories",
      avg_area: { $avg: "$area_sqm" },  // Promedio de superficie
      avg_capacity: { $avg: "$capacity" }  // Promedio de capacidad
    }
  },
  { $sort: { avg_area: -1 } }  // Ordeno por superficie descendente
]);
```

**Salida:**
```json
{ "_id": "art", "avg_area": 477.0416666666667, "avg_capacity": 87.04166666666667 }
{ "_id": "general", "avg_area": 468.6666666666667, "avg_capacity": 91.37037037037037 }
{ "_id": "academic", "avg_area": 424.13513513513516, "avg_capacity": 91.91891891891892 }
{ "_id": "second_hand", "avg_area": 419.95652173913044, "avg_capacity": 94.34782608695652 }
{ "_id": "children", "avg_area": 412.74074074074076, "avg_capacity": 101 }
{ "_id": "comics", "avg_area": 396.0769230769231, "avg_capacity": 85.38461538461539 }
```

**Análisis:** Las librerías de arte tienen la mayor superficie media (477 m²), mientras que las de niños tienen mayor capacidad (101 personas).

---

### 16. Densidad media (aforo/área) por distrito

Primero calculo la densidad con `$addFields`, luego agrupo y promedío.

```javascript
db.bookstores.aggregate([
  { $addFields: { 
      density: { $divide: ["$capacity", "$area_sqm"] }  // Creo campo temporal: densidad = capacidad/superficie
    } 
  },
  { $group: { 
      _id: "$borough", 
      avg_density: { $avg: "$density" }  // Promedio de densidad por distrito
    } 
  },
  { $sort: { avg_density: -1 } }  // Ordeno por densidad descendente
]);
```

**Salida:**
```json
{ "_id": "Salamanca", "avg_density": 0.47323746860282334 }
{ "_id": "Centro", "avg_density": 0.42851717412439877 }
{ "_id": "Retiro", "avg_density": 0.35864740954808105 }
{ "_id": "Tetuán", "avg_density": 0.31892443738039405 }
{ "_id": "Moncloa-Aravaca", "avg_density": 0.3038118978098344 }
{ "_id": "Hortaleza", "avg_density": 0.29506885861323134 }
{ "_id": "Arganzuela", "avg_density": 0.28852114993135874 }
{ "_id": "Chamberí", "avg_density": 0.27656994635016513 }
```

**Análisis:** Salamanca tiene la mayor densidad (0.47 personas/m²), lo que indica espacios más aprovechados.

---

### 17. Conteo de eventos por mes en 2025

Despliego events, filtro por año 2025 y extraigo el mes con `$month`.

```javascript
db.bookstores.aggregate([
  { $unwind: "$events" },  // Descompongo el array events
  {
    $match: {
      "events.date": {  // Filtro por rango de fechas
        $gte: ISODate("2025-01-01T00:00:00Z"),  // Desde 1 enero 2025
        $lt: ISODate("2026-01-01T00:00:00Z")  // Hasta 31 diciembre 2025
      }
    }
  },
  { $group: { 
      _id: { $month: "$events.date" },  // Extraigo el mes de la fecha y agrupo
      count: { $sum: 1 }  // Cuento eventos por mes
    } 
  },
  { $sort: { _id: 1 } },  // Ordeno por mes (1=enero, 12=diciembre)
  { $project: { _id: 0, month: "$_id", count: 1 } }  // Renombro _id a month
]);
```

**Salida:**
```json
{ "month": 1, "count": 4 }
{ "month": 2, "count": 6 }
{ "month": 3, "count": 5 }
{ "month": 4, "count": 2 }
{ "month": 5, "count": 5 }
{ "month": 6, "count": 6 }
{ "month": 7, "count": 9 }
{ "month": 8, "count": 3 }
{ "month": 9, "count": 4 }
{ "month": 10, "count": 9 }
{ "month": 11, "count": 6 }
{ "month": 12, "count": 1 }
```

**Análisis:** Julio y octubre son los meses con más actividad (9 eventos cada uno).

---

### 18. Proporción de librerías que ofrecen inglés por distrito

Uso `$cond` para contar las que tienen "en" y calculo el porcentaje.

```javascript
db.bookstores.aggregate([
  {
    $group: {
      _id: "$borough",
      total: { $sum: 1 },  // Cuento total de librerías por distrito
      with_english: {
        $sum: { $cond: [{ $in: ["en", "$languages"] }, 1, 0] }  // Cuento solo si "en" está en languages
      }
    }
  },
  {
    $project: {
      _id: 1,
      total: 1,
      with_english: 1,
      proportion: { $multiply: [{ $divide: ["$with_english", "$total"] }, 100] }  // Calculo porcentaje
    }
  },
  { $sort: { proportion: -1 } }  // Ordeno por proporción descendente
]);
```

**Salida:**
```json
{ "_id": "Chamberí", "total": 15, "with_english": 9, "proportion": 60 }
{ "_id": "Retiro", "total": 15, "with_english": 7, "proportion": 46.666666666666664 }
{ "_id": "Tetuán", "total": 15, "with_english": 5, "proportion": 33.33333333333333 }
{ "_id": "Centro", "total": 15, "with_english": 4, "proportion": 26.666666666666668 }
{ "_id": "Hortaleza", "total": 15, "with_english": 3, "proportion": 20 }
{ "_id": "Salamanca", "total": 15, "with_english": 3, "proportion": 20 }
{ "_id": "Arganzuela", "total": 15, "with_english": 3, "proportion": 20 }
{ "_id": "Moncloa-Aravaca", "total": 15, "with_english": 3, "proportion": 20 }
```

**Análisis:** Chamberí es el distrito más internacional (60% de librerías ofrecen inglés).

---

### 19. Top 5 librerías por valoración

Simplemente ordeno por `rating.avg` descendente y limito a 5.

```javascript
db.bookstores.aggregate([
  { $sort: { "rating.avg": -1 } },  // Ordeno por rating descendente
  { $limit: 5 },  // Solo las 5 mejores
  { $project: { 
      _id: 0, 
      name: 1, 
      borough: 1, 
      rating: "$rating.avg"  // Renombro rating.avg a rating
    } 
  }
]);
```

**Salida:**
```json
{ "name": "Rincón del Lector - Pinar del Rey", "borough": "Hortaleza", "rating": 5 }
{ "name": "Savia de Tinta - Cortes", "borough": "Centro", "rating": 5 }
{ "name": "Estudios y Manuales - Chueca", "borough": "Centro", "rating": 5 }
{ "name": "Rincón del Lector - Imperial", "borough": "Arganzuela", "rating": 4.9 }
{ "name": "Libromanía - Guindalera", "borough": "Salamanca", "rating": 4.9 }
```

**Análisis:** Tres librerías tienen valoración perfecta de 5.0.

---

### 20. Asistencia total esperada por tipo de evento (Q2 2025)

Rango marzo-junio 2025, despliego eventos y sumo `expected_attendance`.

```javascript
db.bookstores.aggregate([
  { $unwind: "$events" },  // Descompongo el array de eventos
  {
    $match: {  // Filtro solo eventos en Q2 2025 (marzo-junio)
      "events.date": {
        $gte: ISODate("2025-03-01T00:00:00Z"),  // Desde 1 marzo
        $lte: ISODate("2025-06-30T23:59:59Z")  // Hasta 30 junio
      }
    }
  },
  {
    $group: {
      _id: "$events.type",  // Agrupo por tipo de evento
      total_attendance: { $sum: "$events.expected_attendance" }  // Sumo asistencia esperada
    }
  },
  { $sort: { total_attendance: -1 } }  // Ordeno por asistencia descendente
]);
```

**Salida:**
```json
{ "_id": "reading", "total_attendance": 434 }
{ "_id": "workshop", "total_attendance": 288 }
{ "_id": "signing", "total_attendance": 254 }
{ "_id": "exhibition", "total_attendance": 227 }
{ "_id": "kids", "total_attendance": 80 }
```

**Análisis:** Los clubes de lectura ("reading") son los eventos más populares con 434 asistentes esperados en Q2.

---

## Extras

Esta práctica me ha servido para profundizar bastante en MongoDB más allá de lo que habíamos visto en clase. Al principio parece que son 20 consultas sueltas, pero en realidad hay una progresión de dificultad bastante bien pensada. Los primeros ejercicios (1-10) son bastante directos: operadores de comparación, búsquedas en arrays, proyecciones. 

A partir del 11 es donde entran las agregaciones y ahí la cosa cambia. Lo que más me ha costado ha sido el ejercicio 18 con las proporciones, porque usar `$cond` dentro de `$group` para contar condicionalmente no es nada intuitivo. Y el 13 me obligó a darme cuenta de que el orden de las etapas en el pipeline es crítico, si pones `$match` antes o después del `$group` obtienes resultados totalmente diferentes.

El script bash de automatización ha sido útil porque me permite ejecutar todo de golpe y guardar los resultados, mucho más eficiente que ir copiando queries una por una. En general, la práctica está bien estructurada y te obliga a usar prácticamente todo el repertorio de operadores de MongoDB.


![alt text](image-1.png)