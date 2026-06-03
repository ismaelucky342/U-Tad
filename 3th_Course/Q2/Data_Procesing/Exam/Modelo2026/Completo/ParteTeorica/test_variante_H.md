# Test Teoría — Variante H
**10 preguntas · 1 respuesta válida · No restan las erróneas**

---

**1.** En Scala, el **pattern matching** con `match/case` es más potente que un `switch` de Java. ¿Cuál de estas capacidades tiene el pattern matching de Scala que **no** tiene el `switch` de Java?

- a) Puede comparar valores de tipo `Int` y `String`, cosa que Java no permite en `switch`
- b) Permite hacer deconstrucción de case classes, comparar por tipo, usar guardas (`if`) y capturar valores, todo dentro de un mismo `match`
- c) Puede ejecutarse en paralelo sobre colecciones distribuidas como RDDs
- d) El `match` en Scala es una expresión que devuelve un valor; en Java el `switch` nunca puede devolver un valor

---

**2.** En Scala, ¿qué significa que una función sea de **"transparencia referencial"**?

- a) Que la función puede ser llamada desde cualquier parte del código sin imports adicionales
- b) Que la función no tiene efectos secundarios y siempre devuelve el mismo resultado para los mismos argumentos, lo que permite sustituir la llamada por su resultado sin cambiar el comportamiento del programa
- c) Que la función es visible desde clases externas; equivalente a `public` en Java
- d) Que la función está optimizada por el compilador para evitar la creación de objetos temporales

---

**3.** En Hadoop MapReduce, ¿en qué se diferencia el rol del **JobTracker** del **TaskTracker** (arquitectura MRv1)?

- a) El JobTracker ejecuta las tareas Map; el TaskTracker ejecuta las tareas Reduce
- b) El JobTracker gestiona y planifica los trabajos a nivel de clúster; el TaskTracker ejecuta las tareas individuales en cada nodo Worker y reporta su progreso
- c) Son el mismo componente con nombres distintos según la versión de Hadoop
- d) El JobTracker almacena los datos en HDFS; el TaskTracker los lee para ejecutar las tareas

---

**4.** En Kafka, la **retention policy** de un topic define:

- a) El número máximo de consumidores que pueden leer el topic simultáneamente
- b) Durante cuánto tiempo (o hasta qué tamaño) se conservan los mensajes en el topic, independientemente de si han sido consumidos o no
- c) El factor de replicación mínimo que deben tener las particiones del topic
- d) La prioridad de entrega de mensajes cuando hay varios topics compitiendo por recursos del broker

---

**5.** En Spark, ¿qué problema concreto resuelve el uso de **broadcast variables**?

- a) Permiten compartir el estado de un RDD entre distintas aplicaciones Spark del mismo clúster
- b) Evitan enviar una copia de una variable grande a cada tarea individual; en su lugar, se envía una única copia a cada Executor, que la mantiene en memoria para todas sus tareas
- c) Permiten modificar variables desde los Executors y propagarlas de vuelta al Driver
- d) Son la forma de implementar variables globales mutables en un entorno distribuido

---

**6.** La **consistencia eventual** en sistemas distribuidos implica:

- a) Que el sistema garantiza que todas las operaciones de escritura son visibles de forma inmediata en todos los nodos
- b) Que los distintos nodos pueden tener temporalmente versiones diferentes de los mismos datos, pero convergerán al mismo estado si no llegan nuevas escrituras
- c) Que el sistema es consistente solo en situaciones donde no hay particiones de red
- d) Que las lecturas siempre devuelven el dato más reciente, aunque con un retraso máximo configurable

---

**7.** Spark History Server se diferencia de la Spark Web UI (puerto 4040) en que:

- a) La Web UI muestra tareas en ejecución en tiempo real; el History Server permite consultar el historial de aplicaciones ya finalizadas cuyos logs se han persistido en HDFS
- b) La Web UI requiere autenticación; el History Server es de acceso público
- c) El History Server solo funciona con YARN; la Web UI funciona con cualquier gestor de recursos
- d) Son equivalentes; el History Server es simplemente la versión actualizada de la Web UI

---

**8.** En el contexto del **Teorema CAP**, un sistema que elige **CP** (Consistencia + Tolerancia a Particiones) sacrifica disponibilidad. ¿Qué significa esto en la práctica ante una partición de red?

- a) El sistema devuelve datos desactualizados para mantener la operatividad
- b) El sistema deja de aceptar escrituras pero sigue respondiendo lecturas con datos potencialmente viejos
- c) El sistema puede rechazar o bloquear peticiones para garantizar que no se devuelvan datos inconsistentes hasta que la partición se resuelva
- d) El sistema replica los datos a un nodo externo y redirige todas las peticiones allí

---

**9.** ¿Cuál es la diferencia entre las **ventanas de sesión** (session windows) y las **ventanas temporales fijas** (tumbling/sliding) en streaming?

- a) Las ventanas de sesión tienen tamaño fijo; las temporales tienen tamaño dinámico
- b) Las ventanas de sesión se crean y cierran dinámicamente en función de períodos de inactividad del usuario o entidad; las temporales se definen con un tamaño fijo de tiempo
- c) Las ventanas de sesión solo funcionan con DStreams; las temporales solo con Structured Streaming
- d) Las ventanas temporales pueden solaparse; las de sesión nunca se solapan ni tienen tamaño configurado

---

**10.** En Spark ML, la técnica de **cross-validation** se usa para:

- a) Validar que el código Scala compila correctamente antes de ejecutar el modelo
- b) Evaluar el modelo en múltiples particiones del dataset (folds), obteniendo una estimación más robusta del rendimiento que una sola división train/test
- c) Cruzar los resultados de dos modelos distintos para elegir el mejor automáticamente
- d) Asegurar que el mismo DataFrame se puede usar tanto para entrenamiento como para inferencia sin reentrenamiento

---

## ✅ Respuestas Variante H

| # | Resp. | Por qué |
|---|-------|---------|
| 1 | **b** | Pattern matching Scala: deconstrucción de case class, match por tipo, guardas `if`, captura de variables; mucho más allá del `switch` Java |
| 2 | **b** | Transparencia referencial = sin efectos secundarios + mismo input → mismo output; pilar de la programación funcional |
| 3 | **b** | JobTracker: planificador a nivel de clúster (MRv1); TaskTracker: ejecuta tareas en cada nodo y reporta progreso |
| 4 | **b** | Retention policy: tiempo o tamaño máximo de retención de mensajes, independientemente del consumo |
| 5 | **b** | Broadcast variable: una copia por Executor en memoria, evita duplicar una variable grande en cada tarea |
| 6 | **b** | Consistencia eventual: nodos pueden divergir temporalmente, pero convergen si cesan las escrituras |
| 7 | **a** | History Server: consulta histórica persistida en HDFS; Web UI (4040): monitorización en tiempo real solo mientras el Driver vive |
| 8 | **c** | CP en CAP: ante partición, el sistema bloquea o rechaza peticiones para no devolver datos inconsistentes |
| 9 | **b** | Session window: abre/cierra según inactividad (sin tamaño fijo); tumbling/sliding: tamaño fijo definido por tiempo |
| 10 | **b** | Cross-validation: k folds → estimación robusta del rendimiento; más fiable que una sola división train/test |
