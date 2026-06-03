# Test Teoría — Variante E
**10 preguntas · 1 respuesta válida · No restan las erróneas**

---

**1.** En Scala, una función que no devuelve ningún valor útil devuelve el tipo `Unit`. ¿Cuál es la diferencia clave entre `Unit` de Scala y `void` de Java?

- a) Son equivalentes; `Unit` es simplemente el alias de Scala para `void`
- b) `Unit` tiene una única instancia concreta representada por `()`, mientras que `void` en Java no tiene instancia alguna
- c) `Unit` solo puede usarse como tipo de retorno en funciones anónimas; `void` es de propósito general
- d) `void` en Java sí tiene instancia (`Void.TYPE`), mientras que `Unit` en Scala no tiene ninguna

---

**2.** En la jerarquía de tipos de Scala, `Nothing` ocupa una posición especial. ¿Cuál es su característica más importante?

- a) Es la superclase de todos los tipos, equivalente a `Any`
- b) Es el tipo de todas las colecciones vacías y no puede asignarse a ninguna variable
- c) Es el subtipo de todos los tipos (incluyendo `Null`), lo que permite usarlo como tipo de retorno en funciones que nunca terminan o siempre lanzan excepción
- d) Es el tipo que devuelve Scala cuando una función retorna implícitamente sin valor

---

**3.** En el modelo de planificación de Spark, el **Fair Scheduler** se distingue del modelo FIFO por defecto. ¿Cuál es la descripción más precisa del Fair Scheduler?

- a) Ejecuta primero las tareas más cortas para maximizar el throughput del clúster
- b) Distribuye los recursos entre consultas usando un modelo Round Robin, permitiendo que consultas ligeras avancen aunque haya consultas pesadas en ejecución
- c) Asigna prioridad fija a cada tarea según su orden de llegada, igual que FIFO pero con más granularidad
- d) Es el planificador por defecto de Spark; FIFO solo se usa en modo local

---

**4.** Kafka garantiza el orden de los mensajes, pero con una limitación importante. ¿Cuál?

- a) El orden solo se garantiza si el topic tiene exactamente una partición
- b) El orden se garantiza globalmente entre todos los topics del clúster
- c) El orden se garantiza dentro de una misma partición, pero no entre distintas particiones de un mismo topic
- d) El orden se garantiza solo si el productor usa `acks=all`

---

**5.** ¿Cuál es la diferencia entre una transformación **stateless** y una **stateful** en procesamiento de streaming?

- a) Las stateless usan RDDs; las stateful usan DataFrames
- b) Las stateless procesan cada evento de forma independiente sin memoria de eventos anteriores; las stateful mantienen estado acumulado entre eventos (contadores, ventanas, sesiones)
- c) Las stateless solo pueden aplicarse en micro-batch; las stateful en tiempo real
- d) Las stateful son más eficientes porque evitan la recomputación; las stateless siempre recalculan desde cero

---

**6.** En la arquitectura **Kappa**, ¿cuál es la diferencia fundamental respecto a Lambda que la hace más simple de mantener?

- a) Kappa elimina el uso de Kafka y procesa todo con Spark directamente
- b) Kappa usa una sola tecnología de streaming para todo (tiempo real e histórico), almacenando el histórico como log inmutable en lugar de mantener una batch layer separada
- c) Kappa elimina la serving layer y sirve los datos directamente desde el stream
- d) Kappa procesa solo datos en tiempo real; para análisis histórico sigue necesitando una batch layer opcional

---

**7.** En HDFS, ¿qué ocurre cuando el **NameNode** falla en una configuración sin alta disponibilidad?

- a) Los DataNodes eligen automáticamente un nuevo NameNode entre ellos mediante votación
- b) HDFS sigue siendo legible pero no se pueden escribir nuevos datos hasta que el NameNode se recupere
- c) El sistema de ficheros completo queda inaccesible porque el NameNode es el único que conoce los metadatos y dónde están los bloques
- d) YARN asume temporalmente las funciones del NameNode hasta que este se restaure

---

**8.** Un registro en Kafka se identifica de forma única mediante un triplete. ¿Cuáles son los tres elementos de ese triplete?

- a) Broker, topic y timestamp
- b) Topic, partición y offset
- c) Clave, valor y timestamp
- d) Producer ID, topic y sequence number

---

**9.** En Spark, `cache()` y `persist()` permiten reutilizar un RDD sin recomputarlo. ¿Cuál es la diferencia entre ambos?

- a) `cache()` persiste en disco; `persist()` persiste en memoria
- b) `cache()` es equivalente a `persist(StorageLevel.MEMORY_ONLY)`; `persist()` permite especificar el nivel de almacenamiento (memoria, disco, serializado, etc.)
- c) `cache()` aplica solo a DataFrames; `persist()` aplica solo a RDDs
- d) No hay diferencia funcional; son sinónimos totales en todas las versiones de Spark

---

**10.** En Spark ML, ¿qué distinción existe entre un **Transformer** y un **Estimator**?

- a) Un Transformer entrena modelos; un Estimator aplica transformaciones sobre los datos
- b) Un Transformer aplica una función sobre un DataFrame y devuelve otro DataFrame; un Estimator aprende de los datos mediante `fit()` y produce un Transformer
- c) Un Estimator es una clase abstracta que no puede usarse directamente; un Transformer sí
- d) Son sinónimos; la distinción es solo terminológica según la versión de la API

---

## ✅ Respuestas Variante E

| # | Resp. | Por qué |
|---|-------|---------|
| 1 | **b** | `Unit` tiene instancia concreta `()`; `void` en Java es un tipo abstracto sin instancia |
| 2 | **c** | `Nothing` es subtipo de todo: válido en listas vacías (`List[Nothing]`) y funciones que siempre lanzan excepción |
| 3 | **b** | Fair Scheduler = Round Robin entre consultas, evita que una pesada bloquee a las ligeras |
| 4 | **c** | Kafka garantiza orden intra-partición; entre particiones distintas el orden global no está garantizado |
| 5 | **b** | Stateless: evento a evento, sin memoria; Stateful: mantiene estado (ventanas, contadores, sesiones) |
| 6 | **b** | Kappa: un solo stack de streaming + log inmutable como histórico, sin batch layer separada |
| 7 | **c** | El NameNode es SPoF en config básica: sin él los metadatos son inaccesibles y el FS queda inutilizable |
| 8 | **b** | Triplete único en Kafka: topic + partición + offset |
| 9 | **b** | `cache()` = `persist(MEMORY_ONLY)`; `persist()` permite elegir el nivel de almacenamiento |
| 10 | **b** | Transformer: transforma DataFrame → DataFrame; Estimator: aprende con `fit()` → produce un Transformer |
