# Unidad 5. Spark Streaming: Contextualización.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Spark Streaming: Contextualización](#2-spark-streaming-contextualización)
  - [2.1 Introducción](#21-introducción)
  - [2.2 Características de los Sistemas Streaming](#22-características-de-los-sistemas-streaming)
  - [2.3 Procesamiento por lotes (batch) vs Procesamiento Streaming](#23-procesamiento-por-lotes-batch-vs-procesamiento-streaming)
  - [2.4 Dificultades de los sistemas Streaming](#24-dificultades-de-los-sistemas-streaming)
  - [2.5 Procesamiento en Streaming: Estrategias y Retos](#25-procesamiento-en-streaming-estrategias-y-retos)
  - [2.6 Semántica de Entrega en Streaming](#26-semántica-de-entrega-en-streaming)
  - [2.7 Conceptos fundamentales en sistemas de streaming](#27-conceptos-fundamentales-en-sistemas-de-streaming)
  - [2.8 Lambda y Kappa: enfoques arquitectónicos para Big Data](#28-lambda-y-kappa-enfoques-arquitectónicos-para-big-data)
  - [2.9 Cubos OLAP y análisis en tiempo real](#29-cubos-olap-y-análisis-en-tiempo-real)
  - [2.10 Transformaciones sin y con estado en procesamiento de streaming](#210-transformaciones-sin-y-con-estado-en-procesamiento-de-streaming)
  - [2.11 Ejercicios](#211-ejercicios)
- [3. Apache Kafka](#3-apache-kafka)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Arquitectura](#32-arquitectura)
  - [3.3 Conceptos necesarios en Kafka](#33-conceptos-necesarios-en-kafka)
  - [3.4 Ecosistema confluente Platform](#34-ecosistema-confluente-platform)
  - [3.5 Schema Registry](#35-schema-registry)
  - [3.6 Interfaces y herramientas de integración en Kafka](#36-interfaces-y-herramientas-de-integración-en-kafka)
  - [3.7 Ejercicios](#37-ejercicios)
- [4. Structured Streaming](#4-structured-streaming)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Event time](#42-event-time)
  - [4.3 Fault tolerance en structured streaming](#43-fault-tolerance-en-structured-streaming)
  - [4.4 Input Sources](#44-input-sources)
  - [4.5 Operations](#45-operations)
  - [4.6 Output sinks](#46-output-sinks)
  - [4.7 Gestión y monitorización de consultas en Spark Structured Streaming (StreamingQuery)](#47-gestión-y-monitorización-de-consultas-en-spark-structured-streaming-streamingquery)
  - [4.8 Ejercicios](#48-ejercicios)
- [5. Streams](#5-streams)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Fuentes entrada y de salida](#52-fuentes-entrada-y-de-salida)
  - [5.3 Operaciones de ventana](#53-operaciones-de-ventana)
  - [5.4 Principales transformaciones disponibles en Spark Streaming](#54-principales-transformaciones-disponibles-en-spark-streaming)
  - [5.5 Ejemplos](#55-ejemplos)
- [6. Conclusiones](#6-conclusiones)
  - [6.1 Conclusiones de la unidad](#61-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad se abordarán los fundamentos, arquitecturas y herramientas clave para el procesamiento de datos en tiempo real, una necesidad creciente en entornos donde los datos fluyen de manera continua y requieren análisis inmediato. Se presentarán tecnologías como Spark Streaming, Apache Kafka y Structured Streaming, así como el modelo tradicional de DStreams, permitiendo al alumno comprender las distintas aproximaciones y su evolución dentro del ecosistema de Big Data.

El procesamiento en tiempo real es esencial en contextos donde las decisiones deben tomarse con baja latencia, como la monitorización de infraestructuras, la detección de fraudes o la analítica de comportamiento de usuarios. Para lograrlo, se requiere un conocimiento profundo sobre cómo modelar el tiempo en los flujos de datos, gestionar el estado del procesamiento, garantizar tolerancia a fallos y aplicar transformaciones eficaces sobre datos que no dejan de llegar.

A lo largo de esta unidad, se analizarán modelos arquitectónicos como Lambda y Kappa, se estudiarán mecanismos como las ventanas temporales, la semántica de entrega y el control de flujo (backpressure), y se explorarán herramientas especializadas que permiten la ingesta, transporte y transformación de eventos en tiempo real.

Especial atención se dedicará a Apache Kafka como sistema de mensajería distribuido, a las capacidades avanzadas de Structured Streaming para procesar flujos de datos con garantías de exactitud y tolerancia a fallos, y al modelo original de DStreams, permitiendo comparar enfoques basados en micro-lotes.

Además, se propondrán ejercicios prácticos para que el alumno desarrolle habilidades en la implementación de pipelines de datos en tiempo real, aplicando transformaciones, ventanas, controles de estado y estrategias de integración con otras herramientas del ecosistema.

Los apartados a tratar en esta unidad didáctica serán:



- **Spark Streaming: Contextualización**  
  Este capítulo aborda los fundamentos del procesamiento de datos en flujo, sus principales características y diferencias con respecto al procesamiento batch, así como los retos que plantea su implementación en entornos reales. A través del estudio de arquitecturas, técnicas y herramientas específicas, se analizarán las soluciones actuales para lograr un procesamiento continuo, fiable y escalable.
- **Apache Kafka**  
  **Apache Kafka** es una plataforma distribuida de mensajería de alto rendimiento, diseñada para manejar flujos de datos en tiempo real de manera eficiente, fiable y escalable. Fue desarrollada inicialmente por LinkedIn y liberada como software de código abierto en 2011. Está escrita principalmente en **Scala** y **Java,** y cuenta con un equipo activo de desarrollo formado por 9 committers principales y alrededor de 20 colaboradores adicionales.
- **Structured Streaming**  
  **Spark Structured Streaming** es un motor escalable y tolerante a fallos para el procesamiento de flujos de datos en tiempo real. Está construido sobre el motor de **Spark SQL**, lo que permite aplicar la misma lógica y API que se usa para el procesamiento por lotes (batch), simplificando enormemente el desarrollo.
- **DStreams**  
  El modelo de ejecución de Spark Streaming se basa en dividir el flujo de datos en pequeños lotes o **batches**, que se procesan utilizando las capacidades de cómputo de Spark a través de su núcleo: los **RDDs** (Resilient Distributed Datasets). Esto da lugar a una abstracción denominada **DStream** (**Discretized Stream**), que representa un flujo continuo de datos como una **secuencia de RDDs**.



#### Objetivos



1. **Comprender** los fundamentos del procesamiento de datos en tiempo real y su relevancia en el ecosistema Big Data actual.
2. **Diferenciar** los modelos de procesamiento por lotes y en streaming, analizando sus ventajas, limitaciones y casos de uso.
3. **Analizar** las principales arquitecturas para el procesamiento en tiempo real, como los modelos Lambda y Kappa.
4. **Explorar** las características y el funcionamiento de Apache Kafka como sistema de mensajería distribuida para flujos de datos.
5. **Identificar** los componentes clave de Spark Streaming y Structured Streaming, así como su evolución y diferencias técnicas.
6. **Aplicar** transformaciones sobre flujos de datos utilizando conceptos como ventanas temporales, estados y marcas de agua.
7. **Evaluar** los distintos modos de entrega de eventos en sistemas distribuidos (at-most-once, at-least-once, exactly-once) y sus implicaciones.
8. **Configurar** pipelines de procesamiento de datos en tiempo real, integrando Kafka, Spark y herramientas del ecosistema como Connect o ksqlDB.
9. **Desarrollar** aplicaciones prácticas de análisis de eventos en tiempo real, utilizando Structured Streaming con tolerancia a fallos y semántica de entrega controlada.
10. **Afianzar** los conocimientos adquiridos mediante ejercicios prácticos que simulen escenarios reales de monitorización, análisis y toma de decisiones en streaming.



## 2. Spark Streaming: Contextualización



### 2.1 Introducción



![image](assets/cm8z0y767004u356xr2425qmo-stock-image.jpg)



El volumen, la velocidad y la variedad de los datos generados actualmente por sistemas digitales han impulsado la necesidad de nuevas arquitecturas de procesamiento que vayan más allá del enfoque tradicional por lotes (procesos Batch). En numerosos contextos, desde la monitorización de infraestructuras hasta la detección temprana de fraudes, se requiere la capacidad de procesar eventos en el momento en que ocurren, lo que ha dado lugar al paradigma del streaming de datos.

Este capítulo aborda los fundamentos del procesamiento de datos en flujo, sus principales características y diferencias con respecto al procesamiento batch, así como los retos que plantea su implementación en entornos reales. A través del estudio de arquitecturas, técnicas y herramientas específicas, se analizarán las soluciones actuales para lograr un procesamiento continuo, fiable y escalable.

El enfoque progresivo permitirá comprender desde los conceptos esenciales hasta las distintas estrategias de modelado temporal, control de latencia, tolerancia a fallos y mecanismos de consistencia. Todo ello asentará las bases para introducir, más adelante, tecnologías clave como Apache Kafka y Spark Streaming.

Podemos concluir que **un sistema de streaming es una arquitectura que permite procesar datos en tiempo real, a medida que se generan, sin necesidad de almacenarlos previamente.** Está diseñado para manejar flujos continuos e ininterrumpidos de información, lo que lo hace ideal para aplicaciones que requieren respuestas rápidas, como la monitorización, detección de fraudes o el análisis en vivo de datos provenientes de sensores o redes sociales.



### 2.2 Características de los Sistemas Streaming



Los sistemas de procesamiento en *streaming*presentan una serie de particularidades que los diferencian del procesamiento tradicional por lotes. A continuación, se destacan sus principales características:

- Un sistema de streaming procesa datos como una **corriente continua e ininterrumpida de eventos**, sin un punto de finalización definido.
- A diferencia del procesamiento por lotes (*batch*), no es posible tratar todos los eventos a la vez, ya que el flujo de datos es **potencialmente infinito**. Para gestionar esto, se utilizan **ventanas temporales** o estrategias basadas en el número de eventos.
- Una de sus principales ventajas es la **capacidad de respuesta casi inmediata**, lo que permite actuar sobre los datos en tiempo real.
- Se emplea en una gran variedad de aplicaciones, como la **monitorización de dispositivos IoT, detección de fraudes, ciberseguridad y dashboards en tiempo real**, entre otros casos de uso.
- Existen diversas tecnologías diseñadas para el procesamiento en streaming, entre las que destacan **Apache Flink, Apache Kafka, Spark Streaming, Apache Storm y Amazon Kinesis**.



![image](assets/cm8z115bw0090356xpq2zn2ns-INSD_PRDT_U5_Apartado3-2_Imagen1.jpg)



### 2.3 Procesamiento por lotes (batch) vs Procesamiento Streaming



El procesamiento en streaming y el procesamiento por lotes (batch) representan dos enfoques distintos para el tratamiento de datos. Mientras que el batch se centra en conjuntos finitos de datos almacenados, el streaming permite analizar información en tiempo real. La siguiente tabla resume las principales diferencias entre ambos modelos:

| Criterio | Batch (Procesamiento por lotes) | Streaming (Procesamiento en flujo) |
| --- | --- | --- |
| Datos | Se procesan datos almacenados y finitos. | Los datos llegan de manera continua e infinita. |
| Estado | Los datos están en reposo ( at rest ). | Los datos están en movimiento ( in motion ). |
| Procesamiento | Se ejecuta en momentos específicos, procesando grandes volúmenes de datos acumulados. | Se procesan los datos en cuanto llegan, de manera inmediata. |
| Utilidad | Se usa para análisis históricos y entrenar modelos con datos de largo plazo. | Permite monitorizar eventos en tiempo real y reaccionar al instante. |
| Decisiones | Se toman decisiones estratégicas basadas en análisis pasados. | Se toman decisiones tácticas y en tiempo real. |
| Orden | No importa el orden de llegada de los datos. | El orden de llegada es crucial para el procesamiento. |
| Trigger | Se ejecuta bajo demanda, en momentos programados. | Funciona de manera continua, operando 24/7. |
| Coste | Generalmente menor, pues usa recursos de manera puntual. | Mayor costo debido al uso constante de recursos. |
| Actualización | Una vez desplegado, el sistema se actualiza en el siguiente lote. | No se puede actualizar sin detener y reiniciar el proceso. |
| Fuentes | Se basa en datos estáticos, como archivos o bases de datos. | Recibe datos en tiempo real de dispositivos móviles, IoT y sistemas de monitorización. |
| Cuándo usarlo | Ideal para procesamiento ocasional, cuando no es necesaria una respuesta inmediata. | Útil en escenarios con alta demanda de baja latencia, como detección de fraudes o análisis de streaming en vivo. |



### 2.4 Dificultades de los sistemas Streaming



El procesamiento de datos en streaming presenta diversos desafíos técnicos que deben abordarse para garantizar un funcionamiento fiable y eficiente.



1. Uno de los principales retos es garantizar que los eventos se procesen en el orden correcto. Debido a la naturaleza asíncrona del streaming, puede ocurrir que ciertos eventos lleguen antes que otros, aunque cronológicamente deberían haber ocurrido después. Esto puede generar problemas, por ejemplo, si un sistema procesa un evento de *cierre*antes de haber recibido el evento de *apertura*correspondiente.
2. En entornos distribuidos, siempre existe el riesgo de fallos en los nodos de procesamiento *(workers)*. Es crucial contar con mecanismos de recuperación que permitan restaurar el estado del sistema sin perder datos o generar duplicaciones innecesarias. En caso de fallo, el sistema debe poder reanudar la ejecución desde el último punto seguro *(checkpointing)*y redistribuir la carga de trabajo entre los nodos restantes.
3. A diferencia del procesamiento por lotes, donde los datos se procesan en grandes volúmenes de manera periódica, en streaming el flujo de datos es continuo, lo que implica una escritura constante en almacenamiento o bases de datos. Esto supone un desafío en términos de rendimiento y eficiencia, ya que es necesario optimizar el uso de los recursos sin generar cuellos de botella en el sistema.
4. En algunos escenarios, los datos procesados anteriormente pueden necesitar ser corregidos o actualizados. Sin embargo, dado que los sistemas de streaming procesan datos en tiempo real, gestionar cambios en eventos pasados puede ser un desafío, especialmente cuando se trata de garantizar consistencia y evitar inconsistencias en los resultados.
5. Muchas aplicaciones en streaming requieren un funcionamiento ininterrumpido, lo que implica minimizar el tiempo de inactividad y contar con estrategias de recuperación ante fallos. Mantener una infraestructura operativa y escalable en todo momento es esencial para sistemas de misión crítica.



La imagen representa un flujo típico de procesamiento de datos en streaming con un modelo basado en MapReduce.



![image](assets/cm8z1836000fz356xwpurctf4-Imagen1.jpg)



1. **Entrada de eventos:** Se reciben eventos en tiempo real desde dispositivos móviles (por ejemplo, registros de apertura y cierre de aplicaciones).
2. **Mapeo:** Los eventos son clasificados en función de su tipo (open, close) y el tiempo en que ocurrieron.
3. **Reducción:** Se agregan los eventos por acción y por hora, generando recuentos de ocurrencias.
4. **Almacenamiento final:** Los datos procesados se almacenan en una base de datos MySQL como "output sink", listos para su consulta y análisis.

Este esquema ilustra cómo un sistema de streaming puede procesar grandes volúmenes de eventos en tiempo real, aplicando técnicas de agregación para generar métricas útiles y manejar de forma eficiente grandes flujos de datos.



### 2.5 Procesamiento en Streaming: Estrategias y Retos



El procesamiento en streaming puede adoptar diferentes enfoques según las necesidades de latencia, escalabilidad y fiabilidad. Dos de los modelos más utilizados son el procesamiento en **tiempo real** (*real-time*) y el basado en **micro-lotes** (*micro-batch* o *near-real-time*).



- **Real-Time**  
  En este modelo, los datos se procesan de manera continua e inmediata, lo que permite una respuesta en milisegundos. Este enfoque requiere un uso intensivo de recursos y un diseño más complejo para garantizar la escalabilidad. Además, la lógica de procesamiento difiere significativamente del modelo por lotes (batch), lo que implica retos adicionales en su implementación. Entre sus características hay que destacar:

  - Procesa los eventos tan pronto como llegan, sin necesidad de agruparlos.
  - Introducido en **Spark 2.3** con el **Continuous Processing Engine**, diseñado para reducir la latencia al mínimo.
  - Permite alcanzar latencias del orden de **1 milisegundo**, lo que lo convierte en una opción ideal para aplicaciones ultra sensibles al tiempo, como detección de fraudes o control industrial.
- **Micro-Batch o Near-Real-Time**  
  En este esquema, los datos se agrupan en pequeños lotes antes de ser procesados, lo que introduce una latencia relativamente mayor. Sin embargo, su diseño es más simple y se asemeja a la lógica tradicional del procesamiento por lotes, lo que facilita la escalabilidad y la integración con sistemas existentes. Resumiendo sus características podemos decir:

  - Este modelo agrupa los eventos durante un pequeño intervalo de tiempo antes de procesarlos.
  - Fue el comportamiento **por defecto en Spark Streaming hasta la versión 2.3.**
  - Opera con **una latencia media (~100 ms)**, adecuada para muchos casos de uso que no requieren respuesta instantánea.
  - Es **más sencillo de implementar y escalar**, ya que la lógica de procesamiento es muy similar a la del modelo por lotes.

  Esta imagen representa el procesamiento basado en **micro-batches** (*near real-time*), donde los datos no se procesan de forma continua, sino en pequeños lotes.
  ![image](assets/cm8z1bnzv00i3356xrya9x9eu-tab2-img1-INSD_PRDT_U5_Apartado3-5_Imagen3.jpg)



Cada conjunto de eventos se acumula durante un período de tiempo y luego es procesado en bloque (batch). Los embudos en la imagen indican momentos de procesamiento, que ocurren en intervalos regulares. Este modelo introduce una pequeña latencia en comparación con el streaming puro, pero es más fácil de escalar y mantener.

Para garantizar la fiabilidad en sistemas de streaming, es fundamental contar con estrategias que permitan recuperar el estado del procesamiento en caso de fallos. Dos de las más utilizadas son la **replicación de datos** y el **checkpointing.**



- **Replicación de Datos**  
  Consiste en duplicar los datos en múltiples nodos o particiones, asegurando su disponibilidad incluso si una parte del sistema falla. Este enfoque es clave para mantener la continuidad del servicio en arquitecturas distribuidas.
- **Checkpointing**  
  Se basa en guardar periódicamente el estado del procesamiento en un almacenamiento duradero, como HDFS o Amazon S3. En caso de fallo, el sistema puede reiniciar desde el último punto guardado, minimizando la pérdida de datos y asegurando la continuidad de la operación.

  El siguiente esquema ilustra cómo el mecanismo de checkpointing permite recuperar el estado del sistema en caso de fallo, asegurando la continuidad del procesamiento de datos en streaming.
  ![image](assets/cm8z1fa1h00jo356xujpptb3x-tab2-img1-INSD_PRDT_U5_Apartado3-5_Imagen4.jpg)



**Para finalizar este apartado, veamos las dimensiones temporales clave en streaming**

Para interpretar correctamente los datos en sistemas de streaming, es necesario distinguir entre tres conceptos temporales fundamentales:

- **Event time**: Momento exacto en que el evento fue generado en el sistema de origen.
- **Ingestion time**: Momento en que el evento llega al sistema de procesamiento.
- **Processing time**: Momento en que el evento es efectivamente procesado por la aplicación.



### 2.6 Semántica de Entrega en Streaming



Cuando se procesan datos en sistemas distribuidos de streaming, es fundamental definir la semántica de entrega, es decir, cómo se garantiza el procesamiento de cada evento. Existen tres modelos principales, cada uno con implicaciones distintas en cuanto a fiabilidad, duplicidad y pérdida de datos:



- **At-least-once (al menos una vez)**  
  Este enfoque garantiza que todos los eventos serán procesados al menos una vez, incluso si el sistema falla y debe reintentar. El inconveniente es que pueden producirse duplicados, ya que un mismo evento podría procesarse más de una vez en caso de reenvíos automáticos.
- **At-most-once (como mucho una vez)**  
  Asegura que no habrá duplicados, ya que los eventos se procesan una única vez o se descartan. Sin embargo, esto implica que algunos eventos pueden perderse si se produce un fallo antes de su tratamiento.
- **Exactly-once (exactamente una vez)**  
  Es el modelo más deseado, pero también el más complejo de implementar. Garantiza que cada evento será procesado una única vez, sin duplicados y sin pérdidas. Spark Structured Streaming está diseñado para trabajar bajo esta semántica, combinando mecanismos como *checkpointing*y *sinks*idempotentes.



La siguiente imagen muestra una conocida ironía del mundo de los sistemas distribuidos publicada **en Twitter (X)** por el experto Mathias Verraes: lograr la entrega de mensajes exactamente una vez y mantener su orden correcto son considerados dos de los problemas más difíciles, hasta el punto de que incluso se confunden entre sí. Esta cita refleja la complejidad real que conlleva garantizar consistencia en arquitecturas distribuidas de streaming.



![image](assets/cm8z1k3m400nq356x9b3zk6ci-INSD_PRDT_U5_Apartado3-6_Imagen5.jpg)



### 2.7 Conceptos fundamentales en sistemas de streaming



Para comprender en profundidad el funcionamiento de los sistemas de procesamiento en streaming, es necesario conocer una serie de conceptos fundamentales que influyen directamente en su rendimiento, escalabilidad y capacidad de respuesta. A continuación, se describen los más relevantes.



#### Tipos de Ventanas en Streaming



En sistemas de streaming, los datos fluyen de forma continua e ininterrumpida. Para poder analizarlos de forma útil, se agrupan en **ventanas**, que definen cómo segmentar esos flujos para aplicar agregaciones o cálculos.



- **Tumbling Window (Ventana Temporal)**  
  Divide el flujo en bloques de tiempo fijos, no superpuestos.
  Ejemplo: calcular el promedio de ventas por hora.
- **Sliding Window (Ventana Deslizante)**  
  Similar a la anterior, pero los intervalos se solapan.
  Ejemplo: sumar ventas de los últimos 10 minutos, actualizándose cada minuto.
- **Session Window (Ventana de Sesión)**  
  Agrupa eventos en función de la actividad/inactividad del usuario.
  Ejemplo: segmentar sesiones de navegación en una web.
- **Count Window (Ventana por Conteo)**  
  En lugar de tiempo, se basa en la cantidad de eventos recibidos.
  Ejemplo: analizar sentimientos sobre los últimos 100 tweets.



La siguiente imagen compara dos tipos de ventanas comunes en el procesamiento de datos en streaming:

- En la **ventana temporal**, los eventos se agrupan en bloques de tiempo fijo (por ejemplo, cada hora). Cada grupo de eventos se etiqueta y luego se agregan sus datos antes de ser enviados a una base de datos.
- En la **ventana por conteo**, en cambio, se agrupan bloques de eventos en función de su cantidad (por ejemplo, cada 1000 eventos), sin considerar el tiempo. El proceso posterior de etiquetado, agregación y almacenamiento es equivalente.



![image](assets/cm8z1ongj00s0356xrch518yb-INSD_PRDT_U5_Apartado3-7-1_Imagen6.jpg)



El objetivo es mostrar que las ventanas pueden definirse tanto por **tiempo** como por **volumen de datos**, lo cual impacta en cómo se estructura el procesamiento en tiempo real.

Veamos en la siguiente imagen un ejemplo concreto de uso de ventanas temporales en un sistema de ventas por hora:

- Los eventos corresponden a transacciones (con su hora y monto en euros).
- Las ventanas están definidas por franjas horarias fijas (por ejemplo, 16:00–16:59, 17:00–17:59...).
- Cada ventana agrupa las ventas ocurridas en ese intervalo y calcula el total de ingresos.
- Finalmente, los resultados agregados se almacenan en una base de datos.



![image](assets/cm8z1pp7300td356xctx1inlu-Imagen2.jpg)



#### Escalabilidad y Distribución de Carga



El procesamiento de grandes volúmenes de datos en tiempo real requiere que el sistema sea **escalable y eficiente**:



- **Escalabilidad horizontal**  
  El sistema debe poder procesar más datos al añadir más nodos al clúster, idealmente con escalado lineal.
- **Particionamiento**  
  Consiste en dividir los datos para su procesamiento paralelo, mejorando la eficiencia.
- **Balanceo de carga**  
  Distribuye uniformemente el trabajo entre nodos, evitando sobrecargas.
- **Elasticidad**  
  Capacidad de adaptar los recursos dinámicamente según la carga.



La siguiente figura muestra cómo se redistribuye la carga cuando se incrementa el número de eventos por segundo, añadiendo nuevos nodos para mantener el rendimiento.



![image](assets/cm8z1tdts00ws356xfom55q7r-INSD_PRDT_U5_Apartado3-7-2_Imagen8.jpg)



#### Backpressure: Control de Flujo en Tiempo Real



En flujos de datos continuos, puede ocurrir que el ritmo de emisión supere la capacidad de procesamiento del sistema, provocando **saturaciones** o **pérdida de eventos.**

- Esto se conoce como **backpressure**.
- La solución es que el receptor informe al emisor de su capacidad, para que este reduzca la velocidad de emisión.

La imagen ilustra un escenario clásico de backpressure, donde un emisor genera eventos más rápido de lo que el receptor puede procesar, lo que obliga a aplicar mecanismos de control de flujo.



![image](assets/cm8z1uqg700ym356xzxg2vdme-INSD_PRDT_U5_Apartado3-7-3_Imagen9.jpg)



### 2.8 Lambda y Kappa: enfoques arquitectónicos para Big Data



En el contexto del procesamiento de grandes volúmenes de datos, han surgido diversas arquitecturas que intentan equilibrar la necesidad de análisis histórico y el procesamiento en tiempo real. Entre ellas destacan los modelos **Lambda** y **Kappa,** ampliamente utilizados en entornos de Big Data.



#### Arquitectura Lambda



La arquitectura Lambda propone una solución híbrida que combina dos capas de procesamiento:

- Una Batch Layer (capa por lotes) que almacena y procesa todos los datos históricos, produciendo vistas agregadas precisas.
- Una Speed Layer (capa rápida) que permite cálculos inmediatos sobre los datos más recientes, compensando la latencia natural del procesamiento batch.

Finalmente, la Serving Layer unifica ambas capas y proporciona acceso a los datos preprocesados mediante vistas optimizadas.

Este enfoque permite cubrir tanto el análisis en tiempo real como el procesamiento complejo a largo plazo, pero presenta complejidad técnica elevada, ya que requiere mantener y sincronizar dos rutas de código distintas.

La primera imagen ilustra la arquitectura Lambda, mostrando cómo el flujo de eventos se divide en una ruta caliente (hot path) para el procesamiento en tiempo real y una ruta fría (cold path) para el procesamiento batch.



![image](assets/cm8z1x2hc0118356xcbnhb8h4-INSD_PRDT_U5_Apartado3-8_Imagen10.jpg)



La segunda imagen profundiza en esta idea, destacando cómo los datos de distintas fuentes son procesados y posteriormente servidos a sistemas de consulta o visualización.



![image](assets/cm8z1xupu012l356xran5ww2w-INSD_PRDT_U5_Apartado3-8_Imagen11.jpg)



#### Arquitectura Kappa



La arquitectura Kappa, propuesta en 2014 por **Jay Kreps** (fundador de Confluent y uno de los creadores de Kafka), plantea una simplificación radical del modelo Lambda:

- Todos los datos, tanto para procesamiento histórico como en tiempo real, se manejan como **streams**.
- Utiliza una única tecnología de streaming (por ejemplo, Kafka + un motor de procesamiento como Flink o Spark Structured Streaming).
- Todo el histórico se almacena como un **log inmutable**, y las vistas batch pueden ser recalculadas directamente a partir del stream almacenado.

Este modelo busca **simplificar el mantenimiento**, evitando duplicación de lógica y tecnologías, al tiempo que se aprovechan las ventajas del streaming para todas las necesidades analíticas.

La imagen muestra el modelo Kappa, donde todos los datos se almacenan en un log unificado y se procesan desde una única capa en streaming. En caso necesario, es posible recalcular vistas a partir del histórico almacenado, eliminando la necesidad de una capa batch separada.



![image](assets/cm8z1z75k014f356xqncx1e3y-INSD_PRDT_U5_Apartado3-8_Imagen12.jpg)



- **Ventaja de Lambda:** Precisión analítica a largo plazo + capacidad de respuesta rápida.
- **Desventaja de Lambda:** Alta complejidad operacional y mantenimiento duplicado.
- **Ventaja de Kappa:** Sencillez, menor mantenimiento, ideal para pipelines puramente en streaming.
- **Desventaja de Kappa:** Puede no ser ideal para cálculos extremadamente pesados sobre datos históricos extensos.



### 2.9 Cubos OLAP y análisis en tiempo real



Los **cubos OLAP** (Online Analytical Processing) son estructuras de datos multidimensionales diseñadas para facilitar el análisis de grandes volúmenes de información desde múltiples perspectivas. Estos cubos permiten realizar consultas complejas mediante operaciones como **agrupaciones, filtros, drill-down y pivoteos,** lo que los convierte en herramientas clave para detectar **patrones, tendencias y relaciones** en los datos.

Cada cubo se compone de **dimensiones,** que representan las categorías por las que se desea analizar la información (como tiempo, región, producto...),**y medidas,** que son los valores numéricos que se desean estudiar (como ventas, ingresos, etc.).

Tradicionalmente, los cubos OLAP se actualizaban de forma periódica a partir de datos por lotes, lo que limitaba su capacidad de reflejar el estado más reciente del negocio. Sin embargo, gracias al **procesamiento de datos en streaming,** es posible alimentar estos cubos en **tiempo real,** actualizando sus métricas a medida que los datos llegan.

Esta integración permite que los usuarios accedan a informes y análisis**sobre los datos más actuales,** lo que mejora la toma de decisiones y ofrece una visión dinámica del negocio, especialmente útil en contextos como ventas, logística, seguridad o análisis de comportamiento de usuarios.



![image](assets/cm8z22fsx016k356x6w2tob2c-INSD_PRDT_U5_Apartado3-9_Imagen13.jpg)



### 2.10 Transformaciones sin y con estado en procesamiento de streaming



En el contexto del procesamiento de datos en streaming, es fundamental distinguir entre dos tipos de transformaciones según su gestión del estado: las **stateless** y las **stateful**.



- **Transformaciones Stateless (sin estado)**  
  Las transformaciones **stateless** no requieren almacenar información sobre eventos anteriores. Cada evento es procesado de manera independiente, sin necesidad de contexto adicional:

  - El **orden** de llegada no influye en el resultado.
  - No se mantiene **estado interno,** lo que permite que el sistema se recupere fácilmente en caso de fallo.
  - Son ideales para operaciones simples como filtrado, mapeo o validaciones puntuales.
  - Su funcionamiento se basa en **buffers temporales** de eventos entrantes no procesados, sin necesidad de estructuras persistentes.

  Este tipo de transformaciones ofrece alta eficiencia y escalabilidad, siendo adecuadas para sistemas que requieren baja latencia y procesamiento inmediato de eventos individuales.
- **Transformaciones Stateful (con estado)**  
  En cambio, las transformaciones **stateful** requieren mantener información acumulada o contextual sobre los datos previamente procesados. Esto permite realizar cálculos más complejos, pero también introduce ciertos retos:

  - Dependen de **conjuntos de eventos** para generar resultados (por ejemplo, para agregaciones o detección de patrones).
  - El **orden** de los eventos puede ser importante para obtener resultados correctos.
  - Es necesario almacenar y actualizar un **estado interno**, que puede involucrar ventanas de tiempo, contadores o estructuras de agrupación.
  - En caso de fallo, se requiere recuperar el estado previo para continuar el procesamiento sin inconsistencias.
  - Las transformaciones pueden aplicarse sobre el **stream completo** o sobre **subconjuntos definidos por ventanas** (tumbling, sliding, session...).

  Este modelo es fundamental en aplicaciones que requieren lógica más rica, como análisis en tiempo real, detección de fraudes o análisis de sesiones de usuario.



### 2.11 Ejercicios



#### Ejercicio 1: Análisis de velocidades de Fórmula 1



Tenemos un sistema que detecta velocidades en un punto del circuito durante una sesión de entrenamiento de Fórmula 1. Los datos recolectados son eventos con una marca de tiempo, el ID del conductor y la velocidad medida.

Ahora, queremos calcular el rango de velocidades (es decir, la diferencia entre la velocidad máxima y mínima) usando diferentes tipos de ventanas de procesamiento. Estas ventanas nos permiten agrupar eventos de distintas formas para analizar los datos.

Tenemos un sistema de monitorización de una jornada de entrenamientos de Fórmula 1. En un punto dado del circuito, tenemos un radar de velocidad que nos arroja los siguientes datos:



```elixir
EventID, Time, DriverID, Speed
------------------------------
0, 9:00.235, 7, 180
1, 9:00.237, 3, 185
2, 9:00.249. 4, 190
3, 9:00.450, 5, 192
4, 9:00.795, 8, 182
5, 9:00.815, 1, 198
6, 9:01.005, 6, 195
7, 9:01.204, 2, 184
8, 9:01.429, 9, 194
9, 9:01.626, 0, 199
```



Calcula el rango (para ello, indica almancena también valor máximo y mínimo) indicando Key, Max, Min y Range (Key=KeyId, Max=MaxNum, Min=MinNum, Range=MaxNum-MinNum) con los siguientes tipos de ventanas:

1. Resolver con ventana temporal cada segundo (cada ventana empieza con el cambio de segundo)
2. Resolver con ventana por número de eventos de tamaño 5
3. Resolver con ventana deslizante de 200ms para calcular el rango del último segundo (primera ventana entre las 9:00.000 y las 9:01:00)
4. Resolver con venta de sesión donde el periodo de inactividad es de 200ms

En el siguiente video analizamos la resolución de este primer ejercicio:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652194_1/scormcontent/assets/INSD_PRDT_U5_Apartado3-11_Video1EjercicioRangos.mp4?v=1)



#### Ejercicio 2



Tenemos un sistema de monitorización de una jornada de entrenamientos de Fórmula 1. En un momento dado, hay 20 coches en pista y cada uno está produciendo 50 eventos por segundo. Sin embargo, nuestro sistema de monitorización está desplegado con 2 nodos y solo es capaz de procesar 500 eventos por segundo. Propon 2 soluciones para que nuestro sistema no se sature y no se pierdan datos.



#### Ejercicio 3



Indica qué semántica de entrega es más conveniente para cada uno de estos escenarios:

a) Monitorizar sensores de una estación metereológica.

b) Procesamiento de pedidos en tienda on-line.

c) Sistema de control de inventario de una farmacia.

d) Sistema de monitorización de piloto automático de avión

e) Detectar tendencias en redes sociales.

f) Alerta de ataque informático en CPD.

La solución a los ejercicios 2 y 3 se puede comprobar en el siguiente video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652194_1/scormcontent/assets/INSD_PRDT_U5_Apartado3-11_Video2Ejercicio2y3.mp4?v=1)



#### Ejercicio 4:  Preguntas teóricas



1. Si tenemos datos sobre ventas de una tienda on-line almacenados en HDFS, ¿cómo podríamos calcular la media de ventas por día con una arquitectura Lambda? ¿Y con una arquitectura Kappa?
2. Para un sistema de detección de incendios, ¿utilizarías una aproximación Microbatch o Real-time para sus sensores?
3. Tomando el caso de uso del ejercicio 1, explica cuando se producen los siguientes eventos:

- Event time
- Ingestion time
- Processing time



#### Ejercicio 5



Realiza el ejercicio 1 con un sistema Real-Time con estado y qué harías para mejorar la tolerancia a fallos

Finalmente, en el video siguiente se explica la respuesta de los ejercicios 4 y 5:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652194_1/scormcontent/assets/INSD_PRDT_U5_Apartado3-11_Video3Ejercicio4y5.mp4?v=1)



## 3. Apache Kafka



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



**Apache Kafka** es una plataforma distribuida de mensajería de alto rendimiento, diseñada para manejar flujos de datos en tiempo real de manera eficiente, fiable y escalable. Fue desarrollada inicialmente por LinkedIn y liberada como software de código abierto en 2011. Está escrita principalmente en **Scala** y **Java,** y cuenta con un equipo activo de desarrollo formado por 9 committers principales y alrededor de 20 colaboradores adicionales.

​El sitio web oficial de Apache Kafka ([http://kafka.apache.org/](https://kafka.apache.org/)) ofrece una amplia gama de recursos y documentación para comprender y utilizar esta plataforma de streaming de eventos distribuida.

En 2014, los creadores de Kafka fundaron la empresa**Confluent,** una startup enfocada en ofrecer soluciones empresariales y formación avanzada sobre esta tecnología. Se puede acceder a su formación en  ([https://www.confluent.io/training](https://www.confluent.io/training)). Su objetivo era claro: ofrecer una **plataforma unificada para gestionar todos los datos en tiempo real** dentro de una gran organización.



![image](assets/cm8zl9bj3000z356yx7rl6xgm-INSD_PRDT_U5_Apartado4-1_Imagen16.jpg)



La motivación detrás de Kafka surge de la necesidad de una solución capaz de integrar sistemas de producción y consumo de datos en tiempo real de manera robusta. Entre sus principales características destacan:

- **Alto rendimiento:** capaz de manejar millones de eventos por segundo.
- **Durabilidad:** los mensajes se persisten en disco para garantizar su integridad.
- **Alta disponibilidad:** permite la replicación de datos para mantener la continuidad del servicio ante fallos.
- **Escalabilidad:** puede escalar horizontal y verticalmente para adaptarse al volumen y ritmo de los datos.



1. En arquitecturas de mensajería, el **broker** actúa como intermediario entre los productores (quienes generan los datos) y los consumidores (quienes los procesan). Su función es **recibir, almacenar temporalmente y enrutar los eventos de datos** desde los productores hacia los consumidores.

   **En sistemas tradicionales:**

   1. El productor envía los mensajes al broker.
   2. El broker los almacena en memoria o disco.
   3. El cliente consumidor recibe el mensaje.
   4. El broker lo elimina tras ser consumido.
2. ![image](assets/cm8zlaxr1002c356ybb3zem65-step2-INSD_PRDT_U5_Apartado4-1_Imagen17.jpg)
   En los sistemas tradicionales, el modelo de comunicación entre productores, brokers y consumidores presentaba importantes limitaciones en términos de escalabilidad y resiliencia. Una evolución natural fue la introducción del **broker en alta disponibilidad (HA)**, donde se establecía un nodo primario que concentraba todas las colas y tópicos. En este esquema, **los clientes solo podían conectarse a este nodo primario**, lo cual creaba un punto único de acceso y, potencialmente, un cuello de botella o punto único de fallo.
3. ![image](assets/cm8zlaxr1002c356ybb3zem65-step3-INSD_PRDT_U5_Apartado4-1_Imagen18.jpg)
   Además, en este enfoque clásico:

   - **Los brokers se repartían los tópicos de manera fija**, sin posibilidad de compartir la carga de manera eficiente.
   - **Cada cliente debía conectarse exclusivamente al broker que contenía su tópico de interés**, lo que dificultaba la flexibilidad del sistema.
   - **La arquitectura no permitía escalar horizontalmente,** es decir, no se podía añadir más brokers de forma sencilla para aumentar la capacidad de procesamiento o tolerancia a fallos.
4. ![image](assets/cm8zlaxr1002c356ybb3zem65-step4-INSD_PRDT_U5_Apartado4-1_Imagen19.jpg)
   Estas limitaciones marcaron el punto de partida para la evolución hacia plataformas más modernas como Apache Kafka, diseñadas específicamente para superar estas barreras.
5. ![image](assets/cm8zlaxr1002c356ybb3zem65-step5-INSD_PRDT_U5_Apartado4-1_Imagen20.jpg)
   Kafka introduce una arquitectura más flexible y resiliente:

   - Los **tópicos se dividen en particiones**, que a su vez pueden distribuirse entre diferentes brokers.
   - Kafka **replica automáticamente** los datos entre brokers para tolerancia a fallos.
   - Soporta tanto **escalado horizontal** (más brokers) como **escalado vertical** (más capacidad por nodo).
   - A diferencia de los sistemas tradicionales, **los mensajes no se eliminan tras ser consumidos**, sino que se almacenan durante un período configurado, permitiendo a múltiples consumidores acceder a ellos en distintos momentos.



### 3.2 Arquitectura



Recordemos que Apache Kafka es una plataforma distribuida diseñada para construir pipelines de datos y aplicaciones de streaming de alta disponibilidad y rendimiento. Actúa como un buffer centralizado para la ingesta y procesamiento de flujos de datos en tiempo real. Fue creado por LinkedIn y liberado como proyecto open source en 2011. Posteriormente, sus creadores fundaron la empresa **Confluent** en 2014, impulsando su adopción a gran escala.

Uno de los componentes principales de Kafka es el **broker**, un servidor que actúa como intermediario entre los **productores** (quienes publican los eventos) y los **consumidores** (quienes los procesan). Los brokers almacenan temporalmente los mensajes recibidos y los enrutan hacia los consumidores, manteniéndolos disponibles incluso si el consumidor no los procesa inmediatamente. Esta persistencia de los datos resuelve uno de los problemas típicos de los sistemas de streaming: el **backpressure**, es decir, la sobrecarga que ocurre cuando el ritmo de consumo no alcanza al ritmo de producción. Kafka actúa como un búfer duradero que desacopla ambos extremos, permitiendo que los datos sean procesados con flexibilidad.



![image](assets/cm8zlgi8d009d356ylppdggia-INSD_PRDT_U5_Apartado4-2_Imagen21.jpg)



El modelo de Kafka está basado en el patrón **publish-subscribe**. Cada productor emite eventos a un canal lógico denominado **tópico**, y uno o varios consumidores se suscriben a dicho canal para procesar los datos. A diferencia de otros sistemas tradicionales, donde cada cliente está acoplado a un broker específico, Kafka permite que múltiples productores publiquen en un mismo tópico y múltiples consumidores lo lean en paralelo. Esta lógica habilita configuraciones como los **grupos de consumidores**, donde varios consumidores comparten el procesamiento de un tópico sin duplicar la carga, ya que cada mensaje es entregado a un único miembro del grupo.



![image](assets/cm8zlh73o00aq356ybmpzsjou-INSD_PRDT_U5_Apartado4-2_Imagen22.jpg)



#### El rol de los brokers



Un **broker** es un nodo que almacena mensajes de los tópicos y los entrega a los consumidores. Varios brokers se agrupan en un **cluster**, y cada uno puede contener réplicas de datos para garantizar disponibilidad.



![image](assets/cm8zlirw000ck356y1uz5h6is-INSD_PRDT_U5_Apartado4-2-1_Imagen23.jpg)



Este diseño distribuido asegura tolerancia a fallos, ya que si un broker falla, otro con su réplica puede asumir el control sin pérdida de datos.



#### Coordinación con Zookeeper



Kafka utiliza **Apache Zookeeper** para coordinar los brokers, gestionar la configuración y realizar tareas como la elección de líderes o sincronización distribuida. Zookeeper permite a productores y consumidores saber a qué broker deben conectarse.



![image](assets/cm8zlkcsi00f5356y8vgqfqb1-INSD_PRDT_U5_Apartado4-2-2_Imagen24.jpg)



Apache ZooKeeper es un sistema open source diseñado para la **coordinación de aplicaciones distribuidas**. Su función principal es proporcionar un mecanismo centralizado y confiable que permite a los distintos componentes de un sistema distribuido mantenerse sincronizados y actualizados en tiempo real. En entornos donde múltiples servicios interactúan simultáneamente, ZooKeeper actúa como una columna vertebral que garantiza la consistencia y la organización entre ellos.

Entre sus principales **casos de uso**, se encuentran:



- **Gestión de configuración**  
  La **gestión de configuración**, permitiendo que los nodos del sistema compartan y accedan a la misma información de forma coherente.
- **Sincronización distribuida**  
  La **sincronización distribuida**, clave para evitar conflictos y asegurar que los procesos actúen de manera ordenada.
- **Elección de líderes**  
  La **elección de líderes**, esencial en arquitecturas donde se requiere definir nodos coordinadores o maestros entre varios participantes.
- **Soporte para funcionalidades tipo DNS**  
  El soporte para funcionalidades tipo **DNS**, facilitando la localización dinámica de servicios dentro de un clúster.
- **Registro de datos centralizado**  
  Y el **registro de datos centralizado**, que permite mantener un repositorio común de metadatos críticos para el funcionamiento del sistema.



En Apache ZooKeeper, los **znodes** son los nodos de su estructura jerárquica de datos, muy similar a un sistema de archivos. Cada znode puede contener datos y tener hijos, lo que permite organizar la información en una estructura tipo árbol. La imagen muestra un ejemplo de esta jerarquía, donde el nodo raíz (/) contiene subnodos como /app1 y /app2, y a su vez /app1 tiene hijos como /app1/p_1, /app1/p_2 y /app1/p_3. Esta organización facilita la coordinación y el seguimiento del estado de los componentes distribuidos, permitiendo, por ejemplo, registrar la presencia de nodos activos o almacenar configuraciones compartidas.



![image](assets/cm8zlofqg00i9356ya83tuxja-INSD_PRDT_U5_Apartado4-2-2_Imagen25.jpg)



#### Gestión de consumo en Kafka: Offset y Consumer Groups



Las siguientes imágenes ilustran dos conceptos fundamentales en la arquitectura de consumo de Kafka:



1. ![image](assets/cm8zlq14i00k3356ym6hr6bs7-step1-INSD_PRDT_U5_Apartado4-2-3_Imagen26.jpg)
   Cada mensaje publicado en un tópico se guarda de forma persistente durante un periodo configurable (normalmente entre 2 y 7 días). Los consumidores pueden acceder a estos mensajes a través del *offset* (*desplazamiento*), que indica la posición específica de lectura dentro del tópico. Un consumidor puede comenzar desde el primer mensaje (OFFSET=0) o desde el mensaje más reciente si no se especifica offset. Se puede acceder a cualquier evento a través del offset (desplazamiento)
2. ![image](assets/cm8zlq14i00k3356ym6hr6bs7-step2-INSD_PRDT_U5_Apartado4-2-3_Imagen27.jpg)
   Muestra cómo múltiples consumidores pueden compartir la carga de lectura de un mismo tópico formando un *consumer group*. En este modelo, cada mensaje se distribuye a un único consumidor dentro del grupo, asegurando que no se dupliquen los mensajes entre ellos. Esto permite escalar horizontalmente el procesamiento de eventos de manera eficiente.

   - A la izquierda, el **tópico** contiene una secuencia ordenada de mensajes (Mensaje1 a Mensaje6).
   - A la derecha, hay un **consumer group** con dos consumidores: *Consumidor1* y *Consumidor2*.
   - Flechas naranjas: indican los mensajes que están siendo leídos por Consumidor1.
   - Flechas azules: indican los mensajes que están siendo leídos por Consumidor2

   Cada consumidor dentro del grupo recibe un subconjunto exclusivo de mensajes del tópico. Es decir, **los mensajes no se duplican entre consumidores del mismo grupo**, lo que permite **balancear la carga de procesamiento** de forma eficiente. Por ejemplo:

   - *Consumidor1* está procesando Mensaje1, Mensaje3 y Mensaje5.
   - *Consumidor2* está procesando Mensaje2 , Mensaje4 y Mensaje6.

   Este patrón es clave para escalar horizontalmente el consumo de datos sin perder eficiencia.



### 3.3 Conceptos necesarios en Kafka



La siguiente imagen muestra un esquema general del flujo de datos en un sistema distribuido con Kafka, donde múltiples productores y consumidores interactúan a través de un clúster compuesto por tópicos y particiones.



![image](assets/cm8zlv57u00ui356yptj54tku-INSD_PRDT_U5_Apartado4-3_Imagen28.png)



#### Broker, Topics, Partitions y Records



Un **broker** en Apache Kafka es un servidor que recibe, almacena y distribuye mensajes. Actúa como intermediario entre los productores (que envían datos) y los consumidores (que los leen), gestionando los tópicos, particiones y réplicas, y asegurando el flujo eficiente y fiable de los eventos dentro del clúster.

En el contexto de Kafka, un **tópico** es el canal lógico al que se publican los mensajes. Representa un flujo categorizado de datos, similar a una etiqueta o nombre de destino que permite organizar la información producida por los emisores (productores). Los tópicos pueden tener ningún consumidor, uno o múltiples consumidores, lo cual permite distintos patrones de consumo como la difusión o la distribución balanceada de mensajes.

Cada tópico se divide en **particiones**, que son unidades físicas donde se almacenan los mensajes. Estas particiones permiten el procesamiento paralelo y la escalabilidad horizontal del sistema.

La imagen muestra gráficamente cómo un tópico se fragmenta en tres particiones (Partition 0, Partition 1 y Partition 2), cada una representando una secuencia ordenada de mensajes indexados (offsets). Las flechas indican que nuevos mensajes se van escribiendo al final de cada partición, manteniendo el orden dentro de cada una. Este diseño permite una escritura eficiente y un acceso ordenado a los datos para los consumidores.



![image](assets/cm8zlxjul00wc356y6ovqpttw-INSD_PRDT_U5_Apartado4-3-1_Imagen29.png)



En Kafka, una partición es una **unidad lógica de almacenamiento y procesamiento** dentro de un tópico. Cada partición actúa como una **secuencia ordenada e inmutable de registros**, donde los datos se escriben en modo *append-only*, es decir, se añaden al final de forma secuencial sin sobrescribir los anteriores. Esta organización lineal permite que cada mensaje tenga un identificador único llamado **offset**, que indica su posición dentro de la partición.

Gracias a esta estructura, las particiones se convierten en una **unidad de paralelismo y escalabilidad**: múltiples productores pueden escribir en distintas particiones de un mismo tópico, y múltiples consumidores pueden leerlas en paralelo. Además, **las particiones pueden replicarse** entre distintos brokers para asegurar la disponibilidad y la tolerancia a fallos.

La siguiente imagen representa una partición con una secuencia de mensajes identificados por su offset (del 0 al 12). Vemos cómo los productores escriben al final de la cola (offset 12), mientras los consumidores A y B leen en distintos puntos: el consumidor A está en el offset 9, mientras que el B ya ha avanzado al 11. Esto ilustra cómo cada consumidor puede avanzar de manera independiente según su ritmo de procesamiento, y cómo Kafka permite acceder a cualquier mensaje aún si ha pasado tiempo desde su publicación.



![image](assets/cm8zlyjbf00xp356ygzhs0v28-INSD_PRDT_U5_Apartado4-3-1_Imagen30.png)



Los *records* o registros en Kafka son las unidades básicas de datos que circulan a través del sistema. Cada uno se identifica de manera única mediante un triplete compuesto por el *tópico*, la *partición* y el *offset*. Los registros se estructuran como pares clave/valor, lo que permite que todos los mensajes con la misma clave se envíen consistentemente a la misma partición, facilitando así la semántica de orden. Estos mensajes se almacenan en disco independientemente de si han sido consumidos o no, y permanecen allí hasta que se cumple la política de retención configurada (*retention policy*).

La imagen muestra cómo se organizan los *records* en una partición como una secuencia de bloques numerados. A la derecha, se ve el punto de escritura (*Next Write*), que marca dónde se añadirá el siguiente registro. A lo largo del log, se indican también el *Cleaner Point* (momento a partir del cual los registros pueden ser compactados) y el *Delete Retention Point*, que señala el límite en el que los registros anteriores pueden ser eliminados según la política de retención.

- **Log Tail** = registros más antiguos, susceptibles de ser eliminados.
- **Log Head** = registros más recientes, aún activos y en uso.



![image](assets/cm8zm0ac000z2356yu951ukyg-INSD_PRDT_U5_Apartado4-3-1_Imagen31.png)



En Apache Kafka, **las particiones y réplicas** son pilares esenciales para garantizar el rendimiento, la disponibilidad y la tolerancia a fallos. Cada *tópico* puede dividirse en varias particiones, que son unidades independientes de almacenamiento y procesamiento de mensajes. Para mejorar la resiliencia, Kafka permite definir un *factor de replicación*, creando copias idénticas de cada partición distribuidas entre distintos *brokers*. Uno de estos brokers actúa como *líder*, mientras los demás mantienen réplicas sincronizadas. Esta arquitectura permite que, si un broker falla, otro con una réplica pueda asumir el liderazgo sin pérdida de datos ni interrupciones en el servicio.

El siguiente diagrama representa un tópico dividido en cuatro particiones (0, 1, 2, 3), con la partición 1 replicada en tres brokers distintos (broker 2, 3 y 5). Cada réplica tiene un identificador (por ejemplo, 1 [repl 2]), y Kafka se encarga de elegir un *líder* para cada partición entre las réplicas disponibles. Esto ilustra visualmente cómo Kafka distribuye y protege los datos mediante su sistema de replicación.



![image](assets/cm8zm25nq010f356yogtbn85b-INSD_PRDT_U5_Apartado4-3-1_Imagen32.jpg)



#### Modelos de consumición



- **Modelo de consumición: 1 partición, 1 consumidor (modo cola)**  
  En este modelo de consumo, una única partición de Kafka está siendo consumida por un único consumidor, lo que emula el comportamiento clásico de una cola. Los mensajes se almacenan secuencialmente y son procesados uno a uno por ese consumidor. La posición del consumidor dentro de la partición está determinada por el *offset*, que es gestionado por el propio consumidor. Es importante destacar que el broker no tiene conocimiento del avance del consumidor, ya que este mantiene su propio seguimiento de los mensajes leídos, como se representa en la imagen con el offset = 8. Esto permite al consumidor reanudar la lectura desde el punto exacto en caso de fallo o reinicio.
- **Modelo de consumición: 1 partición, múltiples consumidores (Pub/Sub)**  
  En este modelo de tipo *publish/subscribe*, varios consumidores se suscriben a la misma partición de un tópico. Cada uno mantiene su propio offset, por lo que todos reciben los mismos mensajes de forma independiente. Esto permite múltiples lecturas paralelas del mismo flujo de datos sin interferencia entre consumidores. La imagen ilustra cómo tres consumidores (C₁, C₂ y C₃) acceden simultáneamente a los mismos mensajes de la partición, cada uno desde un punto distinto del log.
- **Modelo de consumición: N particiones, 1 consumidor**  
  En este caso, un único consumidor se encarga de leer mensajes provenientes de múltiples particiones de un tópico. Este enfoque centraliza la carga de trabajo en un solo nodo, que debe gestionar múltiples flujos de datos, lo cual puede limitar la escalabilidad pero simplifica la arquitectura cuando el volumen de datos es manejable. La eficiencia depende de la capacidad del consumidor para procesar todos los mensajes a tiempo.
- **Modelo de consumición: N particiones, N consumidores**  
  En este modelo de consumición, múltiples particiones se distribuyen entre un número equivalente de consumidores. Esto permite procesar los datos en paralelo, maximizando el rendimiento. Cada consumidor mantiene su propio offset y se encarga de leer los mensajes de una partición específica. La imagen muestra cómo un productor distribuye eventos en distintas particiones (gestionadas por distintos brokers), y cómo cada consumidor accede de forma independiente a su partición asignada, permitiendo un consumo eficiente y escalable.
- **Consumer Groups: N particiones, 1 grupo de consumidores**  
  En este modelo de consumo, varios consumidores forman parte de un mismo consumer group, lo que permite distribuir el procesamiento de múltiples particiones entre ellos. Cada consumidor del grupo se encarga de leer exclusivamente una o varias particiones, asegurando que los mensajes no se dupliquen dentro del grupo. Esto garantiza un procesamiento eficiente y balanceado, ideal para aplicaciones que requieren escalabilidad.
  En la imagen, el grupo "group1" está compuesto por los consumidores C₁ y C₂, que consumen particiones diferentes del mismo topic gestionadas por distintos brokers, manteniendo un offset propio por partición.
- **Consumer Groups: N particiones, 2 grupos de consumidores**  
  En este modelo de consumición, se tienen múltiples particiones distribuidas entre dos grupos de consumidores distintos. Cada grupo consume los mensajes de manera independiente, lo que implica que un mismo mensaje puede ser procesado por ambos grupos. Por ejemplo, en la imagen se observa cómo los consumidores del group1 y del group2 leen los datos desde las mismas particiones pero de forma separada, lo cual permite múltiples formas de procesamiento en paralelo según el propósito de cada grupo. Esta arquitectura es especialmente útil cuando diferentes aplicaciones necesitan acceder a la misma información de forma desacoplada.
- **Consumer Groups: N particiones, 1 grupo y varios consumidores**  
  En este modelo de consumo, tenemos una única partición que es leída por varios consumidores dentro de un mismo grupo de consumidores. Sin embargo, en Kafka, cada partición solo puede ser asignada a un consumidor dentro de un grupo, por lo que aunque haya múltiples consumidores disponibles, solo uno de ellos estará efectivamente recibiendo los datos de esa partición. Este esquema asegura que los mensajes no se dupliquen entre consumidores del mismo grupo, garantizando procesamiento exclusivo por consumidor.
   La imagen muestra cómo tres consumidores (C₁, C₂ y C₃) comparten un grupo, pero solo uno (en este caso C₂) consume los mensajes de la partición.



#### Mensajería Tradicional vs. Mensajería en Kafka



A diferencia de los sistemas de mensajería tradicionales, que garantizan el orden de entrega de los mensajes a los consumidores, Apache Kafka se enfoca en preservar el orden de procesamiento dentro de una misma partición. Esto implica que todos los registros enviados a una partición específica serán consumidos en el mismo orden en que fueron producidos. Sin embargo, si existen múltiples particiones y consumidores, el orden global entre ellas no está garantizado. En la imagen, se muestra cómo un sistema tradicional centraliza la entrega a través de un único broker, mientras que Kafka distribuye los mensajes en múltiples particiones (P1, P2), cada una con su propio orden interno y consumidor asignado.



![image](assets/cm8zmcavk0143356y099lh55g-INSD_PRDT_U5_Apartado4-3-3_Imagen40.jpg)



#### Gestión y optimización del almacenamiento en Kafka



Kafka replica datos a nivel de partición mediante un líder que gestiona lecturas y escrituras, mientras las réplicas sincronizadas (‘in-sync replicas’) actúan únicamente como respaldo, sin afectar al rendimiento del sistema (No aumento de throughput, solo backup).



![image](assets/cm8zmdhez015x356y8o1o814u-INSD_PRDT_U5_Apartado4-3-4_Imagen41.jpg)



**Kafka garantiza no perder datos,** asegurando que **al menos una réplica sincronizada esté disponible** antes de confirmar un mensaje. Por tanto, Kafka garantiza disponibilidad y tolerancia a particiones, sacrificando la consistencia estricta para no perder datos, si recordamos el Teorema del CAP:



![image](assets/cm8zmi8gu017j356y5ew7vchl-INSD_PRDT_U5_Apartado4-3-4_Imagen42.jpg)



Respecto a la persistencia, la siguiente imagen ilustra el proceso mediante el cual Kafka **elimina entradas obsoletas del log** manteniendo únicamente el **valor más reciente para cada clave**. Este mecanismo es especialmente útil cuando los mensajes representan el estado actual de una entidad identificada por una clave (por ejemplo, el perfil de un usuario o el estado de un pedido).



![image](assets/cm8zmj2ak0195356yvsw0ygcf-INSD_PRDT_U5_Apartado4-3-4_Imagen43.jpg)



En la imagen, la parte superior muestra el log antes de la compactación, donde múltiples valores (V1, V3, V6, etc.) están asociados a la misma clave (K1, K2, K5, etc.) en diferentes offsets. Tras aplicar la compactación, en la parte inferior solo se conservan las **últimas versiones** de cada clave (por ejemplo, K1→V4, K2→V10), lo que **reduce el espacio ocupado y mejora la eficiencia de recuperación del estado**.

Este proceso no depende de si un mensaje ha sido consumido o no, y contrasta con la política de retención por tiempo o tamaño, ya que permite a Kafka actuar como una **base de datos de tipo key-value persistente**.

Respecto a **la tolerancia a fallos** en Kafka se basa en el quorum de Zookeeper —es decir, la mayoría de nodos activos (mitad + 1) necesarios para tomar decisiones y seguir operando— y en la configuración específica de cada tópico. Esta configuración define cuántas **réplicas** existen y cómo se distribuyen entre los brokers, lo que permite a Kafka continuar funcionando incluso si uno o varios nodos fallan, siempre que haya suficientes réplicas sincronizadas disponibles.

Finalmente respecto a la escalabilidad comentar que Kafka **soporta tanto la escalabilidad vertical como horizontal**.



- **Escalabilidad vertical**  
  Consiste en ampliar los recursos de un único nodo. Por ejemplo, al incrementar la capacidad de almacenamiento (más disco), es posible aumentar el tamaño de las particiones.
- **Escalabilidad horizontal**  
  Puede lograrse de dos maneras. Por un lado, **añadiendo más brokers,** lo que permite distribuir la carga y manejar un mayor número de particiones (aunque requiere una operación manual). Por otro, **incrementando el número de particiones,** lo cual facilita un mayor paralelismo y, por tanto, **aumenta el throughput de consumo.**



### 3.4 Ecosistema confluente Platform



El **ecosistema de Confluent Platform**, es una solución completa construida sobre Apache Kafka que extiende sus capacidades para entornos empresariales. En el centro se encuentra Kafka como núcleo de procesamiento de eventos en tiempo real, complementado por módulos para seguridad, escalabilidad, monitorización y desarrollo. A su alrededor, se integran múltiples fuentes de datos (como bases de datos, CRMs o sistemas Hadoop) y aplicaciones en tiempo real (como analítica, detección de fraude o gestión de inventario), permitiendo construir pipelines de datos robustos, distribuidos y en streaming. Esta arquitectura puede desplegarse tanto en local como en la nube gestionada de Confluent.



![image](assets/cm8zmtiyg01c3356ydt2tvqcr-INSD_PRDT_U5_Apartado4-4_Imagen44.jpg)



### 3.5 Schema Registry



El **Schema Registry** es un componente fundamental del ecosistema de Kafka que permite gestionar de forma centralizada los esquemas de los datos, especialmente cuando se utiliza el formato **Avro**. Su principal función es asegurar que los mensajes intercambiados entre productores y consumidores mantengan una estructura coherente, validando y versionando los esquemas para evitar errores de incompatibilidad y facilitar la evolución del sistema.

En entornos distribuidos, donde múltiples aplicaciones producen y consumen datos, es común encontrar incompatibilidades estructurales entre los mensajes. La imagen ilustra cómo diferentes aplicaciones generan datos con formatos distintos, lo que puede romper los consumidores si no se controla la estructura de los mensajes. Aquí entra en juego el Schema Registry, que actúa como intermediario para validar y unificar los esquemas utilizados, asegurando la compatibilidad entre productores y consumidores.



![image](assets/cm8zmunvt01dh356yva8s0t39-INSD_PRDT_U5_Apartado4-5_Imagen45.jpg)



Un **esquema Avro** es una definición estructurada del formato de los datos que se van a enviar o recibir en un sistema, normalmente en Kafka, utilizando el formato **Avro.** Un esquema Avro describe los campos, tipos de datos y estructura general de un mensaje. Está escrito en JSON y permite saber exactamente qué esperar de un mensaje (por ejemplo, qué campos tiene, de qué tipo son, si son obligatorios, etc.).

Ejemplo:



```json
{
  "type": "record",
  "name": "User",
  "fields": [
    { "name": "id", "type": "string" },
    { "name": "age", "type": "int" }
  ]
}
```



**¿Diferencia entre Avro y Json?**

| Característica | JSON | Avro |
| --- | --- | --- |
| Formato | Texto legible para humanos | Binario (compacto y eficiente) |
| Esquema embebido | No lo tiene | No lo incluye en el mensaje (opcional) |
| Separación de esquema y datos | NO. todo está en el mismo archivo | SÍ. los datos se serializan y el esquema se gestiona por separado en un Schema Registry ) |
| Eficiencia | Menos eficiente en espacio y velocidad | Más rápido y compacto |
| Validación de datos | No estricta: cada mensaje puede variar | Sí: todos los mensajes deben cumplir el esquema |
| Evolución del esquema | No soportada formalmente | Soportada (puedes añadir campos sin romper nada) |
| Uso típico | APIs REST, archivos simples | Kafka, Hadoop, sistemas de alto rendimiento |

**¿Por qué usar Avro en Kafka?**

- Avro **no guarda el esquema en cada mensaje**, lo que ahorra espacio.
- Usa **serialización binaria**, mucho más eficiente en entornos de big data o transmisión de eventos.
- Con **Schema Registry**, puedes versionar y validar los datos automáticamente entre productor y consumidor.

Schema Registry almacena esquemas Avro que definen la estructura de los datos. Estos esquemas pueden usarse tanto para las claves como para los valores de los mensajes y están asociados a tópicos concretos en Kafka. Aunque las aplicaciones pueden registrar sus propios esquemas, en entornos productivos es recomendable centralizar este control para evitar inconsistencias. Una de sus mayores ventajas es que permite la evolución segura de los esquemas, garantizando que cualquier cambio respete el contrato entre productor y consumidor, es decir, que los datos sigan siendo comprensibles sin errores.

Una de las capacidades clave de Schema Registry es permitir la evolución de esquemas de forma controlada. En la imagen se observa una versión inicial (V1) de un esquema con dos campos (id y amount) y una versión posterior (V2) que añade un nuevo campo (region) con un valor por defecto. Gracias a esta compatibilidad hacia atrás, los consumidores que aún utilizan el esquema anterior pueden seguir procesando los datos sin errores. Esta gestión de versiones evita roturas y permite adaptar los datos a nuevas necesidades de negocio sin afectar la estabilidad del sistema.



![image](assets/cm8zmxjd401g2356ypbe6ibd1-INSD_PRDT_U5_Apartado4-5_Imagen46.png)



### 3.6 Interfaces y herramientas de integración en Kafka



Kafka no solo proporciona una infraestructura robusta para el procesamiento de datos en tiempo real, sino también un conjunto de herramientas que amplían su usabilidad y facilitan su integración con diferentes tecnologías. Entre ellas se encuentran REST Proxy, Connect, Streams y ksqlDB, que permiten interactuar con Kafka sin necesidad de escribir código Java, integrar sistemas externos, procesar flujos de datos de forma declarativa o programática, y realizar consultas SQL sobre los datos en movimiento. Estas herramientas forman el ecosistema funcional que hace de Kafka una plataforma completa para arquitecturas orientadas a eventos.



#### Rest Proxy



REST Proxy actúa como una puerta de enlace HTTP para interactuar con Kafka, facilitando la comunicación desde aplicaciones que no están escritas en Java. A través de una interfaz RESTful, permite producir y consumir mensajes, incluyendo el soporte a grupos de consumidores, y consultar metadatos del clúster. Si bien simplifica notablemente la integración y operaciones básicas, aún no permite la ejecución de tareas administrativas completas. La imagen ilustra cómo este componente se sitúa entre aplicaciones externas y el ecosistema Kafka, destacando su rol como facilitador de acceso y simplificación de tareas clave.



![image](assets/cm8zmznqo01io356yitudc3kq-INSD_PRDT_U5_Apartado4-6-1_Imagen47.jpg)



#### Connects



Kafka Connect es un componente del ecosistema de Kafka diseñado para facilitar la integración con sistemas externos de forma sencilla, escalable y tolerante a fallos. Actúa como un **framework** que permite transferir datos desde sistemas fuente hacia Kafka (source connectors) o desde Kafka hacia sistemas destino (sink connectors), ya sea en flujos en tiempo real (streaming) o por lotes (batch).

Esta ilustración esquemática muestra cómo Kafka Connect actúa como puente entre las fuentes de datos (Data Source), Kafka y los destinos (Data Sink), utilizando conectores de entrada y salida.



![image](assets/cm8zn0ski01ki356ycpo239m1-INSD_PRDT_U5_Apartado4-6-2_Imagen48.jpg)



Un **Data Sink** (o sumidero de datos) es cualquier sistema o componente que **recibe y almacena datos** provenientes de otro sistema. En el contexto de **Kafka Connect**, un *sink* es el destino final al que se envían los datos que han sido previamente recogidos o generados, por ejemplo, desde una base de datos o una aplicación.

Kafka Connect puede utilizar configuraciones basadas en ventanas por número de eventos para gestionar la forma en que los datos son agrupados antes de ser procesados o enviados a destino. Esto es útil, por ejemplo, al mover datos de un sistema como SQL Server hacia un sistema de almacenamiento como HDFS, controlando el tamaño de los lotes de eventos.

La siguiente imagen representa un flujo de datos de SQL Server a HDFS pasando por Kafka, con segmentación por número de eventos.



![image](assets/cm8zn1mxg01lv356yjvu9dd5h-Imagen3.jpg)



#### Conectores y arquitectura de despliegue



#### Streams



Kafka Streams es una librería de procesamiento de flujos (stream processing) que permite construir aplicaciones y microservicios que consumen datos directamente desde tópicos de Kafka, los procesan en tiempo real y escriben los resultados de nuevo en Kafka. Está diseñada para trabajar sobre la infraestructura de Kafka, aprovechando su escalabilidad, tolerancia a fallos y baja latencia.

Kafka Streams se ejecuta directamente como parte del código de la aplicación, permitiendo integrarse fácilmente con sistemas existentes.



![image](assets/cm8zn4r5k01og356yayqgihuw-Imagen4.jpg)



- **ETLs en tiempo real con Kafka Streams**  
  Kafka Streams permite implementar pipelines de transformación (ETLs) directamente entre tópicos de Kafka. Estas transformaciones pueden incluir filtrado, agregaciones, mapeos o cualquier otra operación de lógica de negocio sobre los datos en tiempo real.

  Kafka Streams permite transformar datos aplicando ventanas temporales o por número de eventos, como por ejemplo la suma de ventas por minuto.
- **Ventajas y desventajas**  
  Kafka Streams se posiciona como una alternativa ligera y sencilla frente a otras soluciones de procesamiento en streaming, como Spark Streaming, Flink o Storm.

  - **Ventaja principal**: Es una **librería** que se puede incluir en cualquier aplicación Java o Scala, sin necesidad de desplegar clústeres adicionales.
  - **Desventaja**: Está limitada a Kafka como única fuente y destino de datos. No puede leer ni escribir directamente desde otras plataformas de datos sin integraciones adicionales.
- **Características destacadas**  
  Kafka Streams ofrece un conjunto completo de funcionalidades para el procesamiento distribuido y tolerante a fallos:

  - Procesamiento de eventos uno a uno con latencias de milisegundos
  - Soporte para operaciones con estado como agregaciones, joins y ventanas
  - Capacidad de reprocesado
  - Tolerancia a fallos y despliegues sin downtime
  - API con dos niveles de abstracción: una sencilla y otra más potente. la **API de dos niveles** significa que ofrece:
    - **API de alto nivel**: más sencilla, declarativa y fácil de usar para operaciones comunes como filtros, mapeos o agregaciones.
    - **API de bajo nivel (Processor API)**: más flexible y potente, permite controlar el flujo y lógica personalizada a nivel de nodo del grafo de procesamiento.



#### KSQL



**KSQL** es un componente que permite realizar transformaciones y análisis sobre flujos de datos en Kafka utilizando una sintaxis SQL-like. Es decir, ofrece las mismas funcionalidades que **Kafka Streams**, pero orientado a usuarios que prefieren trabajar con un lenguaje declarativo similar a SQL, en lugar de escribir código Java o Scala.



![image](assets/cm8zn9mcd01r2356ygjxocoud-INSD_PRDT_U5_Apartado4-6-4_Imagen52.jpg)



Esta imagen ilustra cómo KSQL se integra con un clúster de Kafka a través de su propio servidor, ofreciendo dos interfaces: una CLI y una interfaz gráfica (UI). El servidor ejecuta las consultas sobre los datos que fluyen en tiempo real.

KSQL permite definir consultas como CREATE STREAM para transformar o filtrar eventos de un topic de origen y producir los resultados en un nuevo topic de destino. Es decir, Con KSQL se pueden construir flujos complejos usando sentencias SQL como si se consultara una base de datos, pero en tiempo real.



![image](assets/cm8znabtw01sf356yc76iydts-INSD_PRDT_U5_Apartado4-6-4_Imagen53.jpg)



La siguiente imagen muestra un ejemplo completo de cómo detectar pagos fraudulentos aplicando un filtro sobre un topic de pagos. Se comparan la definición con sentencias KSQL (CREATE STREAM ...) y la versión equivalente en Kafka Streams.



![image](assets/cm8znb30t01ts356yuayi9nk5-INSD_PRDT_U5_Apartado4-6-4_Imagen54.jpg)



### 3.7 Ejercicios



En este apartado vamos a comenzar con un primer ejercicio que va a servir para familiarizarnos con comandos Kafka.

Básicamente ejecutaremos los siguientes comandos:



```bash
cd /home/bigdata/confluent-7.5.1/bin

confluent local services kafka start
confluent local services kafka-rest start

PARTITIONS

bin/kafka-topics --create --topic mi_tema --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
bin/kafka-topics --list --bootstrap-server localhost:9092
bin/kafka-topics --delete --topic mi_tema --bootstrap-server localhost:9092
bin/kafka-topics --list --bootstrap-server localhost:9092
bin/kafka-topics --create --topic mi_tema --bootstrap-server localhost:9092 --partitions 2 --replication-factor 2
bin/kafka-topics --create --topic mi_tema --bootstrap-server localhost:9092 --partitions 2 --replication-factor 1
bin/confluent kafka topic update mi_tema --url http://localhost:8082 --config retention.ms=259200000
bin/kafka-topics --describe --bootstrap-server localhost:9092 --topic mi_tema
bin/kafka-console-producer --bootstrap-server localhost:9092 --topic mi_tema
// Introducir algunos líneas

// Abrir otro terminal para el consumidor
bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mi_tema --from-beginning 
bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mi_tema
// wget https://gist.githubusercontent.com/mafernandez-stratio/1650f124899e0ab7a91851d95fc3bf82/raw/7a425e9dd4e7330954363cf10afe25429ecd3ec9/microcuento.txt
bin/kafka-console-producer --bootstrap-server localhost:9092 --topic mi_tema < /home/bigdata/microcuento.txt
bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mi_tema --from-beginning > /home/bigdata/salida.txt

CONSUMER GROUPS

bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mi_tema --group mi_grupo
bin/kafka-consumer-groups --bootstrap-server localhost:9092 --list
bin/kafka-consumer-groups --bootstrap-server localhost:9092 --group mi_grupo --describe
bin/kafka-console-producer --bootstrap-server localhost:9092 --topic mi_tema --property parse.key=true --property key.separator=":"
// Introduce algunos datos (Ejemplo --> Asignatura1:Procesamiento de Datos)
bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mi_tema --from-beginning --property print.key=true --property key.separator="-"

DATAGEN

cat /home/bigdata/confluent-7.5.1/console-consumer-primitive-keys-values/primitives.json
bin/ksql-datagen schema=/home/bigdata/confluent-7.5.1/console-consumer-primitive-keys-values/primitives.json key-format=json value-format=json topic=mi_tema key=key_field iterations=10
bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mi_tema --property print.key=true --property key.separator="-"

OFFSET

bin/kafka-consumer-groups --bootstrap-server localhost:9092 --group mi_grupo --describe
bin/ksql-datagen quickstart=orders iterations=10 topic=mi_tema key=orderid key-format=delimited
bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mi_tema --partition 0 --offset ???
bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mi_tema --partition 1 --offset ???
bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mi_tema --group mi_grupo
```



Es recomendable visitar los siguientes enlaces para obtener información más detallada:



> **Link 1**
>
> [Link](https://www.confluent.io/blog/easy-ways-generate-test-data-kafka/)

> **Link 2**
>
> [Link](https://developer.confluent.io/tutorials/generate-streams-of-test-data/kafka.html)

> **Link 3**
>
> [Link](https://developer.confluent.io/courses/apache-kafka/get-started-hands-on/)



En el siguiente video se puede ver la ejecución y explicación de los primeros comandos hasta la creación del topic:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652194_1/scormcontent/assets/INSD_PRDT_U5_Apartado4-7_Video4Ejercicio1Kafka1.mp4?v=1)



A continuación se muestra el siguiente video en el cual ya enviaremos mensajes:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652194_1/scormcontent/assets/INSD_PRDT_U5_Apartado4-7_Video5Ejercicio1Kafka2.mp4.mp4?v=1)



A partir de este punto se recomienda a los alumnos seguir con el ejemplo, concretamente con los apartados de Consumer Groups, Datagen y Offset.

Aunque no se coenta en los videos es importante saber que si queremos parar tanto el consumidor como el productor una vez se hayan arrancado podemos pulsar CTRL + C y terminamos el proceso. Si se quedase colgado buscamos su PID con **ps aux | grep kafka-console-producer** y posteriormente matamos el proceso con **kill -9 <PID>**



## 4. Structured Streaming



### 4.1 Introducción



![image](assets/cm8znkv4u0211356ycakacca0-stock-image.jpg)



**Spark Structured Streaming** es un motor escalable y tolerante a fallos para el procesamiento de flujos de datos en tiempo real. Está construido sobre el motor de **Spark SQL**, lo que permite aplicar la misma lógica y API que se usa para el procesamiento por lotes (batch), simplificando enormemente el desarrollo.

La idea central es tratar un flujo de datos como una **tabla que se va extendiendo continuamente**. En lugar de redefinir un modelo de procesamiento exclusivo para streaming, Spark permite escribir una consulta sobre datos estáticos y la ejecuta incrementalmente sobre datos en streaming, lo que hace el desarrollo mucho más intuitivo y natural.

Gracias a la **API de DataFrame**, es posible realizar operaciones avanzadas como agregaciones, ventanas de tiempo, y uniones entre flujos o entre flujos y datos estáticos, con la misma sintaxis que ya se utiliza en batch. Esta unificación facilita la reutilización de código y el aprendizaje.

Además, Structured Streaming **garantiza tolerancia a fallos de extremo a extremo**, gracias al uso de **checkpoints** y registros de logs, lo que permite lograr **exactly-once semantics** (los datos se procesan una única vez, incluso ante fallos).

Por defecto, Spark procesa los datos como una serie de **micro-batches**, con latencias del orden de **100 milisegundos**, permitiendo un equilibrio entre rendimiento y consistencia.

En resumen, la idea es desarrollar una query en Batch sobre datos estáticos y Spark ejecutará esa lógica incrementalmente sobre datos infinitos.

La siguiente ilustración muestra cómo Structured Streaming trata un flujo de datos como una tabla en crecimiento, aplicando consultas SQL-like de manera incremental y continua. Se visualiza el flujo continuo de datos que va alimentando una tabla de entrada (Input Table), sobre la que se aplica una lógica de transformación declarativa que actualiza progresivamente el resultado.



![image](assets/cm8znmggd022d356ygbrs24jm-INSD_PRDT_U5_Apartado5-1_Imagen55.jpg)



#### Actualización de resultados y modos de salida



![image](assets/cm8znqrd9023q356yznv5dqky-INSD_PRDT_U5_Apartado5-1_Imagen56.jpg)



En la práctica, no se materializa toda la tabla entera. El motor recibe los últimos datos de la fuente de Streaming, los procesa para actualizar el resultado y descarta los datos de origen Tan solo mantiene los datos mínimos del estado que son requeridos para actualizar el resultado



### 4.2 Event time



En el procesamiento de flujos de datos, distinguir entre el **momento en que ocurre un evento (event-time)** y el **momento en que se procesa (processing-time)** es fundamental para lograr análisis precisos. *Spark Structured Streaming* trabaja con un modelo basado en **event-time**, es decir, el tiempo real en que ocurrió el evento y no necesariamente cuándo llega al sistema.

Cada evento se representa como una fila con una columna de timestamp y puede ser asignado a **una o varias ventanas de tiempo**, lo que permite realizar agregaciones temporales (como ventas por minuto, promedio cada hora, etc.). Este modelo también admite la llegada tardía de datos gracias al almacenamiento temporal del estado intermedio. A través del mecanismo de **watermarks** (marcas de agua), el sistema puede limpiar estos estados antiguos tras un umbral configurable, equilibrando así precisión y eficiencia de recursos.

La siguiente imagen ilustra la diferencia entre *event-time* y *processing-time*. El evento ocurrió a las 08:12 (event-time), pero fue procesado a las 08:13 (processing-time), lo que demuestra cómo Spark puede seguir asignando eventos a sus ventanas correctas a pesar del retraso en la llegada



![image](assets/cm8znt0w9025v356yvwzw863g-INSD_PRDT_U5_Apartado5-2_Imagen57.jpg)



### 4.3 Fault tolerance en structured streaming



Uno de los pilares fundamentales de **Spark Structured Streaming** es su capacidad para ser tolerante a fallos. El motor supervisa continuamente el progreso del procesamiento para detectar cualquier error. Si ocurre una falla, Spark puede reiniciar o reprocesar automáticamente los datos necesarios para garantizar consistencia en los resultados.

Para lograrlo, el sistema depende de que las **fuentes de datos en streaming** soporten mecanismos como **offsets**, es decir, posiciones de lectura en el flujo de datos. Estos offsets permiten al motor saber exactamente qué datos ya se han procesado y cuáles no.

Spark emplea mecanismos de **checkpointing** y **logs de escritura anticipada (write-ahead logs)** para registrar el estado del procesamiento. Este enfoque asegura que, incluso si ocurre una caída, se puede recuperar el procesamiento justo en el punto donde se quedó.

Además, los **sinks** (destinos de salida de los datos) están diseñados para ser **idempotentes**, lo que significa que pueden recibir múltiples veces los mismos datos sin causar duplicados, permitiendo así el reprocesamiento sin efectos colaterales.

Gracias a todo esto, Spark Structured Streaming proporciona una **garantía de entrega exactly-once**, incluso en presencia de fallos.

La siguiente imagen ilustra cómo Spark Structured Streaming utiliza checkpointing y logs para mantener el estado del sistema y garantizar la recuperación tras fallos. En ella se observa cómo el estado del procesamiento se guarda de forma persistente y puede restaurarse para continuar el flujo de datos sin pérdida o duplicación.



![image](assets/cm8znu73e0279356yc6uq3tu4-INSD_PRDT_U5_Apartado5-3_Imagen58.jpg)



### 4.4 Input Sources



En Spark Structured Streaming, los datos pueden provenir tanto de fuentes estáticas (como ficheros) como de flujos infinitos en tiempo real. La clave es que se trabaja con la misma abstracción de DataFrame, lo que permite reutilizar transformaciones y consultas tanto en batch como en streaming, simplificando así el desarrollo.

El punto de entrada para trabajar con estos flujos es el objeto SparkSession, a través del método .readStream(), que devuelve un DataStreamReader. Este objeto permite especificar el formato, el esquema y otras opciones propias de cada fuente.

Existen múltiples fuentes soportadas de forma nativa, entre las más importantes destacan:

- **File**: monitorea directorios y procesa los nuevos archivos (en formatos como JSON, CSV, Parquet, etc.).
- **Kafka**: integración directa para leer mensajes de topics.
- **Socket**: lectura simple de texto desde conexiones TCP.
- **Rate**: útil para testeo, genera datos automáticamente a una frecuencia fija.
- **Rate Per Micro-Batch**: igual que la anterior, pero los datos se agrupan por micro-batch.

La siguiente imagen representa cómo un SparkSession accede a fuentes de datos mediante readStream() para iniciar la lectura continua del stream de entrada. El método .readStream() es el responsable de crear flujos de datos continuos desde diferentes fuentes como archivos, Kafka, sockets o generadores de datos.



![image](assets/cm8znv7fl028n356ydhuhsa3a-INSD_PRDT_U5_Apartado5-4_Imagen59.jpg)



### 4.5 Operations



Este apartado se centra en las transformaciones y agregaciones que se pueden aplicar a los flujos de datos, especialmente aquellas basadas en el tiempo de evento, y en cómo manejar correctamente los datos que llegan con retraso.



1. Spark Structured Streaming permite utilizar la mayoría de las operaciones comunes de DataFrame y Dataset también sobre flujos de datos en tiempo real. Esto incluye filtros, proyecciones, joins, agrupaciones y agregaciones. Además, se pueden registrar DataFrames de streaming como vistas temporales sobre las que ejecutar consultas SQL estándar.

   Una funcionalidad destacada son las **operaciones de ventana sobre el tiempo de evento**, donde los datos se agrupan según intervalos temporales definidos (ventanas) para realizar agregaciones como conteo o suma.

   Esta imagen ilustra cómo Spark agrupa eventos en ventanas de tiempo basadas en el campo de event-time, y cómo se van actualizando las agregaciones a medida que entran nuevos eventos.
2. ![image](assets/cm8znwu6y02a1356y30mmtqd1-step2-INSD_PRDT_U5_Apartado5-5_Imagen60.jpg)
3. En los entornos de streaming es habitual que los eventos no lleguen en el orden exacto en el que ocurrieron. Para manejar correctamente estos **datos retrasados**, Spark permite definir **marcas de agua (watermarks)**. Estas marcas indican hasta qué punto del tiempo de evento se espera recibir datos y, por tanto, cuándo se puede dar por cerrada una ventana. Spark puede mantener el estado intermedio para agregados parciales durante un largo período de tiempo de manera que los datos retrasados puedan actualizar correctamente los agregados de ventanas antiguas
4. ![image](assets/cm8znwu6y02a1356y30mmtqd1-step4-INSD_PRDT_U5_Apartado5-5_Imagen61.jpg)
   La imagen muestra cómo un evento que ocurrió a las 12:04 pero llegó a las 12:11 puede aún ser procesado si está dentro del umbral definido por la marca de agua.

   Spark mantiene un estado intermedio en memoria que almacena los resultados parciales de cada ventana. Esto permite actualizar correctamente los resultados si llegan datos retrasados dentro del umbral definido. Sin embargo, una vez la marca de agua ha superado una ventana, el estado asociado se elimina para liberar recursos.

   La imagen explica cómo las marcas de agua determinan qué datos retrasados aún se procesan y cuáles se descartan, y cómo esto afecta a la actualización de resultados agregados en ventanas.
5. ![image](assets/cm8znwu6y02a1356y30mmtqd1-step5-INSD_PRDT_U5_Apartado5-5_Imagen62.jpg)



#### Tipos de ventanas



![image](assets/cm8zo0pl202d9356yi40blw4b-INSD_PRDT_U5_Apartado5-5_Imagen63.jpg)



### 4.6 Output sinks



En este apartado dedicado a los *output sinks* en Spark Structured Streaming, se explora cómo se gestionan los destinos de salida de los resultados generados por las consultas en streaming. Tras procesar los datos entrantes y generar una tabla de resultados, Spark permite volcar esa información en distintos tipos de *sinks* (almacenamientos o destinos), configurables en cuanto a formato, frecuencia y granularidad de escritura. Esta flexibilidad permite adaptar el sistema a múltiples casos de uso, desde persistencia en disco o Kafka, hasta visualización directa en consola o almacenamiento en memoria.

Para iniciar el proceso de escritura en streaming, Spark utiliza el objeto DataStreamWriter, que se obtiene al invocar writeStream() sobre un DataFrame. A través de él, se pueden configurar los siguientes elementos:



- **Formato de salida y ubicación**  
  Define cómo y dónde se escriben los datos. Puede ser JSON, Parquet, Kafka, etc.
- **Modo de salida**  
  - **Append (por defecto):** solo se escriben las nuevas filas generadas desde el último trigger.
  - **Complete:** se escribe toda la tabla de resultados en cada trigger.
  - **Update:** se escriben solo las filas que han cambiado.
- **Query name**  
  Identificador opcional para seguir el estado de la consulta.
- **Trigger interval**  
  Define la frecuencia de ejecución. Puede ser continua, programada, puntual (once) o hasta vaciar los datos disponibles (availableNow).
- **Checkpoint location**  
  Obligatorio en sinks que garantizan tolerancia a fallos. Define el lugar donde Spark almacena metadatos para recuperar el estado ante errores.



La siguiente imagen ilustra cómo los datos de salida se van generando de forma acumulativa sobre una tabla, permitiendo realizar acciones sobre los eventos capturados.



![image](assets/cm8zo5kmv02gb356yfqcygw74-INSD_PRDT_U5_Apartado5-6_Imagen64.jpg)



**Tipos de sinks y modos de activación**

Spark Structured Streaming permite varios tipos de *sinks*, cada uno adaptado a distintos escenarios:

- **File:** Escribe los resultados en archivos dentro de un directorio.
- **Kafka:** Produce los resultados como mensajes hacia uno o varios *topics*.
- **Console:** Ideal para pruebas, imprime en stdout cada trigger.
- **Memory:** Guarda la salida en memoria como tabla accesible para consultas interactivas.
- **Foreach:** Ejecuta lógica personalizada sobre cada registro.
- **ForeachBatch:** Permite usar código Batch en cada micro-batch (ideal para integración con bases de datos).
- **Streaming Table:** Soporta la lectura y escritura de DataFrames de streaming como si fueran tablas persistentes.

Además, se definen distintos tipos de *triggers* que determinan cuándo se ejecuta una consulta:

- **Default (as soon as possible):** ejecuta tan pronto como termine el batch anterior.
- **ProcessingTime:** frecuencia definida por el usuario (por ejemplo, cada 10 segundos).
- **Once:** ejecuta una sola vez para los datos disponibles y se detiene.
- **AvailableNow:** procesa todos los datos disponibles hasta vaciar la fuente y luego se detiene.



![image](assets/cm8zo6ldy02hx356yxwx3f4k1-INSD_PRDT_U5_Apartado5-6_Imagen65.jpg)



En esta imagen se representa la arquitectura de alto nivel de Structured Streaming, mostrando cómo múltiples flujos de entrada son procesados y almacenados en diversos destinos de salida.



### 4.7 Gestión y monitorización de consultas en Spark Structured Streaming (StreamingQuery)



En Spark Structured Streaming, una vez iniciada una consulta en streaming mediante writeStream().start(), se genera una instancia de tipo StreamingQuery, que permite controlar, gestionar y monitorizar la ejecución en curso. Esta funcionalidad es esencial para entornos de producción, donde se requiere no solo ejecutar flujos de datos, sino también asegurarse de su correcta operación, gestionar sus estados y detectar errores o condiciones específicas durante su vida útil.

A continuación se detallan los principales métodos disponibles agrupados en tres categorías: **Streams**, **Management** y **Monitoring**.



- **Streams – Consultas activas**  
  Estos métodos permiten interactuar con el conjunto de consultas activas dentro de la sesión de Spark:

  - spark.streams.active: lista todas las consultas de streaming actualmente activas.
  - spark.streams.get(id): recupera una consulta concreta a partir de su identificador único.
  - spark.streams.awaitAnyTermination(): bloquea el hilo actual hasta que alguna consulta termine (por error o parada manual).
- **Management – Gestión de una consulta específica**  
  Una vez obtenida una instancia de StreamingQuery, se puede gestionar directamente con los siguientes atributos y métodos:

  - query.id: identificador único persistente de la consulta.
  - query.runId: identificador único de la ejecución actual (cambia si se reinicia).
  - query.name: nombre asignado por el usuario o generado automáticamente.
  - query.explain(): imprime el plan lógico y físico de la consulta (útil para debugging).
  - query.stop(): detiene la ejecución de la consulta.
  - query.awaitTermination(): bloquea hasta que la consulta finaliza (por stop() o error).
  - query.exception: devuelve la excepción si la consulta terminó con fallo.
  - query.recentProgress: lista de los últimos objetos de progreso reportados.
  - query.lastProgress: información del progreso más reciente.
- **Monitoring – Seguimiento del estado de ejecución**  
  Estos atributos permiten conocer el estado interno de la consulta en tiempo real:

  - query.status: diccionario con detalles como:
    - message: descripción textual del estado actual.
    - isDataAvailable: indica si hay datos disponibles para procesar.
    - isTriggerActive: muestra si el trigger (ejecución periódica) está en ejecución activa.



### 4.8 Ejercicios



En este ejercicio práctico trabajaremos con Spark Structured Streaming utilizando un socket como fuente de datos simulados. Configuraremos un servidor simple con netcat que actuará como entrada de texto en tiempo real, y desde Spark leeremos esas líneas para procesarlas como un flujo continuo. Aplicaremos diferentes transformaciones para dividir las líneas en palabras, agruparlas, contarlas y mostrar los resultados por consola en distintos modos de salida (complete, update, append). Además, aprenderemos a usar ventanas temporales, triggers personalizados, almacenamiento en memoria y escritura de resultados en formatos como CSV, JSON y Kafka. Este conjunto de ejercicios nos permitirá explorar de forma práctica los componentes clave de un sistema de streaming: fuentes, transformaciones, sinks, modos de salida y mecanismos de control del procesamiento.

A continuación se dispone de un video a modo de ejemplo para que los alumnos puedan entender cómo ejecutar el siguiente código:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652194_1/scormcontent/assets/INSD_PRDT_U5_Apartado5-7_Video6EjercicioSparkStreaming.mp4?v=1)



El código a ejecutar es el siguiente:



**//En una terminar sola : Entrada de datos simulada con NC**



```bat
nc -lk 9999
```



**//En otra terminal debemos tener corriendo Kafka:**



```ini
confluent local services kafka start
confluent local services kafka-rest start
```



**//En una tercera terminal debemos arrancar spark-shell**



```bat
cd /home/bigdata/spark-3.3.3-bin-hadoop3
bin/spark-shell
```



**//Lecturas desde socket con distintos modos de salida, todo ejecutado en la tercera terminal y previamente habiendo escrito algo en la terminal 1 que actúa como flujo de datos de entrada.**



```scala
val lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
val words = lines.as[String].flatMap(_.split(" "))
val wordCounts = words.groupBy("value").count()
wordCounts.writeStream.outputMode("complete").format("console").start()

val lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
val words = lines.as[String].flatMap(_.split(" "))
val wordCounts = words.withColumn("timestamp", current_timestamp()).withWatermark("timestamp", "60 seconds").select(upper(col("value")))
wordCounts.writeStream.outputMode("append").format("console").start()

val lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
val words = lines.as[String].flatMap(_.split(" "))
val wordCounts = words.groupBy("value").count()
wordCounts.writeStream.outputMode("update").format("console").start()
```



**//Consulta desde memoria (query en memoria)**



```scala
import scala.concurrent._
implicit val ec: scala.concurrent.ExecutionContext = scala.concurrent.ExecutionContext.global

val lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
val words = lines.as[String].flatMap(_.split(" "))
val wordCounts = words.groupBy("value").count()
Future(wordCounts.writeStream.outputMode("complete").format("memory").queryName("streaming1").start())
val query = spark.streams.active.head
spark.sql("SHOW TABLES").show(500, false)
spark.sql("SELECT * FROM streaming1").show(500, false)
query.isActive
query.id
query.runId
query.status
query.lastProgress
query.recentProgress
query.stop
query.status
```



**// Ejercicio 1: Utiliza foreachBatch para escribir los datos del DataFrame wordCounts en csv y en json en /home/bigdata/streaming1csv/ y /home/bigdata/streaming1json/**

**// Como salida, debe haber un único fichero de cada formato y debe sobreescribirse por cada ventana**



```scala
import org.apache.spark.sql._
val lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
val words = lines.as[String].flatMap(_.split(" "))
val wordCounts = words.groupBy("value").count()
wordCounts.writeStream.outputMode("complete").foreachBatch{ (batchDF: DataFrame, batchId: Long) =>
  batchDF.coalesce(1).write.mode("overwrite").csv("/home/bigdata/streaming1csv")
  batchDF.coalesce(1).write.mode("overwrite").json("/home/bigdata/streaming1json")
}.start()
```



**// Ejercicio 2: Agrupa por ventanas de 30 segundos el DataFrame words. Ten en cuenta que se debe tener una columna con el timestamp del evento**



```scala
val lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
val words = lines.as[String].flatMap(_.split(" "))
val windowedCounts = words.withColumn("timestamp", current_timestamp()).groupBy(window($"timestamp", "30 seconds")).count()
val query = windowedCounts.writeStream.outputMode("complete").format("console").option("truncate", false).start()

import org.apache.spark.sql.streaming._
val lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
val words = lines.as[String].flatMap(_.split(" "))
val wordCounts = words.groupBy("value").count()
wordCounts.writeStream.outputMode("complete").format("console").trigger(Trigger.ProcessingTime("30 seconds")).start()
```



**//Ejercicio 3: Repite la query anterior con trigger Once y explica lo que ocurre**

**import org.apache.spark.sql.streaming._**



```scala
val lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()
val words = lines.as[String].flatMap(_.split(" "))
val wordCounts = words.groupBy("value").count()
wordCounts.writeStream.outputMode("complete").format("console").trigger(Trigger.Once()).start()
```



**// Ejercicio 4: Utiliza como origen del Stream, el fichero /home/bigdata/microcuento.txt**

**// cp /home/bigdata/microcuento.txt /home/bigdata/Plantillas/**



```scala
val lines = spark.readStream.format("text").load("/home/bigdata/Plantillas/")
val words = lines.as[String].flatMap(_.split(" "))
val wordCounts = words.groupBy("value").count()
wordCounts.writeStream.outputMode("complete").format("console").option("truncate", false).start()


//INPUT: -File-, Kafka, -Socket-, Rate, RatePerMicro-Batch

//MODE: -Append-, -Complete-, -Update-

//SINKS: File, Kafka, -Foreach-, -ForeachBatch-, -Console-, -Memory-

//TRIGGERS: -ProcessingTime-, -Once-, -AvailableNow-

//confluent local services kafka start
```



**// Ejercicio 5: Inicia la Spark-shell incluyendo el artefacto de spark-sql-kafka y repite el ejercicio 4 con un topic de Kafka como Sink**

**// Se debe mostrar el resultado con un consumidor de Kafka que muestre las claves de cada mensaje**

**// bin/spark-shell --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.3**



```scala
import org.apache.spark.sql.types._
val lines = spark.readStream.format("text").load("/home/bigdata/Plantillas/")
val words = lines.as[String].flatMap(_.split(" "))
val wordCounts = words.groupBy("value").count().select(col("value").as("key"), col("count").cast(StringType).as("value"))
wordCounts.writeStream.outputMode("complete").format("kafka").option("checkpointLocation", "/tmp/checkpoint/").option("kafka.bootstrap.servers", "localhost:9092").option("topic", "topic1").start()
```



## 5. Streams



### 5.1 Introducción



![image](assets/cm8ztjlny0004356yeqr1i1mx-stock-image.jpg)



Recordemos que Spark Streaming es una extensión de Apache Spark diseñada para ofrecer procesamiento de datos en tiempo real de forma escalable, eficiente y tolerante a fallos. Esta tecnología permite recibir flujos de datos en vivo desde diversas fuentes —como Kafka, sockets, o archivos— y procesarlos distribuidamente en un clúster de Spark, ofreciendo resultados en cuestión de segundos.

El modelo de ejecución de Spark Streaming se basa en dividir el flujo de datos en pequeños lotes o **batches**, que se procesan utilizando las capacidades de cómputo de Spark a través de su núcleo: los **RDDs** (Resilient Distributed Datasets). Esto da lugar a una abstracción denominada **DStream** (**Discretized Stream**), que representa un flujo continuo de datos como una **secuencia de RDDs**.

Cada DStream permite aplicar transformaciones y acciones paralelas, del mismo modo que se haría sobre RDDs tradicionales, lo que facilita su adopción para quienes ya estén familiarizados con la API de Spark. Además, está disponible en **Scala, Java y Python**, y permite construir aplicaciones de streaming robustas, con un modelo de programación funcional y expresivo.

En resumen, DStreams ofrece una forma de **estructurar el procesamiento en tiempo real** basada en micro-lotes, aportando simplicidad conceptual, integración con el ecosistema Spark y garantías de tolerancia a fallos.



![image](assets/cm8ztmenm001g356ye6p87m6e-INSD_PRDT_U5_Apartado6-1_Imagen66.jpg)



Veamos un par de ejemplos en la siguiente imagen:



![image](assets/cm8ztneyz002t356y7exppu0o-INSD_PRDT_U5_Apartado6-1_Imagen67.jpg)



- **Parte superior – Representación del DStream como secuencia de RDDs**  
  Esta parte muestra cómo un DStream se descompone internamente en una **serie de RDDs**, cada uno correspondiente a los datos recibidos en un intervalo de tiempo concreto. Por ejemplo, RDD @ time 1 contiene los datos entre el segundo 0 y el 1, RDD @ time 2 entre el segundo 1 y 2, y así sucesivamente. Esta estructura es la base del modelo de procesamiento de Spark Streaming, donde los flujos de datos en tiempo real se dividen en pequeños *micro-batches* para su procesamiento.
- **Parte inferior – Aplicación de operaciones sobre DStreams**  
  Aquí se ejemplifica cómo cualquier operación realizada sobre un DStream (como flatMap) se aplica **de manera independiente a cada RDD** subyacente. En este caso, se transforma un DStream de líneas de texto en un DStream de palabras, dividiendo el contenido de cada RDD en tokens. Esta forma de transformación mantiene la consistencia temporal del procesamiento, ya que cada transformación se aplica por separado a los datos de cada intervalo.



### 5.2 Fuentes entrada y de salida



En Spark Streaming, las **fuentes de entrada** y **salida** son componentes clave para la ingesta y persistencia de datos en tiempo real. Esta plataforma ofrece una variedad de conectores ya integrados que permiten trabajar fácilmente con múltiples sistemas y protocolos de datos.



- **Fuentes de entrada**  
  Spark Streaming proporciona soporte nativo (*out-of-the-box*) para múltiples fuentes de datos de streaming, como:

  - **Kafka**: el sistema de mensajería distribuida más utilizado en entornos de streaming.
  - **Flume**: ideal para la ingesta de datos desde logs.
  - **Kinesis**: una alternativa de AWS similar a Kafka.
  - **Sockets TCP crudos**: para recibir datos directamente desde conexiones de red.
  - **HDFS (Hadoop Distributed File System)** y otros sistemas de ficheros compatibles.

  Además, Spark facilita la creación de **receptores personalizados**, permitiendo definir exactamente cómo debe comportarse el sistema cuando una fuente se inicia o se detiene. Incluso, si se desea mayor control, se puede generar manualmente una **secuencia de RDDs** y tratarlos como un flujo de datos en tiempo real (stream).
- **Fuentes de salida**  
  Una vez procesados los datos en streaming, Spark permite volcar los resultados a múltiples destinos de almacenamiento. Entre los **sinks** o fuentes de salida más comunes, se incluyen:

  - **HDFS o S3**, es decir, sistemas de archivos distribuidos y tolerantes a fallos.
  - **Cassandra**, mediante el conector oficial Spark-Cassandra, ideal para bases de datos NoSQL.
  - **HBase**, otra opción para persistencia escalable y distribuida.

  Además, gracias a la integración con la API de DataFrame, es posible utilizar **cualquier conector compatible con Spark SQL** para almacenar los datos procesados en diversas plataformas, ofreciendo una gran flexibilidad para integrarse con sistemas existentes.



### 5.3 Operaciones de ventana



Spark Streaming ofrece soporte nativo para operaciones de ventana, lo que permite aplicar transformaciones agregadas sobre una serie de datos que se han recibido durante un período de tiempo determinado. Este enfoque es fundamental para el análisis de patrones y la agregación temporal de eventos, como el recuento de palabras por ventana o la detección de actividad en periodos recientes.



#### Ventanas deslizantes: conceptos básicos
Cuando se aplica una operación de ventana sobre un DStream, Spark combina todos los RDDs que caen dentro del intervalo temporal especificado por la ventana y aplica una transformación. Es necesario definir dos parámetros clave:

- **Window Length**: Duración total de la ventana de tiempo (por ejemplo, 3 segundos en la figura).
- **Sliding Interval**: Frecuencia con la que la ventana se mueve o "desliza" (por ejemplo, cada 2 segundos en la figura).

Ambos valores deben ser múltiplos del intervalo de lote (1 en la figura)

1. ![image](assets/cm8zttxtk006m356y5wlzf62l-step1-INSD_PRDT_U5_Apartado6-3_Imagen69.jpg)
   Esta figura ilustra cómo una ventana de duración 3 se desplaza cada 2 unidades de tiempo sobre una secuencia de datos. Observa cómo los RDDs que caen en la ventana activa se agrupan para producir un nuevo resultado cada vez que la ventana se desplaza
2. Una de las formas más utilizadas de aplicar operaciones de ventana es mediante reduceByKeyAndWindow(). A continuación, se muestra un ejemplo para computar el número de veces que aparece una palabra en los últimos 30 segundos de datos, actualizando el resultado cada 10 segundos:

   windowedWordCounts = pairs.reduceByKeyAndWindow(lambda x, y: x + y,

   lambda x, y: x - y,

   30, 10)

   Esta operación aplica una función de reducción (por ejemplo, suma) para mantener actualizados los agregados dentro de la ventana. La función inversa permite optimizar el rendimiento restando los datos salientes de la ventana, evitando recalcular todo desde cero. En particular este código utiliza la función reduceByKeyAndWindow de Spark Streaming para reducir los datos en una ventana deslizante de 30 segundos, calculando el recuento de palabras cada 10 segundos.
3. A diferencia de reduceByKeyAndWindow, que solo mantiene información temporal, updateStateByKey() permite mantener un **estado acumulativo arbitrario** para cada clave a lo largo del tiempo. Esto resulta útil para casos donde se necesita una memoria más persistente del historial.

   Es decir, la operación updateStateByKey te permite mantener un estado arbitrario mientras lo actualizas continuamente con nueva información. Para usar esto, tendrás que seguir dos pasos.

   - Definir el estado
   - Definir la función de actualización del estado: especifica con una función cómo actualizar el estado utilizando el estado anterior y los nuevos valores de un flujo de entrada.

   En cada lote, Spark aplicará la función de actualización del estado para todas las claves existentes, independientemente de si tienen nuevos datos en un Batch o no.
4. ![image](assets/cm8zttxtk006m356y5wlzf62l-step4-INSD_PRDT_U5_Apartado6-3_Imagen70.jpg)
   Esta imagen ilustra cómo se puede mantener y actualizar el estado de forma continua mediante updateStateByKey, combinando datos previos con nuevas entradas. La lógica sigue una línea temporal donde el estado se arrastra y actualiza con cada nuevo batch.
5. Para ejemplificar el uso de updateStateByKey, supongamos que estamos realizando un conteo de palabras acumulativo:
6. ![image](assets/cm8zttxtk006m356y5wlzf62l-step6-INSD_PRDT_U5_Apartado6-3_Imagen71.jpg)
   En el contexto de procesamiento de flujos con Spark Streaming, la operación updateStateByKey es particularmente útil para mantener contadores acumulativos por clave. Este mecanismo se aplica, por ejemplo, a un DStream que contiene pares del tipo (palabra, 1), donde cada evento representa la aparición de una palabra en un batch de datos.

   Para cada clave (es decir, para cada palabra), Spark invoca una función de actualización que recibe dos elementos:

   - newValues: una secuencia de valores recientes, típicamente una lista de unos (1) si estamos haciendo un recuento de palabras.
   - runningCount: el contador acumulado hasta el momento para esa palabra.

   La función de actualización combina ambos valores para producir un nuevo estado, sumando los nuevos valores al contador previo.

   Cabe destacar que esta funcionalidad requiere que se configure un directorio de **checkpointing**, el cual permite a Spark conservar el estado de forma persistente y recuperarlo en caso de fallo, garantizando así tolerancia a errores y consistencia en el procesamiento de los datos en streaming.
7. La operación updateStateByKey(func) es una herramienta poderosa dentro de Spark Streaming que permite mantener un **estado persistente y evolutivo** asociado a cada clave de un DStream. Este estado no se limita únicamente a contadores o sumas; puede ser **arbitrario**, es decir, cualquier estructura de datos que el usuario necesite mantener a lo largo del tiempo, como listas, histogramas, promedios acumulados, valores booleanos, o incluso objetos más complejos.

   Cada vez que se recibe un nuevo micro-batch de datos, Spark aplica una función definida por el usuario (func) que toma como entrada el conjunto de nuevos valores para cada clave (newValues) y el valor del estado previo (runningState), y devuelve un nuevo estado actualizado. Este nuevo estado se conserva para el siguiente micro-batch, lo que permite a la aplicación tener memoria del pasado y realizar un procesamiento más inteligente y contextual.

   Esta capacidad de **gestionar estado arbitrario por clave** es especialmente útil para casos de uso como detección de patrones, mantenimiento de sesiones de usuario, análisis de comportamiento o seguimiento de eventos. Además, para garantizar tolerancia a fallos y recuperación del estado en caso de reinicios, es obligatorio configurar un directorio de checkpointing, donde Spark guarda de forma segura el estado intermedio.



### 5.4 Principales transformaciones disponibles en Spark Streaming



A continuación, se presenta una tabla con las principales **transformaciones disponibles en Spark Streaming** aplicables sobre DStreams, con especial énfasis en aquellas relacionadas con **operaciones de ventana**. Estas transformaciones permiten realizar desde agregaciones por ventana temporal hasta manipulaciones de bajo nivel sobre los RDDs subyacentes. La tabla incluye tanto funciones específicas para flujos con clave-valor como transformaciones más generales, facilitando un amplio abanico de operaciones sobre datos en tiempo real.

| Transformation | Meaning |
| --- | --- |
| window( windowLength , slideInterval ) | Return a new DStream which is computed based on windowed batches of the  source DStream. |
| countByWindow( windowLength,  slideInterval ) | Return a sliding window count of elements in the stream. |
| reduceByWindow( func , windowLength,  slideInterval ) ) | Return a new single-element stream, created by aggregating elements in the  stream over a sliding interval using func . The function should be associative  so that it can be computed correctly in parallel. |
| reduceByKeyAndWindow( func ,windowLength, slideInterval, [numTasks]) | When called on a DStream of (K, V) pairs, returns a new DStream of (K, V)  pairs where the values for each key are aggregated using the given reduce  function func over batches in a sliding window. Note: By default, this uses  Spark's default number of parallel tasks (2 for local mode, and in cluster  mode the number is determined by the config property spark.default.parallelism) to do the grouping. You can pass an  optional numTasks argument to set a different number of tasks |
| reduceByKeyAndWindow( func , invfunc , windowLength, slideInterval, [numTasks] ) | A more efficient version of the above reduceByKeyAndWindow() where the  reduce value of each window is calculated incrementally using the reduce  values of the previous window. This is done by reducing the new data that  enters the sliding window, and “inverse reducing” the old data that leaves the  window. An example would be that of “adding” and “subtracting” counts of  keys as the window slides. However, it is applicable only to “invertible reduce  functions”, that is, those reduce functions which have a corresponding  “inverse reduce” function (taken as parameter invFunc ). Like in reduceByKeyAndWindow, the number of reduce tasks is configurable  through an optional argument. |
| countByValueAndWindow( windowLength,  slideInterval, [numTasks] ) | When called on a DStream of (K, V) pairs, returns a new DStream of (K,  Long) pairs where the value of each key is its frequency within a sliding  window. Like in reduceByKeyAndWindow, the number of reduce tasks is  configurable through an optional argument. |
| map( func ) | Return a new DStream by passing each element of the  source DStream thorugh a function func |
| flatMap( func) | Similar to map but each input item can be mapped to 0 or  more output items |
| filter( func) | Return a new DStream by selecting only the records of the  source DStream on which func returns true |
| repartition( numPartitions ) | Change the level of parallelism in this DStream by  creating more or fewer partitions |
| union( otherStream ) | Return a new DStream that contains the union of the  elements in the source DStream and other DStream |
| count() | Return a new DStream of single-element RDDs by counting  the number of elements in each RDD of the source DStream |
| reduce( func) | Return a new DStream of single-element RDDs by  aggregating the elements in each RDD of the source  DStream using a function func (which takes two arguments  and returns one). The function should be associative so that  it can be computed in parallel. |
| countByValue( ) | When called on a DStream of elements of type K, return a  new DStream of (K, Long) pairs where the value of each key  is its frequency in each RDD of the source DStream. |
| reduceByKey(func, [numTasks]) | When called on a DStream of (K, V) pairs, return a new  DStream of (K, V) pairs where the values for each key are  aggregated using the given reduce function. Note: By default,  this uses Spark's default number of parallel tasks (2 for local  mode, and in cluster mode the number is determined by the  config property spark.default.parallelism) to do the grouping. You can pass an optional numTasks argument to set a different number of tasks |
| join( otherStream, [numTasks]) | When called on two DStreams of (K, V) and (K, W) pairs,  return a new DStream of (K, (V, W)) pairs with all pairs of  elements for each key. |
| cogroup( otherStream , [numTasks]) | When called on a DStream of (K, V) and (K, W) pairs, return a  new DStream of (K, Seq[V], Seq[W]) tuples. |
| transform( func ) | Return a new DStream by applying a RDD-to-RDD function to  every RDD of the source DStream. This can be used to do  arbitrary RDD operations on the DStream. |
| updateStateByKey( func) | Return a new "state" DStream where the state for each key is  updated by applying the given function on the previous state of  the key and the new values for the key. This can be used to  maintain arbitrary state data for each key. |
| saveAsTextFiles( prefix , [ suffix ]) | Save this DStream's contents as text files. The file name at each batch  interval is generated based on prefix and suffix : "prefix-TIME_IN_MS[.suffix]" . |
| foreachRDD( func ) | The most generic output operator that applies a function, func , to each RDD  generated from the stream. This function should push the data in each RDD  to an external system, such as saving the RDD to files, or writing it over the  network to a database. Note that the function func is executed in the driver  process running the streaming application, and will usually have RDD actions  in it that will force the computation of the streaming RDDs. |



### 5.5 Ejemplos



En este ejercicio trabajaremos con Spark Streaming (DStreams), la API clásica de procesamiento en tiempo real de Spark. Usamos tanto sockets TCP como Kafka como fuentes de datos, y procesamos los flujos entrantes en forma de DStreams (Discretized Streams), que son secuencias de RDDs generadas cada intervalo de tiempo definido (por ejemplo, cada 5 o 10 segundos).

Comenzamos leyendo datos desde un socket abierto con netcat, creando un DStream de texto que se divide en palabras y se transforma en pares clave-valor. A través de la operación updateStateByKey, realizamos un seguimiento acumulativo del recuento de palabras, manteniendo su estado entre micro-lotes. Luego, trabajamos con Kafka como fuente, utilizando KafkaUtils.createDirectStream para crear un DStream de registros Kafka, del cual extraemos claves y valores para aplicar lógica personalizada por micro-lote usando foreachRDD.

Finalmente, resolvemos un caso práctico donde simulamos ventas por departamento enviadas desde Kafka, y usamos updateStateByKey para mantener la venta más alta histórica por departamento, y reduceByKey sobre cada RDD para mostrar la venta máxima en cada ventana de 10 segundos.

El código resuelto para que podáis probarlo es:



```scala
///////////////
// EJEMPLO 1 // updateStateByKey
///////////////

// Supongamos que tenemos un flujo de datos de palabras y queremos realizar un seguimiento del recuento acumulativo de cada palabra

// nc -lk 9999

/*
En este ejemplo:

- Definimos una función updateFunction que toma una secuencia de nuevos valores y un estado anterior y devuelve un nuevo estado actualizado.
- Configuramos un estado inicial utilizando un RDD inicial.
- Creamos un DStream de palabras a partir de un socket de red.
- Dividimos las líneas en palabras y asignamos el valor 1 a cada palabra.
- Usamos updateStateByKey para actualizar el estado de las palabras acumulativas.
- Imprimimos el estado actualizado.
- Iniciamos y esperamos la terminación del contexto de streaming.
*/
import org.apache.spark.streaming.{StreamingContext, Seconds}
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.SparkConf

// Crear un contexto de streaming de Spark
val ssc = new StreamingContext(sc, Seconds(5)) // Intervalo de 5 segundo
ssc.checkpoint("/tmp/streaming1")

// Función para actualizar el estado
val updateFunction = (newValues: Seq[Int], runningCount: Option[Int]) => {
  val newCount = newValues.sum + runningCount.getOrElse(0)
  Some(newCount)
}

// Crear un DStream de palabras
val lines = ssc.socketTextStream("localhost", 9999)

// Dividir las líneas en palabras y asignar el valor 1 a cada palabra
val words = lines.flatMap(_.split(" ")).map(word => (word, 1))

// Actualizar el estado usando updateStateByKey
val stateDstream = words.updateStateByKey(updateFunction, 4)

// Imprimir el estado actualizado
stateDstream.print()

// Iniciar la ejecución del flujo de streaming
ssc.start()
//ssc.stop()

///////////////
// EJEMPLO 2 // foreachRDD
///////////////

// bin/confluent local services kafka start
// bin/kafka-console-producer --bootstrap-server localhost:9092 --topic dstreams2 --property "parse.key=true" --property "key.separator=:"

// bin/spark-shell --packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.3.3

import org.apache.spark.streaming.{StreamingContext, Seconds}
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.SparkConf
import org.apache.spark.streaming.kafka010._

// Crear un contexto de streaming de Spark
val ssc = new StreamingContext(sc, Seconds(10)) // Intervalo de 5 segundo
ssc.checkpoint("/tmp/streaming2")

// Configurar los parámetros de conexión a Kafka
val kafkaParams = Map[String, String](
  "bootstrap.servers" -> "localhost:9092",
  "key.deserializer" -> "org.apache.kafka.common.serialization.StringDeserializer",
  "value.deserializer" -> "org.apache.kafka.common.serialization.StringDeserializer",
  "group.id" -> "test-consumer-group",
  "auto.offset.reset" -> "latest",
  "enable.auto.commit" -> "true"
)

// Crear un DStream que recibe datos de un topic de Kafka
val kafkaStream = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Subscribe[String, String](Set("dstreams2"), kafkaParams)
)

// Procesar cada RDD del DStream
kafkaStream.foreachRDD { rdd =>
  // Lógica de procesamiento para cada RDD aquí
  val result = rdd.map { record =>
    // Procesar cada registro del RDD aquí
    println(s"offset: ${record.offset}, key: ${record.key}, value: ${record.value}")
    (record.key, record.value.toInt)
  }.reduceByKey{case (a, b) => a+b}.collect()
  result.foreach(println)
}

// Iniciar la ejecución del flujo de streaming
ssc.start()

// Ejercicio 1:

// Escribe una aplicación con DStreams para obtener la venta por departamento más cara histórica y por ventana de 10 segundos

// Datos de entrada
// - Ventana1 
// echo -e "Zapatos:40\nCamisetas:20\nZapatos:60" | bin/kafka-console-producer --bootstrap-server localhost:9092 --topic dstreams3 --property "parse.key=true" --property "key.separator=:"
// - Ventana2
// echo -e "Camisetas:40\nCamisetas:10\nZapatos:70" | bin/kafka-console-producer --bootstrap-server localhost:9092 --topic dstreams3 --property "parse.key=true" --property "key.separator=:"

import org.apache.spark.streaming.{StreamingContext, Seconds}
import org.apache.spark.streaming.StreamingContext._
import org.apache.spark.SparkConf
import org.apache.spark.streaming.kafka010._

val ssc = new StreamingContext(sc, Seconds(10))
ssc.checkpoint("/tmp/streaming3")

val kafkaParams = Map[String, String](
  "bootstrap.servers" -> "localhost:9092",
  "key.deserializer" -> "org.apache.kafka.common.serialization.StringDeserializer",
  "value.deserializer" -> "org.apache.kafka.common.serialization.StringDeserializer",
  "group.id" -> "test-consumer-group",
  "auto.offset.reset" -> "latest",
  "enable.auto.commit" -> "true"
)

// Crear un DStream que recibe datos de un topic de Kafka
val kafkaStream = KafkaUtils.createDirectStream[String, String](
  ssc,
  LocationStrategies.PreferConsistent,
  ConsumerStrategies.Subscribe[String, String](Set("dstreams3"), kafkaParams)
)

val updateFunction = (newValues: Seq[Int], runningCount: Option[Int]) => {
  import scala.util._
  val newCount = Math.max(Try(newValues.max).getOrElse(0), runningCount.getOrElse(0))
  Some(newCount)
}

val stateDstream = kafkaStream.map(event => (event.key, event.value.toInt)).updateStateByKey(updateFunction, 4)

stateDstream.print()

kafkaStream.foreachRDD { rdd =>
  val result = rdd.map { record =>
    (record.key, record.value.toInt)
  }.reduceByKey{case (a, b) => Math.max(a, b)}.collect()
  println("LAST WINDOW - START")
  result.foreach(println)
  println("LAST WINDOW - END")
}

ssc.start()
```



## 6. Conclusiones



### 6.1 Conclusiones de la unidad



Tras haber leído el contenido de esta unidad y haber realizado los ejercicios prácticos, el alumno debería ser capaz de:

- **Comprender** la importancia del procesamiento en tiempo real dentro del ecosistema Big Data y su aplicación en contextos de alta demanda de inmediatez.
- **Conocer** las principales arquitecturas de streaming como Lambda y Kappa, y evaluar su idoneidad según el caso de uso.
- **Diferenciar** las tecnologías de procesamiento por lotes y en streaming, identificando sus ventajas, limitaciones y escenarios de aplicación.
- **Dominar** el uso de herramientas clave como Apache Kafka y Spark Structured Streaming para la ingesta, transporte y procesamiento de flujos de datos.
- **Conocer** conceptos fundamentales como el event time, las ventanas temporales, la semántica de entrega, la gestión del estado y el backpressure.
- **Implementar** flujos de datos distribuidos con tolerancia a fallos y semántica de entrega controlada, integrando diversas fuentes y sinks.

El conocimiento del procesamiento en tiempo real es esencial para construir sistemas modernos de análisis continuo, monitorización, detección de anomalías o toma de decisiones automatizada. Se recomienda que el alumno practique con los ejercicios propuestos, afianzando así su comprensión técnica y su capacidad para implementar soluciones completas de streaming.

Si al llegar a este punto:

- **Te sientes confiado explicando** qué es el procesamiento en tiempo real y cuándo resulta preferible frente al procesamiento batch.
- **Comprendes** las arquitecturas Lambda y Kappa, el rol de Kafka como backbone de eventos, y las ventajas de Structured Streaming en entornos críticos.
- **Has asimilado** los ejercicios prácticos y puedes desarrollar pipelines que integran ingestión, procesamiento, almacenamiento y tolerancia a fallos.

Entonces, se puede decir que has superado las expectativas de esta unidad y estás preparado para afrontar con éxito unidades más avanzadas centradas en integración de sistemas, machine learning en tiempo real y arquitecturas orientadas a eventos a gran escala.
