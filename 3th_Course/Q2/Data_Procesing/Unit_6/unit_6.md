# Unidad 6. Spark Machine Learning: Contextualización.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Spark Machine Learning: Contextualización](#2-spark-machine-learning-contextualización)
  - [2.1 Introducción](#21-introducción)
  - [2.2 Spark ML vs MLlib: ¿en qué se diferencian?](#22-spark-ml-vs-mllib-en-qué-se-diferencian)
- [3. Recordatorio De Fundamentos Del Aprendizaje Automático](#3-recordatorio-de-fundamentos-del-aprendizaje-automático)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Concepto de modelo](#32-concepto-de-modelo)
  - [3.3 Tipos de modelos en Machine Learning](#33-tipos-de-modelos-en-machine-learning)
  - [3.4 Revisión de conceptos básicos](#34-revisión-de-conceptos-básicos)
- [4. Metodología](#4-metodología)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Tipos de análisis y objetivos](#42-tipos-de-análisis-y-objetivos)
  - [4.3 Fases del proceso de modelado](#43-fases-del-proceso-de-modelado)
  - [4.4 Herramientas](#44-herramientas)
- [5. Machine Learning Y Big Data](#5-machine-learning-y-big-data)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Preparación de datos y modelado en Spark](#52-preparación-de-datos-y-modelado-en-spark)
- [6. Ejercicios](#6-ejercicios)
  - [6.1 Introducción](#61-introducción)
  - [6.2 Recordatorio Spark SQL (Exploración de datos)](#62-recordatorio-spark-sql-exploración-de-datos)
  - [6.3 Análisis avanzado en la exploración (continuación del ejercicio anterior de vinos)](#63-análisis-avanzado-en-la-exploración-continuación-del-ejercicio-anterior-de-vinos)
  - [6.4 Modelo de clasificación para detectar el género de una voz](#64-modelo-de-clasificación-para-detectar-el-género-de-una-voz)
  - [6.5 Regresión lineal](#65-regresión-lineal)
  - [6.6 Regresión logística](#66-regresión-logística)
  - [6.7 Otro ejemplo con Random forest](#67-otro-ejemplo-con-random-forest)
- [7. Conclusiones](#7-conclusiones)
  - [7.1 Conclusiones de la unidad](#71-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad se abordarán los fundamentos, metodologías y herramientas clave para aplicar **aprendizaje automático sobre grandes volúmenes de datos**, con especial énfasis en el uso de **Apache Spark ML** como entorno escalable de procesamiento distribuido. En la era digital, donde los datos fluyen de manera continua y masiva, el **machine learning** se convierte en una tecnología esencial para convertir esos datos en **conocimiento accionable**, capaz de generar ventajas competitivas en entornos empresariales e industriales.

Se revisarán conceptos fundamentales del aprendizaje automático, diferenciando entre los modelos **supervisados y no supervisados**, así como otras variantes como el aprendizaje por refuerzo o auto-supervisado, contextualizando su uso dentro del ecosistema de Big Data. Se introducirán los conceptos de **modelo, entrenamiento, generalización, overfitting, sesgo-varianza**, y se repasarán los elementos esenciales que definen un flujo de trabajo completo de machine learning: desde la recolección y preparación de datos, hasta el despliegue de modelos productivos.

Especial atención se prestará a la **API de Spark ML**, que permite construir pipelines de machine learning integrados y reproducibles mediante estructuras como DataFrames, Transformers y Estimators. A través de estas abstracciones, Spark ML facilita el diseño modular de soluciones analíticas escalables, aplicables a tareas como clasificación, regresión, clustering o reducción de dimensionalidad, entre otras.

Además, se compararán las dos principales interfaces de aprendizaje automático de Spark —**MLlib** y **Spark ML**— para entender su evolución, diferencias y casos de uso recomendados. También se examinarán los retos y limitaciones actuales de Spark ML, así como su integración con otras tecnologías del ecosistema Big Data.

A lo largo de esta unidad, se propondrán diversos **ejercicios prácticos**, incluyendo modelos de clasificación, regresión y clustering sobre datasets reales (como vinos, voces o datos de usuarios), permitiendo al estudiante **desarrollar habilidades completas en la construcción, evaluación y puesta en producción de modelos de machine learning distribuidos**.

Los apartados principales que estructuran esta unidad didáctica serán:



- **Fundamentos del aprendizaje automático**  
  Conceptos clave, tipos de modelos, métricas de evaluación y desafíos como el overfitting o la maldición de la dimensionalidad.
- **Apache Spark como entorno de aprendizaje automático distribuido**  
  Introducción al motor, ventajas del procesamiento paralelo y uso de DataFrames.
- **Spark ML vs MLlib**  
  Comparación entre APIs, paradigma de desarrollo, soporte para pipelines y estado actual de mantenimiento.
- **Preparación de datos para machine learning**  
  limpieza, transformación, normalización y exploración con Spark SQL.
- **Construcción de pipelines de machine learning en Spark**  
  Uso de transformadores, estimadores y ensamblado modular del flujo de trabajo.
- **Evaluación y despliegue de modelos**  
  Métricas, validación cruzada, reentrenamiento, integración en sistemas y monitorización en producción.
- **Aplicación práctica de modelos**  
  Ejercicios guiados sobre clasificación de voces, regresión deportiva, predicción de comportamiento de clientes y segmentación de vinos por clustering.



#### Objetivos



1. **Comprender** los fundamentos del aprendizaje automático y su papel estratégico en la extracción de valor a partir de datos masivos.
2. **Diferenciar** los principales tipos de modelos de machine learning (supervisados, no supervisados, semi-supervisados, por refuerzo) y sus aplicaciones prácticas.
3. **Analizar** las ventajas y limitaciones de Spark ML frente a otras librerías, valorando su idoneidad en entornos distribuidos.
4. **Explorar** las funcionalidades clave de Apache Spark para la preparación de datos, transformación y modelado a gran escala.
5. **Identificar** las etapas fundamentales de un proyecto de machine learning (comprensión del negocio, preparación, modelado, evaluación y despliegue) siguiendo la metodología CRISP-DM.
6. **Implementar** pipelines completos de machine learning con Spark ML, encadenando transformers y estimators sobre DataFrames.
7. **Aplicar** técnicas de limpieza, codificación, escalado y ensamblado de características para la preparación de conjuntos de datos estructurados.
8. **Evaluar** el rendimiento de modelos mediante métricas estadísticas como precisión, AUC, RMSE, y utilizar validación cruzada para mejorar su generalización.
9. **Desarrollar** modelos de clasificación, regresión y clustering utilizando datasets reales, siguiendo buenas prácticas de preprocesamiento y entrenamiento distribuido.
10. **Interpretar** los resultados de los modelos generados, analizando su utilidad práctica, impacto en el negocio y posibilidad de integración en entornos productivos.



## 2. Spark Machine Learning: Contextualización



### 2.1 Introducción



![image](assets/cm9vhzodn007s356zqeq6ket9-stock-image.jpg)



Aunque ya lo habréis visto en otras asignaturas conviene recordar que en la era digital, el verdadero “oro” no está en las máquinas, sino en los datos. Sin embargo, los datos por sí solos no tienen valor si no somos capaces de interpretarlos, analizarlos y convertirlos en conocimiento accionable. Ahí es donde entra el aprendizaje automático o machine learning, una rama de la inteligencia artificial que permite construir modelos capaces de aprender de los datos para realizar tareas complejas como predicciones, clasificaciones o detección de patrones ocultos.

¿Cuál es entonces el objetivo del machine learning?

El propósito principal es obtener valor de los datos. Este valor se traduce en ventajas competitivas reales para las organizaciones, como entender mejor a los clientes, anticipar fallos técnicos o incluso detectar oportunidades de negocio.



![image](assets/cm9vhvn0e004b356zyd159yhc-INSD_PRDT_U6_Apartado3-1_Imagen1.jpg)



Para que esto ocurra, es necesario descubrir relaciones y dependencias entre variables que a simple vista no se detectan. A través del análisis de grandes volúmenes de datos, podemos responder preguntas críticas como:

- ¿Qué clientes tienen más probabilidad de abandonar mi servicio?
- ¿En qué punto del proceso productivo es más probable que ocurra un fallo?
- ¿Qué patrones de comportamiento predicen compras futuras?

Este proceso de descubrimiento puede abordarse desde distintos niveles:



•

Dependencias simples, unidimensionales, que se pueden descubrir con análisis estadísticos básicos como conteos, medias o correlaciones.

•

Dependencias complejas, multidimensionales, donde intervienen múltiples variables y relaciones no lineales. En estos casos, se recurre a modelos de machine learning capaces de captar estructuras ocultas en los datos.



**Apache Spark ML se muestra como  el motor del análisis masivo.** A medida que crecen los volúmenes de datos, necesitamos herramientas capaces de procesarlos de forma eficiente. Aquí es donde **Apache Spark** juega un papel clave. Spark es un motor de procesamiento distribuido que permite trabajar con grandes volúmenes de datos en paralelo, facilitando tanto el manejo de estructuras de datos (como tablas) como la aplicación de modelos de aprendizaje automático sobre ellos.

Spark ML (la API de machine learning de Spark) proporciona un entorno completo para:

- Preparar datos: limpieza, transformación, normalización…
- Construir y entrenar modelos de machine learning.
- Evaluar resultados y desplegar modelos en producción.

Gracias a su enfoque distribuido y su integración con DataFrames y SQL, Spark ML se convierte en una herramienta poderosa y escalable para aplicar machine learning a nivel industrial, sin necesidad de mover los datos fuera de la infraestructura donde ya residen.



### 2.2 Spark ML vs MLlib: ¿en qué se diferencian?



Apache Spark proporciona dos APIs principales para trabajar con algoritmos de machine learning: MLlib y Spark ML.



![image](assets/cm9vi2exp00bw356zekdxefs9-INSD_PRDT_U6_Apartado3-2_Imagen2.jpg)



La siguiente tabla muestra sus diferencias:

| Característica | MLlib (RDD-based) | Spark ML (DataFrame-based) |
| --- | --- | --- |
| Paradigma base | RDD (Resilient Distributed Datasets) | DataFrame / Dataset |
| API más moderna | ❌ Deprecada para nuevas aplicaciones | Recomendada y en activo |
| Soporte para Pipelines (veremos posteriormente qué es esto) | No integrado | Integrado nativamente |
| Facilidad de uso | Más compleja, estilo funcional | Más expresiva, parecida a scikit-learn |
| Rendimiento y optimización | Menor optimización (sin Catalyst) | Mejor rendimiento gracias a Catalyst + Tungsten |
| Tipos de datos compatibles | Datos no estructurados | Datos estructurados (con esquema) |
| Transformadores/Estimadores (también hablaremos de ello posteriormente) | No disponibles como entidades | Totalmente soportados (fit/transform) |
| Estado actual | Mantenimiento limitado | Activa y en desarrollo |



**Spark ML** es la opción recomendada para nuevos proyectos, ya que aprovecha las ventajas de los DataFrames (mejor rendimiento, integración con SQL, mayor legibilidad del código y facilidad para construir *pipelines*).

**MLlib** se mantiene por compatibilidad con código antiguo, pero ya no es la prioridad de desarrollo.

**¿Spark ML soporta datos no estructurados?** No directamente.
Spark ML está diseñado para trabajar principalmente con **datos estructurados**, es decir, datos organizados en forma de **DataFrames** (tablas con columnas bien definidas y tipos de datos específicos).

**¿Qué pasa entonces con los datos no estructurados?** Cuando trabajas con **datos no estructurados** (como texto libre, imágenes, audio, logs, etc.), **debes transformarlos primero en una forma estructurada** para poder usarlos en Spark ML.
Esto implica aplicar una **fase previa de preprocesamiento**, que puede incluir:

- **Texto → vectores numéricos** (TF-IDF, Word2Vec, CountVectorizer, etc.)
- **Imágenes → arrays de píxeles** o embeddings
- **Logs → extracción de campos relevantes** mediante expresiones regulares o parsing

Una vez convertidos, esos datos pueden representarse como columnas en un DataFrame, y ahí sí puedes usar Spark ML.



## 3. Recordatorio De Fundamentos Del Aprendizaje Automático



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



Antes de adentrarnos en el uso práctico de técnicas de machine learning con Apache Spark, es importante hacer una breve parada para repasar algunos conceptos clave. Muchos de ellos ya han sido abordados en otras asignaturas, por lo que esta sección no pretende enseñar nada nuevo, sino refrescar terminología y fundamentos que serán imprescindibles para comprender y aplicar correctamente los contenidos de esta unidad.

Este capítulo actúa como un pequeño recordatorio: conceptos que, aunque familiares, deben estar frescos para poder construir modelos, interpretar resultados y entender las decisiones que toma un sistema de aprendizaje automático. A través de una revisión ágil, te situaremos rápidamente en el contexto adecuado para aprovechar al máximo el potencial de Spark ML.



### 3.2 Concepto de modelo



Cuando hablamos de *machine learning*, una de las palabras más repetidas —y muchas veces malentendidas— es **modelo**. Pero, ¿qué significa exactamente construir un modelo en este contexto?

Podríamos definirlo de manera informal como **una herramienta capaz de aprender a partir de datos para resolver un problema concreto**. Gracias a las técnicas de aprendizaje automático, podemos desarrollar modelos que permiten abordar tareas muy diversas y con impacto real en nuestra vida cotidiana o en la actividad empresarial.

Estos modelos se aplican a problemas tan variados como el reconocimiento de voz, la detección temprana de fallos en maquinaria, la evaluación del riesgo crediticio o incluso el diagnóstico médico. En todos estos casos, el objetivo es el mismo: **extraer patrones de los datos para tomar decisiones automáticas o hacer predicciones útiles**.

Pero, ¿para qué sirve realmente un modelo? Su utilidad radica en tres pilares clave:

- Primero, **automatizan tareas que antes requerían intervención humana**, como identificar objetos en una imagen o transcribir una conversación.
- Segundo, **mejoran la precisión en la toma de decisiones**, ya que un modelo bien entrenado puede detectar patrones complejos que escapan al análisis humano tradicional.
- Y tercero, **permiten hacer predicciones en base a datos históricos**, como anticipar el mantenimiento de un equipo o prever si un cliente contratará una hipoteca en los próximos meses.

Una vez entendido qué es un modelo y para qué sirve, surge la pregunta clave: **¿cómo construimos uno?** ¿Qué hace falta para que una máquina pueda aprender y tomar decisiones con base en datos?

La respuesta puede parecer simple, pero es fundamental**: necesitamos datos, y además, que esos datos representen bien el problema que queremos resolver.**

Los datos son el combustible del aprendizaje automático. Sin ellos, no hay nada que aprender. Pero no se trata simplemente de tener muchos datos: **lo importante es que sean relevantes y estén bien etiquetados si el problema lo requiere**. Por ejemplo, si queremos entrenar un modelo para distinguir gatos de perros en imágenes, no basta con tener muchas fotos; es necesario que cada imagen esté correctamente clasificada como “gato” o “perro”.

En esta imagen vemos varios ejemplos ilustrativos:



Conjunto de dígitos escritos a mano: este tipo de datos se utiliza para entrenar modelos de reconocimiento de escritura.Imágenes de gatos y perros: ejemplo clásico de clasificación supervisada con datos etiquetados.Un grupo de personas dividido por colores: representa un caso de clustering, donde se busca agrupar elementos similares sin etiquetas previas (aprendizaje no supervisado).Un gráfico de bolsa: ejemplo de datos temporales que pueden usarse para modelos de predicción financiera.



Todos estos casos tienen algo en común: parten de datos bien definidos y alineados con el objetivo del modelo. Sin una **muestra representativa**, el modelo no aprenderá de forma adecuada, y cualquier predicción que haga será poco fiable o incluso peligrosa.

Concluimos por tanto que  **para construir un modelo útil y fiable, hay que empezar por obtener los datos correctos y asegurarse de que reflejan el problema real que queremos resolver.**

Llegados a este punto, la pregunta es inevitable: **¿Qué es exactamente un modelo, en términos formales?**
Un modelo puede entenderse como una **regla o función matemática** que todas las muestras deben seguir. En términos más técnicos:



![image](assets/cm9vibnh000is356z7xivubu1-INSD_PRDT_U6_Apartado4-2_Imagen4.jpg)



- **Modelo = f(x)**  
  Donde x representa las variables de entrada (características del problema) y f es la función que el modelo ha aprendido a partir de los datos.



En realidad, cuando construimos modelos, lo que hacemos es aplicar principios matemáticos y estadísticos. Vemos nuestros datos como **realizaciones de una variable aleatoria** y buscamos encontrar la función que mejor explique su comportamiento. Esta función, en muchos casos, **se basa en la estimación de una función de densidad de probabilidad (fdp)**.

Para evaluar la calidad de nuestros modelos, usamos **métricas estadísticas** que nos indican si el modelo generaliza bien o si simplemente memoriza los datos (overfitting). Algunas métricas comunes incluyen el AUC (Área Bajo la Curva), TPR (Tasa de Verdaderos Positivos), o la TNR (Tasa de Verdaderos Negativos), entre otras.



### 3.3 Tipos de modelos en Machine Learning



Una vez sabemos qué es un modelo y qué necesitamos para construirlo, el siguiente paso natural es preguntarnos: ¿qué tipo de problemas podemos resolver con aprendizaje automático?

Existen múltiples enfoques, pero los más habituales se agrupan en dos grandes categorías**: supervisado y no supervisado**. Esta clasificación se basa principalmente en la disponibilidad de etiquetas o resultados conocidos durante el entrenamiento del modelo.



![image](assets/cm9vie33600lc356zd2mxcil8-INSD_PRDT_U6_Apartado4-3_Imagen5.png)



- **Modelos supervisados**  
  En este tipo de modelos, **los datos de entrenamiento incluyen tanto las características de entrada como la salida esperada (la etiqueta)**. Es decir, sabemos de antemano cuál es la “respuesta correcta” y el objetivo del modelo es aprender a predecirla. Dentro del aprendizaje supervisado, distinguimos dos casos principales:

  - **Clasificación**: cuando la salida es una categoría (por ejemplo, “spam” o “no spam”, o el tipo de enfermedad).
  - **Regresión**: cuando la salida es un valor numérico continuo (por ejemplo, el precio de una casa o la temperatura de una ciudad).

  Matemáticamente hablando se definen como:
  ![image](assets/cm9viekq300ly356zy3x1fd69-tab1-img1-INSD_PRDT_U6_Apartado4-3_Imagen6.jpg)
- **Modelos no supervisados**  
  Aquí, **los datos no vienen etiquetados**, y el modelo debe descubrir por sí mismo patrones, agrupaciones o estructuras ocultas. Los casos más representativos son:

  - **Clustering (agrupamiento)**: separar instancias en grupos según su similitud, sin conocer de antemano las categorías.
  - **Detección de anomalías**: identificar comportamientos que se desvían significativamente del resto, como fraudes financieros o fallos técnicos.

  Matemáticamente hablando se define:
  ![image](assets/cm9viekq300ly356zy3x1fd69-tab2-img1-INSD_PRDT_U6_Apartado4-3_Imagen7.jpg)



#### Otros tipos de aprendizaje



- **Aprendizaje por refuerzo (Reinforcement Learning)**  
  En el que un agente aprende a actuar en un entorno mediante prueba y error, recibiendo recompensas o castigos. Es clave en robótica, juegos o conducción autónoma.
- **Aprendizaje semi-supervisado**  
  Mezcla de datos etiquetados y no etiquetados.
- **Aprendizaje auto-supervisado**  
  El modelo genera sus propias etiquetas a partir de los datos crudos, muy utilizado en visión por computador y procesamiento del lenguaje natural.



**¿Por qué no los tratamos en esta unidad?**
Porque **Spark ML no está orientado al procesamiento de estos paradigmas avanzados**. Su enfoque principal, y mejor soportado,  está en los modelos clásicos supervisados y no supervisados, aplicables a problemas estructurados sobre grandes volúmenes de datos, que son los que típicamente encontramos en entornos empresariales y Big Data.



### 3.4 Revisión de conceptos básicos



A continuación, repasaremos una serie de conceptos fundamentales que **seguramente ya conoces de cursos o asignaturas anteriores**, pero que conviene tener muy presentes antes de adentrarnos en la implementación práctica con Spark ML. Son términos que aparecerán constantemente y sobre los que se construyen los fundamentos del *machine learning* moderno.



- **Conjunto de entrenamiento**  
  Es el **grupo de datos que usamos para enseñar al modelo**. Contiene ejemplos con los que se ajustan los parámetros internos del modelo, permitiéndole aprender las relaciones entre entradas y salidas. Por ejemplo, si estamos construyendo un clasificador de correos spam, el conjunto de entrenamiento incluirá ejemplos de correos ya etiquetados como spam o no spam.
- **Atributo o característica (Xi)**  
  Se refiere a **cada una de las variables que describen una observación**. En términos simples, son las columnas del dataset que contienen información útil para que el modelo aprenda. Por ejemplo, en un dataset de viviendas, atributos pueden ser la superficie, el número de habitaciones o el código postal.
- **Entrenamiento**  
  Es el **proceso mediante el cual el modelo aprende a partir del conjunto de entrenamiento**. Consiste en ajustar sus parámetros internos para minimizar el error entre las predicciones y las respuestas reales. El entrenamiento es la etapa más crítica en la construcción de un modelo de *machine learning*.
- **Capacidad de generalización**  
  Un modelo no solo debe funcionar bien sobre los datos que ha visto (entrenamiento), sino también sobre **datos nuevos que nunca ha procesado**. Esa habilidad se conoce como **capacidad de generalización**, y es lo que distingue un modelo útil de uno que simplemente memoriza.
- **Underfitting y Overfitting**  
  - **Underfitting (subajuste)** ocurre cuando el modelo **no es lo suficientemente complejo** como para captar los patrones del problema. Da malos resultados incluso en entrenamiento.
  - **Overfitting (sobreajuste)** es lo contrario: el modelo **aprende demasiado bien los datos de entrenamiento**, incluyendo el ruido o detalles irrelevantes, y falla al enfrentarse a nuevos datos.

  El reto es encontrar un equilibrio que permita al modelo **aprender lo necesario sin sobreactuar**.
- **Sesgo-varianza**  
  Es un concepto estadístico clave para entender los errores de un modelo:

  - **Sesgo**: error por asumir suposiciones demasiado simples.
  - **Varianza**: error por sensibilidad excesiva a pequeñas variaciones en los datos.

  Un modelo ideal debe **mantener bajo control ambos factores**. Demasiado sesgo → underfitting; demasiada varianza → overfitting.
- **Maldición de la dimensionalidad**  
  Cuantas más variables (atributos) usamos, más complejo se vuelve el espacio en el que opera el modelo. Esto puede parecer positivo, pero **a partir de cierto punto, los datos se dispersan tanto que resulta difícil aprender patrones útiles**.
  Esta problemática se conoce como la **maldición de la dimensionalidad**, y suele combatirse con técnicas de reducción de dimensiones o selección de características relevantes.



## 4. Metodología



### 4.1 Introducción



![image](assets/cm9viojbp00rb356znwbb1nlp-stock-image.jpg)



Construir un modelo de machine learning no es solo aplicar un algoritmo a unos datos y esperar resultados. Detrás de todo modelo útil y fiable hay un proceso metódico y bien estructurado, que va desde entender el problema hasta desplegar el modelo en producción. Esta metodología permite trabajar de forma ordenada, colaborativa y reproducible, y es especialmente importante cuando tratamos con grandes volúmenes de datos o queremos obtener resultados aplicables en entornos reales.

A lo largo de este capítulo, repasaremos las fases fundamentales de este proceso, desde el entendimiento del negocio y los datos, hasta la evaluación y despliegue del modelo. No entraremos en la implementación técnica aún, pero sí sentaremos las bases de cómo debe planificarse un proyecto de machine learning de principio a fin.



### 4.2 Tipos de análisis y objetivos



Uno de los primeros pasos en cualquier proyecto de análisis de datos es **entender qué tipo de preguntas queremos responder**. Esta decisión condicionará no solo la metodología que seguiremos, sino también el tipo de modelo y las herramientas que necesitaremos.

En el ámbito del análisis de datos existen tres grandes tipos de enfoques, cada uno con un nivel creciente de complejidad y valor añadido:



- **Análisis descriptivo: ¿Qué ha sucedido?**  
  Es el más básico, pero también el más extendido. Se centra en **resumir y visualizar los datos para entender el pasado**, detectar patrones históricos y describir el comportamiento observado. Por ejemplo, responder preguntas como:

  - ¿Cuántos clientes hemos perdido este trimestre?
  - ¿Qué productos han tenido mayor demanda?

  Este tipo de análisis es útil para tener una foto clara de la situación, pero no permite anticiparse ni tomar decisiones proactivas.
- **Análisis predictivo: ¿Qué va a suceder?**  
  Aquí entramos de lleno en el mundo del *machine learning*. El análisis predictivo **busca anticipar el futuro a partir de datos históricos**, modelando relaciones complejas entre variables. Algunos ejemplos:

  - ¿Qué clientes tienen mayor probabilidad de abandonar el servicio?
  - ¿Cuál será la demanda de un producto el próximo mes?

  Este tipo de análisis transforma los datos en conocimiento aplicable para **predecir comportamientos, eventos o resultados futuros**, y es uno de los principales objetivos del aprendizaje automático.
- **Análisis prescriptivo: ¿Qué debo hacer si...?**  
  El análisis prescriptivo va un paso más allá. **No solo predice lo que va a pasar, sino que sugiere acciones óptimas en función de esas predicciones.**
  Por ejemplo:

  - Si un cliente tiene alta probabilidad de irse, ¿qué oferta personalizada deberíamos enviarle?
  - Si se prevé un fallo en una máquina, ¿conviene detener la línea o redistribuir la carga?

  Este enfoque **integra modelos predictivos con lógica de decisión**, lo que lo convierte en una herramienta poderosa para la automatización y la optimización en la toma de decisiones.

  **Objetivo general en machine learning: predicción + prescripción**

  Aunque los tres tipos de análisis pueden coexistir en un proyecto, **el verdadero potencial del machine learning aparece cuando combinamos predicción y prescripción**. Es decir, no solo saber qué va a pasar, sino poder actuar con antelación y eficacia.
  Ese es el foco de muchas aplicaciones actuales: sistemas de recomendación, mantenimiento predictivo, marketing automatizado o gestión de riesgos.



### 4.3 Fases del proceso de modelado



El proceso de desarrollo de un modelo de *machine learning* va mucho más allá de elegir un algoritmo y aplicarlo a unos datos. **Se trata de una cadena estructurada de fases**, donde cada etapa depende de la calidad y el enfoque con el que se abordó la anterior.
Este enfoque metodológico no solo mejora los resultados técnicos, sino que también **favorece la trazabilidad, la colaboración y la utilidad práctica de los modelos**.

A continuación, presentamos las seis fases fundamentales que conforman el ciclo de vida de un proyecto de aprendizaje automático.

Esta imagen representa el **ciclo de vida de un proyecto de machine learning**, mostrando cómo las distintas fases —desde la comprensión del negocio hasta el despliegue— se organizan de forma iterativa en torno a los datos, permitiendo refinar continuamente el modelo a medida que se aprende más del problema.



![image](assets/cm9vit3wq00us356zhe25vrqx-INSD_PRDT_U6_Apartado5-3_Imagen8.jpg)



Por otro lado, la siguiente imagen representa el modelo **CRISP-DM (Cross Industry Standard Process for Data Mining)**, una metodología ampliamente adoptada para guiar proyectos de ciencia de datos y machine learning. Divide el ciclo de vida en seis fases —desde la comprensión del negocio hasta el despliegue, detallando tareas clave en cada etapa y enfatizando la naturaleza iterativa del proceso.



![image](assets/cm9vituh700w5356ziaas5x2x-INSD_PRDT_U6_Apartado5-3_Imagen9.jpg)



Ambas imágenes reflejan **el mismo ciclo metodológico**, pero desde perspectivas complementarias:

- La primera ofrece una vista más conceptual y visual del flujo.
- Esta segunda desglosa cada fase con más precisión operativa, **sirviendo como una guía práctica paso a paso** para la ejecución real de proyectos de datos.



- **Comprensión del negocio (Business Understanding)**  
  Todo comienza aquí. Antes de hablar de datos o modelos, hay que entender el contexto del problema, las necesidades del negocio y los objetivos concretos que se desean alcanzar. En esta fase se definen:

  - Qué entidad vamos a modelar (persona, evento, imagen, etc.).
  - Qué tipo de modelo es más adecuado: supervisado o no supervisado.
  - Qué limitaciones temporales o técnicas hay (por ejemplo, frecuencia de predicción o disponibilidad de datos).
  - Qué acciones se podrán tomar a partir de las predicciones (recomendaciones, alertas, decisiones automáticas, etc.).

  Esta etapa marca la dirección del proyecto. Si no se define bien aquí el problema, **todo lo que venga después será técnicamente correcto pero probablemente inútil**.
- **Comprensión de los datos (Data Understanding)**  
  Una vez entendido el problema, pasamos a identificar, explorar y comprender los datos que tenemos disponibles. Aquí es donde se responden preguntas como:

  - ¿De dónde proceden los datos? (bases de datos internas, APIs, sensores, redes sociales…)
  - ¿Son suficientes y relevantes para el problema?
  - ¿Qué calidad tienen? ¿Hay valores faltantes o errores?

  Esta fase permite detectar limitaciones o sesgos que condicionarán el éxito del modelo, y decidir si se requiere recolección adicional o limpieza previa.
- **Preparación de los datos (Data Preparation)**  
  Aquí se realiza el trabajo más costoso y menos glamuroso, pero absolutamente esencial. **Preparar los datos consiste en transformarlos para que puedan ser utilizados por los modelos**. Incluye tareas como:

  - Identificar variables categóricas y numéricas.
  - Normalizar, formatear, limpiar e imputar valores faltantes.
  - Crear nuevas variables a partir de las existentes (feature engineering).
  - Seleccionar características relevantes.
  - Dividir los datos en conjuntos de entrenamiento, validación y test.

  Esta etapa es crítica porque, si los datos no están bien preparados, **el modelo no podrá aprender correctamente, por muy sofisticado que sea**.
- **Modelado (Modeling)**  
  Con los datos ya listos, **es hora de elegir el modelo y entrenarlo**. En esta fase se:

  - Selecciona un algoritmo adecuado (árboles, regresión, redes neuronales…).
  - Ajustan sus hiperparámetros para mejorar el rendimiento.
  - Evalúa si el modelo está aprendiendo correctamente o presenta problemas como *overfitting* o *underfitting*.
  - Se analiza la importancia de las variables en el proceso de decisión del modelo.

  Esta fase es donde se ejecuta el *core* del aprendizaje automático, pero **no debería abordarse sin haber completado correctamente las etapas previas**.
- **Evaluación (Evaluation)**  
  Una vez entrenado, **el modelo debe ser evaluado con datos que no ha visto durante el entrenamiento**, para obtener una estimación realista de su capacidad de generalización. En esta fase se:

  - Evalúa el modelo sobre el conjunto de test.
  - Se calculan métricas como precisión, AUC, RMSE, etc., según el tipo de problema.
  - Se analiza el impacto del modelo en términos de negocio.
  - Se identifican posibles mejoras o limitaciones.

  Evaluar no es solo obtener una métrica, sino entender **si el modelo es útil en la práctica y cómo puede integrarse en la operativa real**.
- **Despliegue (Deployment)**  
  Por último, llega el momento de **pasar el modelo a producción**, es decir, hacerlo accesible para que otras aplicaciones, sistemas o personas puedan usarlo. Esta fase es crítica para que el modelo tenga un impacto real en el negocio, ya que **hasta que no se despliega, todo lo anterior sigue siendo experimental**.

  Esto incluye:

  - **Establecer umbrales mínimos de rendimiento aceptable**, que definan cuándo un modelo puede considerarse válido para operar (por ejemplo, una precisión mínima, o una tasa máxima de falsos positivos).
  - **Integrar el modelo en el entorno operativo**, lo que puede implicar exponerlo como una API, incrustarlo en una aplicación o programarlo como parte de un flujo de datos automatizado.
  - **Automatizar el reentrenamiento**, definiendo con qué frecuencia se debe actualizar el modelo en función de la llegada de nuevos datos o cambios en el entorno.
  - **Monitorizar el comportamiento del modelo en producción**, para detectar si su rendimiento comienza a degradarse (por ejemplo, por *drift* en los datos o cambios en el comportamiento del usuario).
  - **Medir resultados reales** y comparar el impacto del modelo con las expectativas definidas en la fase de negocio.

  En definitiva, **el despliegue convierte al modelo en una herramienta viva**, que debe mantenerse, supervisarse y ajustarse periódicamente para seguir siendo útil y eficaz.



### 4.4 Herramientas



Una vez definido el proceso metodológico para construir modelos de machine learning, el siguiente paso lógico es preguntarnos: ¿con qué herramientas podemos implementarlo?
La elección de herramientas no es trivial: depende del entorno de trabajo, del volumen de datos, del tipo de modelo y de los objetivos del proyecto. A continuación, presentamos una clasificación básica de herramientas, agrupadas según el contexto en que se usan habitualmente.



- **Entornos locales (individuales o pequeños equipos)**  
  Estas herramientas son ideales para desarrollo exploratorio, análisis de prototipos o proyectos con volúmenes de datos manejables desde un solo equipo:

  - **R**: muy popular en estadística y ciencia de datos, con gran número de paquetes especializados y una curva de aprendizaje algo más técnica.
  - **Python**: lenguaje generalista pero muy potente para ciencia de datos gracias a librerías como pandas, scikit-learn, TensorFlow, entre muchas otras.
  - **MATLAB**: entorno cerrado muy utilizado en entornos académicos y de ingeniería, especialmente para análisis numérico y simulación.
- **Herramientas para entornos distribuidos (Big Data)**  
  Cuando el volumen de datos supera la capacidad de procesamiento local, entramos en el terreno de las plataformas distribuidas, capaces de manejar grandes cantidades de información en paralelo:

  - **Apache Spark:** probablemente la herramienta más versátil y extendida para procesamiento distribuido de datos, con soporte específico para machine learning (MLlib y Spark ML).
  - **Apache Flink**: más orientado a procesamiento de flujos en tiempo real, aunque también puede emplearse en modelos de ML.
  - **Hadoop**: pionero en Big Data, centrado en el almacenamiento y procesamiento en batch mediante su sistema distribuido (HDFS y MapReduce). Hoy se complementa con herramientas como Spark.
- **Principales librerías y frameworks de machine learning**  
  Estas librerías permiten aplicar algoritmos de aprendizaje automático de forma directa, flexible y eficiente. Se integran con los lenguajes anteriores y son el núcleo del desarrollo de modelos:

  - **H2O.ai**: plataforma escalable para machine learning y deep learning, con interfaces para R, Python y Java.
  - **Scikit-learn**: la librería más usada en Python para aprendizaje automático clásico (clasificación, regresión, clustering, etc.).
  - **TensorFlow**: framework de Google para deep learning, con gran capacidad para redes neuronales y modelos complejos.
  - **caret**: librería de R para unificar y simplificar procesos de entrenamiento y validación de modelos clásicos (Classification And Regression Training).



## 5. Machine Learning Y Big Data



### 5.1 Introducción



![image](assets/cm9vjgt7w010k356zhw9zc3kj-stock-image.jpg)



En los últimos años, la transformación digital ha generado un crecimiento explosivo en la cantidad de datos disponibles. Desde sensores en dispositivos conectados hasta registros de usuarios en plataformas online, hoy manejamos volúmenes de información que superan la capacidad de procesamiento de una sola máquina. Este fenómeno ha dado lugar al concepto de Big Data, que no solo hace referencia al volumen, sino también a la velocidad, variedad y complejidad de los datos que se generan continuamente.

En este contexto, el machine learning se convierte en una herramienta clave para extraer valor de esa información. Cuantos más datos tenemos, más precisos y robustos pueden llegar a ser nuestros modelos, ya que mejoran su capacidad de generalización y aprenden patrones más complejos. Pero este crecimiento también plantea un reto técnico importante: ¿cómo entrenar modelos sobre millones o miles de millones de registros sin colapsar nuestras máquinas?
La respuesta está en las plataformas escalables de procesamiento distribuido, como Apache Spark, que veremos más adelante.

La siguiente imagen resume muy bien el equilibrio necesario entre dos pilares complementarios:

- Por un lado, **la explotación inteligente de la información**, centrada en el análisis avanzado de los datos, con técnicas de aprendizaje automático que aportan valor a través del conocimiento.
- Por otro, **el manejo ágil y eficaz de la información**, que se apoya en la infraestructura tecnológica capaz de soportar y distribuir el procesamiento de grandes volúmenes de datos.

Ambos componentes son esenciales. De nada sirve tener algoritmos potentes si no contamos con la capacidad de procesar los datos necesarios, y viceversa: una infraestructura robusta sin análisis avanzado no genera conocimiento. **El valor surge cuando análisis e infraestructura trabajan de la mano**.



![image](assets/cm9vji5nl011u356zxl3zegpd-INSD_PRDT_U6_Apartado6-1_Imagen13.png)



#### ¿Por qué hablamos de Big Data?



- **Características claves de Spark**  
  Spark destaca por tres características clave:

  - **Motor de procesamiento distribuido**: permite dividir el trabajo entre múltiples nodos, procesando datos en paralelo de forma eficiente.
  - **Escalabilidad**: se adapta a volúmenes de datos crecientes sin perder rendimiento.
  - **Biblioteca de machine learning**: conocida como Spark ML, que ofrece una amplia gama de algoritmos y herramientas para el entrenamiento, evaluación y despliegue de modelos.
- **Limitaciones de Spark ML**  
  A pesar de sus ventajas, Spark ML no es una herramienta perfecta. Existen algunas **limitaciones que conviene conocer** antes de adoptarla en un proyecto:

  - No incluye todos los algoritmos que ofrecen otras librerías más especializadas (por ejemplo, XGBoost o LightGBM).
  - Tiene **pocas opciones avanzadas de selección de características**, lo que puede limitar la optimización del modelo en fases de ingeniería de variables.
  - Algunos algoritmos disponibles, como redes neuronales multicapa (MLP) o gradient boosting (GBM), **no devuelven probabilidades como salida**, lo cual puede ser un inconveniente para ciertos tipos de aplicaciones (como clasificación probabilística o detección de riesgo).
- **Modos de trabajo en Spark**  
  Apache Spark ofrece **dos enfoques distintos** para trabajar con aprendizaje automático, según la abstracción de datos utilizada:

  - **MLlib (basado en RDDs)**: es la biblioteca original de Spark, centrada en estructuras de datos inmutables y distribuidas llamadas RDDs (Resilient Distributed Datasets). Aunque funcional, **hoy se considera una opción más antigua y limitada**.
  - **Spark ML (basado en DataFrames)**: es la API moderna, basada en DataFrames y Pipelines, que permite construir flujos de trabajo más estructurados y expresivos, similares a los de scikit-learn. **Es la recomendada para nuevos desarrollos**, ya que facilita la integración, evaluación y reutilización de modelos.



En resumen, Spark es **una pieza fundamental en la intersección entre Big Data y machine learning**, gracias a su capacidad para combinar análisis avanzado y escalabilidad. Aunque presenta algunas limitaciones, **su potencia reside en su integración nativa con entornos distribuidos y su versatilidad como plataforma completa de procesamiento y modelado**.



### 5.2 Preparación de datos y modelado en Spark



Una vez entendido el papel de Apache Spark en el ecosistema del machine learning distribuido, es momento de adentrarnos en cómo se implementa un flujo de trabajo completo dentro de esta plataforma. En este subcapítulo abordaremos dos etapas fundamentales del proceso de construcción de modelos: la preparación de los datos y el modelado propiamente dicho.

Ambas fases son críticas para el éxito de cualquier proyecto de aprendizaje automático. La calidad del modelo no solo depende del algoritmo elegido, sino en gran medida de cómo han sido tratados, transformados y representados

El desarrollo de modelos en Spark no comienza directamente con la elección de un algoritmo, sino con una fase previa igual de importante: **la preparación de los datos**. Esta etapa incluye desde la carga y exploración inicial del conjunto de datos, hasta la aplicación de transformaciones y el diseño de flujos de trabajo reutilizables mediante *pipelines*.

Spark ofrece un conjunto de herramientas altamente integradas para facilitar este proceso, combinando la potencia del procesamiento distribuido con una sintaxis accesible y flexible. Conceptos como los **DataFrames**, el uso de **Spark SQL**, y la capacidad de construir *pipelines* permiten organizar el trabajo de forma estructurada y escalarlo fácilmente a grandes volúmenes de datos.

En los siguientes apartados exploraremos paso a paso los elementos clave que permiten preparar y transformar datos de forma eficiente en Spark, sentando las bases para un modelado robusto y reproducible.



#### Spark SQL



Ya en la Unidad 5 exploramos en profundidad el módulo Spark SQL y sus capacidades para el procesamiento de datos estructurados. En esta unidad, retomamos brevemente este componente, pero ahora con una nueva perspectiva: **su papel como herramienta clave para la preparación de datos en proyectos de machine learning**.

Spark SQL permite trabajar con **datos tabulares** de forma muy similar a un sistema tradicional de almacenamiento y análisis, como los entornos *data warehouse*. La gran ventaja es que todo esto se realiza **en un entorno distribuido y altamente escalable**, lo que lo hace ideal para manejar grandes volúmenes de datos —una necesidad habitual cuando se entrena un modelo de aprendizaje automático.

Entre sus principales funcionalidades destacan:

- El soporte completo para **operaciones sobre tablas**, que facilitan tareas como filtrado, agrupación, ordenación o agregación.
- La posibilidad de **ejecutar consultas SQL estándar**, lo cual resulta especialmente útil para quienes ya dominan ese lenguaje y desean integrarlo fácilmente en flujos de datos.
- Dos formas de construir consultas:
  - Usando **sintaxis SQL tradicional**, enviando las queries como cadenas de texto.
  - O bien, utilizando la **API estructurada que proporciona Spark**, que permite construir las consultas mediante código más organizado, legible y menos propenso a errores.

En el contexto del *machine learning*, Spark SQL es fundamental para **preparar los datos de entrada, realizar transformaciones previas, limpiar registros o construir subconjuntos útiles para el modelado**, todo ello sobre grandes volúmenes de información y sin perder rendimiento.



#### Creación del Dataframe



En la Unidad 5 ya tuvimos la oportunidad de familiarizarnos con los **DataFrames**, una de las estructuras de datos fundamentales en Spark. En esta unidad retomamos brevemente su creación y gestión, con un enfoque práctico orientado a su papel en los procesos de aprendizaje automático.

Un DataFrame en Spark es, esencialmente, una **colección distribuida de datos organizados en columnas**, muy similar a una tabla en una base de datos relacional. Esta estructura resulta especialmente útil para tareas de *machine learning*, ya que permite almacenar, transformar y acceder a los datos de manera eficiente y escalable.



![image](assets/cm9vjv49s01bx356zje1pn7rc-INSD_PRDT_U6_Apartado6-2-2_Imagen14.jpg)



Spark ofrece diferentes formas de **crear DataFrames**:

- **Inferencia automática de la estructura**, a partir de una colección de datos en memoria. Esto se logra usando el método toDF(), que genera un DataFrame deduciendo los nombres y tipos de las columnas.
- **Definición explícita de la estructura**, utilizando createDataFrame() junto con una variable de tipo StructType, que permite especificar manualmente los campos mediante objetos StructField.

Además, también es posible **leer directamente estructuras tabulares ya almacenadas** en diversos sistemas, lo que resulta muy práctico en entornos de producción. Por ejemplo, se pueden generar DataFrames a partir de:

- Archivos CSV en HDFS
- Archivos en formato Parquet
- Tablas en Hive
- Bases de datos como Cassandra
- Y otros orígenes compatibles

Estas opciones hacen de los DataFrames una herramienta extremadamente flexible para iniciar un flujo de trabajo de *machine learning*, ya que permiten integrar datos de distintas fuentes y formatos con facilidad.

Una vez creado el DataFrame, el siguiente paso natural es **explorarlo y comprenderlo**, para asegurarnos de que los datos son adecuados para entrenar un modelo. En el próximo apartado revisaremos algunas operaciones iniciales clave para esta fase de exploración, antes de pasar a la transformación y modelado.



#### Exploración inicial del  Dataframe



Antes de comenzar a transformar o modelar nuestros datos, es imprescindible dedicar unos minutos a **explorar su contenido y estructura**. Esta fase, aunque sencilla, resulta clave para detectar posibles errores, inconsistencias o patrones útiles para el análisis posterior. Spark proporciona una serie de métodos que permiten realizar esta exploración inicial de forma eficiente sobre grandes volúmenes de datos.

A nivel funcional, los **DataFrames en Spark** se comportan como tablas, y cada columna está asociada a un nombre y un tipo de dato. Este esquema (o metadatos) puede ser inspeccionado fácilmente mediante comandos muy útiles en las primeras etapas de cualquier proyecto.

A continuación, se resumen algunos de los métodos más empleados en esta fase:

- show(): muestra un conjunto de filas del DataFrame por pantalla, útil para obtener una vista general rápida.
  - Con truncate=false evitamos que se corten las columnas largas.
  - Con n indicamos cuántas filas queremos ver.
- describe(): genera una **descripción estadística** básica (mínimo, máximo, media, desviación estándar…) de las columnas numéricas seleccionadas.
- Otros métodos muy usados:
  - count(): devuelve el número total de filas.
  - distinct(): permite obtener un DataFrame con los registros únicos según una o varias columnas.

Además, para explorar el esquema del DataFrame:

- printSchema(): muestra una representación jerárquica del tipo de datos asociado a cada columna.
- dtypes: devuelve una lista de tuplas con el nombre de la columna y su tipo de dato correspondiente.
- columns: genera una lista con los nombres de todas las columnas del DataFrame.

¿Y si queremos transformar el DataFrame a un nivel más bajo?

En algunos casos más complejos, podemos querer operar sobre los registros del DataFrame de forma personalizada. Para ello, Spark permite convertirlo a una colección distribuida de objetos Row mediante el método rdd.

Una vez obtenemos el RDD, podemos aplicar transformaciones funcionales como map, flatMap, filter, etc., con una flexibilidad total. Este enfoque es más potente, pero también más bajo nivel, y suele reservarse para tareas que **no pueden resolverse con las herramientas estructuradas de Spark SQL o DataFrames**.

Esta fase de exploración no solo ayuda a entender los datos, sino que es esencial para evitar errores posteriores en el pipeline de *machine learning*, especialmente cuando trabajamos con conjuntos de datos grandes y heterogéneos.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652197_1/scormcontent/assets/INSD_PRDT_U6_Apartado6-2-3_Video1Exploraci%C3%B3n.mp4?v=1)



A continuación haceos otra exploración de otro conjunto de datos de ejemplo pero para recordar cómo se realiza si lo que hacemos es crear un fichero .scla y ejecutarlo directamente:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652197_1/scormcontent/assets/INSD_PRDT_U6_Apartado6-2-3_Video2Exploraci%C3%B3n.mp4?v=1)



A continuación, pasaremos a revisar las **operaciones y transformaciones** más frecuentes que pueden realizarse sobre un DataFrame.



#### Operaciones



Una vez explorados y comprendidos los datos, el siguiente paso en cualquier flujo de trabajo en Spark es **transformarlos**. Las operaciones sobre DataFrames permiten modificar, filtrar, combinar o enriquecer la información de manera declarativa, manteniendo eficiencia y escalabilidad. Recordemos bervemente lo ya estudiado.



- **Elementos clave de la API**  
  La API de Spark para manipulación de datos estructurados se apoya principalmente en tres componentes fundamentales:

  - **Clase Dataset** (org.apache.spark.sql.Dataset): es la abstracción principal que representa una colección de datos estructurados. Técnicamente, un DataFrame no es más que un Dataset[Row], es decir, un conjunto de filas sin tipo específico.
  - **Clase Column** (org.apache.spark.sql.Column): representa una columna individual dentro del DataFrame. Esta clase ofrece métodos muy útiles como:
    - isNull(), isNotNull(), isin(), cast(), alias(), entre otros.
  - **Objeto functions** (org.apache.spark.sql.functions): contiene un extenso repertorio de **funciones listas para aplicar sobre columnas**, cubriendo desde operaciones básicas hasta transformaciones complejas.
- **Funciones comunes del objeto functions**  
  Dentro de este objeto encontramos funcionalidades agrupadas por tipos:

  - **Funciones generales:**
    - col("columna"): referencia directa a una columna.
    - lit(valor): crea una columna constante con ese valor.
  - **Agregaciones:**
    - sum(), count(), min(), max(), variance(), etc.
  - **Funciones sobre colecciones:**
    - array_contains(), sort_array(), size()…
  - **Fechas:**
    - datediff(), unix_timestamp(), from_unixtime()…
  - **Matemáticas:**
    - round(), exp(), log(), pow(), cos()…
  - **Sobre cadenas de texto:**
    - length(), lower(), substring(), trim()...

  Estas funciones son esenciales para aplicar transformaciones limpias, expresivas y eficientes dentro de los pipelines de datos.
- **Operaciones elementales sobre DataFrames**  
  Spark ofrece una serie de métodos que constituyen la base de la transformación de datos:

  - select(): permite seleccionar columnas específicas del DataFrame.
  - filter(): filtra filas según condiciones booleanas.
  - groupBy(): agrupa el DataFrame por una o varias columnas.
  - agg(): aplica funciones de agregación a agrupaciones.
  - when().otherwise(): permite crear columnas condicionales, útil para generar nuevas variables en función de criterios lógicos.
- **Transformaciones frecuentes**  
  Además de filtrar o seleccionar, es habitual realizar operaciones más estructurales como:

  - withColumnRenamed(): cambia el nombre de una columna.
  - withColumn(): crea o sobreescribe una columna aplicando una transformación.
  - join(): combina dos DataFrames, al estilo SQL. Spark permite diferentes tipos de joins:
    - inner, left_outer, right_outer, outer.

  Estas operaciones son esenciales, por ejemplo, para enriquecer un dataset con información externa o combinar varias fuentes de datos.
- **UDFs: nuestras propias funciones**  
  Cuando las funciones incorporadas no cubren una necesidad específica, Spark permite **crear nuestras propias funciones personalizadas**, conocidas como UDFs (*user-defined functions*).

  - Se definen con udf(f), donde f es una función en Python que recibe un valor (o varios) y devuelve un resultado procesado.
  - Estas funciones permiten transformar columnas usando cualquier lógica, incluso devolviendo un tipo de dato diferente.



#### Modelado y evaluación en Spark: Pipelines



En el entorno de Apache Spark, el proceso de entrenamiento de modelos de *machine learning* y su evaluación está profundamente vinculado a una herramienta clave: los **pipelines**. Este mecanismo permite orquestar, de forma estructurada y modular, todas las etapas del flujo de trabajo de modelado: desde la preparación de los datos hasta la predicción y validación del modelo resultante.

El objetivo principal de los pipelines es **automatizar y encadenar las transformaciones y etapas necesarias**, garantizando consistencia entre el entrenamiento y la inferencia, y facilitando su reutilización o despliegue posterior.

La **API de machine learning (ML) de Spark**, accesible desde el paquete org.apache.spark.ml, constituye el núcleo funcional para el desarrollo de modelos en el ecosistema Spark. Esta librería ofrece un conjunto de herramientas diseñadas específicamente para trabajar con datos a gran escala, aplicando técnicas de aprendizaje automático de forma eficiente y escalable sobre estructuras distribuidas como los DataFrames.

Uno de los elementos más representativos de esta API es el concepto de **pipeline**. Un pipeline en Spark puede entenderse como una **cadena o flujo de operaciones** que se aplican secuencialmente sobre los datos. Esta idea está directamente inspirada en la filosofía de trabajo de **scikit-learn**, ampliamente utilizada en entornos locales con Python, y busca facilitar la organización modular y reproducible de un proceso completo de modelado: desde la preparación de los datos hasta la evaluación del modelo.



![image](assets/cm9vk27kp01i1356zz3yf31z3-INSD_PRDT_U6_Apartado6-2-5_Imagen16.jpg)



Cada pipeline parte de un **Dataset**, y su aplicación genera un nuevo Dataset enriquecido con las transformaciones o predicciones correspondientes. Esta abstracción no solo permite una mejor estructuración del código, sino que también garantiza la coherencia entre entrenamiento y predicción, simplifica el mantenimiento y habilita el despliegue automático en producción.



- **Componentes de un pipeline**  
  Un **pipeline** en Spark está compuesto por una secuencia de **etapas** (stages), cada una representando una operación. Estas etapas se dividen en dos tipos:

  - **Transformers**: elementos que transforman un DataFrame de entrada en uno de salida (por ejemplo, normalización, codificación, selección de variables…).
  - **Estimators**: elementos que pueden entrenarse a partir de los datos (como clasificadores o regresores), y que generan transformers una vez entrenados.

  A continuación, se detallan los componentes principales que intervienen en este proceso:
- **Dataset**  
  El *dataset* es el punto de partida de toda pipeline en Spark. Este objeto representa una colección tabular de datos estructurados (como si fuese una tabla), que servirá como entrada para el proceso. A medida que se aplican transformaciones sobre este dataset, se genera una nueva versión del mismo con columnas adicionales, las cuales resultan de aplicar las reglas definidas por los transformadores empleados.
- **Transformer**  
  Los *transformers* son elementos clave dentro de las pipelines, ya que aplican funciones o transformaciones sobre una o varias columnas del dataset. Estas transformaciones pueden ser simples (por ejemplo, concatenar columnas o escalar valores) o complejas (como predecir una variable a partir de otras).

  - El resultado de aplicar un transformer se almacena generalmente en una nueva columna.
  - Para realizar la transformación, se emplea el método .transform(), que aplica la función definida sobre los datos de entrada y produce una nueva estructura enriquecida con la información generada.

  **Tipos de transformers:**

  - **Transformador simple**: realiza una transformación directa sobre una o más columnas. Ejemplo: VectorAssembler, que combina múltiples columnas en un vector.
  - **Modelo**: se refiere a una función aprendida a partir de un proceso de modelado. Ejemplo: MinMaxScaler, KMeans, RandomForest.

  **Ejemplos comunes:**

  - VectorAssembler: crea una columna de tipo array que agrupa todas las columnas especificadas.
  - MinMaxScaler: normaliza una columna en el rango [min, max].
  - StringIndexer: asigna un índice numérico a cada categoría en una columna de tipo string.
  - OneHotEncoder: convierte variables categóricas en vectores binarios.
- **Estimator**  
  Un *estimator* representa una operación que aprende a partir de los datos. A diferencia de un transformer, que aplica una transformación directa, el estimator realiza un proceso de aprendizaje mediante el método .fit().

  - El resultado de aplicar un estimator es un transformer.
  - El método .fit() permite ajustar el estimator a los datos de entrada, encontrando así la función que mejor los representa.

  **Ejemplos:**

  - **MinMaxScaler**: el método .fit() aprende cómo escalar los valores de una columna entre los valores mínimos y máximos especificados.
  - **RandomForest**: el método .fit() entrena un modelo que predice una clase o una probabilidad a partir de características de entrada.

  Por ejemplo: una codificación StringIndexer, un escalado StandardScaler o un modelo LogisticRegression son componentes que pueden encadenarse dentro del pipeline.
- **Evaluación del modelo**  
  Una vez entrenado el modelo, Spark permite evaluarlo a través de distintas métricas, según el tipo de problema (clasificación, regresión…). Las clases evaluadoras más comunes son:

  - BinaryClassificationEvaluator
  - MulticlassClassificationEvaluator
  - RegressionEvaluator

  Estas permiten calcular métricas como **AUC**, **accuracy**, **RMSE**, **R²**, entre otras.

  Además, Spark permite dividir los datos en **conjuntos de entrenamiento y prueba** (train/test split) o aplicar **validación cruzada** mediante clases como CrossValidator, para asegurar la robustez del modelo y evitar el sobreajuste.



1234Ejemplo de flujo típico con pipelineUn flujo típico con pipeline podría tener la siguiente estructura:COMENZAR  1Preprocesamiento de característicasStringIndexer para variables categóricas.VectorAssembler para combinar todas las columnas en un único vector.  2Entrenamiento del modeloLogisticRegression como modelo de clasificación.  3EvaluaciónAplicación de BinaryClassificationEvaluator.  4PredicciónAplicación del pipeline completo sobre nuevos datos.



Esto puede definirse y encadenarse fácilmente en Spark con un ejemplo hecho en pyspark para hacer un guiño a otra asignatura donde lo veis:



```lua
from pyspark.ml import Pipeline

pipeline = Pipeline(stages=[
    indexador,
    ensamblador,
    modelo
])

modelo_entrenado = pipeline.fit(datos_entrenamiento)
predicciones = modelo_entrenado.transform(datos_test)

El equivalente en scala sería:
import org.apache.spark.ml.Pipeline

// Definimos la pipeline con sus etapas (stages)
val pipeline = new Pipeline()
  .setStages(Array(indexador, ensamblador, modelo))

// Entrenamos el modelo con los datos de entrenamiento
val modeloEntrenado = pipeline.fit(datosEntrenamiento)

// Aplicamos el modelo entrenado sobre los datos de test
val predicciones = modeloEntrenado.transform(datosTest)
```



**Explicación:**

- indexador, ensamblador y modelo son instancias de transformadores o estimadores, como StringIndexer, VectorAssembler y RandomForestClassifier.
- datosEntrenamiento y datosTest son de tipo DataFrame.
- La función fit() entrena el pipeline y devuelve un PipelineModel.
- La función transform() aplica la transformación (predicción, en este caso) al conjunto de test.



#### Ventajas del uso de pipelines en Spark



![image](assets/cm9vkbnhr01z8356zzqln3id3-INSD_PRDT_U6_Apartado6-2-5_Imagen18.png)



Todo este engranaje permite construir flujos de trabajo reproducibles, escalables y fáciles de mantener. En otras palabras, se parte de un dataset, se aplican transformers (que pueden ser funciones o modelos entrenados), y mediante el uso de estimators se aprende de los datos. Esto queda perfectamente encapsulado dentro de un objeto pipeline, que es el corazón del sistema de modelado de Spark ML.

Este enfoque modular permite a Spark ML ser una herramienta poderosa no solo para tareas clásicas de aprendizaje automático, sino también para integrarse en arquitecturas de procesamiento de datos distribuidos.



## 6. Ejercicios



### 6.1 Introducción



![image](assets/cm9vkdlp4021s356ze36t86nd-stock-image.jpg)



A continuación, se propone una serie de **ejercicios prácticos diseñados para aplicar los conceptos clave** trabajados a lo largo de la unidad. Estos ejemplos cubren diferentes técnicas de procesamiento, análisis y modelado de datos con Apache Spark, tanto en su módulo SQL como en el de machine learning.

Cada ejercicio plantea un caso concreto, acompañado de una implementación en Scala, que permitirá afianzar el aprendizaje mediante la práctica directa y contextualizada.



### 6.2 Recordatorio Spark SQL (Exploración de datos)



Este completo ejercicio utiliza **Spark SQL** para explorar y analizar en profundidad un conjunto de datos de vinos. A través de 37 preguntas/resoluciones, se abordan técnicas de análisis descriptivo, manejo de nulos, creación de nuevas columnas, agrupaciones, estadísticas por grupo, generación de etiquetas, cálculo de correlaciones, detección de duplicados, y categorizaciones avanzadas. También se realiza una simulación de datos de tiendas que venden vinos, integrando la información mediante joins.

Emplearemos el dataset ya conocido de otros ejercicios winequality-red-white.txt. Las 37 preguntas son:

// 1. Obtener una muestra de ejemplo del DF por pantalla

// 2. Visualizar el esquema o estructura del DF

// 3. Quedarnos sólo con los nombres de la columnas que albergan datos de tipo "double"

// 4. Descripción estadística de las variables “fixed_acidity” y "citric_acid" simultáneamente

// 5. Número de muestras total en el dataset?

// 6. Número de filas distintas en el dataset?

// 7. Hay vinos iguales (i.e., hay filas que se repiten)? (True/False)

// 8. Número de nulos en cada columna

// 9. Cuántos vinos hay de cada tipo: blanco, tinto?

// 10. Comparar tintos vs blancos en términos de acidez (fixed_acidity) y calidad (quality): mean +- std

//    - 10.1. Qué categoría tiende a presentar mayor acidez?

//    - 10.2. En qué categoría los vinos tiendedn a tenr mayor calidad?

// 11. Nueva columna "pcg_free_sulfur_dioxide" con el porcentaje de SO2 (Dióxido de Sulfuro) de tipo libre: col("free_sulfur_dioxide")/col("total_sulfur_dioxide")

// 12. Crear una columna "chloride_per_citric_acid" que represente el nivel de “chlorides” por cada unidad de “citric_acid”. Si el valor de esta última es 0, la columna resultante debe ser -1.0

// 13. Nueva columna con "id" del vino

// 14. Valor medio de “fixed_acidity”?

// 15. Recoger el valor medio de “fixed_acidity” en una variable

// 16. Cuántos vinos hay con un “fixed_acidity” superior a la media?

// 17. Media de fixed_acidity en blancos y tintos? Recoger los datos en un Map[String, Double]

// 18. Nueva columna que recoja, para cada vino, el incremento relativo de fixed_acidity respecto al valor

// 19. En cada categoría, blancos y tintos, cuántos vinos hay con "fixed_acidity" superior al valor medio de esta variable en su categoría?

// 20. Crear una columna flag ("alcohol_label") que identifique tres tipos de vino de acuerdo a su grado de alcohol: low -> (-inf, 9.5), high -> [12.0, inf), medium -> [9.5, 12)

// 21. Promedio de cada una de las variables (numéricas) por cada etiqueta de alcohol?

// 22. Promedio y std de cada una de las variables (numéricas) por cada etiqueta de alcohol? Redondeamos a cifras con 4 decimales

// 23. Mostar en orden descendente las combinaciones de categoría y nivel de alcohol en función de pH medio

// 24. Umbrales de primer y tercer cuartil para la variable "total_sulfur_dioxide"

// 25. Nos quedamos sólo con los vinos que no se repiten

// 26. En qué categoría, blanco o tinto, hay más vinos que no se repiten?

// 27. Para cada tipo de vino, nueva columna etiqueta con el cuartil correspondiente de acuerdo al valor de pH

// 28. Testeando la columna previa: mínimo y máximo de pH por cada tipo de vino y cuartil

// 29. Obtener la matriz de correlaciones

// 30. Ordenar los pares de atributos en orden descendente de acuerdo a la correlación

// 31. Ordenar obviando el signo, es decir, de acuerdo a la magnitud de la correlación

// 32. Capacidad discriminatoria (blanco/tinto) de cada atributo por separado (AUC = Area Under the ROC [Receiver Operating Characteristic] Curve)

// 33. Capacidad discriminatoria (high vs low alcohol) de cada atributo por separado

// 34. Generamos un dataset artificial de tiendas de vino (500 tiendas):

// 35. Número de tiendas por ciudad

// 36. Número de tiendas diferentes por ciudad

// 37.  ¿Cuántos de los vinos iniciales pueden encontrarse en las tiendas?

El siguiente video muestra la solución a este ejercicio, pero solo de los primeros apartados:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652197_1/scormcontent/assets/INSD_PRDT_U6_Apartado7-2_Video3EjercicioVinos1.mp4?v=1)



A continuación, se muestra un video con los siguientes apartados hasta el punto que nos sale un error por no tener ciertas librerías importadas:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652197_1/scormcontent/assets/INSD_PRDT_U6_Apartado7-2_Video4EjercicioVinos2.mp4?v=1)



Finalmente se terminan los apartados restantes tras incluir las importaciones de librerías necesarias que nos causaron error en el paso anterior al no estar presentes. Se puede ver en el siguiente video.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652197_1/scormcontent/assets/INSD_PRDT_U6_Apartado7-2_Video5EjercicioVinos3.mp4?v=1)



### 6.3 Análisis avanzado en la exploración (continuación del ejercicio anterior de vinos)



Este segundo conjunto de ejercicios continúa con el análisis del dataset de vinos, enfocándose en aspectos más avanzados. Incluye detección de outliers por IQR (Interquartile Range) o rango intercuartílico, codificación categórica con StringIndexer y OneHotEncoder, ensamblado de vectores, escalado con MinMaxScaler, aplicación de transformaciones SQL sobre columnas, y finalmente la construcción de un modelo de clustering K-Means con normalización previa, todo integrado en un pipeline. También se analiza la composición de los segmentos resultantes.

Primeramente, cargamos el conjunto de datos de vinos desde un archivo CSV, clasificamos cada muestra según su graduación alcohólica en tres niveles (low, medium, high) mediante una nueva columna alcohol_label, y finalmente identificamos las columnas numéricas double del dataset para su posterior análisis.



```r
val winesdf = spark.read.format("csv").option("header", "true").option("delimiter", "|").option("inferSchema", "true").load("/home/bigdata/Descargas/winequality-red-white.txt")

val alclabelf = winesdf.withColumn("alcohol_label", lit("low")).withColumn("alcohol_label", when(col("alcohol") >= 9.5 && col("alcohol") < 12, "medium").otherwise(col("alcohol_label"))).withColumn("alcohol_label", when(col("alcohol") >= 12, "high").otherwise(col("alcohol_label")))

val double_cols = winesdf.dtypes.filter{case(c, t) => t.equalsIgnoreCase("DoubleType")}.map(_._1)
```



// 1. Aplicar la siguiente regla para identificar valores candidatos a "outliers" por cada variable

// Podremos marcar como puntos anómalos aquellos que tengan la mayoría de sus dimensiones marcadas como outliers

// 1.a) Candidato a outlier variable por variable usando Interquartile Range:

// Regla para la identificación de outiers (IQR = Q3 - Q1):

// -- Cualquier valor por debajo de Q1 – 1.5*IQR

// -- Cualquier valor por encima de Q3 + 1.5*IQR

// Generamos una nueva columna por cada variable de nombre "variable_outlier"

/*approxQuantile:

Calculates the approximate quantiles of a numerical column of a DataFrame.

The result of this algorithm has the following deterministic bound: If the DataFrame has N elements and if we request the quantile at probability p up to error err,  then the algorithm will return a sample x from the DataFrame so that the *exact* rank of x is close to (p * N). More precisely,

floor((p - err) *N) <= rank(x) <= ceil((p + err)* N)

Params:

col – the name of the numerical column

probabilities – a list of quantile probabilities Each number must belong to [0, 1]. For example 0 is the minimum, 0.5 is the median, 1 is the maximum.

relativeError – The relative target precision to achieve (greater than or equal to 0). If set to zero, the exact quantiles are computed, which could be very expensive.

Note that values greater than 1 are accepted but give the same result as 1.

Returns:

the approximate quantiles at the given probabilities

Note:

null and NaN values will be removed from the numerical column before calculation. If the dataframe is empty or the column only contains null or NaN, an empty array is returned.

*/



```r
val out_winesdf = double_cols.foldLeft(winesdf){
	case (acc, c) =>
		val Array(q1, q3) = acc.stat...
		acc.withColumn(c + "_outlier", when(...).otherwise(...)) 
}

out_winesdf.show
```



// 1.b) Por cada muestra, obtenemos el número de dimensiones en las que toma valores anómalos: nos quedamos con aquellas que tengan 3 o más

out_winesdf.withColumn("num_outliers", double_cols...).groupBy("num_outliers").agg(...).show

val clean_winesdf = out_winesdf.withColumn("num_outliers", double_cols...).filter(...)

clean_winesdf.show

////////////////////////////////////////////////////////////////////////////////////////

// 2. Codificación de variables categóricas ("style")

// 2.1. StringIndexer: crear una columna "idx_style"

/*

A label indexer that maps string column(s) of labels to ML column(s) of label indices.

If the input columns are numeric, we cast them to string and index the string values.

The indices are in [0, numLabels).

By default, this is ordered by label frequencies so the most frequent label gets index 0.

The ordering behavior is controlled by setting stringOrderType.



```kotlin
*/
import org.apache.spark.ml.feature.StringIndexer
val idxr = new StringIndexer().setInputCol("alcohol_label").setOutputCol("idx_alcohol_label").fit(alclabelf)
val idxrdf = idxr.transform(alclabelf)
idxrdf.show
idxrdf.select("alcohol_label", "idx_alcohol_label").distinct.show
```



// 2.2. OneHotEncoder: codificamos la columna "idx_style" indexada previamente

/*

A one-hot encoder that maps a column of category indices to a column of binary vectors, with at most a single one-value per row that indicates the input category index.

For example with 5 categories, an input value of 2.0 would map to an output vector of [0.0, 0.0, 1.0, 0.0].

The last category is not included by default (configurable via dropLast), because it makes the vector entries sum up to one, and hence linearly dependent.

So an input value of 4.0 maps to [0.0, 0.0, 0.0, 0.0].

Note:

This is different from scikit-learn's OneHotEncoder, which keeps all categories. The output vectors are sparse.

When handleInvalid is configured to 'keep', an extra "category" indicating invalid values is added as last category. So when dropLast is true, invalid values are encoded as all-zeros vector.

Note:

When encoding multi-column by using inputCols and outputCols params, input/output cols come in pairs, specified by the order in the arrays, and each pair is treated independently.

See also:

StringIndexer for converting categorical values into category indices

*/



```julia
import org.apache.spark.ml.feature.OneHotEncoder
val encdr = new OneHotEncoder()...
val encdrdf = encdr...

//enc_alcohol_label: Vector(size: Int, indices: Array[Int], values: Array[Double])

encdrdf.select("alcohol_label", "idx_alcohol_label", "enc_alcohol_label").distinct.show

import org.apache.spark.ml.linalg._
encdrdf.select("alcohol_label", "idx_alcohol_label", "enc_alcohol_label").distinct.collect.head.getAs[SparseVector](2).toArray
encdrdf.select("alcohol_label", "idx_alcohol_label", "enc_alcohol_label").distinct.collect.last.getAs[SparseVector](2).toArray
```



// 3. Obtener una nueva columna con un vector que incluya, como elementos, los bits de la codificación previa y la columna "fixed_acidity"

/* VectorAssembler:

A feature transformer that merges multiple columns into a vector column.

This requires one pass over the entire dataset.

In case we need to infer column lengths from the data we require an additional call to the 'first' Dataset method, see 'handleInvalid' parameter.

*/



```javascript
import org.apache.spark.ml.feature.VectorAssembler
val vAssembler = new VectorAssembler()...
vAssembler.transform(encdrdf).show
vAssembler.transform(encdrdf).select("alcohol_label", "idx_alcohol_label", "enc_alcohol_label", "fixed_acidity", "myvector").filter(col("alcohol_label")==="high").show
```



// 4. Obtener un nuevo DF a partir de clean_winesdf con la column "fixed_acidity" mapeada en el intervalo [-10, 10]



```markdown
val assembler = new VectorAssembler()...
val assembleddf = assembler.transform(clean_winesdf)
assembleddf.select("fixed_acidity", "vec_fixed_acidity").show
```



/* MinMaxScaler

Rescale each feature individually to a common range [min, max] linearly using column summary statistics, which is also known as min-max normalization or Rescaling.

The rescaled value for feature E is calculated as:

$$ Rescaled(e_i) = \frac{e_i - E_{min}}{E_{max} - E_{min}} * (max - min) + min $$

For the case \(E_{max} == E_{min}\), \(Rescaled(e_i) = 0.5 * (max + min)\).

Note:

Since zero values will probably be transformed to non-zero values, output of the transformer will be DenseVector even for sparse input.

*/



```scala
import org.apache.spark.ml.feature.MinMaxScaler
val min_max_scaler = new MinMaxScaler()...
val scalerdf = min_max_scaler.transform(assemblerdf)
scalerdf.select("fixed_acidity", "scaled_fixed_acidity").show
```



// 5. Obtener un nuevo DF con la column "perc_outliers" con el porcentaje de outliers respecto a las features (columnas de tipo double)

double_cols.size

/*

Implements the transformations which are defined by SQL statement. Currently we only support SQL syntax like 'SELECT ... FROM THIS ...' where 'THIS'

represents the underlying table of the input dataset. The select clause specifies the fields, constants, and expressions to display in the output,

it can be any select clause that Spark SQL supports. Users can also use Spark SQL built-in function and UDFs to operate on these selected columns.

For example, SQLTransformer supports statements like:

SELECT a, a + b AS a_b FROM **THIS**

SELECT a, SQRT(b) AS b_sqrt FROM **THIS** where a > 5

SELECT a, b, SUM(c) AS c_sum FROM **THIS** GROUP BY a, b

*/



```scala
import org.apache.spark.ml.feature.SQLTransformer
val sqlTrans = new SQLTransformer()...
val transformerdf = sqlTrans.transform(scalerdf)
transformerdf.show()
```



// 6.b) Scaler: normalizamos nuestras variables para que tengan desviación típica la unidad y media cero

/*

Standardizes features by removing the mean and scaling to unit variance using column summary statistics on the samples in the training set.

The "unit std" is computed using the corrected sample standard deviation, which is computed as the square root of the unbiased sample variance.

*/



```scala
import org.apache.spark.ml.feature.StandardScaler
val scaler = new StandardScaler()...
val fitted_scaler = scaler.fit(assembler.transform(clean_winesdf))
fitted_scaler.transform(assembler.transform(clean_winesdf)).select("features", "scaled_features").show
```



// 6.c) Clustering: modelo basado en k-means



```bat
import org.apache.spark.ml.clustering.KMeans
val km_model = new KMeans()...
```



// 6.d) Construcción del pipelin



```scala
import org.apache.spark.ml.Pipeline
val pipeline = new Pipeline().setStages(Array(assembler, scaler, km_model))
```



// 6.e) Fit: obtenemos el transformador



```bat
val model = pipeline.fit(clean_winesdf)
```



// 6.f) Transform: aplicamos el transformador



```makefile
val predsdf = model.transform(clean_winesdf)
```



// 6.g) Descripción estadística de las variables en cada cluster



```ini
val col_aggs = double_cols...
predsdf...
```



// 6.h) Contando el número de vinos de cada tipo (tinto/blanco) en cada segmento



```ini
predsdf...
```



// - segmento 2: blancos

// - segmento 0: blancos

// - segmento 1: rojos

En resumen: Este bloque de código construye y aplica un **pipeline de clustering en Spark** utilizando el algoritmo **K-Means**. El proceso incluye la estandarización previa de las variables numéricas con StandardScaler, seguida del entrenamiento de un modelo de K-Means con 3 clusters sobre los datos limpios. Una vez entrenado, se aplica el modelo para predecir el segmento (cluster) al que pertenece cada vino. Posteriormente, se realiza un análisis descriptivo de cada segmento mediante la media de las variables numéricas, y se examina la composición de cada grupo en función del tipo de vino (blanco o tinto), permitiendo así interpretar los clusters generados desde un punto de vista enológico.

El siguiente video muestra la solución:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652197_1/scormcontent/assets/INSD_PRDT_U6_Apartado7-3_Video6EjercicioVinosAvanzado.mp4?v=1)



### 6.4 Modelo de clasificación para detectar el género de una voz



Este código implementa una **aplicación de clasificación automática de voces por género (hombre o mujer)** utilizando Spark MLlib y un modelo de **Random Forest**, aplicado al dataset Voice Gender. A continuación se explica lo que hace, **paso a paso y de forma resumida**:

1.       **Carga y exploración de datos**

- Se carga el dataset voice.csv, que contiene medidas acústicas de voces etiquetadas por género (label).
- Se inspecciona la estructura, distribución por clase y presencia de nulos.
- Se muestran estadísticas básicas de las variables.



```yaml
Puedes utilizar este comando para descargar el fichero: wget -P /home/bigdata/Descargas/ https://gist.githubusercontent.com/mafernandez-stratio/9420a84249cc34daa85af3ac085d1a92/raw/6a4289a3c21d83d9d64016c9b82e33287d835080/voice.csv
```



1. **Preparación de conjuntos de entrenamiento y prueba**

- Se divide el dataset en dos subconjuntos del 50% cada uno (trainingSet y testSet).

1. **Definición del pipeline de clasificación**

- Se ensambla un vector de características (VectorAssembler).
- Se transforma la variable objetivo label en índices numéricos (StringIndexer).
- Se entrena un **Random Forest** con parámetros configurados (50 árboles, maxDepth=10, gini, etc.).
- Se construye una Pipeline con estos pasos.
- Se entrena y evalúa el modelo con BinaryClassificationEvaluator utilizando AUC como métrica.

1. **Evaluación con distintos subconjuntos de variables**

- Se evalúa el rendimiento del modelo **con conjuntos crecientes (take(n)) o desplazados (slice(n, 20))** de las variables acústicas.
- Se imprime la mejor combinación según AUC en el conjunto de test.

**Resultado final**

La aplicación busca identificar **cuáles combinaciones de variables acústicas son más eficaces para predecir el género** de una voz. El output final muestra el subconjunto de características con mayor capacidad predictiva (AUC más alto).

El siguiente video muestra la solución:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652197_1/scormcontent/assets/INSD_PRDT_U6_Apartado7-4_Video7EjercicioClasificaci%C3%B3nVoces.mp4?v=1)



En resumen: En este ejercicio se ha desarrollado un modelo de clasificación para detectar el género de una voz utilizando un conjunto de datos acústicos. Se realiza una exploración inicial, se dividen los datos en entrenamiento y prueba, y se construye un modelo de Random Forest con una pipeline que incluye ensamblado de características y codificación de la etiqueta. También se define una función para evaluar distintos subconjuntos de variables y se calcula el AUC para comparar modelos.



### 6.5 Regresión lineal



Este ejercicio aplica regresión lineal sobre un conjunto de datos deportivos que contiene estadísticas de béisbol. Se analiza la relación entre distintas variables (como carreras anotadas o promedio de bateo) y la variable objetivo SLG (slugging percentage). Se construye un pipeline de transformación con VectorAssembler y StandardScaler, se entrena el modelo y se evalúa con métricas como el error cuadrático medio (MSE) y raíz del error cuadrático medio (RMSE).

El dataset se puede descargar con:

El siguiente video muestra la resolución de este ejercicio:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_PRDT_A/content/_652197_1/scormcontent/assets/INSD_PRDT_U6_Apartado7-5_Video8EjercicioRegresi%C3%B3nLineal.mp4?v=1)



### 6.6 Regresión logística



Aquí se entrena un modelo de regresión logística sobre un dataset de usuarios de una tienda online, con el objetivo de predecir si un usuario compra o no. Se realiza codificación de variables categóricas, ensamblado de características, entrenamiento del modelo y evaluación tanto sobre el conjunto de entrenamiento como de test. Se calcula la matriz de confusión, precisión, recall y exactitud, mostrando también probabilidades y predicciones individuales.

El conjunto de datos que vamos a utilizar en este ejemplo es un conjunto de datos ficticio que contiene un total de 20.000 filas y 6 columnas. Debemos usar 5 variables de entrada para predecir la clase objetivo utilizando un modelo de regresión logística.

Este conjunto de datos contiene información sobre usuarios en línea de un sitio web de venta de artículos deportivos. Los datos recogen el país del usuario, la plataforma utilizada, la edad, si es un visitante recurrente o un visitante nuevo, y el número de páginas web visitadas en el sitio. También incluye información sobre si el cliente terminó comprando el producto o no (estado de conversión).

En esta ocasión se proporciona el código al alumno para que pueda probarlo directamente:



```scala
// Obtener el dataset
// wget -P /home/bigdata/Descargas/ https://gist.githubusercontent.com/mafernandez-stratio/d85a328792e644d6e73dfca76d5f065a/raw/1d18d4a8eea1746aa346f7bbc7932be2919dc197/Log_Reg_dataset.csv

//Lectura dataset
val df = spark.read.option("header", "true").option("inferSchema", "true").csv("/home/bigdata/Descargas/Log_Reg_dataset.csv")


//Exploración
println((df.count(), df.columns.size))
df.printSchema

//number of columns in dataset
df.columns

//view the dataset
df.show(5, false)

// Data Analysis
df.describe().show()
df.groupBy("Country").count().show()
df.groupBy("Platform").count().show()
df.groupBy("Status").count().show()
df.groupBy("Country").mean().show()
df.groupBy("Platform").mean().show()
df.groupBy("Status").mean().show()
//converting categorical data to numerical form
//Indexing
import org.apache.spark.ml.feature._
val search_engine_class = new StringIndexer().setInputCol("Platform").setOutputCol("Platform_Num")
val search_engine_obj = search_engine_class.fit(df)
val df2 = search_engine_obj.transform(df)
df2.show(10,false)


//one hot encoding
val search_engine_encoder = new OneHotEncoder().setInputCol("Platform_Num").setOutputCol("Platform_Vector")
val ohe = search_engine_encoder.fit(df2)
val df3 = ohe.transform(df2)
df3.show(3,false)
df3.groupBy("Platform").count().orderBy(desc("count")).show(5,false)
df3.groupBy("Platform_Num").count().orderBy(desc("count")).show(5,false)
df3.groupBy("Platform_Vector").count().orderBy(desc("count")).show(5,false)

//Indexer
val country_indexer = new StringIndexer().setInputCol("Country").setOutputCol("Country_Num").fit(df3)
val df4 = country_indexer.transform(df3)
df4.select("Country","Country_Num").show(10,false)

//one hot encoding
val country_encoder = new OneHotEncoder().setInputCol("Country_Num").setOutputCol("Country_Vector")
val ohe = country_encoder.fit(df4)
val df5 = ohe.transform(df4)
df5.select("Country","country_Num","Country_Vector").show(10,false)
df5.groupBy("Country").count().orderBy(desc("count")).show(5,false)
df5.groupBy("Country_Num").count().orderBy(desc("count")).show(5,false)
df5.groupBy("Country_Vector").count().orderBy(desc("count")).show(5,false)
df5.printSchema

//assembler
val df_assembler = new VectorAssembler().setInputCols(Array("Platform_Vector","Country_Vector","Age","Repeat_Visitor","Web_pages_viewed")).setOutputCol("features")
val df6 = df_assembler.transform(df5)
df6.printSchema
df6.select("features","Status").show(10,false)

//select data for building model
val model_df = df6.select("features","Status")

//split the data 
val split = model_df.randomSplit(Array(0.75,0.25))
val training_df = split.head
val test_df = split.last
(training_df.count(),test_df.count())
training_df.groupBy("Status").count().show()
test_df.count()
test_df.groupBy("Status").count().show()

//Logistic regression
import org.apache.spark.ml.classification._
val log_reg_class = new LogisticRegression().setLabelCol("Status")
val log_reg_model = log_reg_class.fit(training_df)
//Training Results
val train_results = log_reg_model.evaluate(training_df).predictions
train_results.filter($"Status"===1).filter($"prediction"===1).select($"Status",$"prediction",$"probability").show(10,false)
val correct_preds = train_results.filter($"Status"===1).filter($"prediction"===1).count()
training_df.filter($"Status"===1).count()

//accuracy on training dataset 
correct_preds.toFloat/(training_df.filter($"Status"===1).count())

//Test Set results
val results = log_reg_model.evaluate(test_df).predictions
results.select("Status","prediction").show(10,false)
results.printSchema()
import org.apache.spark.ml.evaluation._

//confusion matrix
val true_postives = results.filter($"Status" === 1 && $"prediction" === 1).count()
val true_postives = results.filter($"Status" === 1 && $"prediction" === 1).count()
val true_negatives = results.filter($"Status" === 0 && $"prediction" === 0).count()
val false_positives = results.filter($"Status" === 0 && $"prediction" === 1).count()
val false_negatives = results.filter($"Status" === 1 && $"prediction" === 0).count()
true_postives+true_negatives+false_positives+false_negatives
results.count()
val recall = (true_postives.toFloat)/(true_postives + false_negatives) //Sensibilidad o Tasa de Verdaderos
val precision = (true_postives.toFloat) / (true_postives + false_positives) //Precisión
val accuracy = ((true_postives+true_negatives) /(results.count())).toFloat //Exactitud
val accuracy = ((true_postives+true_negatives).toFloat /(results.count())) //Exactitud
```



### 6.7 Otro ejemplo con Random forest



En este ejercicio se construye un modelo de clasificación basado en Random Forest para predecir si una persona ha tenido una aventura extramatrimonial, usando un dataset sociológico. Se realiza una exploración profunda de los datos, incluyendo cruces de variables (crosstab) y análisis de correlación por grupos (por religión, hijos, etc.). Se preparan las características, se entrena el modelo, y se evalúa con métricas de clasificación. También se analiza la importancia de cada variable predictora y se guarda el modelo entrenado.

Este código implementa un flujo completo de análisis y modelado predictivo sobre un dataset sociológico relacionado con infidelidades matrimoniales, usando **Apache Spark y Random Forest**. Primero, se carga el conjunto de datos desde un archivo CSV que contiene variables como edad, años de matrimonio, número de hijos, grado de religiosidad y nivel de satisfacción con el matrimonio. A continuación, se realiza un análisis exploratorio, incluyendo estadísticas descriptivas, distribuciones de frecuencia y análisis cruzado entre variables categóricas y la variable objetivo (affairs), que indica si una persona ha tenido o no una aventura.

Luego, se prepara el conjunto de datos para el modelado mediante la creación de un vector de características con VectorAssembler, y se entrena un modelo de **clasificación con Random Forest**. Se evalúa el rendimiento del modelo sobre un conjunto de prueba utilizando métricas como **precisión, exactitud y AUC**, y se analiza la importancia de las variables predictoras. Finalmente, el código destaca un aspecto clave y práctico: **cómo guardar el modelo entrenado en disco (.save) y cargarlo posteriormente (.load) para reutilizarlo**, lo que resulta esencial para entornos de producción o para aplicar el modelo en nuevos datos sin tener que reentrenarlo.



```scala
// wget -P /home/bigdata/Descargas/ https://gist.githubusercontent.com/mafernandez-stratio/f239d29515c745e345741630365a9687/raw/c5862ee5685dbefc269dacdfe29d3d7097cdf3c0/affairs.csv

import org.apache.spark.sql.SparkSession

//val spark = SparkSession.builder().appName("RANDOMFORESTCLASSIFIER").getOrCreate()

//read the dataset
val df = spark.read.option("inferSchema", "true").option("header", "true").csv("/home/bigdata/Descargas/affairs.csv")

//check the shape of the data 
println((df.count(), df.columns.length))
//printSchema
df.printSchema()
//view the dataset
df.show(5)
//Exploratory Data Analysis
df.describe().select("summary", "rate_marriage", "age", "yrs_married", "children", "religious").show()
df.groupBy("affairs").count().show()
df.groupBy("rate_marriage").count().show()
df.groupBy("rate_marriage", "affairs").count().orderBy("rate_marriage", "affairs", "count").show()

def ba(spark_df: org.apache.spark.sql.Dataset[org.apache.spark.sql.Row], colA: String, colB: String): org.apache.spark.sql.DataFrame = {
  val dfP = spark_df.stat.crosstab(colA, colB).toDF()
  val dfPWithRate = dfP.withColumn("affair_rate", dfP("1") / (dfP("1") + dfP("0")))
  dfPWithRate.sort($"${colA}_${colB}")
}

ba(df, "rate_marriage", "affairs").show(10, false)
df.groupBy("religious", "affairs").count().orderBy("religious", "affairs", "count").show()
ba(df, "religious", "affairs").show(10, false)
df.groupBy("children", "affairs").count().orderBy("children", "affairs", "count").show()
ba(df, "children", "affairs").show(10, false)
df.groupBy("affairs").mean().show()

import org.apache.spark.ml.feature.VectorAssembler

val df_assembler = new VectorAssembler().setInputCols(Array("rate_marriage", "age", "yrs_married", "children", "religious")).setOutputCol("features")

val df_with_features = df_assembler.transform(df)
df_with_features.printSchema()
df_with_features.select("features", "affairs").show(10, false)

//select data for building model
val model_df = df_with_features.select("features", "affairs")
model_df.show(5)
val Array(train_df, test_df) = model_df.randomSplit(Array(0.75, 0.25))
println(train_df.count())
train_df.groupBy("affairs").count().show()
test_df.groupBy("affairs").count().show()

import org.apache.spark.ml.classification.RandomForestClassifier

val rf_classifier = new RandomForestClassifier().setLabelCol("affairs").setNumTrees(50).fit(train_df)

val rf_predictions = rf_classifier.transform(test_df)
rf_predictions.show()
rf_predictions.groupBy("prediction").count().show()
rf_predictions.select("probability", "affairs", "prediction").show(10, false)

import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.ml.evaluation.BinaryClassificationEvaluator

val rf_accuracy = new MulticlassClassificationEvaluator().setLabelCol("affairs").setMetricName("accuracy").evaluate(rf_predictions)

println(s"The accuracy of RF on test data is ${rf_accuracy * 100}%")
println(rf_accuracy)

val rf_precision = new MulticlassClassificationEvaluator().setLabelCol("affairs").setMetricName("weightedPrecision").evaluate(rf_predictions)

println(s"The precision rate on test data is ${rf_precision * 100}%")
println(rf_precision)

val rf_auc = new BinaryClassificationEvaluator().setLabelCol("affairs").evaluate(rf_predictions)

println(rf_auc)

// Feature importance
println(rf_classifier.featureImportances)
println(df_with_features.schema("features").metadata.getMetadata("ml_attr").getMetadata("attrs"))

rf_classifier.save("/home/bigdata/Descargas/RF_model2")

import org.apache.spark.ml.classification.RandomForestClassificationModel

val rf = RandomForestClassificationModel.load("/home/bigdata/Descargas/RF_model2")
val model_predictions = rf.transform(test_df)
model_predictions.show()
```



## 7. Conclusiones



### 7.1 Conclusiones de la unidad



Tras haber estudiado el contenido de esta unidad y haber realizado los ejercicios prácticos propuestos, el alumno debería ser capaz de:

- **Comprender** los fundamentos del aprendizaje automático y su papel en la obtención de conocimiento a partir de datos masivos.
- **Distinguir** entre los diferentes tipos de modelos de machine learning (supervisados, no supervisados, etc.) y sus aplicaciones en contextos reales.
- **Evaluar** la idoneidad de Spark ML como herramienta de modelado distribuido frente a otras librerías más especializadas.
- **Dominar** el uso de DataFrames y pipelines en Apache Spark para la preparación, transformación y modelado de grandes conjuntos de datos.
- **Aplicar** técnicas de ingeniería de características, codificación categórica, escalado, y ensamblado de variables dentro de flujos reproducibles.
- **Construir** y evaluar modelos de clasificación, regresión y clustering, utilizando estructuras distribuidas y herramientas avanzadas de evaluación.
- **Interpretar** los resultados obtenidos por los modelos, analizando métricas de rendimiento y su utilidad en términos de negocio o contexto de aplicación.

El dominio de Spark ML representa un paso fundamental para quienes buscan aplicar machine learning en entornos de Big Data. Su enfoque escalable, distribuido y modular permite afrontar proyectos de analítica avanzada con volúmenes de datos que exceden las capacidades del procesamiento tradicional.

Se recomienda que el alumno refuerce lo aprendido experimentando con los **ejercicios prácticos**, ya que estos simulan situaciones reales de análisis predictivo, segmentación y modelado aplicado. La práctica consolidará tanto los conocimientos técnicos como las habilidades para tomar decisiones basadas en datos.

Si al llegar a este punto:

- **Te sientes confiado explicando qué es un modelo de machine learning y cuándo conviene usar uno supervisado o no supervisado.**
- **Puedes construir pipelines en Spark ML que incluyan fases de preprocesamiento, entrenamiento, evaluación y predicción.**
- **Has sido capaz de entrenar modelos sobre datos reales, interpretar resultados y ajustar parámetros según el contexto.**

Entonces, se puede decir que **has alcanzado con éxito los objetivos de esta unidad.**
