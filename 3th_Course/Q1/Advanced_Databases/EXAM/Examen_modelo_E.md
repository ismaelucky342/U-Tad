# Examen modelo E — ABDS (resuelto, nivel “rebuscado”)

> Este modelo va a “casos borde” y diseño: sharding/replicación, agregaciones con ventanas “manuales”, Redis TTL/eviction/bitmaps, Neo4j recomendación con pesos, y Chroma con MMR (conceptual).

---

## Parte 1 — Cuestiones breves

### 1) ¿Cuándo un escalado vertical puede salir peor económicamente que horizontal?

**Respuesta:**
Cuando para ganar un poco más de rendimiento necesitas saltar a máquinas muy “premium” (coste no lineal). Horizontal suele permitir crecimiento incremental con hardware commodity, aunque a cambio de complejidad operativa.

### 2) ¿Qué es sharding (particionado) y qué dos problemas aparecen rápido?

**Respuesta:**
Sharding es repartir datos entre nodos según una clave.
Problemas típicos: **hotspots** (shard “caliente” por mala shard key) y **consultas cross-shard** (scatter-gather) que empeoran latencia/coste.

### 3) Redis: diferencia entre TTL y eviction

**Respuesta:**
- **TTL**: caducidad por clave, definida por la aplicación (expira cuando toca).
- **Eviction**: borrado forzado por falta de memoria según política (`maxmemory-policy`). Puede borrar claves antes de su TTL.

### 4) Neo4j: ¿por qué los grafos suelen superar a relacionales en traversals profundos?

**Respuesta:**
Porque el traversal sigue punteros/relaciones explícitas y evita joins repetidos costosos; el modelo está optimizado para navegar relaciones.

---

## Parte 2 — Preguntas cortas (desarrollo)

### 5) MongoDB: elige una shard key “buena” y una “mala” para `orders`

Colección `orders { _id, userId, createdAt, total, status }`.

**Respuesta:**
- Posible shard key **buena**: `(userId, createdAt)` (o `userId` si el patrón de acceso es por usuario) porque distribuye por muchos usuarios y permite consultas por usuario eficientes.
- Posible shard key **mala**: `status` (pocos valores, crea hotspots), o `createdAt` si casi todo cae en el shard “del último rango” (hot shard) cuando hay muchas escrituras recientes.

El criterio base: alta cardinalidad, buena distribución, y alineada con consultas más comunes.

### 6) Redis: diseña un contador de usuarios únicos diarios y justifica el tipo de dato

**Respuesta:**
Una opción “rebuscada” y eficiente en memoria (si hay IDs numéricos acotados) es **bitmap**:
- key: `dau:YYYY-MM-DD`
- bit offset: `userId`

Operaciones:
- marcar visita: `SETBIT dau:2026-01-08 42 1`
- contar únicos: `BITCOUNT dau:2026-01-08`

Justificación: muy rápido y compacto para pertenencia y conteo aproximado exacto (exacto para universo acotado).

### 7) Chroma: ¿qué es MMR y por qué puede mejorar la recuperación?

**Respuesta:**
MMR (Maximal Marginal Relevance) equilibra **relevancia** y **diversidad** al seleccionar resultados: evita devolver top-N muy redundantes (casi idénticos) y mejora cobertura para RAG.

---

## Parte 3 — Práctica

### 8) MongoDB (agregación para “top usuarios por gasto” + filtro complejo)

Colección `orders { _id, userId, status, total, createdAt, items: [{sku, qty}] }`.

**Enunciado:**
Calcula top 10 usuarios por gasto total en pedidos `PAID` del último mes, pero solo contando pedidos donde exista algún item con `qty >= 3`.

**Respuesta:**
```js
db.orders.aggregate([
  {
    $match: {
      status: "PAID",
      createdAt: { $gte: new Date(Date.now() - 30*24*60*60*1000) },
      items: { $elemMatch: { qty: { $gte: 3 } } }
    }
  },
  {
    $group: {
      _id: "$userId",
      totalSpent: { $sum: "$total" },
      ordersCount: { $sum: 1 }
    }
  },
  { $sort: { totalSpent: -1 } },
  { $limit: 10 },
  { $project: { _id: 0, userId: "$_id", totalSpent: 1, ordersCount: 1 } }
])
```

### 9) MongoDB (índice propuesto)

**Enunciado:**
Propón un índice para acelerar la agregación anterior y explica por qué.

**Respuesta:**
Índice compuesto empezando por filtros más selectivos y/o usados en match:
- `{ status: 1, createdAt: -1, userId: 1 }`

Justificación:
- `status` y `createdAt` filtran rápidamente el conjunto (último mes + pagados).
- `userId` ayuda a agrupar/ordenar accesos. (El filtro en `items.qty` es más difícil de indexar bien en compuesto sin conocer patrones; se podría considerar índice multikey sobre `items.qty` si es crítico, pero tiene trade-offs.)

### 10) Redis (TTL + eviction edge case)

**Enunciado:**
Tienes claves de sesión `sess:{id}` con TTL 30 min. Pero Redis está casi sin memoria con política `allkeys-lru`. ¿Qué podría pasar y cómo lo mitigas?

**Respuesta:**
Podrían expulsarse sesiones **antes** de su TTL por LRU ⇒ usuarios “deslogueados” antes de tiempo.
Mitigaciones:
- Separar sesiones en un Redis con memoria/política adecuada.
- Ajustar `maxmemory`.
- Usar `volatile-lru` si todas las claves tienen TTL y quieres limitar eviction a esas.
- Monitorizar hit rate y memory pressure.

### 11) Redis (bitmap de DAU)

**Enunciado:**
Comandos para registrar visita de `userId=123` y obtener DAU del día.

**Respuesta:**
```redis
SETBIT dau:2026-01-08 123 1
BITCOUNT dau:2026-01-08
EXPIRE dau:2026-01-08 604800
```

### 12) Neo4j (recomendación con pesos)

Modelo:
- `(:User {id})-[:RATED {stars}]->(:Movie {id,title})`

**Enunciado:**
Recomienda películas al usuario 42 basándote en usuarios que hayan valorado con `stars >= 4` alguna película en común con 42.
Puntúa cada recomendación con la suma de `stars` que le han dado esos usuarios similares. Excluye ya vistas por 42.

**Respuesta (una solución posible):**
```cypher
MATCH (u:User {id: 42})-[r1:RATED]->(m:Movie)
WHERE r1.stars >= 4
MATCH (other:User)-[r2:RATED]->(m)
WHERE r2.stars >= 4 AND other <> u
WITH u, collect(DISTINCT other) AS similars
UNWIND similars AS s
MATCH (s)-[r:RATED]->(rec:Movie)
WHERE r.stars >= 4 AND NOT (u)-[:RATED]->(rec)
RETURN rec.title AS title, sum(r.stars) AS score, count(DISTINCT s) AS voters
ORDER BY score DESC, voters DESC, title ASC
LIMIT 10
```

### 13) Cassandra (consistencia de lectura)

**Enunciado:**
En un cluster con RF=3, ¿por qué `LOCAL_QUORUM` es relevante con múltiples data centers?

**Respuesta:**
Porque `LOCAL_QUORUM` exige quórum **solo en el data center local**, reduciendo latencia inter-DC y evitando depender del estado de otro DC. Da buen equilibrio entre consistencia y rendimiento en despliegues multi-DC.
