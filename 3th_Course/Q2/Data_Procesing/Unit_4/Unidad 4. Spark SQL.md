# Unidad 4. Spark SQL.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Spark Sql: Contextualización](#2-spark-sql-contextualización)
  - [2.1 Introducción](#21-introducción)
  - [2.2 ¿Qué es Spark SQL?](#22-qué-es-spark-sql)
  - [2.3 ¿Por qué surge Spark SQL?](#23-por-qué-surge-spark-sql)
  - [2.4 Características de Spark SQL](#24-características-de-spark-sql)
  - [2.5 Spark SQL vs Bases de datos relacionales](#25-spark-sql-vs-bases-de-datos-relacionales)
  - [2.6 ¿Qué no es Spark SQL?](#26-qué-no-es-spark-sql)
  - [2.7 Casos de uso](#27-casos-de-uso)
- [3. Apis De Spark Y Modelos De Datos](#3-apis-de-spark-y-modelos-de-datos)
  - [3.1 Introducción](#31-introducción)
  - [3.2 ¿Por qué surgen?](#32-por-qué-surgen)
  - [3.3 Datasets: Concepto](#33-datasets-concepto)
  - [3.4 DataFrame: Concepto](#34-dataframe-concepto)
  - [3.5 Dataset vs DataFrame. Evolución](#35-dataset-vs-dataframe-evolución)
  - [3.6 Diferencias en el Manejo de Errores](#36-diferencias-en-el-manejo-de-errores)
  - [3.7 Schema RDD: La API de RDDs en Spark](#37-schema-rdd-la-api-de-rdds-en-spark)
  - [3.8 Comparación de Rendimiento](#38-comparación-de-rendimiento)
- [4. Consultas En Spark Sql](#4-consultas-en-spark-sql)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Creación y Manipulación de Datasets en Spark SQL](#42-creación-y-manipulación-de-datasets-en-spark-sql)
  - [4.3 Manejo de Datos con Spark SQL y DataFrames](#43-manejo-de-datos-con-spark-sql-y-dataframes)
  - [4.4 Funciones Definidas por el Usuario en Spark SQL (UDFs y UDAFs)](#44-funciones-definidas-por-el-usuario-en-spark-sql-udfs-y-udafs)
- [5. Sparksession, Optimización Y Performance En Spark Sql](#5-sparksession-optimización-y-performance-en-spark-sql)
  - [5.1 Introducción](#51-introducción)
  - [5.2 SparkSession](#52-sparksession)
  - [5.3 Catalyst (Optimizador en Spark SQL)](#53-catalyst-optimizador-en-spark-sql)
  - [5.4 Ejemplos genéricos usando SparkSession](#54-ejemplos-genéricos-usando-sparksession)
- [6. Conectores](#6-conectores)
  - [6.1 Introducción](#61-introducción)
  - [6.2 Cassandra](#62-cassandra)
  - [6.3 Amazon S3](#63-amazon-s3)
  - [6.4 MongoDB](#64-mongodb)
  - [6.5 Json](#65-json)
- [7. Ejemplos](#7-ejemplos)
  - [7.1 Introducción](#71-introducción)
  - [7.2 Ejemplo 1: Exploración y Manipulación de Datos con DataFrames en Spark](#72-ejemplo-1-exploración-y-manipulación-de-datos-con-dataframes-en-spark)
  - [7.3 Ejemplo 2: Exploración, análisis y manipulación de datos](#73-ejemplo-2-exploración-análisis-y-manipulación-de-datos)
  - [7.4 Ejemplo 3: Manipulación general de datos](#74-ejemplo-3-manipulación-general-de-datos)
- [8. Conclusiones](#8-conclusiones)
  - [8.1 Conclusiones de la unidad](#81-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad se abordará Spark SQL, un módulo del framework Apache Spark diseñado para el procesamiento estructurado de datos. Se analizará su importancia dentro del ecosistema de Big Data, su evolución y su impacto en la ejecución de consultas distribuidas con un alto rendimiento. Spark SQL combina la potencia del procesamiento en memoria de Spark con la expresividad y familiaridad del lenguaje SQL, facilitando su integración con sistemas tradicionales de bases de datos y herramientas de análisis de datos.

A lo largo de esta unidad, exploraremos los componentes clave de Spark SQL, su optimización mediante Catalyst, y su interacción con las distintas APIs de Spark como RDDs, DataFrames y Datasets. Se discutirán conceptos esenciales como la gestión de esquemas, la conversión entre estructuras de datos y el aprovechamiento de técnicas de optimización automática en la ejecución de consultas.

Además, se proporcionarán ejercicios prácticos que permitirán afianzar los conocimientos adquiridos y desarrollar habilidades en la implementación de consultas SQL sobre grandes volúmenes de datos en entornos distribuidos.

Los apartados a tratar en esta unidad didáctica serán:



- **Conceptualización de Spark SQL**  
  Origen, evolución y motivaciones detrás de su desarrollo.
- **Arquitectura de Spark SQL**  
  Estructura del módulo, integración con Apache Spark y su motor de ejecución optimizado.
- **Diferencias entre Spark SQL y bases de datos relacionales**  
  Características y limitaciones en comparación con los sistemas OLTP tradicionales.
- **APIs de Spark SQL**  
  RDDs, DataFrames y Datasets como mecanismos para la manipulación eficiente de datos.
- **Optimizaciones en Spark SQL**  
  Funcionamiento del optimizador Catalyst y mejoras de rendimiento en la ejecución de consultas.
- **Ejercicios prácticos**  
  Implementación de consultas SQL sobre Spark y su integración con distintas fuentes de datos.



#### Objetivos



1. **Comprender** el contexto en el que surge **Spark SQL** y su papel dentro del ecosistema **Apache Spark.**
2. **Diferenciar** las características de **Spark SQL** respecto a otros enfoques de procesamiento de datos estructurados, identificando sus ventajas y limitaciones.
3. **Analizar** la arquitectura de **Spark SQL,** sus componentes principales y su integración con el motor de ejecución de Spark.
4. **Explorar** el funcionamiento de **Catalyst,** el optimizador de consultas de Spark SQL, y su impacto en el rendimiento del procesamiento de datos.
5. **Implementar** consultas SQL en **DataFrames** y **Datasets,** aprovechando su integración con Spark y la optimización automática del motor.
6. **Ejecutar** ejercicios prácticos para afianzar el uso de **Spark SQL,** aplicando técnicas de **optimización de consultas** y **manejo de esquemas.**
7. **Configurar y gestionar** la ejecución de consultas en entornos distribuidos, integrando **Spark SQL** **con diversas fuentes de datos** y motores de almacenamiento.



## 2. Spark Sql: Contextualización



### 2.1 Introducción



![image](assets/cm8eztprc0054356x4e7gnlyr-stock-image.jpg)



En la actualidad, el procesamiento de grandes volúmenes de datos se ha convertido en una necesidad para muchas organizaciones. Con la creciente demanda de análisis en tiempo real y la integración de datos estructurados y no estructurados, han surgido diversas herramientas para optimizar estos procesos. En este contexto, Apache Spark se ha consolidado como una de las plataformas más eficientes para el procesamiento distribuido de datos, ofreciendo un ecosistema robusto que incluye Spark SQL, un módulo diseñado para trabajar con datos estructurados mediante una interfaz familiar basada en SQL.

Spark SQL combina la facilidad de uso del lenguaje SQL con la escalabilidad y tolerancia a fallos del motor de procesamiento de Spark. Su capacidad para interactuar con múltiples fuentes de datos y su optimizador interno lo convierten en una opción poderosa para la analítica de datos a gran escala. A lo largo de esta unidad, exploraremos los fundamentos de Spark SQL, sus características principales y su impacto en el ecosistema del Big Data.



### 2.2 ¿Qué es Spark SQL?



**Spark SQL** es un módulo dentro del ecosistema de Apache Spark diseñado para proporcionar una abstracción basada en tablas mediante la definición de esquemas estructurados. Su objetivo principal es acercar las capacidades de un framework de **Big Data** a herramientas de **Business Intelligence (BI),** facilitando la integración con entornos analíticos tradicionales.

Este módulo permite un acceso uniforme a los datos, independientemente de su origen, ofreciendo una interfaz unificada para consultar y procesar información de diversas fuentes de datos. Además, **Spark SQL** es capaz de combinar datos procedentes de diferentes fuentes, proporcionando mayor flexibilidad en los análisis. Gracias a su integración con los **RDDs (Resilient Distributed Datasets)** y el **Engine Core** de Spark, hereda características clave como la tolerancia a fallos y la computación distribuida. Asimismo, incorpora optimizaciones del modelo **Dataset,** lo que mejora su eficiencia y rendimiento en el procesamiento de datos a gran escala.



![image](assets/cm8ezwvg6009a356xc70qmutl-INSD_PRDT_U4_Apartado3-2_Imagen1.jpg)



### 2.3 ¿Por qué surge Spark SQL?



La evolución del procesamiento de datos ha llevado a la necesidad de herramientas que combinen el rendimiento de los sistemas distribuidos con la facilidad de uso de las consultas estructuradas. En este contexto, **Spark SQL** surge como una solución que unifica ambos mundos, permitiendo trabajar con grandes volúmenes de datos de manera eficiente y flexible.

Uno de los principales motivos de su aparición es la prevalencia del estándar **SQL,** que se ha impuesto sobre los lenguajes NoSQL debido a su fuerte integración con herramientas de Business Intelligence (BI). Las empresas requieren soluciones que faciliten el acceso y análisis de datos a través de herramientas familiares, y SQL se mantiene como el lenguaje más utilizado en este ámbito.

Además, la API de **RDDs (Resilient Distributed Datasets)** de Spark, aunque poderosa, no maneja **esquemas de datos,** lo que limita su capacidad para optimizar consultas y garantizar consistencia en los datos estructurados. Los RDDs tampoco aprovechan la información del contexto de ejecución, lo que impide optimizaciones avanzadas como la planificación de consultas mediante **árboles de ejecución,** el uso de **cachés** y la recopilación de **estadísticas** para mejorar el rendimiento.

La siguiente imagen representa un**árbol de ejecución física** en **Spark SQL,** que describe cómo Spark ejecutará una consulta SQL internamente.



![image](assets/cm8ezzvdo00ax356xhz2he7x4-INSD_PRDT_U4_Apartado3-3_Imagen2.jpg)



Este tipo de diagramas se utilizan en Spark SQL para representar cómo se transforman los datos a lo largo del proceso de ejecución. Se construyen a partir del plan lógico optimizado y se convierten en un plan físico que Spark ejecuta en los clústeres distribuidos.



1. - Este nodo indica que el resultado final de la consulta seleccionará solo ciertas columnas de los datos procesados.
2. - Es una estrategia de unión en la que la tabla más pequeña se transmite (broadcast) a todos los nodos, lo que mejora la eficiencia cuando se une con una tabla más grande.
   - Específicamente, es una Left Join, lo que significa que todos los registros de la tabla izquierda se mantienen y solo los coincidentes de la tabla derecha se agregan.
3. - **PhysicalRDD (izquierda):** Representa un conjunto de datos (RDD) físico cargado en Spark. Esto puede venir de una fuente de datos como un archivo, base de datos, etc.
   - **Filter (derecha):** Indica que Spark aplica un filtro a otro conjunto de datos antes de la unión.
     - **Hijo del Filter:** PhysicalRDD → Otra fuente de datos que se filtra antes de unirse con la tabla principal.
4. Resumiendo, en este plan de ejecución se indica que:

   1. Spark carga dos conjuntos de datos (PhysicalRDD).
   2. A uno de ellos se le aplica un **filtro** antes de proceder.
   3. Se realiza un **Broadcast Left Join**, optimizando el rendimiento al transmitir la tabla más pequeña a los nodos.
   4. Finalmente, se **proyectan** (seleccionan) las columnas deseadas en la salida final.



Otra razón clave para la creación de Spark SQL fue la necesidad de mejorar las limitaciones de Apache Hive, que, aunque ofrecía una interfaz SQL sobre Hadoop, presentaba deficiencias en términos de rendimiento y tolerancia a fallos. Spark SQL nació para abordar estos desafíos, proporcionando una solución más rápida, optimizada y compatible con diversos formatos de datos y fuentes de almacenamiento.



### 2.4 Características de Spark SQL



- **Acceso unificado a una gran variedad de fuentes de datos gracias a la API de Datasources**  
  Spark SQL permite conectarse y procesar datos desde múltiples orígenes como **archivos CSV, JSON, Parquet,**  bases de datos relacionales mediante **JDBC,** y sistemas NoSQL como **MongoDB, Cassandra** o **Elasticsearch.** Esta flexibilidad facilita la integración de Spark SQL en diversos entornos de datos.
- **Escalabilidad (RDDs)**  
  Basado en la arquitectura distribuida de Spark, Spark SQL puede manejar grandes volúmenes de datos y escalar horizontalmente al agregar más nodos al clúster. Gracias a los**RDDs (Resilient Distributed Datasets),** permite ejecutar consultas sobre datasets de tamaños muy grandes sin comprometer el rendimiento.
- **Tolerancia a fallos (RDDs)**  
  Los RDDs en los que se basa Spark SQL están diseñados para ser tolerantes a fallos. En caso de una falla en algún nodo del clúster, Spark puede **reconstruir automáticamente** los datos sin necesidad de reiniciar todo el proceso, asegurando alta disponibilidad y confiabilidad en la ejecución de consultas.
- **Motor de ejecución optimizado**  
  Spark SQL utiliza **Catalyst,** un motor de optimización que mejora el rendimiento de las consultas mediante técnicas como la **reorganización de planes de ejecución,** eliminación de redundancias y **push-down de filtros.** Además, aprovecha el **Tungsten Engine,** que optimiza el uso de memoria y CPU para mejorar la eficiencia computacional.
- **Integración con RDDs, DataFrames y Datasets**  
  Spark SQL permite la conversión fluida entre **RDDs, DataFrames y Datasets,** ofreciendo la flexibilidad de operar tanto con**API funcionales** de RDDs como con estructuras más optimizadas para el procesamiento relacional. Esto permite a los desarrolladores elegir la mejor herramienta según el caso de uso.
- **Compatibilidad con sentencias Hive**  
  Spark SQL es compatible con el lenguaje SQL de **Apache Hive,** lo que permite ejecutar consultas **HiveQL** directamente sobre los datos en Spark. Esto facilita la migración de sistemas basados en Hive hacia un entorno más eficiente y distribuido sin necesidad de modificar las consultas existentes.
- **Compatibilidad con Hive Metastore**  
  Además de ser compatible con HiveQL, Spark SQL puede **utilizar el metastore de Hive,** lo que significa que puede interactuar con bases de datos, tablas y esquemas previamente definidos en Hive. Esto facilita la integración con sistemas de almacenamiento ya establecidos y mejora la interoperabilidad con herramientas de análisis.
- **Extensibilidad**  
  Spark SQL permite la creación de **funciones definidas por el usuario (UDFs y UDAFs) (posteriormente las veremos)** en múltiples lenguajes como Scala, Java y Python, lo que permite a los desarrolladores extender sus capacidades y adaptar el motor a necesidades específicas de negocio o análisis de datos.
- **Push-down de filtros**  
  Para mejorar el rendimiento, Spark SQL puede aplicar **filtros directamente en la fuente de datos,** reduciendo la cantidad de datos que se transfieren y procesan en memoria. Esto es especialmente útil al trabajar con bases de datos externas o sistemas de almacenamiento distribuidos, ya que minimiza la latencia y el uso de recursos.



### 2.5 Spark SQL vs Bases de datos relacionales



Aunque **Spark SQL** ofrece una interfaz similar a SQL para el procesamiento de datos, su funcionamiento es muy diferente al de una **base de datos relacional tradicional.** Una de sus principales características es su capacidad para **acceder y procesar datos desde múltiples fuentes heterogéneas,** como archivos en distintos formatos (JSON, CSV, Parquet), bases de datos externas y sistemas de almacenamiento distribuidos. Sin embargo, debido a esta flexibilidad, Spark SQL no incorpora ciertas funcionalidades clave de las bases de datos relacionales.

A diferencia de un sistema **OLTP (Online Transaction Processing)** tradicional, Spark SQL **no maneja conceptos como:**



- **Primary Key y Foreign Key**  
  No existen claves primarias ni foráneas para garantizar la integridad referencial de los datos.
- **Índices**  
  No cuenta con índices como los de las bases de datos para acelerar búsquedas, aunque utiliza estrategias de optimización diferentes.
- **Triggers**  
  No permite la ejecución de acciones automáticas basadas en eventos de inserción, actualización o eliminación.
- **Transacciones ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad)**  
  No ofrece mecanismos de control transaccional que garanticen consistencia en operaciones concurrentes.
- **Roles y control de usuarios**  
  No posee un sistema nativo de gestión de permisos y roles como una base de datos tradicional.
- **Esquema fijo**  
  Aunque Spark SQL soporta esquemas, estos no son estrictos y pueden inferirse o cambiarse dinámicamente.
- **Lenguaje procedural**  
  No permite la ejecución de procedimientos almacenados ni la creación de funciones dentro del motor de base de datos.



A pesar de estas diferencias, Spark SQL **trabaja con dos tipos principales de tablas:**



- **Tablas externas**  
  Referencian datos almacenados fuera de Spark (por ejemplo, en HDFS o bases de datos externas).
- **Tablas manejadas**  
  Spark gestiona tanto los datos como el esquema de la tabla dentro de su almacenamiento interno.



Estas características hacen que **Spark SQL sea más adecuado para análisis masivo de datos en entornos distribuidos,** mientras que las bases de datos relacionales siguen siendo la mejor opción para aplicaciones transaccionales que requieren garantías de consistencia y control detallado sobre los datos.



![image](assets/cm8f0le5w00lj356xr73wtp06-INSD_PRDT_U4_Apartado3-5_Imagen3.jpg)



### 2.6 ¿Qué no es Spark SQL?



- **NO es un Data Warehouse**  
  Spark SQL permite la consulta y procesamiento de datos, pero no ofrece las funcionalidades completas de un almacén de datos tradicional, como la gestión avanzada de esquemas o la optimización de almacenamiento a largo plazo.
- **NO es una base de datos relacional**  
  Aunque soporta SQL, Spark SQL no es una base de datos en sí misma, ya que no maneja transacciones, claves primarias, índices ni almacenamiento persistente como lo haría un sistema relacional.
- **NO es una herramienta transaccional**  
  No está diseñado para operaciones transaccionales con propiedades **ACID**(Atomicidad, Consistencia, Aislamiento y Durabilidad), lo que lo hace inadecuado para sistemas bancarios o aplicaciones que requieran estricta integridad de datos.
- **NO es una herramienta comercial**  
  Apache Spark es un proyecto de código abierto y no una solución comercial con soporte propietario. Sin embargo, varias empresas ofrecen versiones gestionadas con soporte empresarial.
- **NO es una herramienta gráfica**  
  Spark SQL no proporciona una interfaz gráfica para gestionar datos o consultas, sino que se usa a través de código en **Scala, Python, Java o SQL** mediante entornos como notebooks o interfaces de línea de comandos.
- **NO es una herramienta para sentencias online**  
  No está optimizado para ejecutar consultas SQL interactivas en tiempo real como lo haría un **OLAP** o una base de datos diseñada para análisis en vivo.
- **NO es una herramienta que solo utilice memoria**  
  Aunque Spark SQL puede realizar muchas operaciones en memoria para mejorar el rendimiento, también puede leer y escribir datos en almacenamiento persistente como **HDFS, S3 o bases de datos externas.**
- **NO es una cola para el envío de datos**  
  No actúa como un sistema de mensajería o transmisión de datos en tiempo real como **Apache Kafka** o **RabbitMQ,** aunque puede integrarse con ellos.
- **NO es solo una interfaz SQL**  
  Aunque permite consultas SQL, su funcionalidad va más allá, permitiendo el uso de **DataFrames, Datasets** y **API funcionales** para procesamiento avanzado de datos.



### 2.7 Casos de uso



Gracias a su flexibilidad y potencia, Spark SQL se ha convertido en una herramienta clave en el procesamiento de datos a gran escala. Su capacidad para integrarse con múltiples fuentes de datos, ejecutar consultas SQL de alto rendimiento y optimizar el procesamiento distribuido lo hace ideal para una amplia variedad de aplicaciones. A continuación, se presentan algunos de los principales casos de uso en los que Spark SQL destaca:



- **Conectar herramientas de BI con un Data Lake**  
  Spark SQL facilita la integración de herramientas de **Business Intelligence (BI)** con **Data Lakes,** permitiendo la consulta de datos estructurados y semiestructurados de manera eficiente.
- **Realizar analítica avanzada en Batch**  
  Se pueden ejecutar tareas de análisis de datos en **modo batch,** procesando grandes volúmenes de información de forma periódica y optimizada.
- **Realizar analítica avanzada en Streaming**  
  Spark SQL permite procesar datos en **tiempo real,** lo que es útil en aplicaciones que requieren respuestas instantáneas basadas en flujos continuos de información. Como ejemplo más representativo podemos comentar las **Agregaciones en tiempo real (cubos OLAP).** Gracias a su capacidad de **agregación en streaming,** Spark SQL puede manejar datos en estructuras tipo **OLAP,** facilitando consultas analíticas en tiempo real.
- **Machine Learning a través de DataFrames**  
  Al integrarse con **MLlib,** la librería de Machine Learning de Spark, es posible utilizar **DataFrames** para entrenar modelos y realizar análisis predictivos sobre grandes volúmenes de datos.
- **Proporcionar esquema a datos desestructurados**  
  Permite dar **estructura** a datos sin un formato definido, como archivos JSON o logs de sistemas, facilitando su procesamiento y análisis con SQL.
- **ETL (Extract, Transform, Load)**  
  Spark SQL es una herramienta poderosa para implementar **procesos ETL,** extrayendo datos de diversas fuentes, transformándolos y cargándolos en sistemas de almacenamiento o bases de datos.
- **Ingesta de datos**  
  Puede usarse para **ingestar datos** desde múltiples fuentes, como bases de datos, APIs, sistemas de mensajería y archivos, integrándolos en entornos distribuidos.
- **Analítica avanzada en la nube**  
  Se adapta a entornos cloud-native, permitiendo ejecutar análisis sobre datos almacenados en plataformas como Amazon S3, Google Cloud Storage y Azure Data Lake.



## 3. Apis De Spark Y Modelos De Datos



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



Apache Spark ofrece diferentes**APIs** para el procesamiento de datos, cada una diseñada para casos de uso específicos y optimizadas para distintos tipos de estructuras de datos. Desde su primera versión, Spark ha evolucionado incorporando modelos de datos más eficientes y expresivos, mejorando tanto el rendimiento como la facilidad de uso para los desarrolladores.

Las tres principales APIs de Spark son: **RDDs (Resilient Distributed Datasets),** que proporcionan un enfoque de bajo nivel para manipular datos desestructurados (Spark  0.1+);**DataFrames**, que permiten el procesamiento relacional de datos estructurados con una sintaxis similar a SQL (Spark  1.3+); y**Datasets**, que combinan lo mejor de ambos mundos, ofreciendo seguridad de tipos y optimización avanzada (Spark  1.6+). En este capítulo, exploraremos estas APIs en detalle y compararemos sus ventajas y desventajas en distintos escenarios de procesamiento de datos.



### 3.2 ¿Por qué surgen?



En los últimos años, el crecimiento exponencial de los datos ha generado la necesidad de herramientas más eficientes para su procesamiento. Mientras que en un principio los entornos de **Big Data** se centraban en manejar datos desestructurados, como archivos de texto o registros de logs, la demanda de trabajar con **datos estructurados y semiestructurados** ha ido en aumento.

Hadoop, una de las primeras soluciones para el procesamiento distribuido, estaba diseñado para manejar principalmente **datos desestructurados,** lo que limitaba su adopción en entornos que requerían modelos de datos más organizados. Para cubrir esta necesidad, **Apache Spark incorporó APIs especializadas en datos estructurados,** como **DataFrames y Datasets,** permitiendo un manejo más eficiente y expresivo de la información.

Además, las **herramientas de Business Intelligence (BI)** están diseñadas para trabajar con **datos estructurados,** por lo que contar con APIs que permitieran integrar Spark con estas herramientas se volvió fundamental. Gracias a estas mejoras, Spark ha logrado posicionarse como una solución versátil para el análisis y procesamiento de datos a gran escala, combinando la flexibilidad del procesamiento distribuido con la estructura y facilidad de consulta del modelo relacional.



### 3.3 Datasets: Concepto



En **Apache Spark,** un **Dataset** es una colección **fuertemente tipada** de objetos de un dominio específico que puede ser transformada en paralelo utilizando operaciones funcionales (como funciones lambda) y **operaciones relacionales.** Su principal ventaja es que proporciona una interfaz más segura y optimizada en comparación con los**RDDs (Resilient Distributed Datasets)** y los **DataFrames,** combinando lo mejor de ambos mundos.

Un **Dataset** permite representar colecciones de datos, como una lista de facturas o registros de clientes, con un esquema bien definido, donde cada propiedad tiene un **nombre y un tipo de dato.** A diferencia de los RDDs, que no tienen un esquema explícito, los Datasets incluyen una capa de tipado que **reduce errores en tiempo de compilación,** lo que mejora la robustez del código antes de su despliegue.

Otra característica clave de los Datasets es su capacidad de conversión eficiente mediante el uso de **encoders,** que permiten transformar objetos de la**JVM (Java Virtual Machine)** a una representación tabular en formato binario, optimizando el uso de la memoria. Spark SQL incluye **encoders específicos** para tipos primitivos de Scala y **case classes,** lo que facilita la manipulación de datos de manera más estructurada.

Desde el punto de vista de ejecución, los Datasets incluyen un **DSL (Domain-Specific Language)** a medida, lo que permite trabajar con una sintaxis similar a la de los RDDs pero con las ventajas del procesamiento estructurado. Además, la mayoría de las operaciones dentro de un Dataset se ejecutan sobre **código optimizado y serialización eficiente,** lo que mejora su rendimiento dentro del motor de Spark SQL. Recordad que un **DSL (Domain-Specific Language)** es un **lenguaje de programación o un subconjunto de un lenguaje** diseñado específicamente para un dominio o problema en particular. A diferencia de los lenguajes de propósito general (como Python, Java o Scala), que pueden usarse para desarrollar una amplia gama de aplicaciones, los **DSLs** están optimizados para tareas concretas dentro de un área específica.

En términos funcionales, Spark SQL permite trabajar con Datasets mediante **dos tipos de operaciones principales:**



•

Transformaciones, que generan nuevos Datasets a partir de otros aplicando funciones sobre los datos.

•

Acciones, que ejecutan operaciones finales y devuelven resultados al programa.



En definitiva, los Datasets proporcionan una forma flexible, segura y eficiente de procesar datos estructurados en Spark, permitiendo a los desarrolladores aprovechar las ventajas del tipado estático sin sacrificar el rendimiento del procesamiento distribuido.

Posteriormente se verán ejemplos trabajando con Datasets.



### 3.4 DataFrame: Concepto



Un **DataFrame** en **Apache Spark** es una estructura de datos organizada en **columnas nombradas,** similar a una tabla en una **base de datos relacional** o a un **DataFrame en Pandas o R,** pero con optimizaciones avanzadas para el procesamiento distribuido.

Gracias al motor de ejecución de **Spark SQL,** los DataFrames ofrecen mejoras significativas en términos de rendimiento y escalabilidad. Se pueden construir a partir de diversas fuentes de datos, como **archivos estructurados**(CSV, JSON, Parquet), **tablas de Hive, bases de datos externas** o incluso **RDDs preexistentes,** permitiendo una gran flexibilidad en el procesamiento de datos.

La API de **DataFrames** está disponible en múltiples lenguajes, incluyendo**Scala, Java, Python y R,** lo que facilita su adopción en diferentes entornos y comunidades de desarrollo. Internamente, un **DataFrame** en Spark es representado como un **Dataset[Row],** lo que permite combinar la expresividad del SQL con la eficiencia del procesamiento distribuido.

Al igual que los **RDDs** y los **Datasets,** los DataFrames permiten realizar **dos tipos principales de operaciones:**



•

Transformaciones, que generan nuevos DataFrames aplicando funciones sobre los datos sin ejecutarlas inmediatamente.

•

Acciones, que desencadenan la ejecución de las transformaciones y devuelven resultados al usuario.



Resumiendo , un DataFrame es una colección distribuida de datos organizados en columnas nombradas. Conceptualmente, es equivalente a una tabla en una base de datos relacional o a un marco de datos en R/Python, pero con optimizaciones más avanzadas en su funcionamiento interno. Los DataFrames pueden construirse a partir de una amplia variedad de fuentes, como archivos de datos estructurados, tablas en Hive, bases de datos externas o RDDs existentes.



![image](assets/cm8f1k9kw00wi356xtzcdkunz-INSD_PRDT_U4_Apartado4-4_Imagen6.jpg)



### 3.5 Dataset vs DataFrame. Evolución



La siguiente imagen ilustra cómo Spark 2.0 unificó la API para trabajar con datos estructurados, eliminando la distinción rígida entre DataFrames y Datasets. Ahora, DataFrame es simplemente un Dataset sin tipado estático, mientras que los Datasets tipados ofrecen mayor control y seguridad en el procesamiento de datos en Spark.



![image](assets/cm8f1lr2d00xw356x375o9qy6-INSD_PRDT_U4_Apartado4-5_Imagen7.jpg)



Por tanto, en **Spark 2.0** y**versiones posteriores, DataFrame y Dataset** son prácticamente la misma estructura de datos, con una diferencia clave:

- **DataFrame** → Es un **Dataset[Row],** lo que significa que no tiene tipado estático. Los tipos de datos se manejan dinámicamente en tiempo de ejecución.
- **Dataset[T]** → Tiene **tipado estático,** lo que permite detectar errores en **tiempo de compilación,** proporcionando mayor seguridad y control sobre los datos.

**Ejemplo en Scala:**



```scala
// DataFrame (sin tipado estático, Dataset[Row])
val df = spark.read.json("data.json")

// Dataset con tipado (Dataset[T])
case class Person(name: String, age: Int)
val ds = df.as[Person]  // Conversión a Dataset tipado
```



Podemos concluir que DataFrame es solo un alias de Dataset[Row], útil para consultas SQL y manipulación flexible de datos, mientras que Dataset[T] es ideal cuando se necesita tipado fuerte para mayor seguridad y control en el código.



### 3.6 Diferencias en el Manejo de Errores



Esta imagen muestra cómo se manejan los **errores de sintaxis y análisis** en **SQL, DataFrames y Datasets,** destacando la diferencia entre la **detección en tiempo de ejecución (Runtime)** y en t**iempo de compilación (Compile Time).**



![image](assets/cm8f1rhmp0119356xl3a5eeao-INSD_PRDT_U4_Apartado4-6_Imagen8.jpg)



- **SQL (Consultas en cadenas de texto)**  
  - **Errores de sintaxis**: Se detectan **en tiempo de ejecución**, ya que las consultas SQL en Spark suelen escribirse como cadenas de texto, lo que impide la verificación previa a la ejecución.
  - **Errores de análisis**: También se identifican **en tiempo de ejecución**, por ejemplo, si una columna no existe en la consulta.
- **DataFrames (Dataset[Row])**  
  - **Errores de sintaxis**: Se pueden detectar **en tiempo de compilación**, ya que la API de DataFrames permite estructurar consultas de forma programática con validaciones previas.
  - **Errores de análisis**: Se detectan **en tiempo de ejecución**, dado que los DataFrames no tienen tipado estático, lo que puede llevar a errores cuando la consulta es ejecutada.
- **Datasets (Dataset[T])**  
  - **Errores de sintaxis**: Se detectan **en tiempo de compilación**, ya que el tipado fuerte impide escribir código incorrecto antes de ejecutarlo.
  - **Errores de análisis**: También se detectan **en tiempo de compilación**, lo que mejora la seguridad del código al prevenir problemas antes de su ejecución.



En resumen, mientras que SQL y DataFrames permiten mayor flexibilidad,  pero detectan ciertos errores tarde, los Datasets ofrecen más seguridad y robustez, evitando errores desde la compilación.

**Ejemplos:**



•

Ejemplo de error SQL en tiempo de ejecución (Runtime Error):



```ruby
val df = spark.read.json("people.json")
df.createOrReplaceTempView("people")

// Error: "edad" no existe (el nombre correcto es "age"), pero Spark solo lo
 // detectará en tiempo de ejecución.
spark.sql("SELECT nombre, edad FROM people").show()
```



El error ocurre al ejecutar la consulta, ya que SQL en Spark no valida los nombres de columnas antes de ejecutarse.



•

DataFrames en Spark (Errores de Sintaxis en Tiempo de Compilación, pero de Análisis en Tiempo de Ejecución)
Los DataFrames permiten construir consultas de manera programática, por lo que errores de sintaxis pueden detectarse en tiempo de compilación. Sin embargo, si la consulta intenta acceder a una columna inexistente, el error aparecerá solo en tiempo de ejecución.
Ejemplo sin error:



```bat
val df = spark.read.json("people.json")
df.select("name", "age").show()  // Correcto porque "name" y "age" existen.
```



**Ejemplo de error en tiempo de ejecución:**



```ruby
df.select("nombre", "age").show()
```



**Este error ocurre en tiempo de ejecución** porque la columna "nombre" no existe (debería ser "name").



•

Datasets en Spark (Errores de Sintaxis y Análisis en Tiempo de Compilación - Compile Time Errors)
Los Datasets[T] están fuertemente tipados, lo que significa que Spark valida los datos en tiempo de compilación, evitando errores antes de ejecutar el código.
Ejemplo sin error:



```ruby
case class Person(name: String, age: Int)
val ds = df.as[Person]  // Convierte el DataFrame en un Dataset tipado
ds.filter(_.age > 18).show()  // Correcto porque "age" está definido en Person
```



**Ejemplo de error en tiempo de compilación:**



```bash
ds.filter(_.edad > 18).show()  // Error: "edad" no existe en la case class Person
```



**Aquí el error se detecta en tiempo de compilación**, antes de ejecutar el código, evitando fallos en ejecución.



### 3.7 Schema RDD: La API de RDDs en Spark



Antes de la introducción de **DataFrames** y **Datasets,** la API principal para el procesamiento de datos en **Apache Spark** era **RDD (Resilient Distributed Dataset).** Los **RDDs** son estructuras de datos distribuidas que permiten manipular grandes volúmenes de información de manera flexible, pero con c**iertas limitaciones en cuanto a optimización y facilidad de uso.**

Cuando trabajamos con **Spark** + **RDDs,** los datos se manipulan como **objetos no estructurados,** lo que significa que no existe un esquema explícito que defina las columnas o tipos de datos. Este enfoque es **más opaco** al modelo de datos, ya que Spark no puede aprovechar optimizaciones avanzadas basadas en la estructura de los datos.

Por otro lado, cuando se utiliza **SQL + DataFrame,** Spark es capaz de **inferir un esquema,** lo que permite estructurar los datos en columnas y realizar consultas de manera similar a SQL. Esta conversión proporciona **mejor optimización** **y un acceso más intuitivo a la información,** permitiendo que Spark aplique técnicas como **optimización con Catalyst y almacenamiento eficiente con Tungsten.**

En resumen:

- **Los RDDs son la API más básica y flexible de Spark,** pero carecen de optimización automática.
- **Los DataFrames permiten estructurar los datos y optimizar el rendimiento.**
- **El esquema en los DataFrames ayuda a trabajar con los datos de forma más eficiente y similar a SQL.**

Con la evolución de Spark, el uso de **RDDs puros se ha reducido en favor de DataFrames y Datasets,** que ofrecen un mejor rendimiento y facilidad de uso en la mayoría de los casos.



![image](assets/cm8f2bhax01lu356xiw4349ga-INSD_PRDT_U4_Apartado4-7_Imagen9.jpg)



### 3.8 Comparación de Rendimiento



La siguiente imagen muestra una comparativa del **rendimiento en tiempo de ejecución** al realizar una operación de agregación sobre **10 millones de pares de enteros**, utilizando diferentes enfoques en **Apache Spark**. Se comparan dos APIs: **RDDs (Resilient Distributed Datasets)** y **DataFrames (DF)**, y dos lenguajes de programación: **Scala** y **Python**.



![image](assets/cm8f2coqj01n8356x5t619r5b-INSD_PRDT_U4_Apartado4-8_Imagen10.jpg)



Observaciones clave:

- **Los DataFrames son significativamente más rápidos que los RDDs**
- Tanto en **Python** como en **Scala**, los **DataFrames** tienen un tiempo de ejecución mucho menor en comparación con los RDDs.
- Esto se debe a las optimizaciones del motor **Catalyst** en Spark SQL, que permite una ejecución más eficiente.

**Scala tiene mejor rendimiento que Python en RDD’s y similar en DF’s**

- En RDD’s la implementación en **Scala** es más rápida que la de **Python**. Esto ocurre porque **Spark está escrito en Scala**, lo que permite una ejecución más eficiente sin la sobrecarga de interoperabilidad con la JVM (Java Virtual Machine), que sí ocurre con Python a través de **Py4J**.
- **Los RDDs en Python son los más lentos.** La agregación con **RDDs en Python** toma casi **10 segundos**, lo que es considerablemente más lento que cualquier otra opción. Esto se debe a que los RDDs en Python requieren conversiones constantes entre Python y la JVM, afectando el rendimiento.
- En la imagen, tanto **Spark Python DF** como **Spark Scala DF** tienen tiempos de ejecución bajos y muy similares. Esto demuestra que, cuando se usan **DataFrames**, Spark SQL optimiza el rendimiento de manera eficiente en ambos lenguajes.



## 4. Consultas En Spark Sql



### 4.1 Introducción



![image](assets/cm8f2euww01p3356x3qzpevwh-stock-image.jpg)



Apache Spark SQL proporciona una potente interfaz para la ejecución de consultas estructuradas sobre grandes volúmenes de datos. Gracias a su integración con **DataFrames** y su compatibilidad con **SQL estándar**, Spark permite realizar operaciones analíticas de manera eficiente y escalable. A través del uso de **tablas temporales**, es posible convertir estructuras de datos en tablas SQL, lo que facilita la consulta y manipulación de la información con sentencias familiares para los analistas y desarrolladores. Además, el motor de optimización **Catalyst** mejora el rendimiento de las consultas al generar planes de ejecución optimizados.

Una de las características más avanzadas de Spark SQL es la posibilidad de extender sus capacidades mediante **Funciones Definidas por el Usuario (UDFs y UDAFs)**. Estas funciones personalizadas permiten ejecutar transformaciones específicas en los datos, ya sea a nivel de filas (**UDFs**) o agregaciones complejas (**UDAFs**). Gracias a estas funcionalidades, Spark SQL no solo ofrece un entorno flexible para consultas estándar, sino que también permite a los usuarios adaptar el procesamiento de datos a necesidades específicas, mejorando así la expresividad y eficiencia del análisis de datos en entornos distribuidos.



### 4.2 Creación y Manipulación de Datasets en Spark SQL



En este ejercicio, trabajaremos con datos de vuelos de drones almacenados en formato JSON. Cada registro representa información clave sobre un dron en un momento específico, incluyendo su dirección IP, nombre, identificador, marca de tiempo y velocidad.

Nuestro objetivo es procesar estos datos utilizando Apache Spark y su API de Datasets. Específicamente, vamos a:

1. Cargar los datos desde un archivo JSON en un Dataset[DroneData].
2. Filtrar los drones que superen una velocidad de 10 unidades.
3. Transformar los datos para obtener el nombre del dron junto con su velocidad.
4. Agrupar los resultados por el nombre del dron y calcular la velocidad promedio.

Este ejercicio permitirá comprender cómo utilizar Spark para manipular datos estructurados y realizar operaciones de filtrado, transformación y agregación de manera eficiente.

La ejecución de dicho ejemplo se muestra en el siguiente video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652191_1/scormcontent/assets/INSD_PRDT_U4_Apartado5-2_Video1SparkDataset.mp4?v=1)



Básicamente los pasos realizados son:

1. Spark lee el JSON, infiere el esquema y genera una colección de DataFrames.
2. Spark convierte los datos en DataFrame = Dataset[Row], una colección de objetos genéricos de tipo Row, ya que no conoce el tipo exactamente.
3. Spark convierte el Dataset[Row] —> Dataset[DroneData] con tipos específicos de Scala como objetos de la JVM



### 4.3 Manejo de Datos con Spark SQL y DataFrames



A continuación se muestra el código de un ejemplo:



```scala
import org.apache.spark.sql._

val sparkSession = SparkSession.builder().master("local[*]").getOrCreate()

import sparkSession.implicits._

case class Person(name: String, age: Int)

val people = sc.textFile("examples/src/main/resources/people.txt").map(_.split(",")).map(p
=> Person(p(0), p(1).trim.toInt)).toDF()

people.registerTempTable("people")

val teenagers = sparkSession.sql("SELECT name, age FROM people WHERE age >= 13 AND age <=  19")
```



Este código en **Scala y Apache Spark** crea una **sesión de Spark**, carga datos desde un archivo de texto, los transforma en un **DataFrame**, y luego realiza una consulta SQL sobre ellos para obtener solo los registros de adolescentes (personas entre 13 y 19 años).

Posteriormente tendremos ocasión de ejecutarlo y sobretodo entender que  si hemos ejecutado antes bin/spark-shell ya tenemos una sesión abierta y no hay que crear otra.



### 4.4 Funciones Definidas por el Usuario en Spark SQL (UDFs y UDAFs)



Apache Spark permite extender su funcionalidad mediante **Funciones Definidas por el Usuario (UDFs y UDAFs)**. Estas funciones personalizadas permiten realizar transformaciones y agregaciones en los datos más allá de las funciones nativas de Spark SQL.

- **UDF (User Defined Function)**: Funciones personalizadas que transforman datos a nivel de fila.
- **UDAF (User Defined Aggregate Function)**: Funciones de agregación personalizadas que operan sobre múltiples filas y devuelven un único valor.

A continuación, exploraremos en detalle cada una de ellas con ejemplos prácticos.



#### Funciones UDF's



Las **UDFs (User Defined Functions)** permiten definir funciones personalizadas que pueden aplicarse a columnas de un **DataFrame** o dentro de consultas **SQL** en Spark. Estas funciones reciben una entrada, aplican una transformación y devuelven un nuevo valor.

El siguiente video muestra un ejemplo en el que se **crea una UDF para convertir texto a mayúsculas:**



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652191_1/scormcontent/assets/INSD_PRDT_U4_Apartado5-4-1_%20Video2UDF1.mp4?v=1)



Explicación del código del video:



```scala
import org.apache.spark.sql.functions.udf

// Creación de un DataFrame de ejemplo
val dataset = Seq((0, "hello"), (1, "world")).toDF("id", "text")

// Definir la función que convierte texto a mayúsculas
val upper: String => String = _.toUpperCase

// Registrar la UDF en Spark
val upperUDF = udf(upper)

// Aplicar la UDF a una nueva columna
dataset.withColumn("upper", upperUDF($"text")).show()
```



- Se crea un DataFrame con una columna text que contiene palabras en minúsculas.
- Se define una función upper en Scala que convierte un texto en mayúsculas.
- Se registra como UDF usando udf(upper).
- Se aplica la función a la columna text con withColumn.

Seguidamente registramos una UDF para su uso en consultas SQL



```sql
// Registrar la función UDF en el catálogo de Spark SQL
spark.udf.register("myUpper", (input: String) => input.toUpperCase)

// Verificar que la función está registrada en el catálogo
spark.catalog.listFunctions.filter('name like "%upper%").show(false)

// Uso de la UDF en una consulta SQL
spark.sql("SELECT myUpper('prueba')").collect()
```



**Explicación**:

- register permite que la UDF pueda utilizarse en consultas SQL.
- La función myUpper transforma cadenas de texto en mayúsculas dentro de SQL.

**Importante: Hemos visto dos enfoques** de cómo se registra la **User Defined Function (UDF)** y cómo se utiliza en Apache Spark. Aquí está la explicación y el desglose:

1. spark.udf.register("myUpper", (input: String) => input.toUpperCase)

   **¿Qué hace?**

   - Registra la función como una UDF SQL en el catálogo de funciones de Spark.
   - Permite que la UDF se use en consultas SQL ejecutadas sobre DataFrames o tablas.

   **Ejemplo de uso:** Si tienes un DataFrame df, puedes usar la función en SQL:

   df.createOrReplaceTempView("my_table")

   spark.sql("SELECT id, text, myUpper(text) AS upper FROM my_table").show()

   **Ventaja:** Se puede llamar desde SQL sin necesidad de definir una función UDF manualmente en Scala.
2. val upper: String => String = _.toUpperCase

   val upperUDF = udf(upper)

   **¿Qué hace?**

   - Define una función Scala normal (upper).
   - Luego, la convierte en una UDF explícita de Spark con udf(upper).
   - La UDF resultante (upperUDF) se puede usar directamente en operaciones de DataFrame.

   **Ejemplo de uso en DataFrame API:**

   dataset.withColumn("upper", upperUDF($"text")).show()

   **Ventaja:** Permite usar la función dentro del API de DataFrame sin necesidad de registrar una tabla SQL.
3. | Método | Uso Principal | Se Puede Usar en SQL | Se Puede Usar en DataFrames |
   | --- | --- | --- | --- |
   | spark.udf.register("myUpper", (input: String) => input.toUpperCase) | Función registrada globalmente en Spark | Sí | Sí (con expr("myUpper(text)") ) |
   | val upperUDF = udf(upper) | Función específica para DataFrames | No | Sí |

   **¿Cuál usar?**

   - Si quieres usar la función en consultas SQL, usa spark.udf.register.
   - Si solo necesitas la función en la API de DataFrame, usa udf().
   - Si necesitas ambas opciones, puedes registrar la UDF con spark.udf.register y también definirla como udf().



En el siguiente video se muestra un ejemplo de contar la cantidad de caracteres en una cadena usando  ambas formas.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652191_1/scormcontent/assets/INSD_PRDT_U4_Apartado5-4-1_Video3UDF2.mp4?v=1)



#### Funciones UDAF’s



Las **UDAFs (User Defined Aggregate Functions)** permiten definir funciones personalizadas que **agregan valores** de una columna en un único resultado. Son útiles cuando las funciones de agregación nativas de Spark (como sum, avg, count) no cubren las necesidades específicas del usuario.

Ejemplo: Crear una UDAF para concatenar valores de una columna:

El primer video nos dará un warning porque emplea métodos deprecated pero que se ven bastante en códigos que podamos encontrar por internet:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652191_1/scormcontent/assets/INSD_PRDT_U4_Apartado5-4-2_Video4UDAF1ConWarning.mp4?v=1)



En cambio en este segundo video explicamos como quitar ese warning:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652191_1/scormcontent/assets/INSD_PRDT_U4_Apartado5-4-2_Video5UDAF2SinWarning.mp4?v=1)



**Explicación:**

En este caso, la clase GroupConcat extiende UserDefinedAggregateFunction, lo que significa que define una función de agregación personalizada. Su funcionamiento se basa en cuatro pasos fundamentales:



- **Initialize (Inicialización)**  
  Se define el estado inicial del buffer de agregación, que generalmente es un valor vacío o un acumulador.
- **Update (Actualización)**  
  A medida que Spark procesa nuevas filas, esta función agrega cada nuevo valor al estado intermedio.
- **Merge (Fusión)**  
  Dado que Spark ejecuta operaciones en paralelo, se pueden generar múltiples buffers de agregación. Esta función combina esos buffers en uno solo.
- **Evaluate (Evaluación)**  
  Finalmente, una vez que se han procesado todas las filas, se devuelve el valor final de la agregación.



Una vez definida la función GroupConcat, se registra en el motor SQL de Spark con el siguiente comando:



```bat
spark.udf.register("group_concat", new GroupConcat)
```



Después de esto, la UDAF se puede utilizar en consultas SQL dentro de Spark.



## 5. Sparksession, Optimización Y Performance En Spark Sql



### 5.1 Introducción



![image](assets/cm8f32i4s02rw356xlaf8q5q5-stock-image.jpg)



Apache Spark proporciona diferentes puntos de entrada para interactuar con su motor de procesamiento distribuido. Desde versiones anteriores, el acceso a los recursos del clúster y las operaciones sobre datos se gestionaban mediante **SparkContext** y **SQLContext**. Sin embargo, a partir de **Spark 2.0**, se introdujo **SparkSession** como una interfaz unificada que combina todas las funcionalidades clave de Spark.

**SparkContext**

Es la base de cualquier aplicación en Spark y se encarga de la gestión del clúster. Actúa como el punto de control principal para comunicarse con los **executors**, administrar tareas y acceder a la API de **RDDs (Resilient Distributed Datasets)**. Fue el punto de entrada principal en versiones anteriores de Spark.

**SQLContext**

Es una capa sobre **SparkContext** que permite ejecutar consultas en SparkSQL. Proporciona una API para interactuar con **DataFrames** y realizar consultas utilizando SQL estándar. En versiones recientes, **SQLContext ha sido incorporado en SparkSession**, lo que facilita su uso sin necesidad de instanciarlo por separado.

**SparkSession**

Introducida en **Spark 2.0**, **SparkSession** reemplaza a **SQLContext** y **HiveContext**, proporcionando un punto de acceso unificado para trabajar con **RDDs, DataFrames y Datasets**. Es la forma recomendada para interactuar con Spark en aplicaciones modernas, ya que centraliza la creación y gestión de los diferentes componentes.

Ejemplo de creación de una SparkSession:



```scala
import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder()
  .appName("EjemploSparkSession")
  .master("local[*]")
  .getOrCreate()
```



Con SparkSession, los usuarios pueden:

- Crear y manipular RDDs, DataFrames y Datasets.
- Ejecutar consultas SQL sobre los datos.
- Acceder a configuraciones del clúster.
- Integrarse con **Apache Hive** y otras fuentes de datos.

En conclusión, mientras que **SparkContext** sigue existiendo internamente, **SparkSession** es el punto de entrada recomendado para nuevas aplicaciones de Apache Spark, proporcionando una interfaz más sencilla y unificada.



### 5.2 SparkSession



Como se ha comentado, a partir de **Apache Spark 2.0**, se introdujo **SparkSession** como el nuevo punto de entrada para todas las operaciones dentro del entorno de Spark. Su propósito es simplificar la gestión de recursos y unificar el acceso a las diferentes APIs que ofrece Spark.

SparkSession no solo actúa como el punto de inicio para leer y escribir datos, sino que también desempeña un papel clave en la **gestión de metadatos**, la configuración del entorno de ejecución y la administración de los recursos del clúster. Además, permite la creación y manipulación de **Datasets y DataFrames**, facilitando el procesamiento estructurado de datos.

En términos de arquitectura, **SparkSession encapsula componentes esenciales** como:

- **SparkContext** (para la administración del clúster y la ejecución de tareas).
- **SQLContext** (para la ejecución de consultas SQL sobre datos estructurados).
- **StreamingContext** (para el procesamiento de datos en tiempo real).
- **SparkConf** (para la configuración personalizada del entorno de Spark).

Una vez que se crea una instancia de SparkSession, es posible modificar las propiedades de configuración en tiempo de ejecución, lo que proporciona mayor flexibilidad a los usuarios. Por ejemplo, para definir el número de particiones en las operaciones de shuffle, se puede usar:

**spark.conf.set("spark.sql.shuffle.partitions", 6)**

Esta capacidad de ajuste dinámico permite optimizar el rendimiento de las consultas y tareas dentro de Spark, asegurando un uso eficiente de los recursos disponibles.

La siguiente imagen representa el **flujo de ejecución de un Dataset en Apache Spark**.



![image](assets/cm8f3591g02v8356xxa7phtnl-INSD_PRDT_U4_Apartado6-2_Imagen11.jpg)



Un **Dataset** es la estructura de datos principal en Spark SQL, y su procesamiento involucra varios componentes clave.



- **Encoder**  
  Es responsable de la conversión entre objetos de alto nivel y su representación serializada eficiente en memoria.
- **QueryExecution**  
  Gestiona la ejecución de consultas sobre el Dataset, conectándolo con el**Plan Lógico (LogicalPlan),** que representa la estructura abstracta de la consulta.
- **SparkSession**  
  Actúa como el punto de entrada para ejecutar operaciones sobre el Dataset y proporciona acceso a la configuración y el estado de la sesión.
- **SessionState**  
  Contiene información sobre la configuración y el estado de ejecución de la sesión.
- **SparkOptimizer**  
  Es el componente responsable de optimizar las consultas SQL mediante técnicas como reordenamiento de operadores y eliminación de redundancias.



Por tanto, en este diagrama se muestra cómo Spark transforma un Dataset en un plan de ejecución optimizado antes de ejecutarlo, asegurando eficiencia en el procesamiento distribuido.

En la siguiente imagen, tenemos un ejemplo que muestra cómo crear una SparkSession y utilizarla para leer un archivo CSV almacenado en HDFS con Apache Spark.



![image](assets/cm8f3a5qd02y9356xs18bjxtb-INSD_PRDT_U4_Apartado6-2_Imagen12.jpg)



Explicación:

Se inicializa una SparkSession, que es el punto de entrada para usar Spark SQL y DataFrames:

- appName("MySparkSession") asigna un nombre a la sesión.
- master("local[*]") indica que se ejecutará en modo local, utilizando todos los núcleos disponibles (*).
- getOrCreate() devuelve una sesión existente o crea una nueva si no hay ninguna activa.

Lectura del csv en HDFS:

- sparkSession.read crea un lector de datos.
- .option("header", "true") indica que el CSV tiene una fila de encabezado con los nombres de las columnas.
- .csv("hdfs://namenode:9000/data/sales.csv") carga el archivo desde un sistema distribuido HDFS en la ruta especificada.

Este fragmento de código es un ejemplo básico de cómo iniciar una sesión de Spark y leer datos desde HDFS en formato CSV, preparando el DataFrame para futuras consultas o transformaciones.



### 5.3 Catalyst (Optimizador en Spark SQL)



Spark SQL utiliza **Catalyst**, un potente optimizador de consultas, para transformar las consultas SQL y las operaciones en DataFrames en planes de ejecución eficientes. La imagen muestra el flujo de procesamiento de una consulta dentro de **Catalyst**, que consta de varias etapas:



![image](assets/cm8f3ch5s030e356xnj7yq6ic-INSD_PRDT_U4_Apartado6-3_Imagen13.jpg)



1. - Se recibe una consulta en formato SQL o una operación sobre un DataFrame.
2. - Se genera un **Unresolved Logical Plan** (Plan Lógico No Resuelto), donde las referencias a tablas y columnas aún no han sido validadas.
   - El **Catalog** se usa para verificar la existencia de las tablas y resolver referencias.
   - Se obtiene un **Logical Plan** (Plan Lógico Resuelto) válido.
3. - Se generan transformaciones para mejorar la eficiencia, como eliminación de filtros redundantes y **pushdown predicates**.
   - Se produce un **Optimized Logical Plan** (Plan Lógico Optimizado).
4. - Se generan múltiples **Physical Plans** (Planes Físicos) candidatos para ejecutar la consulta.
   - Un **Cost Model** evalúa el costo de cada plan y selecciona el más eficiente.
5. - Se traduce el **Selected Physical Plan** en instrucciones de bajo nivel para ejecución en Spark.
   - Se crean **RDDs (Resilient Distributed Datasets)**, que son la estructura de datos subyacente utilizada para la ejecución distribuida.
6. Este flujo de procesamiento optimiza automáticamente las consultas en Spark SQL, permitiendo **ejecución eficiente y paralelizada** de operaciones en grandes volúmenes de datos.



#### Plan Lógico y Plan Físico en Spark SQL (Logical Plan y Spark Plan)



Apache Spark SQL convierte una consulta SQL o una operación sobre DataFrames en una secuencia de transformaciones antes de ejecutarla. Este proceso involucra la generación de diferentes tipos de planes:



- **Plan Lógico No Resuelto (Unresolved Logical Plan)**  
  Se genera cuando se escribe una consulta, pero aún no se han validado los nombres de las tablas o columnas.
- **Plan Lógico Analizado (Analyzed Logical Plan)**  
  Se resuelven las referencias a columnas y tablas utilizando el **Catálogo de Metadatos**.
- **Plan Lógico Optimizado (Optimized Logical Plan)**  
  Se aplican optimizaciones como la eliminación de columnas innecesarias o la reorganización de filtros.
- **Plan Físico (Physical Plan)**  
  Se generan múltiples opciones de ejecución y se selecciona la más eficiente utilizando un **modelo de costos**.
- **Generación de Código (Code Generation) y RDDs**  
  El plan físico seleccionado se convierte en instrucciones ejecutables sobre RDDs para su procesamiento distribuido.



El siguiente ejemplo muestra cómo inspeccionar estos planes en Spark con EXPLAIN EXTENDED:



![image](assets/cm8f3kfdq036k356xktg5pi0j-INSD_PRDT_U4_Apartado6-3-1_Imagen14.jpg)



La salida de este comando revela las diferentes etapas del procesamiento, desde el plan lógico hasta el plan físico que se ejecutará en Spark.



![image](assets/cm8f3kuzp037x356xr98r3rxk-INSD_PRDT_U4_Apartado6-3-1_Imagen15.png)



#### Optimización de sentencias en Catalyst



El **Optimizador Catalyst** de Spark aplica reglas para mejorar la ejecución de consultas. Estas reglas pueden ser:

- **Genéricas:** Aplicables a cualquier consulta (por ejemplo, eliminar filtros redundantes).
- **Específicas del origen de datos:** Como **Predicate Pushdown**, que filtra datos directamente en el sistema de almacenamiento en lugar de hacerlo en Spark, reduciendo la cantidad de datos procesados.

**Ejemplo de Optimización: Combinación de Reglas**

Antes de la optimización, una consulta puede tener filtros y proyectos que no están en la mejor ubicación. Por ejemplo:

- Un filtro (WHERE) puede aplicarse después de un JOIN, cuando en realidad sería más eficiente aplicarlo antes.

Después de aplicar reglas de optimización, el plan se reestructura para mejorar el rendimiento, asegurando que:

- Las **proyecciones (selección de columnas)** se ejecuten antes del JOIN.
- Los **filtros (WHERE)** se empujen lo más cerca posible de la fuente de datos (**Predicate Pushdown**).

Estos pasos permiten que Spark ejecute las consultas de manera más eficiente, reduciendo la carga computacional y mejorando los tiempos de respuesta.

Podemos verlo en un ejemplo con la siguiente imagen:



![image](assets/cm8f3qa1c03id356xkwjwdnr5-INSD_PRDT_U4_Apartado6-3-2_Imagen16.jpg)

- **Antes de la optimización (Before transformations)**  
  1. Se escanean dos tablas t1 y t2.
  2. Se realiza un **JOIN** entre t1.id y t2.id.
  3. Luego se aplica un **filtro (WHERE t2.id = 50000)** después del JOIN.
  4. Finalmente, se proyectan (SELECT) los valores de t1.id y una operación matemática 3 + t1.value.
- **Después de la optimización (After transformations)**  
  1. El **filtro (WHERE t2.id = 50000) se mueve antes del JOIN**, reduciendo la cantidad de datos que se unen.
  2. Ahora, primero se proyectan las columnas necesarias (t1.id y t1.value de t1, y t2.id de t2).
  3. Luego se ejecuta el JOIN con menos datos, lo que mejora la eficiencia.



**Beneficio:** Se reduce la cantidad de datos procesados en el JOIN, haciendo la consulta más rápida y eficiente.



#### Una capa única de acceso a los datos



Antes de Spark SQL, el procesamiento de datos requería herramientas específicas para cada tipo de fuente (bases de datos relacionales, archivos en HDFS, almacenamiento en la nube, etc.). Con la introducción de **Spark SQL y SparkSession**, Spark actúa como una **capa intermedia** que facilita la conexión con diversas fuentes de datos de manera **transparente y optimizada**.

Esta capa permite a los usuarios ejecutar **consultas SQL, manipular DataFrames y Datasets**, sin preocuparse por la estructura interna o el motor de almacenamiento subyacente.

La imágen muestran cómo esta capa, junto con el Optimizador Catalyst, transforma el procesamiento de consultas para mejorar el rendimiento. Inicialmente, sin optimización, Spark realiza un JOIN costoso antes de aplicar filtros, procesando más datos de los necesarios. Sin embargo, Catalyst reorganiza las operaciones para filtrar antes del JOIN, reduciendo la carga computacional. En su versión más avanzada, Spark aprovecha fuentes de datos inteligentes mediante Predicate Pushdown, trasladando los filtros directamente al almacenamiento, lo que minimiza la transferencia de datos y mejora aún más la eficiencia. Así, la capa única de acceso de Spark SQL no solo simplifica el manejo de datos de diferentes orígenes, sino que también optimiza su procesamiento a nivel lógico y físico.



![image](assets/cm8f3owv603h0356xlfj5s1c0-INSD_PRDT_U4_Apartado6-3-3_Imagen17.jpg)



### 5.4 Ejemplos genéricos usando SparkSession



Apache Spark permite combinar la facilidad del lenguaje SQL con la potencia del procesamiento distribuido mediante DataFrames. A través de SparkSession, los usuarios pueden convertir DataFrames en tablas temporales y ejecutar consultas SQL sobre ellos, sin necesidad de definir esquemas manualmente.

**Ejemplo 1:**



```sql
>	zipsDF.createOrReplaceTempView(“zips_table")
>	zipsDF.cache()
>	val resultsDF = spark.sql("SELECT city, pop, state, zip FROM zips_table”)
>	resultsDF.show(10)
```



En el primer ejemplo, se observa cómo un **DataFrame (zipsDF)** se registra como una tabla temporal con createOrReplaceTempView("zips_table"), permitiendo que Spark SQL lo trate como una tabla relacional. Luego, se **ejecuta una consulta SQL estándar** sobre esta tabla para seleccionar columnas específicas (city, pop, state, zip), demostrando la flexibilidad de Spark para interactuar con datos estructurados.

**Ejemplo 2:**



```scala
>	import org.apache.spark.sql.SparkSession
>	val spark = SparkSession.builder().appName("Spark SQL basic  example").config("spark.some.config.option", "some-value").getOrCreate()
>	import spark.implicits._
>	val df = spark.read.json("examples/src/main/resources/employee.json")  df.show()
>	df.groupBy("age").count().show()
>	df.createOrReplaceTempView("employee")
>	val sqlDF = spark.sql("SELECT * FROM employee")
>	sqlDF.show()
```



En el segundo ejemplo, se destaca otra funcionalidad clave de Spark SQL: la **lectura de datos desde archivos JSON** mediante spark.read.json(). Después de cargar los datos en un **DataFrame (df)**, se aplican operaciones como **agrupaciones (groupBy) y conteo (count)**, mostrando cómo se pueden realizar análisis sin necesidad de escribir consultas SQL. Sin embargo, si se prefiere utilizar SQL, el DataFrame también se puede registrar como una tabla (createOrReplaceTempView("employee")) y consultar mediante spark.sql("SELECT * FROM employee").

Estos ejemplos reflejan la versatilidad de **Spark SQL**, que permite a los usuarios alternar entre el uso de **DataFrames y consultas SQL** según sus necesidades

A continuación, se muestra un video ejecutando el ejemplo 2 pero con un json hardcodeado.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652191_1/scormcontent/assets/INSD_PRDT_U4_Apartado6-4_Video6SparkSessionEj2.mp4?v=1)



**Ejemplo 3 :**

Apache Spark permite convertir **RDDs en DataFrames** para aprovechar las ventajas de **Spark SQL**, como la ejecución optimizada de consultas y el uso de una sintaxis más declarativa.



```scala
>	case class Persona(nombre: String, edad: Int)
>	val personas = sc.textFile("examples/src/main/resources/  people.txt").map(_.split(",")).map(p => Persona(p(0), p(1).trim.toInt)).toDF
>	people.registerAsTempTable(“personas")
>	val adolescentes = sql("SELECT nombre FROM personas WHERE edad >= 13 AND edad<= 19")
>	val nameList = adolescentes => "Nombre: " + t(0)).collect()
>	val adolescentes = people.where('edad>= 10').where('edad<= 19').select('nombre')
```



En este ejemplo, se muestra cómo transformar un **RDD de personas** en un DataFrame y luego registrar una **tabla temporal** para ejecutar consultas SQL sobre ella.



- **Conversión de RDD a DataFrame**  
  Se lee un archivo de texto (people.txt) con información de personas y se transforma en un **RDD de objetos Persona**. Luego, este RDD se convierte en un **DataFrame** con .toDF().
- **Registro como tabla SQL**  
  El DataFrame se registra como una **tabla temporal llamada "personas"** con registerAsTempTable("personas"), permitiendo realizar consultas SQL sobre él.
- **Consulta con SQL**  
  Se ejecuta una consulta SQL para obtener los nombres de las personas cuya edad está entre **13 y 19 años**:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652191_1/scormcontent/assets/INSD_PRDT_U4_Apartado6-4_Video7SparkSessionEj3.mp4?v=1)



> Se recomienda visitar el siguiente enlace para más información acerca de la programación de Spark SQL
>
> [Link](https://spark.apache.org/docs/latest/sql-programming-guide.html)



## 6. Conectores



### 6.1 Introducción



![image](assets/cm8f412f303z5356xqj163jlc-stock-image.jpg)



Apache Spark ofrece soporte para una amplia variedad de **fuentes de datos** a través de conectores integrados y de la comunidad. Estos permiten cargar y guardar datos en diferentes formatos y sistemas de almacenamiento, facilitando la integración con múltiples plataformas.

**Fuentes de datos incluidas en Spark**

Spark tiene conectores nativos para varios formatos populares:

- **CSV**
- **JSON**
- **Parquet**
- **Avro**
- **ORC**
- **Binary**
- **JDBC** (para bases de datos relacionales)
- **Oracle**
- **MySQL**
- **PostgreSQL**



- **Conectores desarrollados por la comunidad**  
  Aparte de los conectores integrados, la comunidad ha desarrollado conectores adicionales para interactuar con bases de datos NoSQL y motores de búsqueda:

  - **Apache Cassandra**
  - **MongoDB**
  - **Elasticsearch**
  - **Neo4j**
- **Conectores para sistemas de archivos distribuidos**  
  Spark también se integra con sistemas de almacenamiento en la nube y distribuidos:

  - **HDFS (Hadoop Distributed File System)**
  - **Amazon S3**
  - **Azure Storage**
  - **Google Cloud Storage**



Gracias a estos conectores, Spark permite procesar datos de diversas fuentes de manera eficiente y escalable



![image](assets/cm8f43qzk041z356xxwe8ivn3-INSD_PRDT_U4_Apartado_207-1_Imagen18.jpg)



Se facilitan a continuación dos links con información oficial acerca de las fuentes de datos y sobre conexión con sistemas cloud:



> **Link 1**
>
> [Link](https://spark.apache.org/docs/latest/sql-data-sources-binaryFile.html)

> **Link 2**
>
> [Link](https://spark.apache.org/docs/latest/cloud-integration.html)



A continuación se muestran ejemplos del uso de algunos conectores.



### 6.2 Cassandra



Cassandra es una base de datos NoSQL altamente escalable utilizada en entornos distribuidos. Spark permite leer y escribir datos en Cassandra con gran eficiencia.



![image](assets/cm8f47073045i356xr93tfnm7-INSD_PRDT_U4_Apartado7-2_Imagen19.jpg)



Recordad los modos de escritura:

- **Append:** Agrega nuevos datos sin sobrescribir.
- **Overwrite:** Sobrescribe la tabla existente.
- **ErrorIfExists:** Lanza un error si la tabla ya existe.
- **Ignore:** No hace nada si la tabla ya existe.



### 6.3 Amazon S3



Para leer archivos desde S3, Spark utiliza el esquema s3n:// o s3a://. En Apache Spark, los esquemas s3n:// y s3a:// son protocolos utilizados para acceder a datos almacenados en **Amazon S3**. Aunque ambos permiten la lectura y escritura en S3, hay diferencias clave en su rendimiento, capacidad y compatibilidad.

Simplemente para vuestro conocimiento general:

| Característica | s3n:// (S3 Native) | s3a:// (S3 Advanced) |
| --- | --- | --- |
| Estado | Obsoleto en versiones recientes de Spark y Hadoop | Reemplazo recomendado, introducido en Hadoop 2.7 |
| Límite de tamaño | Máximo 5 GB por archivo | Tamaño ilimitado, con segmentación automática |
| Compatibilidad IAM | No compatible con autenticación IAM de AWS | Compatible con IAM y roles de acceso en AWS |
| Escalabilidad | Problemas con grandes volúmenes de datos | Mejor rendimiento y escalabilidad |
| Paralelización | Menos eficiente | Optimizado para alto rendimiento y mejor paralelización |
| Seguridad | Sin soporte nativo para cifrado y compresión | Admite cifrado y compresión nativa en la transferencia de datos |

**Conclusión**: Se recomienda **s3a://** en lugar de **s3n://** por su mayor rendimiento, escalabilidad y compatibilidad con AWS, aunque aun se encuentran ejemplos con el conector antiguo como el siguiente.

**Ejemplo:**



```scala
import org.apache.spark.sql._
val people = sc.textFile("s3n://bigdata-utad/data/people.txt")
val schemaString = "name age"
val schema = StructType(schemaString.split(" ").map(fieldName =>StructField(fieldName, StringType, true))) 
val rowRDD = people.map(_.split(",")).map(p => Row(p(0),p(1).trim))
val peopleSchemaRDD = sqlContext.applySchema(rowRDD,schema)
peopleSchemaRDD.registerTempTable("people")
val results = sqlContext.sql("SELECT name FROM people WHEREage >= 13 AND age <= 19")
results.map(t => "Name: " + t(0)).collect().foreach(println)
```



### 6.4 MongoDB



MongoDB es una base de datos orientada a documentos que puede integrarse con Spark mediante mongo-spark-connector.

**Ejemplo de conexión a MongoDB:**



```bat
./bin/spark-shell --conf "spark.mongodb.read.connection.uri=mongodb://127.0.0.1/test.myCollection?readPreference=primaryPreferred" \ --conf "spark.mongodb.write.connection.uri=mongodb://127.0.0.1/test.myCollection" \ --packages org.mongodb.spark:mongo-spark-connector_2.12:10.2.2
```



**Ejemplo de lectura desde MongoDB:**



```lua
val dataFrame = spark.read
  .format("mongodb")
  .option("database", "people")
  .option("collection", "contacts")
  .load()
```



> Para información adicional se recomienda visitar el enlace:
>
> [Link](https://www.mongodb.com/docs/spark-connector/current/batch-mode/batch-read-config/)



### 6.5 Json



El formato JSON es ampliamente usado en Spark por su facilidad de manipulación y estructura flexible, y siempre se podrá solicitar de forma automática o programática a una fuente que nos de la información en este formato. Ya hemos visto algún ejemplo con anterioridad.



## 7. Ejemplos



### 7.1 Introducción



![image](assets/cm8f4dl2q04cf356x3mmjipmt-stock-image.jpg)



A continuación, en los siguientes subcapítulos, se presentarán una serie de **ejercicios prácticos** diseñados para reforzar y aplicar los conocimientos adquiridos hasta el momento. Estos ejercicios abordarán distintos aspectos del uso de **Apache Spark**, desde la manipulación de **DataFrames y RDDs** hasta la ejecución de consultas SQL sobre grandes volúmenes de datos. Cada ejercicio ha sido diseñado para enfrentar al alumno con **situaciones reales de procesamiento de datos distribuidos**, permitiéndole desarrollar habilidades clave en el análisis y transformación de datos.

Si bien se proporcionarán **soluciones en código y recursos adicionales, como vídeos explicativos**, es altamente recomendable que el alumno **intente resolver cada ejercicio por sí mismo antes de consultar la solución**. Este enfoque permitirá identificar **posibles bloqueos o dificultades**, comprender mejor los errores y, en última instancia, **aprender de la experiencia práctica**. Resolver los problemas de forma autónoma fortalece la capacidad de análisis, fomenta el pensamiento crítico y prepara al alumno para enfrentar desafíos en proyectos reales.



### 7.2 Ejemplo 1: Exploración y Manipulación de Datos con DataFrames en Spark



En este ejercicio, trabajaremos con **Apache Spark** para explorar cómo se crean, transforman y consultan los **DataFrames** y **RDDs** en un entorno distribuido. El objetivo es familiarizarnos con la manipulación de datos estructurados en Spark mediante diferentes enfoques y herramientas.

**📌 ¿Qué vamos a hacer?**

1. **Creación de DataFrames en Spark**
  - Crearemos un **DataFrame desde una lista de datos en Scala**.
  - Definiremos manualmente un **esquema estructurado** con tipos de datos específicos.
  - Leeremos datos desde un **archivo CSV** con diferentes configuraciones para manejar delimitadores y tipos de datos.
2. **Exploración de la Estructura de los Datos**
  - Usaremos métodos como printSchema, dtypes y columns para analizar la estructura del DataFrame.
3. **Conversión entre DataFrames y RDDs**
  - Transformaremos un **DataFrame en un RDD** para trabajar con datos en forma de tuplas.
4. **Exploración Inicial de los Datos**
  - Utilizaremos show(), describe() y count() para inspeccionar y analizar el contenido del DataFrame.
5. **Consultas sobre los Datos**
  - Crearemos una **vista temporal** con createGlobalTempView().
  - Ejecutaremos consultas SQL directamente sobre los datos utilizando spark.sql().
  - Realizaremos las mismas consultas mediante la **API de Spark**.

A lo largo del ejercicio, entenderemos cómo manejar datos en **Spark SQL**, realizar consultas sobre ellos y extraer información útil.

El desarrollo del mismo puede comprobarse en el siguiente video



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652191_1/scormcontent/assets/INSD_PRDT_U4_Apartado8-2_Video8Ejemplofinal1.mp4?v=1)



### 7.3 Ejemplo 2: Exploración, análisis y manipulación de datos



Este ejercicio práctico en **Apache Spark** tiene como objetivo explorar, analizar y manipular un conjunto de datos de calidad del vino. A lo largo del ejercicio, se realizan diversas operaciones utilizando **Spark SQL y DataFrames**, tales como la visualización de datos, la inspección del esquema, la identificación de valores numéricos, la realización de estadísticas descriptivas y la detección de valores nulos. Además, se aplican técnicas de agregación, filtrado y transformación de datos, incluyendo la creación de nuevas columnas derivadas de los atributos existentes y el cálculo de métricas como la correlación entre variables.

Asimismo, se introduce la generación de un conjunto de datos artificial que representa tiendas de vino en diferentes ciudades, permitiendo analizar la relación entre los vinos disponibles y sus características comerciales. Se emplean métodos de **agrupación y agregación** para obtener información relevante, como la cantidad de tiendas por ciudad y la distribución de vinos en ellas. Finalmente, se incluyen consultas avanzadas para extraer insights más profundos, como el análisis del impacto del contenido de alcohol y la acidez en la calidad del vino, así como la detección de patrones y tendencias dentro del dataset.

A continuación facilito el código completo para que los alumnos vayan ejecutándolo y descubriendo las distintas posibilidades. Si os fijáis en cada apartado está un enunciado breve y su solución.



```scala
import org.apache.spark.sql.functions._

val winesdf = spark.read.format("csv").option("header", "true").option("delimiter", "|").option("inferSchema", "true").load("/home/bigdata/Descargas/winequality-red-white.txt")

// 1. Obtener una muestra de ejemplo del DF por pantalla
// Método "show" de Dataset
winesdf.show

// 2. Visualizar el esquema o estructura del DF
// Método "printSchema" de Dataset
winesdf.printSchema

// 3. Quedarnos sólo con los nombres de la columnas que albergan datos de tipo "double"
// Método "dtypes" de Dataset
val double_cols = winesdf.dtypes.filter{case(c, t) => t.compareTo("DoubleType")==0}.map(_._1)

// 4. Descripción estadística de las variables “fixed_acidity” y "citric_acid" simultáneamente
// Método "describe" de Dataset
winesdf.describe("fixed_acidity", "citric_acid").show

// 5. Número de muestras total en el dataset?
// Método "count" de Dataset
winesdf.count

// 6. Número de filas distintas en el dataset?
// Método "distinct" y "dropDuplicates" de Dataset
winesdf.distinct().count
winesdf.dropDuplicates().count

// 7. Hay vinos iguales (i.e., hay filas que se repiten)? (True/False)
winesdf.count > winesdf.distinct().count

// 8. Número de nulos en cada columna
// Método "isNull" de Column
// Método "sum" de functions
val all_cols = winesdf.columns
val null_counts = all_cols.map(c => sum(col(c).isNull.cast("int")).alias(c + "_nulls"))
winesdf.select(null_counts:_*).show
winesdf.agg(null_counts.head, null_counts.tail:_*).show

// 9. Cuántos vinos hay de cada tipo: blanco, tinto?
// Método "groupBy" y "agg" de Dataset
winesdf.groupBy("style").agg(count("*")).show

// 10. Comparar tintos vs blancos en términos de acidez (fixed_acidity) y calidad (quality): mean +- std
//    - 10.1. Qué categoría tiende a presentar mayor acidez?
//    - 10.2. En qué categoría los vinos tienden a tener mayor calidad?
// Método "groupBy" y "agg" de Dataset
// Métodos "mean" y "stddev" de functions
winesdf.groupBy("style").agg(count("*"), mean("fixed_acidity"), stddev("fixed_acidity"), mean("quality"), stddev("quality")).show

// 11. Nueva columna "pcg_free_sulfur_dioxide" con el porcentaje de SO2 de tipo libre: col("free_sulfur_dioxide")/col("total_sulfur_dioxide")
// Método "withColumn" de Dataset
// Método col de functions
winesdf.withColumn("pcg_free_sulfur_dioxide", col("free_sulfur_dioxide")/col("total_sulfur_dioxide")).show

// 12. Crear una columna "chloride_per_citric_acid" que represente el nivel de “chlorides” por cada unidad de “citric_acid”. Si el valor de
// esta última es 0, la columna resultante debe ser -1.0
// Método "withColumn" de Dataset
// Método when y col de functions
winesdf.withColumn("chloride_per_citric_acid", when(col("citric_acid") > 0.0, col("chlorides")/col("citric_acid")).otherwise(-1.0)).show

// 13. Nueva columna con "id" del vino
// Método "withColumn" de Dataset
// Método "monotonically_increasing_id" de functions
val winesiddf = winesdf.withColumn("id", monotonically_increasing_id())
winesiddf.show

// 14. Valor medio de “fixed_acidity”?
// Método "select" de Dataset
// Método "mean" de functions
winesdf.select(mean("fixed_acidity")).show


// 15. Recoger el valor medio de “fixed_acidity” en una variable
// Método "first" de Dataset
// Método "getAs" de Row
val mean_fixed_acidity = winesdf.select(mean("fixed_acidity").alias("mean_fixed_acidity")).first.getAs[Double]("mean_fixed_acidity")

// 16. Cuántos vinos hay con un “fixed_acidity” superior a la media?
// Método "filter" de Dataset
winesdf.filter(col("fixed_acidity") > mean_fixed_acidity).count


// 17. Media de fixed_acidity en blancos y tintos? Recoger los datos en un Map[String, Double]
// Método "groupBy" y "agg" de Dataset
// Método "rdd" de Dataset
// Método "getAs" de Row
// Método "collectAsMap" de RDD
val mean_fixed_acidity_map = winesdf.groupBy("style").agg(mean("fixed_acidity").alias("mean_fixed_acidity")).rdd.map(r => (r.getAs[String]("style"), r.getAs[Double]("mean_fixed_acidity"))).collectAsMap()

// 18. Nueva columna que recoja, para cada vino, el incremento relativo de fixed_acidity respecto al valor promedio de este atributo en su categoría (blanco/tinto)
// Método "withColumn" de Dataset
// Objeto "Window"
// https://spark.apache.org/docs/3.3.4/sql-ref-syntax-qry-select-window.html
import org.apache.spark.sql.expressions._
winesdf.withColumn("cat_avg_fixed_acidity", mean("fixed_acidity").over(Window.partitionBy("style"))).withColumn("inc_fixed_acidity", (col("fixed_acidity") - col("cat_avg_fixed_acidity"))/col("cat_avg_fixed_acidity")).select("cat_avg_fixed_acidity", "fixed_acidity", "inc_fixed_acidity").show


// 19. En cada categoría, blancos y tintos, cuántos vinos hay con "fixed_acidity" superior al valor medio de esta variable en su categoría?
// Método "filter" y "count" de Dataset
// Objeto "Window"
winesdf.filter((col("style")==="red") && (col("fixed_acidity") > mean_fixed_acidity_map("red"))).count

winesdf.filter((col("style")==="white") && (col("fixed_acidity") > mean_fixed_acidity_map("white"))).count

winesdf.withColumn("mean_fixed_acidity_style", mean("fixed_acidity").over(Window.partitionBy("style"))).groupBy("style").agg(sum(when(col("fixed_acidity") > col("mean_fixed_acidity_style"), 1.0).otherwise(0.0)).alias("num_acid_wines")).show

// 20. Crear una columna flag ("alcohol_label") que identifique tres tipos de vino de acuerdo a su grado de alcohol: low -> (-inf, 9.5), high -> [12.0, inf), medium -> [9.5, 12)
// Método "withColumn" de Dataset
// Método "when" de functions
val alclabelf = winesdf.withColumn("alcohol_label", lit("low")).withColumn("alcohol_label", when(col("alcohol") >= 9.5 && col("alcohol") < 12, "medium").otherwise(col("alcohol_label"))).withColumn("alcohol_label", when(col("alcohol") >= 12, "high").otherwise(col("alcohol_label")))

alclabelf.show

// 21. Promedio de cada una de las variables (numéricas) por cada etiqueta de alcohol?
// Método "groupBy" y "agg" de Dataset
val mean_double_cols = double_cols.map(c => mean(c).alias("mean_" + c))

alclabelf.groupBy("alcohol_label").agg(mean_double_cols.head, mean_double_cols.tail:_*).show

// 22. Promedio y std de cada una de las variables (numéricas) por cada etiqueta de alcohol? Redondeamos a cifras con 4 decimales
// Método "groupBy" y "agg" de Dataset
// Método "round" de functions
val mean_std_double_cols = double_cols.flatMap(c => List(round(mean(c), 4).alias("mean_" + c), round(stddev(c), 4).alias("std_" + c)))
alclabelf.groupBy("alcohol_label").agg(mean_std_double_cols.head, mean_std_double_cols.tail:_*).show

// 23. Mostar en orden descendente las combinaciones de categoría y nivel de alcohol en función de pH medio
// Método "groupBy" y "agg" de Dataset
// Método "orderBy" de Dataset
// Método "desc" de functions

alclabelf.groupBy("style", "alcohol_label").agg(mean("pH").alias("mean_pH")).orderBy(desc("mean_pH")).show

// 24. Umbrales de primer y tercer cuartil para la variable "total_sulfur_dioxide"
// Método "stat" de Dataset
// Método "approxQuantile" de DataFrameStatFunctions
winesdf.stat.approxQuantile("total_sulfur_dioxide", Array(0.25, 0.75), relativeError=0.0)

// 25. Nos quedamos sólo con los vinos que no se repiten
// Objeto "Window" con partición definida por todas las columnas
// Método "withColumn" para crear una nueva columna que contenga el número de repeticiones
// Método "filter" de Dataset para cribar las filas de acuerdo al valor de la nueva columna
val cols = winesdf.columns

winesdf.withColumn("num_reps", count("*").over(Window.partitionBy(cols.head, cols.tail:_*))).filter(col("num_reps")===1)


// 26. En qué categoría, blanco o tinto, hay más vinos que no se repiten?
/// Objeto "Window" con partición definida por todas las columnas
// Método "withColumn" para crear una nueva columna que contenga el número de repeticiones
// Método when de functions para crear una nueva columna flag "norep" que indique si la fila se repite o no
// Método "groupBy" y "agg" de Dataset para contar sobre "norep"

winesdf.withColumn("num_reps", count("*").over(Window.partitionBy(cols.head, cols.tail:_*))).withColumn("norep", when(col("num_reps") === 1, 1.0).otherwise(0.0)).groupBy("style").agg(sum("norep")).show

// 27. Para cada tipo de vino, nueva columna etiqueta con el cuartil correspondiente de acuerdo al valor de pH
// Método "ntile" de functions
// Objeto "Window"
val phlabeldf = winesdf.withColumn("pH_quartile", ntile(4).over(Window.partitionBy("style").orderBy(asc("pH"))))

phlabeldf.show

// 28. Testeando la columna previa: mínimo y máximo de pH por cada tipo de vino y cuartil
// Método "groupBy" y "agg" de Dataset
// Método "min" y "max" de functions
phlabeldf.groupBy("style", "pH_quartile").agg(mean("pH").alias("pH_mean"), min("pH").alias("min_pH"), max("pH").alias("max_pH")).orderBy(asc("pH_quartile")).show

// 29. Obtener la matriz de correlaciones
// - Pares diferentes de atributos
val pairs = double_cols.toSet.subsets(2).toArray.map(_.toArray).map{case Array(f1,f2) => (f1,f2)}

// - Para cada par, calculamos la correlación. Creamos un DF
// Método "stat" de Dataset
// Método "corr" de DataFrameStatFunctions

val corr_matrix_df = pairs.map{ p =>

	val rho = winesdf.select(p._1, p._2).stat.corr(p._1, p._2)

	(p._1, p._2, rho)

}.toSeq.toDF("feat1", "feat2", "correlation")

// 30. Ordenar los pares de atributos en orden descendente de acuerdo a la correlación
// Método "orderBy" de Dataset
// Método "desc" de functions
corr_matrix_df.orderBy(desc("correlation")).show

// 31. Ordenar obviando el signo, es decir, de acuerdo a la magnitud de la correlación
// Método "withColumn" de Dataset
// Método "abs" de functions
corr_matrix_df.withColumn("abs_correlation", abs(col("correlation"))).orderBy(desc("abs_correlation")).show

// 32. Generamos un dataset artificial de tiendas de vino (500 tiendas):
// - Campos: shop_id, city, wine_id, balance
// -- shop_id: entero en [1, 20000]
// -- city: string de ["Madrid", "Sevilla", "Barcelona", "Zaragoza", "Valencia", "Valladolid", "Malaga", "Bilbao"]
// -- wine_id: one of the values in column "id" of the wine table or one unseen code
// -- balance: double de distribución normal de media 90 y desviación típica 5
val wine_id = winesiddf.select("id").distinct().rdd.map(r => r.getAs[Long]("id").toInt).collect().zipWithIndex.map{case(a,b) => (b,a)}.toMap

val num_wines = wine_id.size.toDouble

val r = scala.util.Random

val get_wine_id = udf((code: Int) => {

	if((code % 3)==0) (20000 + r.nextInt(1000)) else wine_id(code)

})



val shopdf = spark.sqlContext.range(499).withColumn("shop_id", round(lit(20000.0)*rand()).cast("int")).withColumn("city_code", round(lit(7.0)*rand())).withColumn("city", lit("none")).withColumn("city", when(col("city_code")===0, "Madrid").otherwise(col("city"))).withColumn("city", when(col("city_code")===1, "Sevilla").otherwise(col("city"))).withColumn("city", when(col("city_code")===2, "Barcelona").otherwise(col("city"))).withColumn("city", when(col("city_code")===3, "Zaragoza").otherwise(col("city"))).withColumn("city", when(col("city_code")===4, "Valencia").otherwise(col("city"))).withColumn("city", when(col("city_code")===5, "Valladolid").otherwise(col("city"))).withColumn("city", when(col("city_code")===6, "Malaga").otherwise(col("city"))).withColumn("city", when(col("city_code")===7, "Bilbao").otherwise(col("city"))).withColumn("id_code", round(lit(num_wines - 1.0)*rand()).cast("int")).withColumn("id_wine", get_wine_id(col("id_code"))).withColumn("balance", lit(5.0)*randn() + lit(90.0)).drop("id", "city_code", "id_code")


// 33. Número de tiendas por ciudad
// Método "groupBy" y "agg" de Dataset

shopdf.groupBy("city").agg(count("shop_id")).show


// 34. Número de tiendas diferentes por ciudad
// Método "groupBy" y "agg" de Dataset
// Método "countDistinct" de functions

shopdf.groupBy("city").agg(countDistinct("shop_id")).show



// 35. Cuántos de los vinos iniciales pueden encontrarse en las tiendas?
// Método "join" de Dataset

shopdf.select("id_wine").distinct().join(winesiddf, col("id")===col("id_wine"), "inner").count
```



### 7.4 Ejemplo 3: Manipulación general de datos



Este ejercicio consiste en practicar la manipulación de datos en Spark, abarcando desde la carga y filtrado de archivos (JSON, CSV, logs) hasta la conversión entre distintos formatos (RDD, DataFrame, Dataset) y la creación de tablas SQL. Incluye el arranque de HDFS y Spark, el uso de sentencias SQL para consultas y agregaciones, la definición de clases para tipar los datos (case class), la creación de tablas particionadas (parquet), el registro de UDFs (funciones definidas por el usuario) para extraer o transformar información y, finalmente, la carga y particionado de datos en distintos formatos (como JSON) con condiciones específicas (por ejemplo, magnitud de seísmos mayor a 4). De esta forma, se cubren los principales pasos de un flujo ETL en Spark, demostrando la versatilidad de sus APIs para el tratamiento de grandes volúmenes de datos.

Os recuerdo que aunque aquí tengáis el código resuelto es conveniente que lo ejecutéis e intentéis posteriormente hacerlo por vuestra cuenta sin la solución.



```scala
// puntos a tener claros antes de hacer este ejercicio:
//Diferencia entre un Dataframe y un Dataset
//Dataframe (Syntax Errors in Compile Time & Analysis Errors in Runtime)

// En otra terminal arrancamos HDFS (recordad de la unidad 2)
//bigdata@bigdatapc:~$ cd /home/bigdata/hadoop-3.3.6/
//bigdata@bigdatapc:~/hadoop-3.3.6$ sbin/start-dfs.sh


// En otra terminal
// arrancar spark-shell
//bigdata@bigdatapc:~$ cd /home/bigdata/spark-3.3.3-bin-hadoop3/
//bigdata@bigdatapc:~/spark-3.3.3-bin-hadoop3$ bin/spark-shell



spark.read.json("/home/bigdata/Descargas/fruits.json")
val df = spark.read.json("/home/bigdata/Descargas/fruits.json")
df.filter("rating > 8").show()


// ejemplo para ver el error
df.filter("ratingg > 8") // Analysis error in Runtime
//Dataset (Syntax Errors in Compile Time & Analysis Errors in Compile Time)

case class Fruit(id: Long, name: String, rating: Double)
val dataset = df.as[Fruit]
dataset.columns
dataset.filter(_.rating > 8).show() 


// De RDD a Dataframe
val rdd = sc.parallelize(Range(0, 10)).map(x => (x, s"name $x"))
case class KV(key: Int, value: String)
rdd.map{ case(k,v) => KV(k, v) }
val df = rdd.map{ case(k,v) => KV(k, v) }.toDF()
df.show

// De Dataframe a tabla SQL
df.createOrReplaceTempView("KeyValue")
spark.sql("SELECT * FROM KeyValue").show()

//Ejercicio: De RDDs a DataFrame
// ejecutar el wget en otra terminal
// wget https://gist.githubusercontent.com/mafernandez-stratio/a694fe539e4e1b14d151a1ede0339f1d/raw/2056783dfcc057f43e880faabdef63781bf8b193/access.log

val lines = sc.textFile("/home/bigdata/Descargas/access.log", 10).map(_.replaceAll("\\[","\"").replaceAll("\\]", "\"")).map(line => line.split("\"").map(_.trim).filter(_.nonEmpty)).filter(_.size > 6)
case class LogInfo(ip: String, col2: String, user: String, fecha: String, url: String, status: Int, code: Int, col8: String, browser: String, col10: String)

val logs = lines.map(line => Array(line(0).split(" "), Array(line(1)), Array(line(2)), line(3).split(" "), Array(line(4)), Array(line(5)), Array(line(6)))).map(_.flatten).filter(_.size > 9)

import scala.util._

val rows = logs.map(arr => LogInfo(arr(0),arr(1),arr(2),arr(3),arr(4),Try(arr(5).toInt).getOrElse(0),Try(arr(6).toInt).getOrElse(0),arr(7),arr(8),arr(9)))

val df = spark.createDataFrame(rows)
df.agg(max("status")).show
df.createOrReplaceTempView("test")
spark.sql("SHOW TABLES").show
spark.sql("SELECT * FROM test LIMIT 1").show(50, false)
spark.sql("SELECT status, avg(code) FROM test GROUP BY status").show(50, false)


//Ejercicio: De DataFrame a Dataset
case class LogLine(ip: String, col2: String, user: String, fecha: String, url: String, status: Int, code: Int, col8: String, browser: String, col10: String)

import spark.implicits._
val ds = df.as[LogLine]
ds.count


//Ejercicio: De Dataset a DataFrame
ds.toDF().count

//Ejercicio: De DataFrame a RDD
df.rdd.count

//Ejercicio: De RDD a Dataset
spark.createDataset(lines)


//Ejercicio: De Dataset a RDD
ds.rdd.count


//Ejercicio 1: Convertir de RDD a Tabla SQL
// recordad el wget en otra terminal diferente a donde estamos ejecutando spark

// wget https://gist.githubusercontent.com/mafernandez-stratio/c1e092f9a0aeb073a35200f4555cea1d/raw/effba761c6bb0a5a86f6bb2171fbfbf95e3509de/emails.txt

// Estructura de cada línea:
// Asunto: $ Fecha: $ Desde: $ Para: $ Mensaje: $
// Pista --> Funciones de Scala: substring & indexOf
// Pregunta: ¿Cuántos emails van dirigidos a usuarios con email de yahoo?

val emailsRDD = sc.textFile("/home/bigdata/Descargas/emails.txt")
val emailsTuplas = emailsRDD.map{ line => (
						line.substring(line.indexOf("Asunto: ")+8, line.indexOf("Fecha: ")-1).trim(), 

						line.substring(line.indexOf("Fecha: ")+7, line.indexOf("Desde: ")-1).trim(),

						line.substring(line.indexOf("Desde: ")+7, line.indexOf("Para: ")-1).trim(),

						line.substring(line.indexOf("Para: ")+6, line.indexOf("Mensaje: ")-1).trim(),

						line.substring(line.indexOf("Mensaje: ")+9).trim()

					) 

			}


case class	Email(asunto: String, fecha: String, desde: String, para: String, mensaje: String)

val emailsDF = emailsTuplas.map(tupla => Email(tupla._1, tupla._2, tupla._3, tupla._4, tupla._5)).toDF()

emailsDF.createOrReplaceTempView("emails")

spark.sql("SHOW TABLES").show

spark.sql("SELECT COUNT(*) FROM emails WHERE contains(para, 'yahoo')").show



//Ejercicio: UDF

spark.udf.register("extractdomain", (email: String) => { email.dropWhile(c => c!='@').stripPrefix("@") })

spark.sql("SELECT extractdomain(para) FROM emails").show


//Ejercicio 2: UDF extractyear para extraer año de la fecha

spark.udf.register("extractyear", (fecha: String) => { fecha.substring(0, fecha.indexOf("-")) })

spark.sql("SELECT extractyear(fecha) FROM emails").show


//Ejercicio: DataFrame con HDFS+parquet particionado
// en la otra terminal ejecutar lo siguiente para ver lo que hay en HDFS:
// bigdata@bigdatapc:~/Descargas$ cd /home/bigdata/hadoop-3.3.6/
// bigdata@bigdatapc:~/hadoop-3.3.6$ bin/hdfs dfs -ls /

// Found 3 items
// drwxr-xr-x   - bigdata supergroup          0 2025-03-02 19:08 /ebooks
// drwxr-xr-x   - bigdata supergroup          0 2025-03-03 14:38 /ejercicios
// drwx-wx-wx   - bigdata supergroup          0 2024-01-29 01:29 /tmp
// bigdata@bigdatapc:~/hadoop-3.3.6$ bin/hdfs dfs -ls /tmp/
// Found 1 items
// drwx-wx-wx   - bigdata supergroup          0 2024-01-29 01:29 /tmp/hive


spark.sql("CREATE TABLE partitionedtable(id INT, rating DOUBLE, country STRING) USING parquet OPTIONS(path 'hdfs://localhost:9000/tmp/test') PARTITIONED BY (country)")

spark.sql("INSERT INTO partitionedtable VALUES(1, 9.2, 'Spain')")

spark.sql("INSERT INTO partitionedtable VALUES(2, 8.9, 'United States')")

spark.sql("DESCRIBE EXTENDED partitionedtable").show(50, false)

spark.sql("SELECT * FROM partitionedtable").show(50, false)

spark.sql("EXPLAIN EXTENDED SELECT * FROM partitionedtable WHERE country='Spain'").show(50, false)

// volver a ejecutar otra vez y ver lo que se ha creado
//bigdata@bigdatapc:~/hadoop-3.3.6$ bin/hdfs dfs -ls /tmp/
//Found 2 items
//drwx-wx-wx   - bigdata supergroup          0 2024-01-29 01:29 /tmp/hive
//drwx-wx-wx   - bigdata supergroup          0 2025-03-17 06:45 /tmp/test


//Ejercicio: DataFrame con CSV
// recordad hacer el wget en otra terminal

//wget https://gist.githubusercontent.com/mafernandez-stratio/6486eacb387350d8e9b2d5890777dd3a/raw/b83478b6a0471caa4c4abee20c08d2401e380779/winemag.csv

//https://spark.apache.org/docs/3.3.4/sql-data-sources-csv.html



spark.sql("CREATE TABLE winemagcsv USING csv OPTIONS (path '/home/bigdata/Descargas/winemag.csv', header 'true', inferSchema 'true')")

spark.sql("DESCRIBE EXTENDED winemagcsv").show(100, false)

spark.sql("SELECT * FROM winemagcsv").show(50, false)


//Ejercicio 3: Media de puntos de vinos cuyo precio no es nulo
//https://spark.apache.org/docs/latest/api/sql/index.html

spark.sql("SELECT avg(points) FROM winemagcsv WHERE isnotnull(price)").show(50, false)


//Ejercicio 4: Crear tabla a partir del siguiente csv

// ejecutar wget en otra terminal
// wget https://gist.githubusercontent.com/mafernandez-stratio/c97926996ca458e66600215bb47f93b6/raw/9f557a7955c130dda82b640ff512d4f5735e763a/winemag_special_format.csv

// Pregunta: ¿Cuál es el precio del vino más caro de cada país?

spark.sql("CREATE TABLE winemag_quotes USING csv OPTIONS (path '/home/bigdata/Descargas/winemag_special_format.csv', header 'true', inferSchema 'true', quote '$', sep '|', comment '-')")

spark.sql("SELECT country, max(price) FROM winemag_quotes GROUP BY country").show

//Ejercicio: Join

spark.sql("SELECT * FROM partitionedtable, winemagcsv WHERE partitionedtable.id=winemagcsv.id").show(50, false)

//Ejercicio: ETL

spark.sql("CREATE TABLE persistedtest USING parquet OPTIONS (path 'hdfs://localhost:9000/tmp/persistedtest') PARTITIONED BY (status) AS SELECT * FROM test WHERE browser LIKE '%Chrome%'")

spark.sql("DESCRIBE EXTENDED persistedtest").show(50, false)

spark.sql("SELECT * FROM persistedtest LIMIT 1").show(50, false)


//Ejercicio: DataFrame con JSON
// https://www.kaggle.com/datasets/robinsonros/latest-earthquake-dataset-up-to-2024
// ejecutar wget en otra terminal
// wget https://gist.githubusercontent.com/mafernandez-stratio/5cba89aeea095f6afaf4f241b89deec3/raw/14e2fa593c13eef6f3453ced67bc40dafa76dcc1/earthquakes_2024.json



spark.sql("CREATE TABLE jsontable USING json OPTIONS (path '/home/bigdata/Descargas/earthquakes_2024.json')")

spark.sql("SELECT * FROM jsontable LIMIT 1").show(50, false)

spark.sql("DESCRIBE EXTENDED jsontable").show(50, false)

spark.sql("SELECT * FROM jsontable LIMIT 10").printSchema

spark.sql("SELECT id FROM jsontable LIMIT 10").show

spark.sql("SELECT properties.place FROM jsontable LIMIT 10").show(500, false)



//Ejercicio 5: Crear una tabla (formato parquet en HDFS) particionada por tipo (type) de seísmo // de  aquellos terremotos de magnitud (mag) mayor a 4 y que fueran detectados por más de // 50 estaciones (nst).

// La tabla debe contener las columnas relativas a lugar(place), tipo (type), magnitud (mag) y número de estaciones (nst)

spark.sql("CREATE TABLE terremotos USING parquet OPTIONS (path 'hdfs://localhost:9000/data/terremotos') PARTITIONED BY (type) AS SELECT properties.place AS place, properties.mag AS mag, properties.nst AS nst, properties.type AS type FROM jsontable WHERE properties.mag > 4 AND properties.nst > 50").show(500, false)

spark.sql("SELECT * FROM terremotos").show(500, false)
```



## 8. Conclusiones



### 8.1 Conclusiones de la unidad



Tras haber leído el contenido de esta unidad y haber realizado los ejercicios prácticos, el alumno debería ser capaz de:

- **Comprender** la importancia de **Spark SQL** dentro del ecosistema de Apache Spark y su rol en el procesamiento de datos estructurados.
- **Conocer** la arquitectura de **Spark SQL**, identificando sus principales componentes y el impacto del **optimizador Catalyst** en el rendimiento de las consultas.
- **Diferenciar** Spark SQL de las bases de datos relacionales, comprendiendo sus ventajas y limitaciones en comparación con sistemas OLTP tradicionales.
- **Dominar** el uso de **DataFrames y Datasets**, aplicando consultas SQL y aprovechando las optimizaciones automáticas del motor de ejecución de Spark.
- **Conocer** conceptos clave como la gestión de **esquemas**, la integración con diversas fuentes de datos y la optimización de consultas mediante **predicate pushdown** y ejecución distribuida.

El conocimiento de **Spark SQL** es fundamental en el procesamiento de datos a gran escala dentro del ámbito del **Big Data**. Se recomienda que el alumno practique con los ejemplos y ejercicios propuestos para afianzar su comprensión, explorando la ejecución de consultas sobre distintos formatos de datos y aplicando optimizaciones en entornos distribuidos.

Si al llegar a este punto:

- Te sientes confiado explicando qué es **Spark SQL**, cómo se diferencia de una base de datos relacional y su importancia en el análisis de datos masivos.
- Comprendes la arquitectura de **Spark SQL**, el papel del **optimizador Catalyst** y las ventajas de los **DataFrames y Datasets**.
- Has asimilado los ejercicios prácticos y puedes aplicarlos en escenarios reales, integrando Spark SQL con diversas fuentes de datos y optimizando consultas.

Entonces, se puede decir que has superado las expectativas de esta unidad y posees la base necesaria para enfrentarte con éxito a las siguientes unidades del curso, en las cuales se explorarán otras funcionalidades avanzadas de **Spark**, incluyendo su integración con **streaming**, machine learning y herramientas de orquestación.
