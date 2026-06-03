# Test Teoría — Variante A
**10 preguntas · 1 respuesta válida · No restan las erróneas**

---

**1.** ¿Sobre qué entorno de ejecución corre Scala?

- a) Python Virtual Machine (PVM)
- b) Node.js Runtime
- c) Java Virtual Machine (JVM)
- d) .NET Common Language Runtime (CLR)

---

**2.** En Scala, ¿qué diferencia hay entre `val` y `var`?

- a) `val` es para tipos numéricos y `var` para cadenas de texto
- b) `val` declara una referencia inmutable; `var` declara una referencia mutable
- c) `val` solo puede usarse dentro de una función
- d) No hay diferencia funcional, es solo una convención de estilo

---

**3.** ¿Cuál es la función del **NameNode** en HDFS?

- a) Almacenar los bloques de datos replicados en disco
- b) Ejecutar las tareas MapReduce sobre los datos
- c) Gestionar los metadatos: qué bloques forman cada fichero y en qué DataNodes están
- d) Coordinar la comunicación entre los Workers de Spark

---

**4.** ¿Qué significa que una transformación en Spark sea **lazy**?

- a) Que se ejecuta en segundo plano sin bloquear el hilo principal
- b) Que no se ejecuta en el momento en que se define, sino cuando se invoca una acción
- c) Que solo puede aplicarse a RDDs pequeños que caben en memoria
- d) Que el resultado se descarta automáticamente si no se cachea

---

**5.** El **Teorema CAP** establece que un sistema distribuido solo puede garantizar a la vez dos de estas tres propiedades. ¿Cuáles son?

- a) Concurrencia, Atomicidad y Persistencia
- b) Consistencia, Disponibilidad y Tolerancia a Particiones
- c) Coherencia, Accesibilidad y Paralelismo
- d) Consistencia, Aislamiento y Durabilidad

---

**6.** ¿Qué es un **RDD** en Apache Spark?

- a) Un fichero de configuración del clúster distribuido
- b) El gestor de recursos del clúster de Spark
- c) Una colección distribuida, inmutable y tolerante a fallos que se procesa en paralelo
- d) Un tipo de nodo Worker especializado en almacenamiento

---

**7.** ¿Cuál es la principal ventaja de Spark frente a Hadoop MapReduce en cargas **iterativas**?

- a) Usa más nodos simultáneamente, lo que acelera el procesamiento
- b) Procesa los datos en memoria, evitando escrituras en disco entre fases
- c) Está escrito en Scala, que compila más rápido que Java
- d) Elimina completamente la fase de Shuffle

---

**8.** En Spark SQL, ¿cómo se ejecuta una consulta SQL estándar sobre un DataFrame?

- a) Convirtiendo el DataFrame a RDD y usando el método `sql()` sobre él
- b) Importando el módulo `HiveContext` y ejecutando la consulta directamente
- c) Registrando el DataFrame como vista temporal y usando `spark.sql("SELECT ...")`
- d) No es posible mezclar SQL con DataFrames; son APIs incompatibles

---

**9.** En Apache Kafka, ¿qué es el **offset**?

- a) El número de réplicas de un topic en el clúster
- b) El tiempo máximo que un mensaje permanece en el topic antes de borrarse
- c) El identificador único del broker líder de una partición
- d) La posición secuencial de un mensaje dentro de una partición, que permite al consumidor saber hasta dónde ha leído

---

**10.** En Spark ML, ¿qué diferencia existe entre **MLlib** y **Spark ML**?

- a) MLlib usa DataFrames y es la API moderna; Spark ML usa RDDs y está en desuso
- b) MLlib está basada en RDDs y se considera la opción más antigua; Spark ML está basada en DataFrames y es la recomendada actualmente
- c) Spark ML solo admite clasificación; MLlib admite todos los algoritmos
- d) Son el mismo módulo con distinto nombre según la versión de Spark

---

## ✅ Respuestas Variante A

| # | Resp. | Por qué |
|---|-------|---------|
| 1 | **c** | Scala compila a bytecode que se ejecuta sobre la JVM, igual que Java |
| 2 | **b** | `val` = inmutable (como `final` en Java); `var` = mutable |
| 3 | **c** | El NameNode guarda metadatos; los DataNodes guardan los bloques físicos |
| 4 | **b** | Las transformaciones son lazy: se acumulan en el DAG y se ejecutan al invocar una acción |
| 5 | **b** | CAP: Consistency, Availability, Partition tolerance |
| 6 | **c** | RDD = Resilient Distributed Dataset: distribuido, inmutable, tolerante a fallos |
| 7 | **b** | Spark procesa en memoria; MapReduce escribe resultados intermedios en disco |
| 8 | **c** | `createOrReplaceTempView` → `spark.sql("SELECT ...")` |
| 9 | **d** | El offset es el puntero de posición del consumidor dentro de la partición |
| 10 | **b** | MLlib (RDD, deprecated) vs Spark ML (DataFrame, API activa recomendada) |
