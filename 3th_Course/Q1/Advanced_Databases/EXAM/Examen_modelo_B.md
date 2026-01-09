# Examen modelo B — ABDS (resuelto)

> Este modelo cambia el foco: más diseño/rendimiento y añade una práctica de **Chroma** y conceptos de **Cassandra** (además de Mongo/Redis/Neo4j).

---

## Parte 1 — Cuestiones breves

### 1) ¿Qué es consistencia eventual?

**Respuesta:**
En un sistema distribuido, significa que si no hay nuevas actualizaciones, **todas las réplicas convergerán** a un mismo valor con el tiempo, pero no necesariamente de forma inmediata tras una escritura.

### 2) NoSQL: nombra 4 familias y una ventaja típica de cada una

**Respuesta:**
- **Documento (MongoDB):** flexibilidad de esquema y consultas ricas sin joins.
- **Clave-valor (Redis):** latencia muy baja y simplicidad.
- **Grafo (Neo4j):** consultas eficientes sobre relaciones y traversals.
- **Columnas (wide-column, p. ej. Cassandra):** alto rendimiento en escrituras y escalabilidad horizontal.

### 3) En MongoDB, ¿para qué sirve un índice?

**Respuesta:**
Para acelerar búsquedas/ordenaciones/joins (en general) evitando escanear toda la colección; a cambio, ocupa espacio y hace más costosas algunas escrituras (hay que mantener el índice).

### 4) En Neo4j, ¿qué es una “restricción” (constraint)?

**Respuesta:**
Una regla declarativa sobre nodos/propiedades (por ejemplo, unicidad) que asegura integridad y suele crear/usar índices asociados.

---

## Parte 2 — Preguntas cortas (desarrollo)

### 5) Relacional vs NoSQL: ¿qué problemas de las relacionales motivan NoSQL? Relaciónalo con escalabilidad

**Respuesta:**
En sistemas a gran escala aparecen problemas como:

- **Escalado horizontal complejo** en relacionales “clásicas” (sharding, joins distribuidos, coordinación).
- **Modelo rígido** (esquema fuerte) frente a requisitos que cambian rápido.
- **Coste de joins** y normalización en lecturas masivas con latencia baja.
- **Impedance mismatch** con aplicaciones OO y estructuras jerárquicas.

NoSQL suele elegir modelos de datos más cercanos al acceso real (documentos, KV, grafos) y diseños que facilitan **particionado** y **replicación**, aceptando a veces menos consistencia global.

### 6) Redis como caché: explica el patrón cache-aside y problemas típicos

**Respuesta:**
**Cache-aside**:
1) La app busca en caché; si no está (miss), lee de la BD principal.
2) Guarda el resultado en caché con TTL.
3) Devuelve el valor.

Problemas típicos:
- **Cache stampede**: muchos misses simultáneos sobre la misma clave.
- **Inconsistencia temporal**: valores “viejos” hasta que expiran/invalidan.
- **Elección de TTL**: demasiado corto aumenta misses; demasiado largo aumenta staleness.

Mitigaciones: locks suaves, jitter en TTL, warming, invalidaciones.

### 7) Cassandra: explica escritura (write path) a alto nivel

**Respuesta:**
A alto nivel, cuando Cassandra escribe:

- El coordinador recibe la write y la envía a las réplicas según RF.
- Cada réplica escribe primero en el **commit log** (durabilidad) y en la **memtable** (memoria).
- Cuando la memtable se llena, se flushea a disco como **SSTables**.
- Compactions reorganizan/mergen SSTables con el tiempo.

Esto favorece escrituras rápidas (append/estructuras secuenciales) y evita random writes frecuentes.

---

## Parte 3 — Práctica

### 8) MongoDB: diseño y consulta

Colecciones:
- `users { _id, country, createdAt }`
- `events { _id, userId, type, ts }`

**Enunciado:**
1) ¿Cuándo prefieres mantener `events` separado de `users` (referencing) y no embebido?
2) Agregación: últimos 7 días, cuenta eventos por `type` para usuarios de `country = "ES"`.

**Respuesta:**

1) Separado cuando:
- hay **muchísimos eventos por usuario** (1–muchos grande),
- se consulta eventos de forma independiente,
- el documento de usuario crecería sin límite.

2) Pipeline (join con `$lookup`):
```js
db.events.aggregate([
  { $match: { ts: { $gte: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000) } } },
  {
    $lookup: {
      from: "users",
      localField: "userId",
      foreignField: "_id",
      as: "user"
    }
  },
  { $unwind: "$user" },
  { $match: { "user.country": "ES" } },
  { $group: { _id: "$type", count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $project: { _id: 0, type: "$_id", count: 1 } }
])
```

### 9) Redis: pub/sub

**Enunciado:**
Quieres un canal `alerts` donde servicios publiquen mensajes y otros se suscriban. Escribe comandos mínimos.

**Respuesta:**
- Suscriptor:
```redis
SUBSCRIBE alerts
```
- Publicador:
```redis
PUBLISH alerts "CPU high on node-3"
```

### 10) Redis: SCAN vs KEYS

**Enunciado:**
¿Por qué es preferible `SCAN` a `KEYS` en producción? Da un ejemplo.

**Respuesta:**
`KEYS pattern` puede **bloquear** Redis (O(N) y no incremental), afectando latencia. `SCAN` itera incrementalmente y permite paginar.

Ejemplo:
```redis
SCAN 0 MATCH "cart:*" COUNT 100
```

### 11) Neo4j: modelado y consulta

Modelo:
- `(:Person {id, name})`
- `(:Person)-[:FRIEND_OF]->(:Person)`

**Enunciado:**
Dado `id = 1`, devuelve amigos de amigos (2 saltos) excluyendo:
- la propia persona
- sus amigos directos

**Respuesta (Cypher):**
```cypher
MATCH (p:Person {id: 1})-[:FRIEND_OF]->(f:Person)
WITH p, collect(DISTINCT f) AS directFriends
UNWIND directFriends AS f
MATCH (f)-[:FRIEND_OF]->(fof:Person)
WHERE fof <> p AND NOT fof IN directFriends
RETURN DISTINCT fof.id AS id, fof.name AS name
ORDER BY name ASC
```

### 12) Chroma (conceptual + ejemplo)

**Enunciado:**
¿Qué guardas en una BBDD vectorial y qué consultas típicas haces en RAG? Da un mini-ejemplo de “añadir documentos” y “buscar similares”.

**Respuesta:**
Se guardan **embeddings** (vectores) + metadatos (id, texto original, fuente...). En RAG, se hace una búsqueda de vecinos cercanos (similaridad) para recuperar pasajes relevantes.

Mini-ejemplo (pseudo-Python):
```python
# add
collection.add(
  ids=["doc1"],
  documents=["Redis es una base de datos en memoria..."],
  metadatas=[{"topic": "redis"}]
)

# query
collection.query(
  query_texts=["¿Qué es pipelining en Redis?"],
  n_results=3,
  where={"topic": "redis"}
)
```

---

## Criterios típicos de corrección

- ¿Relacionas rendimiento/coste con escalado?
- ¿En agregaciones, orden de etapas eficiente (`$match` temprano)?
- ¿En Redis, eliges comandos que no bloqueen (`SCAN`)?
- ¿En Cypher, filtras correctamente para excluir nodos?
