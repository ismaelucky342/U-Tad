# Test Teoría — Variante G
**10 preguntas · 1 respuesta válida · No restan las erróneas**

---

**1.** En Scala, `AnyVal` y `AnyRef` son las dos subclases directas de `Any`. ¿Cuál es la diferencia clave entre ellas?

- a) `AnyVal` agrupa los tipos de valor (Int, Double, Boolean…) que no se representan como objetos en heap; `AnyRef` agrupa todos los tipos de referencia (String, clases…), equivalente a `Object` en Java
- b) `AnyVal` es inmutable; `AnyRef` puede ser mutable o inmutable según se declare con `val` o `var`
- c) `AnyVal` solo puede usarse como parámetro de funciones genéricas; `AnyRef` puede usarse en cualquier contexto
- d) Son equivalentes; la distinción es solo histórica de versiones antiguas de Scala

---

**2.** En Scala, si declaras `val lista = List(1, 2, 3)` y luego `val lista2 = lista :+ 4`, ¿qué ocurre realmente?

- a) `lista` se modifica in situ añadiendo el 4 al final, ya que `List` en Scala es mutable
- b) Se produce un error de compilación porque `val` no permite modificar la colección
- c) Se crea una nueva lista `List(1, 2, 3, 4)` asignada a `lista2`; `lista` permanece intacta con `List(1, 2, 3)`
- d) `lista2` apunta a la misma referencia que `lista` con el elemento 4 añadido en buffer

---

**3.** En Apache Spark, ¿qué determina el número de **stages** en el DAG de una aplicación?

- a) El número de acciones invocadas en el código
- b) El número de transformaciones aplicadas sobre cada RDD
- c) El número de operaciones de **shuffle** (como `groupByKey`, `reduceByKey`, `join`), ya que cada shuffle introduce un límite de stage
- d) El número de particiones del RDD inicial

---

**4.** En el temario se distingue entre **event time**, **ingestion time** y **processing time** en streaming. ¿Cuál es la diferencia entre **event time** e **ingestion time**?

- a) Son sinónimos; ambos representan el momento en que el evento se crea en la fuente
- b) Event time es cuándo ocurrió el evento en la fuente de datos; ingestion time es cuándo el sistema de streaming (p.ej. Kafka) lo recibe; processing time es cuándo el motor lo procesa
- c) Event time es cuándo el motor procesa el evento; ingestion time es cuándo se almacena en HDFS
- d) Event time solo es relevante en batch; en streaming siempre se usa processing time

---

**5.** ¿Cuál es la principal razón por la que `groupByKey` se considera menos eficiente que `reduceByKey` en Spark?

- a) `groupByKey` no admite tipos genéricos; `reduceByKey` sí
- b) `groupByKey` mueve todos los valores al reducer sin reducción previa en el mapper, lo que genera mucho más tráfico de red; `reduceByKey` combina valores localmente antes del shuffle
- c) `groupByKey` genera siempre más particiones que `reduceByKey`, consumiendo más memoria
- d) `groupByKey` es una acción; `reduceByKey` es una transformación, por lo que no son comparables directamente

---

**6.** En HDFS, los bloques tienen un tamaño por defecto de **128 MB**. ¿Cuál es la razón principal de usar bloques tan grandes respecto a un sistema de ficheros convencional?

- a) Para reducir la sobrecarga de metadatos en el NameNode: menos bloques implica menos entradas en memoria
- b) Para evitar la fragmentación interna de disco en los DataNodes
- c) Para que cada bloque quepa exactamente en la memoria RAM de un nodo Worker
- d) Porque HDFS no admite bloques de menos de 128 MB por limitaciones de diseño

---

**7.** En Kafka, los mensajes con la **misma clave** siempre se envían a la **misma partición**. ¿Qué garantía práctica aporta este comportamiento?

- a) Que los mensajes con la misma clave nunca se replican, ahorrando espacio
- b) Que los mensajes con la misma clave se procesan en orden, ya que dentro de una partición el orden está garantizado
- c) Que los consumidores con la misma clave se asignan al mismo consumer group automáticamente
- d) Que los mensajes con la misma clave se comprimen juntos, mejorando el throughput

---

**8.** En Spark, el comando `spark-submit` incluye el parámetro `--deploy-mode`. ¿Cuál es la diferencia entre `client` y `cluster`?

- a) En modo `client` el Driver se ejecuta en la máquina que lanza el comando; en modo `cluster` el Driver se ejecuta dentro de un nodo Worker del clúster
- b) En modo `client` se usan más Executors; en modo `cluster` se optimiza la memoria del Driver
- c) En modo `cluster` el Driver corre en local y los Executors en remoto; en `client` todo corre en remoto
- d) No hay diferencia funcional; el parámetro solo afecta a los logs generados

---

**9.** En el contexto de streaming, una **ventana deslizante** (sliding window) se diferencia de una **ventana tumbling** en que:

- a) La ventana tumbling puede solaparse con la anterior; la deslizante no
- b) La ventana deslizante avanza en pasos menores que su tamaño, por lo que los eventos pueden pertenecer a varias ventanas; la tumbling no se solapa y cada evento pertenece solo a una ventana
- c) La ventana tumbling procesa eventos en tiempo real; la deslizante procesa en micro-batch
- d) La ventana deslizante solo puede usarse con DStreams; la tumbling también con Structured Streaming

---

**10.** En Spark ML, al dividir los datos en **train set** y **test set**, ¿cuál es el riesgo de evaluar el modelo solo sobre el train set?

- a) El modelo no aprende suficientemente porque tiene menos datos disponibles
- b) El coste computacional de entrenamiento aumenta exponencialmente
- c) El modelo parece tener métricas excelentes pero puede estar sobreajustado (overfitting): ha memorizado el entrenamiento y no sabemos si generaliza bien a datos nuevos
- d) Spark ML no permite evaluar un modelo sobre el mismo conjunto con el que fue entrenado

---

## ✅ Respuestas Variante G

| # | Resp. | Por qué |
|---|-------|---------|
| 1 | **a** | AnyVal: tipos de valor primitivos (no en heap); AnyRef: tipos de referencia, equivalente a `Object` Java |
| 2 | **c** | Las colecciones Scala son inmutables por defecto; `:+` crea una nueva lista, la original no cambia |
| 3 | **c** | Cada shuffle (groupByKey, join…) crea un límite de stage; las etapas del DAG se definen por los shuffles |
| 4 | **b** | Event time: cuándo pasó en la fuente; ingestion time: cuándo entró en Kafka; processing time: cuándo lo procesa el motor |
| 5 | **b** | `groupByKey` envía todo al shuffle sin reducción previa; `reduceByKey` reduce localmente antes → mucho menos tráfico |
| 6 | **a** | Bloques grandes = menos bloques = menos metadatos en el NameNode (que guarda todo en RAM) |
| 7 | **b** | Misma clave → misma partición → orden garantizado intra-partición → procesamiento ordenado por entidad |
| 8 | **a** | `client`: Driver en la máquina local del usuario; `cluster`: Driver en un Worker del clúster |
| 9 | **b** | Sliding: avance < tamaño → solapamiento, eventos en varias ventanas; Tumbling: sin solapamiento |
| 10 | **c** | Evaluar solo en train oculta el overfitting; el test set mide la capacidad de generalización real |
