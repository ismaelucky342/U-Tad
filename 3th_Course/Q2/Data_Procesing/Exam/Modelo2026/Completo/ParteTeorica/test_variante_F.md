# Test Teoría — Variante F
**10 preguntas · 1 respuesta válida · No restan las erróneas**

---

**1.** En Scala, los **companion objects** comparten el mismo nombre que una clase. ¿Qué capacidad exclusiva tienen respecto a esa clase?

- a) Pueden instanciar la clase sin usar `new`, gracias al método `apply` generado automáticamente
- b) Pueden acceder a los miembros `private` de la clase, algo que ningún otro objeto puede hacer
- c) Son la única forma de definir herencia múltiple en Scala
- d) Permiten que la clase sea serializable en Spark sin configuración adicional

---

**2.** En Scala, ¿qué diferencia hay entre `flatMap` y `map` sobre una colección?

- a) `flatMap` filtra los elementos nulos; `map` los transforma todos incluyendo nulos
- b) `map` aplica una función a cada elemento y devuelve una colección del mismo tamaño; `flatMap` aplica una función que devuelve una colección por elemento y aplana el resultado en una sola colección
- c) `flatMap` solo funciona con colecciones de tipo `Option`; `map` funciona con cualquier colección
- d) Son equivalentes salvo que `flatMap` trabaja en paralelo y `map` en secuencial

---

**3.** El **Shuffle** en Spark es una de las operaciones más costosas. ¿Por qué?

- a) Porque obliga a recomputar el DAG desde el inicio cuando se produce
- b) Porque requiere que todos los RDDs sean cacheados antes de ejecutarse
- c) Porque implica redistribuir datos entre particiones de distintos nodos a través de la red y disco, lo que genera I/O intensivo y rompe el pipeline de ejecución en stages
- d) Porque serializa todos los datos a JSON antes de enviarlos por la red

---

**4.** En Kafka, si un topic tiene 4 particiones y un consumer group tiene 6 consumidores, ¿qué sucede con los 2 consumidores extra?

- a) Se asignan como réplicas de respaldo de los otros 4 consumidores activos
- b) Kafka distribuye las particiones de forma que cada consumidor recibe una fracción
- c) Quedan inactivos (idle) porque no puede haber más consumidores activos que particiones en un mismo grupo
- d) Generan un error que detiene el consumo del topic completo

---

**5.** En Spark Structured Streaming, ¿qué problema resuelve el concepto de **watermark**?

- a) Limita el número máximo de mensajes que el sistema puede procesar por segundo
- b) Define un umbral de tiempo que permite al sistema descartar eventos tardíos que llegan demasiado tarde para ser incluidos en una ventana ya procesada, acotando el estado que el sistema debe mantener en memoria
- c) Establece el tiempo mínimo de retención de mensajes en Kafka antes de ser descartados
- d) Es el mecanismo de checkpointing que guarda el estado del stream periódicamente

---

**6.** Respecto al **Teorema CAP**, MongoDB en su configuración por defecto sacrifica la consistencia en favor de disponibilidad y tolerancia a particiones (AP). ¿Qué implica esto en la práctica?

- a) MongoDB no puede recuperarse de la pérdida de nodos; requiere intervención manual
- b) Ante una partición de red, MongoDB puede devolver datos desactualizados en lugar de devolver un error, para no perder disponibilidad
- c) MongoDB garantiza que todas las lecturas siempre devolverán el dato más reciente escrito
- d) MongoDB no admite réplicas; toda la consistencia recae en un único nodo primario

---

**7.** En la arquitectura de Spark, cuando el **Driver** falla en modo `--deploy-mode cluster`, ¿qué ocurre con los Executors?

- a) Los Executors continúan ejecutando las tareas asignadas y envían resultados al nuevo Driver
- b) YARN o el Cluster Manager reasignan automáticamente las tareas a otros Executors disponibles
- c) Los Executors pierden la conexión con el Driver, se detienen y los recursos son liberados al Cluster Manager
- d) Los Executors persisten en memoria hasta que el Driver se reinicia y se reconectan automáticamente

---

**8.** ¿Cuál de estas afirmaciones sobre los **DStreams** (modelo antiguo de Spark Streaming) es correcta?

- a) DStream es una abstracción que representa un flujo de datos como una secuencia de RDDs, cada uno generado en un micro-batch de tiempo
- b) DStream procesa los datos en tiempo real puro (milisegundos), sin necesidad de micro-batches
- c) DStream está basado en DataFrames, por lo que puede aprovechar el optimizador Catalyst
- d) DStream es la API recomendada actualmente para nuevos proyectos de streaming en Spark

---

**9.** En la gestión de dependencias de Scala, ¿cuál es la diferencia principal entre **SBT** y **Maven**?

- a) Maven usa Scala para configurar proyectos; SBT usa XML como Maven en Java
- b) SBT solo puede usarse con proyectos Scala; Maven solo con proyectos Java
- c) SBT define la configuración mediante código Scala y soporta compilación incremental; Maven usa XML (`pom.xml`) y recompila siempre desde cero
- d) No hay diferencia relevante; ambos gestionan dependencias de la misma forma para proyectos Scala

---

**10.** En Machine Learning, el **trade-off sesgo-varianza** describe un equilibrio fundamental. ¿Cuál de estas afirmaciones lo describe correctamente?

- a) Alto sesgo implica overfitting; alta varianza implica underfitting
- b) Un modelo con alto sesgo no aprende los patrones suficientes (underfitting); un modelo con alta varianza es demasiado sensible al ruido del entrenamiento (overfitting)
- c) Sesgo y varianza son métricas de evaluación del rendimiento de un modelo en producción
- d) Reducir el sesgo siempre reduce también la varianza; son métricas inversamente correlacionadas

---

## ✅ Respuestas Variante F

| # | Resp. | Por qué |
|---|-------|---------|
| 1 | **b** | El companion object puede acceder a los `private` de su clase; ningún otro objeto externo puede |
| 2 | **b** | `map`: misma cardinalidad; `flatMap`: transforma + aplana (p.ej. `List(List(1,2), List(3))` → `List(1,2,3)`) |
| 3 | **c** | Shuffle = redistribución de datos entre nodos, I/O de red y disco, crea nuevos stages en el DAG |
| 4 | **c** | Kafka: máximo un consumidor activo por partición en un grupo; los extras quedan idle |
| 5 | **b** | Watermark: umbral para descartar eventos tardíos y acotar el estado en memoria |
| 6 | **b** | AP en CAP: ante partición de red, prefiere responder con dato posiblemente viejo antes que dar error |
| 7 | **c** | Si el Driver muere, los Executors pierden su coordinador y el Cluster Manager libera los recursos |
| 8 | **a** | DStream = flujo como secuencia de RDDs por micro-batch; es la API legacy basada en RDDs |
| 9 | **c** | SBT: config en Scala + incremental; Maven: `pom.xml` XML + recompilación completa |
| 10 | **b** | Alto sesgo = underfitting (modelo simple); alta varianza = overfitting (modelo que memoriza el ruido) |
