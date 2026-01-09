# ABDS — Batería teórica por índice (chuleta larga)

Este documento convierte el índice de `ABDS_contenidos.md` en una **batería teórica**: para cada punto tienes **definición**, **ideas clave**, **preguntas típicas** y, cuando aplica, **mini-ejemplo**.

> Está pensado para repasar rápido y también para responder preguntas abiertas cortas en examen.

---

## Índice

- [Unidad 1 — BBDD NoSQL](#unidad-1--bbdd-nosql)
  - [Tipos de datos](#tipos-de-datos)
  - [Problemas/soluciones de las BBDD relacionales](#problemassoluciones-de-las-bbdd-relacionales)
  - [Propiedades ACID](#propiedades-acid)
  - [Impedance mismatch y ORM](#impedance-mismatch-y-orm)
  - [Escalado vertical vs horizontal](#escalado-vertical-vs-horizontal)
  - [Motivación del surgimiento de NoSQL](#motivación-del-surgimiento-de-nosql)
  - [Clasificación de las BBDD NoSQL](#clasificación-de-las-bbdd-nosql)
- [Unidad 2 — MongoDB (documentos)](#unidad-2--bbdd-orientadas-a-documentos-mongodb)
  - [Características básicas](#características-básicas-documentos)
  - [Rendimiento y diseño](#rendimiento-y-diseño-mongodb)
    - [Embedding vs referencing](#embedding-vs-referencing)
    - [Índices (noción general)](#índices-noción-general)
  - [Operaciones CRUD: consultas](#operaciones-crud-consultas)
  - [Operaciones CRUD: agregaciones](#operaciones-crud-agregaciones)
- [Unidad 3 — Redis (clave-valor)](#unidad-3--bbdd-orientadas-a-clave-valor-redis)
  - [Persistencia](#persistencia-redis)
  - [Clústeres](#clústeres-redis)
  - [Replicación](#replicación-redis)
  - [Casos de uso](#casos-de-uso-redis)
  - [Tipos de datos](#tipos-de-datos-redis)
  - [Operaciones por tipo](#operaciones-por-tipo)
  - [Pipelining](#pipelining)
  - [Transacciones](#transacciones-redis)
  - [Pub/Sub](#publicación-y-suscripción-pubsub)
  - [Eviction Policies](#eviction-policies)
- [Unidad 4 — Neo4j (grafos)](#unidad-4--bbdd-orientadas-a-grafos-neo4j)
  - [Nodos, relaciones, propiedades, etiquetas](#nodos-relaciones-propiedades-etiquetas)
  - [Cypher: operaciones](#cypher-operaciones)
  - [Cypher: patrones y consultas](#cypher-patrones-y-consultas)
  - [Índices y restricciones](#índices-y-restricciones-neo4j)
- [Unidad 5 — Chroma (vectores)](#unidad-5--bbdd-de-vectores-chroma)
  - [Vectores y embeddings](#vectores-y-embeddings)
  - [Estructura y modelo de datos](#estructura-y-modelo-de-datos-chroma)
  - [Aplicaciones](#aplicaciones-chroma)
  - [Búsquedas y familias de índices](#búsquedas-y-familias-de-índices)
  - [Sintaxis básica](#sintaxis-básica-de-chroma)
- [Unidad 6 — Cassandra (distribuidas)](#unidad-6--bbdd-distribuidas-cassandra)
  - [Características](#características-de-cassandra)
  - [Elementos del clúster](#elementos-del-clúster)
  - [Replicación](#replicación-cassandra)
  - [Niveles de consistencia](#niveles-de-consistencia)
  - [Write path](#write-path-flow)
  - [Read path](#read-path-flow)

---

## Unidad 1 — BBDD NoSQL

### Tipos de datos

**Qué es:** clasificación típica de información según estructura.

**Ideas clave:**
- **Estructurados:** encajan en tablas/esquema fijo (p. ej. facturas con campos fijos).
- **Semi-estructurados:** estructura flexible/jerárquica (JSON, XML).
- **No estructurados:** texto libre, audio, imágenes (aunque luego se indexa/embebe).

**Preguntas típicas:**
- ¿Por qué JSON encaja bien en documento?
- ¿Qué tipo de dato te empuja a NoSQL?

---

### Problemas/soluciones de las BBDD relacionales

**Qué es:** límites del modelo relacional “clásico” cuando el sistema crece o el dominio cambia rápido.

**Problemas comunes:**
- **Escalado horizontal** difícil (joins distribuidos, coordinación, particionado).
- **Rigidez de esquema** (migraciones constantes si cambia el modelo).
- **Joins costosos** para lecturas con latencia muy baja.
- **Impedance mismatch** con apps OO.

**Soluciones (o mitigaciones):**
- Replicación/particionado, cachés, denormalización controlada.
- En algunos dominios: adoptar NoSQL (según acceso y consistencia requerida).

---

### Propiedades ACID

**Qué es:** garantías transaccionales clásicas.

- **Atomicidad:** todo o nada.
- **Consistencia:** mantiene invariantes/constraints.
- **Aislamiento:** concurrencia sin efectos indeseados.
- **Durabilidad:** commit persiste.

**Mini-ejemplo (aislamiento):**
Dos compras compiten por el último stock; sin aislamiento, ambas podrían “ver” stock suficiente y vender de más.

**Preguntas típicas:**
- Define ACID.
- ¿Qué propiedad suele relajarse en sistemas distribuidos para ganar disponibilidad/escala?

---

### Impedance mismatch y ORM

**Qué es:** fricción entre objetos (clases, herencia, referencias) y tablas (filas, joins), que obliga a mapear.

**Consecuencias típicas:**
- Código extra (mapeos), consultas generadas, N+1 queries.
- Complejidad en relaciones y carga perezosa.

**Pregunta típica:**
- Explica el problema y por qué NoSQL documento a veces lo reduce (documentos más “naturales” para jerarquías).

---

### Escalado vertical vs horizontal

**Vertical (scale up):**
- Mejorar una máquina.
- Pros: simple.
- Contras: techo físico y coste no lineal.

**Horizontal (scale out):**
- Añadir máquinas y repartir.
- Pros: crece incrementalmente, mejor tolerancia a fallos.
- Contras: complejidad (sharding, replicación, consistencia, coordinación).

**Pregunta típica:**
- Compara rendimiento y coste.

---

### Motivación del surgimiento de NoSQL

**Motivaciones:**
- Escala web, necesidad de **baja latencia** y alto throughput.
- Datos semi-estructurados (JSON) y cambios de esquema rápidos.
- Arquitecturas distribuidas (replicación, particionado) como “first-class”.

**Trade-off típico:**
- A veces relajar consistencia fuerte/joins complejos.

---

### Clasificación de las BBDD NoSQL

**Familias principales:**
- **Documento** (MongoDB): flexibilidad + consultas.
- **Clave-valor** (Redis): ultra baja latencia.
- **Grafo** (Neo4j): relaciones y traversals.
- **Wide-column** (Cassandra): escrituras rápidas, escalado.
- **Vectoriales** (Chroma): búsqueda semántica por similitud.

**Pregunta típica:**
- Dado un caso de uso, elige la familia y justifica.

---

## Unidad 2 — BBDD orientadas a documentos. MongoDB

### Características básicas (documentos)

**Qué es:** almacena documentos (BSON/JSON) en colecciones.

**Ideas clave:**
- Esquema flexible (pero conviene definir convenciones).
- Documentos jerárquicos: arrays/subdocumentos.
- Consultas ricas (filtros, proyecciones, agregación).

---

### Rendimiento y diseño (MongoDB)

**Meta-idea:** diseña según patrones de acceso.

#### Embedding vs referencing

**Embedding:**
- Pros: lecturas rápidas (1 doc), consistencia local.
- Contras: crecimiento de doc, duplicación.

**Referencing:**
- Pros: normaliza, útil para 1–muchos grande.
- Contras: más consultas o `$lookup`.

**Regla práctica:**
- Embedded si se consulta “junto” y el tamaño es controlable.
- Referencias si es grande, reutilizable o muchos-a-muchos.

#### Índices (noción general)

**Qué es:** estructuras para acelerar búsquedas/ordenaciones.

**Trade-off:**
- +Rápido en lectura, -coste en escritura y almacenamiento.

**Pregunta típica:**
- Proponer índice para una consulta concreta y justificar.

---

### Operaciones CRUD: consultas

**Puntos que caen mucho:**
- `find` con filtros (`$gt`, `$gte`, `$in`, `$and`, `$or`).
- Proyección (campos que devuelves).
- `sort`, `limit`, paginación.

**Mini-ejemplo:**
```js
db.orders.find(
  { status: "PAID", total: { $gte: 50 } },
  { _id: 1, total: 1, createdAt: 1 }
).sort({ createdAt: -1 }).limit(10)
```

---

### Operaciones CRUD: agregaciones

**Qué es:** pipeline de etapas que transforman/agrupan.

**Etapas típicas:**
- `$match` (filtrar) — cuanto antes, mejor.
- `$group` (agrupar y acumular)
- `$project` (formatear)
- `$sort`, `$limit`
- `$lookup` (join)

**Mini-ejemplo:**
```js
db.orders.aggregate([
  { $match: { status: "PAID" } },
  { $group: { _id: "$customerId", spent: { $sum: "$total" } } },
  { $sort: { spent: -1 } },
  { $limit: 5 }
])
```

---

## Unidad 3 — BBDD orientadas a clave-valor. Redis

### Persistencia (Redis)

**Qué es:** mecanismos para no perder datos ante reinicios.

**Ideas clave:**
- **RDB** (snapshots): ligero, posible pérdida desde último snapshot.
- **AOF** (append-only file): registra operaciones, más durabilidad, más coste.
- Se pueden combinar.

---

### Clústeres (Redis)

**Qué es:** particionado + alta disponibilidad.

**Ideas clave:**
- Distribuye claves en slots.
- Cuidado con operaciones multi-key (si no caen en el mismo slot).

---

### Replicación (Redis)

**Qué es:** réplica de datos para lectura/HA.

**Idea clave:**
- Primario → réplicas; puede haber lag.

---

### Casos de uso (Redis)

- **BD en memoria:** contadores, estados rápidos.
- **Caché:** cache-aside, TTL.
- **Mensajería:** pub/sub, streams.

**Pregunta típica:**
- Justifica Redis como caché: latencia, TTL, eviction.

---

### Tipos de datos (Redis)

- Strings, Lists, Hashes, Sets, Sorted Sets, Bitmaps.

**Regla práctica:** elige tipo de dato por operación principal.

---

### Operaciones por tipo

**Strings:** `GET`, `SET`, `INCRBY`.

**Lists:** `LPUSH/RPUSH`, `LPOP/RPOP`, `LRANGE`.

**Hashes:** `HSET`, `HGETALL`, `HINCRBY`.

**Sets:** `SADD`, `SMEMBERS`, `SINTER`.

**Sorted sets:** `ZADD`, `ZREVRANGE WITHSCORES`, `ZINCRBY`.

**Bitmaps:** `SETBIT`, `GETBIT`, `BITCOUNT`.

**Iteradores:** `SCAN`, `HSCAN`, `SSCAN`, `ZSCAN`.

---

### Pipelining

**Qué es:** técnica para reducir latencia de red enviando muchos comandos seguidos.

**Clave:** no da atomicidad.

---

### Transacciones (Redis)

**MULTI/EXEC:** agrupa comandos evitando interleaving.

**Ojo:** si necesitas “if/then” atómico, suele ser mejor Lua (`EVAL`).

---

### Publicación y suscripción (pub/sub)

**Qué es:** messaging efímero.

- `SUBSCRIBE canal`
- `PUBLISH canal mensaje`

**Clave:** si no estás suscrito, lo pierdes.

---

### Eviction Policies

**Qué es:** políticas de expulsión al llegar al límite de memoria.

Ejemplos:
- `noeviction`
- `allkeys-lru`
- `volatile-lru`

**Caso típico de examen:**
- Redis como caché: elegir política según si todas las claves tienen TTL, impacto en sesiones, etc.

---

## Unidad 4 — BBDD orientadas a grafos. Neo4j

### Nodos, relaciones, propiedades, etiquetas

**Ideas clave:**
- **Nodo**: entidad.
- **Relación**: conecta nodos, tiene tipo y propiedades.
- **Propiedades**: pares clave-valor.
- **Etiquetas**: “clases” de nodos.

---

### Cypher: operaciones

- Crear nodos: `CREATE (u:User {id: 1})`
- Crear relaciones: `CREATE (u)-[:RATED {stars: 5}]->(m)`
- Actualizar: `SET u.name = "Ana"`

---

### Cypher: patrones y consultas

**Pattern matching:**
- `MATCH (u:User)-[:RATED]->(m:Movie)`
- `WHERE ...`
- `RETURN ...`

**Agregación:** `count`, `sum`, `avg`.

**Pregunta típica:**
- Recomendación simple por “vecinos” (usuarios similares).

---

### Índices y restricciones (Neo4j)

- Índices para encontrar nodos por propiedad rápido.
- Constraints para integridad (unicidad, existencia).

Ejemplo unicidad:
```cypher
CREATE CONSTRAINT user_id_unique IF NOT EXISTS
FOR (u:User)
REQUIRE u.id IS UNIQUE
```

---

## Unidad 5 — BBDD de vectores. Chroma

### Vectores y embeddings

**Qué es:**
- Vector = lista de números.
- Embedding = vector que captura semántica.

**Idea clave:** búsqueda por similitud (coseno/L2 según sistema).

---

### Estructura y modelo de datos (Chroma)

**Qué sueles guardar:**
- `id`
- `embedding`
- `document` (texto)
- `metadata` (fuente, tema, fecha…)

---

### Aplicaciones (Chroma)

- **RAG:** recuperar chunks relevantes para un LLM.
- **Recomendación:** items similares.
- **Deduplicación:** detectar near-duplicates.
- **MMR:** diversidad + relevancia.

---

### Búsquedas y familias de índices

**Idea general:**
- Exacto vs aproximado (ANN).
- Índices para acelerar nearest neighbors.

**Pregunta típica:**
- ¿Por qué ANN? (trade-off precisión vs velocidad/memoria).

---

### Sintaxis básica de Chroma

Pseudo-ejemplo:
```python
collection.add(ids=["1"], documents=["texto"], metadatas=[{"topic": "nosql"}])
collection.query(query_texts=["buscar"], n_results=3)
```

---

## Unidad 6 — BBDD distribuidas. Cassandra

### Características de Cassandra

**Claves:**
- Distribuida, escalable horizontalmente.
- Optimizada para escrituras.
- Consistencia configurable por operación.

---

### Elementos del clúster

- **Nodo**, **partición**, **rack**, **data center**, **clúster**.
- **Nodo semilla**: ayuda al descubrimiento/bootstrapping.
- **Coordinador**: nodo que recibe la petición y coordina con réplicas.
- **Token ring**: asignación de rangos de token.
- **Vnodes**: cada nodo maneja múltiples rangos, mejora balanceo.

---

### Replicación (Cassandra)

**Qué es:** almacenar replicas según RF y estrategia por DC/rack.

**Por qué:** HA y lectura/escritura distribuidas.

---

### Niveles de consistencia

- `ONE`, `QUORUM`, `ALL`.
- En multi-DC: `LOCAL_QUORUM`.

**Relación rápida con RF=3:**
- `QUORUM` = 2.

---

### Write path flow

**Flujo (alto nivel):**
1) Coordinador envía a réplicas.
2) Réplica escribe en **commit log** (durabilidad) + **memtable**.
3) Flush a disco a **SSTables**.
4) Compaction reorganiza SSTables.

---

### Read path flow

**Flujo (alto nivel):**
1) Coordinador consulta réplicas según consistencia.
2) Réplica mira **memtable** y **SSTables**.
3) Combina resultados (y tombstones).
4) Puede haber read repair.

---
