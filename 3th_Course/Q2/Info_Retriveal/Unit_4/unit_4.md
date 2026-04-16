# Unidad 4. Modelización y Análisis en Minería de texto con Python.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Descubrimiento De Tópicos: Lda Con Gensim](#2-descubrimiento-de-tópicos-lda-con-gensim)
  - [2.1 Introducción](#21-introducción)
  - [2.2 Fundamentos del modelo LDA (Latent Dirichlet Allocation)](#22-fundamentos-del-modelo-lda-latent-dirichlet-allocation)
  - [2.3 Fundamentos matemáticos](#23-fundamentos-matemáticos)
  - [2.4 Preparación de datos para LDA](#24-preparación-de-datos-para-lda)
  - [2.5 Implementación con la librería Gensim](#25-implementación-con-la-librería-gensim)
  - [2.6 Evaluación y afinación del modelo](#26-evaluación-y-afinación-del-modelo)
  - [2.7 Enlaces de interés](#27-enlaces-de-interés)
- [3. Análisis De Sentimiento Con Textblob O Spacy](#3-análisis-de-sentimiento-con-textblob-o-spacy)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Estrategias para el análisis de sentimiento](#32-estrategias-para-el-análisis-de-sentimiento)
  - [3.3 Análisis de sentimiento con TextBlob](#33-análisis-de-sentimiento-con-textblob)
  - [3.4 Análisis de sentimiento con spaCy](#34-análisis-de-sentimiento-con-spacy)
  - [3.5 Integración y consideraciones](#35-integración-y-consideraciones)
  - [3.6 Enlaces de interés](#36-enlaces-de-interés)
- [4. Introducción Al Parsing De Documentos (Nltk, Spacy)](#4-introducción-al-parsing-de-documentos-nltk-spacy)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Aspectos teóricos](#42-aspectos-teóricos)
  - [4.3 Parsing con NLTK](#43-parsing-con-nltk)
  - [4.4 Parsing con spaCy](#44-parsing-con-spacy)
  - [4.5 Buenas prácticas para el parseo](#45-buenas-prácticas-para-el-parseo)
  - [4.6 Enlaces de interés](#46-enlaces-de-interés)
- [5. Resumen De Textos Con Técnicas Tradicionales](#5-resumen-de-textos-con-técnicas-tradicionales)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Aspectos básicos](#52-aspectos-básicos)
  - [5.3 Métodos de extracción clásicos](#53-métodos-de-extracción-clásicos)
  - [5.4 Enlaces de interés](#54-enlaces-de-interés)
- [6. Conclusiones](#6-conclusiones)
  - [6.1 Conclusiones de la unidad](#61-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad didáctica profundizaremos en las metodologías y técnicas que permiten extraer información de alto nivel a partir de grandes volúmenes de texto. Tras haber cubierto las fases de recolección, limpieza y preprocesado de datos textuales, daremos un paso más al enfocarnos en la modelización y el análisis avanzado de documentos. Para ello, estudiaremos cómo descubrir automáticamente temas latentes con LDA (Latent Dirichlet Allocation), cómo cuantificar la polaridad y subjetividad de un texto mediante análisis de sentimiento, y cómo aplicar técnicas de parsing que mejoren la comprensión y estructuración de la información.

Además, revisaremos métodos de resumen automático de textos, abordando enfoques tradicionales y su utilidad práctica para resumir grandes documentos o generar versiones condensadas de artículos y noticias. En cada uno de estos apartados, se ilustrarán ejemplos en Python con librerías como gensim, TextBlob, spaCy, NLTK y funciones nativas del lenguaje.

Esta unidad pone el foco en la capacidad de trasladar las etapas iniciales de minería de texto (ya vistas en unidades anteriores) a prácticas de descubrimiento de conocimiento y análisis de alto nivel. Con ello, el estudiante estará capacitado para construir pipelines avanzados que aúnen la obtención de datos, el preprocesado y la aplicación de algoritmos de minería y análisis de textos en proyectos reales.



- **Descubrimiento de tópicos: LDA con Gensim**  
  En este apartado, exploraremos en detalle el modelo LDA, sus fundamentos matemáticos, su implementación con gensim y las recomendaciones prácticas para evaluar y optimizar resultados. Además, veremos cómo integrar la técnica de LDA dentro de un flujo de minería de texto más amplio.
- **Anàlisis de Sentimiento con Textblob o Spacy**  
  El análisis de sentimiento parte de la idea de que cada texto (reseña, tuit, comentario, etc.) expresa una actitud que puede ser “positiva”, “negativa” o “neutra”. En ocasiones, se añaden matices como “muy positivo” o “muy negativo”. Además de la polaridad, a veces interesa la subjetividad, que mide si una oración transmite más bien un hecho objetivo o una opinión. Este tipo de análisis ha demostrado su utilidad en marketing (para conocer la reputación de un producto), en política (para medir la aceptación de un candidato), o en periodismo (para ver la tendencia de la prensa acerca de un suceso).
- **Introducción al Parsing de Documentos (NLTK, SPACY)**  
  El parsing se define como el proceso de analizar la estructura gramatical de un texto para comprender cómo se organizan las palabras y las oraciones. A diferencia de otras etapas de la minería de texto que se centran en el significado léxico de las palabras o en su frecuencia, el parsing nos brinda la relación sintáctica entre términos: qué función gramatical cumple cada palabra, cómo se forman los sintagmas nominales, verbales, etc. En aplicaciones de ingeniería de software que manejan documentación o grandes volúmenes de texto, este conocimiento estructural se vuelve esencial para interpretaciones más ricas de la información, como la extracción de relaciones, la normalización semántica o la generación de resúmenes contextualmente coherentes.
- **Resumen de textos con técnicas tradicionales**  
  Tras adentrarnos en el descubrimiento de tópicos (LDA), el análisis de sentimiento (TextBlob, spaCy) y la comprensión sintáctica (parsing en NLTK y spaCy), completamos la visión de modelización y análisis de textos con otro componente esencial: el resumen automático de documentos. Resumir un texto consiste en producir una versión condensada de su contenido, de modo que se conserven las ideas o elementos más importantes sin necesidad de leer el original de forma íntegra. En ingeniería de software y ciencia de datos, la capacidad de resumir informes, artículos extensos, resultados científicos o documentación puede ahorrar tiempo y posibilitar la toma de decisiones sobre grandes corpus.



#### Objetivos



Al concluir esta unidad, el estudiante será capaz de:



1. Comprender las bases de LDA y su implementación con gensim. Conocer la teoría fundamental del modelo LDA para la detección de tópicos. Aplicar correctamente el preprocesado de datos (tokenización, eliminación de stopwords, etc.) con el fin de mejorar la calidad de los tópicos descubiertos. Evaluar la coherencia de los tópicos y optimizar parámetros como el número de tópicos y los hiperparámetros de Dirichlet.
2. Realizar análisis de sentimiento en Python. Emplear librerías como TextBlob o spaCy para determinar la polaridad y subjetividad en textos. Entender la diferencia entre enfoques basados en diccionarios léxicos y modelos estadísticos entrenados. Integrar los resultados de sentimiento con otras etapas de minería de texto (filtrado, clasificación, etc.)
3. Incorporar parsing de documentos y extracción de información detallada. Manejar técnicas más avanzadas de etiquetado gramatical y dependencia sintáctica para refinar la extracción de entidades y relaciones. Evaluar la utilidad de librerías como NLTK y spaCy en tareas de parsing y análisis profundo de oraciones.
4. Explorar métodos de resumen de textos (text summarization). Implementar métodos extractivos básicos (basados en frecuencia de palabras, oraciones clave, etc.). Comprender las fortalezas y limitaciones de los resúmenes tradicionales frente a los sistemas basados en modelos de lenguaje más avanzados.
5. Diseñar un pipeline cohesivo de análisis. Combinar las distintas técnicas (LDA, sentimiento, parsing, resúmenes) para extraer información sintética y relevante a partir de un corpus extenso. Evaluar la escalabilidad y viabilidad de estos métodos en distintos escenarios profesionales o de investigación.



## 2. Descubrimiento De Tópicos: Lda Con Gensim



### 2.1 Introducción



![image](assets/cm8ddyukb0059356yneb32sqk-stock-image.jpg)



Cuando hablamos del descubrimiento de tópicos, o topic modeling en inglés, nos referimos a una técnica que nos permite agrupar documentos o fragmentos de texto en función de los temas que están presentes en su contenido, sin necesidad de que estos temas estén previamente etiquetados. Es decir, se identifican agrupaciones latentes dentro del corpus para así caracterizarlo y entenderlo de manera más eficiente.

Uno de los modelos más conocidos y ampliamente utilizados para el descubrimiento de tópicos es LDA (Latent Dirichlet Allocation). LDA asume que:

- Cada documento está compuesto por una mezcla de tópicos latentes.
- Cada tópico es, a su vez, una distribución de palabras.

Gracias a esto, se puede inferir qué proporción de cada tema hay en cada documento, y qué palabras caracterizan mejor a cada tema. En Python, la librería gensim se ha consolidado como una herramienta estándar para implementar LDA y otras técnicas de modelado de temas.

En este apartado, exploraremos en detalle el modelo LDA, sus fundamentos matemáticos, su implementación con gensim y las recomendaciones prácticas para evaluar y optimizar resultados. Además, veremos cómo integrar la técnica de LDA dentro de un flujo de minería de texto más amplio.



### 2.2 Fundamentos del modelo LDA (Latent Dirichlet Allocation)



El objetivo de LDA es explicar cómo cada documento puede ser visto como una combinación (distribución) de varios temas latentes, y cómo cada tema (topic) está descrito por un conjunto característico de palabras. LDA modela cada documento como una distribución de tópicos (por ejemplo, 40% tópico A, 30% tópico B, 30% tópico C). Además, cada tópico se modela como una distribución de palabras (p. ej., el tópico A se caracteriza por palabras como “machine”, “learning”, “algorithm”, “model”, etc.).



![image](assets/cm8decz1i009f356yknjruggk-INSD_BAIN_U4_Imagen1.png)



Cabe destacar que LDA no opera con la secuencia real de palabras, sino con la clásica aproximación de “bolsa de palabras” (bag-of-words), donde el orden no se considera relevante. En este marco, cada término se elige fundamentalmente en función del tema que le ha sido asignado. En la práctica, no conocemos por adelantado cuántos temas existen ni cómo se reparten en el corpus, de manera que LDA asume un proceso generativo subyacente y procede a inferirlo a partir de los textos.



### 2.3 Fundamentos matemáticos



A nivel de matemáticas, el LDA se fundamenta en las distribuciones Dirichlet para generar las “mezclas” de tópicos en cada documento.

Una distribución de Dirichlet es una función que asigna la probabilidad total de lo que hemos definido como documento previamente (visualizada como una “porción”, “rebanada” o fracción del total)   a distintos segmentos (en este caso, los tópicos). Si, por ejemplo, decidimos que nuestro modelo tendrá 𝐾 tópicos, la distribución de Dirichlet se encarga de especificar cómo podrían variar las proporciones 𝜃=(𝜃1,𝜃2,…,𝜃𝐾) que suman 1 y que indican en qué medida un documento mezcla cada tema.

Los hiperparámetros de LDA, 𝛼 y 𝛽 (o 𝜂), gobiernan esas distribuciones de Dirichlet. Concretamente, 𝛼 controla cuán concentrada o dispersa está la proporción de tópicos dentro de cada documento, mientras que 𝛽 hace lo propio con la distribución de palabras dentro de cada tópico. Si 𝛼 es grande, los documentos tienden a presentar mezclas más homogéneas de temas (abarcando varios tópicos de forma equilibrada). Por el contrario, si 𝛼 es pequeña, los documentos tienden a concentrar muy fuertemente un par de tópicos principales, y apenas un atisbo de otros. De modo análogo, al variar 𝛽 se regula si los tópicos tienden a incluir muchas palabras frecuentes de forma equilibrada o si, al contrario, se muestran dominados por un subconjunto más reducido de términos.

De forma resumida, el proceso generativo se formula como:

- Para cada documento, se toma una distribución de tópicos 𝜃 a partir de una Dirichlet 𝛼
- Para cada palabra de ese documento, se elige un tópico 𝑧 de acuerdo con 𝜃. A continuación, se escoge una palabra 𝑤 a partir de la distribución 𝜙𝑧 del tópico 𝑧

En la práctica, LDA infiere el proceso inverso: partimos de los documentos (ya escritos y terminados) y, mediante algoritmos de muestreo o métodos variacionales, estimamos qué distribución de temas corresponde a cada documento y qué palabras caracterizan cada tópico.



![image](assets/cm8deg05q00bt356yt7e78l6c-INSD_BAIN_U4_Imagen2.jpg)



### 2.4 Preparación de datos para LDA



Dado que LDA es sensible al ruido y a la calidad de la información, es fundamental preprocesar y vectorizar el texto adecuadamente como ya vimos en unidades anteriores. Este proceso suele incluir:



![image](assets/cm8dei8m100d6356y30268cda-INSD_BAIN_U4_Imagen3.png)

- **Tokenización y normalización**  
  Se separan los documentos en tokens, se convierten a minúsculas y se eliminan caracteres no deseados.
- **Eliminación de stopwords**  
  Se retiran palabras de uso tan frecuente que no contribuyen a la distinción temática (por ejemplo, “the”, “and”, “de”, “que”, etc.)
- **Lematización o stemming**  
  Se reduce cada palabra a su raíz o forma canónica, de modo que “plays”, “played” y “playing” puedan unificarse como “play”.
- **Construcción de diccionario**  
  Se asigna un ID a cada término. Así podemos manejar la correspondencia entre IDs y palabras de manera más compacta, usando librerías como gensim para crear un objeto Dictionary.
- **Generación de la matriz bag-of-words (o TF-IDF)**  
  Cada documento se representa como un vector que contiene la cuenta (o la importancia, si se utiliza TF-IDF) de cada palabra. LDA, de forma tradicional, parte de la representación bag-of-words.



Tras estos pasos, ya se cuenta con un conjunto de documentos vectorizados que puede alimentarse al modelo de LDA para estimar los tópicos.



### 2.5 Implementación con la librería Gensim



#### 1. Introducción e instalación



La librería gensim es una de las más utilizadas en Python para el modelado semántico, ya que ofrece métodos muy sencillos para entrenar, evaluar y desplegar LDA, Word2Vec y otras técnicas de procesamiento de lenguaje.

Lo primero que debemos hacer para instalar la librería es:



```dockerfile
pip install gensim
```



En un escenario real, podríamos tener un corpus grande con noticias, reseñas o artículos científicos. En este caso, a modo de ejemplo, crearemos un archivo llamado text_mining.txt con pocas líneas, cada una representando un documento corto. Por ejemplo:



```markdown
La ciencia e ingeniería de datos con Python es un campo en crecimiento
En la Utad estoy aprendiendo sobre ellos mediante Python
Me encanta leer sobre la ingeniería de datos con Python
La inteligencia artificial está evolucionando rápidamente en la ciencia de datos
Python se utiliza en el análisis de datos y la ingeniería de datos
```



#### 2. Procesado y creación del direccionario



El primer paso es limpiar y normalizar los textos (eliminando símbolos, aplicando minúsculas, etc.) y transformar las oraciones en listas de tokens. Posteriormente, con gensim, creamos un diccionario, que asigna a cada palabra un identificador único.

Por ejemplo, podríamos utilizar el siguiente código:



```python
import nltk
import re
from gensim import corpora
from gensim.utils import simple_preprocess

nltk.download('stopwords')
from nltk.corpus import stopwords

# Creamos stopwords en inglés
stop_words = set(stopwords.words('spanish'))

def preprocess_text(text):
    text = text.lower()
    # Eliminmos caracteres especiales y números
    text = re.sub(r'[\W_]+', ' ', text)
    # Tokenizamos el texto, con deacc=False mantenemos las tildes
    tokens = simple_preprocess(text, deacc=False)
    # Eliminamos stopwords
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Procesamos los documentos
documents = []
# Usamos encoding para asegurar que se procesa bien al estar en español
with open("text_mining.txt", "r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            print(f"Creating document: {line}")
            documents.append(preprocess_text(line))

# Creamos el diccionario con un ID para cada palabra única
dictionary = corpora.Dictionary(documents)
# Accedemos al diccionario
print(f"Data dictionary: {dictionary.token2id}")


# Output
Creating document: La ciencia e ingeniería de datos con Python es un campo en crecimiento
Creating document: En la UTad estoy aprendiendo sobre ellos mediante Python
Creating document: Me encanta leer sobre la ingeniería de datos con Python
Creating document: La inteligencia artificial está evolucionando rápidamente en la ciencia de datos
Creating document: Python se utiliza en el análisis de datos y la ingeniería de datos
Data dictionary: {'campo': 0, 'ciencia': 1, 'crecimiento': 2, 'datos': 3, 'ingeniería': 4, 'python': 5, 'aprendiendo': 6, 'mediante': 7, 'utad': 8, 'encanta': 9, 'leer': 10, 'artificial': 11, 'evolucionando': 12, 'inteligencia': 13, 'rápidamente': 14, 'análisis': 15, 'utiliza': 16}
```



Este diccionario es esencial para luego convertir cada documento en formato bag-of-words.



#### 3. Generar el corpus (bag-of-words)



Una vez creado el diccionario, podemos transformar cada documento en una lista de pares (word_id, count), con la función doc2bow().

Añadiendo al final del código anterior obtendremos para cada documento, en función del id de la palabra, cuantas veces aparece.



```markdown
corpus_bow = [dictionary.doc2bow(doc) for doc in documents]
print(f"Bag of words: {corpus_bow}")
# Output
Bag of words: [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)], [(5, 1), (6, 1), (7, 1), (8, 1)], [(3, 1), (4, 1), (5, 1), (9, 1), (10, 1)], [(1, 1), (3, 1), (11, 1), (12, 1), (13, 1), (14, 1)], [(3, 2), (4, 1), (5, 1), (15, 1), (16, 1)]]
```



Por ejemplo, en el último documento del apartado anterior, vemos como la palabra con id igual a 3 (“datos”) aparece 2 veces. Sabiendo que la frase era “Python se utiliza en el análisis de datos y la ingeniería de datos”, podemos validar que es correcto.

Ahora tenemos, en corpus_bow, la versión vectorizada del conjunto de documentos, lista para alimentar al modelo de LDA.



#### 4. Entrenamiento del modelo LDA



Para entrenar LDA en gensim, debemos crear un objeto LdaModel al que le pasaremos el corpus y el diccionario, junto con parámetros como num_topics (número de tópicos que se desea extraer), passes (número de iteraciones sobre el corpus) y otros.

Por ejemplo, si queremos extraer 3 temas o tópicos del corpus anterior:



```python
from gensim.models.ldamodel import LdaModel

num_topics = 2
lda_model = LdaModel(
    corpus=corpus_bow,
    id2word=dictionary,
    num_topics=num_topics,
    random_state=42,
    passes=10,
    update_every=1,
    chunksize=100,
    alpha='auto',
    per_word_topics=True
)

for idx, topic in lda_model.show_topics(formatted=False, num_words=5):
    print(f"Tópico #{idx}: {[w for w, _ in topic]}")
# Output
Tópico #0: ['datos', 'python', 'ingeniería', 'ciencia', 'crecimiento']
Tópico #1: ['inteligencia', 'rápidamente', 'evolucionando', 'artificial', 'ciencia']
```



Algunos parámetros relevantes son alpha y eta (o beta), parámetros de Dirichlet, que controlan la concentración de la distribución de tópicos y de palabras. Establecerlos en “auto” deja que gensim ajuste heurísticamente dichos valores. En un corpus real, además, es habitual experimentar con distintos valores de num_topics y passes para buscar el equilibrio entre fidelidad y eficiencia.



#### 5. Obtener la distribución de tópicos para un documento



El siguiente paso será conocer las proporciones en las que un documento pertenece a los tópicos identificados.

Para ello, será tan sencillo como usar .get_document_topics() para obtener para cada documento qué distribución tiene:



```python
for doc_idx, doc_bow in enumerate(corpus_bow):
    topics_distribution = lda_model.get_document_topics(doc_bow, minimum_probability=0.0)
    print(f"Document {doc_idx} topics distribution: {topics_distribution}")
# Output
Document 0 topics distribution: [(0, 0.97821593), (1, 0.021784013)]
Document 1 topics distribution: [(0, 0.9688258), (1, 0.031174237)]
Document 2 topics distribution: [(0, 0.9743733), (1, 0.025626708)]
Document 3 topics distribution: [(0, 0.08547968), (1, 0.9145203)]
Document 4 topics distribution: [(0, 0.97824097), (1, 0.021759018)]
```



De esta forma, podemos ver que el último documento que era “Python se utiliza en el análisis de datos y la ingeniería de datos” se le asigna un 97.8% al tópico 0 (Tópico #0: ['datos', 'python', 'ingeniería', 'ciencia', 'crecimiento']) y un 2.2% al tópico 1 (Tópico #1: ['inteligencia', 'rápidamente', 'evolucionando', 'artificial', 'ciencia']).



### 2.6 Evaluación y afinación del modelo



#### 1. Métricas: perplexity y coherencia



Para saber si un modelo LDA está funcionando adecuadamente, se echa mano de ciertas métricas. Una opción clásica es la perplexity, que mide la capacidad de predecir nuevas palabras, pero no siempre correlaciona con la interpretabilidad. Otra alternativa muy usada es la coherencia de tópicos (topic coherence), que evalúa qué tan consistentemente se agrupan las palabras más importantes de cada tema. Librerías como gensim permiten calcular la coherencia de forma sencilla:



```python
from gensim.models import CoherenceModel

coherence_model_lda = CoherenceModel(
    model=lda_model, 
    texts=documents, 
    dictionary=dictionary, 
    coherence='c_v'
)
coherence_score = coherence_model_lda.get_coherence()
print(f"Coherencia: {coherence_score}")
# Output
Coherencia: 0.454470580963248
```



Un valor de coherencia mayor suele indicar que los tópicos presentan conjuntos de palabras más “lógicos” o coherentes. Es común iterar con diferentes num_topics o hiperparámetros para buscar la máxima coherencia posible sin impactar demasiado en el rendimiento.

Si hacemos un análisis, por ejemplo, para obtener la variación de la coherencia en función del número de tópicos, vemos como en nuestro caso no varía debido al tamaño tan reducido de nuestro texto.



```python
import matplotlib.pyplot as plt
from gensim.models.ldamodel import LdaModel
from gensim.models import CoherenceModel

# Definimos un rango de tópicos
k_values = range(1, 10)
coherence_scores = []

for k in k_values:
    print(f"Entrenando LDA con K={k} tópicos...")
    lda_model = LdaModel(
        corpus=corpus_bow,
        id2word=dictionary,
        num_topics=k,
        random_state=42,
        passes=10,
        update_every=1,
        chunksize=100,
        alpha='auto',
        per_word_topics=True
    )
    
    # Calculamos la coherencia del modelo
    coherence_model_lda = CoherenceModel(
        model=lda_model, 
        texts=documents, 
        dictionary=dictionary, 
        coherence='c_v'
    )
    coherence_score = coherence_model_lda.get_coherence()
    coherence_scores.append(coherence_score)
    print(f"Coherencia para K={k}: {coherence_score}")

# Graficar la coherencia en función del número de tópicos
plt.figure(figsize=(10, 6))
plt.plot(k_values, coherence_scores, marker='o')
plt.xlabel("Número de Tópicos (K)")
plt.ylabel("Coherencia (c_v)")
plt.title("Variación de la Coherencia en función de K")
plt.xticks(k_values)
plt.grid(True)
plt.show()
```



La gráfica resultante de este análisis sería algo como:



![image](assets/cm8df5t9a00wt356y98vr1vy5-INSD_BAIN_U4_Imagen4.png)



Por el contrario, si miramos la siguiente gráfica de un estudio más detallado con un tamaño de corpus mucho mayor vemos una variabilidad significante.



![image](assets/cm8df6jft00y6356ydfk2wu7n-INSD_BAIN_U4_Imagen5.png)



Estas prácticas son útiles para identificar cual es la configuración más adecuada para nuestro caso y garantizar precisión y rendimiento.

La perplexity es otra métrica utilizada para evaluar modelos. A diferencia de la coherencia, un valor menor de perplexity indica un mejor desempeño del modelo. De igual manera, podemos usar gensim para obtener su valor:



```ini
perplexity = lda_model.log_perplexity(corpus_bow)
print(f"Perplexity: {perplexity}")
# Output
Perplexity: -3.973405994750835
```



Es importante remarcar que en gensim, la función log_perplexity devuelve el logaritmo de la perplexity. Para obtener la perplexity real, se puede calcular exponencial del valor obtenido con librerías como numpy de la siguiente forma:



```bat
import numpy as np

log_perplexity = lda_model.log_perplexity(corpus_bow)
perplexity = np.exp(-log_perplexity)
print(f"Perplexity: {perplexity}")
# Output
Perplexity: 53.165303084824615
```



Es importante equilibrar ambas métricas, ya que un modelo con baja perplexity podría no ser necesariamente el más interpretable, y viceversa. Por lo tanto, la selección final del número de tópicos y los hiperparámetros debe considerar tanto la perplexity como la coherencia para asegurar un modelo equilibrado entre rendimiento e interpretabilidad.



#### 2. Visualización con pyLDAvis



Además de estas métricas, es muy útil explorar interactivamente el espacio de tópicos. La librería pyLDAvis genera un panel donde cada tópico se ve como una burbuja, y al hacer clic se pueden ver las palabras asociadas.

Para instalarla simplemente deberemos ejecutar conforme a nuestro sistema operativo:



```bat
pip install pyLDAvis
```



Y posteriormente en nuestro notebook:



```python
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis

pyLDAvis.enable_notebook()
visualization = gensimvis.prepare(lda_model, corpus_bow, dictionary)
pyLDAvis.display(visualization)
```



Se obtiene una representación que facilita la interpretación de los tópicos y su solapamiento.



![image](assets/cm8dfer5w015n356yh5yts3tw-INSD_BAIN_U4_Imagen6.png)



En el próximo video, veremos cómo sería un pipeline completo con todas las etapas para la creación y evaluación de un modelo:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651986_1/scormcontent/assets/INSD_BAIN_U4_Video1.mp4?v=1)



### 2.7 Enlaces de interés



> Documentación oficial de gensim
>
> [Link](https://radimrehurek.com/gensim/)

> Modelado y visualización de tópicos
>
> [Link](https://neptune.ai/blog/pyldavis-topic-modelling-exploration-tool-that-every-nlp-data-scientist-should-know)



## 3. Análisis De Sentimiento Con Textblob O Spacy



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



La minería de texto no solo busca clasificar documentos por temas (como en el caso de LDA), sino también determinar la opinión o la emoción subyacente en un texto. Esta tarea se conoce como análisis de sentimiento (sentiment analysis) y resulta crucial para aplicaciones como la monitorización de redes sociales, la satisfacción del cliente, o la evaluación de reseñas y noticias. En este apartado estudiaremos distintas aproximaciones para cuantificar la polaridad (positivo, negativo o neutro) y la subjetividad de un texto, y veremos cómo implementarlas en Python utilizando TextBlob o spaCy. También discutiremos algunas recomendaciones para integrarlo en un pipeline de minería de texto que, tras el preprocesado, sea capaz de identificar la orientación emocional o de opinión de un conjunto de documentos.

El análisis de sentimiento parte de la idea de que cada texto (reseña, tuit, comentario, etc.) expresa una actitud que puede ser “positiva”, “negativa” o “neutra”. En ocasiones, se añaden matices como “muy positivo” o “muy negativo”. Además de la polaridad, a veces interesa la subjetividad, que mide si una oración transmite más bien un hecho objetivo o una opinión. Este tipo de análisis ha demostrado su utilidad en marketing (para conocer la reputación de un producto), en política (para medir la aceptación de un candidato), o en periodismo (para ver la tendencia de la prensa acerca de un suceso).

Existen diversas estrategias para llevarlo a cabo:

- Basadas en diccionarios léxicos con palabras previamente clasificadas por su connotación (por ejemplo, “excelente” = +2, “malo” = -2, y así sucesivamente).
- Apoyadas en modelos estadísticos entrenados a partir de grandes corpus etiquetados.



### 3.2 Estrategias para el análisis de sentimiento



#### Estrategias basadas en diccionarios léxicos



En este caso, cada palabra del texto se asocia a un puntaje de “positividad” o “negatividad” (a veces valores intermedios). Para estimar el sentimiento general, se suman o promedian esos puntajes. Si predominan palabras con connotación positiva (“excelente”, “fantástico”), la polaridad final será alta; si abundan términos negativos (“terrible”, “lamentable”), la polaridad bajará. Este método es muy directo y no requiere entrenar modelos, por lo que se puede aplicar incluso cuando no hay un conjunto etiquetado disponible.

Sin embargo, es vulnerable a problemas como la ironía. Por ejemplo, la frase “¡Excelente, me encanta que se bloquee la app cada 30 segundos!” podría puntuar en diccionarios léxicos como positiva por la palabra “excelente” y “encanta”. La falta de contexto impide capturar el sarcasmo. Además, cada idioma y cada dominio (finanzas, salud, tecnología, etc.) necesita su propio diccionario cuidadosamente elaborado.

Si se elige este método, conviene ajustar el diccionario a la temática en cuestión. Por ejemplo, si la palabra “carga” en un contexto de telefonía es positiva cuando habla de “rapidez de carga”, en cambio en un contexto de software “carga” puede ser neutra o negativa.



#### Estrategias basadas en modelos entrenados



El enfoque supervisado asume que contamos con un corpus etiquetado (por ejemplo, miles de tuits marcados como “positivo”, “negativo”, “neutro”). Con estos datos, se entrenan clasificadores que aprenden patrones de correlación entre n-gramas, embeddings o características léxicas, y la etiqueta de sentimiento. Así, el sistema no se basa en listas de palabras fijas, sino que se adapta a los ejemplos y puede captar combinaciones de términos, contexto y expresiones idiomáticas.

Herramientas como spaCy permiten entrenar su componente de clasificación de texto (TextCategorizer) con datos. De esta manera, el modelo resultante puede ser más robusto que un enfoque puramente léxico, aunque requiere el esfuerzo de reunir y etiquetar datos o descargar un modelo preentrenado adecuado.

Veamos a continuación cómo influye el tipo de estrategia en función de un texto que pueda ser complejo por contener sarcasmo:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651986_1/scormcontent/assets/INSD_BAIN_U4_Video2.mp4?v=1)



A la hora de decidir qué estrategia seguir, hay que tener numerosos criterios en cuenta, analicemos estos criterios:

|  | Diccionarios léxicos | Modelos supervisados |
| --- | --- | --- |
| Dependencia de datos etiquetados | No requiere un corpus pre-etiquetado. Se basa en un conjunto de palabras y sus puntajes (positivos/negativos). | Requiere ejemplos etiquetados (positivos, negativos, etc.) para entrenar un clasificador. Sin estos datos, el método no funciona. |
| Facilidad de implementación | Muy sencillo: basta con disponer de una lista de palabras y valores de sentimiento. Suma o promedio dan la polaridad final. | Más complejo: se necesita la fase de entrenamiento, ajuste de hiperparámetros y validación con un conjunto de pruebas. |
| Adaptación al dominio | Limitada: el diccionario puede no reflejar usos específicos o palabras de jerga. Requiere personalización manual para cada área de aplicación. | Más flexible: el modelo aprende patrones de un corpus real y puede descubrir relaciones de palabras contextuales. Puede ser más robusto ante ironías y expresiones propias del dominio. |
| Interpretación | Alta interpretabilidad: se puede ver fácilmente qué palabras aportan polaridad positiva o negativa. | A menudo más opaco: el modelo estadístico define pesos en función de los datos de entrenamiento, pudiendo ser menos transparente. |
| Rendimiento en matices sutiles | Bajo rendimiento ante sarcasmos, negaciones complejas o lenguaje muy contextual. | Suele ser mejor captando matices, siempre que el corpus de entrenamiento sea adecuado y represente esos matices. |
| Escalabilidad | Computacionalmente ligero, no requiere entrenamiento previo. | Entrenamiento puede ser costoso (depende del tamaño del corpus y tipo de modelo). La predicción en ejecución es ágil, aunque el paso previo de entrenamiento es más exigente. |
| Requerimientos de recursos | Básicos: un diccionario por idioma. Menos dependiente de la calidad de GPU/CPU. | Altos si se entrena un modelo grande o se usan métodos de deep learning. Puede requerir GPU para mejorar tiempos de entrenamiento. |
| Ejemplo de librerías | TextBlob (modo por defecto), VADER (para inglés), herramientas léxicas específicas. | spaCy con un componente TextCategorizer, Transformers (Hugging Face), sklearn (clasificadores SVM, Naive Bayes, etc.). |



### 3.3 Análisis de sentimiento con TextBlob



#### 1. Introducción e instalación



TextBlob es una librería de Python diseñada para simplificar tareas de NLP. Nos ofrece una interfaz intuitiva y accesible. Esta herramienta nos permite realizar operaciones como la tokenización, lematización, traducción y, de manera destacada, el análisis de sentimiento.

El análisis de sentimiento con TextBlob se basa en un enfoque léxico que evalúa la polaridad y subjetividad de las expresiones textuales, proporcionando una medida cuantitativa de las opiniones y emociones presentes en los datos. Su facilidad de uso y eficacia la convierten en una opción popular para proyectos académicos y profesionales en ingeniería de software, donde la interpretación de datos textuales es crucial para el desarrollo de aplicaciones inteligentes y centradas en el usuario.

Además, TextBlob es popular por su sencillez y por basarse en “pattern” (un léxico para inglés).

Su instalación, al igual que el resto de las librerías de Python, es sencilla. Simplemente deberemos ejecutar en función de nuestro sistema operativo:



```bat
pip install textblob
```



#### 2. Aspectos básicos



Como se ha comentado previamente, el análisis de sentimiento es un método para determinar la orientación emocional de un texto, es decir, si es positivo, negativo o neutral, y con qué intensidad se expresa dicha emoción. Además, también se suele estimar la subjetividad, que indica hasta qué punto una frase se basa en juicios o apreciaciones personales en lugar de hechos objetivos. Conviene recordar que la polaridad se acostumbra a representar con un valor continuo entre -1 y +1 (muy negativo a muy positivo), mientras que la subjetividad suele expresarse entre 0 y 1 (completamente objetiva a totalmente subjetiva).

TextBlob proporciona un enfoque rápido y sencillo para obtener estos valores, fundamentándose principalmente en diccionarios léxicos.

Una vez instalado, su uso es muy sencillo, simplemente deberemos acceder tanto a .polatiry como a .subjectivity del texto deseado de la siguiente manera:



```python
from textblob import TextBlob

frase = "I absolutely love this new phone—it's outstanding!"
blob = TextBlob(frase)
print(f"Polaridad: {blob.sentiment.polarity}")
print(f"Subjetividad: {blob.sentiment.subjectivity}")
# Output
Polaridad: 0.4204545454545454
Subjetividad: 0.6431818181818182
```



En este ejemplo, “love” y “outstanding” tienen fuerte connotación positiva y personal, por lo que la polaridad y la subjetividad tendrán un valor significativo, indicando que la frase se basa en una opinión.

Si la oración presenta términos más neutrales o juicios mixtos, el resultado se situará en valores cercanos a 0 para la polaridad, y en un rango medio para la subjetividad. Esto ocurre, por ejemplo, en frases tipo:



```python
from textblob import TextBlob

frase = "That phone is just ok. There is nothing special or new about it."
blob = TextBlob(frase)
print(f"Polaridad: {blob.sentiment.polarity}")
print(f"Subjetividad: {blob.sentiment.subjectivity}")
# Output
Polaridad: 0.33116883116883117
Subjetividad: 0.5086580086580087
```



#### 3. Limitaciones



TextBlob está optimizado para el inglés, ya que aprovecha un diccionario léxico desarrollado principalmente para este idioma. Para otros idiomas, es común que los resultados empeoren, a menos que instalemos paquetes o extensiones específicas como las oficiales de su web [https://textblob.readthedocs.io/en/dev/extensions.html#languages](https://textblob.readthedocs.io/en/dev/extensions.html#languages).

También es importante destacar que el método léxico ignora matices contextuales, como las negaciones complejas (“No es nada malo”) o el sarcasmo (“Me encanta que la app se bloquee cada 30 segundos”). En aplicaciones con textos repletos de ironía o expresiones particulares, es preferible un modelo supervisado o un método que comprenda mejor el contexto.

Aun con estas limitaciones, TextBlob sigue siendo útil para proyectos rápidos o didácticos, donde se requiere una aproximación inmediata sin necesidad de un modelo entrenado.



#### 3. Pipeline de análisis de sentimiento



En un escenario más realista, nos solemos encontrar con un archivo, probablemente obtenido de una etapa anterior de extracción y tratamiento de datos, con contenido de texto. Lo siguiente que querremos hacer es leer estos datos, calcular la polaridad y la subjetividad, y luego guardar los resultados en un DataFrame de Pandas o Polars.

Veamos el siguiente ejemplo de nuestro pipeline. Lo primero que necesitamos es contar con nuestro archivo que contiene comentarios sobre una aplicación, comments.csv:



```csv
id,text
1,"This product is literally trash. Do not waste your money."
2,"Cool, another app that crashes every 5 minutes. Love it!"
3,"Not the worst purchase I've made, but close."
4,"The features are sick, but the battery dies in an hour."
5,"I’m thrilled to have my data sold without consent!"
6,"It’s okay, I guess. If you enjoy disappointment."
7,"Fantastic! Said no one ever about this junk."
8,"Works as intended... if you intend to frustrate users."
9,"A masterpiece of poor design. Truly innovative!"
10,"Not bad, if you ignore the fact that it broke instantly."
11,"Perfect for people who hate reliability."
12,"Wow, just what I needed... another useless gadget!"
13,"The quality is fire! (Literally, it overheats.)"
14,"10/10 would NOT recommend to my worst enemy."
15,"Great, if you define ‘great’ as ‘barely functional’."
16,"This is the worst thing since sliced bread."
17,"Impressive how they made something so mediocre."
18,"It’s fine. If fine means ‘I want a refund’."
19,"Unbelievable! (In the worst way possible.)"
20,"Five stars... for being a doorstop, not a device."
```



Ahora, podremos crear nuestro pipeline de la siguiente manera:



```python
# Pandas
import pandas as pd
from textblob import TextBlob

# Cargamos el CSV con comentarios
df = pd.read_csv("comments.csv", encoding='utf-8')

# Creamos las funciones para calcular polaridad y subjetividad
def obtener_polaridad(texto):
    blob = TextBlob(texto)
    return blob.sentiment.polarity

def obtener_subjetividad(texto):
    blob = TextBlob(texto)
    return blob.sentiment.subjectivity

# Aplicamos TextBlob a cada fila y almacenamos en una columna
df['polaridad'] = df['text'].apply(obtener_polaridad)
df['subjetividad'] = df['text'].apply(obtener_subjetividad)


# Analicemos, identifiquemos comentarios muy negativos (polaridad < -0.3)
negativos = df[df['polaridad'] < -0.3]
print("\nComentarios muy negativos:")
print(negativos)

df
```



```python
# Polars
import polars as pl
from textblob import TextBlob

# Cargamos el CSV con comentarios
df = pl.read_csv("comments.csv", encoding='utf-8')

# Creamos las funciones para calcular polaridad y subjetividad
def obtener_polaridad(texto):
    blob = TextBlob(texto)
    return blob.sentiment.polarity

def obtener_subjetividad(texto):
    blob = TextBlob(texto)
    return blob.sentiment.subjectivity

# Aplicamos TextBlob a cada fila y almacenamos en una columna
df = df.with_columns(
    pl.col('text').map_elements(obtener_polaridad, return_dtype=pl.Float64).alias('polaridad'),
    pl.col('text').map_elements(obtener_subjetividad, return_dtype=pl.Float64).alias('subjetividad'))


# Analicemos, identifiquemos comentarios muy negativos (polaridad < -0.3)
negativos = df.filter(pl.col("polaridad") < -0.3)
print("\nComentarios muy negativos:")
print(negativos)

df
```



Como resultado vemos DataFrames tanto en Polars como Pandas donde podemos observar que hay frases con datos extraños, como por ejemplo 0 en polaridad y 0 en subjetividad.



![image](assets/cm8di7txy01oz356yx5ukhpez-carousel1-INSD_BAIN_U4_Imagen7.jpg)

![image](assets/cm8di7txy01oz356yx5ukhpez-carousel2-INSD_BAIN_U4_Imagen8.jpg)



Estos valores se deben a lo que comentábamos previamente sobre las limitaciones de los métodos basados en léxico, por ejemplo, la frase "Five stars... for being a doorstop, not a device." al contener sarcasmo no es identificada correctamente.



### 3.4 Análisis de sentimiento con spaCy



#### 1. Introducción e instalación



spaCy posee potentes modelos estadísticos y la capacidad de entrenar o cargar pipelines ya existentes, que realicen diversas tareas de procesamiento (tokenización, etiquetado gramatical, reconocimiento de entidades, clasificación de texto, etc.). Para el análisis de sentimiento, se basa en el componente TextCategorizer o en modelos preentrenados provistos por la comunidad, capaz de detectar si un texto es positivo, negativo o neutro (u otras clases configuradas).

Aunque ya hemos instalado spaCy en unidades anteriores, recordemos que para instalar esta librería simplemente deberemos ejecutar el comando:



```bat
pip install spacy
```



Normalmente también debemos instalar pipelines preentreenados. En el caso de spaCy tenemos numerosos pipelines tantos propios ([https://spacy.io/models](https://spacy.io/models)) como de la comunidad ([https://spacy.io/universe/project](https://spacy.io/universe/project)).

Para este curso, además deberemos instalar algunos pipelines preentrenados de spaCy (). Para ello ejecutaremos:

**Windows**



```bat
python -m spacy download en_core_web_sm
```



**MacOS/Linux**



```bat
python3 -m spacy download en_core_web_sm
```



Además, utilizaremos uno de la comunidad que extiende de TextBlob:



```bat
pip install spacytextblob
```



#### 2. Aspectos básicos



Existen diversas maneras de llevar a cabo el análisis de sentimiento en spaCy:

- **Modelos preentrenados:** algunos pipelines en inglés (por ejemplo, en_core_web_trf con extensiones de la comunidad) incluyen ya un clasificador de sentimientos.
- **Entrenamiento manual del TextCategorizer:** se necesitan muestras etiquetadas con “POSITIVE”, “NEGATIVE” y, opcionalmente, “NEUTRAL”. spaCy aprende así a asignar probabilidades a cada categoría. Para este caso necesitaríamos datos estructurados de la siguiente forma:



```javascript
("Great camera and battery life", {"cats": {"POSITIVE": 1.0, "NEGATIVE": 0.0}}),
("Horrible software experience", {"cats": {"POSITIVE": 0.0, "NEGATIVE": 1.0}})
```



Si se cuenta con un corpus en español debidamente anotado, spaCy puede entrenar un modelo en dicho idioma, logrando a menudo resultados superiores a un simple método léxico, especialmente si el dominio es especializado.

En este caso, a pesar de utilizar una extensión de TextBlob, podemos compaginarlo con las funcionalidades de NLP que nos proporciona spaCy vistas en unidades anteriores, por ejemplo, podemos identificar tokens y obtener sus etiquetas.



```python
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

frase = "I absolutely love this new phone—it's outstanding!"

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")
doc = nlp(frase)
print(f"Polaridad: {doc._.blob.polarity}")

print(f"Subjetividad: {doc._.blob.subjectivity}")

# Tokenization & POS Tagging
print("\nTokenization & Part-of-Speech Tagging")
for token in doc:
    print(f"Token: {token.text}, POS: {token.pos_}")
# Output
Polaridad: 0.4204545454545454
Subjetividad: 0.6431818181818182
Tokenization & Part-of-Speech Tagging
Token: I, POS: PRON
Token: absolutely, POS: ADV
Token: love, POS: VERB
Token: this, POS: DET
Token: new, POS: ADJ
Token: phone, POS: NOUN
Token: —, POS: PUNCT
Token: it, POS: PRON
Token: 's, POS: AUX
Token: outstanding, POS: ADJ
Token: !, POS: PUNCT
```



Sin embargo, si no contamos con un modelo prehecho ni disponemos de datos anotados para entrenarlo, la configuración inicial con spaCy resultará algo más laboriosa.



#### 3. Pipeline de análisis de sentimiento



Al igual que en el caso anterior, en un escenario más realista, nos solemos encontrar con un archivo, probablemente obtenido de una etapa anterior de extracción y tratamiento de datos, con contenido de texto. Lo siguiente que querremos hacer es leer estos datos, calcular la polaridad y la subjetividad, y luego guardar los resultados en un DataFrame de Pandas o Polars.

La diferencia con el caso de TextBlob es que podemos obtener más información gracias a las funciones de NLP de spaCy.

Veamos el siguiente ejemplo de nuestro pipeline. Lo primero que necesitamos es contar con nuestro archivo que contiene comentarios sobre una aplicación, comments.csv:



```python
# Pandas
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")
# doc = nlp(frase)

# Cargamos el CSV con comentarios
df = pd.read_csv("comments.csv", encoding='utf-8')

# Creamos las funciones para calcular polaridad y subjetividad
def obtener_polaridad(texto):
    doc = nlp(texto)
    return doc._.blob.polarity

def obtener_subjetividad(texto):
    doc = nlp(texto)
    return doc._.blob.subjectivity

# Definimos funcion para almacenar los tokens y como valor su POS como un diccionario
def obtener_tokens_pos(texto):
    doc = nlp(texto)
    return {token.text: token.pos_ for token in doc}

# Aplicamos TextBlob a cada fila y almacenamos en una columna
df['polaridad'] = df['text'].apply(obtener_polaridad)
df['subjetividad'] = df['text'].apply(obtener_subjetividad)
df['tokens_pos'] = df['text'].apply(obtener_tokens_pos)



# Analicemos, identifiquemos comentarios muy negativos (polaridad < -0.3)
negativos = df[df['polaridad'] < -0.3]
print("\nComentarios muy negativos:")
print(negativos)

df
```



```python
# Polars
import polars as pl
from spacytextblob.spacytextblob import SpacyTextBlob

# Cargamos el CSV con comentarios
df = pl.read_csv("comments.csv", encoding='utf-8')

# Creamos las funciones para calcular polaridad y subjetividad
def obtener_polaridad(texto):
    blob = TextBlob(texto)
    return blob.sentiment.polarity

def obtener_subjetividad(texto):
    blob = TextBlob(texto)
    return blob.sentiment.subjectivity

# Definimos funcion para almacenar los tokens y como valor su POS como un diccionario
def obtener_tokens_pos(texto):
    doc = nlp(texto)
    return {token.text: token.pos_ for token in doc}

# Aplicamos TextBlob a cada fila y almacenamos en una columna
df = df.with_columns(
    pl.col('text').map_elements(obtener_polaridad, return_dtype=pl.Float64).alias('polaridad'),
    pl.col('text').map_elements(obtener_subjetividad, return_dtype=pl.Float64).alias('subjetividad'),
    pl.col('text').map_elements(obtener_tokens_pos, return_dtype=pl.Object).alias('tokens_pos'))

# Analicemos, identifiquemos comentarios muy negativos (polaridad < -0.3)
negativos = df.filter(pl.col("polaridad") < -0.3)
print("\nComentarios muy negativos:")
print(negativos)

df
```



De esta forma podemos apreciar que lo “único” extra que nos aporta spaCy al utilizar un modelo que extiende de TextBlob es toda esa información que podemos almacenar y utilizar.



![image](assets/cm8dim5yp022g356ykohirhsg-INSD_BAIN_U4_Imagen9.jpg)



Veamos a continuación como podemos beneficiarnos de toda esta potencia:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651986_1/scormcontent/assets/INSD_BAIN_U4_Video3.mp4?v=1)



### 3.5 Integración y consideraciones



Ya sea que usemos TextBlob o spaCy, es aconsejable preprocesar el texto eliminando spam, corrigiendo símbolos extraños o codificaciones incorrectas, etc. Para muchos idiomas, eliminar stopwords en la fase previa puede mejorar la señal. Sin embargo, a veces palabras como “no”, “sin”, etc. afectan sustancialmente a la polaridad, por lo que hay que evaluar cuidadosamente el impacto de filtrar stopwords en el análisis de sentimiento.

El sarcasmo sigue siendo uno de los grandes desafíos, ya que una frase puede contener palabras positivas, pero tener una connotación negativa. Algunas líneas de investigación se centran en modelos contextuales o redes neuronales profundas (p. ej., con Transformers) que se entrenan específicamente para reconocer ironías. Para uso general, si el corpus no abunda en sarcasmos, un enfoque supervisado con bastantes ejemplos de ironía puede ayudar a capturarlo.

Cuando se entrena un modelo (supervisado) de análisis de sentimiento, se suelen usar métricas como precisión (accuracy), precision, recall y F1-score. Para un uso práctico, no solo es importante la precisión global, sino la capacidad de distinguir casos negativos. Un pipeline real se beneficiará de una validación con muestras etiquetadas manualmente.



### 3.6 Enlaces de interés



> Entrenamiento de modelos en spaCy
>
> [Link](https://spacy.io/usage/training)

> Documentación de TextBlob
>
> [Link](https://textblob.readthedocs.io/en/dev/)

> Paper sobre sarcasmo en el análisis de sentimiento
>
> [Link](https://aclanthology.org/2022.semeval-1.132.pdf)



## 4. Introducción Al Parsing De Documentos (Nltk, Spacy)



### 4.1 Introducción



![image](assets/cm8div93a026c356ynqi0xqd9-stock-image.jpg)



En los apartados anteriores se ha abordado cómo extraer temas (LDA) y analizar el sentimiento de grandes colecciones de texto, lo cual aporta una vista general de “de qué se habla” y “cómo se valora” en un corpus. Sin embargo, para ciertos proyectos de ingeniería de software y análisis avanzado, se desea ir más allá de la simple “bolsa de palabras” (bag-of-words). Aparece la necesidad de comprender la estructura interna de las oraciones, identificar qué palabras son sujetos, qué términos se relacionan como verbos u objetos, o cómo las entidades (personas, lugares, organizaciones) se relacionan entre sí dentro de un texto.

El parsing se define como el proceso de analizar la estructura gramatical de un texto para comprender cómo se organizan las palabras y las oraciones. A diferencia de otras etapas de la minería de texto que se centran en el significado léxico de las palabras o en su frecuencia, el parsing nos brinda la relación sintáctica entre términos: qué función gramatical cumple cada palabra, cómo se forman los sintagmas nominales, verbales, etc. En aplicaciones de ingeniería de software que manejan documentación o grandes volúmenes de texto, este conocimiento estructural se vuelve esencial para interpretaciones más ricas de la información, como la extracción de relaciones, la normalización semántica o la generación de resúmenes contextualmente coherentes.



### 4.2 Aspectos teóricos



#### Introducción y tipos de parsing



El término parsing en procesamiento de lenguaje natural (NLP) hace referencia a la construcción de una representación estructurada de una oración. Dependiendo de la escuela lingüística y las metas de la tarea, esa estructura puede ser un árbol de constituyentes   (constituency parsing), que descompone la oración en sintagmas (SN, SV, SP, etc.), o un árbol de dependencias (dependency parsing), que establece relaciones directas entre cada palabra y su “palabra cabeza” (head), describiendo la función sintáctica (sujeto, objeto directo, modificador, etc.).

Cuando hablamos de parsing, podemos referirnos a distintos enfoques sobre cómo representar la estructura interna de una oración:



- **Parsing de constituyentes (constituency parsing)**  
  La oración se descompone en un árbol jerárquico de sintagmas (frases nominales, verbales, adjetivales, preposicionales, etc.). El objetivo es agrupar las palabras en unidades que tengan sentido como constituyentes lingüísticos. Por ejemplo:

  - Oración (S)
    - Sintagma nominal (NP)
      - Determinante (DT)
      - Adjetivo (JJ)
      - Sustantivo (NN)
  - Sintagma verbal (VP)
    - Verbo (VBZ)
  - Puntuación (PUNCT)

  Este tipo de parseo se apoya en gramáticas libres de contexto (CFG) o en enfoques estadísticos (p. ej. Probabilistic CFGs) que predicen la estructura más probable. NLTK brinda herramientas para definir gramáticas manuales o para usar parseadores de constituyentes preentrenados.
- **Parsing de dependencias (dependency parsing)**  
  En lugar de “bloques” que agrupan palabras, cada token de la oración se conecta con otro token que es su “cabeza” (head). Las etiquetas de relación (dep_) describen el rol sintáctico: sujeto nominal (nsubj), objeto directo (dobj), modificador adverbial (advmod), etc. Este esquema es habitual en spaCy, donde cada token apunta a su cabeza y se forma un árbol enraizado normalmente en el verbo principal (ROOT). La idea es que la estructura refleja relaciones directas entre palabras—“John” (nsubj) → “sees” (root), “Mary” (dobj) → “sees,” etc.



Cada uno ofrece ventajas y desventajas: el parseo de constituyentes es valioso para técnicas como la generación de oraciones o la chunking a nivel sintagmático; el dependency parse resulta muy ágil y más directo para extraer información semántica (por ejemplo, identificar el sujeto y el objeto de un verbo). A nivel de rendimiento y popularidad en la industria, el dependency parse es hoy dominante, impulsado por librerías como spaCy y transformadores modernos (Transformers-based pipelines).



![image](assets/cm8dj7cs002bf356ygyuwtvwi-INSD_BAIN_U4_Imagen10.jpg)



#### Objetivos y casos de uso



El objetivo de un parseo (ya sea de constituyentes o de dependencias) es capturar la estructura interna de la oración. Esto posibilita, por ejemplo:

- Identificar qué palabra es la raíz de la oración (el núcleo verbal).
- Determinar qué tokens son argumentos del verbo y con qué función (sujeto, objeto, etc.).
- Reconocer estructuras compuestas, como frases preposicionales, oraciones subordinadas, etc.
- Permitir tareas de extracción de relaciones (quién hizo qué a quién), semánticas de oraciones y validaciones lingüísticas en un pipeline de minería de texto.

Desde la perspectiva de ingeniería de software, muchas veces nos interesa extraer datos más precisos de textos no estructurados: “¿Quién menciona a qué producto y con qué adjetivos?”, “¿Cuál es la relación entre un fármaco y sus efectos secundarios en un corpus biomédico?”. El parsing, en conjunto con la etiqueta gramatical (PoS tagging) y el reconocimiento de entidades (NER), sienta las bases para resolver dichas preguntas de forma robusta.

Las tareas de minería de texto a menudo se focalizan en la frecuencia de palabras (bag-of-words), en la detección de la polaridad (análisis de sentimiento) o en la agrupación por tópicos (LDA). Sin embargo, en proyectos complejos de ingeniería de software, se desea una comprensión sintáctica más profunda para:



- **Extracción de hechos y relaciones**  
  Determinar “quién ejecuta la acción,” “cuál es el objeto de la acción,” o “qué propiedad se describe.” Por ejemplo, en la documentación técnica, puede interesar “La clase X hereda de la clase Y, usando el método Z para la tarea.” El parseo da una base para ubicar al sujeto (la clase X), el verbo (hereda), y su complemento (clase Y).
- **Validación y normalización**  
  En manuales, requerimientos o artículos extensos, un parsing correcto ayuda a estructurar la información en bases de datos relacionales, a generar plantillas automáticas o a verificar si las oraciones siguen ciertas convenciones semánticas.
- **Sistemas de soporte**  
  En chatbots o en interfaces de lenguaje natural, el parseo asiste al motor de diálogo para desambiguar consultas. Por ejemplo, “Apaga la luz de la sala con el interruptor principal” vs. “En la sala principal, apaga la luz con interruptor secundario,” donde la frase y la preposición cambian la relación.



### 4.3 Parsing con NLTK



Como ya vimos en unidades anteriores, NLTK (Natural Language Toolkit) es un conjunto de librerías muy utilizadas en el ámbito académico para aprender y experimentar con técnicas de lingüística computacional. Además, NLTK ofrece varios módulos de parsing. Entre los más destacados, se encuentran:



- **NLTK CFG (Context-Free Grammar)**  
  Permite definir gramáticas libres de contexto para parsear oraciones en árboles de constituyentes.
- **RegExParser y Chunking**  
  Para extraer porciones de oraciones basadas en patrones de etiquetas (por ejemplo, NP-chunking para frases nominales).
- **Dependency**  
  NLTK no es tan fuerte en parsing de dependencias como spaCy, pero existen complementos que permiten trabajar con oraciones parseadas en estilo de dependencias.



#### Parsing de constituyentes



El “parsing de constituyentes” (constituency parsing) consiste en descomponer la oración en sintagmas (frases nominales, verbales, etc.) según reglas sintácticas. En NLTK, es posible definir manualmente una gramática o usar un parser estadístico entrenado.

Veamos como definir una gramática propia y analizar un texto. Pero antes de nada recordemos los diferentes símbolos utilizados de forma estándar:

- S = Sentence (oración): es el símbolo inicial que representa una oración completa
- NP = Noun Phrase (sintagma nominal): un grupo de palabras que funcionan como sustantivo
  - Ejemplo: "the telescope" o "John"
- VP = Verb Phrase (sintagma verbal): un grupo de palabras que contiene un verbo y sus complementos
  - Ejemplo: "sees Mary" o "sees Mary with a telescope"
- PP = Prepositional Phrase (frase preposicional): un grupo de palabras que comienza con una preposición
  - Ejemplo: "with a telescope"
- DT = Determiner (determinante): palabras que modifican sustantivos como artículos
  - Ejemplos: "the", "a", "an"
- NN = Noun (sustantivo): palabras que nombran cosas, lugares o conceptos
  - Ejemplo: "telescope"
- PRP = Personal Pronoun (pronombre personal): pronombres que se refieren a personas
  - Ejemplos: "he", "she", "I"
- NNP = Proper Noun (nombre propio): nombres específicos de personas, lugares o cosas
  - Ejemplos: "John", "Mary"
- VBZ = Verb, 3rd person singular present (verbo en tercera persona singular, presente): forma verbal para "he/she/it"
  - Ejemplo: "sees"
- IN = Preposition (preposición): palabras que conectan frases o indican relaciones
  - Ejemplos: "with", "in"
- PUNCT = Punctuation (puntuación): signos de puntuación
  - Ejemplos: ".", "!", "?"

Sabiendo estos símbolos, generemos nuestra propia gramática para analizar frases y ver el árbol de constituyentes:



```python
import nltk

# Descargamos los recursos si no los tenemos
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Oración de ejemplo
sentence = "John sees Mary with a telescope."

# Tokenizamos y realizamos POS tagging
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
print("POS tags:", pos_tags)

# Definimos una gramática libre de contexto muy simple
grammar = r"""
  S -> NP VP PUNCT # definimos que una oración se descompone en un sintagma nonimal, seguido de uno verbal y seguido de signos de puntuación.
  NP -> DT NN | PRP | NP PP | NNP
  VP -> VBZ NP | VBZ NP PP
  PP -> IN NP
  DT -> 'a' | 'the'
  NN -> 'telescope'
  NNP -> 'John' | 'Mary'
  VBZ -> 'sees'
  IN -> 'with' | 'in'
  PUNCT -> '.'
"""

# Construimos el parser
cfg_grammar = nltk.CFG.fromstring(grammar)
parser = nltk.ChartParser(cfg_grammar)

for tree in parser.parse(tokens):
    print(tree)
    tree.draw()  # Abre una ventana con el árbol
# Output
POS tags: [('John', 'NNP'), ('sees', 'VBZ'), ('Mary', 'NNP'), ('with', 'IN'), ('a', 'DT'), ('telescope', 'NN'), ('.', '.')]
(S
  (NP (NNP John))
  (VP
    (VBZ sees)
    (NP (NNP Mary))
    (PP (IN with) (NP (DT a) (NN telescope))))
  (PUNCT .))
```



![image](assets/cm8djst9j02h8356yj2njf1ny-INSD_BAIN_U4_Imagen11.jpg)



Al invocar tree.draw(), se abre una ventana con un árbol que muestra S en la raíz, descomponiéndose en NP y VP, etc. Este parseo de constituyentes puede resultar excesivamente rígido en proyectos reales, pero es didáctico para comprender cómo un árbol sintáctico se forma a partir de reglas definidas.



#### Chunking y RegexParser



Otro método de parsing ligero en NLTK es el chunking, que no construye el árbol completo de la oración, sino que extrae trozos (chunks) basados en patrones. Por ejemplo, para extraer frases nominales (NP-chunks) con expresiones regulares sobre POS tags:



```python
import nltk

sentence = "The big green tree swayed gracefully in the park"
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)

# Definimos la gramática de nuestros chunks
grammar = r"""
   NP: {<DT>?<JJ>*<NN>}   # una regla simple para capturar determinante + adjetivos + sustantivo
   PP: {<IN><NP>}         # preposición + sintagma nominal
   VP: {<RB>*<VB.*><RB>*<NP|PP>*}# un verbo, seguido opcionalmente por NP o PP. Además de adverbios delante y detrás del verbo
"""

chunk_parser = nltk.RegexpParser(grammar)
chunked = chunk_parser.parse(pos_tags)
print(chunked)
chunked.draw()
```



![image](assets/cm8djuszv02ka356yh90wqde9-INSD_BAIN_U4_Imagen12.jpg)



Aquí definimos varias reglas: NP, PP y VP. La instrucción “NP: {<DT>?<JJ>*<NN>}” dice “opcionalmente un determinante, seguido de cero o más adjetivos, seguido de un sustantivo.” De esta forma, “The big green tree” se convierte en un chunk NP. Este chunking no construye la jerarquía de toda la oración, pero aisla trozos relevantes.

El chunking presenta algunas ventajas, como puedan ser:

- Suele ser más simple y rápido que un parser de constituyentes completo.
- Facilita la extracción de “frases nominales importantes” en un texto, crucial en muchas tareas de extracción de información.
- Se puede extender con reglas más sofisticadas, por ejemplo, frases verbales, sintagmas adverbiales, etc.



### 4.4 Parsing con spaCy



#### Introducción y parseo de dependencias



Mientras que NLTK se centra más en el parsing de constituyentes (a menos que instalemos complementos), spaCy está orientado principalmente al dependency parsing. El modelo de dependencias en spaCy se entrena para asignar a cada palabra de la frase un “head” y un “dependency label”, de forma que se cree un árbol enraizado normalmente en el verbo principal (root). Por ejemplo:

- “John sees Mary with a telescope”
  - “sees” es la raíz (VERB)
  - “John” se conecta a “sees” con la etiqueta nsubj (sujeto nominal)
  - “Mary” se conecta a “sees” con la etiqueta dobj (objeto directo)
  - “with” se conecta a “sees” con la etiqueta prep (preposición)
  - “telescope” se conecta a “with” con la etiqueta pobj (objeto de preposición)

Si utilizamos spaCy para ver las dependencias en el parseo:



```elixir
import spacy

# Cargamos un modelo en inglés o español que contenga parser
nlp = spacy.load("en_core_web_sm")
frase="John sees Mary with a telescope."

doc = nlp(frase)

for token in doc:
    print(f"{token.text} -> head: {token.head.text}, dep: {token.dep_}, pos: {token.pos_}")
# Output
John -> head: sees, dep: nsubj, pos: PROPN
sees -> head: sees, dep: ROOT, pos: VERB
Mary -> head: sees, dep: dobj, pos: PROPN
with -> head: sees, dep: prep, pos: ADP
a -> head: telescope, dep: det, pos: DET
telescope -> head: with, dep: pobj, pos: NOUN
. -> head: sees, dep: punct, pos: PUNCT
```



La salida describe, para cada palabra, cuál es su cabeza (head), qué etiqueta de dependencia (dep_) posee, y su categoría gramatical (pos_). Por ejemplo, “John -> head: sees, dep: nsubj, pos: PROPN” indica que “John” es sujeto nominal de “sees”.

En el caso de spaCy, también contamos con pipelines preentrenados en español que nos pueden ayudar a identificar las dependencias.

Para ello el primer paso será instalar dicho pipeline:

**Windows**



```bat
python -m spacy download es_core_news_sm
```



**MacOS/Linux**



```bat
python3 -m spacy download es_core_news_sm
```



Posteriormente, se utiliza de la misma manera que en el caso de inglés:



```yaml
import spacy

# Cargamos un modelo en inglés o español que contenga parser
nlp = spacy.load("es_core_news_sm")
frase= "Juan va a comprar el pan de la tienda donde María trabaja."

doc = nlp(frase)

for token in doc:
    print(f"{token.text} -> head: {token.head.text}, dep: {token.dep_}, pos: {token.pos_}")
# Output
Juan -> head: comprar, dep: nsubj, pos: PROPN
va -> head: comprar, dep: aux, pos: AUX
a -> head: comprar, dep: mark, pos: ADP
comprar -> head: comprar, dep: ROOT, pos: VERB
el -> head: pan, dep: det, pos: DET
pan -> head: comprar, dep: obj, pos: NOUN
de -> head: tienda, dep: case, pos: ADP
la -> head: tienda, dep: det, pos: DET
tienda -> head: pan, dep: nmod, pos: NOUN
donde -> head: trabaja, dep: obl, pos: PRON
María -> head: trabaja, dep: nsubj, pos: PROPN
trabaja -> head: tienda, dep: acl, pos: VERB
. -> head: comprar, dep: punct, pos: PUNCT
```



La representación de dependencias es muy útil para:



- **Extracción de relaciones**  
  Identificar que “John” (sujeto) “ve a Mary” (objeto) con un “telescope” (objeto de la preposición “with”).
- **Transformación semántica**  
  Algunas técnicas de QA (question answering) o resúmenes se apoyan en la estructura de dependencias para reorganizar la información.
- **Análisis de opinión detallado**  
  Saber exactamente a qué se refiere un adjetivo. Por ejemplo, si hay “great service” vs. “great location” en un comentario de hotel.



En el video a continuación veremos un caso completo de cómo obtener información de un documento de opiniones y cómo podemos hacer analítica con él:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651986_1/scormcontent/assets/INSD_BAIN_U4_Video4.mp4?v=1)



El parser de spaCy, aunque muy robusto, no es infalible. En oraciones con ambigüedad, a veces asocia mal las dependencias. Cuanto más contextual y complejo sea el enunciado, más probable que un parse superficial cometa errores. Existen modelos “transformer-based” (como en_core_web_trf) que suelen ofrecer parseos más precisos, pero son más pesados en ejecución y requieren GPU para el mejor rendimiento.



#### Comparativa con NLTK



Si bien NLTK y spaCy pueden solaparse en algunas funcionalidades (p. ej., tokenización, POS tagging), cada librería posee su propia filosofía y fortalezas a la hora de parsear:

|  | NLTK | spaCy |
| --- | --- | --- |
| Tipo de parseo principal | Constituyentes (CFG, PCFG), chunking (RegexParser). | Dependency parsing estadístico, en pipelines preentrenados. |
| Facilidad de uso | Muy educativo, se definen gramáticas y se experimenta. Puede ser algo manual. | Muy orientado a producción, poca configuración: nlp = spacy.load(...). Parsing inmediato en un doc. |
| Rendimiento | Adecuado para prototipos. CFGs manuales pueden ser lentas con oraciones largas. | Más rápido y optimizado, usando parse estadístico en Cython. Soporta nlp.pipe en lotes grandes. |
| Gramáticas personalizadas | Altamente personalizable, posibilidad de escribir CFG, chunkers a la medida. | No provee un parse de constituyentes nativo; el parser es un modelo entrenado. Escasa personalización manual. |
| Soporte multilingüe | Limitado a parseadores de 3.ª parte, chunking manual. | Modelos oficiales para muchos idiomas con parse de dependencias. |
| Integración | Menos nativa con pipeline de NER, sentiment, etc. (aunque hay complementos). | Integrado con etiquetado POS, NER, textcat, etc., en un solo pipeline. |
| Aplicaciones típicas | Entorno académico, experimentos con gramáticas CFG, chunking rápido. | Entorno productivo y de I+D, parse rápido, robusto. Extracción de relaciones, QA, chatbots… |



### 4.5 Buenas prácticas para el parseo



- **Procesado**  
  Asegurarse de un texto “limpio” (corrección de codificaciones, normalización de algunos caracteres) facilita la labor de parseadores. Sin embargo, no conviene eliminar con anticipación tokens relevantes (p. ej. “no”, “sin”, etc.) si la estructura sintáctica es importante.
- **Elección de idioma y modelo**  
  En spaCy, cada idioma tiene sus modelos xx_core_web_sm, md, lg, trf, etc. Elegir uno que contenga el parser y, si es relevante, ner o textcat.
- **Resolución de ambigüedad**  
  Tanto en el parseo de constituyentes como en el parseo de dependencias, pueden surgir ambigüedades. Un parser estadístico (como spaCy) usará la probabilidad más alta según su entrenamiento, pero no siempre será la correcta si encuentra construcciones muy inusuales.
- **Manejo de oraciones largas**  
  Con oraciones extensas o texto semiestructurado (tablas, listados, etc.), conviene segmentar en oraciones más cortas. Herramientas de sentence segmentation (spaCy o NLTK) ayudan a trocear el texto adecuadamente.
- **Integración con NER**  
  A menudo, se combina el parseo con la detección de entidades para enriquecer la semántica. Por ejemplo, en la frase “John, the CEO of AcmeCorp, spoke about new policies,” se puede extraer la relación “John -> (role) CEO -> (organization) AcmeCorp” analizando dependencias y anotaciones de entidades.
- **Escabilidad**  
  Parsear docenas de millones de oraciones puede ser intensivo. A menudo se recurre a batches, orquestación en cluster, o librerías adaptadas al big data. spaCy puede manejar nlp.pipe para procesar oraciones en paralelo.



### 4.6 Enlaces de interés



> Documentación de spaCy sobre el parseo
>
> [Link](https://spacy.io/usage/linguistic-features#dependency-parse)

> Chunking con NLTK
>
> [Link](https://www.nltk.org/_modules/nltk/chunk/regexp.html)

> Parseo con NLTK (capítulos 8 y 9)
>
> [Link](https://www.nltk.org/book/)



## 5. Resumen De Textos Con Técnicas Tradicionales



### 5.1 Introducción



![image](assets/cm8dkix2402zn356yocubua6j-stock-image.jpg)



Tras adentrarnos en el descubrimiento de tópicos (LDA), el análisis de sentimiento (TextBlob, spaCy) y la comprensión sintáctica (parsing en NLTK y spaCy), completamos la visión de modelización y análisis de textos con otro componente esencial: el resumen automático de documentos. Resumir un texto consiste en producir una versión condensada de su contenido, de modo que se conserven las ideas o elementos más importantes sin necesidad de leer el original de forma íntegra. En ingeniería de software y ciencia de datos, la capacidad de resumir informes, artículos extensos, resultados científicos o documentación puede ahorrar tiempo y posibilitar la toma de decisiones sobre grandes corpus.



### 5.2 Aspectos básicos



En la práctica, existen múltiples paradigmas de resumen de texto. Generalmente se distinguen los extractivos (las frases más relevantes se extraen tal cual del documento) de los abstractive (se genera nuevo texto que “parafrasea” el contenido). Este apartado se enfoca en las técnicas tradicionales extractivas, que combinan criterios de relevancia (por frecuencia de palabras, TF-IDF, ranking basado en grafos, etc.) para seleccionar un subconjunto de oraciones que conformen un “resumen.” Aunque las corrientes más recientes tienden a utilizar modelos neuronales y transformadores (por ejemplo, T5, BART, GPT, etc.), en un grado de ingeniería de software es muy instructivo conocer primero los fundamentos de las técnicas clásicas:



- **Modelos de frecuencia de palabras**  
  - Se asume que las palabras más frecuentes y relevantes (a menudo con TF-IDF) dan pistas de la importancia de ciertos fragmentos.
  - Para cada oración, se calcula una puntuación según las palabras que contiene y la relevancia de esas palabras en el texto.
  - Se seleccionan las oraciones con mayor puntuación.
- **Métodos basados en grafos (TextRank, LexRank)**  
  - Se construye un grafo donde cada nodo representa una oración y la similitud (típicamente coseno TF-IDF) entre oraciones define los enlaces.
  - Se aplica un método estilo PageRank para propagar “importancia” entre nodos, asumiendo que oraciones conectadas con oraciones importantes también tienen relevancia.
  - Se extraen las oraciones con puntuaciones top.
- **Heurísticas de posición**  
  - En artículos noticiosos o informes técnicos, a menudo las primeras (o últimas) oraciones sintetizan el contenido.
  - Se define un score más alto para oraciones en ciertas posiciones (por ejemplo, la oración inicial de cada párrafo o la “conclusión”).
- **Modelos basados en LSA (Latent Semantic Analysis)**  
  - Se representa el documento en una matriz (número de oraciones × número de palabras), se hace una descomposición SVD, y se identifican los vectores oracionales que mejor cubren la variación semántica.
  - Se eligen oraciones que correspondan a la dimensión latente más representativa.



El “resumen automático” es el proceso de generar una versión breve de un documento o conjunto de documentos, tratando de retener la esencia del contenido original. Desde un punto de vista computacional, se han distinguido tradicionalmente dos grandes enfoques:



- **Resumen extractivo**  
  Se eligen oraciones (u otros fragmentos) existentes del documento original, sin reescribirlas, y se las concatena en un orden que conserve coherencia.
- **Resumen abstractive**  
  Se produce un texto “nuevo,” reformulando oraciones y potencialmente introduciendo conectores. Los métodos más recientes (modelos neuronales y transformadores) sobresalen en este campo, pero se salen del alcance de estas “técnicas tradicionales” que abordamos aquí.



El porqué del resumen se comprende mejor al observar la explosión de datos textuales en la web y en sistemas empresariales. Para un ingeniero de software o un analista de datos, revisar toda la documentación, manuales o artículos puede ser inviable. En cambio, un sistema que extraiga un “resumen” con 3-4 oraciones por documento posibilita la exploración inicial y la focalización en los materiales más relevantes.



### 5.3 Métodos de extracción clásicos



En ingeniería de software, las técnicas extractivas han sido muy populares porque:

- Son fáciles de implementar y no requieren un corpus entrenado para aprender a “generar” texto.
- Preservan la redacción exacta de las oraciones escogidas, evitando (o minimizando) errores gramaticales.
- Funcionan razonablemente bien en documentos informativos, donde cada frase suela contener un aporte concreto.

Aunque no generan resúmenes tan refinados como un humano (o como un modelo abstractive de alta calidad), su sencillez y la ausencia de datos de entrenamiento los hacen atractivos.



#### Métodos basados en frecuencia de palabras



El método de frecuencia de términos parte de la hipótesis de que las palabras clave en un texto se repiten con mayor frecuencia. Una oración que agrupe varias de estas palabras (o la media de sus relevancias sea alta) es, potencialmente, una oración esencial. Para perfeccionar este enfoque, se suele usar TF-IDF (Term Frequency – Inverse Document Frequency) en lugar de la frecuencia pura. TF-IDF penaliza las palabras demasiado comunes en el idioma (p. ej. “the,” “and,” “of,” etc.) y resalta las que sean específicas del texto.

El pipeline típico es:

1. Dividir el texto en oraciones.
2. Tokenizar las oraciones en palabras, filtrar stopwords, etc.
3. Calcular la frecuencia de cada palabra en el texto (o su TF-IDF si hay un corpus mayor de referencia).
4. Para cada oración, sumar (o promediar) los valores de las palabras que contiene.
5. Ordenar las oraciones de mayor a menor puntuación.
6. Escoger el tope de oraciones, reordenarlas según su posición original.



![image](assets/cm8dkz3y2036u356y92kxejun-INSD_BAIN_U4_Imagen14.png)



La complejidad principal es O(N × M), donde N es la cantidad de oraciones y M el número de términos a manejar. Es un método rápido y de baja demanda computacional, ideal para pipelines que manejan un volumen considerable de documentos.

Este pipeline a nivel de código se debe implementar en diferentes etapas, para este caso utilizaremos NLTK:



```python
import re
import math
import nltk

nltk.download('punkt')
nltk.download('stopwords')

text = """
    Natural language processing (NLP) is a subfield of linguistics, 
    computer science, and artificial intelligence concerned with 
    the interactions between computers and human language. 
    It is used to apply algorithms to identify and extract the 
    natural language rules such that the unstructured language data 
    is converted into a form that computers can understand. 
    Once the text has been provided, the computer will utilize 
    algorithms to extract meaning associated with every sentence 
    and collect the essential data from them. 
    """

ratio=0.3

# 1. Segmentamos en oraciones
original_sentences = nltk.sent_tokenize(text)

# 2. Construimos un diccionario de frecuencias
word_counts = {}
stop_words = set(nltk.corpus.stopwords.words('english'))

for sent in original_sentences:
    # Limpiamos puntuación y pasamos a minúsculas
    cleaned = re.sub(r'[^\w\s]', '', sent.lower())
    tokens = nltk.word_tokenize(cleaned)
    for t in tokens:
        if t not in stop_words and t.isalpha():
            word_counts[t] = word_counts.get(t, 0) + 1

max_freq = max(word_counts.values())

# 3. Puntuamos cada oración
sentence_scores = {}
for idx, sent in enumerate(original_sentences):
    cleaned = re.sub(r'[^\w\s]', '', sent.lower())
    tokens = nltk.word_tokenize(cleaned)
    score = 0
    for w in tokens:
        if w in word_counts:
            # Normalizamos dividiendo por la freq máxima
            score += word_counts[w] / max_freq
    # Almacenamos el score
    sentence_scores[idx] = score

# 4. Ordenamos oraciones por score
sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)

# 5. Determinamos cuántas oraciones tendrá el resumen
total_sentences = len(original_sentences)
top_n = math.ceil(total_sentences * ratio)

# 6. Seleccionamos las oraciones top
selected_idx = [idx for idx, score in sorted_sentences[:top_n]]
selected_idx.sort()
summary_sentences = [original_sentences[i] for i in selected_idx]

# 7. Combinamos en el orden original
summary = " ".join(summary_sentences)

print("Resumen:\n", summary)
# Output
Resumen:
 It is used to apply algorithms to identify and extract the 
    natural language rules such that the unstructured language data 
    is converted into a form that computers can understand.
```



El ratio=0.2 (o 0.3 en el ejemplo) indica qué fracción de oraciones se desea retener. Si hay 10 oraciones y ratio=0.3, extraeremos 3 oraciones. Por otro lado, eliminamos las stopwords, como “the,” “of,” “and.” Así se resaltan las palabras que sí aportan contenido.

Computamos la frecuencia con un simple diccionario word_counts. Este es un método “bag-of-words” local al documento. A continuación, para la normalización, dividimos por max_freq para que la palabra más frecuente tenga un peso 1.0. Palabras con menor frecuencia se ubican en un rango 0 < peso < 1.

Para ir concluyendo, la puntuación de la oración se define sumando (o promediando) las frecuencias de las palabras que contiene. Se podría usar un “promedio” en lugar de la “suma” para no favorecer oraciones demasiado extensas, todo depende del criterio. Por último, para seleccionar ordenamos y tomamos la fracción superior. Esto corresponde a un “resumen” de dichas oraciones, reagrupadas en el orden en que aparecían en el texto.

Si quisiéramos incorporar TF-IDF en lugar de frecuencia pura, se necesitaría un corpus más amplio o un transformador que calcule TF-IDF para cada término en el documento. Sin embargo, la lógica de “sumar/puntuar oraciones” se mantendría.



#### Métodos basados en TextRank



TextRank es un método de ranking de oraciones que toma inspiración en el algoritmo PageRank, el cual hizo famoso a Google para ordenar resultados de búsqueda. La intuición es que las oraciones se enlazan entre sí si su contenido es similar (por ejemplo, un coseno de TF-IDF > 0.1). De esta manera, oraciones que estén fuertemente interconectadas con oraciones relevantes obtendrán un alto puntaje. Oraciones desconectadas o con escasa similitud quedan en puntajes bajos.

El pipeline general para un solo documento es:

1. Segmentar en oraciones.
2. Calcular la similitud entre cada par (i, j). Se usa TF-IDF, Word2Vec o embeddings para representar oraciones.
3. Construir un grafo no dirigido con N nodos (N = número de oraciones). El peso del enlace i-j es la similitud coseno. A veces se filtra con un umbral para no conectar oraciones muy disímiles.
4. Aplicar PageRank o un método análogo para computar la “importancia” de cada nodo-oración.
5. Escoger las oraciones top y reordenarlas en el orden original.



![image](assets/cm8dl33a503an356y94fgguii-INSD_BAIN_U4_Imagen15.png)



El score que una oración recibe en TextRank depende de cuántos nodos la puntúan y cuán importantes sean esos nodos. La justificación es que una oración que coincide en contenido con otras oraciones relevantes se asume igualmente relevante.

En este caso, aprovecharemos la potencia y comunidad de spaCy para utilizar PyTextRank. Para ello deberemos instalarlo con:



```bat
pip install pytextrank
```



Recordemos que será necesario tener descargado el pipeline mediante:

**Windows**



```bat
python -m spacy download en_core_web_sm
```



**MacOS/Linux**



```bat
python3 -m spacy download en_core_web_sm
```



Y la implementación del pipeline será tan sencilla como:



```python
import spacy
import pytextrank

nlp = spacy.load("en_core_web_sm")

# Añadimos PyTextRank pipeline
nlp.add_pipe("textrank")

text = """
    Natural language processing (NLP) is a subfield of linguistics, 
    computer science, and artificial intelligence concerned with 
    the interactions between computers and human language. 
    It is used to apply algorithms to identify and extract the 
    natural language rules such that the unstructured language data 
    is converted into a form that computers can understand. 
    Once the text has been provided, the computer will utilize 
    algorithms to extract meaning associated with every sentence 
    and collect the essential data from them. 
    """

doc = nlp(text)

# Generar resumen
for phrase in doc._.textrank.summary(limit_phrases=2, limit_sentences=2):
    print(f"frase: {phrase}")
# Output
frase: 
    Natural language processing (NLP) is a subfield of linguistics, 
    computer science, and artificial intelligence concerned with 
    the interactions between computers and human language. 
    
frase: It is used to apply algorithms to identify and extract the 
    natural language rules such that the unstructured language data 
    is converted into a form that computers can understand.
```



Veamos a continuación un pipeline complejo:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651986_1/scormcontent/assets/INSD_BAIN_U4_Video5.mp4?v=1)



#### Otras técnicas



En ciertos géneros textuales (p. ej. noticias periodísticas o papers científicos), la disposición de la información clave puede ser predecible. Por ejemplo, en un paper, la primera oración del abstract y la primera del conclusion suelen ser muy relevantes. En una noticia, el primer párrafo típicamente da el “lead” con la idea principal.

Un método de heurística posicional define, por ejemplo:

- Puntuación de una oración = (1 / (índice_de_la_oración + 1)) × (alguna valoración lexicográfica).
- Oraciones en la introducción y conclusiones suman +X puntos.
- Si el medio es un blog periodístico, quizás la primera o la segunda frase contenga la “idea fuerza”.

Estas heurísticas son simples, pero en documentos con redacción estructurada, a menudo “funcionan” razonablemente bien. Combinarlas con un factor de “frecuencia de palabras” o “TextRank” puede otorgar un plus de eficacia.

En la comparación con metodologías basadas en deep learning (abstractive), cabe mencionar:

- Las técnicas clásicas (frecuencia, TextRank, etc.) no generan nuevas oraciones ni conectores, por lo que el resumen puede tener repeticiones y sonar algo robótico o telegráfico.
- Los modelos abstractive (BART, T5, GPT) pueden “resumir” con frases reescritas elegantemente, pero requieren un corpus de entrenamiento y potencia computacional, y a veces inventan datos (problema de factualidad).
- Para un pipeline ligero que no requiera GPU ni grandes corpus, las técnicas tradicionales siguen siendo la opción más directa.



### 5.4 Enlaces de interés



> Documentación PyTextRank
>
> [Link](https://spacy.io/universe/project/spacy-pytextrank)

> Resúmenes con NLTK
>
> [Link](https://www.nltk.org/howto/summarize.html)



## 6. Conclusiones



### 6.1 Conclusiones de la unidad



A lo largo de esta unidad, hemos profundizado en el modelado y análisis de texto desde varios enfoques que buscan extraer conocimiento de grandes volúmenes de documentos. Comenzamos por el descubrimiento de tópicos con LDA (Latent Dirichlet Allocation), donde comprendimos su fundamento matemático basado en las distribuciones Dirichlet y practicamos su implementación con la librería gensim. Observamos la importancia de preprocesar y vectorizar los datos (mediante bolsa de palabras o TF-IDF), así como la relevancia de métricas como la coherencia para encontrar el número óptimo de tópicos y asegurar que el modelo represente fielmente el corpus.

Después, nos adentramos en el análisis de sentimiento, comparando estrategias de diccionario léxico (TextBlob) frente a modelos supervisados (spaCy). Reconocimos que mientras los métodos basados en diccionarios requieren menos recursos y son fáciles de configurar, los algoritmos entrenados ofrecen mayor precisión, especialmente en dominios con vocabulario especializado o expresiones irónicas. Sin embargo, constatamos que detectar el sarcasmo y las sutilezas del lenguaje sigue siendo un desafío pendiente para muchos sistemas de NLP.

En la tercera sección, abordamos el parsing de documentos para obtener una vista estructural profunda de las oraciones. Conocimos la diferencia entre parseo de constituyentes (NLTK) y parseo de dependencias (spaCy), y comprobamos cómo las relaciones sintácticas o la detección de entidades pueden enriquecer el análisis. Esto abre puertas a aplicaciones más avanzadas de extracción de hechos y verificación semántica, donde el orden y la función gramatical de las palabras son fundamentales.

Por último, cerramos la unidad con los métodos tradicionales de resumen. Desde enfoques que priorizan la frecuencia de términos hasta algoritmos estilo PageRank (TextRank), aprendimos a producir resúmenes extractivos que facilitan la lectura y exploración de documentos largos. Estas técnicas, si bien no crean nuevo texto, resultan valiosas por su sencillez y rapidez, y se integran sin problema en pipelines que ya incorporan análisis de tópicos, sentimiento y parsing profundo.

En conjunto, cada apartado (LDA, sentimiento, parsing, resúmenes) aporta una pieza esencial en el rompecabezas de la minería de texto, permitiendo desde la agregación temática y la evaluación afectiva, hasta la comprensión sintáctica de las oraciones y la síntesis automatizada de su contenido. Este bloque de conocimientos sienta la base para construir pipelines robustos en ingeniería de software, capaces de procesar y sintetizar datos textuales con un enfoque modular y escalable.



Nota final:

Experimentar con corpus reales y métricas adecuadas (coherencia, ROUGE, precisión, etc.) garantiza una visión más práctica.

Ajustar hiperparámetros (número de tópicos en LDA, umbrales de análisis de sentimiento o heurísticas en el resumen) es esencial para cada dominio.

Adoptar un enfoque iterativo (prototipo → validación → refinamiento) es la ruta más fiable para desarrollar soluciones efectivas en minería de texto.
