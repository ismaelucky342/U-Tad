# Examen modelo D — ABDS (resuelto, nivel “rebuscado”)

> Este modelo mete preguntas menos obvias: consistencia/aislamiento “de verdad”, pipeline con `$lookup` + `$facet`, Redis Streams/Lua, Cypher con paths y constraints, y consistencia/tombstones en Cassandra.

---

## Parte 1 — Cuestiones breves (pero con mala leche)

### 1) ¿Qué diferencia hay entre **aislamiento** y **serializabilidad**?

**Respuesta:**
- **Aislamiento** es una propiedad general: transacciones concurrentes no deberían interferir en resultados visibles.
- **Serializabilidad** es un nivel fuerte de aislamiento: el resultado es equivalente a ejecutar transacciones en algún orden secuencial (como si fueran una detrás de otra).

### 2) Explica “write skew” con un ejemplo (2–3 líneas)

**Respuesta:**
Ocurre cuando dos transacciones leen el mismo conjunto de filas y escriben en filas distintas, de modo que cada una ve un estado válido, pero juntas violan una restricción global.
Ejemplo típico: “tiene que haber al menos un médico de guardia”; dos transacciones ven 2 médicos y cada una quita a uno distinto → quedan 0.

### 3) En Redis, ¿qué ganas y qué pierdes con `SET key value NX EX 10` como lock?

**Respuesta:**
- Ganas: lock sencillo y rápido, con expiración (evitas locks eternos).
- Pierdes: si el proceso tarda más que el TTL puede expirar y otro proceso adquirir el lock (riesgo de sección crítica simultánea). Soluciones: renovar TTL, token único + verificación al liberar, o patrón tipo Redlock (según contexto).

### 4) Neo4j: diferencia entre índice y constraint de unicidad

**Respuesta:**
- Un **índice** acelera encontrar nodos por propiedad.
- Un **constraint de unicidad** impone que no haya duplicados para una propiedad (y normalmente crea un índice para soportarlo).

---

## Parte 2 — Preguntas cortas (desarrollo)

### 5) MongoDB: `readConcern` vs `writeConcern` (visión práctica)

**Respuesta:**
- **`writeConcern`**: qué garantías pides al escribir (p. ej. esperar confirmación de N réplicas, o a que esté en journal). Más seguridad ⇒ más latencia.
- **`readConcern`**: qué “calidad” de lectura pides (p. ej. leer solo datos confirmados/estables). Más garantías ⇒ más latencia y posible menos disponibilidad.

En práctica: subes `writeConcern` cuando no puedes permitir perder escrituras; ajustas `readConcern` cuando te preocupa leer datos no confirmados o con rollbacks.

### 6) Redis Streams vs Pub/Sub: ¿cuándo usar cada uno?

**Respuesta:**
- **Pub/Sub**: mensajes volátiles; si el consumidor no está suscrito en ese momento, se pierden. Útil para notificaciones en “tiempo real” donde no importa la entrega garantizada.
- **Streams**: log persistente (hasta política de trimming), con consumidores y grupos; puedes reintentar, hacer ack, y procesar desde un offset. Útil para colas/event sourcing ligero.

### 7) Cassandra: tombstones — qué son y por qué afectan a lecturas

**Respuesta:**
Cuando borras o expiras (TTL) datos, Cassandra crea **tombstones** que marcan “borrado” hasta que la compaction los purga. Si acumulas muchos tombstones, las lecturas tienen que procesarlos/mezclarlos al leer SSTables ⇒ empeoran latencia y pueden causar timeouts.

---

## Parte 3 — Práctica

### 8) MongoDB (pipeline con `$lookup` + `$facet`)

Colecciones:
- `customers { _id, name, tier }`
- `orders { _id, customerId, status, total, createdAt }`

**Enunciado:**
Para `status="PAID"` en los últimos 90 días, devuelve:
- Un listado paginado (page 1, size 10) con: `customerName`, `tier`, `ordersCount`, `totalSpent`
- Y a la vez un resumen global con:
  - `totalCustomers` (nº de customers con algún pedido)
  - `grandTotal` (suma total)

**Respuesta:** (una solución posible)
```js
db.orders.aggregate([
  { $match: { status: "PAID", createdAt: { $gte: new Date(Date.now() - 90*24*60*60*1000) } } },
  {
    $group: {
      _id: "$customerId",
      ordersCount: { $sum: 1 },
      totalSpent: { $sum: "$total" }
    }
  },
  {
    $lookup: {
      from: "customers",
      localField: "_id",
      foreignField: "_id",
      as: "customer"
    }
  },
  { $unwind: "$customer" },
  {
    $facet: {
      page: [
        { $sort: { totalSpent: -1 } },
        { $skip: 0 },
        { $limit: 10 },
        {
          $project: {
            _id: 0,
            customerId: "$_id",
            customerName: "$customer.name",
            tier: "$customer.tier",
            ordersCount: 1,
            totalSpent: 1
          }
        }
      ],
      summary: [
        {
          $group: {
            _id: null,
            totalCustomers: { $sum: 1 },
            grandTotal: { $sum: "$totalSpent" }
          }
        },
        { $project: { _id: 0, totalCustomers: 1, grandTotal: 1 } }
      ]
    }
  }
])
```

### 9) Redis (Streams + consumer group)

**Enunciado:**
Tienes un stream `events`. Crea un consumer group `workers`, añade 2 eventos y lee como consumidor `c1`.

**Respuesta:**
```redis
XGROUP CREATE events workers $ MKSTREAM
XADD events * type "signup" userId "42"
XADD events * type "purchase" userId "42" amount "19.9"
XREADGROUP GROUP workers c1 COUNT 10 STREAMS events >
```

### 10) Redis (Lua: check-and-set atómico)

**Enunciado:**
Saldo en `balance:{userId}` (string). Implementa “si saldo >= amount entonces decrementa y devuelve 1; si no, devuelve 0”.

**Respuesta (script Lua):**
```lua
-- KEYS[1] = balance key
-- ARGV[1] = amount
local bal = tonumber(redis.call('GET', KEYS[1]) or '0')
local amt = tonumber(ARGV[1])
if bal >= amt then
  redis.call('DECRBY', KEYS[1], amt)
  return 1
end
return 0
```

(Se ejecutaría con `EVAL ... 1 balance:42 50`.)

### 11) Neo4j (shortest path)

Modelo:
- `(:Person {id})-[:FRIEND_OF]->(:Person {id})`

**Enunciado:**
Devuelve la longitud del camino más corto entre `id=1` e `id=9`.

**Respuesta:**
```cypher
MATCH (a:Person {id: 1}), (b:Person {id: 9})
MATCH p = shortestPath((a)-[:FRIEND_OF*..10]->(b))
RETURN length(p) AS hops
```

### 12) Neo4j (constraint)

**Enunciado:**
Crea una restricción para que `User.id` sea único.

**Respuesta:**
```cypher
CREATE CONSTRAINT user_id_unique IF NOT EXISTS
FOR (u:User)
REQUIRE u.id IS UNIQUE
```

### 13) Cassandra (consistencia y QUORUM)

**Enunciado:**
Si RF=3, explica qué significa escribir con `QUORUM` y leer con `ONE`. ¿Qué riesgo hay?

**Respuesta:**
- Escribir con `QUORUM` ⇒ la escritura se confirma cuando **2 de 3** réplicas confirman.
- Leer con `ONE` ⇒ lees de **1 réplica** cualquiera.
Riesgo: podrías leer de una réplica desactualizada (stale) si esa réplica no recibió/confirmó la última escritura; con el tiempo se arreglará por mecanismos internos, pero la lectura inmediata puede ser vieja.
