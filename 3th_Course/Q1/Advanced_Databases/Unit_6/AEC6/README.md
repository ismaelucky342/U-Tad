# AEC6 - Read Path Flow en Cassandra

## Descripción del Proyecto

Para esta actividad he desarrollado una explicación detallada de 3 escenarios de lectura de datos en Cassandra, enfocándome en el Read Path Flow. Cada escenario ilustra un flujo de lectura diferente, cubriendo las estructuras clave como Memtable, Row Cache, Bloom Filter, Partition Key Cache, Partition Summary, Partition Index, Compression Offset Map y SSTables. Se incluyen diagramas textuales, ejemplos concretos con valores de registros y explicaciones sobre el contenido de cada estructura, justificando por qué ciertos datos están presentes o ausentes basados en operaciones previas.

**Escenarios cubiertos:**
- Escenario 1: Row Cache y Partition Key Cache habilitadas, con datos en ambas caches.
- Escenario 2: Solo Row Cache habilitada, Partition Key no en cache.
- Escenario 3: Ninguna cache habilitada, datos únicamente en SSTables.

## Justificación de Cassandra y el Read Path Flow

Cassandra es una base de datos distribuida NoSQL diseñada para alta escalabilidad y rendimiento en lecturas/escrituras masivas. El Read Path Flow optimiza las lecturas combinando datos de Memtable y SSTables, utilizando caches y filtros para minimizar accesos a disco. Entender estos flujos es crucial para tuning de rendimiento, ya que revela cómo Cassandra prioriza datos recientes (Memtable), frecuentemente accedidos (Row Cache) o claves específicas (Partition Key Cache), reduciendo latencia en entornos de big data.

En mi experiencia con bases de datos distribuidas, Cassandra destaca por su arquitectura de almacenamiento LSM (Log-Structured Merge), donde el Read Path evita lecturas aleatorias costosas mediante estructuras como Bloom Filters y Compression Offset Maps. Esta práctica me ha permitido profundizar en cómo estas optimizaciones hacen que Cassandra maneje millones de registros eficientemente.

## Estructura del Proyecto

```
AEC6/
├── README.md                          # Este archivo - Explicación completa de escenarios
├── escenarios/
│   ├── escenario1_diagrama.txt        # Diagrama textual del Escenario 1
│   ├── escenario2_diagrama.txt        # Diagrama textual del Escenario 2
│   └── escenario3_diagrama.txt        # Diagrama textual del Escenario 3
└── ejemplos/
    └── datos_ejemplo.json             # Datos de ejemplo para ilustrar estructuras
```

## Inicio Rápido

Esta actividad es teórica y no requiere ejecución de código. Revisa las secciones de escenarios para entender los flujos de lectura.

## ¿Qué he usado?

La explicación se basa en conceptos de Cassandra estudiados en la unidad:

- **Memtable**: Almacena datos recientes en memoria (últimas escrituras).
- **Row Cache**: Cache de filas completas para datos frecuentemente accedidos.
- **Bloom Filter**: Filtro probabilístico para verificar presencia de partitions en SSTables.
- **Partition Key Cache**: Cache de claves de partición para acceso rápido.
- **Partition Summary**: Resumen de partitions para navegación eficiente.
- **Partition Index**: Índice de offsets dentro de partitions.
- **Compression Offset Map**: Mapa de offsets comprimidos para localización en disco.
- **SSTables**: Archivos inmutables en disco con datos históricos.

### Funcionalidades concretas
- **Escenarios variados**: Cubren combinaciones de caches habilitadas/deshabilitadas.
- **Ejemplos concretos**: Valores de claves, registros y estructuras.
- **Explicaciones detalladas**: Por qué datos están en ciertas estructuras (e.g., Row Cache para accesos recientes).

## Escenarios de Lectura en Cassandra

### Escenario 1: Row Cache y Partition Key Cache Habilitadas, Datos en Ambas Caches

**Contexto**: La tabla `users` tiene una fila con partition key `pk1` y clustering key `ck1`, accedida recientemente (última escritura hace 1 hora, leída 5 veces en las últimas 24 horas). Row Cache almacena filas completas de datos frecuentemente accedidos. Partition Key Cache almacena claves de partición para evitar búsquedas en índices.

**Flujo de Lectura**:
1. **Comprueba la Memtable**: Busca `pk1`. No encuentra (datos antiguos, ya flushed a SSTable).
2. **Comprueba la Row Cache**: Encuentra la fila completa: `{pk1: {ck1: {name: 'John', age: 30}}}`. Devuelve datos. (Row Cache tiene esta fila porque fue accedida frecuentemente, priorizando lecturas rápidas).
3. **Bloom Filter, Partition Key Cache, etc.**: No se accede, ya que Row Cache sirvió la consulta.

**Diagrama**:
```
Cliente -> Cassandra Node
  |-> Memtable: No data for pk1
  |-> Row Cache: Hit - {pk1: {ck1: {name: 'John', age: 30}}}
  |-> Resultado: Datos devueltos
```

**Explicación**: Row Cache evita accesos a disco porque almacena filas completas de datos hot (accedidos recientemente). Partition Key Cache no se usa aquí porque Row Cache es más eficiente para filas completas.

### Escenario 2: Solo Row Cache Habilitada, Partition Key No en Cache

**Contexto**: Similar a Escenario 1, pero Partition Key Cache deshabilitada. La fila fue escrita recientemente (en Memtable) pero no accedida lo suficiente para Row Cache. Partition Key `pk2` no está en cache porque no fue buscada recientemente.

**Flujo de Lectura** (diferencias desde Escenario 1):
- Comparte pasos 1-2 con Escenario 1, pero Row Cache miss.
3. **Comprueba el Bloom Filter**: Verifica si `pk2` existe en SSTables. Bloom Filter indica posible presencia (probabilístico, bajo false positive).
4. **Partition Key Cache**: Deshabilitada, así que no se consulta.
5. **Partition Summary**: Busca `pk2`. Encuentra resumen: `{pk2: offset_start=1000, offset_end=1500}` (resumen de partitions para navegación rápida).
6. **Partition Index**: Accede al índice: `{pk2: {ck2: disk_offset=1200}}` (índice de clustering keys dentro de partition).
7. **Compression Offset Map**: Localiza datos: `offset=1200 -> uncompressed_pos=5000` (mapa para descompresión).
8. **SSTable en Disco**: Lee datos: `{pk2: {ck2: {email: 'john@example.com'}}}`.

**Diagrama**:
```
Cliente -> Cassandra Node
  |-> Memtable: No data for pk2
  |-> Row Cache: Miss
  |-> Bloom Filter: Possible hit
  |-> Partition Summary: {pk2: offset_start=1000}
  |-> Partition Index: {pk2: {ck2: disk_offset=1200}}
  |-> Compression Offset Map: offset=1200 -> pos=5000
  |-> SSTable: {pk2: {ck2: {email: 'john@example.com'}}}
  |-> Resultado: Datos devueltos
```

**Explicación**: Sin Partition Key Cache, se recurre a Partition Summary e Index, que son estructuras en disco pero optimizadas. Row Cache miss porque la fila no fue accedida lo suficiente para cachearla.

### Escenario 3: Ninguna Cache Habilitada, Datos en SSTables

**Contexto**: Caches deshabilitadas para minimizar memoria. Datos antiguos, solo en SSTables. Partition Key `pk3` existe en SSTable tras compaction.

**Flujo de Lectura**:
1. **Comprueba la Memtable**: No encuentra `pk3` (datos flushed).
2. **Row Cache**: Deshabilitada, skip.
3. **Bloom Filter**: Confirma presencia de `pk3` en SSTables.
4. **Partition Key Cache**: Deshabilitada, skip.
5. **Partition Summary**: Busca `pk3`: `{pk3: offset_start=2000, offset_end=2500}`.
6. **Partition Index**: `{pk3: {ck3: disk_offset=2200}}`.
7. **Compression Offset Map**: `offset=2200 -> uncompressed_pos=8000`.
8. **SSTable en Disco**: Lee `{pk3: {ck3: {city: 'Madrid'}}}`.

**Diagrama**:
```
Cliente -> Cassandra Node
  |-> Memtable: No data for pk3
  |-> Row Cache: Disabled
  |-> Bloom Filter: Hit
  |-> Partition Summary: {pk3: offset_start=2000}
  |-> Partition Index: {pk3: {ck3: disk_offset=2200}}
  |-> Compression Offset Map: offset=2200 -> pos=8000
  |-> SSTable: {pk3: {ck3: {city: 'Madrid'}}}
  |-> Resultado: Datos devueltos
```

**Explicación**: Sin caches, el flujo recurre completamente a estructuras en disco. Bloom Filter evita lecturas innecesarias; Partition Summary/Index permiten navegación eficiente en SSTables comprimidas.

## Pruebas y validación

Los escenarios están validados contra la documentación oficial de Cassandra. Ejemplos usan datos ficticios pero realistas (e.g., partition keys como `pk1`, valores como `name: 'John'`). Diagramas textuales ilustran flujos; explicaciones detallan contenido de estructuras basadas en operaciones previas (e.g., escrituras recientes en Memtable, accesos frecuentes en Row Cache).

---

### Escenario 1 Diagrama Detallado

```
[Cliente Query: SELECT * FROM users WHERE pk = 'pk1' AND ck = 'ck1']

1. Memtable Check:
   - Contenido: {pk_recent: {ck_recent: {data: 'new'}}}
   - Resultado: Miss (pk1 no presente, datos antiguos flushed)

2. Row Cache Check (Habilitada):
   - Contenido: {pk1: {ck1: {name: 'John', age: 30}}} (fila completa, accedida 5 veces)
   - Resultado: Hit - Devuelve datos

Fin del flujo.
```

### Escenario 2 Diagrama Detallado

```
[Cliente Query: SELECT * FROM users WHERE pk = 'pk2' AND ck = 'ck2']

1-2. Memtable & Row Cache: Miss (similar a Esc1, pero fila no cached)

3. Bloom Filter:
   - Contenido: Bitmap probabilístico indicando presencia de pk2
   - Resultado: Possible hit

4. Partition Key Cache: Disabled

5. Partition Summary:
   - Contenido: {pk2: offset_start=1000, offset_end=1500}
   - Resultado: Encuentra resumen

6. Partition Index:
   - Contenido: {pk2: {ck2: disk_offset=1200}}
   - Resultado: Offset localizado

7. Compression Offset Map:
   - Contenido: {1200: uncompressed_pos=5000}
   - Resultado: Posición descomprimida

8. SSTable Read:
   - Contenido: {pk2: {ck2: {email: 'john@example.com'}}}
   - Resultado: Datos leídos del disco
```

### Escenario 3 Diagrama Detallado

```
[Cliente Query: SELECT * FROM users WHERE pk = 'pk3' AND ck = 'ck3']

1-4. Memtable, Row Cache, Bloom Filter: Miss/Hit como arriba, caches disabled

5. Partition Summary:
   - Contenido: {pk3: offset_start=2000, offset_end=2500}
   - Resultado: Resumen encontrado

6-8. Partition Index, Compression Offset Map, SSTable: Similar a Esc2, lee {pk3: {ck3: {city: 'Madrid'}}}
```
