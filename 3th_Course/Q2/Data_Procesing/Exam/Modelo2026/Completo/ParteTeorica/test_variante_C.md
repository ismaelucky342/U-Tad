# Test Teoría — Variante C
**10 preguntas · 1 respuesta válida · No restan las erróneas**

---

**1.** ¿Cuál de las siguientes afirmaciones describe mejor una **case class** en Scala?

- a) Una clase abstracta que no puede ser instanciada directamente
- b) Una clase diseñada para modelar datos inmutables, con `equals`, `hashCode`, `copy` y soporte para pattern matching generados automáticamente
- c) Un objeto singleton que actúa como punto de entrada de la aplicación
- d) Una clase que hereda obligatoriamente de un trait concreto

---

**2.** ¿Cuál es la diferencia fundamental entre un **trait** y una clase abstracta en Scala?

- a) Un trait no puede tener métodos implementados; una clase abstracta sí
- b) Una clase abstracta permite herencia múltiple; un trait no
- c) Un trait puede mezclarse (mix-in) en múltiples clases a la vez y puede incluir implementaciones concretas; una clase abstracta solo admite herencia simple
- d) No hay diferencia funcional entre ambos; son intercambiables

---

**3.** En el modelo **MapReduce** de Hadoop, ¿qué ocurre entre la fase Map y la fase Reduce?

- a) Los datos se cachean en memoria para acelerar la fase de Reduce
- b) Se produce una fase de Shuffle & Sort: los pares clave-valor se agrupan por clave y se redistribuyen entre los reducers
- c) El NameNode reordena los bloques en HDFS antes de lanzar los reducers
- d) Spark intercepta los datos para optimizarlos antes de continuar

---

**4.** ¿Qué son las **5 V's del Big Data**?

- a) Velocidad, Virtualización, Variedad, Volumen, Verificación
- b) Volumen, Velocidad, Variedad, Veracidad y Valor
- c) Volumen, Versión, Variedad, Validez y Visibilidad
- d) Velocidad, Variedad, Volumen, Virtualización y Viabilidad

---

**5.** ¿Qué ventaja principal aporta el **DataFrame** sobre el **RDD** en Spark?

- a) Los DataFrames permiten almacenar datos no estructurados de forma nativa
- b) Los DataFrames no requieren una SparkSession para ser creados
- c) Los DataFrames tienen un esquema conocido, lo que permite al optimizador Catalyst generar planes de ejecución más eficientes
- d) Los DataFrames eliminan completamente la necesidad de serialización entre nodos

---

**6.** En Hadoop, ¿qué hace el componente **YARN**?

- a) Almacena los bloques de datos distribuidos en el clúster
- b) Gestiona los recursos del clúster (CPU, memoria) y planifica las tareas de las aplicaciones
- c) Proporciona una interfaz SQL para consultar datos en HDFS
- d) Es el motor de procesamiento en memoria que reemplaza a MapReduce

---

**7.** ¿Qué problema describe el concepto de **backpressure** en sistemas de streaming?

- a) La latencia añadida por la replicación de mensajes en Kafka
- b) El coste de reescribir eventos pasados cuando se detectan errores en el flujo
- c) La pérdida de mensajes cuando el broker se reinicia inesperadamente
- d) La situación en la que el sistema de procesamiento no puede consumir datos tan rápido como el productor los genera, acumulando presión en el buffer

---

**8.** ¿Cuál es el rol del **SparkSession** en una aplicación Spark moderna?

- a) Es el proceso que gestiona los recursos del clúster y asigna tareas a los Executors
- b) Es el punto de entrada unificado para usar Spark SQL, DataFrames, Datasets y configurar la aplicación
- c) Es el módulo que gestiona la tolerancia a fallos mediante checkpointing
- d) Es el componente de Structured Streaming que lee datos de Kafka

---

**9.** En Kafka, ¿qué permite un **consumer group**?

- a) Que varios productores publiquen en el mismo topic de forma ordenada
- b) Que varios consumidores compartan la lectura de un topic, repartiendo las particiones entre ellos para no duplicar el procesamiento
- c) Que un único consumidor lea de múltiples brokers a la vez
- d) Que los mensajes se almacenen indefinidamente en el topic

---

**10.** En Machine Learning, ¿qué significa **overfitting**?

- a) Cuando el modelo es demasiado simple y no captura los patrones de los datos de entrenamiento
- b) Cuando el proceso de entrenamiento consume demasiada memoria en el clúster
- c) Cuando se usan más nodos de los necesarios para entrenar un modelo distribuido
- d) Cuando el modelo aprende demasiado bien los datos de entrenamiento, incluyendo el ruido, y pierde capacidad de generalizar a datos nuevos

---

## ✅ Respuestas Variante C

| # | Resp. | Por qué |
|---|-------|---------|
| 1 | **b** | Case class: datos inmutables, pattern matching, métodos auto-generados (equals, copy…) |
| 2 | **c** | Trait: mix-in múltiple + implementaciones concretas; clase abstracta: herencia simple |
| 3 | **b** | Entre Map y Reduce existe el Shuffle & Sort: agrupa y redistribuye por clave |
| 4 | **b** | Las 5 V's son Volumen, Velocidad, Variedad, Veracidad y Valor |
| 5 | **c** | Schema conocido → Catalyst puede optimizar; RDDs son opacos al optimizador |
| 6 | **b** | YARN = Yet Another Resource Negotiator; gestiona CPU/memoria del clúster |
| 7 | **d** | Backpressure: productor más rápido que el consumidor, se acumula presión |
| 8 | **b** | SparkSession: punto de entrada unificado (reemplaza a SQLContext y HiveContext) |
| 9 | **b** | Consumer group: varios consumidores se reparten particiones sin duplicar mensajes |
| 10 | **d** | Overfitting = memorizar el entrenamiento (incluido el ruido), sin generalizar |
