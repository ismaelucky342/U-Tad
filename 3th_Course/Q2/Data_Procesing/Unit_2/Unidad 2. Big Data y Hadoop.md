# Unidad 2. Big Data y Hadoop



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Big Data: Profundizando En La Contextualización](#2-big-data-profundizando-en-la-contextualización)
  - [2.1 Introducción](#21-introducción)
  - [2.2 Generación de datos a los largo de la historia](#22-generación-de-datos-a-los-largo-de-la-historia)
  - [2.3 Evolución de la Gestión de Datos: Retos y Soluciones en el Contexto de Big Data](#23-evolución-de-la-gestión-de-datos-retos-y-soluciones-en-el-contexto-de-big-data)
  - [2.4 ¿Qué es Big data?](#24-qué-es-big-data)
  - [2.5 Grado de madurez de la tecnología Big data](#25-grado-de-madurez-de-la-tecnología-big-data)
  - [2.6 Principales fuentes generadora de datos](#26-principales-fuentes-generadora-de-datos)
  - [2.7 Recordatorio de clasificación de los datos según su estructura](#27-recordatorio-de-clasificación-de-los-datos-según-su-estructura)
  - [2.8 Las V’s del Big data. Un enfoque práctico](#28-las-vs-del-big-data-un-enfoque-práctico)
- [3. Importancia Del Big Data. Casos De Uso](#3-importancia-del-big-data-casos-de-uso)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Casos de uso](#32-casos-de-uso)
- [4. Sistemas Distribuidos Y Su Relación Con Big Data](#4-sistemas-distribuidos-y-su-relación-con-big-data)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Definición de Sistema distribuido](#42-definición-de-sistema-distribuido)
  - [4.3 Componentes de un Sistema Distribuido](#43-componentes-de-un-sistema-distribuido)
  - [4.4 Sistemas distribuidos y big data](#44-sistemas-distribuidos-y-big-data)
  - [4.5 Contextualización de los sistemas distribuidos](#45-contextualización-de-los-sistemas-distribuidos)
  - [4.6 Conceptos relacionados con  sistemas distribuidos](#46-conceptos-relacionados-con-sistemas-distribuidos)
  - [4.7 Teorema del CAP](#47-teorema-del-cap)
  - [4.8 Reto de la concurrencia de usuarios](#48-reto-de-la-concurrencia-de-usuarios)
  - [4.9 Latencia vs rendimiento](#49-latencia-vs-rendimiento)
  - [4.10 OLAP vs OLTP](#410-olap-vs-oltp)
  - [4.11 Bases de datos NoSQL (Not Only SQL)](#411-bases-de-datos-nosql-not-only-sql)
  - [4.12 Preguntas básicas acerca de los sistemas distribuidos](#412-preguntas-básicas-acerca-de-los-sistemas-distribuidos)
- [5. Apache Hadoop](#5-apache-hadoop)
  - [5.1 Introducción (historia)](#51-introducción-historia)
  - [5.2 Características](#52-características)
  - [5.3 Modos de despliegue](#53-modos-de-despliegue)
  - [5.4 Limitaciones de hadoop](#54-limitaciones-de-hadoop)
  - [5.5 Componentes](#55-componentes)
  - [5.6 Ecosistema Hadoop](#56-ecosistema-hadoop)
  - [5.7 HDFS](#57-hdfs)
  - [5.8 MAP REDUCE](#58-map-reduce)
  - [5.9 YARN](#59-yarn)
- [6. Conclusiones](#6-conclusiones)
  - [6.1 Conclusiones de la unidad](#61-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad recordaremos conceptos básicos aprendidos en la asignatura “Ampliación de Bases de datos” si bien profundizaremos en algunos aspectos relevantes así como en conceptos más complejos. Por ejemplo,  ampliaremos el concepto de **Big Data**, contando su evolución a lo largo de la historia y su relevancia en el contexto actual de la gestión de datos. Se explorarán los principales retos y soluciones que han surgido en torno a esta tecnología, así como su grado de madurez y las principales fuentes de generación de datos.

Asimismo, se analizarán las características de los datos según su estructura y la importancia del Big Data a través de casos de uso en diversas industrias. También se presentará el papel de los **sistemas distribuidos**, fundamentales para el procesamiento de grandes volúmenes de datos, destacando conceptos clave como el **Teorema CAP, la concurrencia, la latencia y el rendimiento**. Como he comentado, algunos de estos conceptos ya se han visto y sencillamente se recuerdan, con el fin de darles un enfoque práctico.

Finalmente, se recordará **Apache Hadoop**, una de las tecnologías más relevantes en este ámbito, incidiendo sus características, componentes y ecosistema, y realizando ejecuciones prácticas. Se explorarán sus principales módulos, como **HDFS, MapReduce y YARN**, detallando su funcionamiento y las ventajas que aportan al procesamiento distribuido de datos masivos.

Los apartados a tratar en esta unidad didáctica serán:

- **Conceptualización de Big Data:** evolución histórica y madurez tecnológica.
- **Las V’s del Big Data** y su impacto en la gestión de datos. Recordando cuáles son y viedo casos prácticos de qcómo están implementadas en la industria.
- **Fuentes de generación de datos** y clasificación según su estructura.
- Importancia del**Big Data con casos de uso relevantes.**
- **Profundizaremos en el conocimiento de lo ya aprendido sobre Sistemas distribuidos y su relación con Big Data,** incluyendo su definición, componentes y desafíos.
- **Apache Hadoop**, su ecosistema y principales componentes como HDFS, MapReduce y YARN.



#### Objetivos



1. Comprender la evolución y el contexto actual del Big Data. Desde las necesidades que motivaron su aparición hasta la explicación de cada una de sus características.
2. Identificar las principales fuentes y estructuras de los datos masivos.
3. Analizar la importancia y aplicación del Big Data en distintos sectores.
4. Entender el papel de los sistemas distribuidos en la gestión de datos a gran escala.
5. Explorar las características y funcionamiento de Apache Hadoop y sus principales componentes.
6. Aplicar conocimientos adquiridos mediante ejercicios prácticos sobre HDFS y MapReduce.



## 2. Big Data: Profundizando En La Contextualización



### 2.1 Introducción



![image](assets/cm6htzvmr004h3571l3j3z3pc-BIG_20DATA.jpg)



Big Data representa una transformación fundamental en la manera en que se recopilan, almacenan y analizan los datos en la era digital.



En un mundo donde la cantidad de información generada crece exponencialmente, surge la necesidad de herramientas y enfoques innovadores para extraer valor de datos complejos y masivos



### 2.2 Generación de datos a los largo de la historia



La humanidad ha recopilado, almacenado y utilizado información desde tiempos inmemoriales. Desde los primeros métodos rudimentarios hasta los complejos centros de datos actuales, la capacidad de generar y gestionar datos ha evolucionado significativamente, marcando hitos cruciales en el desarrollo de la civilización.



En el Paleolítico se utilizaban palos o muescas en huesos como métodos primitivos de registro y almacenamiento de información. Más adelante, hacia el 2,400 a.C., en Babilonia surgió el uso del ábaco como herramienta de cálculo, acompañado del desarrollo de las primeras bibliotecas, que representaron un avance monumental en la preservación del conocimiento.



Como hecho reseñable y trágico tenemos la destrucción de la biblioteca de Alejandría con la invasión romana. Esta biblioteca fue el primer intento conocido de centralizar todo el saber humano, y su destrucción supuso un retroceso en el conocimiento a la par que surgió la necesidad de buscar métodos para almacenar y preservar la información.

A lo largo de posteriores años, se han ido dando múltiples avances relevantes en el manejo de la información, los cuales no detallaremos por no ser objeto de estudio de esta asignatura. La idea que se pretende transmitir con este apartado es que desde siempre ha existido la necesidad de recopilar, almacenar y procesar información.



#### ¿qué es lo que ha cambiado ahora entonces?



Vamos a centrarnos en unos experimentos estadísticos de hace unos años y posteriormente lo compararemos con una situación que se dio hace poco relativamente.

1. Primeramente nombrar los experimentos realizados por John Graunt en 1663  que supusieron el  progreso hacia el análisis sistemático de datos. Dichos análisis estaban destinados a entender y controlar la propagación de la peste bubónica en Europa.
2. ![image](assets/cm7d51w7y00an3j78yzncwtmv-step2-INSD_PRDT_U2_Apartado3-2_Imagen1.jpg)
   Posteriormente en 1854 se dio una epidemia de cólera en Londres. Esta imagen muestra una representación del mapa original que indicaba la residencia de los grupos de individuos afectados por la epidemia.

   Posteriormente se indica qué señala la flecha azul
3. ![image](assets/cm7d51w7y00an3j78yzncwtmv-step3-INSD_PRDT_U2_Apartado3-2_Imagen2.jpg)
   Sobre ese mapa, John Snow lo que hizo fue crear un gráfico de curvas de nivel para señalar las zonas con mayor concentración de afectados obteniendo como resultado el mapa de la imagen.

   Si os fijáis la zona del mapa que tiene el color más cálido y por tanto la mayor concentración de casos coincide con el punto que marcaba la flecha incluida en el primer mapa. En ese punto justamente se encontraba una fuente pública de la cual los vecinos de Londres obtenían agua corriente para su consumo. Analizando dicha fuente se observó que era el foco principal donde se encontraba la proliferación del cólera, y todo aquellos que bebían agua de la misma quedaban infectados.
4. Esto inevitablemente nos lleva a recordar lo vivido hace unos años con la pandemia del COVID. Realizaban analíticas PCR a los individuos, y en Madrid por ejemplo los resultados se agrupaban por calles y barrios decidiendo posteriormente si un barrio debía estar confinado o no.

   Si os fijáis tanto el problema como las bases para abordarlo son los mismos en ambos casos. ¿qué cambia? Básicamente las herramientas empleadas para el análisis, el volumen de datos y el procesado de los mismos prácticamente en tiempo real.



### 2.3 Evolución de la Gestión de Datos: Retos y Soluciones en el Contexto de Big Data



En la evolución de las tecnologías de datos, se han identificado desafíos importantes que han impulsado la creación de nuevas soluciones, como las que ofrece el ecosistema de Big Data. Tradicionalmente, los sistemas de gestión de bases de datos relacionales (RDBMS) han sido el estándar para almacenar y procesar información estructurada. Sin embargo, con la creciente generación de información desestructurada (como imágenes, videos y texto libre) y el aumento exponencial del volumen de datos, estos sistemas han mostrado limitaciones significativas.

Uno de los retos principales es la dependencia de arquitecturas con un único servidor potente. Estas arquitecturas suelen optar por migraciones a servidores más grandes para manejar mayores volúmenes de datos, pero este enfoque tiene varias desventajas: genera altos costos, cuellos de botella, fallos en el rendimiento y un riesgo significativo de Single Point of Failure (SPoF), donde un solo fallo en el sistema puede detener completamente las operaciones.

Adicionalmente, aunque tecnologías como el High Performing Computing (HPC) y el Massively Parallel Processing (MPP) han intentado abordar estos problemas mediante procesamiento paralelo, su implementación y escalabilidad siguen siendo limitadas en comparación con los sistemas distribuidos. Desarrollar estos sistemas de manera eficiente es complejo y conlleva desafíos en la gestión de cuellos de botella y fallos. Además, mover grandes cantidades de datos en estas arquitecturas centralizadas resulta ineficiente.

Es aquí donde Big Data, y herramientas desarrolladas bajo la Fundación Apache, marcan la diferencia. Tecnologías como **Hadoop y Spark** ofrecen soluciones distribuidas que eliminan los riesgos de SPoF al repartir los datos y el procesamiento entre múltiples nodos. Estas herramientas no solo permiten manejar grandes volúmenes de información de manera eficiente, sino que también son capaces de integrar tanto datos estructurados como desestructurados, superando las limitaciones de los sistemas tradicionales.



#### En resumen...



Los problemas históricos en la gestión y procesamiento de datos, como los cuellos de botella, la dependencia de servidores únicos y la ineficiencia en el manejo de grandes volúmenes de información, han sido el motor para el desarrollo de las tecnologías de Big Data. Estas herramientas han redefinido cómo las organizaciones almacenan, procesan y aprovechan la información, proporcionando soluciones escalables y distribuidas que transforman los datos en conocimiento que puede utilizarse.



### 2.4 ¿Qué es Big data?



No existe una definición única.  Según a la fuente a la cual acudas puedes encontrar unas u otras definiciones como se muestra a continuación:



- **Webopedia**  
  Big data es utilizado para describir un volumen masivo de datos estructurados y no estructurados que es tan grande que resulta difícil de procesar utilizando técnicas tradicionales de bases de datos y software.
- **Gartner**  
  Big data es un conjunto de activos de información de alto volumen, alta velocidad y/o alta variedad que requieren nuevas formas de procesamiento para permitir una mejor toma de decisiones, descubrimiento de información y optimización de procesos.
- **National Institute of Standards and Technology (USA)**  
  Big Data consiste en conjuntos de datos extensos, caracterizados principalmente por volumen, velocidad y/o variedad, que requieren una arquitectura escalable para un almacenamiento, manipulación y análisis eficientes.
- **IBM**  
  Big data es el término para una colección de conjuntos de datos tan grandes y complejos que se vuelve difícil procesarlos utilizando herramientas de gestión de bases de datos tradicionales o aplicaciones de procesamiento de datos convencionales.



Pero todas las definiciones comparten en menor o mayor medida los mismos conceptos. Podemos por tanto concluir una definición para nosotros:



- **Por un lado**  
  Con el término Big data nos referimos al análisis masivo de datos. El volumen es de tal proporción que las técnicas y herramientas clásicas que se venían utilizando hasta ahora para la recopilación, almacenamiento y procesado de datos resultan ineficientes ya que dan tiempos de respuestas no asumibles. Necesitamos tener resultados antes.
- **Por otro lado**  
  Big Data hace también referencia a todas las herramientas modernas y nuevas tecnología que permiten la ingestión, el almacenamiento y el tratamiento de tal volumen de datos.



### 2.5 Grado de madurez de la tecnología Big data



Para justificar el grado de madurez de la tecnología Big Data vamos a utilizar como herramienta una gráfica ampliamente conocida que se denomina Curva de Gartner.

La **Curva de Gartner**, conocida también como el **"Hype Cycle"**, es una representación gráfica que ilustra el ciclo de vida de la adopción y madurez de una tecnología o innovación. Fue introducida por la consultora Gartner y se utiliza ampliamente para analizar las expectativas del mercado frente a nuevas tecnologías. Su objetivo principal es proporcionar una visión estratégica sobre cómo las tecnologías emergentes evolucionan desde su lanzamiento hasta su adopción madura.



La curva se divide en cinco fases principales:



![image](assets/cm7d5vgid01613j78na72uz01-INSD_PRDT_U2_Apartado3-5_Imagen4.jpg)

- **Lanzamiento de la Tecnología (Innovation Trigger)**  
  - En esta fase inicial, se introduce una nueva tecnología o innovación al mercado. Aunque aún no existen aplicaciones prácticas generalizadas, hay un alto interés por su potencial.
  - Las expectativas son alimentadas por avances iniciales, investigaciones, o demostraciones de prueba de concepto.
- **Pico de Expectativas Infladas (Peak of Inflated Expectations)**  
  - Aquí, la tecnología gana popularidad rápidamente debido a las altas expectativas que genera. Sin embargo, estas expectativas suelen ser exageradas, y muchas veces no se basan en resultados reales.
  - Es común que haya una gran inversión inicial y que surjan aplicaciones experimentales que prometen transformar industrias completas.
- **Valle de la Desilusión (Trough of Disillusionment)**  
  - La realidad comienza a establecerse: muchas implementaciones iniciales fracasan o no cumplen con las expectativas generadas.
  - Las organizaciones empiezan a cuestionar la viabilidad de la tecnología y el mercado experimenta un descenso en el entusiasmo.
- **Pendiente de la Iluminación (Slope of Enlightenment)**  
  - En esta fase, las organizaciones que perseveraron comienzan a identificar usos prácticos y sostenibles de la tecnología.
  - Los enfoques se vuelven más realistas y los beneficios tangibles comienzan a aparecer.
- **Meseta de la Productividad (Plateau of Productivity)**  
  Finalmente, la tecnología alcanza su madurez y adopción generalizada. Los estándares están bien definidos, y la tecnología se convierte en una herramienta común en la industria.



#### ¿En qué fase consideráis que se encuentra Big data en la actualidad?



Si revisamos la image siguiente correspondiente a la curva de Gartner de 2012 comprobamos que en este momento es cuando se empezó a hablar de Big Data y las organizaciones reconocieron su potencial para transformar negocios. Durante los primeros años, Big Data fue considerado una solución milagrosa que podía resolver cualquier problema empresarial alcanzando el pico de expectativas. 

Pasados 3 años en 2015 nos encontramos con que Big data tiene otra posición en la curva como se puede ver en la imagen.

Se trata del valle de la desilusión. Las organizaciones enfrentaron problemas al lidiar con la complejidad de los sistemas distribuidos y la falta de especialistas en datos. 

Si saltamos a la gráfica de 2020 (ver siguiente imagen) comprobamos que Big data ha desaparecido. 

Big data, como tecnología, antes de 2020 ya había pasado por la fase de Pendiente de iluminación, con la aparición de tecnologías como Hadoop y Spark, junto con enfoques más realistas, Big Data comenzó a generar resultados sostenibles. Posteriormente se asentó en la Meseta de productividad hasta desaparecer de las curvas.  

Hoy en día, Big Data está integrado en las estrategias de negocio, y su uso es generalizado en análisis predictivos, inteligencia artificial y machine learning.



#### En resumen



### 2.6 Principales fuentes generadora de datos



Aunque ya se han visto, en otras asignaturas, diversas fuentes origen de la masiva generación de datos que tenemos en la actualidad,  conviene recordarlas y sobretodo verlas desde la perspectiva de esta asignatura.

En el contexto actual, el volumen de datos generados a nivel global sigue creciendo de forma exponencial. Las fuentes de datos son diversas y provienen de múltiples sectores y actividades.

A continuación, se enumeran las principales categorías de fuentes de datos:



#### Datos producidos por personas



Estos datos son generados por las actividades cotidianas de los usuarios y constituyen una fuente clave para el análisis de comportamientos humanos. Ejemplos incluyen:



•

Correos electrónicos: Miles de millones de correos electrónicos enviados diariamente. 

•

Redes sociales: Publicaciones, comentarios, imágenes y videos compartidos en plataformas como Facebook, Twitter e Instagram. 

•

Encuestas y formularios: Datos recopilados de cuestionarios en línea. 

•

Interacción con sitios web: Incluye clics, formularios completados y actividades en plataformas de comercio electrónico.



#### Datos generados entre máquinas (M2M - Machine to Machine)



Los dispositivos inteligentes conectados generan datos de manera autónoma al comunicarse entre sí. Este tipo de datos es fundamental en el Internet de las cosas (IoT). Ejemplos incluyen:



•

Termómetros y sensores: Dispositivos de monitoreo ambiental. 

•

GPS: Información de ubicación y movimiento recopilada en tiempo real. 

•

Medidores inteligentes: Contadores de electricidad, agua y gas que transmiten datos de consumo a los proveedores.



#### Datos biométricos.



Provenientes de dispositivos que capturan características únicas de los individuos, utilizados principalmente en seguridad y autenticación. Ejemplos:



•

Sensores de huellas dactilares: Implementados en teléfonos inteligentes y sistemas de control de acceso

•

Escáneres de retina y reconocimiento facial: Comunes en aeropuertos y dispositivos electrónicos.

•

Reconocimiento de voz: Utilizado en asistentes virtuales como Alexa, Google Assistant o Siri.



#### Datos de marketing web.



Se generan al rastrear y analizar la actividad de los usuarios en internet para comprender su comportamiento. Incluyen:



•

Rastreo del cursor: Información sobre cómo los usuarios interactúan con las páginas web. 

•

Historial de navegación: Datos sobre los sitios visitados y el tiempo dedicado a cada página. 

•

Cookies y metadatos: Información capturada para optimizar estrategias de marketing y personalización de contenido.



#### Datos de transacciones.



Estas fuentes provienen de las operaciones realizadas en sistemas digitales, como:



•

Transferencias bancarias: Información sobre pagos, depósitos y movimientos financieros. 

•

Reservas de vuelos: Registros de itinerarios y datos de pasajeros. 

•

Compras en línea: Detalles de productos adquiridos, cantidades y métodos de pago.



#### Datos generados por dispositivos de IoT (Internet de las Cosas).



Estos datos están vinculados a los dispositivos inteligentes conectados a la red. Ejemplos incluyen:



•

Electrodomésticos inteligentes: Refrigeradores, lavadoras y otros aparatos que recopilan datos de uso. 

•

Automóviles conectados: Vehículos que generan datos de telemetría, rutas y diagnósticos. 

•

Cámaras de seguridad: Videovigilancia que produce datos visuales.



#### Mira el siguiente video



En el siguiente video se comentan algunos usos prácticos a partir de los datos obtenidos de dichas fuentes.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652185_1/scormcontent/assets/Video%201%20CasospractFuentes.mp4?v=1)



### 2.7 Recordatorio de clasificación de los datos según su estructura



Hasta el momento habéis visto a lo largo de varias asignaturas la clasificación de los datos en estructurados, no estructurados y semiestructurados. Ciertas asignaturas se han centrado en un tipo de ellos en particular como la asignatura de bases de datos relaciones y posteriormente habéis cursado otras como ampliación de bases de datos donde habéis empleado otros tipos de datos.



El objetivo de este apartado es recordar esta clasificación y sus características , es por ellos que se incluye la siguiente tabla a modo de resumen:

| Tipos de datos | Definición | Características | Ejemplos | Ventajas | Inconvenientes |
| --- | --- | --- | --- | --- | --- |
| Estructurados | Los datos estructurados son aquellos organizados de manera definida, generalmente en forma de filas y columnas en bases de datos relacionales (SQL). Este tipo de datos es fácilmente accesible y procesable mediante herramientas tradicionales de análisis y bases de datos. | Organización rígida en tablas, con esquemas predefinidos. Estructura fija: cada columna tiene un tipo de dato específico. * Fácil de consultar mediante lenguajes como SQL. | Registros bancarios (número de cuenta, saldo, historial de transacciones). Inventarios de productos (número de referencia, precio, stock disponible). Bases de datos de empleados (nombres, cargos, salarios). | Su estructura facilita el análisis rápido y la integración con sistemas de gestión. | No es adecuado para manejar grandes volúmenes de datos no homogéneos. |
| Semiestructurados | Los datos semiestructurados son aquellos que no se ajustan completamente a un esquema fijo, pero poseen una cierta organización que los hace más fáciles de analizar que los no estructurados. Generalmente, estos datos incluyen etiquetas o delimitadores que proporcionan estructura parcial. | No están organizados en tablas, pero incluyen elementos que indican relaciones (e.g., etiquetas XML o claves en JSON). Mayor flexibilidad que los datos estructurados. * Necesitan herramientas especializadas para el análisis. | Archivos JSON utilizados en APIs y sistemas web. Correos electrónicos (metadatos como remitente, asunto, y cuerpo del mensaje). Archivos XML utilizados en configuraciones o intercambios de datos entre sistemas. | Adaptabilidad a datos complejos y heterogéneos . | Requieren procesamiento adicional para integrarse en análisis tradicionales. |
| No estructurados | Los datos no estructurados carecen de cualquier tipo de organización predefinida. Representan la mayoría de los datos generados actualmente y requieren tecnologías avanzadas para su almacenamiento y análisis. | No tienen formato definido ni etiquetas que estructuren la información. Representan un desafío mayor para el análisis debido a su heterogeneidad. | Imágenes y videos (archivos multimedia de cámaras de seguridad o redes sociales). Texto libre (comentarios en redes sociales, reseñas de productos). Audio (grabaciones de voz en asistentes virtuales como Alexa o Google Assistant). | Representan una gran riqueza de información que, una vez procesada, puede generar insights valiosos. | Su análisis requiere tecnologías avanzadas como aprendizaje automático, procesamiento de lenguaje natural (NLP) o herramientas Big Data como Hadoop y Spark. |



### 2.8 Las V’s del Big data. Un enfoque práctico



Al igual que en el marketing existen las conocidas «4P» (Producto, Precio, Promoción y Distribución (en inglés Placement)), en el ámbito del Big Data se han identificado características esenciales agrupadas bajo la inicial V debido a que representan conceptos clave en su manejo y análisis. Vamos a recordarlas.

Las tres principales V’s del Big Data, que ya has estudiado y abordado en profundidad el semestre anterior, son : **Volumen, Velocidad y Variedad**. Añadiéndose poco después la de **Veracidad**, tal y como se muestra en la siguiente imagen.



![image](assets/cm7d7sijv02eo3j78yqbw1wia-INSD_PRDT_U2_Apartado4_Imagen8.jpg)



Posteriormente diversos autores han ampliado la lista para incluir más propiedades como se puede observar en las siguientes imágenes:



![image](assets/cm7d7uyhv02fa3j78psq6vh61-INSD_PRDT_U2_Apartado4_Imagen9.jpg)



En la actualidad, las 7 «V» del Big Data que tienen mayor aceptación son las siguientes:



- **Volumen**  
  Quizás sea la principal de todas. A continuación se muestra un video explicativo/recordatorio acerca del volumen. Es importante conocer tanto las unidades como su equivalencia si las llevásemos al mundo de las distancias.
- **Velocidad**  
  Para refrescar esta característica puede resultar útil ver el siguiente video, que aunque tiene algunos años, muestra claramente una implementación real que hace uso de esta característica.
- **Variedad**  
  Entendiéndola en sentido amplio. Por un lado teniendo en cuenta la tipología de datos. Por otro también las formas, fuentes y dominios de conocimiento en los que se registran.
- **Veracidad**  
  Este aspecto es crucial, ya que los análisis basados en datos de baja calidad pueden conducir a decisiones e investigaciones erróneas.

  A modo de recordatorio mencionaremos alguno de  los principales problemas relacionados con la calidad de los datos como son: **Datos inexactos o erróneos, Datos inconsistentes, Datos incompletos o Datos ambiguos**. Seguramente en otras asignaturas os han enseñado las estrategias y enfoques rigurosos para abordar estos problemas como: **Detectar anomalías de forma temprana o identificar y tratar conjuntos de datos dispersos e incompletos.**
- **Variabilidad**  
  En este contexto, los modelos de análisis y predicción requieren actualizaciones y revisiones periódicas . Vamos a ver un ejemplo práctico de cómo la variabilidad influye en el Big data en el siguiente video:
- **Visualización**  
  La visualización en Big Data se refiere a cómo los datos son presentados de manera gráfica y comprensible tras su procesamiento. Aquí entran en juego conceptos como el storytelling, donde los datos cuentan una historia que apoya la narrativa del análisis e insights que son los aprendizajes que se descubren en las visualizaciones. Esto se verá más en etalle en la asignatura de visualización.
- **Valor**  
  El verdadero valor surge cuando los datos permiten obtener conocimiento que puede traducirse en acciones estratégicas y decisiones informadas.



## 3. Importancia Del Big Data. Casos De Uso



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-INSD_PRDT_U2_Apartado5_Imagen10.jpg)



En este capitulo comentaremos algunos casos de uso en los que se han puesto en marcha proyectos de Big data.



Cuando nos enfrentamos al comienzo de un proyecto Big data lo primero que hay que decidir es si vamos a  utilizar herramientas ya existentes o si por el contrario vamos a crear soluciones específicas que se adapten a las necesidades del proyecto



Otro concepto primordial que hay que manejar a la hora de realizar proyectos de Big Data es el de Datalake.

Un Data Lake es un repositorio centralizado diseñado para almacenar grandes volúmenes de datos en su forma original, sin procesar ni estructurar. A diferencia de un almacén de datos tradicional (Data Warehouse), un Data Lake puede contener datos estructurados, semiestructurados y no estructurados, como registros, imágenes, videos, documentos y datos provenientes de sensores o redes sociales, como se muestra en la siguiente figura:



![image](assets/cm7d8a2ea02js3j78pfkwbeqk-INSD_PRDT_U2_Apartado5_Imagen10.jpg)



### 3.2 Casos de uso



Para la descripción de algunos de los casos de uso mencioandos, tienes a continuación  un video en el cual se describen casos de usos reales del Big data en el mundo empresarial:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652185_1/scormcontent/assets/Video%204%20Casos%20de%20uso.mp4?v=1)



## 4. Sistemas Distribuidos Y Su Relación Con Big Data



### 4.1 Introducción



![image](assets/cm6jbkknd017f35705vqv8gcg-stock-image.jpg)



En este apartado recordaremos algunos aspectos ya estudiados sobre los sistemas distribuidos profundizando en su origen, diseño, componentes y fundamentalmente en su relación con el BIg Data.



Desde los inicios de la informática moderna en 1945 hasta mediados de los años ochenta, los sistemas informáticos se caracterizaban por su gran tamaño, elevado costo y operación independiente. Las computadoras, debido a la falta de tecnología para interconectarlas, funcionaban como sistemas aislados, lo que limitaba significativamente su alcance y posibilidades de colaboración. Sin embargo, el panorama comenzó a cambiar rápidamente a partir de los años ochenta, marcando un hito en la evolución de la informática.



La arquitectura cliente-servidor puede considerarse un subconjunto o precursor de los sistemas distribuidos. Mientras que cliente-servidor se centra en la interacción entre un cliente y un servidor, los sistemas distribuidos extienden esta idea a redes más complejas con múltiples nodos que interactúan entre sí para proporcionar soluciones más robustas, escalables y flexibles.

La arquitectura cliente-servidor se basa en una clara división de responsabilidades entre el cliente, que solicita servicios, y el servidor, que los proporciona. Esta interacción se realiza mediante comunicación a través de la red, empleando un modelo de solicitud-respuesta que asegura un flujo eficiente de datos. Además, esta arquitectura destaca por su escalabilidad, ya que puede ajustarse para manejar mayores demandas, y por su enfoque en la seguridad, con mecanismos que protegen tanto la información como las comunicaciones. Asimismo, promueve la independencia de la plataforma, lo que garantiza que los componentes funcionen en diversos entornos tecnológicos. Por último, su diseño fomenta el desarrollo distribuido, facilitando la colaboración y la modularidad en los sistemas que la implementan.



### 4.2 Definición de Sistema distribuido



Un sistema distribuido es un conjunto de componentes de hardware y software que se ejecutan en múltiples nodos interconectados y colaboran entre sí para lograr un objetivo común. Estos sistemas permiten el procesamiento paralelo de datos y la distribución de la carga de trabajo para mejorar el rendimiento y la escalabilidad.



#### ¿Cuáles son los beneficios de los entornos distribuidos?



Algunos de los principales beneficios de los entornos distribuidos incluyen la escalabilidad, la tolerancia a fallos, el rendimiento mejorado y la capacidad de procesar grandes volúmenes de datos de manera eficiente. Estos sistemas también pueden ofrecer una mayor disponibilidad y capacidad de recuperación en comparación con los sistemas centralizados.



### 4.3 Componentes de un Sistema Distribuido



Un sistema distribuido está compuesto por diversos elementos que trabajan en conjunto para permitir la ejecución distribuida de aplicaciones y el procesamiento de datos a través de múltiples nodos interconectados. A continuación, se describen sus principales componentes:



•

Programas: Conjunto de instrucciones que conforman las aplicaciones o procesos que se ejecutan en el sistema distribuido. 

•

Procesos: Instancias en ejecución de los programas, que pueden ejecutarse en distintos nodos dentro del sistema. 

•

Datos: Información estructurada y no estructurada que es procesada y manipulada por los programas dentro del sistema distribuido. 

•

Componentes varios: Elementos de hardware y software que sustentan la ejecución del sistema, incluyendo servidores, bases de datos y sistemas operativos. 

•

Redes de computadores: Infraestructura que permite la comunicación entre los diferentes componentes del sistema, facilitando el intercambio de datos. 

•

Protocolos: Conjunto de reglas y estándares que definen cómo se lleva a cabo la comunicación y el formato de los mensajes intercambiados entre los componentes. 

•

Middleware: Capa de software que facilita la ejecución distribuida al gestionar la interacción entre los componentes y ocultar la complejidad de la distribución al desarrollador.



### 4.4 Sistemas distribuidos y big data



Los sistemas distribuidos y el Big Data están estrechamente relacionados, ya que el procesamiento y análisis de grandes volúmenes de datos requieren infraestructuras distribuidas que permitan gestionar eficientemente la gran cantidad de datos (Volumen), la velocidad con la que se generan y procesan, y la variedad de formatos que pueden presentar (estructurados, no estructurados y semiestructurados). En un entorno de Big Data, los sistemas distribuidos proporcionan la capacidad de escalabilidad horizontal, permitiendo distribuir el almacenamiento y procesamiento en múltiples nodos interconectados. Además, garantizan la veracidad de los datos al incorporar mecanismos de tolerancia a fallos y replicación, y mejoran el valor extraído de los datos mediante arquitecturas como Hadoop, Apache Spark y bases de datos distribuidas. Así, los sistemas distribuidos son la base tecnológica que hace posible el procesamiento eficiente y en tiempo real de los grandes volúmenes de datos característicos del Big Data.



### 4.5 Contextualización de los sistemas distribuidos



En la actualidad, el crecimiento exponencial de los datos y la necesidad de procesamiento eficiente han impulsado la evolución de los sistemas distribuidos. Estos sistemas permiten distribuir la carga de trabajo en múltiples nodos interconectados, proporcionando beneficios clave como **localidad del dato**, es decir, acercar el procesamiento a donde se almacenan los datos para mejorar el rendimiento. Debemos tener en cuenta que si mis datos están distribuidos en nodos, no tiene sentido que para procesarlos los recopile en un nodo ya que esto sería un cuello de botella. De ahí que se suela decir que en los sistemas distribuidos no viaja el dato sino el proceso.



#### Características



- **computación distribuida**  
  La **computación distribuida** es un pilar fundamental, ya que permite ejecutar tareas en paralelo en diferentes nodos, lo que mejora la escalabilidad y la eficiencia. Para garantizar la continuidad operativa, los sistemas distribuidos implementan **tolerancia a fallos y replicación,** asegurando la disponibilidad y confiabilidad de los datos mediante la duplicación de información en distintos servidores.
- **elasticidad**  
  Otra característica clave es la **elasticidad**, que permite ajustar dinámicamente los recursos en función de la carga de trabajo, optimizando así el uso de la infraestructura. Además, estos sistemas suelen basarse en **commodity hardware**, es decir, hardware de bajo costo y fácil acceso, lo que los hace más rentables en comparación con arquitecturas centralizadas costosas.



En el ámbito del procesamiento de datos a gran escala, Google revolucionó el paradigma con el concepto de **MapReduce**, un modelo que permite procesar grandes volúmenes de información de manera distribuida. Esta innovación dio lugar a la creación de **sistemas de ficheros distribuidos**, como GFS (Google File System) y HDFS (Hadoop Distributed File System) de Yahoo!, que permiten almacenar y gestionar grandes cantidades de datos en entornos distribuidos.

El auge de los dispositivos **móviles y tablets** ha incrementado significativamente la generación de eventos y datos en tiempo real, lo que ha impulsado la necesidad de sistemas capaces de procesar **información** de manera eficiente y actualizada. Gracias a estas arquitecturas, las **aplicaciones modernas** pueden ofrecer información en **tiempo real** y responder rápidamente a los cambios del entorno, permitiendo casos de uso como la analítica en streaming, la inteligencia artificial aplicada y la automatización avanzada.



### 4.6 Conceptos relacionados con  sistemas distribuidos



A continuación, se detallan una serie de conceptos necesarios para entender los sistemas distribuidos:



#### Procesamiento de datos



En el contexto de los sistemas distribuidos, el **procesamiento de datos** juega un papel fundamental al permitir la transformación de conjuntos de datos en información útil para su posterior análisis y visualización. Este proceso involucra una serie de operaciones que convierten los datos en bruto en formatos estructurados y preparados para la toma de decisiones.



#### Análisis de datos



Por su parte, el **análisis de datos** se encarga de recolectar información almacenada en diversas fuentes y aplicar técnicas especializadas para extraer patrones, tendencias y conocimientos relevantes. A través de este proceso, los datos pasan por diferentes fases de manipulación y procesamiento con el objetivo de generar resultados que faciliten la interpretación y optimización de procesos.



![image](assets/cm7d92qdt03mv3j78hsg6axdy-INSD_PRDT_U2_Apartado6-6_Imagen11.jpg)



#### Procesamiento distribuido



En entornos donde el volumen y la velocidad de los datos son elevados, el **procesamiento distribuido** se convierte en una estrategia clave. Este enfoque consiste en la utilización de múltiples nodos de procesamiento que trabajan en conjunto dentro de un sistema distribuido. Para mejorar la eficiencia, los datos se dividen en **fragmentos o particiones** más pequeñas, las cuales se procesan de manera paralela en diferentes servidores o nodos. Esta arquitectura permite reducir tiempos de respuesta, mejorar la escalabilidad del sistema y garantizar una mayor disponibilidad y tolerancia a fallos en el manejo de la información.



#### ¿Cuál es la diferencia entre un sistema distribuido y un sistema paralelo?



Aunque ambos tipos de sistemas procesan tareas simultáneamente, la diferencia radica en cómo se organizan y gestionan. En un sistema distribuido, los recursos se encuentran en diferentes ubicaciones físicas y están conectados a través de una red, mientras que en un sistema paralelo, los recursos están centralizados en un único lugar y se comunican a través de buses o interconexiones internas.



![image](assets/cm7d94znm03pq3j78s4h428pw-INSD_PRDT_U2_Apartado6-6_Imagen12.jpg)



#### Arquitectura cliente-servidor



Otro concepto muy importante es el de **arquitectura cliente-servidor**. La **arquitectura cliente-servidor** es un modelo fundamental dentro de los **sistemas distribuidos,** ya que establece una estructura en la que diferentes componentes del sistema interactúan a través de la red para proporcionar servicios de manera eficiente y escalable. En este modelo, se distingue una **división de responsabilidades** clara entre los clientes, que solicitan servicios o recursos, y los servidores, que procesan estas solicitudes y devuelven las respuestas adecuadas.

Uno de los aspectos esenciales de esta arquitectura es la **comunicación a través de la red**, la cual permite la interacción entre clientes y servidores en entornos distribuidos, sin importar su ubicación física. Para gestionar estas interacciones, se adopta un **modelo de solicitud-respuesta**, en el que los clientes envían peticiones a los servidores y esperan una respuesta en función de los datos procesados.

Los sistemas distribuidos que implementan esta arquitectura destacan por su **escalabilidad**, ya que pueden aumentar su capacidad al agregar más servidores o clientes sin afectar el rendimiento general. Además, la **seguridad** es un factor clave, ya que la separación entre clientes y servidores permite aplicar estrategias de autenticación, cifrado y control de acceso para proteger la información transmitida.

Otro beneficio de este enfoque es la **independencia de la plataforma**, lo que significa que los clientes y servidores pueden operar en distintos sistemas operativos y entornos sin generar incompatibilidades. Esto también facilita el **desarrollo distribuido**, permitiendo que múltiples equipos trabajen en diferentes partes del sistema de manera descentralizada, mejorando la modularidad y el mantenimiento del software.



![image](assets/cm7d9d9pq03x73j78l2muyn4z-INSD_PRDT_U2_Apartado6-6_Imagen13.jpg)



En el contexto de los sistemas distribuidos, los **clústeres de servidores** representan una arquitectura clave para mejorar la eficiencia, disponibilidad y rendimiento de las aplicaciones y servicios distribuidos. Un clúster de servidores es un conjunto de servidores interconectados que trabajan en conjunto como si fueran una única unidad, proporcionando una serie de beneficios esenciales en entornos de alto rendimiento y disponibilidad.

Uno de los aspectos más importantes de esta arquitectura es la **alta disponibilidad**, que garantiza que los servicios permanezcan operativos incluso ante fallos en uno o varios nodos. A esto se suma la **escalabilidad**, que permite aumentar la capacidad del sistema agregando más servidores según la demanda, optimizando así el uso de recursos sin afectar el rendimiento.

Para distribuir eficientemente la carga de trabajo entre los distintos servidores, se implementa un mecanismo de **balanceo de carga**, el cual evita la saturación de un único nodo y mejora la eficiencia del sistema. Además, la **tolerancia a fallos** es un principio clave en los clústeres de servidores, ya que permite la continuidad del servicio mediante estrategias como la replicación de datos y la redundancia de componentes.

El **rendimiento** es otro beneficio esencial, ya que, al distribuir tareas entre varios servidores, se reduce la latencia y se mejora el tiempo de respuesta. Asimismo, los clústeres permiten **una administración centralizada**, facilitando la gestión de recursos, la monitorización y el mantenimiento del sistema.

Finalmente, la **seguridad** en un clúster de servidores se refuerza mediante controles de acceso, cifrado de datos y políticas de autenticación que garantizan la integridad y confidencialidad de la información distribuida.



![image](assets/cm7d9ftua03xt3j78dylxdy31-INSD_PRDT_U2_Apartado6-6_Imagen14.jpg)



### 4.7 Teorema del CAP



Aunque conoceréis el enunciado de dicho teorema por el estudio de otras signaturas, en este apartado por un lado vamos a contextualizarlo y descubrir por qué surgió y posteriormente vamos a darle aplicación práctica.



Hace algunos años, mejorar el rendimiento de un sistema de software era un proceso relativamente sencillo: se podía aumentar la capacidad del hardware (escalado vertical) o se optimizaba la aplicación para hacer un uso más eficiente de los recursos disponibles (ajuste de rendimiento).



El teorema enuncia que es imposible que un sistema computarizado distribuido proporcione simultáneamente las tres garantías siguientes:



- **Consistencia (C)**  
  En todo momento, todos los nodos del sistema deben acceder y mostrar los mismos datos, garantizando coherencia en la información.
- **Disponibilidad (A)**  
  Cada solicitud enviada a cualquier nodo del sistema debe obtener una respuesta válida y sin errores, incluso en presencia de fallos.
- **Tolerancia a particiones (P)**  
  El sistema debe seguir operando correctamente incluso si la red experimenta fallos o divisiones que impidan la comunicación entre algunos de sus nodos.



**Seguro conocéis y habréis estudiado la siguiente imagen. Es un clásico para representar de forma gráfica dónde caen cada una de las tecnologías de Bases de datos según las dos características que se copromenten a mantener. En los ejercicios os pediré trabajar con casos de uso reales no sólo centrados en tipologías de bases de datos.**



![image](assets/cm6jgq74k03m03570jk7vn70m-INSD_PRDT_U2_Apartado6-7_Imagen15.jpg)



### 4.8 Reto de la concurrencia de usuarios



En los **sistemas distribuidos**, uno de los desafíos más críticos es la concurrencia de usuarios, es decir, la capacidad del sistema para manejar múltiples solicitudes simultáneas sin comprometer su rendimiento. A medida que el número de usuarios aumenta, surgen distintos retos técnicos que deben abordarse para garantizar un funcionamiento eficiente y estable.



#### La escalabilidad



Uno de los principales aspectos a considerar es la escalabilidad, que permite que el sistema crezca sin experimentar degradación en los tiempos de respuesta. Para lograrlo, es fundamental diseñar una infraestructura capaz de expandirse dinámicamente sin afectar el rendimiento general.



#### La disponibilidad



**La disponibilidad** es otro factor clave, ya que los sistemas deben ser capaces de procesar múltiples **consultas simultáneas** sin interrupciones. Esto requiere mecanismos eficientes de gestión de recursos y optimización en la distribución de cargas de trabajo.



#### Balanceo de carga



El **balanceo de carga** juega un papel fundamental al evitar **cuellos de botella**, distribuyendo equitativamente las solicitudes entre los distintos servidores o nodos. Una mala gestión en este aspecto puede derivar en un uso desigual de los recursos, afectando negativamente la eficiencia del sistema.



#### Resistencia a fallos



Además, los sistemas distribuidos deben contar con **resistencia a fallos**, asegurando la continuidad del servicio incluso en situaciones de alta demanda o fallos inesperados. Sin embargo, si la arquitectura no está correctamente diseñada, el sistema podría enfrentarse a **posibles saturaciones**, afectando la experiencia de los usuarios.



#### Tiempo de respuesta



Otro reto importante es el **tiempo de respuesta**, ya que los usuarios esperan obtener información en el menor tiempo posible. En entornos distribuidos, este aspecto puede volverse complejo debido al llamado **efecto de caja negra**, donde el sistema se comporta como un conjunto de procesos opacos cuya latencia puede ser difícil de diagnosticar y optimizar.



### 4.9 Latencia vs rendimiento



En el diseño y optimización de **sistemas distribuidos**, dos métricas clave determinan la eficiencia y capacidad de respuesta del sistema: la **latencia** y el **rendimiento**. Aunque están relacionadas, representan conceptos distintos que deben ser analizados y optimizados según las necesidades del sistema y la carga de trabajo esperada.



#### La Latencia



**La latencia** se refiere al **tiempo que tarda una operación específica en completarse**, lo cual es fundamental para garantizar una respuesta rápida a las solicitudes de los usuarios. Se mide en **milisegundos (ms)**, y una latencia baja implica tiempos de espera reducidos, mejorando la experiencia del usuario en aplicaciones que requieren respuestas inmediatas, como bases de datos transaccionales o servicios en tiempo real.



#### El Rendimiento



Por otro lado, el **rendimiento** mide la **cantidad de trabajo que un sistema puede procesar en un período determinado de tiempo**. Se expresa en términos de operaciones por segundo, utilizando métricas como **FLOPS (Floating Point Operations Per Second)** en sistemas de alto rendimiento. Un sistema con alto rendimiento puede manejar un gran volumen de solicitudes simultáneas, lo que es crucial en entornos donde se procesan grandes volúmenes de datos o en sistemas que requieren escalabilidad masiva.



### 4.10 OLAP vs OLTP



En los **sistemas distribuidos**, el manejo eficiente de los datos depende en gran medida del tipo de procesamiento que se requiera. Existen dos enfoques fundamentales en la gestión de bases de datos distribuidas: **Online Analytical Processing (OLAP) y Online Transaction Processing (OLTP)**, cada uno diseñado para cumplir diferentes propósitos dentro de una infraestructura escalable.



- **OLAP**  
  El **procesamiento analítico en línea (OLAP)** se centra en la generación de **informes y análisis históricos**. Los datos en estos sistemas se organizan en múltiples dimensiones, como tiempo, producto, ubicación y categoría, permitiendo la exploración detallada de grandes volúmenes de información. Dado que estos análisis suelen requerir la agregación de datos complejos y cálculos intensivos, los **tiempos de respuesta no son inmediatos**, y su procesamiento se realiza en **sistemas distribuidos especializados** en almacenamiento y consulta de datos, como los data warehouses.
- **OLTP**  
  Por otro lado, el **procesamiento de transacciones en línea (OLTP)** está diseñado para manejar **operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en tiempo real.** Este tipo de procesamiento es crítico para sistemas con alta concurrencia, donde miles o millones de usuarios pueden estar ejecutando transacciones simultáneamente. A diferencia de OLAP, **OLTP requiere tiempos de respuesta rápidos** y una alta disponibilidad, lo que se logra mediante arquitecturas distribuidas que balancean la carga entre múltiples servidores y garantizan la integridad de los datos.



En el contexto de los **sistemas distribuidos**, ambos modelos coexisten y requieren infraestructuras adaptadas a sus necesidades. Mientras que **OLAP** se beneficia de arquitecturas escalables que optimizan consultas analíticas masivas, **OLTP** necesita sistemas altamente eficientes que prioricen la velocidad y consistencia de las transacciones. La combinación de estos enfoques permite construir sistemas robustos que soporten tanto la operatividad en tiempo real como el análisis estratégico de datos a gran escala.



![image](assets/cm7da5ls104t33j78bq89s17m-INSD_PRDT_U2_Apartado6-10_Imagen18.jpg)



### 4.11 Bases de datos NoSQL (Not Only SQL)



Entendemos que en otras asignatura se ha profundiado en conceptos y uso de bases de datos NoSQL. En este punto nos limitaremos a mencionar lo más importante que debemos saber como pre-requisito para futuros ejercicios. Puntos clave:

- Las bases de datos como una alternativa a los modelos relacionales

- Mayor flexibilidad, escalabilidad y tolerancia a fallos. Estas bases de datos están

- Diseñadas para gestionar grandes volúmenes de información y operar en arquitecturas descentralizadas.

- Permiten almacenar información en distintos formatos como **clave-valor, documentos y grafos.**

- Están diseñadas para **escalar horizontalmente**.

- Cuentan con **tolerancia a fallos.**

- Presentan **escalabilidad flexible**, permitiendo ajustar los recursos del sistema en función de la demanda sin afectar su rendimiento.



![image](assets/cm7da80hi054n3j78s9w9m56n-INSD_PRDT_U2_Apartado6-11_Imagen19.jpg)



Dentro del ecosistema de bases de datos **NoSQL**, el **almacenamiento por columnas** (Columnar Storage) es una técnica ampliamente utilizada en bases de datos orientadas a columnas como **Apache Cassandra, HBase y Google Bigtable**.  Como características principales de este tipo de BBDD  recordar:

- **Almacenan los datos agrupados por columnas**

- **Compresión eficiente**, ya que los datos dentro de una misma columna suelen ser homogéneos.

- Operaciones **selectivas más rápidas,** ya que, en lugar de leer registros completos, el sistema puede acceder directamente a las columnas relevantes



![image](assets/cm7daasmr05593j78boybpqck-INSD_PRDT_U2_Apartado6-11_Imagen20.jpg)



### 4.12 Preguntas básicas acerca de los sistemas distribuidos



#### ¿Cuáles son los desafíos principales de los sistemas distribuidos?



Algunos de los desafíos principales incluyen la gestión de la concurrencia y la coherencia de los datos, la tolerancia a fallos, la comunicación y sincronización entre nodos, la seguridad de los datos y la escalabilidad. Además, la complejidad de la programación y el diagnóstico de problemas pueden aumentar en entornos distribuidos.



#### ¿Qué estrategias se utilizan para abordar la tolerancia a fallos en sistemas distribuidos?



Las estrategias comunes incluyen la replicación de datos para garantizar la disponibilidad y la redundancia, el uso de algoritmos de consenso para lograr la coherencia de datos en presencia de fallos y la implementación de mecanismos de detección y recuperación de fallos automáticos.



#### ¿Cuáles son los principales desafíos de la escalabilidad en sistemas distribuidos?



Algunos desafíos incluyen el diseño de algoritmos y protocolos que puedan manejar un aumento en el número de nodos y la cantidad de datos, la gestión eficiente de recursos para evitar cuellos de botella y la minimización de la sobrecarga de comunicación y coordinación entre nodos.



#### ¿Qué es la consistencia eventual en sistemas distribuidos?



La consistencia eventual es un modelo de consistencia que permite que los diferentes nodos de un sistema distribuido tengan copias diferentes de los datos durante un período de tiempo, pero garantiza que eventualmente converjan a un estado consistente. Este modelo se utiliza para mejorar el rendimiento y la disponibilidad en sistemas donde la coherencia inmediata de los datos no es crítica.



#### ¿Cuáles son los principales desafíos al diseñar una arquitectura Big Data?



Algunos de los principales desafíos incluyen la gestión de grandes volúmenes de datos, la variedad de fuentes de datos y formatos, la velocidad a la que se generan y procesan los datos, la garantía de la calidad y la integridad de los datos, la seguridad y privacidad de los datos, y la escalabilidad para manejar el crecimiento futuro de datos y usuarios.



## 5. Apache Hadoop



### 5.1 Introducción (historia)



![image](assets/cm6jisvsu05623570k3pmis82-stock-image.jpg)



Al igual que en otros apartados, refrescaremos aquí lo aprendido sobre Hadoop introduciendo algunos aspectos no tratados y profundizando en conceptos más complejos necesarios para poner en práctica el conocimiento.



El origen de **Hadoop** se remonta a principios de los años 2000, cuando **Google** desarrolló tecnologías clave para manejar grandes volúmenes de datos de manera eficiente. En **2003**, Google presentó el **Google File System (GFS)**, un sistema de almacenamiento distribuido diseñado para gestionar datos a gran escala con alta tolerancia a fallos. Posteriormente, en **2004**, Google publicó un artículo sobre **MapReduce**, un modelo de programación que simplifica el procesamiento de grandes volúmenes de información en clústeres distribuidos.



Inspirado en estas ideas, en **2005** se desarrolló **Nutch**, un motor de búsqueda web de código abierto que necesitaba una infraestructura escalable para el procesamiento de datos. Para resolver este desafío, se comenzó a trabajar en una nueva solución basada en las ideas de GFS y MapReduce, lo que dio origen a **Hadoop** como un proyecto independiente.



En **2006**, Yahoo! adoptó Hadoop, contribuyendo significativamente a su desarrollo y utilizándolo internamente para procesar grandes volúmenes de datos. Posteriormente, en **2008**, Hadoop fue donado a la **Apache Software Foundation**, convirtiéndose en un proyecto de código abierto respaldado por una comunidad activa de desarrolladores y empresas.



Desde entonces, **Hadoop ha evolucionado hasta convertirse en un ecosistema completo**, con múltiples componentes como **HDFS (Hadoop Distributed File System)**, **YARN (gestión de recursos)**, **Hive (consulta de datos)**, **HBase (base de datos NoSQL)** y **Spark (procesamiento en memoria)**. Gracias a su escalabilidad y flexibilidad, Hadoop ha sido adoptado ampliamente en la **industria**, siendo utilizado en sectores como finanzas, telecomunicaciones, salud y comercio electrónico para el análisis y procesamiento de Big Data.



![image](assets/cm7d8hbyp008u3578ey9foeme-INSD_PRDT_U2_Apartado7-1_Imagen21.jpg)



### 5.2 Características



Como se ha comentado, Hadoop es un ecosistema de **código abierto**, desarrollado y mantenido por la **Apache Software Foundation**, diseñado para gestionar grandes volúmenes de datos de manera distribuida. Gracias a su arquitectura escalable y tolerante a fallos, se ha convertido en una solución esencial para el procesamiento de **Big Data**. A continuación, se presentan sus principales características:



- **Código abierto (Fundación Apache):** Hadoop es un proyecto de código abierto, lo que significa que cualquier organización o desarrollador puede utilizarlo, modificarlo y mejorarlo sin costos de licencia. Su comunidad activa garantiza mejoras constantes y una amplia compatibilidad con otras tecnologías.

- **Computación distribuida:** Hadoop divide los datos y las tareas de procesamiento en múltiples nodos dentro de un clúster, permitiendo el procesamiento en paralelo y optimizando el rendimiento en grandes volúmenes de información.

- **Tolerancia a fallos:** En caso de fallo de un nodo dentro del clúster, Hadoop redirige automáticamente la tarea a otro nodo disponible, asegurando que los procesos continúen sin interrupciones.

- **Alta disponibilidad:** Su arquitectura permite que los datos y servicios estén siempre accesibles mediante replicación, evitando la pérdida de información y garantizando su disponibilidad incluso en caso de fallos.

- **Extensible:** Hadoop permite la integración con diversas herramientas y frameworks como **Apache Spark, Hive, HBase y Pig**, ampliando sus capacidades de análisis y procesamiento de datos.

- **HDFS Snapshots:** El sistema de archivos distribuido de Hadoop (**HDFS**) permite la creación de snapshots, lo que facilita la recuperación de datos y la gestión eficiente de versiones de archivos.

- **Disk Driver Awareness:** Hadoop tiene la capacidad de reconocer y optimizar el uso de los distintos discos físicos dentro de un clúster, mejorando la distribución de la carga y la eficiencia en el acceso a los datos.

- **Performance:** Aunque Hadoop es altamente eficiente en el procesamiento de grandes volúmenes de datos, su rendimiento depende de la correcta configuración del clúster y del hardware utilizado.

- **Escalabilidad:** Hadoop puede expandirse fácilmente agregando más nodos al clúster sin necesidad de modificar la arquitectura subyacente, permitiendo adaptarse a crecientes volúmenes de datos.

- **Fiabilidad:** Su diseño robusto y su modelo de replicación de datos aseguran que la información almacenada en HDFS se mantenga disponible y segura frente a posibles fallos.

- **Curva de aprendizaje elevada:** Debido a la complejidad de su ecosistema y su arquitectura distribuida, Hadoop requiere un proceso de aprendizaje considerable para su implementación y optimización efectiva.

- **Localidad del dato:** En lugar de mover grandes volúmenes de datos a los procesos de cómputo, Hadoop acerca los cálculos a los datos, reduciendo la latencia y mejorando el rendimiento general del sistema.

- **Apoyo de empresas líderes:** Hadoop cuenta con el respaldo de grandes empresas tecnológicas como **IBM, Oracle, EMC y Cloudera**, lo que ha impulsado su desarrollo, integración con otros productos y adopción en la industria a gran escala.

- **Framework para computación distribuida:** Hadoop es un **framework diseñado para procesar grandes conjuntos de datos** en clústeres de ordenadores, utilizando programación distribuida para gestionar el procesamiento paralelo y maximizar la eficiencia.

- **Escalabilidad masiva:** Está diseñado para **escalar desde un único servidor hasta miles de máquinas**, lo que le permite ofrecer tanto capacidad de cómputo como almacenamiento a medida que crece el volumen de datos o los requisitos de procesamiento.

- **Alta disponibilidad y tolerancia a fallos:** Hadoop es capaz de **detectar fallos y recuperarse automáticamente**, garantizando que los servicios continúen operativos incluso cuando ocurren fallos en uno o más nodos del sistema.

- **Capacidad para manejar grandes volúmenes de datos:** Hadoop está diseñado para trabajar con **petabytes de información**, lo que lo convierte en una opción adecuada para aplicaciones de Big Data y análisis a gran escala.

- **Uso de hardware económico:** A diferencia de otros sistemas centralizados que dependen de hardware costoso, Hadoop está diseñado para ejecutarse en **hardware económico (commodity hardware)**, lo que reduce significativamente los costos de implementación y operación.

- **Inicialmente, capa de persistencia de otros frameworks Big Data:** En sus inicios, Hadoop se utilizaba como la **única capa de almacenamiento y persistencia para otros frameworks de Big Data**, como Spark y Hive, consolidándose como un componente esencial en arquitecturas de análisis masivo.

- **No es una base de datos:** Aunque Hadoop gestiona y almacena grandes volúmenes de datos mediante su sistema de archivos distribuido (**HDFS**), no es una base de datos. No ofrece las capacidades tradicionales de gestión de datos estructurados como SQL, sino que sirve como infraestructura para otras herramientas que proporcionan esas funcionalidades.



Gracias a estas características, Hadoop se ha convertido en una solución clave para el procesamiento masivo de datos en entornos distribuidos



### 5.3 Modos de despliegue



Apache hadoop presenta los siguientes modos de despliegue:



•

Local: Modo por defecto que se ejecuta como un único proceso de Java. 

No hay demonios ejecutándose 

El trabajo es ejecutado en la máquina virtual de Java (JVM) local 

El trabajo es ejecutado por el local job runner, una versión más simple del motor de ejecución MapReduce de Hadoop 

Puede ser usado en una fase de desarrollo inicial para depurar el código 

•

Pseudo-distribuido: Varios procesos de java ejecutándose en la misma máquina 

Los demonios de Hadoop se lanzan igual que si fuera un clúster distribuido sólo que todos ellos se ejecutan en la máquina local 

Adecuado para ser usado en la fase de desarrollo ya que permite testar el código en un entorno lo más parecido posible al de producción 

•

Distribuido: Se maximiza el paralelismo de procesos y se utilizan todos los recursos disponibles del clúster en el que se va a configurar Hadoop 

Los demonios de Hadoop se ejecutan en un clúster distribuidos 

Adecuado para producción



### 5.4 Limitaciones de hadoop



Si bien **Hadoop** es una de las tecnologías más utilizadas en **Big Data** y procesamiento distribuido, también presenta ciertas limitaciones que pueden afectar su rendimiento, facilidad de uso y eficiencia. A continuación, se detallan algunos de sus puntos débiles:



- **Uso del disco como mecanismo de comunicación entre procesos:** Hadoop depende en gran medida del almacenamiento en disco para intercambiar información entre tareas, lo que introduce latencias y ralentiza el procesamiento en comparación con soluciones en memoria como **Apache Spark**.

- **API rudimentaria y poco expresiva:** Aunque el modelo **MapReduce** es funcional, su API en **Java** puede resultar compleja y poco intuitiva para los desarrolladores, lo que dificulta la implementación de ciertas tareas y reduce la productividad.

- **Excesivo código para poca funcionalidad:** Desarrollar aplicaciones en Hadoop suele requerir una gran cantidad de código para implementar funcionalidades relativamente simples, lo que aumenta la carga de trabajo y la curva de aprendizaje para los programadores.

- **Código repetitivo e ineficiente:** La necesidad de escribir código repetitivo en varias partes de una aplicación hace que el desarrollo sea menos eficiente y dificulta el mantenimiento del sistema.

- **Requisitos de infraestructura exigentes:** En algunos casos, los requisitos de hardware y configuración de Hadoop pueden ser demasiado exigentes, lo que implica costos elevados en términos de almacenamiento, procesamiento y mantenimiento de clústeres.

- **Problemas de sobreparticionamiento:** La forma en que Hadoop divide los datos en múltiples particiones para su procesamiento puede generar un exceso de fragmentación, lo que afecta el rendimiento y aumenta la latencia de ejecución.



A pesar de estas limitaciones, Hadoop sigue siendo una tecnología clave en el ecosistema de Big Data, especialmente cuando se combina con otras soluciones como **Apache Spark**, **Hive** y **HBase**, (ver sección de ecosistema Hadoop) que ayudan a mitigar algunos de estos problemas y mejorar su eficiencia.



### 5.5 Componentes



Recordemos brevemente los componentes de Hadoop ya vistos en otras materias ya que los necesitaremos en ésta.



Hadoop está compuesto por varios módulos que trabajan en conjunto para proporcionar una solución escalable y distribuida para el almacenamiento y procesamiento de datos. Los principales componentes de **Hadoop** son:



1. **HDFS (Hadoop Distributed File System)**

   - Sistema de almacenamiento distribuido que divide los datos en bloques y los distribuye en múltiples nodos del clúster.

   - Ofrece tolerancia a fallos mediante replicación de datos.
2. **YARN (Yet Another Resource Negotiator)**

   - Administrador de recursos de Hadoop que gestiona la asignación de CPU y memoria en el clúster.

   - Permite la ejecución simultánea de múltiples aplicaciones sobre Hadoop.
3. **MapReduce**

   - Modelo de programación para el procesamiento paralelo de grandes volúmenes de datos.

   - Divide las tareas en Map (procesamiento de datos) y Reduce (agregación de resultados).
4. **Common**

   - Biblioteca de utilidades compartidas por los demás módulos de Hadoop.

   - Proporciona funciones esenciales como autenticación, configuración y herramientas de integración.
5. **Otros Componentes del Ecosistema Hadoop**

   - Apache Hive: Lenguaje SQL para consultas en HDFS.

   - Apache HBase: Base de datos NoSQL sobre HDFS para consultas rápidas.

   - Apache Spark: Procesamiento en memoria más eficiente que MapReduce.

   - Apache Flume y Kafka: Herramientas para la ingesta de datos en Hadoop.



Estos módulos son los principales, entre otros, y forman la base de Hadoop y permiten su integración con múltiples tecnologías dentro del mundo Big Data. En la siguiente sección veremos un esquema de este ecosistema.



![image](assets/cm7d8y6uf00r035786mrjluo2-INSD_PRDT_U2_Apartado7-5_Imagen22.jpg)



### 5.6 Ecosistema Hadoop



El **ecosistema Hadoop** es un conjunto de tecnologías y herramientas diseñadas para el **almacenamiento**, procesamiento y **análisis de grandes volúmenes de datos en entornos distribuidos**. Su núcleo está compuesto por HDFS **(Hadoop Distributed File System)**, que permite el almacenamiento distribuido de datos, **YARN (Yet Another Resource Negotiator)**, encargado de la gestión de recursos del clúster, y **MapReduce**, un modelo de programación para el procesamiento paralelo de datos a gran escala.



Además, el ecosistema se complementa con herramientas como **Apache Hive**, que permite ejecutar consultas SQL sobre Hadoop, **Apache HBase,** una base de datos NoSQL sobre HDFS, y **Apache Spark**, un motor de procesamiento en memoria más eficiente que MapReduce. También incluye soluciones para la ingesta de datos como **Apache Flume** y **Apache Kafka**. Gracias a su escalabilidad, tolerancia a fallos y flexibilidad, el ecosistema Hadoop es una de las soluciones más utilizadas en Big Data, permitiendo a las empresas analizar y gestionar datos de manera eficiente en entornos distribuidos.



![image](assets/cm7d92zr400zo3578w9iyth7p-INSD_PRDT_U2_Apartado7-6_Imagen23.jpg)



Este esquema, o uno similar, ya ha sido visto en otras asignaturas. Con el fin de que la unidad sea autocontenida y que el alumno no tenga que acudir  otras asignaturas, a continuación en el siguiente video se realiza una breve explicación de los elementos más representativos del entorno hadoop:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652185_1/scormcontent/assets/Video%205%20Elementos%20Hadoop%20%281%29.mp4?v=1)



#### Plataformas



Algo que no se ha abordado con anterioridad es la forma de implementar ese entorno hadoop en la realidad.



El ecosistema de Hadoop se ha convertido en un estándar fundamental para el procesamiento y almacenamiento distribuido de grandes volúmenes de datos en entornos de Big Data. Hadoop proporciona una infraestructura escalable y tolerante a fallos, permitiendo gestionar datos estructurados y no estructurados a través de su arquitectura distribuida basada en HDFS (Hadoop Distributed File System) y MapReduce.



Dado que la implementación y gestión de Hadoop puede ser compleja, han surgido diversas plataformas que facilitan su despliegue y administración en infraestructuras locales o en la nube. Entre estas plataformas se encuentran:



•

Cloudera: Una de las distribuciones más utilizadas de Hadoop, que proporciona herramientas avanzadas de administración, seguridad y optimización para entornos empresariales.



La siguiente imagen muestra su estructura así como dónde se engloban  los distintos componentes del ecosistema hadoop:



![image](assets/cm7d9bd62017f3578gkjuhr6q-INSD_PRDT_U2_Apartado7-6-1_Imagen24.jpg)



•

Stratio: Plataforma enfocada en la analítica avanzada y procesamiento de datos basada en tecnologías como Hadoop y Spark.



A continuación se muestra un esquema de su arquitectura:



![image](assets/cm7d9cwoq019g35783ti5bjvn-INSD_PRDT_U2_Apartado7-6-1_Imagen25.jpg)



•

AWS (Amazon Web Services): Ofrece servicios como Amazon EMR (Elastic MapReduce), que permite desplegar y gestionar clústeres de Hadoop en la nube de manera eficiente y escalable.



En la siguiente imagen se muestran algunos de los productos ofrecidos por aws relacionados con big data:



![image](assets/cm7d9e3te01ca3578uu51qivi-INSD_PRDT_U2_Apartado7-6-1_Imagen26.jpg)



•

Azure (Microsoft): Proporciona Azure HDInsight, una solución gestionada de Hadoop que facilita la integración con otras herramientas de análisis y machine learning dentro del ecosistema de Microsoft.



El siguiente diagrama muestra algunos d ellos productos ofrecidos por Microsoft Azure:



![image](assets/cm7d9fgdv01f43578mapuulw8-INSD_PRDT_U2_Apartado7-6-1_Imagen27.jpg)



•

Google Cloud: Ofrece Google Dataproc, un servicio optimizado para ejecutar tareas de Hadoop y Spark en la nube, reduciendo tiempos de implementación y costos operativos.



A continuación se muestran algunos de los productos ofrecidos por la nube de Google:



![image](assets/cm7d9gn2301hy3578s1vucce7-INSD_PRDT_U2_Apartado7-6-1_Imagen28.jpg)



Estas plataformas permiten que las organizaciones desplieguen y gestionen Hadoop de manera más eficiente, aprovechando la escalabilidad, seguridad y flexibilidad que ofrecen tanto las soluciones on-premise como los entornos en la nube. En conjunto, estas tecnologías hacen posible el procesamiento masivo de datos, la analítica avanzada y la toma de decisiones basada en información a gran escala.



### 5.7 HDFS



A modo de resumen diremos que Hadoop Distributed File System (HDFS) es un sistema de almacenamiento distribuido diseñado para manejar grandes volúmenes de datos con alta disponibilidad y tolerancia a fallos. Funciona dividiendo los archivos en bloques, que se distribuyen entre múltiples DataNodes dentro del clúster.

El NameNode, como gestor de metadatos, rastrea la ubicación de los bloques sin almacenarlos directamente. Los usuarios interactúan con HDFS como si fuera un único disco virtual, accediendo a los datos a través de un cliente que coordina con el NameNode y los DataNodes.



#### Características clave de HDFS



Recordemos que entre sus características más importantes hay que destacar:



- **Gestión de archivos grandes**: Diseñado para manejar archivos de gran tamaño (GB o más), ideal para Big Data.

- **Particionamiento de archivos**: Divide los datos en bloques y los distribuye en nodos para mejorar eficiencia y procesamiento paralelo.

- **Tolerancia a fallos**: Replica los bloques en varios nodos para garantizar disponibilidad y evitar pérdida de datos.

- **Optimización para lecturas frecuentes**: Sigue un modelo de "una escritura, muchas lecturas", favoreciendo el acceso rápido en aplicaciones analíticas.

- Y eficiente a los datos, en lugar de la modificación constante de la información almacenada.



#### Limitaciones de HDFS



Asimismo es conveniente recordar que HDFS también posee limitaciones:



- **Alta latencia de red**: No optimizado para operaciones en tiempo real, ya que la transferencia de datos entre nodos introduce latencia.

- **Ineficiencia con archivos pequeños**: Almacenarlos genera una carga excesiva en el NameNode debido a la gestión de metadatos.

- **Limitación en múltiples escritores**: No permite escritura simultánea en un mismo archivo, restringiendo casos de uso en entornos de modificación en tiempo real.

- **Modificaciones restringidas**: No se pueden editar archivos existentes, solo agregar datos al final (append), limitando su flexibilidad.



#### Características HDFS



El **Hadoop Distributed File System (HDFS)** es un sistema de archivos distribuido inspirado en **Google File System (GFS)**, diseñado para gestionar grandes volúmenes de datos en entornos de **Big Data**.

Su arquitectura se basa en la división de archivos en bloques de tamaño configurable (típicamente **128 MB** **por bloque**), lo que permite una distribución eficiente de los datos en múltiples nodos del clúster.



Para garantizar un equilibrio en el almacenamiento y la carga de trabajo, HDFS cuenta con un mecanismo de **rebalanceo de bloques**, que redistribuye los datos entre los nodos cuando se detectan desequilibrios en la utilización del espacio o la carga de procesamiento.



Este sistema está optimizado para archivos enormes, como logs, imágenes satelitales o registros financieros, asegurando una gestión eficiente del almacenamiento.



Una de sus principales fortalezas es su **tolerancia a fallos**, ya que mantiene múltiples copias de cada bloque en distintos nodos mediante replicación, garantizando **alta disponibilidad** incluso en caso de fallos de hardware o caídas de servidores. Además, HDFS sigue un modelo de consistencia fuerte, asegurando que los datos almacenados sean coherentes en todo el sistema y evitando inconsistencias.



Gracias a su capacidad de escalabilidad, HDFS puede crecer de manera horizontal agregando nuevos nodos sin afectar el rendimiento del sistema, lo que lo convierte en una solución ideal para entornos donde los volúmenes de datos aumentan constantemente.



Hoy en día, **HDFS sigue siendo la capa de persistencia más popular para los datalakes**, y su uso no se limita exclusivamente al ecosistema de Hadoop. Es común encontrarlo implementado de forma independiente en arquitecturas modernas de análisis de datos, donde se combina con tecnologías como **Apache Spark, Presto o Trino** para explotar su capacidad de almacenamiento distribuido.



#### Componentes  de HDFS



El **Hadoop Distributed File System (HDFS)** está diseñado para proporcionar almacenamiento distribuido y tolerante a fallos para grandes volúmenes de datos.  Recordemos de forma resumidad sus componentes:



NameNode (gestor de metadatos):



- Mantiene información de la ubicación de bloques (no almacena datos).

- Gestiona operaciones de lectura/escritura, pero los datos viajan entre cliente y DataNodes.

- Alta disponibilidad: Standby NameNode y Quorum Journal Nodes.

- Failover con Zookeeper: Conmutación automática en caso de fallo.



Secondary NameNode:



- Crea puntos de control (checkpoints) del estado del NameNode.

- No es un NameNode de respaldo ni reemplazo en caso de fallo.

- Sustituido en versiones recientes por Standby NameNode y Quorum Journal Nodes.



DataNodes (almacenamiento real de datos):



- Replicación: Bloques replicados según configuración en hdfs-site.xml.

- Organización en racks/datacenters: Optimización de red y tolerancia a fallos.

- Operaciones I/O: Lectura/escritura directa sin pasar por NameNode.

- Tolerancia a fallos: Recuperación automática de datos en caso de fallo.

- Configuración: Archivos core-site.xml, hdfs-site.xml y demonio start-dfs.sh.



![image](assets/cm7d9v12c021235788xu9p26i-INSD_PRDT_U2_Apartado7-7-4_Imagen29.jpg)



#### Replicación de bloques



La funcionalidad de replicación de bloques ya ha sido vista en otras asignaturas. Este epígrafe es meramente un recordtorio.



Es conveniente recordar el conceto de replicación de bloques. HDFS garantiza la tolerancia a fallos mediante un sistema de replicación de bloques, donde cada bloque de datos tiene múltiples copias distribuidas en distintos DataNodes. El factor de replicación, por defecto 3, determina cuántas copias se almacenan.

El NameNode gestiona esta replicación, asegurando que cada bloque mantenga su número de copias. Si un bloque es modificado o eliminado, el NameNode actualiza automáticamente las copias en otros nodos.



Este mecanismo permite la recuperación de datos en caso de fallo de un DataNode, asegurando disponibilidad y consistencia en todo el sistema.



Un ejemplo práctico se puede ver en la siguiente imagen:



![image](assets/cm7d9yc57024m35789xfqvfus-INSD_PRDT_U2_Apartado7-7-5_Imagen30.jpg)



En este punto es importante nombrar el algoritmo de rack awareness también visto en otras asignaturas. Este algoritmo impide que todas las copias se realicen en el mismo rack asegurando una mayor tolerancia a fallos.



Su funcionamiento se basa en la siguiente lógica:



•

La primera réplica de un bloque se almacena dentro del mismo rack en el que se encuentra el nodo que originalmente escribe los datos, minimizando la latencia de acceso. 

•

La segunda réplica se coloca en un rack remoto, asegurando la tolerancia a fallos en caso de que un rack completo falle. 

•

Si el factor de replicación es mayor, las réplicas adicionales se distribuyen de manera aleatoria, pero evitando que haya más de dos copias dentro del mismo rack. Esto equilibra la carga de almacenamiento y mejora la eficiencia de la recuperación de datos en caso de fallos.



![image](assets/cm7da13sl027v3578wdot985a-INSD_PRDT_U2_Apartado7-7-5_Imagen31.jpg)



El siguiente video es interesante al mostrar y explicar el funcionamiento de HDFS con legos:



YOUTUBE
Understanding HDFS using Legos
You've been hearing about Hadoop and HDFS. How does it work? In this video, we use an innovative method to show how HDFS works with Legos. Jesse Anderson shows how HDFS handles files and replicates the data, then covers the read and write paths for the data.
VIEW ON YOUTUBE



#### Recordatorio del chequeo del estado de los datanodes



Resulta indispensable recordar cómo se consigue que el namenode se entere de que un datanode se encuentra fuera de servicio. Los **DataNodes** envían **Heartbeats** al **NameNode** cada 3 segundos para confirmar su estado.

Si un DataNode deja de responder, el NameNode lo considera inactivo y redistribuye sus bloques a otros nodos para mantener la replicación. Este proceso garantiza la tolerancia a **fallos** y la **alta disponibilidad** del sistema.



![image](assets/cm7da55kd02az3578bufbcown-INSD_PRDT_U2_Apartado7-7-6_Imagen32.jpg)



#### Lectura en HDFS



El siguiente esquema muestra cómo se realiza la lectura en HDFS, el cual os va a resultar familiar con lo equivalente visto para la base de datos Cassandra.



![image](assets/cm7da6pa502ct3578134mnryk-INSD_PRDT_U2_Apartado7-7-7_Imagen33.jpg)



Se explica este proceso en el siguiente video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652185_1/scormcontent/assets/Video%206%20Lectura%20HDFS.mp4?v=1)



#### Formatos de ficheros en  HDFS



En este apartado repasamos brevemente los distintos formatos de ficheros que ya han sido vistos en varias asignatura y que es necesario tener presentes.



En **HDFS**, los datos pueden almacenarse en diversos formatos según las necesidades de procesamiento, eficiencia y compresión. Existen formatos **basados en texto**, como **ficheros secuenciales (clave-valor)**, **CSV (Comma Separated Values)** y **JSON**, que ofrecen compatibilidad y facilidad de lectura, pero pueden ser menos eficientes en términos de almacenamiento y consulta.



Por otro lado, los formatos binarios optimizados, como Avro, ORC (Optimized Row Columnar) y Parquet, permiten un almacenamiento más eficiente y mejor compresión. Avro es un formato de filas compacto que incluye un esquema en JSON, facilitando la serialización de datos. ORC y Parquet son formatos columnarizados, ideales para consultas analíticas, aunque Parquet destaca por ser el más eficiente en filtrado por columnas.



Además, Parquet incluye una cabecera con metadatos como el número de registros y el esquema, lo que mejora su compresión y rendimiento en análisis de datos.



La elección del formato dependerá de factores como la velocidad de acceso, la compatibilidad con otras herramientas y la eficiencia en el almacenamiento dentro del ecosistema Hadoop.



#### Ejercicio  HDFS



A continuación se detalla un ejercicio que debéis reproducir todos en vuestra máquina virtual para familiarizaros con los comandos hdfs, que vais a ver que derivan de los de Linux.



En anteriores asignaturas se nombraron dichos comandos aunque no tuvisteis ocasión de emplearlos. Para refrescarlos se recomienda visitar la documentación oficial general de HDFS en el enlace:

[Apache Hadoop 3.4.1 – HDFS Commands Guide](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html)

Los comando relacionados con el filesystem están concretamente en el enlace:

[Apache Hadoop 3.4.1 – Overview](https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/FileSystemShell.html)



Los pasos a realizar son:

| Paso | Comando | Descripción |
| --- | --- | --- |
| 1 | cd /home/bigdata/hadoop-3.3.6/ | Cambia al directorio donde está instalado Hadoop. |
| 2 | sbin /start-dfs.sh | Inicia el sistema de archivos HDFS. |
| 3 | bin/hdfs dfs -help | Muestra ayuda sobre los comandos de HDFS. |
| 4 | bin/hdfs dfs -ls / | Lista los archivos en el directorio raíz de HDFS. |
| 5 | bin/hdfs dfs -mkdir /ebooks | Crea un directorio en HDFS. |
| 6 | wget URL -P destino/ | Descarga un archivo desde Internet. |
| 7 | bin/hdfs dfs -put local_path hdfs_path | Sube un archivo desde el sistema local a HDFS. |
| 8 | bin/hdfs dfs -copyFromLocal local_path hdfs_path | Copia un archivo local a HDFS. |
| 9 | bin/hdfs dfs -get hdfs_path local_path | Descarga un archivo desde HDFS al sistema local. |
| 10 | bin/hdfs dfs -cat hdfs_path | Muestra el contenido de un archivo en HDFS. |
| 11 | bin/hdfs dfs -rm hdfs_path | Elimina un archivo en HDFS. |
| 12 | bin/hdfs dfs -mv old_path new_path | Mueve o renombra un archivo en HDFS. |
| 13 | bin/hdfs dfs -du -h hdfs_path | Muestra el uso de espacio en disco de un directorio en HDFS. |
| 14 | bin/hdfs dfs -count hdfs_path | Muestra el número de archivos y espacio utilizado en HDFS. |
| 15 | bin/hdfs dfs -find / -name file_name | Busca un archivo por su nombre en HDFS. |
| 16 | bin/hdfs dfs -head hdfs_path | Muestra las primeras 10 líneas de un archivo. |
| 17 | bin/hdfs dfs -tail hdfs_path | Muestra las últimas líneas de un archiv |
| 18 | sbin/ stop-dfs.sh | Detiene el sistema de archivos HDFS. |



Es muy importante que tengáis en cuenta que en HDFS no tenemos ni el comando pwd ni el cd ya que los ficheros estás troceados y distribuidos.

Es conveniente que el alumno practique con los comandos y se familiarice con la gestión de un sistema de ficheros distribuido como es HDFS. Por tanto se espera que ejecute dichos comandos en la máquina virtual.



### 5.8 MAP REDUCE



**MapReduce** es un **modelo de programación** diseñado para procesar grandes volúmenes de datos de manera eficiente en entornos distribuidos. Es un sistema intrínsecamente paralelo, lo que significa que divide el procesamiento en múltiples tareas que pueden ejecutarse simultáneamente en diferentes nodos dentro del clúster de Hadoop.



Recuerda de lo ya estudiado, que este modelo se basa en dos fases principales:



- **Fase Map**: Convierte los elementos de un conjunto de datos en pares clave-valor, organizando la información de manera estructurada para su posterior procesamiento.

- **Fase Reduce**: Agrupa los pares de datos generados en la fase Map y aplica operaciones de agregación para obtener un conjunto más reducido y consolidado de resultados.



MapReduce fue creado por Doug Cutting, quien ha trabajado en empresas como Yahoo, Apple, Cloudera y es reconocido por su desarrollo en el ecosistema Hadoop. Su implementación está basada en el algoritmo publicado por Google en 2004, el cual definió este modelo de procesamiento distribuido.



La ejecución en MapReduce se divide en dos procesos separados (Map y Reduce), lo que permite una gran escalabilidad y el procesamiento eficiente de datos masivos.



Además, ofrece tolerancia a fallos, ya que, si un nodo falla, las tareas pueden redistribuirse a otros nodos activos sin afectar la ejecución general.



A pesar de sus ventajas, MapReduce presenta una curva de **aprendizaje elevada**, ya que requiere conocimientos en programación (principalmente en Java) y en la optimización del procesamiento distribuido. Sin embargo, sigue siendo un modelo clave en el ecosistema Hadoop y ha sentado las bases para tecnologías más modernas como **Apache Spark**.



Hadoop proporciona un entorno de ejecución diseñado específicamente para aplicaciones basadas en el modelo de programación **MapReduce**. Este modelo se divide en dos fases principales:

- **Map**, donde se lleva a cabo la ingestión y transformación de los datos de entrada. En esta etapa, los registros pueden ser procesados en paralelo, lo que permite un procesamiento distribuido y eficiente.

- **Reduce**, que se encarga de la agregación de los datos. Aquí, todos los registros que comparten una misma clave deben ser procesados juntos por una única entidad, consolidando los resultados obtenidos en la fase Map.



Para gestionar la ejecución de tareas MapReduce, Hadoop utiliza el demonio **mr-jobhistory-daemon.sh**, encargado de registrar el historial de trabajos ejecutados. La configuración de este entorno se define en el archivo **mapred-site.xml**, donde se establece el marco de ejecución de **MapReduce** mediante la propiedad **mapreduce.framework.name**.



#### Ejemplo de un proceso map reduce



Primeramente recordaremos ejemplos teóricos que seguramente ya hayáis visto, con el fin de tener la información autocontenida en esta unidad.

El procesamiento en **MapReduce** se compone de varias fases que transforman los datos de manera eficiente y distribuida.



En la **fase de datos iniciales**, los archivos almacenados en HDFS se dividen en fragmentos llamados Splits, los cuales son asignados a distintas tareas de procesamiento en paralelo. Luego, en la **fase de Map**, cada **Split** es procesado por una función de mapeo que convierte los datos en pares clave-valor, estructurando la información para su posterior agrupación.



![image](assets/cm7dawrl602vz35780e6rf2mg-INSD_PRDT_U2_Apartado7-8-1_Imagen34.jpg)



A continuación, en la fase de **Shuffle**, los datos intermedios son organizados y repartidos entre los nodos de reducción según sus claves, asegurando que todos los valores asociados a una misma clave sean enviados al mismo nodo. Es una fase de mezcla y ordenación a la vez.



![image](assets/cm7daxhke02xl3578eq7zlrr4-INSD_PRDT_U2_Apartado7-8-1_Imagen35.jpg)



Finalmente, en la fase de **Reduce**, los valores de cada clave se consolidan mediante operaciones de agregación, generando un conjunto de datos de salida más compacto y estructurado, listo para su almacenamiento o análisis posterior. Este flujo de procesamiento distribuido permite manejar grandes volúmenes de datos con alta escalabilidad y tolerancia a fallos.



![image](assets/cm7daycm6030535784f3sa1cq-INSD_PRDT_U2_Apartado7-8-1_Imagen36.jpg)



A continuación vemos un ejemplo del programa “Hola mundo” del map reduce. Es un clásico wordcount:



![image](assets/cm7daz6ax031c3578aoqg2fvo-INSD_PRDT_U2_Apartado7-8-1_Imagen37.jpg)



Otro ejemplo más gráfico es el siguiente:



![image](assets/cm7dazy9s032y3578ywmzobm5-INSD_PRDT_U2_Apartado7-8-1_Imagen38.jpg)



La siguiente imagen ilustra un código de implementación de dicho paradigma MAPREDUCE:



![image](assets/cm7db0pfp034o3578d3g8fimi-INSD_PRDT_U2_Apartado7-8-1_Imagen39.jpg)



Para profundizar en este aspecto, seguidamente se muestra un video con una ejecución de map-reduce:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652185_1/scormcontent/assets/INSD_PRDT_U2_Apartado7-8-1_Video8.mp4?v=1)



Los alumnos interesados pueden consultar información adicional en el siguiente enlace:

[Apache Hadoop 3.4.1 – MapReduce Tutorial](https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)



#### Ejemplo de ejercicio a mano de MAPREDUCE



Imaginemos que nos dan el siguiente enunciado: Calcular la media de pulsaciones de cada equipo de ciclismo cuando sus corredores llegan a meta.



Los datos son:



- 33, Contador, Movistar, 110

- 1, Induráin, Banesto, 87

- 27, Armstrong, Sky, 99

- 2, Arroyo, Banesto, 103

- 9, Olano, Banesto, 119

- 5, Ocaña, Banesto, 88

- 22, Smith, Sky, 89

- 31, Valverde, Movistar, 101

- 23, Miller, Sky, 98

- 26, Froome, Sky, 109

- 34, Quintana, Movistar, 112



Y las columnas son: Dorsal, nombre, equipo, pulsaciones. Nos piden que el cálculo se realice aplicando el model map reduce. Vamos a mostrar su resolución en un video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652185_1/scormcontent/assets/Video%207%20EjercicioMapReduce.mp4?v=1)



Este apartado será de gran utilidad para la actividad práctica de la unidad



### 5.9 YARN



**Yet Another Resource Manager (YARN)** es el componente central de Hadoop encargado de gestionar los recursos del clúster y distribuirlos eficientemente entre las diferentes aplicaciones que se ejecutan en el sistema. Su principal función es coordinar la asignación de **CPU (cores)** y **memoria (RAM)** para garantizar que cada aplicación disponga de los recursos necesarios sin afectar la ejecución de otras tareas.



YARN opera mediante un mecanismo de reserva y asignación de recursos. Cuando una aplicación solicita recursos para su ejecución, **YARN revisa el estado del clúster**, identificando qué recursos están disponibles en cada nodo. Si hay suficientes recursos libres, **asigna a la aplicación los cores y la RAM correspondientes en los nodos disponibles**. De esta manera, optimiza el uso del hardware, evita la sobrecarga de los nodos y permite la ejecución eficiente de múltiples aplicaciones en paralelo.



Gracias a esta arquitectura, **YARN mejora la escalabilidad y flexibilidad** del ecosistema Hadoop, permitiendo la coexistencia de distintos motores de procesamiento como **MapReduce, Spark, Tez y Flink** sobre un mismo clúster, lo que lo convierte en un elemento clave en entornos de Big Data modernos.



![image](assets/cm7dbhzfc03ds3578qxav8bt7-INSD_PRDT_U2_Apartado7-9_Imagen40.jpg)



#### Características de YARN



A continuación se detallan una serie de características de Yarn:



- **Sistema operativo distribuido de Hadoop**: YARN actúa como un sistema operativo distribuido dentro del ecosistema Hadoop, gestionando los recursos del clúster de manera eficiente.

- **Yet Another Resource Negotiator**: Su nombre proviene de su función principal como un negociador de recursos en entornos de procesamiento distribuido.

- **Multi-tenant**: Permite que múltiples aplicaciones y usuarios compartan los mismos recursos del clúster de manera segura y eficiente.

- **Utilización del clúster**: Optimiza el uso de los nodos disponibles, evitando desperdicio de recursos y maximizando el rendimiento.

- **Gestionar recursos**: Controla la asignación de CPU, memoria y otros recursos a las aplicaciones en ejecución.

- **Planificar tareas**: Decide qué trabajos deben ejecutarse, en qué nodos y en qué orden, optimizando la distribución de la carga de trabajo.

- **Escalabilidad**: Se adapta al crecimiento del clúster, permitiendo la ejecución de aplicaciones en infraestructuras de gran tamaño.

- **Compatibilidad**: Soporta diferentes frameworks de procesamiento como MapReduce, Spark, Tez y Flink, permitiendo la ejecución de múltiples motores en un mismo entorno.

- **Optimiza qué nodos deben recibir trabajo**: Selecciona los nodos más adecuados para ejecutar tareas basándose en su carga y disponibilidad.

- **Reasigna trabajos en caso de fallo**: Garantiza la tolerancia a fallos al redistribuir tareas si un nodo deja de responder.

- **Propósito específico**: Está diseñado específicamente para Hadoop y otros frameworks que utilizan HDFS como sistema de almacenamiento distribuido.

- **Su gran competidor es Mesos**: Apache Mesos es otra tecnología de orquestación de recursos, utilizada en entornos más generales y no limitada a Hadoop.

- **Demonio**: start-yarn.conf: Archivo de configuración utilizado para iniciar YARN en un clúster Hadoop.

- **Configuración**: yarn-site.xml: Contiene las propiedades de configuración clave para definir el comportamiento de YARN.

- **Propiedad yarn.resourcemanager.hostname**: Define la dirección del nodo que actúa como ResourceManager, encargado de coordinar la asignación de recursos en el clúster.



#### Componentes de YARN



El procesamiento en YARN sigue una arquitectura maestro-esclavo. El **ResourceManager** actúa como el nodo maestro y recibe todas las solicitudes de procesamiento. Su función es asignar las tareas a los distintos **NodeManagers**, que son los nodos encargados de la ejecución real de las tareas.



Los **NodeManagers** están instalados en cada máquina que contiene **DataNodes** y son responsables de la ejecución de las tareas en esos nodos.



A medida que los datos son procesados en paralelo en diferentes nodos, los resultados parciales son enviados de vuelta al ResourceManager, que finalmente fusiona los resultados y envía la respuesta al cliente.



En términos de configuración, el **ResourceManager** puede o no estar en la misma máquina que el **NameNode**, aunque generalmente es recomendable que lo esté, ya que ambos actúan como nodos maestros en el clúster. En contraste, los **NodeManagers** deben instalarse y configurarse en todas las máquinas donde operan los **DataNodes**, ya que son responsables de coordinar y ejecutar las tareas dentro del clúster.



La siguiente imagen ilustra dichos componentes:



![image](assets/cm7dbpi7d03jq3578cjy3lyvf-INSD_PRDT_U2_Apartado7-9_Imagen40.jpg)



## 6. Conclusiones



### 6.1 Conclusiones de la unidad



Tras haber estudiado el contenido de esta unidad y haber visualizado los vídeos, el alumno debería ser capaz de:



1. Entender las motivaciones de la aparición de Big data
2. Conocer la arquitectura ( sistemas distribuidos) que lo soporta
3. Identificar el ecosistema Hadoop como una de las soluciones principales, identificando componentes y funcionalidades
4. Dominar HDFS y el framework MAPREDUCE



Resulta vital saber manejarse en un sistema de ficheros distribuidos como es HDFS , recomendando al alumnos realizar prácticas en la creación y manipulación de ficheros en ese filesystem.

Adicionalmente es interesante entrenar en la creación de soluciones basadas en el modelo MAPREDUCE. del lenguaje que ayude a alumno a realizar códigos de forma eficiente y con un enfoque funcional.



También es muy aconsejable recordar aquellos conceptos que se han visto en otras asignaturas y que en esta sección se vuelven a mencionar a modo de recuerdo.



Si al llegar a este punto:



•

Sientes confianza y soltura para explicar todo lo relacionado con Big data ( motivación de parición, características V’s e implementación mediante entorno Hadoop) 

•

Entiendes el entrono Hadoop con foco principal en HDFS y MAPREDUCE 

•

Comprendes los ejercicios realizados



Se podría decir que has superado las expectativas de esta primera unidad y posees la base que se requiere para enfrentarte con éxito primeramente a las actividades prácticas de esta unidad y seguidamente a las siguientes unidades.
