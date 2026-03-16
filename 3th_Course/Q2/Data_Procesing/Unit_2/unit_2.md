![image.png](attachment:63f47af6-1659-4bc4-9bdc-b83c79ecaa10:image.png)

## **Generación de datos a los largo de la historia**

La humanidad ha recopilado, almacenado y utilizado información desde tiempos inmemoriales. Desde los primeros métodos rudimentarios hasta los complejos centros de datos actuales, la capacidad de generar y gestionar datos ha evolucionado significativamente, marcando hitos cruciales en el desarrollo de la civilización.

- Primeramente nombrar los experimentos realizados por John Graunt en 1663  que supusieron el  progreso hacia el análisis sistemático de datos. Dichos análisis estaban destinados a entender y controlar la propagación de la peste bubónica en Europa.
- Posteriormente en 1854 se dio una epidemia de cólera en Londres. Esta imagen muestra una representación del mapa original que indicaba la residencia de los grupos de individuos afectados por la epidemia. Sobre ese mapa, John Snow lo que hizo fue crear un gráfico de curvas de nivel para señalar las zonas con mayor concentración de afectados obteniendo como resultado el mapa de la imagen.
- Esto inevitablemente nos lleva a recordar lo vivido hace unos años con la pandemia del COVID. Realizaban analíticas PCR a los individuos, y en Madrid por ejemplo los resultados se agrupaban por calles y barrios decidiendo posteriormente si un barrio debía estar confinado o no.

### Evolución de la gestión de datos

En la evolución de las tecnologías de datos, se han identificado desafíos importantes que han impulsado la creación de nuevas soluciones, como las que ofrece el ecosistema de Big Data. Tradicionalmente, los sistemas de gestión de bases de datos relacionales (RDBMS) han sido el estándar para almacenar y procesar información estructurada. 

Sin embargo, con la creciente generación de información desestructurada (como imágenes, videos y texto libre) y el aumento exponencial del volumen de datos, estos sistemas han mostrado limitaciones significativas. Uno de los retos principales es la dependencia de arquitecturas con un único servidor potente. 

Estas arquitecturas suelen optar por migraciones a servidores más grandes para manejar mayores volúmenes de datos, pero este enfoque tiene varias desventajas: genera altos costos, cuellos de botella, fallos en el rendimiento y un riesgo significativo de Single Point of Failure (SPoF), donde un solo fallo en el sistema puede detener completamente las operaciones.

Aunque tecnologías como el High Performing Computing (HPC) y el Massively Parallel Processing (MPP) han intentado abordar estos problemas mediante procesamiento paralelo, su implementación y escalabilidad siguen siendo limitadas en comparación con los sistemas distribuidos. Desarrollar estos sistemas de manera eficiente es complejo
 y conlleva desafíos en la gestión de cuellos de botella y fallos. Además, mover grandes cantidades de datos en estas arquitecturas centralizadas resulta ineficiente.

Es aquí donde Big Data, y herramientas desarrolladas bajo la Fundación Apache, marcan la diferencia. Tecnologías como **Hadoop y Spark** ofrecen soluciones distribuidas que eliminan los riesgos de SPoF al repartir los datos y el procesamiento entre múltiples nodos. Estas herramientas no solo permiten manejar grandes volúmenes de información 
de manera eficiente, sino que también son capaces de integrar tanto datos estructurados como desestructurados, superando las limitaciones de los sistemas tradicionales.

### ¿Qué es Big Data?

No existe una definición única.  Según a la fuente a la cual acudas puedes encontrar unas u otras definiciones como se muestra a continuación:

- Big data es utilizado para describir un volumen masivo de datos estructurados y no estructurados que es tan grande que resulta difícil de procesar utilizando técnicas tradicionales de bases de datos y software.
- Big data es un conjunto de activos de información de alto volumen, alta velocidad y/o alta variedad que requieren nuevas formas de procesamiento para permitir una mejor toma de decisiones, descubrimiento de información y optimización de procesos.
- Según IBM, Big data es el término para una colección de conjuntos de datos tan grandes y complejos que se vuelve difícil procesarlos utilizando herramientas de gestión de bases de datos tradicionales o aplicaciones de procesamiento de datos convencionales.

Con el término Big data nos referimos al análisis masivo de datos. El volumen es de tal proporción que las técnicas y herramientas clásicas que se venían utilizando hasta ahora para la recopilación, almacenamiento y procesado de datos resultan ineficientes ya que dan tiempos de respuestas no asumibles. Necesitamos tener resultados antes. 

> *“Big Data hace también referencia a todas las herramientas modernas y nuevas tecnología que permiten la ingestión, el almacenamiento y el tratamiento de tal volumen de datos. “*
> 

### Grado de madurez de la tecnología Big Data

Para justificar el grado de madurez de la tecnología Big Data vamos a utilizar como herramienta una gráfica ampliamente conocida que se denomina Curva de Gartner.

La **Curva de Gartner**, conocida también como el **"Hype Cycle"**, es una representación gráfica que ilustra el ciclo de vida de la adopción y madurez de una tecnología o innovación. Fue introducida por la consultora Gartner y se utiliza ampliamente para analizar las expectativas del mercado frente a nuevas tecnologías. Su objetivo principal es proporcionar una visión estratégica sobre cómo las tecnologías emergentes evolucionan desde su lanzamiento hasta su adopción madura. 

![image.png](attachment:b13a6c34-2e33-43fd-aedd-507850e5abb8:image.png)

- **Lanzamiento (Innovation Trigger):** Un avance tecnológico o evento mediático despierta el interés público. No suelen existir productos comerciales utilizables y su viabilidad no está probada.
- **Pico de expectativas sobredimensionadas (Peak of Inflated Expectations):** El entusiasmo masivo genera historias de éxito, pero también muchos fracasos. Las expectativas superan la realidad técnica de la
herramienta.
- **Abismo de desilusión (Trough of Disillusionment):** El interés decae cuando los experimentos fallan al no cumplir con las promesas iniciales. Los proveedores débiles desaparecen y la prensa se vuelve crítica.
- **Rampa de consolidación (Slope of Enlightenment):** Se empieza a entender el beneficio real y práctico. Surgen productos de segunda y tercera generación más estables, y más empresas se atreven con proyectos piloto.
- **Meseta de productividad (Plateau of Productivity):** La adopción masiva despega. Los beneficios son claros y demostrables, y la tecnología se convierte en una herramienta estándar del mercado.

### Principales fuentes generadoras de datos

En el contexto actual, el volumen de datos generados a nivel global sigue creciendo de forma exponencial. Las fuentes de datos son diversas y provienen de múltiples sectores y actividades. 

| **Categoría de Fuente** | **Descripción** | **Ejemplos Clave** |
| --- | --- | --- |
| **Generados por Personas** | Datos derivados de la actividad social, comunicativa y creativa de los usuarios. | Redes sociales, correos electrónicos, encuestas y clics en sitios web. |
| **Transacciones** | Registros generados por operaciones comerciales, financieras o de servicios. | Transferencias bancarias, compras en línea y reservas de viajes. |
| **Marketing Web** | Datos de rastreo para analizar el comportamiento del usuario y optimizar publicidad. | Cookies, historial de navegación y mapas de calor (rastreo del cursor). |
| **Biométricos** | Identificadores físicos o conductuales únicos utilizados para seguridad y acceso. | Huellas dactilares, reconocimiento facial y patrones de voz. |
| **Máquina a Máquina (M2M)** | Comunicación autónoma entre dispositivos sin intervención humana directa. | Sensores industriales, telemetría GPS y medidores inteligentes de servicios. |
| **Internet de las Cosas (IoT)** | Dispositivos domésticos y urbanos conectados que recopilan datos de uso. | Electrodomésticos inteligentes, cámaras de seguridad y vehículos conectados. |

## Clasificación de los Datos según su Estructura

En el ecosistema del Big Data, la capacidad de procesar la información depende directamente de cómo esté organizada originalmente.

| **Tipo de Dato** | **Definición** | **Características** | **Ejemplos** | **Ventajas** | **Inconvenientes** |
| --- | --- | --- | --- | --- | --- |
| **Estructurados** | Datos organizados en esquemas definidos (filas y columnas), típicos de bases de datos relacionales (SQL). | • Organización rígida.
• Esquemas predefinidos.
• Consultas fáciles mediante SQL. | Registros bancarios, inventarios, bases de datos de empleados. | Facilitan el análisis rápido y la integración con sistemas tradicionales. | No aptos para manejar grandes volúmenes de datos heterogéneos. |
| **Semiestructurados** | Datos sin esquema fijo pero con marcadores (etiquetas o claves) que separan los elementos. | • Flexibilidad mayor que los estructurados.
• Uso de etiquetas o delimitadores.
• Requieren herramientas específicas. | Archivos **JSON**, **XML**, metadatos de correos electrónicos. | Gran adaptabilidad a datos complejos y heterogéneos. | Necesitan procesamiento adicional para análisis tradicionales. |
| **No Estructurados** | Datos sin organización interna ni formato predefinido. Representan la mayor parte de la información actual. | • Sin etiquetas ni formato definido.
• Alta heterogeneidad.
• Máximo nivel de complejidad. | Imágenes, videos, audios, texto libre (redes sociales). | Contienen información rica y profunda para obtener *insights* valiosos. | Exigen tecnologías avanzadas (Hadoop, Spark, NLP, Machine Learning). |

### **Las V’s del Big data. Un enfoque práctico**

Este esquema amplía las dimensiones técnicas originales con factores de calidad y negocio.

| **V de Big Data** | **Definición** | **Aplicación Práctica** |
| --- | --- | --- |
| **1. Volumen** | La magnitud de los datos (Terabytes a Zettabytes). | Almacenar billones de registros de tarjetas de crédito. |
| **2. Velocidad** | El ritmo de generación y procesamiento en tiempo real. | Detectar un fraude bancario en el milisegundo que ocurre. |
| **3. Variedad** | La combinación de datos estructurados, semi y no estructurados. | Analizar un video de YouTube junto con sus comentarios (texto). |
| **4. Veracidad** | La fiabilidad y limpieza de los datos (evitar sesgos o errores). | Filtrar datos erróneos de un sensor de temperatura estropeado. |
| **5. Viabilidad** | La capacidad de la organización para manejar esos datos. | ¿Tenemos el presupuesto y la tecnología (Spark/Hadoop) necesarios? |
| **6. Visualización** | El modo en que se presentan los datos para ser legibles. | Crear un dashboard en PowerBI o Tableau que un directivo entienda. |
| **7. Valor** | El beneficio económico o social extraído de los datos. | Optimizar una ruta logística para ahorrar 10% en combustible. |

## Sistemas Distribuidos y su relación con el Big Data

La evolución de la informática ha transitado desde los sistemas aislados y costosos de mediados del siglo XX hacia un ecosistema de colaboración masiva definido por los **sistemas distribuidos**. Mientras que la arquitectura **cliente-servidor** sentó las bases mediante una división clara de roles y un modelo de solicitud-respuesta, el paradigma actual extiende esta idea a redes complejas de múltiples nodos interconectados. 

Esta transición no solo ha permitido superar las limitaciones de escala y costo de los antiguos equipos independientes, sino que ha dotado a la infraestructura moderna de la robustez, flexibilidad y **escalabilidad** necesarias para dar soporte a las demandas del **Big Data**. Así, lo que comenzó como una interacción binaria entre plataformas heterogéneas se ha convertido hoy en el motor que permite procesar volúmenes masivos de información de manera eficiente y segura.

### Definición de Sistema distribuido

Un sistema distribuido es un conjunto de componentes de hardware y software que se ejecutan en múltiples nodos interconectados y colaboran entre sí para lograr un objetivo común. Estos sistemas permiten el procesamiento paralelo de datos y la distribución de la carga de trabajo para mejorar el rendimiento y la escalabilidad.

**¿Cuáles son los beneficios de los entornos distribuidos?**

Algunos de los principales beneficios de los entornos distribuidos incluyen la escalabilidad, la tolerancia a fallos, el rendimiento mejorado y la capacidad de procesar grandes volúmenes de datos de manera eficiente. Estos sistemas también pueden ofrecer una mayor disponibilidad y capacidad de recuperación en comparación con los sistemas centralizados.

### Componentes de un Sistema Distribuido

Un sistema distribuido está compuesto por diversos elementos que trabajan en conjunto para permitir la ejecución distribuida de aplicaciones y el procesamiento de datos a través de múltiples nodos interconectados. A 
continuación, se describen sus principales componentes:

- **Programas:** Conjunto de instrucciones que conforman las aplicaciones o procesos que se ejecutan en el sistema distribuido.
- **Procesos:** Instancias en ejecución de los programas, que pueden ejecutarse en distintos nodos dentro del sistema.
- **Datos:** Información estructurada y no estructurada que es procesada y manipulada por los programas dentro del sistema distribuido.
- **Componentes varios:** Elementos de hardware y software que sustentan la ejecución del sistema, incluyendo servidores, bases de datos y sistemas operativos.
- **Redes de computadores:** Infraestructura que permite la comunicación entre los diferentes componentes del sistema, facilitando el intercambio de datos.
- **Protocolos:** Conjunto de reglas y estándares que definen cómo se lleva a cabo la comunicación y el formato de los mensajes intercambiados entre los 
componentes.
- **Middleware:** Capa de software que facilita la ejecución distribuida al gestionar la interacción entre los componentes y ocultar la complejidad de la 
distribución al desarrollador.

### Sistemas distribuidos y big data

Los sistemas distribuidos y el Big Data están estrechamente relacionados, 
ya que el procesamiento y análisis de grandes volúmenes de datos requieren infraestructuras distribuidas que permitan gestionar eficientemente la gran cantidad de datos (Volumen), la velocidad con la que se generan y procesan, y la variedad de formatos que pueden presentar (estructurados, no estructurados y semiestructurados). 

En un entorno de Big Data, los sistemas distribuidos proporcionan la capacidad de escalabilidad horizontal, permitiendo distribuir el almacenamiento y procesamiento en múltiples nodos interconectados. Además, garantizan la veracidad de los datos al incorporar mecanismos de tolerancia a fallos y replicación, y mejoran el valor extraído de los datos mediante arquitecturas como Hadoop, Apache Spark y bases de datos distribuidas. 

> Así, los sistemas distribuidos son la base tecnológica que hace posible 
el procesamiento eficiente y en tiempo real de los grandes volúmenes de 
datos característicos del Big Data.
> 

### Contextualizacion de los sistemas distribuidos

En la actualidad, el crecimiento exponencial de los datos y la necesidad de un procesamiento eficiente han impulsado una evolución radical en los sistemas distribuidos. Estos sistemas permiten repartir la carga de trabajo entre múltiples nodos interconectados, introduciendo un cambio de paradigma fundamental: la **localidad del dato**. 

En lugar de trasladar volúmenes masivos de información hacia un nodo central, lo cual generaría cuellos de botella críticos en la red, los sistemas modernos operan bajo la premisa de que **"el proceso viaja al dato"**. Al acercar el procesamiento al lugar donde se almacena la información, se optimiza el rendimiento y se permite una escalabilidad que sería imposible en arquitecturas centralizadas.

Esta arquitectura se apoya en la **computación distribuida** como pilar fundamental, ejecutando tareas en paralelo para maximizar la eficiencia operativa. 

- Para asegurar que el sistema sea confiable, se implementan mecanismos de **tolerancia a fallos y replicación**, garantizando la disponibilidad de los datos mediante su duplicación en distintos servidores.
- Además, destaca su capacidad de **elasticidad**, que permite ajustar los recursos de forma dinámica según la demanda, y el uso de **commodity hardware**, lo que hace que estas infraestructuras sean mucho más rentables al utilizar equipos de bajo costo y fácil acceso en lugar de supercomputadoras propietarias.

El procesamiento a gran escala dio un salto cualitativo cuando Google revolucionó el sector con el concepto de **MapReduce**, un modelo que segmenta y procesa información masiva de manera distribuida. Esta innovación propició el desarrollo de sistemas de ficheros específicos como **GFS** (Google File System) y su homólogo en el ecosistema abierto, **HDFS** (Hadoop Distributed File System), los cuales permiten gestionar cantidades ingentes de datos como si fuera una única unidad lógica. 

> *“Hoy en día, este modelo es indispensable para responder al auge de los dispositivos móviles, facilitando la analítica en streaming y el procesamiento en tiempo real, lo que permite a las aplicaciones modernas reaccionar instantáneamente a eventos globales.”*
> 

---

### Conceptos clave en los sistemas distribuidos

Para comprender mejor el funcionamiento de los sistemas distribuidos, es necesario introducir algunos conceptos fundamentales relacionados con el manejo y procesamiento de la información.

**Procesamiento de datos**

El **procesamiento de datos** consiste en transformar datos en bruto en información estructurada y útil. En los sistemas distribuidos, este proceso se realiza sobre grandes volúmenes de datos repartidos entre múltiples nodos, lo que permite manejar cantidades de información mucho mayores que en sistemas tradicionales.

**Análisis de datos**

Una vez procesados, los datos pasan a la fase de **análisis**, donde se aplican diferentes técnicas para identificar **patrones, tendencias o relaciones**. Este análisis permite extraer conocimiento relevante que puede utilizarse para optimizar procesos o apoyar la toma de decisiones.

**Procesamiento distribuido**

Cuando el volumen o la velocidad de los datos es muy elevado, entra en juego el **procesamiento distribuido**.

En este modelo:

- Los datos se **dividen en fragmentos o particiones**.
- Cada fragmento se procesa **de forma paralela en diferentes nodos**.
- Los resultados se **agregan posteriormente** para obtener el resultado final.

Este enfoque aporta varias ventajas clave:

- **Mayor velocidad de procesamiento**
- **Escalabilidad horizontal**
- **Tolerancia a fallos**

### Sistemas distribuidos vs sistemas paralelos

Aunque ambos permiten ejecutar tareas simultáneamente, su organización es distinta:

| Sistema distribuido | Sistema paralelo |
| --- | --- |
| Recursos ubicados en **diferentes máquinas** | Recursos dentro de **una misma máquina o sistema** |
| Comunicación a través de **red** | Comunicación mediante **interconexiones internas** |
| Escalabilidad mediante **más nodos** | Escalabilidad limitada por el hardware |

**Arquitectura cliente-servidor**

Uno de los modelos más utilizados en sistemas distribuidos es la **arquitectura cliente-servidor**. En este modelo el **Cliente** solicita un servicio o recurso y el **Servidor** procesa la petición y devuelve una respuesta. La comunicación se basa en un **modelo solicitud–respuesta** a través de la red.

**Clústeres de servidores**

Para mejorar el rendimiento y la disponibilidad, los sistemas distribuidos suelen utilizar **clústeres de servidores**.

Un **clúster** es un conjunto de servidores que trabajan de forma coordinada como si fueran un único sistema.

Sus principales características son:

- **Alta disponibilidad** → el sistema sigue funcionando aunque falle un nodo.
- **Balanceo de carga** → distribución eficiente del trabajo entre servidores.
- **Escalabilidad** → posibilidad de añadir nuevos nodos fácilmente.
- **Tolerancia a fallos** → mediante replicación y redundancia.
- **Mejor rendimiento** → al procesar tareas en paralelo.

---

### Teorema CAP

En los sistemas distribuidos aparece una limitación fundamental conocida como **teorema CAP**, que explica los compromisos que deben asumir estos sistemas.

En sistemas tradicionales, mejorar el rendimiento era relativamente sencillo:

- **Escalado vertical** → aumentar la potencia del hardware.
- **Optimización del software** → mejorar el uso de los recursos.

Sin embargo, cuando los datos se distribuyen entre múltiples nodos conectados por red, surgen nuevos problemas relacionados con la coordinación y los fallos de comunicación.

El **teorema CAP** establece que **un sistema distribuido no puede garantizar simultáneamente tres propiedades**:

- **Consistencia (Consistency)** → todos los nodos muestran los mismos datos en todo momento.
- **Disponibilidad (Availability)** → cada solicitud recibe siempre una respuesta válida.
- **Tolerancia a particiones (Partition Tolerance)** → el sistema sigue funcionando incluso si existen fallos en la red entre nodos.

Cuando ocurre una **partición de red**, el sistema debe priorizar entre:

- **Consistencia (CP)**
- **Disponibilidad (AP)**

> Por ello, muchas tecnologías distribuidas se diseñan priorizando **dos de estas tres propiedades** según el caso de uso.
> 

### Reto de la concurrencia de usuarios

En los **sistemas distribuidos**, uno de los desafíos más críticos es la concurrencia de usuarios, es decir, la capacidad del sistema para manejar múltiples solicitudes simultáneas sin comprometer su rendimiento. A medida que el número de usuarios aumenta, surgen distintos retos técnicos que deben abordarse para garantizar un funcionamiento eficiente y estable.

- **La escalabilidad:** permite que el sistema crezca sin experimentar degradación en los 
tiempos de respuesta. Para lograrlo, es fundamental diseñar una infraestructura capaz de expandirse dinámicamente sin afectar el rendimiento general.
- **La disponibilidad:** los sistemas deben ser capaces de procesar múltiples **consultas simultáneas** sin interrupciones. Esto requiere mecanismos eficientes de gestión de recursos y optimización en la distribución de cargas de trabajo.
- **Balanceo de carga:** evita **cuellos de botella**, distribuyendo equitativamente las solicitudes entre los distintos servidores o nodos. Una mala gestión en este aspecto puede derivar en un uso desigual de los recursos, afectando negativamente la eficiencia del sistema.
- **Resistencia a fallos:** asegurando la continuidad del servicio incluso en situaciones de alta demanda o fallos inesperados. Sin embargo, si la arquitectura no está correctamente diseñada, el sistema podría enfrentarse a **posibles saturaciones**, afectando la experiencia de los usuarios.
- **Tiempo de respuesta:** los usuarios esperan obtener información en el menor tiempo posible. En entornos distribuidos, este aspecto puede volverse complejo debido al llamado **efecto de caja negra**, donde el sistema se comporta como un conjunto de procesos opacos cuya latencia puede ser difícil de diagnosticar y optimizar.

### Latencia vs rendimiento

En el diseño y optimización de **sistemas distribuidos**, dos métricas clave determinan la eficiencia y capacidad de respuesta del sistema: 

- **La latencia** se refiere al tiempo que tarda una operación específica en completarse, lo cual es fundamental para garantizar una respuesta rápida a las solicitudes de los usuarios (medida en milisegundos - ms).
- Por otro lado, **el rendimiento** mide la cantidad de trabajo que un sistema puede procesar en un período determinado de tiempo. Se expresa en términos de operaciones por segundo, utilizando métricas como FLOPS (Floating Point Operations Per Second) en sistemas de alto rendimiento.

### OLAP y OLTP en sistemas distribuidos

En los sistemas distribuidos, el tipo de procesamiento de datos determina cómo se diseñan las bases de datos y la infraestructura. Existen dos enfoques principales: **OLAP** y **OLTP**.

- **OLAP (Online Analytical Processing):** Se utiliza para **análisis de datos e informes históricos**. Los datos se organizan en múltiples dimensiones (tiempo, producto, ubicación, etc.), permitiendo analizar grandes volúmenes de información.
    
    > Este tipo de procesamiento suele ejecutarse en **data warehouses** y prioriza la capacidad de análisis sobre la velocidad inmediata de respuesta.
    > 
- **OLTP (Online Transaction Processing):** Está orientado a **gestionar transacciones en tiempo real**, como operaciones CRUD (crear, leer, actualizar y eliminar).
    
    > Se utiliza en sistemas con **alta concurrencia**, donde muchos usuarios realizan operaciones simultáneamente, por lo que requiere **respuestas rápidas, alta disponibilidad e integridad de datos**.
    > 

En los sistemas distribuidos, ambos modelos suelen **complementarse**:

- **OLTP** gestiona la operativa diaria en tiempo real.
- **OLAP** permite analizar grandes volúmenes de datos para obtener información estratégica.

### Bases de datos NoSQL (Not Only SQL)

Las **bases de datos NoSQL** surgen como una alternativa a los modelos relacionales tradicionales, especialmente en entornos de **sistemas distribuidos y grandes volúmenes de datos**. Sus características principales son:

- **Mayor flexibilidad** en la estructura de los datos.
- **Escalabilidad horizontal**, añadiendo nuevos nodos al sistema.
- **Tolerancia a fallos**, adecuada para arquitecturas distribuidas.
- Capacidad para almacenar información en distintos formatos: **clave-valor, documentos o grafos**.
- Diseñadas para gestionar **grandes volúmenes de información** en infraestructuras descentralizadas.

**Almacenamiento por columnas**

Dentro del ecosistema NoSQL, una técnica muy utilizada es el almacenamiento por columnas, presente en bases de datos como Apache Cassandra, HBase o Google Bigtable. Sus características principales son:

- Los datos se almacenan agrupados por columnas en lugar de por filas.
- Compresión más eficiente, ya que los valores de una misma columna suelen ser similares.
- Consultas selectivas más rápidas, al poder acceder directamente a las columnas necesarias sin leer todo el registro.

### Preguntas básicas sobre sistemas distribuidos

**¿Cuáles son los principales desafíos de los sistemas distribuidos?**

Los retos más importantes incluyen:

- **Concurrencia y coherencia de datos** entre múltiples nodos.
- **Tolerancia a fallos** para mantener el sistema operativo ante errores.
- **Comunicación y sincronización** entre nodos distribuidos.
- **Seguridad de los datos** en entornos de red.
- **Escalabilidad** para soportar el crecimiento del sistema.

---

**¿Qué estrategias se utilizan para la tolerancia a fallos?**

Algunas estrategias habituales son:

- **Replicación de datos** para garantizar disponibilidad.
- **Algoritmos de consenso** para mantener la coherencia entre nodos.
- **Detección y recuperación automática de fallos**.

---

**¿Cuáles son los desafíos de la escalabilidad?**

- Diseñar **algoritmos y protocolos** que funcionen con muchos nodos.
- **Gestionar recursos** para evitar cuellos de botella.
- Reducir la **sobrecarga de comunicación y coordinación** entre nodos.

---

**¿Qué es la consistencia eventual?**

La **consistencia eventual** es un modelo en el que los nodos pueden tener **copias temporales distintas de los datos**, pero el sistema garantiza que **con el tiempo todas convergerán a un estado consistente**.

Se utiliza para mejorar **rendimiento y disponibilidad**.

---

**¿Cuáles son los desafíos al diseñar una arquitectura Big Data?**

Los principales son:

- Manejar **grandes volúmenes de datos**.
- Gestionar **variedad de fuentes y formatos**.
- Procesar datos a **alta velocidad**.
- Garantizar **calidad, seguridad y privacidad de los datos**.
- Mantener la **escalabilidad** del sistema.

## Apache Hadoop

El origen de Hadoop se remonta a principios de los años 2000, cuando Google desarrolló tecnologías clave para manejar grandes volúmenes de datos de manera eficiente. En 2003, Google presentó el Google File System (GFS), un sistema de almacenamiento distribuido diseñado para gestionar datos a gran escala con alta tolerancia a fallos. Posteriormente, en 2004, Google publicó un artículo sobre MapReduce, un modelo de programación que simplifica el procesamiento de grandes volúmenes de información en clústeres distribuidos. 

Desde entonces, Hadoop ha evolucionado hasta convertirse en un ecosistema completo, con múltiples componentes como HDFS (Hadoop Distributed File System), YARN gestión de recursos), Hive (consulta de datos), HBase (base de datos NoSQL) y Spark procesamiento en memoria). Gracias a su escalabilidad y flexibilidad, Hadoop ha sido adoptado ampliamente en la industria, siendo utilizado en sectores como finanzas, telecomunicaciones, salud y comercio electrónico para el análisis y procesamiento de Big Data. 

### Características principales

Hadoop es un **ecosistema de código abierto** de la Apache Software Foundation para **procesamiento distribuido de grandes volúmenes de datos**. Sus principales características son:

- **Código abierto y respaldado por empresas líderes** → uso y mejora sin licencia, comunidad activa.
- **Procesamiento distribuido** → divide datos y tareas en múltiples nodos para ejecución paralela.
- **Tolerancia a fallos y alta disponibilidad** → replicación de datos y redirección automática de tareas.
- **Escalabilidad masiva** → fácil expansión del clúster según demanda.
- **Extensible** → integración con Spark, Hive, HBase, Pig, etc.
- **Localidad del dato** → los cálculos se realizan cerca de donde se almacenan los datos.
- **Optimización de recursos** → gestión de discos físicos y hardware económico (commodity hardware).
- **HDFS Snapshots** → recuperación eficiente y control de versiones.
- **Rendimiento y fiabilidad** → depende de configuración y replicación de datos.
- **No es una base de datos** → funciona como infraestructura para otras herramientas de análisis.

> En pocas palabras: Hadoop permite **procesar grandes volúmenes de datos en clústeres de manera eficiente, escalable y tolerante a fallos**, siendo la base de muchos sistemas Big Data modernos.
> 

### Modos de despliegue de Hadoop

Apache Hadoop puede desplegarse en tres modos principales:

1. **Local (modo por defecto)**
    - Se ejecuta como **un único proceso Java** en la máquina local.
    - No hay demonios activos; las tareas se ejecutan en la **JVM local** mediante el **local job runner**.
    - Útil para **desarrollo inicial y depuración de código**.
2. **Pseudo-distribuido**
    - Varios procesos Java se ejecutan en la **misma máquina**, simulando un clúster distribuido.
    - Los **demonios de Hadoop** se lanzan como en producción, pero todos en la máquina local.
    - Permite **testear el código en un entorno similar al de producción**.
3. **Distribuido**
    - Los procesos se ejecutan en un **clúster completo**, maximizando el paralelismo y los recursos disponibles.
    - Los **demonios se ejecutan en nodos distribuidos**.
    - Adecuado para **entornos de producción**.

### Limitaciones de Hadoop

Aunque Hadoop es clave en Big Data, presenta algunas limitaciones:

- **Dependencia del disco** → la comunicación entre tareas usa almacenamiento en disco, aumentando la latencia frente a soluciones en memoria como Spark.
- **API poco expresiva** → MapReduce en Java puede ser compleja y menos intuitiva.
- **Código extenso y repetitivo** → incluso tareas simples requieren mucho código, lo que dificulta el desarrollo y mantenimiento.
- **Requisitos de infraestructura** → necesita clústeres robustos, implicando mayor costo y complejidad.
- **Sobreparticionamiento de datos** → demasiadas particiones pueden ralentizar el procesamiento.

A pesar de esto, sigue siendo fundamental en Big Data, especialmente combinado con herramientas como Spark, Hive o HBase, que mejoran su eficiencia y facilidad de uso.

### Componentes de Hadoop

Hadoop es un **ecosistema modular** que permite **almacenamiento y procesamiento distribuido de datos**. Sus principales componentes son:

1. **HDFS (Hadoop Distributed File System)**
    - Sistema de almacenamiento distribuido.
    - Divide los datos en bloques y los distribuye en varios nodos.
    - **Tolerancia a fallos** mediante replicación.
2. **YARN (Yet Another Resource Negotiator)**
    - Administrador de recursos del clúster (CPU, memoria).
    - Permite ejecutar **varias aplicaciones simultáneamente**.
3. **MapReduce**
    - Modelo de programación para **procesamiento paralelo**.
    - Divide tareas en **Map** (procesamiento) y **Reduce** (agregación).
4. **Common**
    - Biblioteca de utilidades compartidas entre módulos.
    - Incluye funciones de **autenticación, configuración e integración**.
5. **Otros componentes del ecosistema**
    - **Hive** → consultas SQL sobre HDFS.
    - **HBase** → base de datos NoSQL sobre HDFS para consultas rápidas.
    - **Spark** → procesamiento en memoria más rápido que MapReduce.
    - **Flume / Kafka** → ingesta de datos hacia Hadoop.

> Estos módulos permiten que Hadoop integre múltiples tecnologías de Big Data y formen la base de arquitecturas escalables y distribuidas.
> 

### Ecosistema Hadoop

El ecosistema Hadoop es un conjunto de tecnologías y herramientas diseñadas para el almacenamiento, procesamiento y análisis de grandes volúmenes de datos en entornos distribuidos. Su núcleo está compuesto por HDFS (Hadoop Distributed File System), que permite el almacenamiento distribuido de datos, YARN (Yet Another Resource Negotiator), encargado de la gestión de recursos del clúster, y MapReduce, un modelo de programación para el procesamiento paralelo de datos a gran escala.

Además, el ecosistema se complementa con herramientas como Apache Hive, que permite ejecutar consultas SQL sobre Hadoop, Apache HBase, una base de datos NoSQL sobre HDFS, y Apache Spark, un motor de procesamiento en memoria más eficiente que MapReduce. También incluye soluciones para la ingesta de datos como Apache Flume y Apache Kafka.
 Gracias a su escalabilidad, tolerancia a fallos y flexibilidad, el ecosistema Hadoop es una de las soluciones más utilizadas en Big Data, permitiendo a las empresas analizar y gestionar datos de manera eficiente en entornos distribuidos.

### HDFS (Hadoop Distributed File System)

Es un sistema de almacenamiento distribuido para grandes volúmenes de datos, con alta disponibilidad, tolerancia a fallos y escalabilidad horizontal. Divide archivos en bloques distribuidos en múltiples nodos (DataNodes), gestionados por el NameNode.

---

### Características clave

- **Archivos grandes:** Optimizado para GB o más.
- **Particionamiento de datos:** Bloques distribuidos para procesamiento paralelo.
- **Tolerancia a fallos:** Replicación de bloques (factor por defecto: 3).
- **Optimizado para lectura:** “Una escritura, muchas lecturas”.
- **Consistencia fuerte:** Datos coherentes en todo el clúster.
- **Escalabilidad:** Agrega nodos sin afectar rendimiento.
- **Uso extendido:** Base para datalakes, compatible con Spark, Presto, Trino.

---

### Limitaciones

- Alta latencia de red → no optimizado para tiempo real.
- Ineficiente con archivos pequeños → sobrecarga del NameNode.
- No permite múltiples escritores ni edición de archivos existentes (solo append).

---

### Componentes de HDFS

- **NameNode:** Gestor de metadatos, coordina lecturas/escrituras.
- **Secondary/Standby NameNode:** Checkpoints y failover.
- **DataNodes:** Almacenamiento real, replicación, recuperación automática.

**Mecanismos importantes:**

- **Replicación de bloques:** Mantiene varias copias para tolerancia a fallos.
- **Rack Awareness:** Evita que todas las réplicas queden en el mismo rack.
- **Heartbeats:** DataNodes notifican su estado al NameNode cada 3 segundos.

---

### Formatos de archivos en HDFS

- **Texto:** CSV, JSON, secuenciales (clave-valor). Fácil lectura, menos eficiente.
- **Binario optimizado:** Avro (filas), ORC y Parquet (columnar).
    - Parquet → mejor compresión y filtrado por columnas, ideal para análisis.

---

### Lectura y escritura

- El **cliente coordina con NameNode y DataNodes** para acceder a los bloques.
- Lectura → los datos se obtienen de los DataNodes que almacenan las réplicas.
- Escritura → bloques replicados según factor de replicación; distribución optimizada por racks.

---

### Comandos básicos de HDFS

| Paso | Comando | Función |
| --- | --- | --- |
| 1 | `cd /home/bigdata/hadoop-3.3.6/` | Acceder al directorio Hadoop |
| 2 | `sbin/start-dfs.sh` | Inicia HDFS |
| 3 | `bin/hdfs dfs -ls /` | Lista archivos en HDFS |
| 4 | `bin/hdfs dfs -mkdir /ebooks` | Crea directorio |
| 5 | `bin/hdfs dfs -put local_path hdfs_path` | Sube archivo a HDFS |
| 6 | `bin/hdfs dfs -get hdfs_path local_path` | Descarga archivo de HDFS |
| 7 | `bin/hdfs dfs -rm hdfs_path` | Elimina archivo |
| 8 | `sbin/stop-dfs.sh` | Detiene HDFS |

> Nota: No hay `pwd` ni `cd` tradicionales; los archivos están distribuidos en bloques.
> 

### MapReduce

Modelo de programación para **procesar grandes volúmenes de datos** en entornos distribuidos de manera **paralela y tolerante a fallos**. Base del ecosistema Hadoop y precursor de tecnologías modernas como **Apache Spark**.

---

### Fases principales

1. **Map** – Transformación y estructuración
    - Convierte los datos en **pares clave-valor**.
    - Procesamiento **paralelo** de los splits de HDFS.
2. **Shuffle** – Organización de datos intermedios
    - Reparte los pares clave-valor a los nodos de reducción según sus claves.
    - Mezcla y ordena los datos para la fase Reduce.
3. **Reduce** – Agregación y consolidación
    - Agrupa todos los valores de cada clave.
    - Aplica operaciones de agregación para generar resultados finales compactos.

---

### Componentes y ejecución en Hadoop

- **mr-jobhistory-daemon.sh** → registra historial de trabajos MapReduce.
- **mapred-site.xml** → define configuración y framework de ejecución.
- **Splits** → fragmentos de archivos HDFS asignados a tareas Map.
- **Paralelismo y tolerancia a fallos** → si un nodo falla, las tareas se redistribuyen.

---

### Ventajas

- Escalabilidad horizontal y paralelismo eficiente.
- Tolerancia a fallos integrada.
- Permite procesar **petabytes de datos** de forma distribuida.

### Limitaciones

- Curva de aprendizaje elevada (principalmente Java).
- Optimización del rendimiento requiere experiencia en Hadoop.

---

### Ejemplo práctico (teórico)

**Cálculo de media de pulsaciones por equipo**

| Dorsal | Nombre | Equipo | Pulsaciones |
| --- | --- | --- | --- |
| 33 | Contador | Movistar | 110 |
| 1 | Induráin | Banesto | 87 |
| 27 | Armstrong | Sky | 99 |
| 2 | Arroyo | Banesto | 103 |
| 9 | Olano | Banesto | 119 |
| 5 | Ocaña | Banesto | 88 |
| 22 | Smith | Sky | 89 |
| 31 | Valverde | Movistar | 101 |
| 23 | Miller | Sky | 98 |
| 26 | Froome | Sky | 109 |
| 34 | Quintana | Movistar | 112 |

**Resolución con MapReduce:**

- **Map:** asigna cada registro a un par `(Equipo, pulsaciones)`.
- **Shuffle:** agrupa los pulsos por equipo.
- **Reduce:** calcula la **media** de pulsaciones por equipo.

Resultado final:

- **Movistar:** (110 + 101 + 112)/3 = 107.7
- **Banesto:** (87 + 103 + 119 + 88)/4 = 99.25
- **Sky:** (99 + 89 + 98 + 109)/4 = 98.75

### YARN - **Yet Another Resource Manager**

Es el componente central de Hadoop encargado de gestionar los recursos del clúster y distribuirlos eficientemente entre las diferentes aplicaciones que se ejecutan en el sistema. Su principal función es coordinar la asignación de **CPU (cores)** y **memoria (RAM)** para garantizar que cada aplicación disponga de los recursos necesarios sin afectar la ejecución de otras tareas.

YARN opera mediante un mecanismo de reserva y asignación de recursos. Cuando una aplicación solicita recursos para su ejecución, **YARN revisa el estado del clúster**, identificando qué recursos están disponibles en cada nodo. Si hay suficientes recursos libres, asigna a la aplicación los cores y la RAM correspondientes en los nodos disponibles. 

> Gracias a esta arquitectura, **YARN mejora la escalabilidad y flexibilidad** del ecosistema Hadoop, permitiendo la coexistencia de distintos motores de procesamiento como **MapReduce, Spark, Tez y Flink** sobre un mismo clúster, lo que lo convierte en un elemento clave en entornos de Big Data modernos.
>