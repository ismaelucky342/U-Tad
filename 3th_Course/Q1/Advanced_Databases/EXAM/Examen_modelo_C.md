# Examen modelo C — ABDS (resuelto)

> Modelo orientado a “preguntas abiertas cortas” y práctica compacta. Incluye también una pregunta de **Cassandra (read path + consistencia)**.

---

## Parte 1 — Cuestiones breves

### 1) ¿Qué significa que una BD sea “orientada a documentos”?

**Respuesta:**
Que la unidad principal de almacenamiento/consulta es un **documento** (normalmente JSON/BSON) con estructura jerárquica, y las entidades se representan como documentos (posiblemente con arrays/subdocumentos) en vez de filas en tablas.

### 2) ¿Qué es una relación en Neo4j y qué puede almacenar?

**Respuesta:**
Una relación es una arista dirigida entre dos nodos. Puede tener **tipo** (p. ej. `RATED`) y **propiedades** (p. ej. `stars`, `since`).

### 3) En Redis, di un caso claro para Hash y otro para List

**Respuesta:**
- **Hash:** objeto con campos (p. ej. `user:42` con `name`, `email`, `age`).
- **List:** cola/historial ordenado (p. ej. últimos eventos o jobs FIFO).

### 4) ¿Qué es un embedding (en el contexto de Chroma)?

**Respuesta:**
Un vector numérico que representa semánticamente un texto/imagen/etc. en un espacio donde la **distancia/similitud** aproxima “parecido” semántico.

---

## Parte 2 — Preguntas cortas (desarrollo)

### 5) Explica ACID (breve) y da un ejemplo de por qué “aislamiento” importa

**Respuesta:**
- **Atomicidad:** todo o nada.
- **Consistencia:** se respetan constraints/reglas.
- **Aislamiento:** concurrencia sin interferencias visibles.
- **Durabilidad:** persistencia tras commit.

Ejemplo de aislamiento:
- Dos compras simultáneas de la última unidad de stock. Sin aislamiento, ambas podrían leer “stock=1” y ambas decrementar → stock negativo o venta doble. Con aislamiento (o control de concurrencia), una transacción debe ver un estado coherente y evitar la doble venta.

### 6) Redis: explica transacciones vs scripts

**Respuesta:**
- Con `MULTI/EXEC` agrupas comandos; evita interleaving, pero no proporciona lógica condicional compleja.
- Con **Lua scripting** (`EVAL`) puedes ejecutar lógica en el servidor de forma atómica (p. ej. “si saldo >= x entonces decrementa y registra”). Suele ser la opción para operaciones “check-and-set” complejas.

### 7) Neo4j: índices y restricciones — ¿para qué sirven y cómo afectan a rendimiento?

**Respuesta:**
- **Índices** aceleran búsquedas por propiedades (p. ej. encontrar `User{id:42}` rápido).
- **Restricciones** garantizan integridad (p. ej. unicidad) y normalmente crean o se apoyan en índices.

Impacto:
- Lecturas/búsquedas iniciales (match por propiedad) mejoran.
- Escribir/actualizar propiedades indexadas cuesta algo más por mantenimiento del índice.

### 8) Cassandra: consistencia y quórum

**Respuesta:**
Cassandra permite elegir nivel de consistencia por operación.
- Si RF=3:
  - `ONE`: 1 réplica responde → baja latencia, menos garantía.
  - `QUORUM`: mayoría (2 de 3) → compromiso entre coherencia y disponibilidad.
  - `ALL`: 3 de 3 → más coherente, pero más latencia y más fallos si una réplica cae.

Heurística: `QUORUM` suele dar buen equilibrio en muchos casos.

---

## Parte 3 — Práctica

### 9) MongoDB: actualización y consulta

Colección `products`:
- Campos: `_id`, `name`, `price`, `tags` (array de strings), `stock`.

**Enunciado:**
1) Sube un 10% el precio de los productos con tag `"gaming"`.
2) Lista productos con `stock < 5`, ordenados por `stock` asc, mostrando `name`, `stock` y `price`.

**Respuesta:**

1) Update:
```js
db.products.updateMany(
  { tags: "gaming" },
  [ { $set: { price: { $multiply: ["$price", 1.10] } } } ]
)
```

2) Find:
```js
db.products.find(
  { stock: { $lt: 5 } },
  { _id: 0, name: 1, stock: 1, price: 1 }
).sort({ stock: 1 })
```

### 10) Redis: rate limiting simple

**Enunciado:**
Quieres limitar a 100 peticiones/minuto por usuario (`userId`). Propón una solución simple en Redis basada en contador + TTL.

**Respuesta (solución simple válida):**
- Clave: `rl:{userId}:{window}` donde `window = epochMinute`.
- Incrementas y pones TTL.

Pseudo-flujo:
```redis
INCR rl:42:29347231
EXPIRE rl:42:29347231 60
```
Si el valor supera 100, bloqueas.

Comentarios:
- Es simple y funciona, aunque no es sliding window fino.
- En producción se puede mejorar con zset o token bucket.

### 11) Neo4j: patrón y agregación

Modelo:
- `(:User {id})`
- `(:User)-[:BOUGHT]->(:Product {id, category})`

**Enunciado:**
Para cada categoría, cuenta cuántas compras hizo el usuario `id=7`.

**Respuesta:**
```cypher
MATCH (u:User {id: 7})-[:BOUGHT]->(p:Product)
RETURN p.category AS category, count(*) AS purchases
ORDER BY purchases DESC, category ASC
```

### 12) Cassandra: read path (alto nivel) y estructuras

**Enunciado:**
Describe a alto nivel el read path y qué estructuras intervienen.

**Respuesta:**
Una lectura típica implica:

- El coordinador consulta a las réplicas según el nivel de consistencia.
- Cada réplica puede mirar en:
  - **Memtable** (datos recientes en memoria).
  - **SSTables** en disco, usando estructuras auxiliares (p. ej. filtros/índices internos) para reducir lecturas.
- Si hay múltiples SSTables con versiones, se combinan resultados (y se resuelven tombstones).
- Puede haber **read repair** si detecta divergencias y el nivel/estrategia lo permite.

---

## Auto-repaso rápido

- ¿Tus respuestas conectan conceptos con rendimiento/coste?
- ¿Mongo updates: distingues update clásico vs update pipeline?
- ¿Redis: usas TTL cuando procede?
- ¿Cypher: MATCH/RETURN correctos y agregaciones bien?
