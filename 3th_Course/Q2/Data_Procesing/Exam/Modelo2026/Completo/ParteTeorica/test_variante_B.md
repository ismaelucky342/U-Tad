# Test Teoría — Variante B
**10 preguntas · 1 respuesta válida · No restan las erróneas**

---

**1.** ¿Cuál es la característica que distingue a Scala de Java en cuanto a **inmutabilidad**?

- a) Java promueve la inmutabilidad por defecto; Scala usa estructuras mutables
- b) Scala promueve la inmutabilidad por defecto; `val` y las colecciones inmutables son el estándar
- c) Ambos lenguajes tratan la inmutabilidad de la misma forma
- d) La inmutabilidad en Scala solo aplica a tipos primitivos

---

**2.** En Scala, ¿para qué sirve el tipo `Option[T]`?

- a) Para declarar parámetros opcionales con valor por defecto en funciones
- b) Para indicar que una función puede lanzar una excepción comprobada
- c) Para representar un valor que puede ser `Some(valor)` o `None`, evitando NullPointerExceptions
- d) Para definir colecciones que pueden estar vacías o llenas

---

**3.** En HDFS, ¿por qué se replica cada bloque de datos (factor 3 por defecto)?

- a) Para acelerar las escrituras distribuyendo la carga entre nodos
- b) Para garantizar tolerancia a fallos: si un DataNode falla, los datos siguen disponibles en otras réplicas
- c) Para que el NameNode tenga siempre una copia local de cada bloque
- d) Es un requisito de licencia de Apache Hadoop

---

**4.** ¿Qué es un **Pair RDD** en Spark?

- a) Un RDD formado por exactamente dos particiones
- b) Un RDD cuyos elementos son pares `(clave, valor)`, que permite operaciones como `groupByKey`, `reduceByKey` o `join`
- c) El resultado de unir dos RDDs con una operación `zip`
- d) Un RDD que se ejecuta en dos nodos de forma sincronizada

---

**5.** ¿Qué diferencia principal hay entre **procesamiento batch** y **procesamiento streaming**?

- a) El batch es más rápido; el streaming es más preciso
- b) El batch requiere Kafka; el streaming requiere Hadoop
- c) El batch procesa conjuntos finitos de datos en momentos programados; el streaming procesa datos de forma continua a medida que llegan
- d) No hay diferencia relevante en la actualidad con las herramientas modernas

---

**6.** En la arquitectura de Spark, ¿cuál es la diferencia entre el **Driver** y el **Master** (Cluster Manager)?

- a) Son el mismo componente con nombres distintos según el gestor de recursos
- b) El Driver contiene la lógica de la aplicación y coordina los Executors; el Master gestiona los recursos del clúster
- c) El Driver almacena los datos; el Master ejecuta las tareas
- d) El Master solo existe en modo local; en clúster se usa únicamente el Driver

---

**7.** ¿Qué es el **DAG** (Directed Acyclic Graph) en Spark?

- a) Un tipo de RDD especializado para datos de grafos de red social
- b) Un formato de almacenamiento columnar eficiente en HDFS
- c) La representación del plan de ejecución de transformaciones que Spark optimiza antes de ejecutar
- d) El protocolo de comunicación entre los nodos del clúster

---

**8.** En Kafka, ¿qué es un **topic**?

- a) El componente que decide qué consumidor recibe cada mensaje
- b) El nodo principal que gestiona los metadatos del clúster Kafka
- c) El índice de desplazamiento que indica el último mensaje leído por un consumidor
- d) Una categoría o canal lógico al que los productores envían mensajes y del que los consumidores los leen

---

**9.** ¿Qué semántica de entrega garantiza que cada mensaje se procesa **exactamente una vez**, sin pérdidas ni duplicados?

- a) At-most-once
- b) At-least-once
- c) Exactly-once
- d) Best-effort

---

**10.** Según la metodología **CRISP-DM**, ¿cuál es el orden correcto de sus fases principales?

- a) Modelado → Datos → Negocio → Evaluación → Despliegue → Preparación
- b) Comprensión del negocio → Comprensión de los datos → Preparación → Modelado → Evaluación → Despliegue
- c) Preparación → Modelado → Evaluación → Comprensión del negocio → Despliegue
- d) Datos → Modelado → Negocio → Despliegue → Evaluación

---

## ✅ Respuestas Variante B

| # | Resp. | Por qué |
|---|-------|---------|
| 1 | **b** | Scala usa `val` e inmutabilidad por defecto; Java usa mutabilidad por defecto |
| 2 | **c** | `Option` = `Some(v)` o `None`; alternativa funcional a null |
| 3 | **b** | La replicación es el mecanismo de tolerancia a fallos de HDFS |
| 4 | **b** | Pair RDD: elementos (K,V) que habilitan groupByKey, reduceByKey, join… |
| 5 | **c** | Batch: datos finitos + programado; Streaming: flujo continuo en tiempo real |
| 6 | **b** | Driver = lógica de la app; Master/Cluster Manager = gestión de recursos |
| 7 | **c** | DAG = plan de ejecución dirigido y acíclico que Spark optimiza antes de lanzar |
| 8 | **d** | Topic = canal lógico; productores publican, consumidores suscriben |
| 9 | **c** | Exactly-once es la semántica más estricta (sin pérdidas ni duplicados) |
| 10 | **b** | CRISP-DM: Negocio → Datos → Preparación → Modelado → Evaluación → Despliegue |
