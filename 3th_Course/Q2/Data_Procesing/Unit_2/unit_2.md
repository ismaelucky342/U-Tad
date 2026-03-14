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