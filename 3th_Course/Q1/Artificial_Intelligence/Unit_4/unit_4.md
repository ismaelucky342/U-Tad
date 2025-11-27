# Unidad 4

Creado: 19 de noviembre de 2025 23:17

![image.png](unit_4/image.png)

# **Procesamiento del Lenguaje Natural**

El **Procesamiento del Lenguaje Natural (PLN o NLP en inglés)** es un campo interdisciplinario de la inteligencia artificial y la lingüística computacional que se enfoca en la interacción entre las 
máquinas y el lenguaje humano. Su objetivo principal es desarrollar algoritmos y modelos que permitan a las máquinas comprender, interpretar y generar lenguaje de manera similar a los humanos.

## **Importancia del Procesamiento del Lenguaje Natural**

El uso del PLN ha crecido exponencialmente en los últimos años, gracias a la cantidad masiva de datos de tipo texto y la necesidad de automatizar las tareas relacionadas con el lenguaje.

Desde asistentes virtuales como Siri o Alexa hasta sistemas de traducción automática como Google Translate, las aplicaciones de PLN han transformado la manera en que interactuamos con la tecnología.

Este campo abarca una amplia gama de tareas que van desde el análisis de sentimientos y la clasificación de textos hasta la generación de lenguaje natural y la traducción automática. Algunas de las **aplicaciones** más comunes incluyen:

- Generación de texto
- Traducción automática
- Clasificación de documentos
- Análisis de emociones y sentimientos

## Desafios del PLN

Uno de los principales retos de PLN es la complejidad del lenguaje humano, que está lleno de ambigüedades, ironías y significados contextuales. Las variaciones en gramática, vocabulario y la semántica hacen que el procesamiento del lenguaje no sea una tarea sencilla para las máquinas. Además, las diferencias entre lenguajes y dialectos agregan una capa adicional de dificultad.

Otro desafío importante es la necesidad de comprender el contexto. Los modelos de PLN modernos han avanzado significativamente en esta área gracias al uso de redes neuronales profundas y a técnicas como el aprendizaje por transferencia (Transfer Learning), que hemos visto en la unidad anterior.

![image.png](unit_4/image%201.png)

El procesamiento del lenguaje natural no es un campo nuevo, ya que sus raíces se remontan a los primeros intentos de traducción automática y al desarrollo de los primeros modelos lingüísticos en los años 50 y 60. Sin embargo, los avances recientes en redes neuronales y el auge de los grandes modelos preentrenados como GPT y BERT han revolucionado este campo. 

Estos modelos han permitido obtener resultados sin precedentes en tareas complejas como son la comprensión lectora o la generación de lenguaje coherente.

### Importancia en el campo de la IA

El PLN es una pieza clave en el desarrollo de sistemas de inteligencia artificial que buscan interactuar de manera natural con los humanos. La capacidad de las máquinas para comprender el lenguaje les permite realizar tareas como el reconocimiento de voz, la interpretación de comandos en lenguaje natural y la interacción en conversaciones.

Esto convierte al PLN en una herramienta esencial para la construcción de asistentes inteligentes, sistemas de recomendación y herramientas de análisis semántico.

# Fundamentos del Procesamiento del Lenguaje Natural

El Procesamiento del Lenguaje Natural (PLN) se basa en varios conceptos fundamentales que permiten a las máquinas interpretar, analizar y generar texto. En este apartado, exploraremos algunos de estos conceptos básicos, como la tokenización, la normalización y los modelos de lenguaje. Además, veremos métodos comunes para representar texto, como One-Hot Encoding y TF-IDF.

### Tokenización

Es el proceso de dividir un texto en unidades más pequeñas llamadas tokens. Estos tokens pueden ser palabras, caracteres o sub-palabras, dependiendo del enfoque. La tokenización es uno de los primeros pasos en cualquier tarea de PLN, ya que transforma el texto en una secuencia que puede ser procesada por los algoritmos.

La tokenización basada en palabras consiste en dividir el texto por palabras. Por ejemplo, la frase "Hoy es viernes" se tokenizaría en ["Hoy", "es", "viernes"].

La tokenización basada en caracteres divide el texto en caracteres individuales, y es útil para tareas como la generación de texto. Por ejemplo, "Hoy es" se tokeniza en ['H', 'o', 'y ', 'e', 's', 'v', 'i', 'e ', 'r', 'n', 'e', 's' ].

![image.png](unit_4/image%202.png)

Las sub-palabras se utilizan en modelos como BERT o GPT, donde las palabras raras o largas se dividen en componentes más pequeños, lo que reduce el vocabulario pero mantiene la capacidad de representar palabras desconocidas.

### Normalización

Es el conjunto de técnicas que se aplican para estandarizar el texto antes de su procesamiento. Las técnicas más comunes incluyen:

- Conversión a minúsculas
- Eliminación de signos de puntuación
- Lematización
- Stemming

Estos pasos son esenciales para preparar el texto de manera que pueda ser tratado adecuadamente por los modelos de PLN.

## Modelos de lenguaje Básicos

Un modelo de lenguaje es una representación probabilística que asigna una probabilidad a una secuencia de palabras. Los modelos de lenguaje son fundamentales en tareas como la predicción de la siguiente palabra en una secuencia, la traducción automática o la generación de texto.

A continuación, se describen algunos modelos básicos:

- Modelo de N-Gramas: Es uno de los modelos de lenguaje más simples, que estima la probabilidad de una palabra en función de las N palabras anteriores. Por ejemplo, en un modelo de 2-gramas, la probabilidad de la palabra siguiente se basa en la palabra inmediatamente anterior. Aunque los modelos de N-gramas son intuitivos, tienen limitaciones en cuanto a la cantidad de contexto que pueden manejar.
    
    ![image.png](unit_4/image%203.png)
    
- Modelo basado en redes Neuronales: A medida que la capacidad de procesamiento y los datos aumentaron, los modelos neuronales como las Redes Neuronales Recurrentes (RNN) y las Redes Neuronales Convolucionales (CNN) comenzaron a reemplazar los N-gramas. Estos modelos permiten trabajar con secuencias más largas y aprender representaciones más profundas del lenguaje.
    
    ![image.png](unit_4/image%204.png)
    
- Modelos Basados en transformadores: Los modelos como BERT y GPT están basados en la arquitectura de transformadores, que utilizan mecanismos de atención para modelar relaciones entre palabras a larga distancia en una oración. Estos modelos han llevado a un avance significativo en la capacidad de las máquinas para comprender el contexto y generar texto.
    
    ![image.png](unit_4/image%205.png)
    

## **Representación de Texto**

La representación del texto es un paso clave en el procesamiento del lenguaje natural, ya que los modelos de machine learning no pueden procesar directamente palabras o caracteres como tal. Necesitamos convertir el texto en una forma numérica que los algoritmos puedan entender. 

- One Hot encoding: Es una de las formas más simples de representar texto. En este método cada palabra en el vocabulario se convierte en un vector binario de longitud igual al número de palabras en el vocabulario. Este vector tiene todos sus valores en 0 excepto en la posición correspondiente a la palabra específica, que tiene un valor de 1.
    
    Aunque es fácil de implementar, el One-Hot Encoding tiene las siguientes limitaciones:
    
    - Escalabilidad: si el vocabulario es grande los vectores resultantes pueden ser muy largos y esparcidos (sparse).
    - Falta de relación semántica: no capta relaciones entre palabras. Por ejemplo, en una frase en la que aparecieran "gato" y "perro" estarían
    representadas como vectores ortogonales (sin relación), a pesar de ser
    conceptualmente similares.
- TF-IDF: Es un método mucho mas avanzado que tiene en cuenta tanto la frecuencia de una palabra como la rareza de esa palabra en todo el texto. Lo cual en la práctica ayuda a identificar términos importantes dentro de un doc, como “el” o “la”.
    
    ![image.png](unit_4/image%206.png)
    

# Modelos de Representación de Texto

La representación de texto en Procesamiento del Lenguaje Natural (PLN) ha evolucionado significativamente desde métodos sencillos como el One-Hot Encoding y TF-IDF hasta representaciones más avanzadas que capturan las relaciones semánticas entre palabras. 

## Word Embeddings

Son representaciones vectoriales densas de palabras que capturan relaciones semánticas y contextuales. A diferencia de los enfoques anteriores, como One-Hot Encoding, donde cada palabra está representada de manera independiente, los Word Embeddings permiten que palabras similares en significado estén representadas por vectores cercanos en un espacio multidimensional.

**Word2Vec (Google, 2013):**

- Método para generar representaciones vectoriales de palabras usando una red neuronal superficial.
- **Variantes:**
    - **Skip-Gram:** predice palabras de contexto a partir de una palabra objetivo.
    - **CBOW (Continuous Bag of Words):** predice la palabra central a partir de su contexto.
- **Características:**
    - Captura relaciones semánticas y de género (p. ej., “rey” ≈ “reina”).
    - Permite analogías vectoriales (p. ej., rey − hombre + mujer = reina).

**GloVe (Stanford):**

- Basado en análisis de coocurrencia de palabras, no en redes neuronales.
- Combina información **local** (relaciones cercanas) y **global** (tendencias en todo el corpus).
- Los vectores también permiten analogías y capturan patrones generales de manera eficiente.

**Comparación:**

- Word2Vec aprende relaciones contextuales directas.
- GloVe incorpora estadísticas globales, logrando un enfoque más robusto para capturar tendencias generales.

## Contextual Embeddings

A  medida que la tecnología avanzó, surgió la necesidad de representaciones más sofisticadas que no solo capturaran el significado de las palabras, sino también el contexto en el que se usan. Esto llevó al desarrollo de Contextual Embeddings, donde las representaciones de las palabras cambian dependiendo del contexto en el que aparecen. Los modelos más destacados en esta categoría son **BERT** y **GPT.**

**BERT (Google):**

- Arquitectura: transformadores bidireccionales.
- Representaciones contextuales: ajusta la vectorización de una palabra según su contexto **antes y después**.
    - Ejemplo: "banco" cambia según si se refiere a institución financiera o asiento.
- Entrenamiento: **Masked Language Modeling** (palabras ocultas que el modelo debe predecir).
- Aplicaciones: clasificación de texto, extracción de entidades, respuesta a preguntas.

**GPT (OpenAI):**

- Arquitectura: transformadores unidireccionales (procesa palabras secuencialmente).
- Entrenamiento: predicción de la siguiente palabra en una secuencia.
- Aplicaciones: generación automática de texto, chatbots, respuestas coherentes en diálogo.

**Característica clave de los transformadores:**

- **Atención:** permite al modelo enfocarse en diferentes partes del texto, capturando dependencias a largo plazo y mejorando la comprensión del contexto.

# Redes Neuronales para NLP

Las Redes Neuronales para el Procesamiento del Lenguaje Natural (PLN) se dividen en 2 grandes grupos, por un lado las Long Short-Term Memory (LSTM) y las Gated Recurrent Units (GRU),  fundamentales para resolver tareas de PLN debido a su capacidad de trabajar con secuencias de datos, como texto y voz, manteniendo información contextual a lo largo de la secuencia.

### Redes Neuronales recurrentes

Las RNN son un tipo de red neuronal diseñada para procesar secuencias de datos, como el lenguaje. A diferencia de las redes neuronales tradicionales, las RNN pueden mantener un "estado" interno que les permite recordar información anterior en una secuencia. Esto se logra mediante conexiones recurrentes entre las capas, que permiten que la salida de una neurona se retroalimente en la red, afectando el procesamiento de futuros pasos.

![image.png](unit_4/image%207.png)

En una RNN, cada elemento de la secuencia se procesa uno a uno. La información sobre el procesamiento de elementos anteriores se almacena en una "memoria" interna de la red, que puede influir en la predicción de futuros elementos en la secuencia. Esta propiedad hace que las RNN sean ideales para tareas donde el contexto importa, como en la traducción automática, el reconocimiento de voz o la generación de texto.

A pesar de sus ventajas, las RNN presentan problemas a la hora de capturar dependencias a largo plazo debido al fenómeno conocido como desvanecimiento o explosión del gradiente. En largas secuencias, las señales de error pueden hacerse muy pequeñas o extremadamente grandes durante el entrenamiento, dificultando el ajuste de los pesos.

### **Long Short-Term Memory (LSTM)**

Las LSTM son una mejora sobre las RNN tradicionales. Buscan solucionar los problemas de las dependencias a largo plazo. Las LSTM introducen una estructura de celda más compleja, que incluye puertas de entrada, salida y olvido. Estas puertas permiten a las LSTM aprender cuándo debe recordar o cuándo olvidarse de la información en una secuencia, preservando el contexto importante para tomar decisiones en el futuro.

**estrucutra:**

- **Puerta de olvido:** controla qué información debe descartarse de la memoria.
- **Puerta de entrada:** decide qué nueva información debe ser almacenada en la memoria.
- **Puerta de salida:** determina qué parte de la memoria interna se utiliza para la predicción.

Esta estructura permite a las LSTM recordar información relevante durante largos periodos, lo que las hace útiles para tareas complejas de NLP como la síntesis de texto, análisis de sentimientos y clasificación de secuencias.

**ventajas:**

- Capacidad para aprender dependencias a largo plazo.
- Eficiencia en tareas donde es crucial recordar información de pasos anteriores lejanos.

### **Gated Recurrent Units (GRU)**

Las GRU son una variante más simple de las LSTM. También buscan manejar dependencias a largo plazo en secuencias. A diferencia de las LSTM, las GRU combinan las puertas de entrada y olvido en una sola puerta, lo que las hace computacionalmente más eficientes y más fáciles de entrenar.

- Utilizan una sola puerta de actualización que controla tanto la memoria como la exposición de la memoria al siguiente estado.
- No tienen una celda de memoria separada, como en las LSTM, lo que simplifica su arquitectura.
- Menos parámetros que ajustar, lo que reduce el tiempo de entrenamiento.
- Rendimiento similar a las LSTM en muchas tareas, con una menor carga computacional.

## Modelos basados en atención

Los modelos basados en atención han transformado el PLN al permitir que las redes identifiquen dinámicamente qué partes de un texto son más relevantes, superando las limitaciones de arquitecturas secuenciales tradicionales para capturar dependencias largas. Este mecanismo es fundamental en los Transformers, base de modelos como BERT y GPT, que destacan por su rendimiento en tareas como traducción, generación de texto o análisis de sentimientos. 

> Gracias a la atención, estos modelos pueden manejar contextos complejos y grandes volúmenes de datos con gran eficiencia.
> 

### Mecanismos de atención

El mecanismo de atención permite que un modelo dé más importancia a ciertas partes de la entrada según lo requiera la tarea. En lugar de tratar toda la información igual, calcula puntuaciones que indican qué elementos son más relevantes, aplica un softmax para obtener pesos normalizados y genera una representación contextualizada combinando la entrada según esos pesos.

En RNN, la atención soluciona problemas como la dificultad para manejar dependencias largas, ya que el modelo puede acceder directamente a cualquier parte de la secuencia sin depender solo del estado oculto. Al ponderar dinámicamente la información, el mecanismo mejora la coherencia y precisión de las salidas, volviéndose un componente clave en muchos modelos modernos de PLN.

### Transformers y su arquitectura

Los **Transformers** revolucionaron el PLN al reemplazar las RNN por mecanismos de **atención**, permitiendo procesar secuencias en paralelo y capturar dependencias a largo plazo de forma más eficiente. Su arquitectura se compone de un **codificador** y un **decodificador**, formados por múltiples capas idénticas.

El codificador convierte la secuencia de entrada en una representación interna, mientras que el decodificador genera la salida basándose en esa representación.

Cada capa incluye dos bloques principales:

- **Autoatención**, que relaciona cada posición de la secuencia con todas las demás.
- **Red feed-forward**, que transforma las representaciones obtenidas.

También emplean **conexiones residuales** y **normalización de capa** para mejorar la estabilidad del entrenamiento y facilitar el flujo del gradiente. Estos elementos permiten construir modelos profundos capaces de aprender relaciones complejas en los datos.

## Tareas comunes en NLP

El Procesamiento del Lenguaje Natural se aplica en una amplia gama de tareas, permitiendo a las máquinas interpretar, entender y generar lenguaje humano. A continuación, se describen algunas de las tareas más comunes en NLP.

### Clasificacion de texto

La clasificación de texto es una tarea fundamental en PLN. Consiste en asignar categorías predefinidas a un documento o fragmento de texto. Esta técnica se utiliza en aplicaciones como:

- Filtrado de spam: Clasificar correos electrónicos como spam o no spam.
- Clasificación de noticias: Categorizar noticias en diferentes temas como deportes, política o tecnología…
- Analisis de sentimientos: Clasificar reseñas de productos, opiniones o publicaciones en redes sociales como positivas, negativas o neutrales.

Los enfoques más comunes incluyen modelos de aprendizaje supervisado como Naive Bayes, Support Vector Machines (SVM) y redes neuronales profundas, como LSTM y Transformers.

### Análisis de sentimientos

El análisis de sentimientos es un subtipo de clasificación de texto donde el objetivo es identificar la polaridad emocional del texto (positivo, negativo o neutral). Este tipo de análisis es útil en diversas áreas, como:

- Para analizar reseñas de productos o servicios.
- Para medir la opinión pública sobre un tema o marca.
- Para clasificar las interacciones y poder priorizar las más urgentes.

En esta tarea se pueden utilizar modelos como LSTM que capturan dependencias a largo plazo, o Transformers que pueden manejar grandes secuencias de texto con mayor precisión.

### **Reconocimiento de entidades nombradas (NER)**

El reconocimiento de entidades nombradas es una tarea clave en PLN que consiste en identificar y clasificar entidades dentro del texto en categorías predefinidas como:

- Nombres de individuos.
- Empresas, instituciones gubernamentales o no gubernamentales.
- Lugares geográficos, fechas específicas, etc.

El NER es importante en áreas como la extracción de información y el análisis de documentos jurídicos o financieros. Para realizar esta tarea las redes neuronales recurrentes (RNN), LSTM o los modelos basados en atención como BERT son frecuentes, ya que manejan de manera efectiva la naturaleza secuencial del texto.

## Evaluacion de modelos en NLP

La evaluación efectiva de modelos en el ámbito del Procesamiento del Lenguaje Natural (PLN) es crucial para garantizar que los modelos no solo se ajusten bien a los datos de entrenamiento, sino que también generalicen adecuadamente a nuevos datos. 

### Métricas

En PLN las métricas de evaluación permiten medir el rendimiento de un modelo de manera cuantitativa. Tres de las métricas más comunes son la precisión, el recall y el F1 Score:

- La precisión se refiere a la proporción de verdaderos positivos entre el total de positivos predichos. Es decir, de todos los elementos que el modelo predijo como positivos, cuántos realmente lo son. Se calcula como:
    - Precisión=TP/(TP+FP)
    
    *“donde TP es el número de verdaderos positivos y FP es el número de falsos positivos.”*
    
- El recall mide la proporción de verdaderos positivos detectados entre todos los positivos reales. Se calcula como:
    - Recall = TP/(TP+FN)
    
    donde FN es el número de falsos negativos.El recall es crucial cuando es importante capturar todos los casos positivos, incluso si esto significa que algunos falsos positivos sean incluidos.
    
- Es la media armónica entre la precisión y el recall. Proporciona una única métrica que equilibra ambas, especialmente útil cuando se busca un balance entre precisión y exhaustividad. Se calcula como:
    - F1 Score= 2*((Precisión*Recall)/(Precisión+Recall))
    
    El F1 Score es particularmente útil en contextos donde las clases están desbalanceadas, es decir, cuando hay muchas más instancias de una clase en comparación con la otra.
    

### Validación cruzada

La **validación cruzada** evalúa la capacidad de generalización de un modelo dividiendo los datos en varios subconjuntos o “folds”. En cada iteración, un subconjunto sirve como prueba y el resto como entrenamiento; el rendimiento final se obtiene promediando todas las iteraciones. Esto reduce la variabilidad y proporciona una estimación más fiable del desempeño del modelo.

El **ajuste de hiperparámetros** busca encontrar los valores óptimos de los parámetros que no se aprenden durante el entrenamiento. Se prueban distintas combinaciones mediante métodos como **grid search** o **random search**, optimizando así el rendimiento del modelo, aunque a veces con alto costo computacional.

## Implementación y despliegue de modelos NLP

El despliegue de modelos de Procesamiento del Lenguaje Natural (PLN) en aplicaciones del mundo real es un paso crucial para convertir un modelo entrenado en una herramienta funcional. Esto implica varios retos técnicos, como la integración del modelo en aplicaciones web, su optimización para responder en tiempo real, y su mantenimiento en producción.

### **Integración con aplicaciones web**

Una vez entrenado un modelo de PLN, el siguiente paso es integrarlo en una aplicación para que los usuarios puedan interactuar con él. Esta integración se realiza frecuentemente a través de APIs o servicios web. De esta forma el modelo procesa las entradas del usuario (como texto) y devuelve una predicción (como una clasificación de sentimiento, una respuesta generada automáticamente, etc.).

El flujo general de integración con aplicaciones web suele seguir los siguientes pasos:

- Preprocesamiento de la entrada del usuario: Cuando el usuario ingresa texto se preprocesa de la misma manera que se entrenó el modelo, lo que puede incluir tokenización, eliminación de 
ruido y conversión de palabras en vectores o secuencias de tokens.
- Interacción con el modelo: El texto preprocesado se envía al modelo PLN, que genera una salida basada en su entrenamiento. En este caso, se trata de una predicción que puede
 ser una categoría (por ejemplo, "positivo" o "negativo") o una respuesta en lenguaje natural.
- Postprocesamiento de la salida: Una vez obtenida la salida del modelo, esta se formatea adecuadamente para ser entendida por el usuario o la aplicación que la solicita.
- Integración con front-end: Finalmente el resultado se envía a la interfaz de usuario, como una página web o aplicación móvil.

Para facilitar esta interacción, los modelos de NLP suelen exponerse a través de una API RESTful, lo que permite la comunicación entre el back-end, donde reside el modelo, y el front-end.

### Despliegue en producción

El **despliegue en producción** de un modelo de PLN consiste en ponerlo disponible para responder solicitudes en tiempo real. Los modelos deben ser **rápidos y eficientes**, utilizando compresión o GPU, y capaces de manejar **múltiples solicitudes simultáneas**, con escalabilidad automática mediante herramientas como Kubernetes.

Al exponer el modelo vía **API**, se debe proteger la información de los usuarios y controlar el acceso. Además, es esencial **monitorear el rendimiento** del modelo y actualizarlo periódicamente para mantener su precisión.