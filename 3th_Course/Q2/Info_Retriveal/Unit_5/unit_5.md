# Unidad 5. Análisis de Redes Sociales con Python.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Aspectos Teóricos Del Sna](#2-aspectos-teóricos-del-sna)
  - [2.1 Introducción](#21-introducción)
  - [2.2 Grafos y redes, ¿qué son?](#22-grafos-y-redes-qué-son)
  - [2.3 Tipos de redes](#23-tipos-de-redes)
  - [2.4 Propiedades fundamentales](#24-propiedades-fundamentales)
- [3. El Caso Enron](#3-el-caso-enron)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Estructura de datos y limpieza](#32-estructura-de-datos-y-limpieza)
  - [3.3 Pipeline, flujo completo de tratamiento de datos](#33-pipeline-flujo-completo-de-tratamiento-de-datos)
- [4. Librería Networkx](#4-librería-networkx)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Creación y manipulación de grafos](#42-creación-y-manipulación-de-grafos)
  - [4.3 Operaciones fundamentales en NetworkX](#43-operaciones-fundamentales-en-networkx)
  - [4.4 Enlaces de interés](#44-enlaces-de-interés)
- [5. Análisis De Métricas De Red Con Networkx](#5-análisis-de-métricas-de-red-con-networkx)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Métricas de grado](#52-métricas-de-grado)
  - [5.3 Centralidad de intermediación (Betweenness Centrality)](#53-centralidad-de-intermediación-betweenness-centrality)
  - [5.4 Centralidad de cercanía (Closeness Centrality)](#54-centralidad-de-cercanía-closeness-centrality)
  - [5.5 Centralidad de autovector (Eigenvector Centrality) y PageRank](#55-centralidad-de-autovector-eigenvector-centrality-y-pagerank)
  - [5.6 Caso de uso](#56-caso-de-uso)
- [6. Análisis De Comunidades Con Networkx O Community](#6-análisis-de-comunidades-con-networkx-o-community)
  - [6.1 Introducción](#61-introducción)
  - [6.2 Métodos para la detección de comunidades](#62-métodos-para-la-detección-de-comunidades)
  - [6.3 Implementación con NetworkX](#63-implementación-con-networkx)
  - [6.4 Interpretación de uso](#64-interpretación-de-uso)
  - [6.5 Enlaces de interés](#65-enlaces-de-interés)
- [7. Visualización De Redes: Gephi Y Matplotlib](#7-visualización-de-redes-gephi-y-matplotlib)
  - [7.1 Introducción](#71-introducción)
  - [7.2 Visualización con matplotlib y NetworkX](#72-visualización-con-matplotlib-y-networkx)
  - [7.3 Visualización con Gephi](#73-visualización-con-gephi)
- [8. Aplicaciones De Sna](#8-aplicaciones-de-sna)
  - [8.1 Introducción](#81-introducción)
  - [8.2 Análisis de redes sociales corporativas](#82-análisis-de-redes-sociales-corporativas)
  - [8.3 Sistemas de recomendación basados en grafos](#83-sistemas-de-recomendación-basados-en-grafos)
  - [8.4 Detección de fraude y anomalías](#84-detección-de-fraude-y-anomalías)
- [9. Conclusiones](#9-conclusiones)
  - [9.1 Conclusiones de la unidad](#91-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad, nos adentraremos en el universo del Análisis de Redes Sociales (Social Network Analysis, SNA) empleando herramientas de Python, con un enfoque técnico e integral. La teoría de grafos y el análisis de redes no se limitan a las populares redes sociales como Twitter, Facebook o LinkedIn; de hecho, pueden aplicarse al análisis de relaciones internas en empresas (como el conocido caso Enron), a la comunicación entre repositorios de software, a la propagación de información en comunidades de desarrolladores y a muchos otros contextos.

¿Por qué es relevante el SNA en un grado de Ingeniería de Software?

- Permite modelar y abstraer interacciones complejas mediante nodos (entidades) y aristas (relaciones).
- Proporciona métricas y métodos para cuantificar la importancia de ciertos nodos en la red, ya sea para identificar “influencers”, detectar riesgos o mejorar la arquitectura de un sistema.
- Facilita la determinación de patrones y la segmentación de comunidades dentro de cualquier conjunto de datos con elementos interconectados, generando insights estratégicos para la toma de decisiones.

En los apartados que componen esta unidad, abordaremos primero los fundamentos teóricos, antes de pasar a la práctica con herramientas específicas como NetworkX. Posteriormente, aplicaremos estos conocimientos al caso Enron, un conjunto de datos real y emblemático que nos revelará cómo es posible descubrir información oculta y patrones relacionales en grandes volúmenes de datos corporativos. Asimismo, trataremos el análisis de comunidades, la visualización de redes con librerías y plataformas como gephi y matplotlib, y cerraremos con diversas aplicaciones prácticas, algunas directamente relacionadas con lo que ya hemos visto en unidades anteriores (por ejemplo, la extracción de datos de Twitter y su representación en forma de red).



- **Aspectos teóricos del SNA**  
  La Teoría de Grafos es la base técnica del SNA, una rama de las matemáticas y la computación que se encarga de modelar escenarios complejos mediante una combinación de “nodos” y “aristas” (las conexiones entre nodos). Cada nodo representa un ente individual (un usuario, un dispositivo, una cuenta de correo, etc.), y cada arista representa la relación entre esos entes. Por ejemplo, si analizamos la red de empleados de una empresa, cada persona podría ser un nodo, y las aristas podrían simbolizar si dos empleados se comunican por correo con cierta frecuencia, si trabajan juntos en proyectos o si están en el mismo departamento.
- **El Caso Enron**  
  El caso Enron es uno de los ejemplos más ilustres de cómo el Análisis de Redes Sociales (SNA) puede aportar claridad y evidencias en situaciones corporativas complejas. El estudio de los correos electrónicos de Enron, disponibles en un extenso dataset público ([https://www.kaggle.com/datasets/wcukierski/enron-email-dataset/data](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset/data)), ha permitido examinar la interacción entre empleados y descubrir patrones de comunicación insólitos que contribuyeron a destapar irregularidades. En este apartado, revisaremos de forma detallada la historia y relevancia de este caso, la estructura de sus datos y la manera en que podemos comenzar a tratarlos para su posterior análisis de redes.
- **Librería Networkx**  
  En este apartado, nos concentraremos en:

  - Explicar qué es NetworkX y por qué resulta tan relevante en el análisis de redes sociales en Python.
  - Instalar y configurar el entorno de trabajo.
  - Crear, modificar y consultar grafos en NetworkX (añadiendo nodos, aristas y atributos).
  - Leer y escribir grafos desde y hacia formatos estándar (y, en especial, desde los DataFrames que hemos preparado tras la limpieza del dataset Enron).
- **Análisis de métricas de red con Networkx**  
  En el contexto de Enron, estas métricas pueden arrojar luz sobre cuestiones tan esenciales como:

  - ¿Quiénes eran los empleados con un rol central en la comunicación?
  - ¿Qué nodos actuaban como puentes entre distintos departamentos?
  - ¿Se distinguen usuarios con alto poder de diseminación de información?
- **Análisis de comunidades con Networkx o Community**  
  En este apartado, abordaremos las técnicas de detección de comunidades (o community detection) con Python, apoyándonos en NetworkX y en librerías complementarias como python-louvain (a menudo referida sencillamente como community). Veremos, en detalle, la justificación teórica de la detección de comunidades, la interpretación práctica de los resultados y, por supuesto, la implementación técnica con el dataset de Enron como ejemplo de uso.
- **Visualización de redes: Gephi y Matplotlib**  
  En este apartado, profundizaremos en dos enfoques complementarios para la visualización de redes:

  - **matplotlib,** la librería estándar de Python para gráficos, que junto con las funciones de dibujo de NetworkX permite producir diagramas de red de forma relativamente directa.
  - **gephi,** una herramienta especializada en la exploración visual de grafos, más potente e interactiva que matplotlib, y muy utilizada tanto en entornos académicos como profesionales.
- **Aplicaciones de SNA**  
  En este apartado, revisaremos aplicaciones destacadas del SNA que pueden resultar de gran interés para estudiantes y profesionales de la Ingeniería de Software, mostrando cómo estas técnicas se aplican en distintos contextos y qué beneficios aportan.



#### Objetivos



Al concluir esta unidad, el estudiante será capaz de:



1. Comprender la base teórica del Análisis de Redes Sociales (SNA)
2. Distinguir los conceptos fundamentales de grafos (nodos, aristas, grados, centralidades, densidad, etc.)
3. Conocer las propiedades y tipos de redes (dirigidas, no dirigidas, ponderadas, bipartitas, multigrafo, etc.).
4. Revisar y analizar un caso real (Enron) para entender la utilidad de los grafos en la detección de patrones y flujos de comunicación corporativos.
5. Aprender a utilizar la librería NetworkX de Python para crear, manipular y analizar redes, aplicando métodos de cálculo de métricas como centralidad de grado, centralidad de intermediación, cercanía, entre otros.
6. Familiarizarse con algoritmos de detección de comunidades (por ejemplo, Louvain), así como con el manejo de librerías adicionales (o extensiones como community) que facilitan la partición de la red en subgrupos.
7. Dominar técnicas de visualización de redes con matplotlib y herramientas externas como gephi, que permiten presentar los hallazgos de manera clara y efectiva.
8. Explorar aplicaciones prácticas del SNA en contextos que van más allá de las redes sociales convencionales, incluyendo proyectos de software, redes colaborativas, análisis de repositorios y sistemas de recomendación basados en grafos



## 2. Aspectos Teóricos Del Sna



### 2.1 Introducción



![image](assets/cm8nnbiwj005c356xpcmtofzg-stock-image.jpg)



La Teoría de Grafos es la base técnica del SNA, una rama de las matemáticas y la computación que se encarga de modelar escenarios complejos mediante una combinación de “nodos” y “aristas” (las conexiones entre nodos). Cada nodo representa un ente individual (un usuario, un dispositivo, una cuenta de correo, etc.), y cada arista representa la relación entre esos entes. Por ejemplo, si analizamos la red de empleados de una empresa, cada persona podría ser un nodo, y las aristas podrían simbolizar si dos empleados se comunican por correo con cierta frecuencia, si trabajan juntos en proyectos o si están en el mismo departamento.

Lo siguiente que nos preguntaremos es, ¿qué aporta el Análisis de Redes Sociales en la práctica a la ingeniería de software?

Imagina que lideras un proyecto de desarrollo de software y quieres descubrir cuáles son los repositorios más importantes en tu organización, o cuáles son los programadores que suelen actuar como “puente” en la transmisión de conocimiento entre diferentes equipos. O tal vez, desde un enfoque de marketing digital, te interese saber en qué punto de la red de usuarios hay mayor probabilidad de que se viralice una oferta o un contenido. El SNA te proporciona un conjunto de técnicas cuantitativas y cualitativas para dar respuesta a estas preguntas, detectando “nodos clave”, identificando comunidades de usuarios afines, o revelando patrones ocultos de comunicación.

En este sentido, una persona que maneje conceptos de SNA se encuentra en una posición privilegiada para diseñar soluciones que exploten la estructura de los datos. Por ejemplo, es posible desarrollar sistemas de recomendación basados en la proximidad en la red (un clásico de servicios como YouTube, Netflix o redes de empleo como LinkedIn). También puede ser útil en la optimización de la comunicación interna de grandes empresas o en la detección de anomalías en flujos de información (relevante en ciberseguridad y en auditoría interna).



### 2.2 Grafos y redes, ¿qué son?



La forma más común de representar un conjunto de relaciones es mediante un grafo. Desde la perspectiva formal de la teoría de grafos, un grafo 𝐺 se define como un par (𝑉, 𝐸), donde 𝑉 representa el conjunto de nodos (o vértices) y 𝐸 el conjunto de aristas (o enlaces, o relaciones).

Para comprenderlo intuitivamente, puedes imaginar un grafo como un mapa conceptual en el que cada círculo (nodo) corresponde a una entidad (una persona, un servidor, un repositorio, etc.), y cada línea (arista) que conecta dos círculos representa alguna relación entre esas dos entidades (una amistad, una mención en Twitter, un correo enviado, un vínculo en un repositorio).

Cuando decimos “red social”, nos referimos a un tipo de grafo específico en el que los nodos representan actores sociales (personas, organizaciones, cuentas de redes sociales, etc.) y las aristas describen relaciones o interacciones. De esta forma, la “red social” no siempre tiene que ver con aplicaciones tecnológicas de interacción. Por ejemplo, podemos hablar de la red social de investigadores que publican artículos conjuntos en un congreso, o de la red social de máquinas en un entorno de Internet de las Cosas, siempre y cuando haya una relación que las vincule.

Imaginemos una red social compuesta por tres personas: Ana, Bruno y Carlos. Supongamos que Ana y Bruno son amigos, y que Bruno y Carlos también lo son, pero Ana y Carlos no se conocen. En el grafo, habría tres nodos (Ana, Bruno y Carlos) y dos aristas (Ana-Bruno y Bruno-Carlos).



![image](assets/cm8nndu4x009i356xs2g8m66z-Imagen34.png)



Aunque en teoría un grafo es una abstracción general de nodos y aristas, al tratarse de redes sociales hablamos de interacciones humanas o de sistemas sociales. Esto implica ciertas características adicionales:



- **Interpretación contextual**  
  No basta con contar cuántos enlaces hay; debemos comprender el significado de cada relación (seguidores, co-ocurrencia de hashtags, colaboraciones en proyectos, etc.).
- **Importancia de la metadata**  
  A menudo, cada arista y nodo contiene atributos adicionales (edad, género, ubicación geográfica, volumen de tuits, etc.) que enriquecen el análisis.
- **Dinámica temporal**  
  Las redes sociales cambian constantemente y el análisis estático (sacar un “snapshot” de la red en un momento dado) puede complementarse con un análisis temporal.



Cuando construyes un grafo genérico, a menudo centras la atención en la forma y la topología de la red. En cambio, al hablar de redes sociales, el análisis se enriquece al añadir la dimensión humana o interaccional, lo que permite responder preguntas más específicas:



•

¿Quién es el más influyente en la discusión?

•

¿Cómo se agrupan las personas por intereses comunes?

•

¿Quién actúa como puente entre dos comunidades que de otro modo no se comunicarían?



### 2.3 Tipos de redes



Dentro de la teoría de grafos aplicada al SNA, es esencial distinguir varias categorías de redes, ya que determinan cómo interpretamos las relaciones y qué algoritmos o métricas conviene aplicar.



- **Redes no dirigidas**  
  Si la relación entre dos de los nodos es **bidireccional,** es decir, no importa quién inicia la conexión, hablamos de redes no dirigidas. Por ejemplo, si consideramos la “amistad” en Facebook, por lo general es mutua: si yo soy tu amigo, tú también eres mi amigo. En la notación formal, se representa una arista no dirigida entre nodos u y v como (u,v), implicando que la conexión es simétrica.
- **Redes dirigidas**  
  En otros casos, la relación sí tiene una **dirección**. Por ejemplo, en Twitter yo te puedo seguir a ti, pero tú no necesariamente me sigues a mí. Esto se modela con **redes dirigidas,** donde las aristas tienen un sentido específico, que se suele denotar con ⟨u,v⟩, indicando que la conexión “va” de u hacia v. Este tipo de redes cobra especial relevancia en el análisis de flujos de información (quién envía correo a quién, quién retuitea a quién, etc.).
- **Redes ponderadas**  
  En muchas situaciones, no solo interesa saber si dos nodos están conectados, sino también la **intensidad** o el **peso** de esa conexión. En estos casos hablamos de redes ponderadas (weighted graphs), donde a cada arista se le asigna un valor numérico que puede representar la frecuencia de los mensajes intercambiados, el volumen de tráfico, la fortaleza de una relación, etc. Así, una arista entre dos personas que se envían 10 correos al día podría tener un peso mayor que la de dos personas que se envían 1 correo al mes. Además, estas se pueden combinar con otros tipos de redes como las dirigidas o no dirigidas
- **Redes bipartitas**  
  Existen escenarios donde los nodos se dividen naturalmente en **dos conjuntos disjuntos** y las conexiones solo se dan entre estos dos grupos, no dentro de un mismo grupo. Es el caso de las llamadas **redes bipartitas.** Un ejemplo muy común es el de “usuarios” y “productos” en un sistema de recomendación: cada usuario puede “conectarse” con uno o varios productos que ha comprado o que le gustan, pero los usuarios no se conectan directamente entre sí, y los productos no se conectan directamente entre ellos. Este tipo de modelado es útil para algoritmos de recomendación, para análisis de coautorías o para estudios de afinidad en marketing.



![image](assets/cm8nnkkql00ct356x3qjvle3e-Imagen35.png)



### 2.4 Propiedades fundamentales



El conocimiento de ciertas propiedades en un grafo proporciona una perspectiva más rica del funcionamiento de la red. A continuación, veamos las propiedades esenciales, útiles para caracterizar y comparar distintos tipos de redes sociales.



1. El grado se refiere, de forma general, al número de conexiones que tiene un nodo. En redes no dirigidas, simplemente se llama “grado” (degree). En redes dirigidas, se distingue entre grado de entrada (in-degree), el número de aristas que llegan a un nodo, y grado de salida (out-degree), el número de aristas que parten de él.

   Por ejemplo, si en Twitter Bruno sigue a 20 personas, entonces su out-degree es 20, pero si tiene 100 seguidores, su in-degree es 100. Conocer el grado de cada nodo nos permite identificar a los actores con más conexiones, que suelen ser piezas claves en la propagación de información o en la cohesión de la red.
2. La densidad de un grafo mide qué proporción de las conexiones posibles está efectivamente presente. En un grafo con 𝑛 nodos no dirigido, el máximo número de aristas posible (si todos los nodos se conectan con todos) es

   La densidad, por ende, se calcula como:

   Cuando este valor es cercano a 1, significa que el grafo está muy interconectado (casi todos los nodos están unidos entre sí). Por el contrario, si es muy bajo, la red se halla muy dispersa o desconectada.
3. El diámetro de un grafo es la máxima distancia entre cualquier par de nodos. La distancia se mide, generalmente, en número de aristas que se deben recorrer para ir de un nodo a otro por el camino más corto.

   Un diámetro pequeño indica que la red es, en cierto modo, “pequeña”, pues incluso los dos nodos más alejados están a pocos pasos de distancia.
4. Finalmente, la conectividad determina si hay un camino que conecte a todos los nodos de la red. En un grafo no dirigido, se dice que es conexo si para cualquier par de nodos existe un camino entre ellos.

   En un grafo dirigido, la noción equivalente es la de fuertemente conexo (si es posible ir de cualquier nodo a cualquier otro nodo siguiendo la dirección de las aristas) o débilmente conexo (si al ignorar la dirección, el grafo se vuelve conexo). La conectividad ayuda a entender hasta qué punto una red está fragmentada en subredes aisladas.



## 3. El Caso Enron



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



El caso Enron es uno de los ejemplos más ilustres de cómo el Análisis de Redes Sociales (SNA) puede aportar claridad y evidencias en situaciones corporativas complejas. El estudio de los correos electrónicos de Enron, disponibles en un extenso dataset público ([https://www.kaggle.com/datasets/wcukierski/enron-email-dataset/data](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset/data)), ha permitido examinar la interacción entre empleados y descubrir patrones de comunicación insólitos que contribuyeron a destapar irregularidades. En este apartado, revisaremos de forma detallada la historia y relevancia de este caso, la estructura de sus datos y la manera en que podemos comenzar a tratarlos para su posterior análisis de redes.

Enron era una compañía estadounidense del sector energético que, a finales de la década de 1990, figuraba entre las mayores empresas de Estados Unidos. Sin embargo, se vio envuelta en uno de los mayores escándalos financieros de la historia corporativa. A raíz de prácticas contables irregulares, la empresa se declaró en bancarrota en diciembre de 2001, arrastrando con ello la credibilidad de auditores y organismos reguladores.

Durante las investigaciones llevadas a cabo por la Comisión de Bolsa y Valores (SEC, por sus siglas en inglés) y otras entidades gubernamentales, se incautó una gran cantidad de correos electrónicos internos. Dichos correos fueron posteriormente desclasificados (en parte, con fines legales y académicos), dando lugar a un dataset muy rico en contenido, pues abarca varios años de comunicación entre empleados de distintos rangos dentro de la organización. Este conjunto de datos se ha convertido en un recurso fundamental para el estudio del Análisis de Redes Sociales y la minería de textos, ya que ofrece un caso real —y lamentablemente famoso— de cómo la información fluye en una gran corporación.

La relevancia de este dataset de Enron radica en que no se trata de una simulación o de datos anecdóticos, sino de información real sobre interacciones humanas y empresariales. Más allá del mero interés histórico, estos correos permiten investigar la dinámica de la comunicación en entornos corporativos a gran escala, la formación de comunidades dentro de la empresa y la detección de patrones relacionales que, a menudo, resultan invisibles sin técnicas de SNA.



### 3.2 Estructura de datos y limpieza



Para entender cómo se lleva a cabo el Análisis de Redes Sociales en el caso Enron, es esencial conocer cómo están organizados los correos y cuáles son los pasos de limpieza de datos más habituales. Incluso si la meta final es construir un grafo que represente las relaciones de envío y recepción de mensajes, debemos antes asegurar que la información se encuentra en un estado homogéneo y fiable.



#### Formato de los correos



El Enron Email Dataset se distribuye a menudo en el formato Maildir, una convención típica en sistemas UNIX en la que cada buzón de correo se estructura en diferentes carpetas (por ejemplo, sent_items, inbox, deleted_items, all_documents, etc.). Cada mensaje se almacena generalmente en un archivo de texto plano con encabezados en estilo MIME:

- **Message-ID:** Identificador único del correo.
- **Date:** Fecha y hora de envío.
- **From:** Dirección de correo del remitente.
- **To:** Lista de destinatarios principales.
- **Subject:** Asunto del correo.
- **Cc y Bcc:** Destinatarios en copia visible y oculta.
- **Body:** Contenido principal del mensaje, que puede ser texto plano o HTML.

Las versiones más recientes o adaptadas del dataset pueden venir en otros formatos, como CSV, PST (propio de Microsoft Outlook) o incluso JSON. En cualquier caso, la estructura lógica es similar: disponemos de un conjunto de mensajes, cada uno con sus metadatos (campos de cabecera) y su cuerpo de texto.



![image](assets/cm8nnz4cs005z356x9b1c9lbs-Imagen36.jpg)



#### Limpieza y normalización



Trabajar con un dataset tan amplio y variado supone afrontar numerosos desafíos, especialmente cuando deseamos obtener un grafo de calidad.

Uno de los problemas son los correos duplicados. Es frecuente que un mismo hilo de conversación aparezca en las carpetas de varios empleados. Por ejemplo, si un empleado reenvía un correo a otro grupo, generará múltiples copias casi idénticas.

Por otro lado, tenemos los alias y variantes de direcciones. Un mismo usuario puede figurar como [firstname.lastname@enron.com](mailto:firstname.lastname@enron.com), [f.lastname@enron.com](mailto:f.lastname@enron.com), [apelido_nombre@enron.com](mailto:apelido_nombre@enron.com), e incluso con direcciones personales o antiguas.

También nos encontramos correos personales o spam. La actividad de los empleados no siempre está relacionada con tareas corporativas; en ocasiones, los buzones incluyen correos personales o spam. Dependiendo de los objetivos del análisis, puede interesar excluirlos.

Los campos incompletos son otro problema. No todos los correos tienen el campo Subject rellenado, y a veces los campos To o From pueden estar vacíos o contener direcciones inválidas (por ejemplo, cadenas de texto que no se corresponden con una dirección de correo).

Por último, podemos tener codificaciones mixtas. Es posible encontrar texto en ASCII, UTF-8 y otras codificaciones, lo cual complica la normalización del contenido.

Aunque existen scripts y librerías específicamente diseñadas para el Enron Email Dataset, el proceso de limpieza suele seguir un enfoque general que puede resumirse en:

1. **Lectura sistemática de todos los ficheros del dataset.** Se recorre cada carpeta y subcarpeta para obtener la ruta de cada archivo que representa un correo.
2. **Parseado de los metadatos (Message-ID, From, To, Cc, Bcc, Date, Subject).** Aquí se suelen usar herramientas como email de Python o expresiones regulares que reconozcan cabeceras MIME.
3. **Identificación y resolución de alias:** Para cada dirección de correo, se implementa un método de normalización que convierta variantes en un nombre único de usuario. Por ejemplo, [firstname.lastname@enron.com](mailto:firstname.lastname@enron.com), [f.lastname@enron.com](mailto:f.lastname@enron.com) y [firstname.l@enron.com](mailto:firstname.l@enron.com) podrían unificarse si se evidencia que todas pertenecen a la misma persona. En entornos corporativos a menudo se dispone de un directorio interno que asocia alias con nombres reales.
4. **Eliminación de duplicados:** Para este paso, se comparan las cabeceras (Message-ID, Date, From, To) y, si coincide un porcentaje alto de campos o el Message-ID, se asume que se trata del mismo correo.
5. **Filtrado por rango temporal:** Según el objetivo del análisis, se selecciona un período de estudio (por ejemplo, 1999-2001) para excluir correos demasiado antiguos o posteriores al colapso de la empresa que no aporten valor.
6. **Almacenamiento en formato estructurado (CSV, JSON, base de datos relacional, etc.):** Cada correo limpio se representa como una fila o documento con los campos principales. De esta forma, se facilita su consulta y el procesamiento ulterior.

Este tipo de rutinas de limpieza y normalización son cruciales para evitar que un mismo usuario aparezca con varios nombres en el grafo (lo cual provocaría segmentaciones artificiales). Por ejemplo, podríamos hacer una función básica para normalizar las direcciones de correo.



```coffeescript
def normalizar_direccion(correo):
    if not correo:
        return None

    # Convertir a minúsculas
    correo = correo.lower().strip()

    # Eliminar comillas o caracteres extraños
    correo = correo.replace('"', '').replace("'", "")

    # Podríamos agregar más reglas, p.e. eliminar 'enron.com' repetido
    # correo = re.sub(r'\@enron\.com+', '@enron.com', correo)

    return correo

entradas_test = ["  John.Smith@ENRON.COM ", "J.SMITH@enron.com  ", "john.smith@ENRON.com", None]
for e in entradas_test:
    print(e, " -> ", normalizar_direccion(e))
# Output
  John.Smith@ENRON.COM   ->  john.smith@enron.com
J.SMITH@enron.com    ->  j.smith@enron.com
john.smith@ENRON.com  ->  john.smith@enron.com
None  ->  None
```



#### Privacidad



Es fundamental recalcar que, aunque el dataset sea de acceso público, contiene información sensible de personas que quizá no dieron consentimiento expreso para el uso de sus correos en investigaciones abiertas. Si bien los correos de Enron se han empleado durante años en contextos académicos, conviene siempre tener presente la dimensión ética:



- **Anonimización**  
  Algunas versiones del dataset sustituyen los nombres de los empleados por identificadores anónimos.
- **Uso responsable**  
  Se aconseja no difundir los contenidos de los mensajes si estos incluyen datos personales o confidenciales que no sean estrictamente necesarios para el análisis de redes.
- **Formación**  
  Este caso es un recordatorio valioso de cómo la comunicación interna de una empresa puede volverse pública e incluso evidencia en litigios. Las organizaciones deben contar con políticas claras de retención de datos y privacidad.



### 3.3 Pipeline, flujo completo de tratamiento de datos



A continuación, veremos cómo crear un pipeline completo que resulta esencial a la hora de analizar los datos. Este pipeline nos deberá permitir:

1. Obtener el dataset desde la fuente oficial o un repositorio fiable.
2. Recorrer la estructura de ficheros y extraer los campos de interés (remitente, destinatario, fecha, etc.).
3. Normalizar direcciones de correo y otros metadatos (por ejemplo, fechas, formatos de texto).
4. Eliminar duplicados y correos irrelevantes (spam, correos vacíos, etc.).
5. Exportar el resultado a un formato fácil de usar (CSV, JSON, etc.) para su posterior análisis con NetworkX.



![image](assets/cm8no9lln00bq356xyogf4qqt-Imagen37.jpg)



#### Obtención del dataset



El Enron Email Dataset puede descargarse de varios sitios académicos y repositorios. Uno de los más usados históricamente es el de la Universidad Carnegie Mellon (CMU). La siguiente URL suele ofrecer distintas versiones y tamaños del dataset, [https://www.cs.cmu.edu/~enron/](https://www.cs.cmu.edu/~enron/), por ejemplo, la última versión disponible de 2015 la encontramos: [https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz](https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz)

En este enlace puedes encontrar archivos comprimidos que contienen la estructura Maildir para diversos empleados de Enron.

Sin embargo, en este curso, por facilidad, vamos a recurrir al famoso sitio de repositorios de datos Kaggle, donde encontraremos diversas versiones de este dataset. En nuestro caso, utilizarmo es el siguiente: [https://www.kaggle.com/datasets/wcukierski/enron-email-dataset/data](https://www.kaggle.com/datasets/wcukierski/enron-email-dataset/data).

Para ello simplemente deberemos ejecutar el siguiente código:



```python
import kagglehub

# Download latest version
path = kagglehub.dataset_download("wcukierski/enron-email-dataset")

print("Path to dataset files:", path)
```



Se descargará un único CSV con el dataset en el siguiente directorio en caso de utilizar Google Colab: “/root/.cache/kagglehub/datasets/wcukierski/enron-email-dataset/versions/2/emails.csv”, lo cual nos facilitará el trabajo al no tener que recorrer todos los directorios extraídos con el archivo comprimido. Si el código anterior nos proporciona otro directorio, lo único que deberemos saber es que dentro de ese directorio se encuentra el archivo “emails.csv”.



#### Estructura de datos



Al leer el CSV encontraremos dos columnas que nos ayudarán a conocer a qué archivo hace referencia y su contenido. En el interior del mensaje (columna “message”), cada correo electrónico está representado por un texto plano con cabeceras en formato MIME.

Si quisiésemos leerlo podríamos ejecutar:



```ruby
import pandas as pd

df = pd.read_csv("/root/.cache/kagglehub/datasets/wcukierski/enron-email-dataset/versions/2/emails.csv")

print(df['message'].iloc[0])
```



```python
import polars as pl

df = pl.read_csv("/root/.cache/kagglehub/datasets/wcukierski/enron-email-dataset/versions/2/emails.csv")

print(df['message'][0])
```



Y podemos ver los diferentes MIME con el contenido en nuestro mensaje:



```yaml
Message-ID: <18782981.1075855378110.JavaMail.evans@thyme>
Date: Mon, 14 May 2001 16:39:00 -0700 (PDT)
From: phillip.allen@enron.com
To: tim.belden@enron.com
Subject: 
Mime-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
X-From: Phillip K Allen
X-To: Tim Belden <Tim Belden/Enron@EnronXGate>
X-cc: 
X-bcc: 
X-Folder: \Phillip_Allen_Jan2002_1\Allen, Phillip K.\'Sent Mail
X-Origin: Allen-P
X-FileName: pallen (Non-Privileged).pst

Here is our forecast
```



Conociendo esto, podríamos extraer el contenido de un header de MIME. Es importante recordar la codificación, ya que según el idioma podemos tener caracteres especiales que arrojen errores.

Por ejemplo, podríamos extraer el asunto del email y el listado de emails:

- Primero leer el mensaje deseado con Pandas o Polars



```ruby
import pandas as pd

df_pandas = pd.read_csv(base_path)

raw_message = df_pandas['message'].iloc[25]
```



```ruby
import polars as pl

df_polars = pl.read_csv(base_path)

raw_message = df_polars['message'][25]
```



- A continuación, definimos las funciones para decodificar texto adecuadamente y leer el contenido del mensaje



```python
def decode_mime_header(header_value: str) -> str:
    """
    Decodifica cabeceras MIME con caracteres especiales.
    """
    if not header_value:
        return ''
    decoded_parts = decode_header(header_value)
    decoded_string = ""
    for text, enc in decoded_parts:
        if isinstance(text, bytes):
            try:
                decoded_string += text.decode(enc or 'utf-8', errors='replace')
            except:
                decoded_string += text.decode('utf-8', errors='replace')
        else:
            decoded_string += str(text)
    return decoded_string


def parse_recipients(field_data: str) -> list:
    """
    Toma el contenido de un campo 'To', 'Cc', 'Bcc' o 'From' (string)
    y devuelve una lista de direcciones normalizadas.
    """
    if not field_data:
        return []
    # Sustituir punto y coma por coma (por si vienen separados de forma distinta)
    field_data = field_data.replace(';', ',')
    candidatos = [x.strip() for x in field_data.split(',')]
    direcciones = [d for d in candidatos]
    return direcciones

msg = email.message_from_string(raw_message, policy=default_policy)

to_list = parse_recipients(msg.get("To", ""))
cc_list = parse_recipients(msg.get("Cc", ""))
bcc_list = parse_recipients(msg.get("Bcc", ""))
from_list = parse_recipients(msg.get("From", ""))

subject = decode_mime_header(msg.get("Subject", ""))


print("To:", to_list)
print("Cc:", cc_list)
print("Bcc:", bcc_list)
print("From:", from_list)
print("Subject:", subject)
# Output
To: ['kholst@enron.com']
Cc: []
Bcc: []
From: ['phillip.allen@enron.com']
Subject: Investment Structure
```



#### Normalización



Una vez que conocemos cómo obtener los valores de los campos del mensaje, es importante normalizar. Esto nos ayudará a tener una analítica más exacta y evitar que se considere diferente “Enron” y “ENRON”.

Por ejemplo, expandiendo la función que vimos anteriormente:



```coffeescript
import re 
def normalizar_direccion(correo: str) -> str:
    """
    Convierte la dirección de correo a minúsculas, elimina espacios y caracteres no deseados,
    y unifica repeticiones anómalas de enron.com.
    """
    if not correo:
        return None
    correo = correo.lower().strip()
    correo = correo.replace('"', '').replace("'", "").replace("<", "").replace(">", "")
    # Buscamos @enron. y @enron.enron.enron... y lo reemplazamos por @enron.com
    correo = re.sub(r'(\@enron\.)(?:enron\.)+com$', '@enron.com', correo)
    if '@' not in correo or '.' not in correo:
        return None
    return correo

entradas_test = ["  John.Smith@ENRON.COM ", "J.SMITH@enron.com  ", "john.smith@ENRON.com", None]
for e in entradas_test:
    print(e, " -> ", normalizar_direccion(e))
# Output
  John.Smith@ENRON.COM   ->  john.smith@enron.com
J.SMITH@enron.com    ->  j.smith@enron.com
john.smith@ENRON.com  ->  john.smith@enron.com
None  ->  None
```



Esta función se puede integrar en el paso anterior sin necesidad de tener que hacerlo a posteriori. Esto nos proporcionará una mejor eficiencia a la hora de procesar los datos.



#### Tratamiento de datos



En este punto, ya podríamos crear una función que combine lo anterior y nos ayude a procesar los datos devolviéndolos en un formato más fácil para el análisis.

Veamos como obtener todos los detalles:



```lua
def parse_raw_email(raw_message: str) -> dict:
    """
    Recibe el texto completo de un correo (columna 'message') y devuelve
    un diccionario con los campos parseados y normalizados.
    """
    # Cargamos el contenido con la librería 'email'
    msg = email.message_from_string(raw_message, policy=default_policy)
    
    # Extraer Message-ID (si no existe, generamos uno ficticio)
    message_id = msg.get("Message-ID", "").strip()
    if not message_id:
        message_id = "ficticio_" + str(abs(hash(raw_message)))

    # Fecha
    date_str = msg.get("Date", "").strip()

    # Asunto
    subject = decode_mime_header(msg.get("Subject", ""))

    # Remitente
    from_str = normalizar_direccion(msg.get("From", ""))

    # Destinatarios
    to_list = parse_recipients(msg.get("To", ""))
    cc_list = parse_recipients(msg.get("Cc", ""))
    bcc_list = parse_recipients(msg.get("Bcc", ""))

    # Cuerpo (solo text/plain, unimos partes si es multipart)
    body_text = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    body_text += part.get_content()
                except:
                    pass
    else:
        body_text = msg.get_content()

    # Construimos un diccionario con los campos parseados
    registro = {
        "message_id": message_id,
        "date_str": date_str,
        "from": from_str,
        "to_list": to_list,
        "cc_list": cc_list,
        "bcc_list": bcc_list,
        "subject": subject,
        "body": body_text.strip()
    }
    return registro

parse_raw_email(raw_message)
# Output
{'message_id': '<19034252.1075855687825.JavaMail.evans@thyme>',
 'date_str': 'Tue, 26 Sep 2000 09:28:00 -0700',
 'from': 'phillip.allen@enron.com',
 'to_list': ['kholst@enron.com'],
 'cc_list': [],
 'bcc_list': [],
 'subject': 'Investment Structure',
 'body': '---------------------- Forwarded by Phillip K Allen/HOU/ECT on 09/26/2000 \n04:28 PM ---------------------------\n\n\n"George Richards" <cbpres@austin.rr.com> on 09/26/2000 01:18:45 PM\nPlease respond to <cbpres@austin.rr.com>\nTo: "Phillip Allen" <pallen@enron.com>\ncc: "Larry Lewter" <retwell@mail.sanmarcos.net>, "Claudia L. Crocker" \n<clclegal2@aol.com> \nSubject: Investment Structure\n\n\nSTRUCTURE:\nTypically the structure is a limited partnership with a corporate (or LLC)\ngeneral partner.  The General Partner owns 1% of the project and carries the\nliability of construction.\n\nLAND OWNERSHIP & LOANS\nThe property would be purchased in the name of the limited partnership and\nany land loans, land improvements loans and construction loans would be in\nthe name of the limited partnership.  Each of the individual investors and\nall of the principals in Creekside would also personally guarantee the\nloans.  If the investor(s) do not sign on the loans, this generally means\nthat a larger amount of cash is required and the investor\'s share of profits\nis reduced.\n\nAll loans for residential construction, that are intended for re-sale, are\nfull recourse loans.  If we are pursuing multifamily rental developments,\nthe construction loans are still full recourse but the mortgage can often be\nnon-recourse.\n\nUSE OF INITIAL INVESTMENT\nThe initial investment is used for land deposit, engineering &\narchitectural design, soils tests, surveys, filing fees, legal fees for\norganization and condominium association formation,  and appraisals.  Unlike\nmany real estate investment programs, none of the funds are used for fees to\nCreekside Builders, LLC.  These professional expenses will be incurred over\nthe estimated 6 month design and approval period.\n\nEARLY LAND COSTS\nThe $4,000 per month costs listed in the cash flow as part of land cost\nrepresent the extension fees due to the seller for up to 4 months of\nextensions on closing.  As an alternative, we can close into a land loan at\nprobably 70% of appraised value.  With a land value equal to the purchase\nprice of $680,000 this would mean a land loan of $476,000 with estimated\nmonthly interest payments of $3,966, given a 10% annual interest rate, plus\napproximately 1.25% of the loan amount for closing costs and loan fees.\n\nEQUITY AT IMPROVEMENT LOAN\nOnce the site plan is approved by the City of Austin, the City will require\nthe development entity to post funds for fiscal improvements, referred to as\nthe "fiscals".  This cost represents a bond for the completion of\nimprovements that COA considers vital and these funds are released once the\nimprovements have been completed and accepted by COA.  This release will be\nfor 90% of the cost with the remaining 10% released one year after\ncompletion.  Releases can be granted once every 90 days and you should\nexpect that the release would occur 6 months after the start of lot\nimprovement construction.  These fiscals are usually posted in cash or an\nirrevocable letter of credit.  As such, they have to be counted as a\ndevelopment cost, even though they are not spent.  Because they are not\nspent no interest is charged on these funds.\n\nThe lot improvement loan is typically 75% of the appraised value of a\nfinished lot, which I suspect will be at least $20,000 and potentially as\nhigh as $25,000.  This would produce a loan amount of  $15,000 on $20,000\nper lot.  With estimated per lot improvement costs of $9,000, \'fiscals\' at\n$2,000 and the land cost at $8,000 , total improved lot cost is $19,000\nwhich means $0 to $4,000 per lot in total equity.  The investment prior to\nobtaining the improvement loan would count towards any equity requirement\nprovided it was for direct costs.  Thus, the additional equity for the\nimprovement loan would be $0-$184,000.   Even if the maximum loan would\ncover all costs, it is unlikely the bank would allow reimbursement of funds\nspent. The higher estimates of equity investments are shown in the\npreliminary proforma to be on the safe side.  The engineer is preparing a\ntentative site layout with an initial evaluation of the phasing, which can\nsignificantly reduce the cash equity requirement.\n\nPhasing works as follows.  If the first phase was say 40 units, the total\nlot improvement cost might average $31,000 per lot.   Of this, probably\n$13,000 would be for improvements and $19,000 for the land cost.  The\nimprovements are higher to cover large one time up front costs for design\ncosts, the entry road, water treatment costs, perimeter fencing and\nlandscaping, and so on, as well as for 100% of the land.  The land loan for\nundeveloped lots would be 70% of the appraised raw lot value, which I would\nestimate as $10,000 per lot for a loan value of $7,000 per lot.  Then the\nloan value for each improved lot would be $15,000 per lot.  This would give\nyou a total loan of $992,000, total cost of $1,232,645 for equity required\nof $241,000.  This was not presented in the initial analysis as the phasing\nis depended on a more careful assessment by the Civil Engineer as the\nseparate phases must each be able to stand on its own from a utility\nstandpoint.\n\nCONSTRUCTION LOANS\nThere are three types of  construction loans.  First, is a speculative\n(spec) loan that is taken out prior to any pre-sales activity.  Second,  is\na construction loan for a pre-sold unit, but the loan remains in the\nbuilder/developers name.  Third, is a pre-sold unit with the construction\nloan in the name of the buyer.  We expect to have up to 8 spec loans to\nstart the project and expect all other loans to be pre-sold units with loans\nin the name of the builder/developer.  We do not expect to have any\nconstruction loans in the name of the buyers, as such loans are too\ndifficult to manage and please new buyers unfamiliar with the process.\n\nSpec loans will be for 70% to 75% of value and construction loans for\npre-sold units, if the construction loan is from the mortgage lender,  will\nbe from 80% to 95% of value.\n\nDISBURSEMENTS\nDisbursements will be handled by the General Partner to cover current and\nnear term third party costs, then to necessary reserves, then to priority\npayments and then to the partners per the agreement.  The General Partner\nwill contract with Creekside Builders, LLC to construct the units and the\nfee to CB will include a construction management and overhead fee equal to\n15% of the direct hard cost excluding land, financing and sales costs.\nThese fees are the only monies to Creekside, Larry Lewter or myself prior to\ncalculation of profit, except for a) direct reimbursement for partnership\nexpenses and b) direct payment to CB for any subcontractor costs that it has\nto perform.  For example, if CB cannot find a good trim carpenter sub, or\ncannot find enough trim carpenters, etc., and it decides to undertake this\nfunction, it will charge the partnership the same fee it was able to obtain\nfrom third parties and will disclose those cases to the partnership.\nFinally, CB will receive a fee for the use of any of its equipment if it is\nused in lieu of leasing equipment from others.  At present CB does not own\nany significant equipment, but it is considering the purchase of a sky track\nto facilitate and speed up framing, cornice, roofing and drywall spreading.\n\nREPORTING\nWe are more than willing to provide reports to track expenses vs. plan.\nWhat did you have in mind?  I would like to use some form of internet based\nreporting.\n\nBOOKKEEPING\nI am not sure what you are referring to by the question, "Bookkeeping\nprocedures to record actual expenses?"  Please expand.\n\nINVESTOR INPUT\nWe are glad to have the investor\'s input on design and materials.  As always\nthe question will be who has final say if there is disagreement, but in my\nexperience I have always been able to reach consensus. As you, and I presume\nKeith, want to be involved to learn as much as possible we would make every\neffort to be accommodating.\n\nCREEKSIDE PROCEEDURES\nCB procedures for dealing with subs, vendors and professionals is not as\nformal as your question indicates.  In the EXTREMELY tight labor market\nobtaining 3 bids for each labor trade is not feasible.  For the professional\nsubs we use those with whom we have developed a previous rapport.  Finally,\nfor vendors they are constantly shopped.\n\nPRE-SELECTED PROFESSIONALS, SUBS AND VENDORS\nYes there are many different subs that have been identified and I can\nprovide these if you are interested.\n\nI know I have not answered everything, but this is a starting point.  Call\nwhen you have reviewed and we can discuss further.\n\nSincerely,\n\nGeorge Richards\nPresident, Creekside Builders, LLC\n\n\n\n\n - winmail.dat'}
```



#### Ejemplos de uso



Teniendo todas las etapas del pipeline con sus correspondientes funciones que nos ayudarán a trabajar con los datos, podemos montar un pipeline completo donde integremos todas las etapas en un único flujo que nos proporcione un nuevo archivo de salida con los datos como queramos.

Para este pipeline, utilizaremos las mismas funciones ya definidas. Solo haremos una ligera modificación en la función de “parse_recipients” para incluir la función de normalización dentro de ella:



```python
def parse_recipients(field_data: str) -> list:
    """
    Toma el contenido de un campo 'To', 'Cc' o 'Bcc' (string)
    y retorna una lista de direcciones normalizadas.
    """
    if not field_data:
        return []
    candidatos = [x.strip() for x in field_data.split(',')]
    direcciones = [normalizar_direccion(c) for c in candidatos if normalizar_direccion(c)]
    return direcciones
### Pipeline completo
```



```python
## Pandas
import re
import email
import pandas as pd
from email.policy import compat32 as default_policy
from email.header import decode_header
from datetime import datetime
import kagglehub

path = kagglehub.dataset_download("wcukierski/enron-email-dataset")

print("Path to dataset files:", path)
base_path = path + "\emails.csv"

INPUT_CSV = base_path  # Ajustar a la ruta real
OUTPUT_PARQUET = "./enron_cleaned_pandas.parquet"

def pipeline():
    # 1. Cargar el CSV original (columnas: file, message)
    df_raw = pd.read_csv(INPUT_CSV, encoding='utf-8')
    print(f"CSV original cargado: {len(df_raw)} filas.")

    # 2. Parsear cada 'message' para extraer campos relevantes
    # Generamos una lista de diccionarios
    registros = []
    for idx, row in df_raw.iterrows():
        raw_msg = row['message']
        parsed = parse_raw_email(raw_msg)
        # Podemos añadir la info de 'file' si lo deseamos
        parsed['file'] = row['file']
        registros.append(parsed)

    # Convertimos a DataFrame
    df_emails = pd.DataFrame(registros)
    print(f"DataFrame parseado: {len(df_emails)} correos antes de limpieza.")

    # 3. Eliminación de duplicados
    # Definimos una clave única en base a (message_id, from, to_list)
    df_emails['unique_key'] = list(zip(
        df_emails['message_id'],
        df_emails['from'],
        [tuple(x) for x in df_emails['to_list']]
    ))
    df_emails.drop_duplicates(subset='unique_key', inplace=True)
    df_emails.drop(columns='unique_key', inplace=True)

    # 4. Parsear fecha (posible uso de pd.to_datetime con múltiples formatos)
    def parse_date(d):
        try:
            return pd.to_datetime(d)
        except:
            return pd.NaT

    df_emails['date'] = df_emails['date_str'].apply(parse_date)
    df_emails.drop(columns='date_str', inplace=True)

    # Filtramos correos sin remitente
    df_emails = df_emails[~df_emails['from'].isna()].reset_index(drop=True)

    print(f"Correos restantes tras limpieza: {len(df_emails)}")

    # 5. Guardar en formato parquet
    df_emails.to_parquet(OUTPUT_PARQUET, index=False)
    print(f"Archivo parquet generado: {OUTPUT_PARQUET}")

pipeline()
```



```python
## Polars
import re
import email
import pandas as pd
from email.policy import compat32 as default_policy
from email.header import decode_header
from datetime import datetime
import kagglehub

path = kagglehub.dataset_download("wcukierski/enron-email-dataset")

print("Path to dataset files:", path)
base_path = path + "\emails.csv"

INPUT_CSV = base_path  # Ajustar a la ruta real
OUTPUT_PARQUET = "./enron_cleaned_polars.parquet"

def pipeline_polars():
    # 1. Cargamos el CSV con Polars
    df_raw = pl.read_csv(INPUT_CSV, has_header=True)
    print(f"CSV original cargado: {df_raw.height} filas.")

    # 2. Parseamos cada fila, generando una lista de diccionarios
    registros = []
    for row in df_raw.iter_rows(named=True):
        raw_msg = row['message']
        parsed = parse_raw_email(raw_msg)
        # Podríamos añadir 'file' si deseamos
        parsed['file'] = row['file']
        registros.append(parsed)
    
    # 3. Convertimos la lista de dicts en DataFrame de Polars
    df_emails = pl.DataFrame(registros)
    print(f"DataFrame inicial: {df_emails.height} correos.")

    # 4. Eliminación de duplicados
    # Creamos una 'unique_key' en base a (message_id, from, to_list).
    # Convertimos to_list a str para poder agrupar
    df_emails = df_emails.with_columns(
        (pl.col("message_id") + "__" +
         pl.col("from").cast(pl.Utf8).fill_null("None") + "__" +
         pl.col("to_list").list.join(", ").fill_null("None")
        ).alias("unique_key")
    )
    df_emails = df_emails.unique(subset=["unique_key"])
    df_emails = df_emails.drop(["unique_key"])

    # 5. Parseo de fecha
    def try_parse_date(d):
        if not d:
            return None
        try:
            return datetime.strptime(d[:25], "%a, %d %b %Y %H:%M:%S")
        except:
            # Fallback
            try:
                return datetime.fromisoformat(d)
            except:
                return None
    
    df_emails = df_emails.with_columns(
        pl.col("date_str").map_elements(lambda d: try_parse_date(d), return_dtype = pl.Datetime).alias("date")
    ).drop(["date_str"])

    # Filtrar correos sin 'from'
    df_emails = df_emails.filter(pl.col("from").is_not_null())

    print(f"Tras limpieza, quedan {df_emails.height} correos.")

    # 6. Guardar en Parquet
    df_emails.write_parquet(OUTPUT_PARQUET_POLARS)
    print(f"Archivo parquet generado: {OUTPUT_PARQUET_POLARS}")

pipeline_polars()
```



Veamos en el video a continuación en detalle cada uno de los pasos y la diferencia de rendimiento entre Pandas y Polars:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651989_1/scormcontent/assets/INSD_BAIN_U5_Video1.mp4?v=1)



## 4. Librería Networkx



### 4.1 Introducción



![image](assets/cm8nolqv300vj356x8uezrd79-stock-image.jpg)



En esta sección, nos adentraremos en el uso de NetworkX, la librería de Python que se ha convertido en un estándar de facto para el análisis y manipulación de grafos en entornos académicos y profesionales. Hasta ahora, hemos preparado el terreno revisando la teoría de grafos y el análisis de redes, explorando el célebre Caso Enron y obteniendo un dataset limpio y estructurado listo para su uso en Python. Llegó el momento de dar el salto a la práctica con NetworkX para construir, manipular y, más adelante, analizar y visualizar nuestras redes de forma eficiente.

En este apartado, nos concentraremos en:

- Explicar qué es NetworkX y por qué resulta tan relevante en el análisis de redes sociales en Python.
- Instalar y configurar el entorno de trabajo.
- Crear, modificar y consultar grafos en NetworkX (añadiendo nodos, aristas y atributos).
- Leer y escribir grafos desde y hacia formatos estándar (y, en especial, desde los DataFrames que hemos preparado tras la limpieza del dataset Enron).

NetworkX se trata de un paquete de Python que está especializado en analizar y manipular grafos. Destaca por su flexibilidad, ya que no impone grandes restricciones sobre el tipo de redes que se pueden modelar:

- Permite trabajar con grafos dirigidos, no dirigidos e incluso multigrafos (donde pueden existir múltiples aristas entre el mismo par de nodos).
- Facilita el cálculo de métricas clásicas de la teoría de grafos (centralidades, clustering, PageRank, entre otras).
- Ofrece estructuras de datos internas muy completas: un “Graph”, un “DiGraph” (grafo dirigido) o un “MultiGraph”, cada uno optimizado para distintas necesidades.
- Dispone de métodos integrados para detección de comunidades, algoritmos de rutas más cortas, buscadores de isomorfismos y muchas otras funcionalidades.

El punto fuerte de NetworkX radica en su facilidad de uso y en la compatibilidad con el ecosistema de ciencia de datos en Python. Podemos unirlo sin problemas con Pandas, Polars o NumPy para manipular datos de gran tamaño, y con librerías de visualización como matplotlib o Plotly para generar diagramas de redes.

Para instalar la versión más reciente de NetworkX, normalmente basta con ejecutar:

pip install networkx

Es recomendable, además, contar con matplotlib u otra biblioteca de visualización si planemos representar grafos:

pip install matplotlib



### 4.2 Creación y manipulación de grafos



Uno de los objetivos de este apartado es comprender de manera práctica cómo construir grafos en NetworkX, cómo añadir nodos y aristas, y cómo manipular atributos. Este conocimiento es esencial para, posteriormente, calcular métricas y realizar análisis de comunidades.

La esencia de NetworkX se resume en la capacidad de definir y manipular grafos de manera muy directa. Sus clases principales son:

- **Graph:** Para redes no dirigidas.
- **DiGraph:** Para redes dirigidas.
- **MultiGraph:** Para redes no dirigidas con posibilidad de múltiples aristas entre el mismo par de nodos.
- **MultiDiGraph:** Variante dirigida del anterior.

En el caso Enron (y en muchos análisis de redes sociales), solemos usar DiGraph porque nos interesa distinguir la dirección de cada interacción (por ejemplo, un correo va de un remitente a un destinatario). Sin embargo, si tu análisis no necesita direccionalidad, podrías optar por un Graph.

Para crear un grafo vacío y añadirle nodos y aristas manualmente, deberemos utilizar los métodos .add_node() y .add_edge() de la librería:



```python
import networkx as nx

# Creamos un grafo dirigido
G = nx.DiGraph()

# Añadimos nodos de forma individual
G.add_node("alice")
G.add_node("bob")

# O en lote
G.add_nodes_from(["carol", "david"])

# Añadimos aristas
G.add_edge("alice", "bob")  # alice -> bob
G.add_edge("carol", "david")
G.add_edge("alice", "carol")

# Imprimimos información
print("Nodos:", G.nodes())
print("Aristas:", G.edges())
# Output
Nodos: ['alice', 'bob', 'carol', 'david']
Aristas: [('alice', 'bob'), ('alice', 'carol'), ('carol', 'david')]
```



En la práctica, cuando se trabaja con miles o cientos de miles de interacciones (como en Enron), se preferirá crear el grafo desde datos almacenados en un DataFrame (pandas o Polars), en ficheros CSV, o incluso en bases de datos.

Si utilizamos, del apartado anterior, tras el pipeline de limpieza, poseemos un archivo parquet (o un DataFrame directo en memoria) con columnas como:

- message_id
- from (remitente)
- to_list (lista de destinatarios)
- date (fecha del correo)
- subject, etc.

Para construir un DiGraph a partir de estos datos:



```python
import networkx as nx
import pandas as pd
import numpy as np

def construir_grafo_enron(df_emails):
    """
    Recibe un DataFrame (pandas) con columnas 'from' y 'to_list'.
    Devuelve un DiGraph de NetworkX donde cada arista representa el envío de un correo.
    
    Args:
        df_emails (pd.DataFrame): DataFrame con columnas 'from' y 'to_list'
        
    Returns:
        nx.DiGraph: Grafo dirigido donde los nodos son direcciones de correo y las aristas representan envíos
    """
    G = nx.DiGraph()
    
    for idx, row in df_emails.iterrows():
        remitente = row['from']
        to_list = row['to_list']
        
        # Skip if sender is missing
        if pd.isna(remitente):
            continue
            
        # Handle numpy array
        if isinstance(to_list, np.ndarray):
            # Add edges for each recipient
            for dest in to_list:
                if pd.notna(dest):
                    G.add_edge(remitente, dest)
                    
    return G

df_enron = pd.read_parquet("enron_cleaned_pandas.parquet")
grafo_enron = construir_grafo_enron(df_enron)
print("\nNetwork Statistics:")
print("Nodos en el grafo:", grafo_enron.number_of_nodes())
print("Aristas en el grafo:", grafo_enron.number_of_edges())
# Output
Network Statistics:
Nodos en el grafo: 78842
Aristas en el grafo: 310717
```



### 4.3 Operaciones fundamentales en NetworkX



Una vez tenemos nuestro grafo, NetworkX ofrece numerosas operaciones que permiten agregar, consultar y eliminar nodos o aristas, así como acceder a la información de atributos de cada elemento.



#### Atributos en nodos y aristas



En muchas ocasiones, querremos asociar información extra a cada nodo (por ejemplo, el departamento del empleado, su rol, etc.) o a cada arista (la fecha del correo, el asunto, un ID de mensaje, etc.). NetworkX permite esto mediante diccionarios de atributos.

- Atributos en nodos:



```python
# Siendo G el grafo creado en el apartado anterior
G.add_node("alice", department="Finance", role="Manager")
print(G.nodes["alice"]["department"])
# Output
{'department': 'Finance', 'role': 'Manager'}
```



- Atributos en aristas:



```ruby
G.add_edge("alice", "bob", subject="Meeting Reminder", date="2025-01-05")
print(G["alice"]["bob"]["subject"])
# Output
{'subject': 'Meeting Reminder', 'date': '2025-01-05'}
```



Para el Caso Enron, puede ser interesante añadir la fecha o incluso el message_id como atributo de la arista. Sin embargo, hay que tener presente que, si trabajamos con un volumen muy grande de correos (centenares de miles), el almacenamiento de muchos atributos puede impactar la memoria. Una alternativa es desduplicar y representar las relaciones de forma más agregada (por ejemplo, en lugar de tener una arista por cada correo, sumar un “peso” que sea el conteo de correos de remitente a destinatario).



#### Consultas



También podemos realizar operaciones para conocer detalles de nuestro grafo, por ejemplo, tener el numero de nodos, nodos vecinos, etc:

- Listar nodos y aristas:



```python
print("Nodos:", list(G.nodes()))
print("Aristas:", list(G.edges()))
# Output
Nodos: ['alice', 'bob', 'carol', 'david']
Aristas: [('alice', 'bob'), ('alice', 'carol'), ('carol', 'david')]
```



- Contar nodos y aristas:



```bat
print("Total de nodos:", G.number_of_nodes())
print("Total de aristas:", G.number_of_edges())
# Output
Total de nodos: 4
Total de aristas: 3
```



- Identificar camino entre dos nodos



```python
from networkx import has_path
if has_path(G, "alice", "david"):
    print("Existe un camino desde alice hasta david.")
# Output
Existe un camino desde alice hasta david.
```



- Nodos vecinos



```groovy
print("Vecinos salientes de alice:", list(G.successors("alice")))
print("Vecinos entrantes de bob:", list(G.predecessors("bob")))
# Output
Vecinos salientes de alice: ['bob', 'carol']
Vecinos entrantes de bob: ['alice']
```



#### Lectura y escritura



Si en algún momento deseamos guardar nuestro grafo de NetworkX en un formato estándar (por ejemplo, GraphML, GEXF, GML), NetworkX ofrece métodos nativos para ello:



```r
# Guardar en GEXF (habitual para gephi)
nx.write_gexf(grafo_enron, "enron_network.gexf")

# Leer un grafo GEXF
grafo_leido = nx.read_gexf("enron_network.gexf")
```



Esto es útil si planeas utilizar herramientas externas de visualización, como Gephi.



### 4.4 Enlaces de interés



> Documentación oficial NetworkX
>
> [Link](https://networkx.org/documentation/stable/)

> Github oficial NetworkX
>
> [Link](https://github.com/networkx/networkx)



## 5. Análisis De Métricas De Red Con Networkx



### 5.1 Introducción



![image](assets/cm8np0p4y01ii356x3unxjcog-stock-image.jpg)



En las secciones anteriores, hemos entendido los fundamentos teóricos del Análisis de Redes Sociales (SNA), hemos explorado el caso Enron y hemos aprendido a limpiar y normalizar sus correos, terminando con la creación de un grafo en NetworkX que representa la comunicación entre empleados. Ahora, en este apartado, damos el siguiente paso lógico: analizar la red a través de métricas que nos permitan identificar la importancia de cada nodo, entender la estructura global de la red y localizar patrones relevantes.

En el contexto de Enron, estas métricas pueden arrojar luz sobre cuestiones tan esenciales como:

- ¿Quiénes eran los empleados con un rol central en la comunicación?
- ¿Qué nodos actuaban como puentes entre distintos departamentos?
- ¿Se distinguen usuarios con alto poder de diseminación de información?

Los resultados no solo tienen valor histórico o forense (en el caso Enron), sino que ilustran el potencial del SNA para distintas aplicaciones empresariales, académicas o tecnológicas. A continuación, revisaremos las métricas de red más destacadas, describiremos sus implicaciones y mostraremos cómo se calculan en NetworkX, poniendo siempre como ejemplo el grafo de Enron que hemos venido construyendo.

Cuando representamos un sistema como un grafo —donde los nodos simbolizan entidades (personas, cuentas de correo, repositorios de software, etc.) y las aristas representan relaciones o comunicaciones—, necesitamos cuantificar de forma objetiva la relevancia de cada elemento en la red. Las métricas de red, o medidas de centralidad, cumplen precisamente esa función: proporcionan valores numéricos que reflejan la posición estructural de un nodo o la cohesión global de la red.

En la práctica, las métricas de red sirven para:

- Identificar líderes de opinión o nodos clave: en el caso de Twitter, sería descubrir quiénes son los “influencers” más influyentes; en una empresa, quiénes concentran la mayor comunicación o actúan como referentes técnicos o directivos.
- Localizar “puentes” entre comunidades: esto resulta crucial cuando se busca optimizar la colaboración interdepartamental o detectar vulnerabilidades donde un solo nodo puede aislar a toda una subcomunidad si deja de funcionar.
- Predecir la propagación de información: un nodo con alta importancia en ciertas métricas puede ser un buen difusor de noticias internas, alertas de seguridad o innovaciones tecnológicas.

En el conjunto de correos de Enron, se han realizado numerosos estudios que muestran cómo ciertos ejecutivos tenían una posición de poder no solo formal, sino también reflejada en el flujo de información, mientras que otros empleados, sin rango directivo, resultaban ser puentes de comunicación muy relevantes.



### 5.2 Métricas de grado



La métrica de grado es la más elemental en teoría de grafos, pero no por ello deja de ser sumamente útil en un primer acercamiento. En una red dirigida, distinguimos:



- **Grado de salida (out-degree)**  
  Número de aristas que salen de un nodo (en el caso Enron, cuántos correos envió una persona).
- **Grado de entrada (in-degree)**  
  Número de aristas que llegan a un nodo (en Enron, cuántos correos recibió una persona).



Además, podemos hablar de degree centrality en su forma normalizada, que en un grafo de 𝑛 nodos toma valores entre 0 y 1, siendo la fracción de nodos a los que un nodo está conectado (para out-degree en un grafo dirigido) o de los que recibe conexiones (para in-degree).

En el caso Enron podemos interpretarlas como:



- **Mayor in-degree**  
  Empleados que más correos han recibido. Podrían ser asistencias ejecutivas, directivos que reciben reportes, cuentas de distribución, etc
- **Mayor out-degree**  
  Empleados que más correos envían, a menudo figuras que gestionan la información y la reparten (jefes de proyecto, secretarías, responsables de comunicación interna).



No siempre la persona con mayor out-degree es la de mayor poder, ya que podría tratarse de alguien que envía correos masivos con boletines. Por ello, solemos combinar esta métrica con otras que veremos más adelante.

Utilizando el grafo de Enron construido en el apartado anterior sobre la creación y manipulación de grafos, podemos calcular estas métricas mediante:



```python
# Grado de salida (out-degree) para cada nodo
out_degs = dict(grafo_enron.out_degree())
# Grado de entrada (in-degree) para cada nodo
in_degs = dict(grafo_enron.in_degree())

# Degree centrality (normalizada en [0..1])
out_degree_centrality = nx.out_degree_centrality(grafo_enron)
in_degree_centrality = nx.in_degree_centrality(grafo_enron)

# Ejemplo: mostrar los 10 nodos con mayor out-degree centrality
top10_out = sorted(out_degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 (out-degree centrality):", top10_out)
# Output
Top 10 (out-degree centrality): [('outlook.team@enron.com', 0.01986276176101267), ('david.forster@enron.com', 0.017693839499752666), ('sally.beck@enron.com', 0.015854694892251494), ('technology.enron@enron.com', 0.01582932738042389), ('kenneth.lay@enron.com', 0.013355994977232657), ('jeff.dasovich@enron.com', 0.012290559480473357), ('tracey.kozadinos@enron.com', 0.011669055440697098), ('julie.clyatt@enron.com', 0.011123653936403648), ('bodyshop@enron.com', 0.011009500133179436), ('lee.wright@enron.com', 0.010679722479420605)]
```



Así pues, Podemos ver que el primer nodo que más correos envía es un email genérico de “[outlook.team](http://outlook.team)” y puede que no sea relevante para nuestro análisis. Sin embargo, vemos que le sigue David Forster quien fue vicepresidente de Enron.



### 5.3 Centralidad de intermediación (Betweenness Centrality)



La centralidad de intermediación, también conocida como betweenness, mide hasta qué punto un nodo se sitúa en los caminos más cortos entre otros pares de nodos de la red. Su definición formal surge de la idea de que, si un nodo se repite con mucha frecuencia en las rutas más eficientes que conectan a otros, entonces actúa como un puente o broker de información.

En el entorno Enron, un empleado con alta centralidad de intermediación podría ser un colaborador transversal que mantiene la comunicación fluida entre diferentes departamentos o niveles jerárquicos. A veces, estos nodos no son directivos, sino figuras administrativas o de soporte que, sin su presencia, se fragmentaría buena parte de la red.

La relevancia práctica radica en que estos usuarios pueden convertirse en “cuellos de botella” o, al contrario, ser “puntos de control” donde la información se filtra y se direcciona. Desde el punto de vista de la ciberseguridad, son lugares sensibles para la vigilancia o el control de la comunicación; desde un enfoque organizativo, podrían ser nodos que, de no estar, romperían la fluidez de la colaboración.

NetworkX proporciona una función betweenness_centrality que, por defecto, asume un grafo no ponderado. En redes de tamaño medio (como la de Enron, con decenas de miles de nodos), el cálculo de betweenness puede ser pesado computacionalmente. Existen versiones aproximadas que permiten acelerar el proceso, como nx.betweenness_centrality_subset o el uso de muestras.



```python
import networkx as nx

bet_centr = nx.betweenness_centrality(grafo_enron, k=20, normalized=True)
# k=None implica que considera todos los pares de nodos, lo cual es costoso.

# Podemos ordenar para obtener los10 con mayor intermediación
top10_bet = sorted(bet_centr.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 (betweenness centrality):", top10_bet)
# Output
Top 10 (betweenness centrality): [('mark.e.haedicke@enron.com', 0.032038711794762344), ('doug.gilbert-smith@enron.com', 0.026769494940790794), ('margaret.doucette@enron.com', 0.01907972980087021), ('deb.korkmas@enron.com', 0.014920610447498338), ('teb.lokey@enron.com', 0.0104071107100723), ('jeff.dasovich@enron.com', 0.008448749429160305), ('julia.murray@enron.com', 0.008008958207963199), ('edie.leschber@enron.com', 0.007768526275053675), ('shelley.corman@enron.com', 0.006908728795699572), ('gerald.nemec@enron.com', 0.005649111214883276)]
```



En el caso Enron, es habitual encontrar cuentas de perfil administrativo con un betweenness centrality elevado. Un estudio detallado en su momento mostró que ciertos asistentes de altos directivos poseían más poder de intermediación que algunos mandos medios.

En este caso podemos observar que Mark E. Haedicke es un nodo por el que deben de pasar muchas comunicaciones para llegar a otro punto del grafo.



### 5.4 Centralidad de cercanía (Closeness Centrality)



La centralidad de cercanía indica qué tan cerca está un nodo, en promedio, del resto de los nodos, considerando las rutas más cortas. Cuanto menor sea la distancia promedio de un nodo hacia todos los demás, mayor será su closeness centrality.

En una red dirigida, a menudo diferenciamos closeness saliente (distancia para llegar desde un nodo a los demás) y closeness entrante (distancia para llegar a un nodo desde los demás), aunque en muchos casos se aplica la versión genérica que ignora la dirección.

Los nodos con alta centralidad de cercanía en Enron podrían ser aquellos que, a muy pocos “saltos” de correo, pueden alcanzar a la mayoría de la empresa. Esto refleja un potencial de difusión de información elevado. Por ejemplo, si “X” tiene closeness alto, significa que “X” puede hacer llegar cualquier noticia o aviso a la mayoría de los empleados con pocas iteraciones de reenvío.

NetworkX ofrece nx.closeness_centrality. El resultado se normaliza a menudo por el tamaño de la componente conectada. Para grafos dirigidos, es común transformarlos en no dirigidos si uno desea la noción tradicional de cercanía. De lo contrario, conviene leer la documentación para elegir la variante apropiada:



```ini
closeness_dict = nx.closeness_centrality(grafo_enron.to_undirected())

top10_closeness = sorted(closeness_dict.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 (closeness centrality, sin dirección):", top10_closeness)
```



Si la red no es completamente conexa (lo cual es muy factible en Enron, donde hay nodos sin muchas conexiones), la definición de cercanía puede sufrir matices. NetworkX maneja esto asignando 0 a nodos que están en componentes aisladas, salvo que se especifique un método de cálculo diferente.

En el video a continuación veremos un ejemplo de cómo identificar cada una de estas métricas y qué nodos tendrán un mayor valor:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651989_1/scormcontent/assets/INSD_BAIN_U5_Video2.mp4?v=1)



### 5.5 Centralidad de autovector (Eigenvector Centrality) y PageRank



Eigenvector Centrality y PageRank son métricas avanzadas que, más allá de contar simplemente el número de conexiones, ponderan la importancia de quién te conecta. En cierto modo, un nodo es importante si está conectado con nodos importantes. Esto es especialmente relevante en redes como la web (de ahí surgió el PageRank) o en redes sociales donde no todos los enlaces tienen el mismo “peso reputacional”.

La idea central es resolver un problema de autovectores en la matriz de adyacencia del grafo. Un nodo con alta puntuación en eigenvector centrality suele estar conectado a otros nodos que, a su vez, tienen alta puntuación. En un escenario corporativo, esto puede significar que un empleado interactúa con ejecutivos y figuras centrales, reforzando así su propia posición.



```ini
ev_centrality = nx.eigenvector_centrality(grafo_enron.to_undirected(), max_iter=1000)
top10_ev = sorted(ev_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 (Eigenvector Centrality):", top10_ev)
```



Hay que destacar que, en redes grandes y dispersas, a veces la eigenvector centrality no converge fácilmente, o se converge a una solución que no siempre es interpretada del todo bien si hay componentes desconectados.

El PageRank se popularizó con Google como un método para medir la importancia de páginas web. En el caso de un grafo dirigido, su uso es muy natural. Un nodo con un PageRank alto recibe muchos enlaces (o correos, en este caso), especialmente de nodos que, a su vez, tienen PageRank alto. Además, el PageRank introduce un factor de “aleatoriedad” (el “damping factor”) que simula la navegación al azar de un usuario por la red.

En un dataset como Enron, PageRank puede resaltar usuarios que no solo reciben muchos correos, sino que reciben correspondencia de nodos influyentes (otros con alto PageRank). Es decir, si “A” recibe muchos correos de “B”, y “B” está considerado un nodo relevante, “A” hereda parte de esa relevancia.



```ini
pagerank_dict = nx.pagerank(grafo_enron, alpha=0.85)
top10_pr = sorted(pagerank_dict.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top 10 (PageRank):", top10_pr)
```



El parámetro alpha (o “damping factor”) suele fijarse alrededor de 0.85 o 0.9. Una persona con alto PageRank en Enron no siempre será quien más correos envía, pero sí quien recibe desde nodos que, a su vez, tienen relevancia. Es una medida que, en un grafo corporativo, combina popularidad con reconocimiento por parte de otros nodos importantes.



![image](assets/cm8npc9x001xg356xx98mll8d-Imagen38.jpg)



### 5.6 Caso de uso



1. En redes de dimensión mediana, como puede llegar a ser la red de Enron con miles o decenas de miles de nodos, el cálculo de métricas como la centralidad de grado o el PageRank suele ser bastante rápido. Sin embargo, la betweenness centrality puede volverse costosa, pues en su definición exacta se realiza un recuento de caminos cortos para todos los pares de nodos.

   Para lidiar con este desafío, se han desarrollado técnicas de muestreo o algoritmos aproximados que reducen el coste computacional. Por ejemplo, nx.betweenness_centrality soporta un argumento k que especifica un subconjunto de nodos de muestra, reduciendo el número de rutas calculadas.
2. En proyectos reales, conviene:

   - **Verificar la conectividad de la red.** Si hay subgrafos desconectados, algunas métricas (closeness, eigenvector) pueden arrojar resultados poco interpretables.
   - **Definir si se usarán pesos en las aristas.** Para Enron, no es lo mismo un único correo que un hilo con decenas de respuestas. Podríamos agrupar o asignar pesos en la arista (A, B) según la frecuencia de correos de “A” a “B”.
   - **Analizar la escala.** Aun con la complejidad de Enron, la red puede no ser tan grande como para imposibilitar un cálculo exacto, pero el tiempo de ejecución puede ser de minutos o horas, según el hardware.
3. Una de las motivaciones al analizar el Caso Enron con métricas de red es comprobar cómo, más allá de los ejecutivos principales, surgieron figuras con un papel de liderazgo comunicativo o de intermediación que no era obvio en el organigrama oficial. Ejemplos hipotéticos:

   - **Nodos con alto out-degree:** podrían ser secretarias, jefes de departamento u oficinas que gestionaban el envío de comunicados internos.
   - **Nodos con alto betweenness:** empleados que resultaron puentes críticos entre distintos departamentos financieros y legales, lo cual fue clave para las investigaciones sobre prácticas contables irregulares.
   - **Nodos con PageRank alto:** figuras que reciben correos desde múltiples puntos influyentes, lo que indica una posición de prestigio o de referencia interna.

   Estos hallazgos conducen a interpretaciones sobre la estructura informal de la empresa y acerca de cómo la información fluía realmente, al margen de jerarquías escritas.



Con todo esto, podemos enriquecer nuestro pipeline ya desarrollado con la obtención de métricas. Veamos cómo funciona en el siguiente video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651989_1/scormcontent/assets/INSD_BAIN_U5_Video3.mp4?v=1)



## 6. Análisis De Comunidades Con Networkx O Community



### 6.1 Introducción



![image](assets/cm8nph711022u356xb8hom8u6-stock-image.jpg)



En el análisis de redes sociales, no solo es relevante identificar a los nodos más influyentes o con mayor centralidad (como vimos en el apartado anterior), sino también descubrir estructuras de agrupamiento o subredes dentro de la red global. A menudo, en las grandes redes surgen “comunidades” que concentran un número elevado de interacciones internas y un número reducido de vínculos con otros grupos. En el Caso Enron, resulta muy útil determinar cuáles departamentos, equipos de trabajo o grupos informales formaban “casi una isla” de comunicación, y hasta qué punto existían puentes que unían dichas islas.

En este apartado, abordaremos las técnicas de detección de comunidades (o community detection) con Python, apoyándonos en NetworkX y en librerías complementarias como python-louvain (a menudo referida sencillamente como community). Veremos, en detalle, la justificación teórica de la detección de comunidades, la interpretación práctica de los resultados y, por supuesto, la implementación técnica con el dataset de Enron como ejemplo de uso.

Una comunidad (o cluster) en una red social es un conjunto de nodos que se caracterizan por estar más densamente conectados entre sí que con el resto de la red. Dicho de otro modo, dentro de una comunidad, cada nodo tiende a vincularse con mayor frecuencia a otros miembros del grupo que a nodos externos.

Por ejemplo, en una empresa, los nodos de un mismo departamento interactúan más entre sí (reuniones, correos, proyectos comunes) que con colegas de otras áreas. Sin embargo, en ocasiones emergen comunidades transversales basadas en intereses, proyectos temporales o relaciones informales.

Desde el punto de vista del Análisis de Redes Sociales, detectar estas comunidades puede dar lugar a conocimientos valiosos:

- **Organización interna:**¿coincide la estructura de la comunidad con el organigrama oficial? ¿Existen subgrupos no oficiales que podrían impulsar la innovación o, en su defecto, aislar información?
- **Diseño de estrategias:** ubicar a los “puentes” entre comunidades, facilitando la comunicación interdepartamental, o reforzando la seguridad en caso de que un grupo sea muy cerrado.
- **Segmentación:** en redes de marketing o de usuarios finales, las comunidades pueden asociarse a segmentos de clientes o audiencias con intereses similares.

En el Caso Enron, se ha estudiado cómo algunos correos y nodos resultaban aislados por la estructura informal de la compañía y cómo eso contribuyó a la falta de transparencia. De igual manera, se ha visto que ciertos departamentos estaban muy cohesionados, mientras que otros resultaban dispersos, apoyando las hipótesis de una gerencia poco integrada.



### 6.2 Métodos para la detección de comunidades



Existen múltiples algoritmos que abordan la detección de comunidades en grafos. Entre los más populares destacan:



- **Girvan–Newman**  
  Se basa en la idea de eliminar aristas con alta intermediación (betweenness) de manera iterativa, esperando que, al quitar las “puentes” principales, la red se divida progresivamente en grupos. Este método es muy ilustrativo, pero tiende a ser costoso para redes grandes.
- **Louvain**  
  Propone un método jerárquico y heurístico para maximizar la modularidad. Inicialmente, cada nodo se considera una comunidad en sí misma y, poco a poco, se agrupan nodos (o comunidades intermedias) que mejoran la modularidad global. Louvain se considera uno de los métodos de referencia por su rapidez y buena calidad de agrupamiento en redes de tamaño grande o mediano.
- **Leiden (evolución de Louvain)**  
  Mejora algunos aspectos de Louvain para evitar “artifacts” y refinar la partición. Es un método cada vez más adoptado en entornos académicos.
- **Algoritmos basados en propagación de rótulos (label propagation)**  
  Extienden la idea de que los nodos van adoptando la etiqueta (o comunidad) de la mayoría de sus vecinos, hasta converger a un estado estable.



Para la mayoría de los análisis de SNA en la industria o en la investigación, Louvain es el método preferido, especialmente cuando queremos un equilibrio entre velocidad y calidad de la partición. Girvan–Newman, si bien es un clásico, puede resultar impráctico en redes muy grandes como la de Enron (miles de nodos y aristas).



### 6.3 Implementación con NetworkX



En Python, NetworkX ofrece algunos algoritmos de detección de comunidades integrados. Por ejemplo, nx.community.louvain_communities, un método que directamente aplica el algoritmo de Louvain para redes no dirigidas (o tratadas como no dirigidas). Esto evita la necesidad de instalar librerías externas como python-louvain.



#### Louvain



Continuando con nuestro grafo de Enron, que se halla en la variable grafo_enron, un DiGraph. El método Louvain, por definición, trabaja con grafos no dirigidos, de modo que, si queremos ignorar la dirección de las aristas, deberemos convertir el grafo:



```python
import networkx as nx
from networkx.algorithms import community

# Convertimos a grafo no dirigido
G_undirected = grafo_enron.to_undirected()

# Aplicamos Louvain, asumiendo un grafo sin pesos
communities_louvain = community.louvain_communities(G_undirected, weight=None, resolution=1.0, seed=None)

# 'communities_louvain' es una lista de conjuntos (cada conjunto = comunidad)
print(f"Número de comunidades detectadas: {len(communities_louvain)}")
print(f"Comunidades (primeras 3): {list(communities_louvain)[:3]}")
# Output
Número de comunidades detectadas: 1498
Comunidades (primeras 3): [{'distribution@pira.com', 'sande@pira.com', 'vwatkins@pira.com', 'eileen@pira.com', 'cathy@pira.com', 'rich@pira.com', 'glenn@pira.com', 'greg@pira.com'}, {'tina.barroso@wdr.com', 'mlbarroso@tmh.tmc.edu', 'lbarroso@civilmail.tamu.edu', 'lburns@hotmail.com', 'jrlewis@airmail.net', 'daphne_roque@mhhs.org', 'fun972@prodigy.net', 'maceciv@hotmail.com', 'lbarroso@ism.com.br', 'nhobsons@aol.com', 'tina.barroso@ibm.net', 'nmclemor@houstonisd.org', 'hegnatuk@hotmail.com', 'margot@iis.com.br', 'derrick183@aol.com', 'klinsu@hotmail.com', 'twinliz@aol.com', 'barbara.latham@pdq.net', 'paula_barroso@uol.com.br', 'hm4183@sbc.com', 'krobbins@houston.org', 'joaogodoy@hotmail.com', 'jnjtrout94@aol.com', 'fbarroso@ism.com.br', 'lmgodoy@escelsa.com.br', 'mlbarroso@aol.com', 'kblasing@flash.net', 'breytspraak@yahoo.com', 'lzapalacpr@aol.com', 'lisabrown@andrews-kurth.com', 'abs182@psu.edu', 'sandweg_steve@emc.com', 'barroso@pa.dec.com', 'kconat@chmc.org', 'paula.barroso@br.abnamro.com', 'rbsandweg@houston.rr.com', 'abarroso@bcm.tmc.edu', 'cbarroso@arches.uga.edu'}, {'market_alert@listserv.dowjones.com', 'market-reply@listserv.dowjones.com'}]
```



Con este método, communities_louvain nos dará todos los nodos de cada comunidad, por ejemplo, la primera comunidad estará compuesta de: {'[distribution@pira.com](mailto:distribution@pira.com)', '[sande@pira.com](mailto:sande@pira.com)', '[vwatkins@pira.com](mailto:vwatkins@pira.com)', '[eileen@pira.com](mailto:eileen@pira.com)', '[cathy@pira.com](mailto:cathy@pira.com)', '[rich@pira.com](mailto:rich@pira.com)', '[glenn@pira.com](mailto:glenn@pira.com)', '[greg@pira.com](mailto:greg@pira.com)'}. Cabe destacar que el algoritmo no proporciona siempre el mismo número de comunidades, por lo que entre ejecuciones podemos tener diferentes valores.

Para medir la calidad de esa partición, podemos usar community.modularity:



```ini
mod = community.modularity(G_undirected, communities_louvain, weight=None)
print(f"Modularidad de la partición (Louvain): {mod:.4f}")
# Output
Modularidad de la partición (Louvain): 0.6548
```



Valores relativamente altos (por ejemplo, por encima de 0.3 o 0.4) sugieren que la red está organizada en comunidades bien definidas.



#### Girvan–Newman



El algoritmo Girvan–Newman parte del cálculo de la intermediación de aristas (edge betweenness) y va eliminando las que tienen mayor valor, separando gradualmente el grafo en múltiples subcomponentes. NetworkX ofrece un generador que, en cada iteración, produce una partición con un número creciente de comunidades:



```python
gn_generator = community.girvan_newman(G_undirected)

# La primera partición (cuando se elimina la primera arista de mayor betweenness)
first_partition = next(gn_generator)
print("Partición con 2 comunidades:", [list(c) for c in first_partition])

# La segunda partición (cuando se ha eliminado la siguiente arista de mayor betweenness)
second_partition = next(gn_generator)
print("Partición con 3 comunidades:", [list(c) for c in second_partition])
```



Sin embargo, el algoritmo de Girvan-Newman es muy caro computacionalmente, puedo tardar horas en el caso Enron. Esto se debe a que recalcula el edge betweenness tras cada eliminación de arista. Para optimizarlo es recomendable trabajar con subsets o limitar el número de iteraciones, por ejemplo, si solo queremos obtener las dos primeras comunidades.

Veamos como sería con un subset:



```python
import networkx as nx
from networkx.algorithms import community

# Convertimos a grafo no dirigido
G_undirected = grafo_enron.to_undirected()

# Seleccionamos los primeros 500 nodos
nodes_subset = list(G_undirected.nodes())[:500]
G_subset = G_undirected.subgraph(nodes_subset).copy()

gn_generator = community.girvan_newman(G_subset)

# La primera partición con 2 comunidades
first_partition = next(gn_generator)
print("Partition with 2 communities:", [list(c) for c in first_partition])

# La primera partición con 3 comunidades
second_partition = next(gn_generator)
print("Partition with 3 communities:", [list(c) for c in second_partition])
# Output
Partition with 2 communities: [['suzanne.nicholie@enron.com', 'jay.reitmeyer@enron.com', 'karen.buckley@enron.com', 'matt.smith@enron.com', 'savita.puthigai@enron.com', 'c@enron.com', 'barry.tycholiz@enron.com', 'daniel.quezada@enron.com', 'mery.l.brown@accenture.com', 'credit .williams@enron.com', 'reagan.rorschach@enron.com', 'mark.dobler@enron.com', 'colleen.sullivan@enron.com' ….
```



En la práctica, se pueden generar múltiples particiones y evaluar cada una con community.modularity para seleccionar aquella con la mayor modularidad. Sin embargo, en redes de tamaño mediano o grande, Girvan–Newman se torna computacionalmente caro, por lo que Louvain suele preferirse en entornos productivos.

Este ejemplo demuestra el aspecto iterativo de Girvan–Newman. A medida que se van eliminando aristas con alta betweenness, el grafo se fragmenta en más comunidades. Se puede obtener la partición final o la partición que maximiza la modularidad.



```r
best_modularity = -1
best_partition = None
for idx, partition_gn in enumerate(community.girvan_newman(G_subset)):
    partition_list = list(partition_gn)  # tuple of sets
    mod_gn = community.modularity(G_subset, partition_list)
    print(f"Iteración {idx+1} -> {len(partition_list)} comunidades, modularidad = {mod_gn:.4f}")
    if mod_gn > best_modularity:
        best_modularity = mod_gn
        best_partition = partition_list
    else:
        # A veces se rompe el bucle cuando la modularidad empieza a bajar
        break

print(f"Mejor modularidad con {len(best_partition)} comunidades: {best_modularity:.4f}")
# Output
Iteración 1 -> 7 comunidades, modularidad = 0.0073
Iteración 2 -> 8 comunidades, modularidad = 0.0081
Iteración 3 -> 9 comunidades, modularidad = 0.0122
Iteración 4 -> 10 comunidades, modularidad = 0.0138
Iteración 5 -> 11 comunidades, modularidad = 0.0435
Iteración 6 -> 12 comunidades, modularidad = 0.0435
Mejor modularidad con 11 comunidades: 0.0435
```



### 6.4 Interpretación de uso



Tras aplicar Louvain o Girvan–Newman, obtendremos varios subconjuntos de nodos. Cada subconjunto podría corresponder, por ejemplo, a un departamento de la empresa o a un proyecto transversal. Al examinar los correos de la comunidad (o la metadata, como roles y puestos), es frecuente hallar:

- **Correspondencia con la estructura formal:** nodos de “contabilidad” muy concentrados en el mismo subconjunto, “trading” en otro, etc.
- **Comunidades mixtas:** empleados de áreas diferentes, pero con una interacción muy densa en torno a un proyecto determinado.
- **Nodos puente** que, si calculamos métricas como la betweenness, resultan vitales para la cohesión global. Estos nodos pueden pertenecer a comunidades distintas en diferentes pasos del algoritmo, según la configuración.

Dicho análisis puede verificar, por ejemplo, si la falta de comunicación entre dos departamentos fue un factor que propició la falta de supervisión en ciertas prácticas contables, o si ciertas subcomunidades con altos directivos intercambiaban correos reservados sin involucrar a otros nodos.

Como en todo análisis de SNA, visualizar las comunidades suele ser de gran ayuda. NetworkX y matplotlib permiten colorear los nodos según su comunidad. Veamos como funciona en el próximo video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651989_1/scormcontent/assets/INSD_BAIN_U5_Video4.mp4?v=1)



### 6.5 Enlaces de interés



> Algoritmos disponibles para community en NetworkX
>
> [Link](https://networkx.org/documentation/stable/reference/algorithms/community.html)

> SNA del caso Enron
>
> [Link](https://www.researchgate.net/publication/221598998_Social_Network_Analysis_and_Organizational_Disintegration_The_Case_of_Enron_Corporation)



## 7. Visualización De Redes: Gephi Y Matplotlib



### 7.1 Introducción



![image](assets/cm8npvi6s02js356xmoe5e94z-stock-image.jpg)



En el análisis de redes sociales, la visualización cumple un papel esencial a la hora de interpretar y comunicar los hallazgos. Hasta ahora, en los apartados anteriores, hemos aprendido a crear y manipular grafos con NetworkX, calcular métricas (grado, centralidades, PageRank...) y detectar comunidades (Louvain, Girvan–Newman). Sin embargo, ver la red “en acción” a menudo aporta una claridad que los listados de nodos y métricas numéricas no pueden lograr por sí solos.

En este apartado, profundizaremos en dos enfoques complementarios para la visualización de redes:

- matplotlib, la librería estándar de Python para gráficos, que junto con las funciones de dibujo de NetworkX permite producir diagramas de red de forma relativamente directa.
- gephi, una herramienta especializada en la exploración visual de grafos, más potente e interactiva que matplotlib, y muy utilizada tanto en entornos académicos como profesionales.

Emplearemos la red de Enron que hemos venido analizando, con un especial interés en mostrar de manera gráfica las comunidades detectadas o los nodos más relevantes según las métricas estudiadas.

La visualización de una red permite, entre otras cosas:

- Identificar patrones de conexión: es mucho más fácil reconocer subgrupos, “estrellas” o nodos fuertemente conectados cuando se observan en un diagrama.
- Resaltar anomalías: nodos aislados, puentes que conectan dos grandes “bloques” de la red, etc.
- Comunicar hallazgos de forma clara y persuasiva a públicos no técnicos (directivos, colegas de otras áreas, etc.).
- Explorar interactivamente en busca de relaciones inesperadas, arrastrando, ampliando y filtrando secciones del grafo.

En el caso Enron, visualizar la red ayuda a entender quién se comunicaba con quién, cómo se formaban las comunidades o cómo ciertos nodos puente unían diversas partes de la empresa.

Utilizaremos tanto NetworkX como matplotlib, para ello deberemos ejecutar el siguiente comando para asegurar que todo lo necesario está instalado

pip install networkx matplotlib scipy

Para el caso de gephi, deberemos ir a su web [https://gephi.org/users/download/](https://gephi.org/users/download/) y descargarnos la última versión estable, nosotros utilizaremos la 0.10. Una vez hecho esto, ejecutamos el instalador e instalamos sin modificar las opciones por defecto.



### 7.2 Visualización con matplotlib y NetworkX



La librería NetworkX incorpora funciones que facilitan la representación de grafos en 2D mediante matplotlib. Estas funciones están pensadas para gráficos de tamaño mediano (centenares o, a lo sumo, pocos miles de nodos). Con decenas de miles de nodos, la visualización puede saturarse y perder legibilidad.

Las funciones básicas son:

- nx.draw(G, pos=None, ...): Dibuja el grafo 𝐺 usando un layout de fuerza por defecto si no se especifica pos.
- nx.draw_networkx_nodes(G, pos, ...): Dibuja solo los nodos con sus características.
- nx.draw_networkx_edges(G, pos, ...): Dibuja las aristas.
- nx.draw_networkx_labels(G, pos, ...): Añade etiquetas al diagrama.

Un layout es la estrategia que define en qué posición (𝑥,𝑦) se coloca cada nodo en el plano. Por ejemplo, nx.spring_layout aplica fuerzas de atracción y repulsión para tratar de que los nodos más relacionados aparezcan más cerca entre sí, aunque no garantiza un resultado totalmente reproducible (a menos que fijemos una semilla aleatoria).



```python
import networkx as nx
import matplotlib.pyplot as plt

# Asumiendo un subconjunto de 100 nodos
sub_nodes = list(grafo_enron.nodes())[:100] 
G_sub = grafo_enron.subgraph(sub_nodes).copy()

pos = nx.spring_layout(G_sub, seed=42)

plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G_sub, pos, node_size=50, node_color='blue', alpha=0.7)
nx.draw_networkx_edges(G_sub, pos, edge_color='gray', alpha=0.4)
plt.axis('off')
plt.title("Subconjunto de la red Enron (100 nodos)")
plt.show()
```



![image](assets/cm8npzc6k02md356xw01h2asp-Imagen39.jpg)



Si ya detectamos comunidades (por ejemplo, con Louvain), podemos colorear cada comunidad con un color distinto. La idea sería:

- Obtener la partición en forma de lista de conjuntos.
- Asignar un color distinto a cada conjunto.
- Dibujar los nodos de cada comunidad por separado.

Para redes pequeñas o medianas, este método suele funcionar aceptablemente. Sin embargo, si la red supera unos pocos miles de nodos, la figura puede volverse caótica y lenta de generar.



```python
import matplotlib.pyplot as plt
from networkx.algorithms import community

communities_louvain = community.louvain_communities(G_undirected)

num_comunidades = len(communities_louvain)

pos = nx.spring_layout(G_undirected, seed=42)
plt.figure(figsize=(12,8))

cmap = plt.cm.get_cmap('tab20', num_comunidades)
for idx, comm_set in enumerate(communities_louvain):
    nx.draw_networkx_nodes(
        G_undirected, 
        pos,
        nodelist=list(comm_set),
        node_color=[cmap(idx)],
        node_size=20,
        alpha=0.7
    )

nx.draw_networkx_edges(G_undirected, pos, alpha=0.2, edge_color='gray')
plt.axis('off')
plt.title("Comunidades detectadas (Louvain) en la red Enron")
plt.show()
```



### 7.3 Visualización con Gephi



Cuando la red es grande o se requiere interactividad para explorar, gephi se convierte en una opción mucho más profesional. gephi es un software de escritorio gratuito y open source, diseñado específicamente para la manipulación y visualización de redes.

El primer paso para usar gephi con la red de Enron es exportar nuestro grafo de NetworkX a un formato que gephi reconozca, siendo GEXF uno de los más utilizados:

nx.write_gexf(G_undirected, "enron_network.gexf")

Con esto, disponemos de un archivo enron_network.gexf que puede abrirse directamente en gephi. Para ello simplemente abrimos Gephi, vamos a “Archivo” > “Abrir” y seleccionamos el archivo exportado.

También podremos previsualizar con diferentes layout, aplicar filtros, modificar estilos, etc. Además, nos permite inspeccionar un nodo en particular, resaltar sus conexiones, agrupar nodos, aplicar diferentes layouts en sucesión (por ejemplo, primero Force Atlas 2, luego un ajuste manual), etc. Este dinamismo facilita mucho la exploración.

Exploremos en el siguiente video cómo podemos hacer todas estas operaciones:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651989_1/scormcontent/assets/INSD_BAIN_U5_Video5.mp4?v=1)



## 8. Aplicaciones De Sna



### 8.1 Introducción



![image](assets/cm8nq1wqb02py356xvha27l8y-stock-image.jpg)



En los apartados anteriores, hemos explorado las bases teóricas y prácticas del Análisis de Redes Sociales (SNA), usando como ejemplo central la red de correos del caso Enron. Sin embargo, los principios y métodos que hemos desarrollado —construcción de grafos, cálculo de métricas de centralidad, detección de comunidades y visualización— trascienden ampliamente ese escenario. De hecho, el SNA se ha convertido en una disciplina clave para abordar problemas muy diversos, tanto en el ámbito empresarial como en la investigación académica y en el desarrollo de sistemas de software.

En este apartado, revisaremos aplicaciones destacadas del SNA que pueden resultar de gran interés para estudiantes y profesionales de la Ingeniería de Software, mostrando cómo estas técnicas se aplican en distintos contextos y qué beneficios aportan.



### 8.2 Análisis de redes sociales corporativas



El caso Enron no es el único ejemplo de estudio de redes sociales internas (también llamadas Enterprise Social Networks). Muchas grandes corporaciones disponen de intranets, sistemas de correo corporativo o plataformas de mensajería interna (por ejemplo, Slack, Microsoft Teams) que generan volúmenes importantes de datos relacionales.

¿Qué aporta el SNA en estos entornos?



- **Optimización de la comunicación interna**  
  Identificar cuellos de botella, personas que centralizan en exceso los flujos de información o detectar subgrupos con poca interacción con el resto.
- **Mapeo de la cultura organizativa**  
  A menudo, los organigramas formales difieren de la realidad operativa. El SNA revela “jefes informales” o líderes de proyecto que no figuran en puestos jerárquicos altos, pero que desempeñan un rol clave en la coordinación.
- **Gestión del conocimiento**  
  Encontrar expertos técnicos (nodos con alta centralidad) o departamentos que requerirían mayor coordinación.
- **Ciberseguridad y auditoría**  
  Similar al caso Enron, se puede usar el SNA para descubrir flujos anómalos (p.ej., un usuario que envía mucho tráfico fuera de la empresa), o comunidades sospechosamente herméticas en contextos de fraude.



En la práctica, se diseñan dashboards que muestran un diagrama simplificado (o métricas clave) de la red de comunicación, permitiendo a los directivos tomar decisiones informadas sobre reorganizaciones, asignaciones de personal, etc.



### 8.3 Sistemas de recomendación basados en grafos



Los sistemas de recomendación (como los de Netflix, YouTube o Amazon) se basan con frecuencia en redes bipartitas: un conjunto de nodos representa usuarios, y el otro conjunto representa productos o recursos (películas, libros, cursos, etc.). Una arista entre usuario y producto indica que el usuario ha consumido, comprado o valorado ese ítem.

A partir de esa red bipartita, aplicamos SNA para:

- Medir la similitud entre usuarios (quienes comparten productos) o entre productos (comparten usuarios).
- Agrupar comunidades (detectando grupos de usuarios con gustos parecidos).
- Propagar la relevancia: un producto con alta centralidad (por estar conectado a usuarios influyentes) tiende a recibir más recomendaciones.

En la Ingeniería de Software, imaginar un sistema de recomendación para documentos técnicos o repositorios de código es muy plausible. Si cada usuario (desarrollador) se conecta a repositorios que ha clonado o a proyectos en los que colabora, se puede inferir “si a un desarrollador le gusta tal repositorio, probablemente también le interese este otro”.



### 8.4 Detección de fraude y anomalías



Finalmente, un ámbito en rápida expansión para las aplicaciones del SNA es la detección de fraude. En sistemas financieros, aseguradoras, bancos o incluso en plataformas de comercio electrónico, se forman redes de transacciones o de relaciones (por ejemplo, cuentas bancarias enlazadas a los mismos dispositivos, tarjetas de crédito, etc.). El SNA puede señalar:

**Comportamientos sospechosos**: subredes muy cerradas que se dedican a wash transactions, o nodos con conexiones anormalmente dispersas que podrían indicar intentos de fraude multi-relacional.

**Uso de métricas de centralidad**: un actor con una intermediación elevada puede representar una “mula” financiera que transfiere fondos entre varias cuentas.

**Aplicación de algoritmos de clustering**: para aislar comunidades fraudulentas que intercambian transacciones de bajo valor, intentando no despertar sospechas.

Por ejemplo, se puede modelar una red de cuentas (nodos = cuentas bancarias, aristas = transacciones). Un cluster de nodos con alto volumen de transacciones cíclicas podría ser un indicio de blanqueo de dinero. Varias empresas FinTech y bancos recurren a estos análisis para reforzar sus sistemas de compliance.



## 9. Conclusiones



### 9.1 Conclusiones de la unidad



Al finalizar esta unidad dedicada al Análisis de Redes Sociales (SNA) con Python, resulta evidente el enorme potencial que tienen los métodos y técnicas aquí estudiados para abordar problemas muy diversos en el ámbito de la ingeniería de software y la ciencia de datos. Desde el caso Enron, donde el estudio de la red de correos permitió desvelar subgrupos y flujos de información críticos, hasta la creación de sistemas de recomendación y la detección de fraude, el SNA aporta herramientas cuantitativas y cualitativas que facilitan la comprensión de cómo están conectados los elementos de un sistema.

La Teoría de Grafos nos sirvió de base para modelar escenarios complejos mediante nodos y aristas, allanando el camino para estudiar propiedades esenciales como el grado, la densidad, el diámetro y la conectividad. Posteriormente, nos enfocamos en la construcción de redes en Python, empleando librerías como NetworkX, que combina flexibilidad y potencia a la hora de crear, manipular y analizar grafos. El caso Enron evidenció, además, la relevancia de limpiar y normalizar los datos antes de realizar cualquier análisis, así como la importancia de tener en cuenta el contexto organizativo y las implicaciones éticas de examinar comunicaciones privadas.

Las métricas de red (centralidades de grado, intermediación, cercanía, PageRank, entre otras) proporcionaron un modo de identificar nodos clave o “puentes” críticos en la transmisión de información. Por su parte, los algoritmos de detección de comunidades (Louvain, Girvan–Newman) revelaron subgrupos con alta cohesión interna y poca conexión con otros grupos, lo que puede interpretarse de distintas maneras, desde el surgimiento de silos hasta la formación de equipos especializados.



Nota Final: Se anima a los estudiantes a continuar explorando el ecosistema Python y enfrentarse a proyectos personales. La tecnología evoluciona rápidamente y es necesario estar atentos a las nuevas actualizaciones y librerías. Sólo así se podrá mantener una ventaja competitiva y aprovechar al máximo todas las posibilidades que ofrece el Análisis de Redes Sociales en entornos de software y más allá.
