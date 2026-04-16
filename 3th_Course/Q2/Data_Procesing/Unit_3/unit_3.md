# Unidad 3. Spark y Spark Cluster.

## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Spark: Contextualización](#2-spark-contextualización)
  - [2.1 Introducción](#21-introducción)
  - [2.2 ¿Qué es Spark?](#22-qué-es-spark)
  - [2.3 ¿Por qué nace Spark?](#23-por-qué-nace-spark)
  - [2.4 Historia de Spark](#24-historia-de-spark)
  - [2.5 Spark vs MAPREDUCE](#25-spark-vs-mapreduce)
  - [2.6 Elementos que componen Spark](#26-elementos-que-componen-spark)
- [3. Arquitectura Spark](#3-arquitectura-spark)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Componentes de la arquitectura](#32-componentes-de-la-arquitectura)
  - [3.3 El parámetro máster](#33-el-parámetro-máster)
  - [3.4 Máster vs Driver](#34-máster-vs-driver)
- [4. Conceptos Necesarios En Spark](#4-conceptos-necesarios-en-spark)
  - [4.1 Introducción](#41-introducción)
  - [4.2 RDD's](#42-rdds)
  - [4.3 DAG's](#43-dags)
  - [4.4 Pair RDDs](#44-pair-rdds)
  - [4.5 Transformaciones](#45-transformaciones)
  - [4.6 Acciones](#46-acciones)
- [5. Ejercicios Básicos](#5-ejercicios-básicos)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Algunas nociones y código básicos](#52-algunas-nociones-y-código-básicos)
  - [5.3 Ejemplo Spark Básico](#53-ejemplo-spark-básico)
  - [5.4 Ejemplo de RDD's](#54-ejemplo-de-rdds)
  - [5.5 Ejemplo de  KeyValue RDD’s](#55-ejemplo-de-keyvalue-rdds)
  - [5.6 Ejemplo de Acciones y transformaciones](#56-ejemplo-de-acciones-y-transformaciones)
- [6. Gestión Y Despliegue De Aplicaciones En Spark](#6-gestión-y-despliegue-de-aplicaciones-en-spark)
  - [6.1 Introducción](#61-introducción)
  - [6.2 Gestión de recursos Spark](#62-gestión-de-recursos-spark)
  - [6.3 Gestión de dependencias en Scala](#63-gestión-de-dependencias-en-scala)
  - [6.4 Despliegue de aplicaciones Spark](#64-despliegue-de-aplicaciones-spark)
  - [6.5 Planificación y gestión de tareas en Spark](#65-planificación-y-gestión-de-tareas-en-spark)
  - [6.6 Ejercicios práctico](#66-ejercicios-práctico)
- [7. Conclusiones](#7-conclusiones)
  - [7.1 Conclusiones de la unidad](#71-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad se abordará el framework Apache Spark dentro del ecosistema de Scala, su evolución a lo largo del tiempo y su impacto en el procesamiento de grandes volúmenes de datos. Se analizarán los principales desafíos que han llevado a su desarrollo, las diferencias clave con otros paradigmas como Hadoop y MapReduce, y cómo Spark ha revolucionado el mundo del Big Data con su enfoque en el procesamiento en memoria y la computación distribuida.

A lo largo de esta unidad, exploraremos los componentes fundamentales de Spark, su arquitectura interna y los conceptos clave que permiten la paralelización eficiente de tareas. Se discutirán aspectos como el uso de RDDs (Resilient Distributed Datasets), la optimización del procesamiento distribuido mediante DAGs (Directed Acyclic Graphs), y las operaciones esenciales que permiten la manipulación de datos a gran escala. Resulta elemental conocer las diferencias entre transformaciones y acciones.

Además, se proporcionarán ejercicios prácticos que ayudarán a consolidar los conocimientos adquiridos y a desarrollar habilidades en la gestión y despliegue de aplicaciones en Apache Spark.

Los apartados a tratar en esta unidad didáctica serán:

- Conceptualización de Apache Spark: contexto y evolución histórica.
- Diferencias entre Spark y MapReduce: ventajas y desafíos de cada enfoque.
- Arquitectura de Spark: componentes clave y su interacción.
- Conceptos esenciales: RDDs, DAGs, transformaciones y acciones.
- Ejercicios prácticos: implementación y optimización de procesamiento distribuido en Spark.
- Gestión y despliegue de aplicaciones Spark: ejecución en clústeres y entornos distribuidos.



- **Spark: Contextualización**  
  Hadoop ha sido una solución ampliamente adoptada en el ámbito del procesamiento de datos a gran escala, ofreciendo un modelo distribuido eficiente basado en el paradigma MapReduce. Sin embargo, con el tiempo, varias limitaciones en su diseño han evidenciado la necesidad de soluciones más avanzadas, como Apache Spark.
- **Arquitectura Spark**  
  Apache Spark se basa en una arquitectura distribuida diseñada para optimizar el procesamiento de grandes volúmenes de datos de manera eficiente y escalable. Su funcionamiento se estructura en torno a un modelo maestro-esclavo, donde diferentes componentes interactúan para coordinar la ejecución de tareas en un clúster. En el siguiente apartado se ve una gráfica que muestra dicha arquitectura y explicamos cada uno de los componentes.
- **Conceptos necesarios en Spark**  
  En este capítulo, se presentan los elementos esenciales que conforman su estructura interna y su modelo de ejecución, estableciendo las bases para comprender cómo Spark gestiona y optimiza los procesos de análisis de datos. A lo largo de las siguientes secciones, se explorarán los principios clave que permiten la paralelización, la organización del flujo de trabajo y la manipulación de datos dentro del ecosistema de Spark.
- **Ejercicios básicos**  
  La mejor manera de comprender Apache Spark y su funcionamiento es a través de la práctica. A lo largo de esta sección, exploraremos ejercicios que te permitirán familiarizarte con los conceptos fundamentales de Spark, desde la manipulación básica de datos hasta el uso de **Key-Value RDDs**, así como la aplicación de **acciones y transformaciones** para procesar información de manera eficiente. Cada ejercicio está diseñado para reforzar el aprendizaje mediante la experimentación directa, permitiéndote aplicar los conocimientos adquiridos en escenarios reales.
- **Gestión y Despliege de aplicaciones en Spark**  
  Recordamos brevemente cómo es la arquitectura Spark antes de hablar de los gestores de recursos en Spark. En Apache Spark, el **Spark Driver** es el encargado de coordinar todas las tareas dentro de una aplicación. Un ejemplo de su uso es a través de la interfaz interactiva **Spark-Shell**.



#### Objetivos



1. Comprender el contexto en el que surge Apache Spark y su evolución dentro del ecosistema Big Data.
2. Diferenciar las características y ventajas de Spark frente a MapReduce, identificando sus principales mejoras y aplicaciones.
3. Analizar la arquitectura de Spark y el papel de sus componentes en la ejecución de procesos distribuidos.
4. Explorar el funcionamiento de los RDDs y los DAGs, evaluando su impacto en la optimización del procesamiento de datos.
5. Implementar transformaciones y acciones en Spark para manipular grandes volúmenes de datos de manera eficiente.
6. Ejecutar ejercicios prácticos para afianzar el uso de Spark en entornos reales, aplicando técnicas de paralelización y procesamiento en memoria.
7. Configurar y desplegar aplicaciones en Spark, gestionando los recursos del clúster para mejorar su rendimiento.



## 2. Spark: Contextualización



### 2.1 Introducción



![image](assets/cm7uzaxjd004i356zl1yt1zot-stock-image.jpg)



Hadoop ha sido una solución ampliamente adoptada en el ámbito del procesamiento de datos a gran escala, ofreciendo un modelo distribuido eficiente basado en el paradigma MapReduce. Sin embargo, con el tiempo, varias limitaciones en su diseño han evidenciado la necesidad de soluciones más avanzadas, como Apache Spark. A continuación, se detallan los principales problemas de Hadoop que impulsaron el desarrollo de Spark:



- **Persistencia y uso intensivo de disco**  
  1. Hadoop utiliza intensivamente el almacenamiento en disco para la gestión de datos intermedios entre las distintas fases de procesamiento. Esto se debe a su enfoque basado en MapReduce, donde cada tarea escribe sus resultados en disco antes de ser procesados en la siguiente fase. Esta constante escritura y lectura introduce una latencia significativa y ralentiza el rendimiento general.
  2. Infrautilización de la Memoria: El modelo de Hadoop no aprovecha eficientemente la memoria RAM de los nodos en el clúster, ya que sus operaciones están diseñadas para almacenar y recuperar datos principalmente desde el disco. Esto genera un desperdicio de recursos, ya que los sistemas modernos cuentan con grandes cantidades de memoria que podrían ser utilizadas para acelerar las operaciones.
- **Implementación de MapReduce y la Fase de Shuffle**  
  1. MapReduce sigue un esquema rígido de procesamiento en dos fases principales: Map y Reduce. Entre ellas, es necesario un proceso de Shuffle, donde los datos se redistribuyen entre los nodos para agruparlos adecuadamente antes de la reducción final. Este proceso de reorganización puede ser costoso en términos de tiempo y recursos computacionales, ya que depende de múltiples escrituras en disco y transferencias de datos en red.
  2. Redistribución Irregular de Datos: El mecanismo de repartición de datos en Hadoop no siempre es eficiente. Dependiendo de la distribución inicial de los datos y la clave utilizada en el procesamiento, pueden generarse desequilibrios entre los nodos del clúster. Esto implica que algunos nodos pueden estar sobrecargados mientras otros permanecen subutilizados, lo que afecta el rendimiento general del sistema.
  3. Falta de Localidad del Dato: Hadoop trata de minimizar el tráfico en la red ejecutando procesos lo más cerca posible de donde se almacenan los datos (data locality). Sin embargo, debido a su esquema de procesamiento basado en disco y a la distribución variable de los datos, no siempre es posible garantizar esta proximidad, lo que conlleva latencias adicionales en la transmisión de datos.
- **Ineficiencia en cálculos iterativos y Overhead en nuevos trabajos**  
  1. Muchos algoritmos de aprendizaje automático y procesamiento de grafos requieren cálculos iterativos, donde los mismos datos son procesados múltiples veces. En Hadoop, cada iteración debe iniciarse como un nuevo trabajo, lo que implica una sobrecarga significativa (overhead) en la inicialización, planificación y gestión de tareas. Esta ineficiencia hace que Hadoop no sea la opción ideal para este tipo de cargas de trabajo.
  2. Dependencia del Disco en el Intercambio de datos entre etapas: En Hadoop, cada etapa del procesamiento necesita escribir datos en disco antes de que la siguiente pueda continuar, tal y como comentamos anteriormente. Esto no solo incrementa la latencia, sino que también añade un costo computacional elevado debido a las constantes operaciones de lectura y escritura.
  3. Redundancia de disco en las fases de Map y Reduce: En el modelo de Hadoop, tanto la fase de Map como la de Reduce requieren redundancia en la escritura y lectura de datos en disco. Esto introduce una penalización de rendimiento significativa, ya que el sistema debe realizar múltiples accesos a disco incluso cuando los datos podrían gestionarse directamente en memoria.



### 2.2 ¿Qué es Spark?



Apache Spark es un potente motor de procesamiento diseñado para entornos de **Big Data**, como los **Data Lakes**, que se caracteriza por su capacidad de realizar análisis de datos de manera eficiente y con alto rendimiento. Su principal ventaja radica en su **procesamiento en memoria distribuido**, lo que le permite manejar grandes volúmenes de datos de manera óptima.

Una de las grandes fortalezas de Spark es su **flexibilidad** para acceder a prácticamente cualquier fuente de datos, lo que lo convierte en una solución versátil dentro del ecosistema de análisis de datos. Gracias a su escalabilidad y velocidad, se ha consolidado como uno de los **proyectos más populares dentro de la Apache Foundation**, formando parte de las plataformas de **Big Data más importantes**, como **Cloudera y Stratio**, y de servicios en la nube como **Amazon Web Services (AWS), Microsoft Azure y Google Cloud Platform (GCP).**

Spark es un **proyecto de código abierto**, respaldado principalmente por **Databricks**, y se ejecuta sobre la **Máquina Virtual de Java (JVM)**. Se presenta como un **framework de programación distribuida** que facilita el **procesamiento tanto por lotes como en tiempo real**, ofreciendo un rendimiento superior en comparación con otros sistemas tradicionales de procesamiento de datos.

Uno de los aspectos que distingue a Apache Spark de otros sistemas como **Hadoop** es su enfoque en el **procesamiento en memoria**, lo que permite ejecutar operaciones en varias fases de manera más eficiente. En contraste, Hadoop sigue basándose en el clásico modelo de programación **MapReduce**, publicado por Google, que depende en gran medida del almacenamiento intermedio en disco, lo que puede ralentizar el procesamiento en comparación con Spark.

Gracias a su arquitectura optimizada, Apache Spark se ha convertido en la opción preferida para proyectos de análisis de datos a gran escala, machine learning y procesamiento en tiempo real, consolidándose como una de las herramientas clave en la actualidad dentro del ecosistema **Big Data**.



![image](assets/cm7uzgose009f356zjb81ik5w-INSD_PRDT_U3_Apartado3-2_Imagen1.jpg)



### 2.3 ¿Por qué nace Spark?



Apache Spark surge como una alternativa a la l**entitud de algunos procesos MapReduce** en Hadoop, con el objetivo de ofrecer un entorno de desarrollo más **amigable y transparente** para los programadores. Uno de los principales problemas de Hadoop en sus primeras versiones era su forma de manejar los **procesos iterativos e interactivos,** ya que cada cálculo intermedio debía ser **persistido en disco,** lo que reducía significativamente la velocidad de procesamiento.



![image](assets/cm7uzj2zx00b2356zd6o5fdzp-INSD_PRDT_U3_Apartado3-3_Imagen2.jpg)



Con el tiempo, se hicieron evidentes las limitaciones de este enfoque, y surgió la necesidad de un **framework capaz de distribuir el procesamiento de manera paralela entre múltiples nodos**, minimizando la dependencia del almacenamiento en disco. Aunque Spark permite utilizar el disco para la **persistencia temporal**, su gran innovación radica en que el procesamiento se realiza **completamente en memoria**, logrando así **una velocidad hasta 100 veces superior a Hadoop en ciertos casos**.

Otra motivación clave detrás del nacimiento de Spark fue la necesidad de contar con un **framework con tolerancia a fallos automática**, lo que permitió a los desarrolladores trabajar con grandes volúmenes de datos sin preocuparse por interrupciones en el proceso.

Apache Spark nació en **2009 como un proyecto de investigación** en la **Universidad de Berkeley**, con el objetivo de solucionar los problemas de eficiencia de MapReduce en tareas iterativas. Un año después, en **2010, el proyecto se liberó como software de código abierto**, y en **2013 fue transferido a la Apache Software Foundation**, consolidándose como un estándar dentro del ecosistema de Big Data.

Desde su concepción, Spark tenía dos objetivos fundamentales:

1. **Ser extremadamente rápido**, gracias al procesamiento en memoria.
2. **Unificar en un solo framework** diversas tareas relacionadas con los grandes volúmenes de datos, incluyendo **procesamiento en Batch, análisis en tiempo real (*streaming*), aprendizaje automático (*machine learning*) y consultas SQL**.

En 2014, **Apache Spark** demostró su capacidad para el procesamiento de grandes volúmenes de datos al establecer un récord en la competencia **Daytona Gray Sort**, un benchmark que mide la eficiencia en la clasificación de grandes conjuntos de datos. Spark logró ordenar **100 TB de datos en solo 23 minutos**, superando significativamente el récord anterior de Hadoop, que tardaba más de **72 minutos** en completar la misma tarea. Este hito validó la superioridad de Spark en términos de **velocidad y eficiencia**, gracias a su modelo de **procesamiento en memoria** y su capacidad para realizar operaciones distribuidas de manera altamente optimizada. Desde entonces, Spark se consolidó como la plataforma líder para procesamiento de datos masivos en entornos de Big Data.



![image](assets/cm7uzkebl00cf356zg31zdjyo-INSD_PRDT_U3_Apartado3-3_Imagen3.jpg)



### 2.4 Historia de Spark



Apache Spark fue desarrollado originalmente en **2009** en la **Universidad de California, Berkeley**, como parte de un proyecto de investigación liderado por **Matei Zaharia** dentro del **AMPLab**. En sus inicios, Spark surgió como un **ejemplo de framework** construido sobre **Apache Mesos**, un sistema para la gestión de recursos en entornos distribuidos.



![image](assets/cm7uzligx00ds356zz134bteh-INSD_PRDT_U3_Apartado3-4_Imagen4.jpg)



La primera aplicación práctica de Spark fue utilizada para **monitorear y predecir el tráfico en la Bahía de San Francisco**, demostrando su potencial para el procesamiento en tiempo real de grandes volúmenes de datos. A medida que el proyecto avanzaba, una comunidad de desarrolladores comenzó a formarse en torno a él, lo que llevó a que en **2013** Spark ingresara en el programa **Apache Incubator**, marcando el inicio de su consolidación como una tecnología clave dentro del ecosistema de Big Data.

El crecimiento del proyecto fue exponencial, y en **2014**, gracias a su **estabilidad y rápido desarrollo**, Apache Spark fue promovido a la categoría de **Apache Top-Level Project**, consolidándose como uno de los frameworks de procesamiento de datos más influyentes y utilizados en la industria.

Desde entonces, Spark ha seguido evolucionando y expandiéndose, convirtiéndose en una herramienta fundamental en áreas como **análisis de datos, machine learning, procesamiento de streaming y consultas SQL**, con una comunidad activa y un fuerte respaldo de empresas líderes en tecnología.



### 2.5 Spark vs MAPREDUCE



La siguiente imagen muestra la comparativa entre el número de líneas de código que se necesitan para implementar un MAPREDUCE en Java para hacer el programa de conteo de palabras (considerado el  “Hola Mundo” de esta disciplina), frente a las líneas de código necesarias para realizar lo mismo pero en Spark.



![image](assets/cm7uzmu4k00fw356zd41a1nm5-INSD_PRDT_U3_Apartado3-5_Imagen5.jpg)



Tanto **MapReduce** como **Apache Spark** son **frameworks diseñados para el procesamiento de Big Data**, compartiendo una arquitectura basada en **clústeres distribuidos** que operan sobre **múltiples nodos**. Además, ambos sistemas destacan por su **escalabilidad**, permitiendo manejar crecientes volúmenes de datos sin perder eficiencia, y por su **tolerancia a fallos**, asegurando la continuidad del procesamiento incluso ante errores en los nodos.

Por contrario, la siguiente tabla muestra sus diferencias:

| MAPREDUCE | SPARK |
| --- | --- |
| En MapReduce, la unidad de computación principal es la tarea. | En Spark, la unidad de computación principal es una aplicación. |
| Se basa en el procesamiento en disco, lo que lo hace más lento. | Utiliza procesamiento en memoria, lo que mejora su velocidad. |
| Requiere una mayor cantidad de código para su implementación. | Permite implementar soluciones con menos código. |
| Sus APIs son más complejas y requieren mayor esfuerzo de desarrollo. | Ofrece APIs más intuitivas y fáciles de usar. |
| No cuenta con módulos adicionales integrados. | Incorpora componentes especializados, como MLlib para aprendizaje automático, GraphX para análisis de grafos, Spark Streaming para procesamiento en tiempo real y Spark SQL para consultas estructuradas. |
| Desarrollado en Java. | Desarrollado en Scala. |
| Está diseñado principalmente para el procesamiento batch. | Soporta tanto procesamiento batch como en tiempo real. |



### 2.6 Elementos que componen Spark



Apache Spark es una plataforma de computación distribuida de propósito general que destaca por su capacidad de integrar múltiples paradigmas de procesamiento de datos dentro de un motor unificado de análisis. Gracias a esta arquitectura, Spark permite combinar diferentes enfoques, como la ejecución de sentencias SQL, la aplicación de algoritmos de Machine Learning, el procesamiento de datos en streaming, y el análisis de datos estructurados y grafos, todo dentro de un mismo ecosistema.

Para lograr esta versatilidad, Spark incorpora una serie de librerías especializadas, cada una diseñada para un tipo de procesamiento específico:

- Spark SQL, para el manejo eficiente de datos estructurados y consultas SQL.
- Spark Streaming, que permite procesar datos en tiempo real con flujos continuos.
- MLlib, una completa biblioteca de algoritmos de aprendizaje automático.
- GraphX, un módulo orientado a la computación sobre grafos y análisis de redes complejas.
- MLPipelines: API de alto nivel para pipelines Machine learning sobre DataFrames.
- SparkR: Paquete de R package con una interfaz ligera.

Esta integración de tecnologías hace de Apache Spark una solución integral para el procesamiento de datos a gran escala,

Apache Spark destaca por su flexibilidad y compatibilidad con diversos lenguajes de programación, permitiendo a los desarrolladores trabajar con Java, Scala, Python y R, según sus necesidades y preferencias.

En la siguiente imagen se puede comprobar cómo se llama a Spark desde diferentes lenguajes:



![image](assets/cm7uzq1kc00i1356zc988acv7-INSD_PRDT_U3_Apartado3-6_Imagen6.jpg)



Además, Spark ofrece múltiples opciones para la gestión y planificación de tareas (scheduling), siendo capaz de ejecutarse sobre plataformas como Kubernetes, su propio Apache Spark Standalone, Mesos y YARN, lo que le permite adaptarse a distintos entornos y arquitecturas de computación distribuida.

En cuanto al almacenamiento de datos, Spark es altamente versátil y puede procesar información almacenada en una amplia variedad de sistemas, incluyendo sistemas de archivos locales, Amazon S3, Ceph FS, Google Cloud Storage (GCS FS) y Apache Hadoop HDFS, asegurando compatibilidad con las infraestructuras más utilizadas en entornos de Big Data.



![image](assets/cm7uzqv1500je356zb83nmfjw-INSD_PRDT_U3_Apartado3-6_Imagen7.jpg)



## 3. Arquitectura Spark



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



Apache Spark se basa en una arquitectura distribuida diseñada para optimizar el procesamiento de grandes volúmenes de datos de manera eficiente y escalable. Su funcionamiento se estructura en torno a un modelo maestro-esclavo, donde diferentes componentes interactúan para coordinar la ejecución de tareas en un clúster. En el siguiente apartado se ve una gráfica que muestra dicha arquitectura y explicamos cada uno de los componentes.

Aunque en la asignatura de Búsqueda y Análisis de la Información los alumnos trabajan con Spark para Python mediante PySpark, introduciendo brevemente conceptos clave sobre los elementos de Spark y su arquitectura, en esta asignatura se profundizará en su funcionamiento interno, optimización del procesamiento distribuido, gestión eficiente de recursos y despliegue de aplicaciones en entornos reales, permitiendo un dominio más completo de la herramienta dentro del ecosistema Big Data.



### 3.2 Componentes de la arquitectura



El Driver Program es el componente central de cualquier aplicación de Spark. Su función principal es orquestar la ejecución del programa, coordinando la asignación de tareas y gestionando la interacción con el clúster de cómputo. Es el punto de entrada de la aplicación y es donde el usuario define la lógica de procesamiento.

Dentro del Driver Program se crean y gestionan los objetos RDD (Resilient Distributed Datasets) los cuales se explican posteriormente, y que representan los conjuntos de datos distribuidos que se procesarán. Además, supervisa el progreso de la ejecución y maneja posibles fallos, asegurando la resiliencia del sistema.

El SparkContext es el componente que actúa como intermediario entre el Driver Program y el Cluster Manager. Es responsable de establecer la conexión con el clúster y de solicitar los recursos necesarios para ejecutar la aplicación.

A través del SparkContext, el driver puede enviar instrucciones al clúster, definir RDDs, realizar transformaciones y ejecutar acciones sobre los datos distribuidos. Además, mantiene la información del estado de la aplicación y supervisa la asignación de tareas a los ejecutores. En versiones modernas de Spark, el SparkContext ha sido reemplazado por el SparkSession, que proporciona una API unificada para el procesamiento de datos estructurados y no estructurados.



El siguiente esquema resume la arquitectura:



![image](assets/cm7v01zkm00n9356ze6cvx6sz-INSD_PRDT_U3_Apartado4-2_Imagen8.jpg)



### 3.3 El parámetro máster



El parámetro master en Apache Spark es un elemento fundamental para la ejecución de aplicaciones distribuidas, ya que especifica la ubicación del nodo maestro dentro del clúster de procesamiento. Dependiendo de su configuración, este parámetro puede definir desde una ejecución local hasta la conexión con un clúster distribuido más complejo.

En escenarios de desarrollo y pruebas, es común utilizar configuraciones locales de Spark. La opción local permite ejecutar Spark en un solo hilo, sin aprovechar el paralelismo, lo que resulta útil para depurar código o realizar pruebas sencillas. Por otro lado, la variante local[K] permite ejecutar Spark en un entorno local con K hilos de trabajo, donde el valor de K idealmente coincide con el número de núcleos del procesador disponible. Esta configuración maximiza el aprovechamiento de los recursos locales sin necesidad de un clúster externo.

Cuando se requiere un entorno de ejecución distribuido, Spark permite conectarse a clústeres externos utilizando el protocolo spark://HOST:PORT. En este caso, el parámetro master apunta a un clúster de Spark en modo standalone, con un puerto predeterminado de 7077. Este esquema es común en arquitecturas donde se desea administrar los recursos de manera más eficiente y distribuir la carga de trabajo entre múltiples nodos.

Alternativamente, Spark ofrece compatibilidad con Mesos, un gestor de clústeres que permite compartir recursos entre distintas aplicaciones. Para ello, el parámetro master debe configurarse como mesos://HOST:PORT, donde el puerto predeterminado es 5050. Esta integración facilita la ejecución de Spark en entornos donde se utilizan múltiples frameworks de procesamiento de datos.

La selección del valor adecuado para master depende del contexto y los recursos disponibles. Para un desarrollo ligero, una configuración local es suficiente; sin embargo, en entornos de producción con grandes volúmenes de datos, se recomienda conectar Spark a un clúster distribuido para garantizar eficiencia y escalabilidad.



![image](assets/cm7v03dfz00oc356zr02lpxf6-INSD_PRDT_U3_Apartado4-3_Imagen9.png)



### 3.4 Máster vs Driver



En la arquitectura de Apache Spark, el **Master** y el **Driver** desempeñan roles clave en la gestión y ejecución de las aplicaciones distribuidas. Aunque ambos son fundamentales para el funcionamiento del sistema, tienen responsabilidades distintas en la coordinación de los recursos y la ejecución de tareas dentro del clúster.



- **El Rol del Máster**  
  El Master actúa como el gestor de recursos dentro del clúster de Spark. Su función principal es administrar y asignar los recursos computacionales a las diferentes aplicaciones que se ejecutan en el entorno distribuido. Para ello, adquiere executors en los nodos del clúster, que son los encargados de procesar la información y gestionar las cachés de datos. Este mecanismo permite optimizar el rendimiento del sistema, asegurando una distribución eficiente de las cargas de trabajo entre los nodos disponibles.
- **El Rol del Driver**  
  Por otro lado, el **Driver** es el componente que inicia y coordina la ejecución de una aplicación en Spark. Su primera tarea es establecer una conexión con el **Cluster Manager**, permitiéndole solicitar los recursos necesarios para levantar el clúster de ejecución. Una vez configurado, el **Driver** distribuye el código de la aplicación entre los **executors**, asegurando que cada uno reciba la porción de trabajo correspondiente. Además, el **Driver** es responsable de enviar y supervisar la ejecución de las tareas asignadas a los **executors**, garantizando que los procesos se lleven a cabo de manera eficiente y controlada.

  En resumen, mientras el **Master** se encarga de administrar los recursos del clúster, el **Driver** gestiona la ejecución de las aplicaciones dentro de dicho entorno. La interacción entre ambos componentes es fundamental para lograr una ejecución distribuida eficiente en Apache Spark.



![image](assets/cm7v060dx00qh356zrv9ecnbd-INSD_PRDT_U3_Apartado4-4_Imagen10.jpg)



## 4. Conceptos Necesarios En Spark



### 4.1 Introducción



![image](assets/cm7v07e3700rl356zmw3bs9xq-stock-image.jpg)



El procesamiento distribuido de datos a gran escala requiere una arquitectura eficiente y bien definida que permita la ejecución óptima de tareas sobre grandes volúmenes de información. Apache Spark proporciona un conjunto de conceptos fundamentales que sustentan su funcionamiento y lo diferencian de otros modelos de procesamiento. En este capítulo, se presentan los elementos esenciales que conforman su estructura interna y su modelo de ejecución, estableciendo las bases para comprender cómo Spark gestiona y optimiza los procesos de análisis de datos. A lo largo de las siguientes secciones, se explorarán los principios clave que permiten la paralelización, la organización del flujo de trabajo y la manipulación de datos dentro del ecosistema de Spark.



### 4.2 RDD's



Los Resilient Distributed Datasets (RDDs) constituyen la abstracción fundamental de datos en Spark Core y son la base sobre la que se construye el procesamiento distribuido en este framework. Un RDD es una estructura inmutable y tolerante a fallos que distribuye los datos en particiones a lo largo de los nodos de un clúster, permitiendo su procesamiento en paralelo de manera eficiente.

Uno de los principales beneficios de los RDDs es su tolerancia a fallos. En un entorno distribuido, donde los nodos pueden fallar de manera impredecible, Spark emplea un mecanismo basado en linaje de datos (lineage) que permite reconstruir automáticamente cualquier partición perdida sin necesidad de realizar copias redundantes, lo que optimiza el uso de recursos. Además, los RDDs aprovechan la localidad de los datos, es decir, intentan minimizar la transferencia de información entre nodos, lo que reduce la latencia y mejora el rendimiento del sistema.



![image](assets/cm7v0bbpy00te356zfqc7xzn5-Imagen2.jpg)



Los RDDs son especialmente adecuados para **algoritmos iterativos**, como aquellos empleados en aprendizaje automático y procesamiento de grafos, ya que permiten reutilizar datos en memoria sin necesidad de escribir en disco en cada iteración. Esta eficiencia ha sido clave en la evolución de Spark como alternativa al modelo tradicional de **Batch Processing**, ampliando sus aplicaciones a un espectro más amplio de casos de uso.

El concepto de RDD fue introducido en el artículo **"Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing"**, en el cual se establece cómo esta abstracción facilita el procesamiento distribuido al usuario, ocultando parcialmente la complejidad de la distribución y ejecución paralela de tareas.

La generación de un RDD puede darse en dos escenarios principales:

1. **Desde una colección de datos existente en el driver**, la cual es distribuida entre los nodos del clúster para su procesamiento.
2. **Desde una fuente de datos externa**, como un sistema de archivos distribuido (HDFS, Amazon S3), una base de datos o cualquier otro repositorio de datos accesible por Spark.



![image](assets/cm7v0cwx800us356z8bxr4h3s-Imagen3.jpg)



### 4.3 DAG's



Un **Grafo Acíclico Dirigido (DAG, por sus siglas en inglés Directed Acyclic Graph)** es la estructura fundamental utilizada por Apache Spark para representar el flujo de ejecución de una aplicación. En términos simples, un DAG es un conjunto de vértices y aristas donde cada vértice representa una operación en los datos y las aristas indican la dependencia entre estas operaciones. La propiedad de ser **acíclico** significa que el flujo de ejecución no contiene ciclos, es decir, no hay caminos en el grafo que lleven a una repetición infinita de tareas.

Cuando una aplicación Spark ejecuta transformaciones sobre un **Resilient Distributed Dataset (RDD)** o un **DataFrame**, no se procesan inmediatamente, sino que se construye un **DAG lógico** que define cómo se encadenan las transformaciones. Solo cuando se ejecuta una **acción**, como una agregación o una escritura en disco, Spark convierte este DAG lógico en un **DAG físico**, dividiéndolo en etapas (*stages*) y tareas (*tasks*), optimizando así su ejecución distribuida. Esta estructura permite a Spark ejecutar tareas en paralelo siempre que sea posible y minimizar la recomputación en caso de fallo, asegurando una ejecución eficiente de los procesos de análisis de datos.

El **DAG Scheduler** es el componente de Apache Spark encargado de transformar el **Grafo Acíclico Dirigido (DAG)** lógico de una aplicación en un conjunto de **etapas (*stages*) y tareas (*tasks*)** optimizadas para su ejecución en un clúster distribuido. Su principal función es dividir el flujo de trabajo en bloques de ejecución independientes, asignando tareas a los nodos disponibles y gestionando la ejecución en paralelo siempre que sea posible.

Cuando una acción es invocada en un RDD o DataFrame, el **DAG Scheduler** analiza el DAG lógico y lo descompone en **stages,** que se definen por la existencia de *shuffles*(operaciones que requieren intercambio de datos entre nodos, como *groupBy*o *join*). Cada *stage*contiene múltiples **tasks,** que son unidades de trabajo ejecutadas en paralelo sobre distintas particiones de datos. Una vez estructurado el flujo de ejecución, el **DAG Scheduler** envía estas tareas al **Task Scheduler,** quien se encarga de su distribución en los ejecutores dentro del clúster.



![image](assets/cm7v0fq6100w6356z9z9gv3gn-INSD_PRDT_U3_Apartado5-3_Imagen13.jpg)



### 4.4 Pair RDDs



En Apache Spark, los términos **Key-Value RDD** y **Pair RDD** se refieren a lo mismo. Un **Pair RDD** es un tipo especial de **Resilient Distributed Dataset (RDD)** en el que cada elemento es una pareja **(clave, valor) (key, value)**. Se denomina **Key-Value RDD** porque organiza los datos en esta estructura, lo que facilita ciertas operaciones como agrupamientos, agregaciones y combinaciones entre conjuntos de datos.

Un **Pair RDD** permite aplicar operaciones específicas que no están disponibles en los RDDs estándar (compuestos solo por valores). Algunas de las operaciones más comunes en **Pair RDDs** incluyen:

- **groupByKey()**: Agrupa los valores por clave.
- **reduceByKey(func)**: Aplica una función de reducción a los valores que comparten la misma clave.
- **join(otherRDD)**: Une dos RDDs por clave, combinando los valores asociados.
- **mapValues(func)**: Aplica una función únicamente a los valores, manteniendo las claves intactas.

Estos RDDs son fundamentales cuando se trabaja con datos estructurados como registros de logs, datos de sensores o cualquier dataset en el que cada entrada tenga una clave y un valor asociado.

En resumen, **Pair RDD y Key-Value RDD son términos intercambiables**, ambos refiriéndose a RDDs donde los datos se organizan en pares (K, V), permitiendo operaciones avanzadas de procesamiento distribuido en Spark.



### 4.5 Transformaciones



Las **transformaciones** en Apache Spark son operaciones que se aplican sobre un **Resilient Distributed Dataset (RDD)** para producir un nuevo RDD. Sin embargo, una característica clave de estas transformaciones es que son **"lazy" (perezosas)**, lo que significa que no se ejecutan de inmediato. En lugar de procesar los datos en el momento en que se define la transformación, Spark simplemente registra la operación y la almacena en el **Driver**, construyendo un **Grafo Acíclico Dirigido (DAG)** con la secuencia de transformaciones aplicadas.

Dado que las transformaciones no realizan cálculos de manera inmediata, Spark solo evalúa y ejecuta el flujo de trabajo cuando se invoca una **acción**, como count() o collect(). Este enfoque permite optimizar el procesamiento, ya que Spark puede reorganizar las operaciones y minimizar la cantidad de cómputo necesario. Algunas de las transformaciones más utilizadas en Spark incluyen map, filter, sample, union, groupByKey, reduceByKey, join y cache, cada una diseñada para manipular los datos de manera eficiente en entornos distribuidos.

En el siguiente enlace : [https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations](https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations) se pueden encontrar las distintas transformaciones que ofrece Spark.



![image](assets/cm7v0n73000yc356zurec138s-INSD_PRDT_U3_Apartado5-5_Imagen14.jpg)



### 4.6 Acciones



En Apache Spark, las **acciones** son operaciones que desencadenan la ejecución real de las tareas distribuidas en los **executors**. A diferencia de las transformaciones, que son perezosas (*lazy*) y solo construyen un flujo de ejecución, las acciones obligan a Spark a evaluar las transformaciones pendientes y devolver un resultado al **driver** o escribir los datos en un sistema de almacenamiento.

Este diseño permite a Spark optimizar la ejecución de tareas, retrasando los cálculos hasta que sea estrictamente necesario. En lugar de procesar cada transformación inmediatamente, Spark acumula una serie de operaciones y las ejecuta de manera eficiente en el momento en que se requiere un resultado. Esto permite realizar una **lógica incremental** sobre los datos hasta llegar a un conjunto reducido de información que puede ser almacenado o analizado.

Entre las acciones más comunes en Spark se encuentran:

- **reduce(func)**: Agrega los elementos de un RDD utilizando una función de reducción.
- **collect()**: Recupera todos los elementos de un RDD y los envía al driver.
- **count()**: Devuelve el número de elementos en el RDD.
- **saveAsTextFile(path)**: Guarda el contenido de un RDD en un archivo.
- **lookup(key)**: Recupera los valores asociados a una clave específica en un *Pair RDD*.



> Para más detalles sobre las acciones en Apache Spark, puedes consultar la documentación oficial en el siguiente link
>
> [Link](https://spark.apache.org/docs/latest/rdd-programming-guide.html#actions)



![image](assets/cm7v0pty3010a356zmc5a9ops-Imagen4.jpg)



## 5. Ejercicios Básicos



### 5.1 Introducción



![image](assets/cm7v0ru5z011f356zgk01zbtx-stock-image.jpg)



La mejor manera de comprender Apache Spark y su funcionamiento es a través de la práctica. A lo largo de esta sección, exploraremos ejercicios que te permitirán familiarizarte con los conceptos fundamentales de Spark, desde la manipulación básica de datos hasta el uso de **Key-Value RDDs**, así como la aplicación de **acciones y transformaciones** para procesar información de manera eficiente. Cada ejercicio está diseñado para reforzar el aprendizaje mediante la experimentación directa, permitiéndote aplicar los conocimientos adquiridos en escenarios reales.

Te animo a que intentes resolver cada ejercicio antes de consultar la solución. Si encuentras dificultades, revisa la teoría y vuelve a intentarlo con un enfoque diferente. Una vez que hayas comparado tu solución con la propuesta, es recomendable repetir el ejercicio para consolidar los conceptos. La práctica activa y la repetición son clave para dominar Spark y desarrollar la confianza necesaria para aplicar estos conocimientos en proyectos más complejos.

Comenzaremos explicando un programa ejemplo con el siguiente código:



```scala
// base RDD
val lines = sc.textFile(“dummy.log”)
// transformed RDDs
val errors = lines.filter(_.startsWith("ERROR"))
val messages = errors.map(_.split("\t")).map(r => r(1))
messages.cache()
// action 1
messages.filter(_.contains("mysql")).count()
// action 2
messages.filter(_.contains("php")).count()
```



Este programa en **Apache Spark** procesa un archivo de logs llamado "dummy.log", extrayendo y analizando mensajes de error.

Primero, se crea un **RDD base** (lines) cargando el archivo de texto.

1. ![image](assets/cm7v0vjpa015c356zfr7ve8ta-step1-INSD_PRDT_U3_Apartado6-1_Imagen16.jpg)
2. Luego, se filtran las líneas que comienzan con "ERROR", generando un nuevo RDD (errors). A partir de este conjunto filtrado, se extraen los mensajes de error dividiendo cada línea por tabulaciones (\t) y seleccionando la segunda columna (messages). Para mejorar la eficiencia, este RDD se almacena en caché con cache(), evitando su recomputación en futuras consultas.
3. ![image](assets/cm7v0vjpa015c356zfr7ve8ta-step3-INSD_PRDT_U3_Apartado6-1_Imagen17.jpg)
4. Posteriormente, se ejecutan dos acciones sobre messages: la primera cuenta cuántos mensajes contienen la palabra "mysql", mientras que la segunda cuenta cuántos mensajes incluyen "php". Esto permite analizar la frecuencia de estos errores en los registros sin necesidad de volver a cargar ni transformar los datos en cada consulta.
5. ![image](assets/cm7v0vjpa015c356zfr7ve8ta-step5-INSD_PRDT_U3_Apartado6-1_Imagen18.jpg)



### 5.2 Algunas nociones y código básicos



#### Persistencia



En Apache Spark, el almacenamiento y reutilización de datos en memoria es clave para optimizar el rendimiento de las aplicaciones distribuidas. Dado que los **Resilient Distributed Datasets (RDDs)** son estructuras inmutables y perezosas (*lazy*), cada vez que se ejecuta una acción, Spark debe recomputar todas las transformaciones previas desde el origen de los datos. Para evitar esta recomputación y mejorar la eficiencia, Spark ofrece mecanismos de **persistencia** a través de los métodos cache() y persist().

**Uso de cache() y persist()**

El método rdd.cache() permite almacenar el RDD en memoria como objetos deserializados en la JVM, evitando que Spark lo vuelva a calcular en futuras acciones. Este método es una abreviación de rdd.persist(StorageLevel.MEMORY_ONLY), lo que significa que los datos solo se guardan en memoria y, si no caben completamente, las particiones faltantes se recomputarán en lugar de almacenarse en disco.

Por otro lado, rdd.persist() es más flexible y permite definir diferentes niveles de almacenamiento mediante StorageLevel. Dependiendo de la configuración elegida, Spark puede almacenar los RDDs en memoria, en disco o incluso usar técnicas de serialización para reducir el consumo de memoria. Algunas de las opciones más utilizadas incluyen:



- **MEMORY_ONLY**  
  Guarda el RDD en memoria deserializado. Si no cabe, las particiones faltantes se recalculan.
- **MEMORY_AND_DISK**  
  Guarda en memoria y, si no cabe, almacena en disco para evitar recomputaciones.
- **MEMORY_ONLY_SER**  
  Almacena el RDD serializado para optimizar espacio, pero aumenta el costo de lectura.
- **DISK_ONLY**  
  Guarda los datos únicamente en disco, sin usar memoria.
- **OFF_HEAP (experimental)**  
  Usa memoria fuera del heap de la JVM para mejorar la gestión de recursos.



La siguiente tabla resume lo comentado pero según la documentación original y en inglés:



![image](assets/cm7v14wsz01bc356zbxd86edl-INSD_PRDT_U3_Apartado6-2_Imagen19.jpg)



#### Liberación de Memoria con unpersist()



#### Variables



En Apache Spark, las **variables compartidas** permiten optimizar el procesamiento distribuido al reducir la cantidad de datos que se envían entre los nodos. Dos tipos fundamentales de variables utilizadas en Spark son **las variables de difusión (Broadcast Variables)** y **los acumuladores (Accumulators)**.



- **Variables Broadcast**  
  Las **variables de difusión (Broadcast Variables)** permiten compartir grandes conjuntos de datos de solo lectura con todos los nodos del clúster sin necesidad de enviarlos múltiples veces. Esto reduce significativamente la sobrecarga en la comunicación y mejora la eficiencia del procesamiento distribuido.

  Por ejemplo, al ejecutar el siguiente código:

  **val broadcastVar = sc.broadcast(Array(1,2,3))**

  Spark distribuye el array [1,2,3] a todos los nodos ejecutores como una variable de solo lectura, en lugar de enviarla repetidamente en cada tarea. Posteriormente, se puede acceder al valor de la variable mediante broadcastVar.value, obteniendo la salida Array(1,2,3).
- **Acumuladores en Spark**  
  Los **acumuladores (Accumulators)** son variables utilizadas para agregar valores de manera eficiente en un entorno distribuido. Se emplean comúnmente para realizar sumas o contar eventos dentro de un conjunto de datos distribuido sin afectar el flujo de procesamiento de los RDDs.

  Por ejemplo, el siguiente código inicializa un acumulador con un valor de 0:

  **val accum = sc.accumulator(0)**

  Luego, al ejecutar un proceso distribuido donde cada elemento de un array se agrega al acumulador mediante foreach, se suma el valor de cada elemento:

  **sc.parallelize(Array(1,2,3,4)).foreach(x => accum += x)**

  Finalmente, al acceder a accum.value, se obtiene el resultado 10, que representa la suma de los valores en el array.

  A diferencia de las variables Broadcast, los acumuladores son ideales para realizar agregaciones globales sin necesidad de modificar los datos distribuidos en los RDDs. Son especialmente útiles en contadores de logs, sumas de métricas y cálculos en paralelo.

  Resumen: Mientras que las Broadcast Variables permiten compartir datos de solo lectura de manera eficiente, los Accumulators facilitan la agregación de valores en cálculos distribuidos.



#### Paralelización de una colección



En Apache Spark, es posible convertir una colección de datos en un **Resilient Distributed Dataset (RDD)** para aprovechar el procesamiento distribuido. Este proceso se conoce como **paralelización de una colección** y permite dividir los datos en particiones que pueden ser procesadas en paralelo por los nodos del clúster.

En este caso, se comienza con la creación de una colección en **Scala**, definida como un **array de enteros**:

val data = Array(25, 20, 15, 10, 5)

Luego, se utiliza el método sc.parallelize(data), que convierte la colección en un **RDD distribuido** llamado distData:

val distData = sc.parallelize(data)

Este RDD ahora puede aprovechar la capacidad de cómputo distribuido de Spark, permitiendo operaciones en paralelo en múltiples particiones.

Finalmente, se aplica la operación reduce(_ + _) sobre distData, que suma todos los elementos del RDD utilizando la función de reducción:

distData.reduce(_ + _)

El resultado obtenido es 75, que corresponde a la suma de los valores [25 + 20 + 15 + 10 + 5].

Este enfoque permite realizar cálculos eficientes sobre grandes volúmenes de datos sin depender de una única máquina, distribuyendo la carga de trabajo en los ejecutores del clúster y optimizando el tiempo de procesamiento.



#### Lectura de un fichero



Primeramente veremos la lectura de un fichero local:

En Apache Spark, la lectura de archivos de texto se realiza utilizando el método sc.textFile(), que carga el contenido del fichero en un **Resilient Distributed Dataset (RDD)**. Este enfoque permite procesar archivos de gran tamaño de manera distribuida en un clúster, facilitando la manipulación y análisis de datos.

En el ejemplo a continuación, se carga un archivo llamado "README.md" en un **RDD de tipo String**, donde cada línea del archivo se convierte en un elemento del RDD:

val distFile = sc.textFile("README.md")

Este comando crea un RDD denominado distFile, que permite realizar transformaciones y acciones sobre el contenido del archivo.

A continuación, se ejecuta la acción first, que devuelve la primera línea del archivo:

distFile.first

El resultado indica que la primera línea del archivo es "#Apache Spark".

Seguidamente comentamos la lectura de un fichero de HDFS:

Apache Spark permite leer archivos almacenados en el **Hadoop Distributed File System (HDFS)** utilizando el método sc.textFile(). Esta funcionalidad es esencial para procesar grandes volúmenes de datos distribuidos en un clúster.

En este ejemplo, se carga un archivo de texto llamado "README.txt", ubicado en una carpeta dentro de **HDFS**:

val distFile = sc.textFile("hdfs://mi_carpeta:9000/README.txt")

Este comando crea un **RDD distribuido de tipo String**, donde cada línea del archivo se convierte en un elemento del RDD. La ventaja de este enfoque es que Spark puede dividir automáticamente el archivo en particiones y distribuirlas entre los nodos del clúster, optimizando el procesamiento paralelo.

A continuación, se ejecuta la acción first, que recupera la primera línea del archivo:

distFile.first

El resultado muestra que la primera línea del archivo contiene información sobre **Hadoop.**



#### MapReduce wordcount



El conteo de palabras (*Word Count*) es un ejemplo clásico de procesamiento distribuido en **Apache Spark** utilizando el paradigma **MapReduce**. En este caso, el objetivo es leer un archivo almacenado en **HDFS**, contar la frecuencia de cada palabra y almacenar los resultados nuevamente en **HDFS**.



- **Carga del Archivo desde HDFS**  
  **val file = sc.textFile("hdfs://…")**

  Se carga un archivo de texto desde **HDFS** en un **RDD,** donde cada línea del archivo se convierte en un elemento del RDD. Esto permite procesar el contenido del archivo de manera distribuida.
- **Transformaciones para el Conteo de Palabras**  
  val counts = file.flatMap(line => line.split(" "))

  .map(word => (word, 1))

  .reduceByKey(_ + _)

  Aquí se aplican varias transformaciones sobre el RDD:

  - **flatMap(line => line.split(" "))**: Divide cada línea en palabras, generando un nuevo RDD donde cada palabra es un elemento independiente.
  - **map(word => (word, 1))**: Convierte cada palabra en un par clave-valor (palabra, 1), asignando un conteo inicial de 1.
  - **reduceByKey(_ + _)**: Agrupa todas las palabras iguales y suma sus valores, obteniendo la cantidad de veces que aparece cada palabra en el texto.

  Este enfoque se basa en el modelo **MapReduce,** donde **map** asigna claves y valores, mientras que **reduceByKey** realiza la agregación por clave.
- **Almacenamiento del Resultado en HDFS**  
  counts.saveAsTextFile("hdfs://…")

  Finalmente, los resultados del conteo de palabras se guardan en **HDFS** mediante saveAsTextFile(), lo que permite su consulta y análisis posterior.



#### Funcionamiento de Spark en stages



En **Apache Spark**, la ejecución de un **job** se divide en **stages (etapas)** basadas en su **Grafo Acíclico Dirigido (DAG)**. Cada **stage** representa un conjunto de tareas que pueden ejecutarse en paralelo sobre diferentes particiones de datos antes de requerir una reorganización (*shuffle*).



**Proceso de Ejecución en Stages**

1. - Se carga un archivo de texto con textFile(), generando un RDD particionado.
   - Se aplican transformaciones como map(), que se ejecutan en cada partición sin necesidad de comunicación entre nodos.
2. - Operaciones como reduceByKey() requieren un **shuffle**, redistribuyendo los datos entre particiones.
   - Una vez completada la reorganización, Spark ejecuta la reducción en cada partición.
3. - La acción collect() obtiene el resultado final y lo envía al **driver**.
   - Cada etapa se ejecuta en paralelo como un conjunto de **tareas individuales** (una por partición).



![image](assets/cm7v1m3qm01us356zoecho7iv-INSD_PRDT_U3_Apartado6-2-6_Imagen20.jpg)



#### Fase de Suffle



La **fase de Shuffle** en Apache Spark es el proceso de **redistribución de datos** entre nodos cuando se ejecutan transformaciones que requieren agrupar información basada en una clave, como groupByKey, reduceByKey o join. Esta fase es crítica para la ejecución de tareas que dependen de datos dispersos en múltiples particiones.



#### Etapas del Shuffle

1. - Cada **Map Task** procesa una partición de datos y asigna los valores a diferentes **buckets** según su clave.
   - Los datos son organizados y almacenados temporalmente en disco o memoria.
2. - Cada **Reduce Task** lee los datos desde múltiples buckets distribuidos en diferentes nodos.
   - Se realiza una agregación de datos antes de ejecutar la operación final.
3. Este proceso puede ser **costoso en términos de rendimiento**, ya que implica escritura y lectura de datos en red y disco. Para optimizar el Shuffle, Spark permite ajustar parámetros como spark.sql.shuffle.partitions y utilizar funciones como combineByKey para reducir la cantidad de datos intercambiados.
4. ![image](assets/cm7v1oqqb01wm356z3hhzyzjr-step4-INSD_PRDT_U3_Apartado6-2-7_Imagen21.jpg)



#### Gestión de la memoria



La gestión de memoria en **Apache Spark** está dividida en diferentes segmentos para optimizar el rendimiento de las aplicaciones. Spark asigna un **75% de la memoria total disponible** (spark.memory.fraction = 0.75) para la ejecución de tareas y almacenamiento de datos en caché, mientras que el restante 25% se reserva para la memoria del usuario y otros procesos del sistema.

Dentro del espacio asignado a Spark, la memoria se divide en dos principales componentes:



- **Execution Memory (Memoria de Ejecución)**  
  Se utiliza para operaciones como *joins, aggregations y sorting.* Si no hay suficiente memoria, Spark realiza un **spill to disk,** moviendo datos al disco para evitar fallos de memoria.
- **Storage Memory (Memoria de Almacenamiento)**  
  Se emplea para caché de **RDDs, DataFrames y Broadcast Variables.** Si la memoria de almacenamiento no está completamente utilizada, Spark puede liberar espacio para la ejecución de tareas.



![image](assets/cm7v20p1102n4356ze7cb1fc6-INSD_PRDT_U3_Apartado6-2-8_Imagen22.jpg)



La siguiente imagen muestra diferentes escenarios en los que **Execution Memory y Storage Memory** comparten espacio de forma dinámica. Cuando una de ellas necesita más recursos, puede utilizar la memoria libre disponible en la otra. Sin embargo, si la memoria se llena, Spark mueve datos al disco para evitar fallos. Este balance dinámico optimiza la eficiencia del procesamiento distribuido en Spark.



![image](assets/cm7v21luj02oh356zjhy7derl-INSD_PRDT_U3_Apartado6-2-8_Imagen23.jpg)



### 5.3 Ejemplo Spark Básico



En esta serie de ejercicios, pondrás en práctica los pasos fundamentales para iniciar y configurar una sesión de **Spark Shell**.



- **Ejercicio 1: Acceso al Directorio de Spark**  
  - Abre una terminal en tu sistema.
  - Navega al directorio donde está instalado Spark (/home/bigdata/spark-3.3.3-bin-hadoop3/).
  - ¿Qué archivos y carpetas contiene este directorio?

  Este comando cambia el directorio de trabajo al que contiene la instalación de **Apache Spark 3.3.3** con compatibilidad para **Hadoop 3**. Aquí es donde se encuentran todos los archivos ejecutables y de configuración de Spark.
- **Ejercicio 2: Exploración de la Ayuda de Spark Shell**  
  - Ejecuta el siguiente comando para consultar las opciones disponibles en Spark Shell:

  **bin/spark-shell --help**

  - Revisa las diferentes opciones de configuración. ¿Cuáles crees que podrían ser útiles para mejorar el rendimiento en un entorno distribuido?

  Este comando ejecuta la interfaz interactiva **Spark Shell** con la opción --help, lo que muestra una lista de opciones disponibles para configurar la sesión de Spark. **Spark Shell** es un entorno de línea de comandos basado en **Scala** que permite ejecutar comandos Spark de manera interactiva.
- **Ejercicio 3: Iniciar Spark Shell con Configuración Personalizada**  
  - Inicia **Spark Shell** con los siguientes parámetros:

  bin/spark-shell --master local[*] --name SparkBasico --deploy-mode client --driver-memory 1G --executor-memory 1G --conf spark.sql.shuffle.partitions=50

  - Explica el significado de cada parámetro utilizado en el comando.
  - Una vez iniciada la sesión, observa los mensajes que aparecen en la terminal. ¿Puedes identificar cuántos ejecutores se han asignado?

  Aquí se está lanzando **Spark Shell** con una configuración específica:

  - --master local[*]: Ejecuta Spark en **modo local**, utilizando todos los núcleos disponibles del procesador (* indica todos los núcleos).
  - --name SparkBasico: Asigna el nombre **"SparkBasico"** a la aplicación Spark.
  - --deploy-mode client: Ejecuta Spark en modo **cliente**, donde el driver se ejecuta en la misma máquina en la que se lanzó el comando.
  - --driver-memory 1G: Asigna **1 GB de memoria** para el proceso **driver**.
  - --executor-memory 1G: Asigna **1 GB de memoria** para cada **executor**.

  --conf spark.sql.shuffle.partitions=50: Configura Spark para realizar 50 particiones durante las operaciones de shuffle (intercambio de datos entre nodos), lo que afecta el rendimiento en operaciones como groupBy o join.
- **Ejercicio 4: Acceder a la Interfaz Web de Spark UI**  
  - Abre un navegador web y accede a la interfaz de usuario de Spark en la siguiente dirección:

  http://10.0.2.15:4040

  - Explora las pestañas disponibles y responde:
    - ¿Cuántos jobs se han ejecutado hasta ahora?
    - ¿Qué información encuentras en la sección de *Stages* y *Storage*?

  Este enlace abre la interfaz de usuario de Spark en el navegador. La Spark UI proporciona información detallada sobre la ejecución de tareas, memoria utilizada, procesos en curso y estadísticas de rendimiento. Se ejecuta por defecto en el puerto 4040.
- **Ejercicio 5: Consultar la Documentación Oficial de Transformaciones y Acciones**  
  - Accede a los siguientes enlaces en la documentación oficial de Spark tanto de transformaciones como de acciones comentada previamente.
  - Identifica y describe al menos tres transformaciones y tres acciones que puedan ser útiles en un análisis de datos.

  Recuerda que : **Transformaciones:** Operaciones perezosas que generan nuevos RDDs sin ejecutarse inmediatamente. Y **Acciones:** Operaciones que activan la ejecución real de los cálculos y devuelven un resultado o guardan los datos.



El siguiente video muestra la solución y explicación del ejercicio:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652188_1/scormcontent/assets/INSD_PRDT_U3_Apartado6-3_Video1SparkBasico.mp4?v=1)



### 5.4 Ejemplo de RDD's



En este ejercicio, aplicarás el paradigma **MapReduce** utilizando **RDDs** en Apache Spark para analizar el texto de *El Quijote* descargado desde *Project Gutenberg*. A lo largo de los pasos, explorarás la distribución del archivo en particiones, realizarás conteo de palabras y analizarás diversas características del texto. Es muy importante tener el HDF levantado y haber hecho los pasos de la unidad anterior del ejercicio de HDFS ya que nos dejaba preparado el fichero en HDFS. Todo esto se explica en el video al final.



- **Preparación del Entorno**  
  - Descarga el texto de *El Quijote* con el siguiente comando: bigdata> wget http://www.gutenberg.org/cache/epub/2000/pg2000.txt

  - Carga el archivo en un RDD desde el sistema de archivos local: spark> val quijoteRDD = sc.textFile("file:///home/bigdata/Descargas/pg2000.txt")

  - Verifica cuántas particiones tiene el RDD: spark> quijoteRDD.getNumPartitions

  - Carga el archivo desde HDFS, especificando 10 particiones: spark> val quijoteRDD = sc.textFile("hdfs://localhost:9000/ebooks/quijote.txt", 10)

  - Comprueba nuevamente la cantidad de particiones en este nuevo RDD: spark> quijoteRDD.getNumPartitions
- **Análisis del Texto con RDDs**  
  - **¿En cuántas líneas aparece la palabra "molino"?**
    - Escribe una consulta en **Spark Shell** que cuente cuántas líneas contienen la palabra "molino".
  - **¿Cuántas palabras distintas aparecen en el texto?**
    - Aplica transformaciones sobre el RDD para obtener un conteo de palabras únicas.
  - **¿Cuáles son las 10 palabras más repetidas (con más de 3 letras) y cuántas veces aparecen?**
    - Filtra las palabras con más de 3 caracteres y obtén las 10 más frecuentes junto con su frecuencia.
  - **¿Cuántas veces aparece la palabra “hidalgo”?**
    - Busca específicamente cuántas veces se menciona la palabra "hidalgo" en el texto.
  - **¿Cuántas líneas tiene el texto?**
    - Obtén el número total de líneas en el archivo.
  - **¿Cuántas líneas tienen más de 20 caracteres?**
    - Filtra las líneas con más de 20 caracteres y cuenta cuántas cumplen esta condición.
  - **¿Cuál es la línea más larga y cuántos caracteres tiene?**
    - Determina la línea con mayor cantidad de caracteres en el archivo.



El siguiente video muestra la solución y explicación del ejercicio:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652188_1/scormcontent/assets/INSD_PRDT_U3_Apartado6-4_Video2RDD.mp4?v=1)



### 5.5 Ejemplo de  KeyValue RDD’s



#### Ejercicios Prácticos: Operaciones con Key-Value RDDs en Apache Spark



- **Ejercicio 1: Número de Particiones en reduceByKey**  
  - Identifica qué método se puede utilizar para conocer el número de particiones por defecto en **reduceByKey**.
  - Explica qué representa este número de particiones y cómo influye en el rendimiento de la operación.
- **Ejercicio 2: Reducir valores por clave**  
  - Usa reduceByKey para encontrar el valor máximo de cada clave en un RDD de pares (clave, valor).
  - **Objetivo:** Obtener un resultado donde cada clave esté asociada a su valor más alto.

  // Resultado esperado: Array((1,2), (3,6))
- **Ejercicio 3: Agrupación y filtrado con groupByKey**  
  - Aplica groupByKey para agrupar valores por clave.
  - Usa otra transformación para obtener el valor mínimo de cada clave.

  // Resultado esperado: Array((1,2), (3,4))
- **Ejercicio 4: Transformaciones con mapValues**  
  - Utiliza mapValues para modificar los valores del RDD.
  - Multiplica por 3 solo los valores que sean múltiplos de 3.

  // Resultado esperado: Array((1,2), (3,4), (3,18))
- **Ejercicio 5: Salario más alto por departamento con combineByKey**  
  - A partir de un conjunto de datos de empleados con su departamento y salario, usa combineByKey para calcular el salario máximo en cada departamento.
  - **Resultado esperado:** Mostrar el salario más alto para cada departamento.

  // Resultado esperado: Salario máximo en TI: 2500\n Salario máximo en Marketing: 1600\n Salario máximo en Ventas: 2100
- **Ejercicio 6: Descomposición con flatMapValues**  
  - Utiliza flatMapValues para descomponer los valores de un RDD en listas de números.
  - Obtén el número máximo dentro de cada grupo.

  // Resultado esperado: Array((pares,6), (impares,3))
- **Ejercicio 7: Ordenación de resultados**  
  - Ordena los resultados del ejercicio 5 de mayor a menor según el salario más alto.

  // Resultado esperado: Array((TI,2350), (Ventas,1800), (Marketing,1600))
- **Ejercicio 8: Operaciones de combinación con Join**  
  - Usa leftOuterJoin y calcula el sumatorio de valores por clave.

  // Resultado esperado: Array((1,2), (3,28))
- **Ejercicio 9: Filtrado de claves repetidas**  
  - Filtra claves que tengan al menos **dos valores** asociados en el RDD.
  - Mantén solo las llaves con al menos **dos repeticiones**, eliminando aquellas que aparecen solo una vez.

  // Resultado esperado: Array((key1,1), (key1,2), (key1,4), (key2,1), (key2,3), (key4,1), (key4,1))
- **Ejercicio 10: Evaluación de notas finales de estudiantes**  
  - Dados registros de alumnos con asistencia, parcial, práctica y examen, calcula la nota final con la siguiente fórmula: Nota Final=10%×Asistencia+20%×Parcial+20%×Praˊctica+50%×Examen\text{Nota Final} = 10\% \times \text{Asistencia} + 20\% \times \text{Parcial} + 20\% \times \text{Práctica} + 50\% \times \text{Examen}Nota Final=10%×Asistencia+20%×Parcial+20%×Praˊctica+50%×Examen
    - Filtra los alumnos que **no sean de Erasmus** y hayan aprobado ambas asignaturas (examen ≥ 4).

  // Resultado esperado: Array((Manolito,5.1000000000000005))

  Para: val clase1 = sc.parallelize(Seq(("Juanito", Seq(10, 5, 9, 3)), ("Pepito", Seq(8, 8, 5, 8)), ("Manolito", Seq(7, 3, 9, 4))))
- **Ejercicio 11: Almacenamiento en HDFS**  
  - Antes de guardar los datos, **¿cómo iniciarías HDFS?**
  - Guarda el resultado del **Ejercicio 9** en la ruta /ejercicios/ejercicio9 de **HDFS** utilizando saveAsTextFile.
  - Pregunta: ¿Cuántos ficheros se han creado en dicha carpeta? Explica por qué



Para la resolución de estos ejercicios se han realizado dos videos separados con el fin de limitar su extensión.

El siguiente video muestra la solución y explicación hasta el ejericico 5 incluído:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652188_1/scormcontent/assets/INSD_PRDT_U3_Apartado6-5_Video3PairRDD1.mp4?v=1)



Por otro lado el siguiente video continúa con los ejercicios desde el 6 hasta el 11 incluídos:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652188_1/scormcontent/assets/INSD_PRDT_U3_Apartado6-5_Video4PairRDD2.mp4?v=1)



### 5.6 Ejemplo de Acciones y transformaciones



En este conjunto de ejercicios, explorarás las principales transformaciones y acciones aplicadas sobre **Resilient Distributed Datasets (RDDs)** en Apache Spark. Aprenderás a manipular, filtrar, combinar y transformar datos de manera eficiente, utilizando operaciones como **map, flatMap, filter, distinct, union, intersection, cartesian, reduce, aggregate, countByValue**, entre otras.



- **Ejercicio 1: Creación y Exploración de RDDs**  
  - Crea un RDD con una secuencia de números y verifica la cantidad de elementos.
  - Crea un RDD de líneas de texto y otro con números repetidos.
- **Ejercicio 2: Transformaciones Básicas**  
  - Diferencia entre map y flatMap: transforma un RDD de líneas en palabras individuales.
  - Aplica filter para extraer elementos que cumplan una condición específica.
  - Compara el comportamiento de flatMap y filter cuando se aplican en distintos órdenes.
- **Ejercicio 3: Operaciones sobre Datos Repetidos**  
  - Utiliza distinct para eliminar duplicados en un RDD de números.
  - Aplica countByValue para contar la ocurrencia de cada número.
- **Ejercicio 4: Muestreo de Datos**  
  - Experimenta con sample y takeSample para extraer subconjuntos de datos con y sin reemplazo
- **Ejercicio 5: Combinación de RDDs**  
  - Une dos RDDs usando union.
  - Obtén la intersección de dos RDDs con intersection.
  - Resta los elementos de un RDD en otro utilizando subtract.
- **Ejercicio 6: Producto Cartesiano y Ordenación**  
  - Genera combinaciones entre elementos de dos RDDs utilizando cartesian.
  - Ordena los resultados en orden ascendente y descendente con sortByKey.
- **Ejercicio 7: Cálculo de Estadísticas sobre RDDs**  
  - Aplica countByValue sobre un conjunto de palabras para obtener la frecuencia de cada una.
  - Utiliza top y takeOrdered para extraer los valores más altos o más bajos.
- **Ejercicio 8: Operaciones de Reducción**  
  - Usa reduce para obtener la suma y la multiplicación de todos los elementos de un RDD.
  - Aplica fold con valores iniciales diferentes y observa su impacto en el resultado.
  - Implementa aggregate para dividir el procesamiento en particiones y combinar los resultados.
- **Ejercicio 9: Agrupación y Reducción por Clave**  
  - Aplica reduceByKey para sumar valores por clave en un conjunto de pares clave-valor.
  - Usa map con interpolación de cadenas para generar mensajes descriptivos a partir de los resultados.
- **Ejercicio 10: Particionamiento de RDDs**  
  - Verifica el número de particiones de un RDD.
  - Reparticiona un RDD usando repartition y coalesce, y analiza su impacto en la distribución de datos.
- **Ejercicio 11: Contador de Palabras Específicas**  
  - Filtra un RDD de palabras para contar cuántas veces aparecen "Spark" y "Scala" utilizando reduceByKey.
- **Ejercicio 12: Agrupación por Módulo**  
  - Agrupa los números del 0 al 99 en función de su resto al dividir por 3 y suma los valores de cada grupo



El siguiente video muestra la solución y explicación del ejercicio:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652188_1/scormcontent/assets/INSD_PRDT_U3_Apartado6-6_Video5TransformcionesYAcciones.mp4?v=1)



## 6. Gestión Y Despliegue De Aplicaciones En Spark



### 6.1 Introducción



![image](assets/cm7vkyy2l002q356zwnvqat1c-stock-image.jpg)



Recordamos brevemente cómo es la arquitectura Spark antes de hablar de los gestores de recursos en Spark. En Apache Spark, el **Spark Driver** es el encargado de coordinar todas las tareas dentro de una aplicación. Un ejemplo de su uso es a través de la interfaz interactiva **Spark-Shell**.

Cuando se inicia un Spark Driver, lo primero que se genera es un **Spark Context**, que actúa como la conexión entre la aplicación y el clúster de ejecución. Este contexto permite la comunicación con los recursos del sistema.

Dentro de la infraestructura de Spark, los **Worker Nodes** son las unidades encargadas de alojar los recursos asignados por el **Gestor de Recursos**. Estos nodos reservan recursos como **núcleos de CPU, memoria y almacenamiento en disco** dentro de las máquinas donde el gestor está desplegado.

Cuando el Spark Driver inicia, solicita al Gestor de Recursos una asignación de recursos específica. Si el gestor tiene capacidad suficiente, asigna **Executors de Spark** dentro de los Worker Nodes. En caso contrario, el gestor envía ofertas parciales al **Spark Context**, permitiendo que este decida si acepta la oferta disponible o prefiere esperar un tiempo determinado para recibir una mejor.

Los **Executors** son procesos basados en **JVM (Java Virtual Machine)** que ejecutan las tareas enviadas por el Spark Driver. Además, almacenan en caché los datos y se comunican entre sí para intercambiar información a través del proceso de **Shuffle**.

El Spark Driver organiza el procesamiento en distintas etapas: **Jobs, Stages y Tasks**. A partir de un **RDD (Resilient Distributed Dataset)**, genera un Job, que luego se divide en Stages, y estos, a su vez, en múltiples Tasks.

Si un Executor falla, el **Gestor de Recursos** se encarga de iniciar un nuevo Executor, y el Spark Driver reasigna la tarea que no pudo completarse, garantizando así la tolerancia a fallos dentro del sistema.

Gracias a esta arquitectura, cada aplicación de Spark puede procesarse de forma aislada de las demás, evitando interferencias. Sin embargo, para optimizar el rendimiento y minimizar la latencia en la comunicación, se recomienda que el **Spark Driver y los Executors se encuentren dentro de la misma red**.



### 6.2 Gestión de recursos Spark



En Apache Spark, la gestión eficiente de recursos es un aspecto fundamental para optimizar el rendimiento y escalabilidad de las aplicaciones distribuidas. Dado que Spark puede ejecutarse en diferentes entornos de clúster, es compatible con múltiples gestores de recursos, cada uno con sus propias características y ventajas. Dependiendo del caso de uso y los requisitos del sistema, se pueden elegir distintas opciones para asignar y administrar los recursos de cómputo, memoria y almacenamiento. En esta sección, exploraremos los cuatro principales gestores de recursos soportados por Spark: **Spark Standalone**, un gestor nativo de Spark recomendado para entornos de prueba y desarrollo; **YARN (Yet Another Resource Negotiator)**, ampliamente utilizado en ecosistemas Hadoop y en entornos productivos; **Mesos**, el sistema sobre el cual nació Spark y que permite una gestión dinámica de recursos; y finalmente, **Kubernetes**, una solución moderna centrada en la orquestación de contenedores, ofreciendo escalabilidad y balanceo de carga automatizados.



![image](assets/cm7vl0cer004u356z3yodqqjy-INSD_PRDT_U3_Apartado7-2_Imagen24.jpg)



A continuación, se detallarán las características clave de cada uno de estos gestores de recursos y su funcionamiento dentro del ecosistema Spark:



- **Spark stand alone**  
  El modo **Spark Standalone** es el gestor de recursos incluido por defecto en la distribución Open-Source de Apache Spark. Es una opción sencilla de configurar, especialmente en entornos de desarrollo o pruebas, ya que permite desplegar Spark en un único nodo sin necesidad de configuraciones complejas. Sin embargo, **no es recomendable para entornos productivos**, ya que carece de funcionalidades avanzadas de gestión de recursos y escalabilidad.

  Entre sus características principales destacan

  - **Aislamiento de recursos**, permitiendo especificar la cantidad de **núcleos de CPU y memoria** asignados tanto para el **máster** como para los **workers**.
  - **Modos de ejecución:**
    - **Client:** el **Driver** se ejecuta en la misma máquina donde se lanzó la aplicación.
    - **Cluster:** el **Driver** se ejecuta dentro de un **Worker Node** gestionado por el clúster.
  - Se puede habilitar la opción **"supervise"**, que permite reiniciar la aplicación si el proceso finaliza con un código distinto de cero.
  - Para garantizar alta disponibilidad (**HA**), se puede configurar un máster redundante utilizando **ZooKeeper**
  - Proporciona una **API REST** para el despliegue de aplicaciones Spark.
  - Configuración de parámetros de recursos al lanzar la aplicación:
    - **Driver**: --driver-memory, --driver-cores (solo en modo cluster).
    - **Executors**: --total-executor-cores, --executor-cores.
  - Para definir el número de Executors que se iniciarán, es necesario ajustar correctamente los parámetros de asignación de recursos.
- **Yarn**  
  **YARN** es el gestor de recursos utilizado en el ecosistema Hadoop y una de las opciones más comunes en entornos productivos para ejecutar Spark. Su integración con **HDFS** y su capacidad para manejar múltiples aplicaciones en paralelo lo convierten en una opción robusta y flexible.

  Sus características más relevantes incluyen:

  - **Compatibilidad con Docker**, permitiendo ejecutar aplicaciones en contenedores.
  - **Particionamiento dinámico**, lo que permite ajustar el uso de recursos en función de la carga del sistema.
  - **Despliegue de contenedores** en los Worker Nodes.
  - **Soporte para recursos especializados**, como **GPUs y FPGAs**.
  - **Uso de colas de prioridad** (queue) de YARN para gestionar la asignación de recursos en función de la prioridad de las aplicaciones.
  - **Modos de ejecución:**
    - **Client:** el **Driver** se ejecuta en la misma máquina donde se inicia la aplicación.
    - **Cluster:** el **Driver** se ejecuta dentro de un **Worker Node** del clúster.
  - Configuración mediante el archivo de configuración yarn-site.xml.
  - Parámetros de recursos al lanzar la aplicación:
    - **Driver**: --driver-memory, --driver-cores (solo en modo cluster).
    - **Executors**: --num-executors, --executor-cores.
  - Se debe calcular correctamente el número total de núcleos disponibles en el clúster para asignarlos de manera eficiente a los ejecutores de Spark.
- **Mesos**  
  Apache **Mesos** fue el sistema sobre el cual originalmente se diseñó Spark y sigue siendo una opción popular en entornos productivos, especialmente en arquitecturas con múltiples aplicaciones y uso dinámico de recursos.

  Algunas de sus principales características son:

  - **Compatibilidad con Docker**, lo que permite encapsular aplicaciones en contenedores.
  - **Gestión dinámica de recursos**, permitiendo aprovechar recursos adicionales si están disponibles en el clúster.
  - **Despliegue de agentes (workers)** que ejecutan tareas distribuidas en el sistema.
  - **Soporte para GPUs y FPGAs**, lo que lo hace útil en aplicaciones que requieren procesamiento acelerado.
  - **Alta disponibilidad (HA)** mediante la integración con **ZooKeeper**.
  - **Modos de ejecución:**
    - **Client:** el **Driver** se ejecuta en la misma máquina donde se inicia la aplicación.
    - **Cluster:** el **Driver** se ejecuta dentro de un **Worker Node** del gestor de recursos. Se puede activar el **modo supervise**, que permite reiniciar automáticamente la aplicación si falla.
  - Parámetros de configuración de recursos al lanzar la aplicación:
    - **Driver**: --driver-memory, --driver-cores (solo en modo cluster).
    - **Executors**: --total-executor-cores, --executor-cores.
  - Para definir el número de Executors que se levantarán, se deben considerar los recursos disponibles en Mesos y la configuración del clúster.
- **Kubernetes**  
  **Kubernetes** es un sistema de orquestación de contenedores desarrollado originalmente por Google y se ha convertido en una opción popular para la gestión de aplicaciones distribuidas, incluyendo Apache Spark. Se destaca por su **escalabilidad automática** y **balanceo de carga dinámico**, lo que lo hace ideal para entornos en la nube y clústeres modernos.

  Entre sus características principales se encuentran:

  - **Uso de contenedores Docker** como base principal para ejecutar aplicaciones Spark.
  - **Balanceo de carga automático y escalabilidad** en función de la demanda.
  - **Despliegue de pods (workers)** para la ejecución de tareas distribuidas.
  - **Soporte para GPUs y FPGAs**, facilitando su uso en aplicaciones que requieren cómputo acelerado.
  - **Uso de volúmenes persistentes** para almacenar datos intermedios en operaciones de shuffle.
  - **Modos de ejecución:**
    - **Client:** el **Driver** se ejecuta en la misma máquina donde se inicia la aplicación.
    - **Cluster:** el **Driver** se ejecuta dentro de un **Worker Node** gestionado por Kubernetes. Se puede habilitar el **modo supervise** para la recuperación automática en caso de fallos.
  - Parámetros de recursos al lanzar la aplicación:
    - **Driver**:
      - --spark.kubernetes.driver.request.cores
      - --spark.kubernetes.driver.limit.cores
    - **Executors**:
      - --spark.kubernetes.executor.request.cores
      - --spark.kubernetes.executor.limit.cores

  En entornos donde se prioriza la gestión de contenedores y la ejecución en la nube, Kubernetes se presenta como una de las mejores opciones para desplegar Spark, ofreciendo flexibilidad, resiliencia y eficiencia en la asignación de recursos.



### 6.3 Gestión de dependencias en Scala



Comenzamos con una introducción a los gestores de dependencias. Un **gestor de dependencias** es una herramienta esencial en el desarrollo de software que permite **añadir, priorizar y configurar** los artefactos que componen un proyecto. Estos artefactos pueden incluir **librerías, ficheros de configuración, paquetes y módulos**, entre otros.

El uso de un gestor de dependencias facilita la instalación, actualización y mantenimiento de las dependencias de un proyecto, asegurando la compatibilidad entre versiones y permitiendo la automatización del ciclo de vida del software. Además, estas herramientas pueden ser específicas para un lenguaje de programación o de **propósito general**, lo que permite integrarse en distintos entornos y facilitar el desarrollo y distribución de software.

Las principales tareas que realizan los gestores de dependencias incluyen:

- **Instalación de dependencias:** descarga e instalación de paquetes necesarios.
- **Resolución de dependencias:** garantiza la compatibilidad entre versiones de los distintos artefactos utilizados en el proyecto.
- **Actualización de dependencias:** simplifica la actualización de librerías y módulos sin afectar el funcionamiento del software.
- **Gestión de versiones:** permite reproducir entornos de ejecución asegurando la estabilidad del software.
- **Aislamiento de entornos:** facilita la independencia de cada proyecto evitando conflictos entre dependencias de distintas aplicaciones.

Ejemplos de gestores de dependencias populares incluyen:

- **npm** para **JavaScript**
- **pip** para **Python**
- **Composer** para **PHP**
- **Bundler** para **Ruby**
- **Maven** para **Java**
- **SBT** para **Scala**
- **Gradle** para **Android**



![image](assets/cm7vld4yr007u356zls7u7pei-INSD_PRDT_U3_Apartado7-3_Imagen25.jpg)



A continuación, se describen en detalle dos de los gestores de dependencias más utilizados en el desarrollo de software basado en Java y Scala: **Maven y SBT**.



- **Maven**  
  **Maven** es una de las herramientas más utilizadas en el desarrollo de software con **Java**, proporcionando un mecanismo estructurado para la **construcción, gestión de dependencias y distribución de proyectos**. Su uso facilita la automatización del proceso de compilación y empaquetado, reduciendo la complejidad del desarrollo.

  En Maven, la definición de un proyecto se centraliza en el archivo **pom.xml** (**Project Object Model**), el cual contiene distintas secciones clave:

  - **<project>**: define el **groupId, artifactId y version**, que identifican el proyecto de forma única.
  - **<properties>**: almacena constantes como versiones de dependencias utilizadas.
  - **<dependencies>**: especifica las librerías de las que depende el proyecto, indicando su **groupId, artifactId y version**.
  - **<build>**: contiene las especificaciones relacionadas con la **compilación, empaquetado y ejecución de pruebas**.
  - **<plugins>**: permite añadir funcionalidades adicionales durante el proceso de construcción del software.
  - **<repositories>**: define repositorios adicionales donde buscar librerías y artefactos.
  - **<profiles>**: configura diferentes perfiles de ejecución del proyecto, adaptándose a distintos entornos.

  **Comandos más comunes en Maven:**

  - **Clean**: elimina la carpeta **target** que contiene archivos generados en compilaciones anteriores.
  - **Compile**: compila el código fuente sin generar un JAR.
  - **Test**: ejecuta las pruebas unitarias definidas en el proyecto.
  - **Package**: compila, ejecuta pruebas y genera un archivo **JAR** con los binarios del proyecto.
  - **Install**: ejecuta **Package** y además instala el proyecto en el repositorio local.
  - **Deploy**: similar a **Install**, pero instala los artefactos en un repositorio remoto.
  - Los comandos en Maven pueden **combinarse** para realizar múltiples acciones en un solo paso. Por ejemplo, mvn clean install permite limpiar la carpeta de compilación y luego construir e instalar el proyecto localmente.

  **Repositorios de librerías más populares en Maven:**

  - **Maven Central:** [https://central.sonatype.com/](https://central.sonatype.com/)
  - **Maven Repository:**[https://mvnrepository.com/](https://mvnrepository.com/)

  Maven se ha convertido en un estándar en el ecosistema Java debido a su capacidad para gestionar proyectos de forma modular y escalable.
- **SBT (Simple Build Tool)**  
  **SBT (Simple Build Tool)** es el gestor de dependencias más utilizado en el ecosistema de **Scala**. Además de permitir la gestión de librerías, facilita tareas como la **compilación, empaquetado, pruebas y ejecución de código**.

  A diferencia de Maven, en SBT la configuración del proyecto se define mediante código Scala, lo que proporciona mayor flexibilidad y dinamismo en la gestión de dependencias y configuraciones.

  Una de sus características más destacadas es su capacidad de realizar **construcciones incrementales**, es decir, solo se recompilan aquellos archivos que han cambiado desde la última ejecución, optimizando así los tiempos de construcción del proyecto.

  **Principales archivos de configuración en SBT:**

  - **build.sbt** → Define las dependencias del proyecto, la configuración del compilador y tareas personalizadas.
  - **project**/build.properties → Especifica la versión de **SBT** que se debe utilizar.
  - **project/plugins.sbt** → Contiene extensiones y herramientas adicionales para mejorar el proceso de construcción del proyecto.

  **Comandos más comunes en SBT:**

  - **Compile**: compila el código fuente de manera incremental.
  - **Test**: ejecuta pruebas unitarias.
  - **Run**: ejecuta la clase principal sin necesidad de empaquetar el código en un JAR.
  - **Clean**: elimina los archivos compilados y los artefactos generados en ejecuciones previas.
  - **Package**: compila y empaqueta los binarios en un archivo **JAR**.
  - **Publish**: publica los artefactos en un repositorio remoto para ser utilizados por otros proyectos.
  - **Reload**: recarga la configuración del archivo **build.sbt** sin necesidad de reiniciar SBT.

  SBT es ampliamente utilizado en proyectos basados en Scala y Apache Spark, ya que se integra de manera nativa con estos entornos y permite una gestión eficiente de dependencias y configuración de compilación.



### 6.4 Despliegue de aplicaciones Spark



El despliegue de aplicaciones en **Apache Spark** es un proceso fundamental para ejecutar código distribuido en un clúster de procesamiento. Existen diferentes formas de desplegar una aplicación Spark, dependiendo del entorno y los requisitos específicos del proyecto. En términos generales, este proceso implica **definir, desarrollar y empaquetar el código en un archivo JAR**, que luego será ejecutado en un entorno distribuido.

Una aplicación Spark debe incluir un **punto de entrada**, generalmente definido en una **clase Main**, donde se inicializa al menos una instancia de **SparkSession**. Es importante que en esta configuración **no se especifique el Master**, ya que este se define en el momento de la ejecución dependiendo del gestor de recursos seleccionado.

A continuación, se presentan las principales formas de desplegar una aplicación en Apache Spark:



- **spark-submit**  
  La herramienta **spark-submit** es el mecanismo estándar para ejecutar aplicaciones en Apache Spark. Permite especificar detalles como el clúster donde se ejecutará, la cantidad de recursos asignados y el archivo JAR que contiene la aplicación. Su uso es clave para lanzar trabajos en entornos de producción o pruebas, facilitando el control sobre los parámetros de ejecución.

  En el siguiente subapartado lo describimos un poco más en detalle
- **Spark standalone API REST**  
  Para entornos que utilizan **Spark Standalone,** se puede emplear una API REST para gestionar el envío de trabajos. Spark ofrece una interfaz de administración que permite enviar tareas al clúster sin necesidad de utilizar la línea de comandos.

  Formato de la API REST:

  http://[host:port]/[version]/submissions/[action]

  Por ejemplo, para enviar un trabajo al gestor en localhost, se utilizaría:

  http://localhost:6066/v1/submissions/create
- **Spark-shell**  
  Para pruebas y desarrollo interactivo, Spark ofrece **spark-shell,** una interfaz interactiva que permite ejecutar código de forma incremental. Es especialmente útil cuando se desea probar fragmentos de código sin necesidad de empaquetar y desplegar una aplicación completa.
- **Ejecución de Main Class**  
  Si se desarrolla un proyecto en **Java o Scala,** la ejecución del código puede hacerse directamente llamando a la **MainClass** del programa. Para esto, el código debe incluir la creación de una **SparkSession**, especificando el Spark Master.

  Código de creación de SparkSession especificando Spark Master:



#### Sparksubmit



Como se ha comentado, **spark-submit** es la utilidad estándar de **Apache Spark** utilizada para **lanzar aplicaciones al clúster** y ejecutar código distribuido. Es la herramienta más común para desplegar aplicaciones en Spark, ya que permite especificar múltiples parámetros de configuración y adaptarse a distintos entornos de ejecución.

Este comando admite proyectos desarrollados en varios lenguajes compatibles con Spark, como **Scala, Java, Python y R**, proporcionando flexibilidad en la implementación de aplicaciones de análisis de datos y procesamiento distribuido.

El uso más simple de spark-submit sigue la siguiente estructura:



```ruby
spark-submit --class <AppMainClass> --master <master> <jar-file>
```



Donde:

- **--class** especifica la clase principal de la aplicación.
- **--master** indica el gestor de recursos donde se ejecutará la aplicación (**local, standalone, YARN, Mesos o Kubernetes**).
- **<jar-file>** es el archivo empaquetado que contiene el código de la aplicación.

**Ejemplo:**



```bat
spark-submit --class com.ejemplo.MainClass --master yarn --deploy-mode cluster mi-aplicacion.jar
```



#### Opciones adicionales en spark-submit



```bat
spark-submit --status [submission ID] --master <master>
```



Este comando es útil para monitorear la ejecución de trabajos en un entorno distribuido y verificar si una aplicación ha finalizado correctamente o sigue en proceso.



![image](assets/cm7vr99ed005c356z7w60j28i-INSD_PRDT_U3_Apartado7-4-1_Imagen30.jpg)



#### History server



Apache Spark proporciona una Web UI para el monitoreo de aplicaciones en ejecución. Esta interfaz está disponible en la URL:

http://<driver-node>:4040

y permite visualizar métricas en tiempo real sobre la ejecución de los procesos. Sin embargo, esta interfaz se ejecuta dentro del mismo **Driver**, lo que significa que las estadísticas de ejecución **se almacenan en memoria** y **se pierden una vez que el Driver se detiene**.

Para superar esta limitación y poder consultar la información de aplicaciones finalizadas, **Spark History Server** proporciona una solución de almacenamiento persistente y visualización de logs históricos.



#### Funcionamiento de Spark History Server
El **Spark History Server** consta de dos procesos principales:

1. Para mantener registros de ejecución después de que una aplicación haya finalizado, es necesario configurar el **Spark Driver** para que guarde las estadísticas en **HDFS** en lugar de solo en memoria. Esto se hace habilitando la siguiente configuración en Spark:

   spark.eventLog.enabled: true

   spark.eventLog.dir: hdfs://namenode/shared/spark-logs

   Con esta configuración, cada ejecución de Spark almacenará su historial en el directorio especificado dentro del sistema de archivos distribuido.
2. Una vez almacenados los registros de ejecución en HDFS, se puede levantar el **History Server** para visualizar las aplicaciones que se han ejecutado. Para ello, se usa el siguiente comando:

   sbin/start-history-server.sh

   Una vez en funcionamiento, la interfaz de **Spark History Server** estará disponible en la siguiente URL:

   http://<server-url>:18080

   Esto permitirá acceder a los registros históricos y analizar aplicaciones ya finalizadas.

   Para garantizar que History Server pueda acceder a los logs almacenados, se debe configurar la siguiente propiedad:

   spark.history.fs.logDirectory: hdfs://namenode/shared/spark-logs

   Esta propiedad define el directorio donde se encuentran los archivos de logs que serán cargados y visualizados en la interfaz web.
3. ![image](assets/cm7vrblq20076356zg40jv67a-step3-INSD_PRDT_U3_Apartado7-4-2_Imagen31.jpg)



#### ¿Cómo cancelar un Job o App de Spark?



En Apache Spark, es posible detener la ejecución de un Job o una aplicación completa a través de diferentes métodos, dependiendo del entorno de ejecución. La cancelación de tareas puede ser necesaria cuando una aplicación está consumiendo demasiados recursos, cuando se ha detectado un error en el código o simplemente cuando se desea finalizar un proceso en ejecución.

1. Cuando se ejecuta una aplicación Spark, el **Spark Driver UI** proporciona una interfaz visual donde se pueden monitorear los Jobs en ejecución. En la descripción de cada Job, aparece la opción **"Kill"**, que permite finalizar la ejecución de la tarea correspondiente de manera inmediata.
2. Si la aplicación está ejecutándose en modo clúster bajo un gestor de recursos como **Spark Standalone**, la interfaz del **Spark Master UI** también permite cancelar aplicaciones activas. Junto al **Submission ID** de cada aplicación en ejecución, se encuentra un **botón Kill**, el cual detiene la ejecución de la aplicación de forma controlada.
3. Desde la línea de comandos, también es posible detener una aplicación Spark utilizando **spark-submit** con la opción --kill. La sintaxis para cancelar una aplicación específica es la siguiente:

   spark-submit --kill [submission ID] --master [spark://…]

   Aquí, [submission ID] es el identificador de la aplicación en ejecución y [spark://…] es la dirección del **Spark Master** que gestiona los recursos del clúster.
4. En algunos casos, puede ser necesario cancelar un Job directamente desde el código. Para esto, se pueden utilizar los métodos **setJobGroup** y **cancelJobGroup** del objeto **SparkContext**. Estos métodos permiten definir un grupo de Jobs y cancelarlos de manera programada.

   Ejemplo en Scala:

   val sc = SparkContext.getOrCreate()

   // Asigna un grupo a un Job

   sc.setJobGroup("grupo1", "Ejemplo de cancelación programada")

   // Cancela todos los Jobs asociados al grupo "grupo1"

   sc.cancelJobGroup("grupo1")

   Este método es útil cuando se quiere detener procesos en ejecución desde dentro de la propia aplicación, sin necesidad de usar la interfaz web o la línea de comandos.
5. ![image](assets/cm7vrgfsj00fc356zgfkb2nhh-step5-INSD_PRDT_U3_Apartado7-4-3_Imagen32.jpg)
   En resumen: Apache Spark ofrece múltiples formas de cancelar Jobs o aplicaciones en ejecución, ya sea a través de la **Web UI del Driver o del Master,** utilizando **spark-submit,** o incluso mediante código dentro de la propia aplicación.



### 6.5 Planificación y gestión de tareas en Spark



En un entorno **multiusuario**, una aplicación de Apache Spark puede ejecutar varias consultas en paralelo desde una misma instancia de **SparkContext**. Cada consulta o usuario que envía una tarea a Spark es procesado en un **hilo de ejecución independiente**, lo que permite una ejecución concurrente de múltiples cargas de trabajo dentro de la misma aplicación.



- **Modelo de Planificación por Defecto: FIFO**  
  Por defecto, el **planificador de Spark** sigue un modelo basado en una cola **FIFO (First In, First Out)**. Esto significa que:

  - Las consultas se encolan en orden de llegada.
  - La consulta que está en la **cabeza de la cola** obtiene prioridad absoluta sobre todos los recursos disponibles del clúster.
  - Si esta consulta no utiliza todos los recursos del clúster, las consultas posteriores pueden aprovechar los recursos sobrantes.
  - En el caso de que la consulta prioritaria sea **muy pesada en consumo de recursos**, las consultas más ligeras pueden experimentar retrasos significativos, ya que deben esperar a que la primera consulta finalice o libere recursos.

  Este modelo puede ser adecuado en ciertos escenarios, pero no siempre es óptimo cuando se requiere una distribución más equitativa de los recursos entre múltiples consultas.
- **Planificación Equitativa: Fair Scheduler**  
  Para mejorar la distribución de los recursos y evitar que una única consulta monopolice el clúster, **Spark permite configurar un planificador equitativo, conocido como Fair Scheduler**.

  Este modelo sigue un enfoque de **"Round Robin" (por turnos)**, donde los recursos se distribuyen de manera más equitativa entre todas las consultas en ejecución. Con esta estrategia:

  - Las consultas ligeras pueden avanzar y ejecutarse sin necesidad de esperar la finalización de consultas pesadas.
  - Se logra un mejor aprovechamiento de los recursos disponibles, evitando bloqueos prolongados en la ejecución de tareas.
  - Se minimizan los tiempos de espera y se optimiza la experiencia en entornos compartidos con múltiples usuarios.

  El **Fair Scheduler** es compatible con los principales gestores de recursos soportados por Apache Spark, incluyendo **Standalone, YARN, Mesos y Kubernetes (K8s)**, lo que lo convierte en una opción flexible para mejorar la planificación de tareas en distintos entornos de despliegue.
- **Pools de Planificación en Apache Spark**  
  El **planificador Fair** en Apache Spark permite agrupar consultas en **pools**, lo que proporciona un mayor control sobre la distribución de recursos dentro de una aplicación. Gracias a este enfoque, es posible definir **colas de prioridad** y gestionar los recursos de manera más eficiente, evitando que ciertas tareas monopolicen el clúster.

  Uno de los principales beneficios de los pools de planificación es la capacidad de asignar recursos de forma **equitativa entre diferentes usuarios**, sin importar cuántas consultas concurrentes ejecute cada uno. De esta manera, se garantiza que ningún usuario acapare los recursos y se mejora la experiencia en entornos multiusuario.

  El modelo de planificación de pools en Spark está basado en el **planificador Fair de Hadoop,** lo que permite su integración con infraestructuras distribuidas que utilizan este sistema de gestión de recursos.
- **Funcionamiento de los Pools de Planificación**  
  Por defecto, si no se modifica la configuración, todas las consultas ejecutadas en una aplicación Spark son enviadas a un **pool por defecto**. Sin embargo, Spark permite asignar tareas a pools específicos dentro de una aplicación. Para definir un pool para un hilo en particular, se puede utilizar el siguiente comando en **SparkContext**:

  sc.setLocalProperty("spark.scheduler.pool", "pool1")

  Si en algún momento se necesita regresar al **pool por defecto**, basta con ejecutar:

  sc.setLocalProperty("spark.scheduler.pool", null)
- **Distribución de Recursos en los Pools**  
  Por defecto, todos los pools reciben la **misma cantidad de recursos** del clúster. Sin embargo, dentro de cada pool, las consultas se ejecutan siguiendo un modelo **FIFO** (First In, First Out). Esto significa que las consultas más antiguas tienen prioridad sobre las más recientes dentro de un mismo pool.

  No obstante, Spark permite modificar este comportamiento mediante la **configuración de pools**, lo que se realiza a través del archivo de configuración **fairscheduler.xml**, ubicado en el **classpath**, o mediante la propiedad global:

  spark.scheduler.allocation.file

  Dentro de este archivo de configuración, se pueden definir diferentes parámetros para los pools de ejecución:

  - **schedulingMode**: Define si la ejecución dentro del pool será en **FIFO** (prioridad por orden de llegada) o en **FAIR** (distribución equitativa de recursos).
  - **weight**: Permite asignar una **mayor prioridad a ciertos pools** asignándoles un peso mayor. Un pool con un peso más alto recibirá más recursos en comparación con otros.
  - **minShare:** Especifica el **mínimo número de cores** que el planificador debe asignar a un pool, garantizando que siempre tenga una cantidad base de recursos disponibles.



#### Planificación entre apps



En Apache Spark, cada aplicación en ejecución obtiene un **conjunto independiente de ejecutores**, los cuales son procesos **JVM (Java Virtual Machine)** encargados de ejecutar tareas y almacenar datos en memoria. Sin embargo, en **entornos compartidos**, donde múltiples aplicaciones se ejecutan simultáneamente en un mismo clúster, la asignación de recursos entre aplicaciones se vuelve un factor crítico que puede afectar el rendimiento global del sistema.

Para administrar eficientemente los recursos disponibles, Spark ofrece diferentes estrategias de planificación entre aplicaciones, permitiendo definir límites en el uso de CPU y memoria para evitar la sobresaturación del entorno.



- **Particionamiento Estático de Recursos**  
  La forma más sencilla de distribuir los recursos en un entorno compartido es mediante el **particionamiento estático**. En este enfoque, cada aplicación bloquea una **cantidad fija de recursos**, evitando que otras aplicaciones puedan consumir más allá de su límite asignado. Dependiendo del gestor de recursos utilizado, los parámetros de configuración varían:

  - **Spark Standalone:** spark.cores.max Este parámetro define el número máximo de cores que una aplicación puede utilizar en un clúster Spark Standalone.

  - **Apache Mesos:** spark.cores.max Similar a Standalone, en Mesos este parámetro fija el número máximo de cores disponibles para una aplicación específica.

  - **YARN:** spark.executor.instances spark.executor.cores En entornos YARN, la planificación de recursos se gestiona especificando el número de **executors** (spark.executor.instances) y la cantidad de **cores por executor** (spark.executor.cores).

  Este modelo garantiza una distribución predecible de los recursos, pero puede generar subutilización si las aplicaciones no consumen toda su asignación.
- **Compartición Dinámica de Cores en Mesos**  
  En Apache Mesos, además del particionamiento estático, existe la opción de habilitar una **compartición dinámica de cores**. En este caso, los cores asignados a una aplicación pueden **prestarse temporalmente a otras aplicaciones** si no están siendo utilizados activamente.

  - La cantidad de memoria asignada a cada aplicación sigue siendo fija, definida por: spark.executor.memory
  - Sin embargo, si una aplicación no tiene tareas en ejecución, **Mesos puede ceder sus cores a otras aplicaciones** que los necesiten en ese momento.
  - Cuando la aplicación original reanuda la ejecución de tareas, puede recuperar sus cores, aunque esto introduce **una latencia** en el proceso de reasignación de recursos.

  Este enfoque mejora la utilización global del clúster, ya que permite un uso más flexible de los recursos. Sin embargo, introduce cierta imprevisibilidad en el rendimiento de las aplicaciones, ya que el tiempo de recuperación de los cores prestados puede afectar la ejecución de nuevas tareas.



#### Dynamic allocation



La **asignación dinámica de recursos** (**Dynamic Allocation**) es un mecanismo en Apache Spark que permite ajustar automáticamente la cantidad de recursos utilizados por una aplicación en función de la carga de trabajo. En lugar de asignar una cantidad fija de **Executors** desde el inicio, Spark puede **escalar dinámicamente el número de Executors**, añadiendo o liberando recursos según sea necesario.

Este enfoque optimiza la utilización del clúster, permitiendo que los recursos no utilizados sean devueltos al gestor de recursos y reasignados a otras aplicaciones. Cuando una aplicación requiere más capacidad de cómputo, solicita nuevamente los recursos y los incorpora a la ejecución.



- **Estado por Defecto y Requisitos**  
  Por defecto, la asignación dinámica de recursos está desactivada en los principales gestores de recursos compatibles con Spark:

  - Standalone
  - YARN
  - Mesos
  - Kubernetes (K8s)

  Para habilitar esta funcionalidad, se deben cumplir ciertos requisitos técnicos. Uno de los aspectos clave es que los Executors no deben borrar los archivos de shuffle, ya que Spark necesita conservar estos datos para garantizar la consistencia en la ejecución.
- **Opciones para Activar Dynamic Allocation**  
  Existen dos formas principales de activar la asignación dinámica de recursos en Spark:

  1. **Modo estándar con seguimiento interno del shuffle:** spark.dynamicAllocation.enabled = true spark.dynamicAllocation.shuffleTracking.enabled = true Este método permite a Spark gestionar la asignación dinámica sin necesidad de un servicio de shuffle externo.

  1. **Modo con servicio de Shuffle externo:** spark.dynamicAllocation.enabled = true spark.shuffle.service.enabled = true En este caso, se requiere un **servicio de shuffle externo** que gestione los datos intermedios generados por las tareas de Spark. Un ejemplo en **Mesos** es el servicio que se inicia con: start-mesos-shuffle-service.sh Este comando debe ejecutarse en cada nodo **Mesos Worker** para permitir la correcta redistribución de recursos.
- **Parámetros para la Adquisición de Recursos**  
  Cuando una aplicación Spark necesita más recursos, se van añadiendo **Executors de forma progresiva**, aumentando su número de manera exponencial en **potencias de 2** (2, 4, 8, 16, etc.).

  Algunos parámetros clave para controlar la expansión de los recursos incluyen:

  - **spark.dynamicAllocation.schedulerBacklogTimeout = 1s**
    - Si hay tareas pendientes en la cola durante **más de 1 segundo**, Spark solicita más **Executors**.
  - **spark.dynamicAllocation.sustainedSchedulerBacklogTimeout**
    - Permite ajustar el tiempo que Spark espera antes de solicitar nuevos recursos adicionales.
- **Parámetros para la Liberación de Recursos**  
  Cuando una aplicación Spark ya no necesita ciertos recursos, los devuelve al gestor para evitar desperdicio. La liberación de **Executors** sigue estas reglas:

  - **spark.dynamicAllocation.executorIdleTimeout = 60s**
    - Si un **Executor** permanece inactivo durante **60 segundos**, Spark lo apaga.
  - **spark.dynamicAllocation.cachedExecutorIdleTimeout = infinito**
    - Evita que Spark libere **Executors** que almacenan datos en caché.
- **Otros Parámetros de Configuración**  
  - **spark.dynamicAllocation.maxExecutors = infinito**
    - No hay un límite máximo en la cantidad de **Executors** que Spark puede solicitar.
  - **spark.dynamicAllocation.minExecutors = 0**
    - Permite que una aplicación se ejecute sin ningún **Executor** hasta que necesite recursos.
  - **spark.dynamicAllocation.initialExecutors**
    - Define cuántos **Executors** iniciales se asignan al comienzo de la ejecución.



### 6.6 Ejercicios práctico



En este subcapítulo realizaremos algunos ejercicios para poner en práctica los conceptos vistos sobre despliegue y planificación en spark.



#### Ejercicio de Spark standalone



Comenzaremos configurando un entorno spark en modo standalone. Para ello debemos ejecutar los siguientes comandos:



```bash
bigdata> cd /home/bigdata/spark-3.3.3-bin-hadoop3/
bigdata> ls sbin/
bigdata> sbin/start-master.sh --help
bigdata> cat conf/spark-defaults.conf.template
bigdata> tail logs/spark-bigdata-org.apache.spark.deploy.master.Master-1-bigdatapc.out
firefox> http://10.0.2.15:8080
bigdata> cat conf/workers.template
bigdata> sbin/start-slave.sh spark://bigdatapc:7077
bigdata> sbin/stop-slave.sh
bigdata> sbin/start-slave.sh spark://bigdatapc:7077 --cores 2 --memory 1g
bigdata> cat conf/spark-env.sh.template
firefox> https://spark.apache.org/docs/3.3.4/spark-standalone.html#cluster-launch-scripts
bigdata> vi conf/spark-env.sh
			SPARK_WORKER_CORES=2
			SPARK_WORKER_INSTANCES=2
			SPARK_WORKER_MEMORY=1g
bigdata> sbin/start-slaves.sh spark://bigdatapc:7077
bigdata> jps
```



Seguidamente conectamos Spark Driver de la Shell al Gestor de recursos Standalone



```bat
bigdata> bin/spark-shell --master spark://bigdatapc:7077 --driver-memory 1G --executor-memory 1G --total-executor-cores 2 --executor-cores 2
spark> sc.isLocal
spark> sc.parallelize(Range(0, 100)).filter(_%2==0).collect()
spark> :q
```



Una vez hemos configurado el entorno los ejercicios a realizar son los siguientes:



1. **EJERCICIO 1:** Levanta una aplicación shell que utilice un core de cada worker
2. **EJERCICIO 2:** Lanza los siguientes comandos y explica lo que ocurre



```bat
bigdata> bin/spark-shell --master spark://bigdatapc:7077 --driver-memory 1G --executor-memory 16G --total-executor-cores 8 --executor-cores 2
spark> sc.parallelize(Range(0, 100)).filter(_%2==0).collect()
```



3. **EJERCICIO 3:** Lanza los siguientes comandos y explica lo que ocurre



```bat
bigdata> bin/spark-shell --master spark://bigdatapc:7077 --driver-memory 1G --executor-memory 1G --total-executor-cores 8 --executor-cores 2
spark> sc.parallelize(Range(0, 100)).filter(_%2==0).collect()
```



4. **EJERCICIO 4:**

   Lee [https://spark.apache.org/docs/3.3.4/configuration.html#scheduling](https://spark.apache.org/docs/3.3.4/configuration.html#scheduling) (Parámetro spark.scheduler.minRegisteredResourcesRatio)

   ¿Qué ocurre cuando lanzo una shell con --conf spark.scheduler.minRegisteredResourcesRatio=1.0?



```bat
bigdata> bin/spark-shell --master spark://bigdatapc:7077 --driver-memory 1G --executor-memory 16G --total-executor-cores 8 --executor-cores 2 --conf spark.scheduler.minRegisteredResourcesRatio=1.0
```



5. **EJERCICIO 5:**¿Qué pasará si lanzo una shell con --executor-memory 1G y --total-executor-cores 6?



```bat
bigdata> bin/spark-shell --master spark://bigdatapc:7077 --driver-memory 1G --executor-memory 1G --total-executor-cores 6 --executor-cores 2 --conf spark.scheduler.minRegisteredResourcesRatio=1.0
```



6. **EJERCICIO 6:** ¿Qué pasará si lanzo una shell con --conf spark.scheduler.minRegisteredResourcesRatio=0.5?



```bat
bigdata> bin/spark-shell --master spark://bigdatapc:7077 --driver-memory 1G --executor-memory 1G --total-executor-cores 6 --executor-cores 2 --conf spark.scheduler.minRegisteredResourcesRatio=0.5 
```



El siguiente video comenta la resolución de los ejercicios de este apartado:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652188_1/scormcontent/assets/INSD_PRDT_U3_Apartado7-6-1_Video6Sparkstandalone.mp4?v=1)



#### Ejercicio de Dynamic allocation



Se habilita la asignación dinámica de recursos en Spark, permitiendo escalar automáticamente los ejecutores en función de la carga de trabajo.

La solución en este caso sería:



```bat
bin/spark-shell --master spark://bigdatapc:7077 --driver-memory 1G --executor-memory 1G --total-executor-cores 4 --executor-cores 2 --conf spark.dynamicAllocation.enabled=true --conf spark.dynamicAllocation.shuffleTracking.enabled=true --conf spark.dynamicAllocation.executorIdleTimeout=60s --conf spark.dynamicAllocation.minExecutors=0 --conf spark.dynamicAllocation.initialExecutors=0
spark> sc.parallelize(Range(0, 100000000), 64).filter(_%2==0).collect()
```



#### Ejercicio de Scheduler pools



Se configuran pools de planificación en Spark para gestionar la prioridad de ejecución de tareas en entornos multiusuario.



```scala
bigdata> bin/spark-shell --master spark://bigdatapc:7077 --driver-memory 1G --executor-memory 1G --total-executor-cores 4 --executor-cores 2
import scala.concurrent._
import scala.concurrent.ExecutionContext.Implicits.global
sc.setLocalProperty("spark.scheduler.pool", null)
Future{
	sc.setLocalProperty("spark.scheduler.pool", null)
	sc.parallelize(Range(0, 100), 40).mapPartitions{x => Thread.sleep(1000); x}.filter(_%2==0).map(_*2).distinct().mapPartitions{x => Thread.sleep(1000); x}.collect()
}.onSuccess{case array => println(array.mkString(",")); println("Job 1 Finished")}
Thread.sleep(100)
Future{
	sc.setLocalProperty("spark.scheduler.pool", null)
	sc.parallelize(Range(0, 100), 40).mapPartitions{x => Thread.sleep(1000); x}.filter(_%2==1).map(_*2).distinct().collect()
}.onSuccess{case array => println(array.mkString(",")); println("Job 2 Finished")}


bigdata> bin/spark-shell --master spark://bigdatapc:7077 --deploy-mode client --driver-memory 1G --executor-memory 1G --total-executor-cores 4 --executor-cores 2 --conf spark.scheduler.mode=FAIR
spark> import scala.concurrent._
spark> import scala.concurrent.ExecutionContext.Implicits.global
spark> Future{
	sc.setLocalProperty("spark.scheduler.pool", "production")
	sc.parallelize(Range(0, 100), 40).mapPartitions{x => Thread.sleep(1000); x}.filter(_%2==0).map(_*2).distinct().mapPartitions{x => Thread.sleep(1000); x}.collect()
}.onSuccess{case array => println(array.mkString(",")); println("Job 1 Finished")}
spark> Thread.sleep(100)
spark> Future{
	sc.setLocalProperty("spark.scheduler.pool", "test")
	sc.parallelize(Range(0, 100), 40).mapPartitions{x => Thread.sleep(1000); x}.filter(_%2==1).map(_*2).distinct().collect()
}.onSuccess{case array => println(array.mkString(",")); println("Job 2 Finished")}
```



Este código inicia **Spark Shell** en modo **Standalone** con un **Master en spark://bigdatapc:7077**, asignando **1GB de memoria** al **Driver** y los **Executors**, con un total de **4 cores** distribuidos en **2 por Executor**. Luego, se ejecutan dos tareas en paralelo utilizando **Scala Futures**, procesando números del 0 al 99 con particiones y pausas para simular carga. En la primera ejecución, **sin planificación explícita**, Spark usa la planificación por defecto (**FIFO**). En la segunda ejecución, se inicia Spark con el planificador **FAIR**, dividiendo las tareas en **pools de prioridad** ("production" y "test"), asegurando que ambas tareas compartan los recursos de manera más equitativa. Esto permite gestionar múltiples trabajos simultáneos de forma eficiente en entornos multiusuario. Recordad que en **Scala**, un **Future** representa una computación que **se ejecuta en segundo plano y devuelve un resultado en algún momento en el futuro**. Es una herramienta clave para la **programación asíncrona y concurrente**, permitiendo ejecutar tareas sin bloquear el flujo principal del programa.



#### Ejercicio de history server



El Spark History Server es una herramienta esencial para el monitoreo y análisis de aplicaciones ejecutadas en Apache Spark, permitiendo visualizar métricas y registros de trabajos pasados incluso después de que han finalizado. Dado que la interfaz web estándar de Spark solo muestra información en tiempo real mientras el Driver está en ejecución, el History Server almacena los logs de ejecución en un sistema de archivos distribuido, como HDFS, asegurando su persistencia para futuras consultas. En este ejercicio, primero se configura HDFS para almacenar los registros de Spark en la ruta /shared/spark-logs, luego se inicia el History Server y, finalmente, se ejecuta Spark Shell con la configuración adecuada para habilitar la captura de logs en HDFS, permitiendo su análisis a través de la interfaz web en [http://10.0.2.15:18080](http://10.0.2.15:18080)

// History server ([https://spark.apache.org/docs/3.3.4/monitoring.html#viewing-after-the-fact](https://spark.apache.org/docs/3.3.4/monitoring.html#viewing-after-the-fact))



7. **EJERCICIO 7:** Arranca HDFS y genera la ruta /shared/spark-logs con una única instrucción



```bash
bigdata> cd /home/bigdata/hadoop-3.3.6/
bigdata> sbin/start-dfs.sh
bigdata> bin/hdfs dfs -mkdir -p /shared/spark-logs


bigdata> /home/bigdata/spark-3.3.3-bin-hadoop3
bigdata> cp conf/spark-defaults.conf.template conf/spark-defaults.conf
bigdata> vi conf/spark-defaults.conf
			spark.history.fs.logDirectory   hdfs://localhost:9000/shared/spark-logs
bigdata> sbin/start-history-server.sh
firefox> http://10.0.2.15:18080
```



8. **EJERCICIO 8:**¿Cómo arrancarías una shell de Spark para que utilice el history server que se ha lanzado?



```bat
bigdata> bin/spark-shell --master spark://bigdatapc:7077 --driver-memory 1G --executor-memory 1G --total-executor-cores 4 --executor-cores 2 --conf spark.eventLog.enabled=true --conf spark.eventLog.dir=hdfs://localhost:9000/shared/spark-logs
```



Recuerda al terminar parar los procesos de Spark:



```bash
bigdata> sbin/stop-history-server.sh
bigdata> sbin/stop-all.sh
```



#### Ejercicio De Sparksubmit y API REST



En este ejemplo se configura y levanta **Apache Spark en modo Standalone** con la **API REST activada**, permitiendo la gestión de aplicaciones a través de solicitudes HTTP. Primero, se modifica la configuración en spark-defaults.conf para habilitar la API REST, luego se inicia el **Master** y los **Workers** del clúster. A continuación, se instala **Git** y **Maven**, se clona un repositorio con una aplicación Spark de ejemplo (spark-very-basic-server), y se compila el código con Maven para generar un **JAR ejecutable**. Finalmente, se usa **spark-submit** para desplegar la aplicación en el clúster, asignando recursos y ejecutándola en **modo clúster**, permitiendo la interacción con el servicio a través del puerto 9070



```bash
// Levantar Spark Standalone con API Rest activada
bigdata> cd /home/bigdata/spark-3.3.3-bin-hadoop3/
bigdata> cp conf/spark-defaults.conf.template conf/spark-defaults.conf
bigdata> gedit conf/spark-defaults.conf
			spark.master.rest.enabled	true
bigdata> sbin/start-master.sh
bigdata> sbin/start-slaves.sh spark://bigdatapc:7077

// Spark-Submit para desplegar aplicación empaquetada en un fichoer JAR
bigdata> sudo apt-get install git
bigdata> sudo apt-get install maven
bigdata> git clone https://github.com/mafernandez-stratio/spark-very-basic-server.git
bigdata> cd spark-very-basic-server/
bigdata> gedit pom.xml
bigdata> gedit src/main/scala/examples/batch/VowelsCounter.scala
bigdata> mvn package
bigdata> mvn clean compile assembly:single
bigdata> cd ../spark-3.3.3-bin-hadoop3/
bigdata> bin/spark-submit --class examples.batch.VowelsCounter --master spark://bigdatapc:7077 --deploy-mode cluster --driver-memory 1G --driver-cores 2 --executor-memory 1G --total-executor-cores 2 --executor-cores 2 /home/bigdata/spark-very-basic-server/target/very-basic-server-0.1-SNAPSHOT-jar-with-dependencies.jar 9070
bigdata> nc localhost 9070
```



Para detener una aplicación en Spark Standalone, se puede utilizar la API REST enviando una solicitud POST con el Submission ID, o desde la Web UI del Master, donde se encuentra el botón Kill en la sección de aplicaciones en ejecución. También es posible cancelar programáticamente la aplicación VowelsCounter tras 30 segundos, utilizando un Future que llama a sc.cancelJobGroup. En modo clúster, si el Driver falla, Spark lo reinicia automáticamente, lo que puede causar la reaparición del proceso. Para evitar esto, se recomienda manejar excepciones, utilizando Try para capturar errores y evitar reinicios inesperados. Finalmente, se pueden detener todos los procesos con sbin/stop-all.sh

// Parar aplicación utilizando la API Rest

curl -X POST http://bigdatapc:6066/v1/submissions/kill/<Submission ID>

//¿Cómo cancelarías la aplicación VowelsCounter desde la WebUI del Master de Spark Standalone?

//Botón kill al lado del Application ID dentro de la sección Running Applications



1. **Ejercicio 1:** ¿Cómo cancelarías la aplicación VowelsCounter programáticamente a los 30 segundos modificando el código?



```scala
import scala.concurrent._
val MyJobGroup = "VowelsCounter"
implicit val ec: scala.concurrent.ExecutionContext = scala.concurrent.ExecutionContext.global
Future {
  	Thread.sleep(30000)
	sc.cancelJobGroup(MyJobGroup)
}
sc.setJobGroup(MyJobGroup, "App Counting Vowels")
// Añadir Thread.sleep(60000) en un mapPartitions para result
val result = resultRDD.mapPartitions{iter => Thread.sleep(60000); iter}.collect().mkString("; ")
```



2. **Ejercicio 2:** Observa lo que ocurre con el driver en la UI de Spark Standalone. ¿Por qué se levanta otro driver?

   Modo Cluster: Vuelve a levatar el Driver si se produce una excepción fatal en el Driver



En **modo clúster**, Spark está diseñado para **reiniciar automáticamente el Driver** si detecta una **excepción fatal**, garantizando la continuidad de la aplicación. Esto ocurre porque el clúster asume que el fallo fue inesperado y trata de **recuperar el estado de ejecución**, lanzando un nuevo Driver para gestionar la aplicación. Sin embargo, este comportamiento puede generar reinicios infinitos si la causa del error no se corrige, por lo que es recomendable **manejar excepciones adecuadamente** para evitar reinicios innecesarios



3. **Ejercicio 3:** ¿Cómo lo solucionarías?
   Añadir tratamiento de excepciones para devolver error



```scala
import scala.util._
val result = Try(resultRDD.mapPartitions{iter => Thread.sleep(60000); iter}.collect().mkString("; ")) match {
	case Success(value) => value
    case Failure(exception) => exception.getMessage
}

bigdata> sbin/stop-all.sh
```



## 7. Conclusiones



### 7.1 Conclusiones de la unidad



Tras haber leído el contenido de esta unidad y haber realizado los ejercicios prácticos, el alumno debería ser capaz de:

- **Comprender** las razones que motivaron la creación de **Apache Spark**
- **Conocer** la arquitectura distribuida de Spark, identificando sus principales componentes y su interacción en el procesamiento de datos.
- **Diferenciar Spark y Map Reduce**.
- **Dominar** el uso de **RDDs**, **DAGs**, transformaciones y acciones en Spark de una forma práctica
- **Conocer conceptos como** como paralelización, persistencia de datos y gestión de tareas y aplicaciones en Spark dentro de un entorno distribuido, explorando opciones de despliegue y asignación de recursos.

El conocimiento de Spark es fundamental en el ámbito del **Big Data** y se recomienda que el alumno practique con los ejemplos para afianzar su comprensión. Es clave desarrollar ejercicios en los que se manipulen **RDDs**, se implementen transformaciones y se realicen optimizaciones en la ejecución de procesos distribuidos.

Si al llegar a este punto:

- **Te sientes confiado** explicando qué es Spark, cómo se diferencia de Hadoop y su relevancia en el procesamiento de datos masivos.
- **Comprendes la arquitectura** de Spark y el funcionamiento de sus principales componentes.
- **Has asimilado** los ejercicios prácticos y puedes aplicarlos en escenarios reales.

Entonces, se puede decir que has superado las expectativas de esta unidad y posees la base necesaria para enfrentarte con éxito a las siguientes unidades del curso, en las cuales se verán otras funcionalidades de spark.
