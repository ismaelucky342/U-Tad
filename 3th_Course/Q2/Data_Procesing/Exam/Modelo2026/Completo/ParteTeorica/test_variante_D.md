# Test Teoría — Variante D
**10 preguntas · 1 respuesta válida · No restan las erróneas**

---

**1.** En Scala, la función `map` aplicada a una colección:

- a) Filtra los elementos que cumplen una condición y devuelve una nueva colección
- b) Combina todos los elementos en un único valor acumulado
- c) Aplica una función a cada elemento y devuelve una nueva colección con los resultados transformados
- d) Ordena los elementos de menor a mayor

---

**2.** En Scala, ¿qué hace el operador `_` (guion bajo) cuando se usa como marcador de posición en una lambda?

- a) Indica que el parámetro es opcional y puede omitirse
- b) Es un comodín que representa el parámetro de la función anónima, permitiendo escribir `.map(_.toInt)` en lugar de `.map(x => x.toInt)`
- c) Descarta el resultado de la expresión anterior
- d) Se usa exclusivamente en pattern matching para indicar el caso por defecto

---

**3.** ¿Cuáles fueron las principales **limitaciones de Hadoop MapReduce** que motivaron el desarrollo de Spark?

- a) Hadoop no soporta Java ni Scala como lenguajes de programación
- b) Hadoop no puede manejar ficheros de más de 1 GB
- c) El uso intensivo de disco entre fases, la ineficiencia en algoritmos iterativos y el desaprovechamiento de la RAM
- d) Hadoop no tiene tolerancia a fallos en sus DataNodes

---

**4.** ¿Qué son los **Executors** en la arquitectura de Spark?

- a) Los nodos que almacenan bloques de datos en HDFS
- b) Los componentes del Driver que planifican las tareas del DAG
- c) Los gestores de recursos del clúster (YARN, Mesos, etc.)
- d) Los procesos lanzados en los nodos Worker que ejecutan las tareas y almacenan datos en caché

---

**5.** ¿Qué diferencia hay entre **OLAP** y **OLTP**?

- a) OLAP gestiona transacciones en tiempo real; OLTP realiza análisis históricos
- b) OLAP (analítico) está orientado a consultas sobre grandes volúmenes históricos; OLTP (transaccional) gestiona operaciones CRUD frecuentes en tiempo real
- c) OLAP es una base de datos NoSQL; OLTP es una base de datos relacional
- d) OLAP y OLTP son sinónimos; se usan indistintamente

---

**6.** En la arquitectura **Lambda**, ¿qué capas la componen?

- a) Capa de ingestión, capa de transformación y capa de visualización
- b) Capa de producción, capa de consumo y capa de almacenamiento
- c) Capa batch, capa speed (tiempo real) y capa serving (consultas)
- d) Capa de metadatos, capa de datos y capa de índices

---

**7.** En Spark Structured Streaming, ¿qué garantiza el mecanismo de **checkpointing**?

- a) Que los datos se comprimen antes de almacenarse en HDFS
- b) Que ante un fallo, el sistema puede recuperar el estado del procesamiento desde el último punto guardado, sin recomenzar desde el inicio
- c) Que cada mensaje de Kafka se consume exactamente en el orden de inserción global
- d) Que el DataFrame resultante se cachea automáticamente en memoria

---

**8.** ¿Qué función tiene **Apache ZooKeeper** en el ecosistema Kafka?

- a) Almacenar los mensajes del topic cuando los brokers están caídos
- b) Cifrar las comunicaciones entre productores y consumidores
- c) Comprimir los mensajes antes de enviarlos a los consumidores
- d) Coordinar el clúster: elección de broker líder, metadatos y configuración distribuida

---

**9.** En Spark ML, un **Pipeline** es:

- a) La conexión de red entre el Driver y los Executors
- b) El nombre del fichero de configuración del entorno de Spark
- c) El mecanismo de checkpointing para tolerancia a fallos en Streaming
- d) Una secuencia encadenada de Transformers y Estimators que se aplica de forma reproducible sobre un DataFrame

---

**10.** En el contexto de las bases de datos **NoSQL**, ¿cuál es su principal ventaja respecto a las relacionales en Big Data?

- a) Las bases de datos NoSQL son siempre más rápidas que las relacionales en cualquier escenario
- b) Las bases de datos NoSQL no permiten ningún tipo de consulta estructurada
- c) Las bases de datos NoSQL solo almacenan datos en formato JSON
- d) Las bases de datos NoSQL ofrecen mayor escalabilidad horizontal y flexibilidad de esquema, sacrificando parte de las garantías ACID, lo que las hace adecuadas para grandes volúmenes de datos variados

---

## ✅ Respuestas Variante D

| # | Resp. | Por qué |
|---|-------|---------|
| 1 | **c** | `map`: aplica función a cada elemento y devuelve nueva colección transformada |
| 2 | **b** | `_` es placeholder: `_.toInt` equivale a `x => x.toInt`, forma concisa de lambda |
| 3 | **c** | I/O disco intensivo + ineficiencia iterativa + memoria desaprovechada |
| 4 | **d** | Executors: procesos en Workers que ejecutan tareas y cachean datos |
| 5 | **b** | OLAP: analítico/histórico (data warehouse); OLTP: transaccional/operacional (tiempo real) |
| 6 | **c** | Lambda = batch layer + speed layer + serving layer |
| 7 | **b** | Checkpointing guarda el estado periódicamente para poder recuperarse ante fallos |
| 8 | **d** | ZooKeeper: coordinación del clúster Kafka (metadatos, elección de líder) |
| 9 | **d** | Pipeline ML = cadena Transformer/Estimator reproducible sobre DataFrame |
| 10 | **d** | NoSQL: escalabilidad horizontal y esquema flexible a cambio de relajar ACID |
