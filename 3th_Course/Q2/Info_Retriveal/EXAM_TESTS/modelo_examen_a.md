# Modelo de Examen — Modelo 1
## Ingeniería de Datos y NLP con Python
### 45 preguntas tipo test · Una sola respuesta correcta

---

## UNIDAD 1 — El ecosistema Python

---

**Pregunta 1**

¿Qué estructura de datos de Python NO puede usarse como clave en un diccionario?

A) Tupla

B) Cadena de texto

C) Entero

D) Lista ✅

---

**Pregunta 2**

Tenemos el siguiente fragmento. ¿Cuál es el resultado de ejecutarlo?

```python
datos = {}
claves = ['a', 'b', 'c']
valores = [1, 2, 3]
datos = {k: v for k, v in zip(claves, valores)}
print(datos['b'] * 3)
```

A) Error: zip no funciona con listas de diferente tipo.

B) 2

C) 6 ✅

D) 'bbb'

---

**Pregunta 3**

Ejecutamos el siguiente código. ¿Qué imprimirá por pantalla?

```python
def acumulador(n, lista=[]):
    lista.append(n)
    return lista

print(acumulador(1))
print(acumulador(2))
```

A) [1] y [2]

B) [1] y [1, 2] ✅

C) Error: los argumentos mutables no están permitidos como valor por defecto.

D) [1, 2] y [1, 2]

---

**Pregunta 4**

¿Cuál es la principal diferencia entre Parquet y CSV?

A) CSV soporta tipos complejos; Parquet no.

B) Parquet almacena datos en formato columnar y aplica compresión eficiente. ✅

C) CSV es más rápido para consultas analíticas sobre columnas.

D) Parquet no es compatible con Pandas.

---

**Pregunta 5**

Tenemos un pipeline de carga de datos. ¿Qué ocurre al ejecutar este fragmento si el archivo no existe?

```python
import pandas as pd

def cargar_datos(ruta):
    """
    1) Leer CSV
    2) Eliminar filas con NaN
    3) Devolver el DataFrame limpio
    """
    df = pd.read_csv(ruta)
    df = df.dropna()
    return df

resultado = cargar_datos('no_existe.csv')
```

A) Devuelve un DataFrame vacío.

B) Devuelve None.

C) Lanza FileNotFoundError. ✅

D) Lanza un ValueError.

---

**Pregunta 6**

Queremos inspeccionar un DataFrame con Pandas. ¿Qué método muestra las primeras 5 filas por defecto?

A) `df.tail()`

B) `df.info()`

C) `df.head()` ✅

D) `df.describe()`

---

**Pregunta 7**

Tenemos el siguiente código con Polars. ¿Qué hace la línea marcada?

```python
import polars as pl

df = pl.read_csv('ventas.csv')
# Línea marcada:
resultado = df.filter(pl.col('importe') > 1000)
```

A) Ordena el DataFrame por la columna 'importe' descendente.

B) Elimina la columna 'importe'.

C) Selecciona solo las filas donde 'importe' es mayor que 1000. ✅

D) Crea una nueva columna llamada 'resultado'.

---

**Pregunta 8**

Necesitamos instalar la librería `scikit-learn` en un entorno virtual. ¿Cuál es el comando correcto?

A) `python install scikit-learn`

B) `pip install scikit-learn` ✅

C) `pip download scikit-learn`

D) `conda get scikit-learn`

---

## UNIDAD 2 — Minería de texto con Python

---

**Pregunta 9**

Tenemos el siguiente código de preprocesamiento de texto. ¿Qué devuelve `resultado`?

```python
import re

texto = "Hola, ¿cómo estás? Tengo 3 manzanas."
resultado = re.findall(r'\b\w+\b', texto)
```

A) Una lista con todas las palabras y números del texto. ✅

B) Una lista con solo las palabras en mayúscula.

C) Un string sin signos de puntuación.

D) Error: `\b` no está soportado en Python.

---

**Pregunta 10**

Implementamos un pipeline de limpieza de texto. ¿Qué hace el siguiente fragmento?

```python
import re

def limpiar_texto(texto):
    """
    1) Pasar a minúsculas
    2) Eliminar URLs
    3) Eliminar caracteres no alfabéticos
    """
    texto = texto.lower()
    texto = re.sub(r'http\S+', '', texto)
    texto = re.sub(r'[^a-záéíóúüñ\s]', '', texto)
    return texto.strip()
```

A) Tokeniza el texto por oraciones.

B) Limpia el texto eliminando URLs y caracteres no alfabéticos, pasándolo a minúsculas. ✅

C) Elimina stopwords del texto.

D) Convierte el texto a encoding UTF-8.

---

**Pregunta 11**

Usamos NLTK para tokenizar y contar palabras. ¿Qué contiene `freq_dist` tras ejecutar el código?

```python
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

texto = "el gato come el ratón el gato duerme"
tokens = word_tokenize(texto)
freq_dist = FreqDist(tokens)
print(freq_dist.most_common(1))
```

A) [('gato', 1)]

B) [('el', 3)] ✅

C) Error: FreqDist requiere un corpus descargado.

D) [('el', 2)]

---

**Pregunta 12**

¿Cuál es la diferencia principal entre stemming y lematización?

A) El stemming usa un vocabulario; la lematización trunca por reglas fijas.

B) El stemming trunca la palabra por reglas morfológicas; la lematización devuelve la forma canónica del diccionario. ✅

C) No hay diferencia: ambas técnicas son equivalentes.

D) La lematización solo funciona en inglés.

---

**Pregunta 13**

Aplicamos spaCy a un texto en inglés. ¿Qué atributo del token devuelve su categoría gramatical (POS tag)?

A) `token.dep_`

B) `token.lemma_`

C) `token.pos_` ✅

D) `token.ent_type_`

---

**Pregunta 14**

Creamos una nube de palabras con frecuencias. ¿Qué produce el siguiente código?

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

freq = {'Python': 50, 'datos': 30, 'NLP': 45, 'modelo': 20}
wc = WordCloud(width=800, height=400, background_color='white')
wc.generate_from_frequencies(freq)
plt.imshow(wc)
plt.axis('off')
plt.show()
```

A) Una nube de palabras donde todas las palabras tienen el mismo tamaño.

B) Una nube de palabras donde el tamaño de cada palabra es proporcional a su frecuencia. ✅

C) Error: `generate_from_frequencies` no existe en WordCloud.

D) Una nube de palabras ordenada alfabéticamente.

---

**Pregunta 15**

Usamos Pandas para realizar minería de texto sobre un DataFrame. ¿Qué hace la línea marcada?

```python
import pandas as pd

df = pd.DataFrame({'texto': ['Hola Mundo', 'Python es genial', 'NLP con pandas']})
# Línea marcada:
df['longitud'] = df['texto'].str.split().str.len()
```

A) Cuenta el número de caracteres de cada texto.

B) Convierte cada texto a lista de caracteres.

C) Cuenta el número de palabras de cada texto. ✅

D) Elimina los espacios de cada texto.

---

**Pregunta 16**

¿Cuál de los siguientes estándares de codificación puede representar cualquier carácter de cualquier idioma del mundo?

A) ASCII

B) ISO-8859-1

C) Unicode (UTF-8) ✅

D) Base64

---

## UNIDAD 3 — Fuentes de datos de tipo texto

---

**Pregunta 17**

Usamos BeautifulSoup para extraer datos de una página web estática. ¿Qué devuelve el siguiente fragmento?

```python
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>Título principal</h1>
    <p class="resumen">Este es el resumen.</p>
    <p class="resumen">Segundo párrafo.</p>
  </body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
resultado = soup.find_all('p', class_='resumen')
print(len(resultado))
```

A) 0

B) 1

C) 2 ✅

D) Error: `class` es una palabra reservada de Python.

---

**Pregunta 18**

Necesitamos hacer scraping de una página que carga contenido dinámicamente con JavaScript. ¿Qué herramienta debemos usar?

A) BeautifulSoup directamente sobre `requests.get()`.

B) Solo el módulo `re` para parsear el HTML.

C) Selenium, porque puede interactuar con el DOM tras la ejecución de JavaScript. ✅

D) Pandas `read_html()`, que maneja JavaScript automáticamente.

---

**Pregunta 19**

Implementamos un pipeline con PySpark. ¿Qué hace el siguiente fragmento?

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TextPipeline").getOrCreate()
df = spark.read.json("hdfs://datos/tweets/*.json")
resultado = df.filter(df['lang'] == 'es').count()
spark.stop()
```

A) Carga todos los JSON, filtra los tweets en español y devuelve su conteo. ✅

B) Escribe los tweets en español en un nuevo archivo JSON.

C) Devuelve el número total de archivos JSON en el directorio.

D) Error: PySpark no puede leer múltiples JSON con wildcard.

---

**Pregunta 20**

¿Cuál es la ventaja principal de usar PySpark frente a Pandas cuando el dataset supera la RAM disponible?

A) PySpark usa menos memoria porque elimina columnas automáticamente.

B) PySpark permite procesar datos distribuidos en un clúster sin cargar todo en memoria. ✅

C) PySpark carga automáticamente los datos en GPU.

D) No hay diferencia: Pandas también puede manejar datos fuera de memoria.

---

**Pregunta 21**

Realizamos un merge de dos DataFrames con Pandas. ¿Cuántas filas tendrá `df_merged`?

```python
import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 3], 'nombre': ['Ana', 'Luis', 'Mar']})
df2 = pd.DataFrame({'id': [2, 3, 4], 'ciudad': ['Madrid', 'BCN', 'SEV']})

df_merged = pd.merge(df1, df2, on='id', how='inner')
```

A) 3

B) 4

C) 2 ✅

D) 6

---

**Pregunta 22**

Usamos la API de Reddit con `praw`. ¿Qué representa el siguiente bucle?

```python
import praw

reddit = praw.Reddit(client_id='...', client_secret='...', user_agent='script')
for submission in reddit.subreddit('python').hot(limit=10):
    print(submission.title)
```

A) Descarga los 10 comentarios más votados del subreddit 'python'.

B) Imprime los títulos de los 10 posts más populares del subreddit 'python'. ✅

C) Busca los 10 usuarios más activos del subreddit 'python'.

D) Error: `praw` no tiene el método `.hot()`.

---

**Pregunta 23**

Creamos una función para leer un CSV con Polars. ¿Qué diferencia clave tiene respecto a Pandas?

```python
import polars as pl

df = pl.read_csv('datos.csv')
df2 = df.with_columns(pl.col('precio') * 1.21)
```

A) En Polars, `with_columns` modifica el DataFrame original `df`.

B) En Polars, el DataFrame es inmutable: `with_columns` devuelve un nuevo DataFrame sin modificar `df`. ✅

C) Error: Polars no tiene el método `with_columns`.

D) Polars no puede multiplicar columnas numéricas directamente.

---

## UNIDAD 4 — Modelización y análisis en minería de texto

---

**Pregunta 24**

Preparamos corpus para LDA con Gensim. ¿Qué representa `corpus` en el siguiente fragmento?

```python
from gensim import corpora

textos = [['gato', 'perro', 'animal'], ['python', 'datos', 'código'], ['animal', 'datos']]
dictionary = corpora.Dictionary(textos)
corpus = [dictionary.doc2bow(texto) for texto in textos]
```

A) Una lista de strings con los documentos originales.

B) Una lista de listas donde cada elemento es un par (id_palabra, frecuencia) por documento. ✅

C) Una matriz TF-IDF de todos los documentos.

D) Error: `doc2bow` solo acepta un documento, no una lista.

---

**Pregunta 25**

Entrenamos un modelo LDA. ¿Qué hiperparámetro controla el número de tópicos a descubrir?

```python
from gensim.models import LdaModel

modelo = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, passes=10)
```

A) `passes`

B) `id2word`

C) `num_topics` ✅

D) `corpus`

---

**Pregunta 26**

Analizamos sentimientos con TextBlob. ¿Qué devuelve `blob.sentiment.polarity` para la frase "This product is absolutely terrible"?

A) Un valor positivo cercano a 1.

B) Un valor exactamente igual a 0.

C) Un valor negativo. ✅

D) Error: TextBlob no analiza frases negativas con "absolutely".

---

**Pregunta 27**

Implementamos un clasificador de sentimientos con TextBlob. Si `polarity >= 0` se etiqueta como "positive", ¿qué ocurre con una frase de polarity exactamente 0?

```python
from textblob import TextBlob

def clasificar(texto):
    p = TextBlob(texto).sentiment.polarity
    return "positive" if p >= 0 else "negative"
```

A) Se lanza una excepción porque 0 no es positivo ni negativo.

B) Se etiqueta como "negative".

C) Se etiqueta como "positive". ✅

D) Se etiqueta como "neutral".

---

**Pregunta 28**

Usamos NLTK para parsing de dependencias. ¿Qué analiza un `DependencyGraph`?

A) Las frecuencias de aparición de cada token.

B) Las relaciones gramaticales entre palabras de una oración (sujeto, objeto, etc.). ✅

C) Los tópicos latentes de un corpus completo.

D) El sentimiento de cada oración del texto.

---

**Pregunta 29**

Implementamos un resumidor extractivo. ¿Qué hace el siguiente fragmento?

```python
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

def resumir(texto, n=3):
    """
    1) Tokenizar en oraciones
    2) Calcular frecuencia de palabras
    3) Puntuar oraciones por suma de frecuencias de sus palabras
    4) Devolver las n oraciones con mayor puntuación
    """
    oraciones = sent_tokenize(texto)
    palabras = word_tokenize(texto.lower())
    freq = FreqDist(palabras)
    puntuaciones = {s: sum(freq[w] for w in word_tokenize(s.lower())) for s in oraciones}
    return sorted(oraciones, key=lambda s: puntuaciones[s], reverse=True)[:n]
```

A) Genera un resumen abstractivo reescribiendo las frases más importantes.

B) Devuelve las 3 oraciones con mayor densidad de palabras frecuentes. ✅

C) Devuelve las 3 oraciones más largas del texto.

D) Aplica LDA para encontrar las oraciones más representativas de cada tópico.

---

**Pregunta 30**

Tenemos el siguiente pipeline de análisis. ¿Qué imprime el código si el texto tiene 10 oraciones, de las cuales 4 contienen la palabra "datos"?

```python
import spacy

nlp = spacy.load('en_core_web_sm')
texto = "... (10 oraciones, 4 contienen 'datos') ..."
doc = nlp(texto)

conteo = sum(1 for sent in doc.sents if 'datos' in sent.text)
print(conteo)
```

A) 10

B) 0

C) 4 ✅

D) Error: `doc.sents` no está disponible sin el componente `sentencizer`.

---

## UNIDAD 5 — Análisis de redes sociales con Python

---

**Pregunta 31**

Creamos un grafo con NetworkX. ¿Cuántos nodos y aristas tiene el grafo tras ejecutar el código?

```python
import networkx as nx

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 4)])
print(G.number_of_nodes(), G.number_of_edges())
```

A) 3 nodos, 3 aristas.

B) 4 nodos, 2 aristas.

C) 4 nodos, 3 aristas. ✅

D) Error: no se pueden añadir nodos y aristas por separado.

---

**Pregunta 32**

¿Qué mide la **betweenness centrality** de un nodo en una red?

A) El número de conexiones directas que tiene un nodo.

B) La cercanía media del nodo al resto de nodos de la red.

C) La frecuencia con la que un nodo aparece en los caminos más cortos entre otros pares de nodos. ✅

D) El porcentaje de vecinos comunes con el resto de nodos.

---

**Pregunta 33**

Analizamos la red de emails del caso Enron con NetworkX. ¿Qué devuelve el siguiente fragmento?

```python
import networkx as nx

G = nx.DiGraph()
G.add_edge('alice', 'bob')
G.add_edge('bob', 'alice')
G.add_edge('alice', 'carol')

print(G.in_degree('bob'))
```

A) 2

B) 0

C) 1 ✅

D) Error: `DiGraph` no tiene el método `in_degree`.

---

**Pregunta 34**

Queremos detectar comunidades en una red. ¿Qué algoritmo es el más habitual en NetworkX para esta tarea?

A) PageRank

B) Algoritmo de Louvain (greedy modularity communities). ✅

C) Dijkstra

D) BFS (Breadth First Search)

---

**Pregunta 35**

Implementamos un análisis de métricas de red. ¿Qué calcula `nx.density(G)`?

```python
import networkx as nx

G = nx.karate_club_graph()
print(nx.density(G))
```

A) El número total de nodos del grafo.

B) El nodo con mayor número de conexiones.

C) La proporción de aristas existentes respecto al máximo posible. ✅

D) El diámetro máximo del grafo.

---

**Pregunta 36**

Visualizamos una red con Matplotlib y NetworkX. ¿Qué controla el parámetro `pos` en `nx.draw`?

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()
```

A) El color de los nodos.

B) La posición (coordenadas x, y) de cada nodo en el dibujo. ✅

C) El tamaño de los nodos.

D) El algoritmo de detección de comunidades.

---

**Pregunta 37**

¿Qué tipo de grafo debemos usar en NetworkX para modelar una red de emails donde importa quién envía y quién recibe?

A) `nx.Graph()`, porque los emails son conexiones simétricas.

B) `nx.MultiGraph()`, porque puede haber múltiples emails entre el mismo par.

C) `nx.DiGraph()`, porque la dirección del envío es relevante. ✅

D) `nx.BiGraph()`, para separar remitentes y destinatarios.

---

## UNIDAD 6 — Deep Learning y LLMs con Python

---

**Pregunta 38**

Usamos Hugging Face Transformers para clasificación de sentimientos. ¿Qué devuelve `resultado`?

```python
from transformers import pipeline

clasificador = pipeline('sentiment-analysis')
resultado = clasificador("I love working with Python and NLP!")
print(resultado)
```

A) Un float con el valor de polaridad entre -1 y 1.

B) Una lista con el label predicho y su score de confianza. ✅

C) Un embedding vectorial de la frase.

D) Error: `pipeline` requiere indicar explícitamente el nombre del modelo.

---

**Pregunta 39**

Cargamos un modelo preentrenado BERT con Hugging Face. ¿Qué representa el `tokenizer`?

```python
from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

inputs = tokenizer("Hello, world!", return_tensors='pt')
outputs = model(**inputs)
```

A) Un módulo que convierte el texto en embeddings directamente.

B) Un módulo que convierte el texto en IDs de tokens y máscaras de atención que el modelo puede procesar. ✅

C) El módulo de decodificación que convierte las salidas del modelo en texto legible.

D) Un módulo que realiza la predicción de la tarea final (clasificación, NER, etc.).

---

**Pregunta 40**

¿Cuál es la principal razón para preferir GPU sobre CPU al entrenar o hacer inferencia con LLMs?

A) Las GPUs tienen mayor capacidad de almacenamiento en disco.

B) Las GPUs ejecutan operaciones matriciales en paralelo masivo, reduciendo drásticamente los tiempos de cómputo. ✅

C) Las CPUs no soportan librerías como PyTorch o TensorFlow.

D) Las GPUs consumen menos energía que las CPUs para tareas de NLP.

---

**Pregunta 41**

Entrenamos una red neuronal con Keras para clasificación de texto. ¿Qué hace la capa `Embedding` en el siguiente modelo?

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense

model = Sequential([
    Embedding(input_dim=10000, output_dim=64),
    GlobalAveragePooling1D(),
    Dense(1, activation='sigmoid')
])
```

A) Convierte los IDs de tokens en vectores densos de dimensión 64. ✅

B) Aplica atención multi-cabeza sobre los tokens.

C) Normaliza los vectores de entrada al rango [0, 1].

D) Reduce la secuencia a su token más relevante.

---

**Pregunta 42**

Implementamos fine-tuning de un modelo con Hugging Face. ¿Qué hace el parámetro `num_train_epochs=3` en el siguiente fragmento?

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir='./resultados',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    evaluation_strategy='epoch'
)
```

A) Divide el dataset en 3 particiones para validación cruzada.

B) Indica que el modelo recorrerá el conjunto de entrenamiento completo 3 veces. ✅

C) Limita el entrenamiento a 3 batches por época.

D) Guarda el modelo cada 3 pasos de entrenamiento.

---

**Pregunta 43**

Usamos PyTorch para definir un modelo de clasificación de texto. ¿Qué hace `optimizer.zero_grad()` en el bucle de entrenamiento?

```python
import torch

for batch in dataloader:
    optimizer.zero_grad()
    outputs = model(**batch)
    loss = outputs.loss
    loss.backward()
    optimizer.step()
```

A) Reinicia los parámetros del modelo a sus valores iniciales.

B) Limpia los gradientes acumulados del paso anterior para que no interfieran en el cálculo actual. ✅

C) Detiene el cálculo del gradiente para los parámetros congelados.

D) Pone a cero la función de pérdida acumulada.

---

**Pregunta 44**

Subimos un modelo a Hugging Face Hub. ¿Qué hace el siguiente fragmento?

```python
from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained('./mi_modelo_entrenado')
model.push_to_hub('mi_usuario/clasificador-sentimientos')
```

A) Descarga el modelo 'clasificador-sentimientos' desde el Hub al directorio local.

B) Publica el modelo local en el Hub de Hugging Face bajo el nombre indicado, haciéndolo accesible públicamente. ✅

C) Crea una copia de seguridad local del modelo en formato ONNX.

D) Error: `push_to_hub` solo está disponible para tokenizadores, no para modelos.

---

**Pregunta 45**

Comparamos TensorFlow y PyTorch para NLP. ¿Cuál de las siguientes afirmaciones es correcta?

A) PyTorch no puede usarse en producción; es solo para investigación.

B) TensorFlow usa grafos de computación dinámicos por defecto desde la versión 2.x; PyTorch siempre ha usado grafos dinámicos (eager execution). ✅

C) Solo TensorFlow es compatible con Hugging Face Transformers.

D) TensorFlow y PyTorch son incompatibles con GPUs NVIDIA.

---

*Fin del Modelo 1 — 45 preguntas*
