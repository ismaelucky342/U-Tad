# Examen modelo A — ABDS (resuelto)

> Objetivo: practicar un examen mixto con **teoría (breve + desarrollo corto)** y **práctica** (consultas/op. en MongoDB, Redis y Neo4j).
>
> Nota: el examen real puede variar. Este modelo está diseñado para cubrir el estilo descrito por el profesor.

---

## Instrucciones (simuladas)

- Tiempo recomendado: 90–120 min.
- Responde de forma clara y concisa.
- En las preguntas prácticas, se valora: corrección, uso adecuado de operadores y claridad.

---

## Parte 1 — Cuestiones breves (tipo test / muy cortas)

### 1) Define ACID en una línea cada propiedad

**Respuesta:**
- **Atomicidad:** una transacción ocurre completa o no ocurre.
- **Consistencia:** una transacción válida lleva la BD de un estado consistente a otro consistente.
- **Aislamiento:** transacciones concurrentes no se “pisan”; el resultado equivale a algún orden secuencial.
- **Durabilidad:** una vez confirmados, los cambios persisten incluso ante fallos.

### 2) ¿Qué problema intenta resolver el “impedance mismatch”?

**Respuesta:**
Es la fricción entre el modelo **orientado a objetos** (objetos con jerarquías, referencias, etc.) y el modelo **relacional** (tablas, filas, joins). Obliga a mapear/converter estructuras (ORM) y puede añadir complejidad y coste.

### 3) Escalado vertical vs horizontal (elige la idea clave)

**Respuesta:**
- **Vertical (scale up):** mejorar una máquina (CPU/RAM/IO). Más simple, pero tiene techo y suele encarecerse mucho.
- **Horizontal (scale out):** añadir más máquinas y repartir carga/datos. Mejor crecimiento y tolerancia a fallos, pero más complejidad (particionado, replicación, consistencia).

### 4) En Redis, ¿qué diferencia hay entre `MULTI/EXEC` y pipelining?

**Respuesta:**
- **Pipelining:** optimización de red; envías muchos comandos sin esperar respuesta uno a uno. No garantiza atomicidad.
- **`MULTI/EXEC`:** agrupa comandos en una **transacción** (se ejecutan secuencialmente sin intercalarse con otros comandos). No es aislamiento “serializable” completo, pero sí evita interleaving.

---

## Parte 2 — Preguntas cortas (desarrollo)

### 5) Explica por qué surgen las BBDD NoSQL y qué “trade-offs” suelen aceptar

**Respuesta:**
Surgen por necesidades de **escala**, **flexibilidad de esquema** y **alto rendimiento** en sistemas distribuidos (web, big data, baja latencia). Muchas NoSQL priorizan:

- **Escalabilidad horizontal** (particionado/sharding) y operación distribuida.
- **Disponibilidad** y tolerancia a fallos.
- **Modelo de datos más cercano al consumo** (documento, clave-valor, grafo, columna).

Trade-offs típicos:
- Relajar garantías ACID en favor de **consistencia eventual** (según diseño).
- Limitar joins complejos y transacciones multi-entidad.
- Cambiar potencia de consulta por rendimiento (según tipo: KV vs documento vs grafo).

### 6) MongoDB: embedding vs referencing. Da criterios y un ejemplo típico

**Respuesta:**
- **Embedding (incrustar):** meter subdocumentos dentro del documento principal.
  - Pros: lecturas rápidas (una sola consulta), consistencia local, menos joins.
  - Contras: crecimiento de documento, duplicación, actualizaciones más costosas.
  - Útil cuando la relación es 1–pocos y se accede junto (p. ej., pedido con líneas).

- **Referencing (referenciar):** guardar IDs y consultar colecciones separadas.
  - Pros: normaliza, evita duplicación, útil para 1–muchos grandes o muchos–muchos.
  - Contras: más consultas o `$lookup`, más coste en lecturas.
  - Útil para relación grande (p. ej., usuario y eventos/actividad masiva).

### 7) Redis eviction policies: ¿qué son y cuándo importan?

**Respuesta:**
Son estrategias para decidir **qué claves eliminar** cuando Redis alcanza el límite de memoria (`maxmemory`). Importan sobre todo cuando Redis funciona como **caché** o almacén en memoria con límite.

Ejemplos habituales:
- `noeviction`: no borra, devuelve error al escribir.
- `allkeys-lru`: borra claves según LRU entre todas.
- `volatile-ttl`: borra solo claves con TTL, priorizando las que expiran antes.

La elección depende de si todas las claves son cacheables, si hay TTL, y del patrón de acceso.

### 8) Cassandra: token ring, particiones y consistencia

**Respuesta:**
- Un **partition key** se hashea a un **token** y se asigna a un rango del **token ring**.
- Los nodos (idealmente con **vnodes**) se reparten rangos de tokens → balanceo.
- **Replicación**: un factor RF determina cuántas réplicas se guardan (posiblemente en racks/DC distintos).
- **Consistencia (nivel de consistencia):** define cuántas réplicas deben confirmar lectura/escritura (p. ej., `ONE`, `QUORUM`, `ALL`).
  - Mayor consistencia ⇒ más latencia y menor disponibilidad.
  - Menor consistencia ⇒ más disponibilidad y menor latencia, pero lecturas potencialmente “stale”.

---

## Parte 3 — Práctica

### 9) MongoDB (find)

Colección `orders` (ejemplo):

- Campos: `_id`, `customerId`, `status`, `total`, `createdAt` (Date), `items` (array con `{ sku, qty, price }`).

**Enunciado:** devuelve los pedidos de `status = "PAID"` de los últimos 30 días, mostrando solo `_id`, `customerId`, `total` y `createdAt`, ordenados por `total` desc y limitando a 20.

**Respuesta (consulta):**
```js
db.orders.find(
  {
    status: "PAID",
    createdAt: { $gte: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000) }
  },
  {
    _id: 1,
    customerId: 1,
    total: 1,
    createdAt: 1
  }
).sort({ total: -1 }).limit(20)
```

### 10) MongoDB (agregación)

**Enunciado:** calcula, para cada `customerId`, el número de pedidos y el gasto total (`sum(total)`) solo de pedidos `PAID`. Devuelve top 5 por gasto.

**Respuesta (pipeline):**
```js
db.orders.aggregate([
  { $match: { status: "PAID" } },
  {
    $group: {
      _id: "$customerId",
      ordersCount: { $sum: 1 },
      totalSpent: { $sum: "$total" }
    }
  },
  { $sort: { totalSpent: -1 } },
  { $limit: 5 },
  {
    $project: {
      _id: 0,
      customerId: "$_id",
      ordersCount: 1,
      totalSpent: 1
    }
  }
])
```

### 11) Redis (modelado + operaciones)

**Enunciado:** quieres almacenar el carrito de compra por usuario. Cada ítem tiene `sku` y `qty`. Propón una estructura y comandos para:
1) añadir/modificar qty
2) leer el carrito completo
3) borrar un sku

**Respuesta (una solución válida):** usar **Hash** por usuario.

- Key: `cart:{userId}`
- Fields: `sku -> qty`

Comandos:
```redis
HSET cart:42 SKU123 2
HINCRBY cart:42 SKU123 1
HGETALL cart:42
HDEL cart:42 SKU123
```

### 12) Redis (sorted set)

**Enunciado:** ranking de jugadores con score. Inserta/actualiza score y consulta top 3.

**Respuesta:**
```redis
ZADD leaderboard 1500 "alice"
ZADD leaderboard 1750 "bob"
ZINCRBY leaderboard 50 "alice"
ZREVRANGE leaderboard 0 2 WITHSCORES
```

### 13) Neo4j / Cypher

Modelo:
- `(:User {id, name})`
- `(:Movie {id, title})`
- `(:User)-[:RATED {stars}]->(:Movie)`

**Enunciado:**
1) devuelve las películas que ha valorado el usuario `id = 42` con sus estrellas
2) recomendaciones simples: películas valoradas por “usuarios similares” (que han valorado alguna película en común con el usuario 42), excluyendo las ya valoradas por 42, y ordena por número de usuarios similares que la han valorado.

**Respuesta:**

1) Valoraciones del usuario:
```cypher
MATCH (u:User {id: 42})-[r:RATED]->(m:Movie)
RETURN m.title AS title, r.stars AS stars
ORDER BY r.stars DESC, title ASC
```

2) Recomendación simple por co-rating:
```cypher
MATCH (u:User {id: 42})-[:RATED]->(m:Movie)<-[:RATED]-(other:User)
WITH u, collect(DISTINCT other) AS similars
UNWIND similars AS s
MATCH (s)-[:RATED]->(rec:Movie)
WHERE NOT (u)-[:RATED]->(rec)
RETURN rec.title AS recommendedTitle, count(DISTINCT s) AS similarRaters
ORDER BY similarRaters DESC, recommendedTitle ASC
LIMIT 10
```

---

## Mini-checklist de corrección (para ti)

- ¿Definiste bien ACID y escalado vertical/horizontal?
- ¿Mongo: `$match` antes de `$group` y proyecciones correctas?
- ¿Redis: elegiste tipo de dato adecuado (hash, zset, etc.)?
- ¿Neo4j: excluiste lo ya visto con `WHERE NOT (u)-[:RATED]->(rec)`?
