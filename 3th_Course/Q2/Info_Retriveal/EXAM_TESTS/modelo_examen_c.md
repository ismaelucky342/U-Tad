# Modelo de Examen — Modelo 3
## Ingeniería de Datos y NLP con Python
### 45 preguntas tipo test · Una sola respuesta correcta

---

**Pregunta 1** *(U2)*

Procesamos tweets con NLTK. ¿Qué devuelve `tokens` tras ejecutar el fragmento?

```python
from nltk.tokenize import TweetTokenizer

tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
tokens = tknzr.tokenize("@usuario Estoooooy muy feliz!!! 😊 #Python")
```

A) `['Estoooooy', 'muy', 'feliz', 'Python']`

B) `['Estoy', 'muy', 'feliz!!!', '#Python']`

C) `['Estooo', 'muy', 'feliz!!!', '😊', '#Python']` ✅

D) Error: `TweetTokenizer` no admite emojis.

---

**Pregunta 2** *(U4)*

Entrenamos un modelo LDA y queremos visualizar los tópicos. ¿Qué devuelve `modelo.print_topics(num_topics=2, num_words=3)`?

```python
from gensim.models import LdaModel

modelo = LdaModel(corpus=corpus, id2word=dictionary, num_topics=4, passes=15)
print(modelo.print_topics(num_topics=2, num_words=3))
```

A) Una lista de 4 tópicos con todas sus palabras del vocabulario.

B) Una lista de 2 tuplas con el índice del tópico y las 3 palabras más representativas con su peso. ✅

C) Un DataFrame con la distribución de tópicos por documento.

D) Error: `print_topics` no acepta `num_words` como parámetro.

---

**Pregunta 3** *(U1)*

Implementamos una función de transformación. ¿Qué ocurre al llamar a `transformar(df)` si la columna `'fecha'` contiene strings con formato `'2024-01-15'`?

```python
import pandas as pd

def transformar(df):
    """
    1) Convertir columna 'fecha' a datetime
    2) Extraer el mes
    3) Agrupar por mes y sumar 'ventas'
    """
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['mes'] = df['fecha'].dt.month
    return df.groupby('mes')['ventas'].sum()
```

A) Error: `pd.to_datetime` no puede convertir strings con guiones.

B) Devuelve una Serie con la suma de ventas por número de mes. ✅

C) Devuelve un DataFrame con todas las columnas originales más 'mes'.

D) Devuelve una Serie con la media de ventas por mes.

---

**Pregunta 4** *(U6 — teórica)*

¿Qué ventaja tienen las **TPUs** frente a las GPUs para el entrenamiento de LLMs?

A) Las TPUs tienen mayor capacidad de almacenamiento en RAM que las GPUs.

B) Las TPUs están diseñadas específicamente para operaciones matriciales de precisión reducida usadas en deep learning, ofreciendo mayor throughput para modelos grandes. ✅

C) Las TPUs son más baratas y accesibles que las GPUs para uso doméstico.

D) Las TPUs son compatibles con cualquier framework; las GPUs solo con CUDA.

---

**Pregunta 5** *(U3)*

Hacemos scraping con BeautifulSoup. ¿Qué devuelve `dato` tras ejecutar el fragmento?

```python
from bs4 import BeautifulSoup

html = """
<table>
  <tr><th>Nombre</th><th>Precio</th></tr>
  <tr><td>Libro A</td><td>12.99</td></tr>
  <tr><td>Libro B</td><td>9.50</td></tr>
</table>
"""
soup = BeautifulSoup(html, 'html.parser')
filas = soup.find_all('tr')
dato = filas[1].find_all('td')[1].text
```

A) `'Nombre'`

B) `'Libro A'`

C) `'12.99'` ✅

D) Error: el índice 1 está fuera de rango.

---

**Pregunta 6** *(U2)*

Aplicamos normalización de texto. ¿Qué imprime el siguiente código?

```python
import unicodedata

texto = "café résumé naïve"
normalizado = unicodedata.normalize('NFD', texto)
sin_acentos = ''.join(c for c in normalizado if unicodedata.category(c) != 'Mn')
print(sin_acentos)
```

A) `'cafe resume naive'` ✅

B) `'café résumé naïve'` (sin cambios)

C) Error: `unicodedata.normalize` no acepta texto con espacios.

D) `'caf rsum nav'`

---

**Pregunta 7** *(U5)*

Calculamos el diámetro de una red con NetworkX. ¿Qué representa `nx.diameter(G)`?

A) El número total de aristas del grafo.

B) La longitud del camino más corto entre los dos nodos más alejados del grafo. ✅

C) La media de todas las distancias entre pares de nodos.

D) El número de componentes conectadas del grafo.

---

**Pregunta 8** *(U4)*

Implementamos análisis de sentimiento con spaCy y un componente personalizado. ¿Qué ocurre si `doc.cats` devuelve `{'POSITIVE': 0.85, 'NEGATIVE': 0.15}`?

```python
import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("The new update is absolutely amazing")
etiqueta = max(doc.cats, key=doc.cats.get)
print(etiqueta)
```

A) `'NEGATIVE'`

B) `0.85`

C) `'POSITIVE'` ✅

D) Error: `doc.cats` solo existe si el modelo tiene el componente `textcat`.

---

**Pregunta 9** *(U1 — teórica)*

¿Qué diferencia principal existe entre una **lista** y una **tupla** en Python?

A) Las listas solo pueden contener elementos del mismo tipo; las tuplas pueden mezclar tipos.

B) Las tuplas son inmutables (no se pueden modificar tras su creación); las listas son mutables. ✅

C) Las listas tienen acceso por índice; las tuplas no.

D) Las tuplas no pueden usarse dentro de otros contenedores.

---

**Pregunta 10** *(U3)*

Procesamos un dataset masivo con PySpark. ¿Qué hace `cache()` en el siguiente fragmento?

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("App").getOrCreate()
df = spark.read.parquet("hdfs://datos/logs.parquet")
df_filtrado = df.filter(df['nivel'] == 'ERROR').cache()

conteo = df_filtrado.count()
muestra = df_filtrado.limit(10).collect()
```

A) Guarda `df_filtrado` en disco como archivo temporal.

B) Almacena `df_filtrado` en memoria para evitar recalcularlo en cada acción posterior. ✅

C) Duplica el DataFrame para tener una copia de seguridad.

D) Error: `cache()` no está disponible en DataFrames de PySpark, solo en RDDs.

---

**Pregunta 11** *(U6)*

Implementamos un pipeline de clasificación con Hugging Face. ¿Cuántas etiquetas puede predecir el modelo del siguiente fragmento?

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model = AutoModelForSequenceClassification.from_pretrained('mi_modelo')
tokenizer = AutoTokenizer.from_pretrained('mi_modelo')

inputs = tokenizer("Texto de prueba", return_tensors='pt')
outputs = model(**inputs)
print(outputs.logits.shape)  # torch.Size([1, 3])
```

A) 1

B) 2

C) 3 ✅

D) Depende del texto de entrada.

---

**Pregunta 12** *(U2)*

Implementamos un pipeline de limpieza con spaCy. ¿Qué hace el siguiente fragmento?

```python
import spacy

nlp = spacy.load('es_core_news_sm')

def limpiar(texto):
    doc = nlp(texto)
    return [token.lemma_ for token in doc
            if not token.is_stop and not token.is_punct and token.is_alpha]

resultado = limpiar("Los gatos corren rápidamente por el jardín.")
```

A) Devuelve todos los tokens del texto en minúsculas.

B) Devuelve los lemas de las palabras significativas, excluyendo stopwords y puntuación. ✅

C) Devuelve las entidades nombradas del texto.

D) Error: `token.lemma_` no está disponible en modelos de español.

---

**Pregunta 13** *(U5)*

Visualizamos una red con Gephi. ¿Cuál es la principal ventaja de Gephi frente a visualizar con Matplotlib + NetworkX?

A) Gephi es más rápido que NetworkX para calcular métricas de red.

B) Gephi ofrece una interfaz interactiva y visual para explorar y personalizar redes grandes sin escribir código. ✅

C) Gephi puede analizar grafos dirigidos; NetworkX no.

D) Gephi genera automáticamente informes en PDF con las métricas de la red.

---

**Pregunta 14** *(U4 — teórica)*

¿Qué es el **modelo Bag of Words (BoW)** en NLP?

A) Un modelo que representa el texto como una secuencia ordenada de tokens con sus posiciones.

B) Un modelo que representa un documento como un vector de frecuencias de palabras, ignorando el orden. ✅

C) Un modelo neuronal que genera embeddings contextuales para cada token.

D) Un modelo que agrupa palabras semánticamente similares en el mismo cluster.

---

**Pregunta 15** *(U1)*

Usamos Pandas para unir dos DataFrames. ¿Qué tipo de join produce el siguiente código?

```python
import pandas as pd

df1 = pd.DataFrame({'id': [1, 2, 3], 'a': ['x', 'y', 'z']})
df2 = pd.DataFrame({'id': [2, 3, 4], 'b': ['p', 'q', 'r']})

resultado = pd.merge(df1, df2, on='id', how='left')
print(resultado.shape)
```

A) `(2, 3)` porque solo conserva los IDs comunes.

B) `(4, 3)` porque conserva todos los IDs de ambos DataFrames.

C) `(3, 3)` porque conserva todas las filas de `df1`, con NaN donde no hay match en `df2`. ✅

D) Error: `how='left'` no está soportado en `pd.merge`.

---

**Pregunta 16** *(U3)*

Usamos la API de Reddit para recopilar datos. ¿Qué tipo de autenticación usa `praw` por defecto para aplicaciones de solo lectura (script apps)?

A) Autenticación básica con usuario y contraseña en cada petición.

B) OAuth 2.0 con `client_id`, `client_secret` y `user_agent`. ✅

C) API key enviada en la cabecera HTTP `X-Api-Key`.

D) No requiere autenticación para datos públicos de Reddit.

---

**Pregunta 17** *(U6)*

Implementamos inferencia optimizada con PyTorch. ¿Por qué usamos `torch.no_grad()` en el siguiente fragmento?

```python
import torch

model.eval()
with torch.no_grad():
    outputs = model(**inputs)
    predicciones = torch.argmax(outputs.logits, dim=-1)
```

A) Para evitar que el modelo actualice sus pesos durante la inferencia.

B) Para desactivar el cálculo del grafo de gradientes, reduciendo el uso de memoria y acelerando la inferencia. ✅

C) Para que el modelo use CPU en lugar de GPU durante la predicción.

D) Para congelar los pesos de las capas de embedding solamente.

---

**Pregunta 18** *(U2)*

Calculamos frecuencias de bigramas con NLTK. ¿Qué contiene `bigramas[:2]`?

```python
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

texto = "el gato negro duerme en el sofá negro"
tokens = word_tokenize(texto)
bigramas = Counter(ngrams(tokens, 2)).most_common(2)
print(bigramas)
```

A) `[('el', 'gato'), ('gato', 'negro')]`

B) Los 2 bigramas más frecuentes del texto, siendo `('el', 'sofá')` el más común.

C) Los 2 bigramas más frecuentes; `('negro', 'duerme')` y `('gato', 'negro')` empatan en frecuencia 1.

D) Los 2 bigramas más frecuentes del texto; como `('el', 'gato')` aparece 1 vez y `('negro', 'duerme')` también, el más común depende del orden; pero ningún bigrama se repite excepto si hay coincidencia real en el texto. ✅

---

**Pregunta 19** *(U5)*

Analizamos una red de retweets. Tenemos el siguiente código. ¿Qué representa `G.edges(data=True)`?

```python
import networkx as nx

G = nx.DiGraph()
G.add_edge('Alice', 'Bob', weight=5)
G.add_edge('Bob', 'Carol', weight=2)

for u, v, attrs in G.edges(data=True):
    print(u, v, attrs)
```

A) Imprime solo los nodos origen de cada arista.

B) Imprime cada arista con su nodo origen, nodo destino y diccionario de atributos (como el peso). ✅

C) Error: `data=True` solo funciona en grafos no dirigidos.

D) Imprime las aristas sin atributos porque `data=True` es ignorado.

---

**Pregunta 20** *(U4)*

Evaluamos un modelo LDA con la métrica de coherencia. ¿Qué valor indica un modelo con mejor calidad de tópicos?

```python
from gensim.models import CoherenceModel

cm = CoherenceModel(model=lda, texts=textos_tokenizados,
                    dictionary=dictionary, coherence='c_v')
score = cm.get_coherence()
print(score)
```

A) Un valor cercano a 0, que indica tópicos muy equilibrados.

B) Un valor negativo, que indica que las palabras del tópico son muy distintas entre sí.

C) Un valor más alto (cercano a 1), que indica mayor coherencia semántica entre las palabras de cada tópico. ✅

D) El valor de coherencia no tiene interpretación clara; solo sirve para comparar modelos entre sí de forma relativa.

---

**Pregunta 21** *(U1)*

Construimos un módulo Python propio. ¿Qué archivo es imprescindible para que Python reconozca un directorio como paquete?

A) `setup.py`

B) `requirements.txt`

C) `__init__.py` ✅

D) `main.py`

---

**Pregunta 22** *(U3)*

Implementamos un pipeline de extracción de datos de Twitter y almacenamiento. ¿Cuántos tweets se guardarán en el CSV si la API devuelve páginas de 100 tweets y fijamos `max_results=100`?

```python
import tweepy, csv

client = tweepy.Client(bearer_token='...')
respuesta = client.search_recent_tweets(
    query='#MachineLearning lang:en',
    max_results=100,
    tweet_fields=['created_at', 'author_id']
)

with open('tweets.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'text', 'created_at'])
    for tweet in respuesta.data:
        writer.writerow([tweet.id, tweet.text, tweet.created_at])
```

A) Más de 100, porque la API pagina automáticamente.

B) Exactamente los tweets devueltos en la única página de respuesta, hasta un máximo de 100. ✅

C) Exactamente 100, porque `max_results=100` garantiza siempre ese número.

D) Error: `csv.writer` no puede escribir objetos `Tweet` de Tweepy.

---

**Pregunta 23** *(U6)*

Implementamos un chat local con un modelo del Hub. ¿Qué hace `model.generate` en el siguiente fragmento?

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained('gpt2')
model = AutoModelForCausalLM.from_pretrained('gpt2')

inputs = tokenizer("La inteligencia artificial", return_tensors='pt')
output = model.generate(**inputs, max_new_tokens=30, do_sample=True, temperature=0.7)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

A) Clasifica el texto de entrada en una de las categorías del modelo.

B) Genera una continuación del texto de entrada de hasta 30 tokens nuevos con muestreo estocástico. ✅

C) Traduce el texto al inglés usando el modelo GPT-2.

D) Error: GPT-2 no soporta el parámetro `temperature`.

---

**Pregunta 24** *(U2 — teórica)*

¿Qué son las **stopwords** en el contexto de NLP?

A) Palabras que causan errores en los tokenizadores por su longitud.

B) Palabras de alta frecuencia y bajo contenido semántico (artículos, preposiciones, conjunciones) que habitualmente se eliminan en el preprocesado. ✅

C) Palabras fuera del vocabulario del modelo (OOV tokens).

D) Palabras que contienen caracteres especiales o números.

---

**Pregunta 25** *(U5)*

Implementamos detección de anomalías en una red bancaria. ¿Qué característica de un nodo podría indicar comportamiento fraudulento?

```python
import networkx as nx

G = nx.DiGraph()
# ... (grafo con transacciones entre cuentas)
bc = nx.betweenness_centrality(G, normalized=True)
sospechosos = [n for n, v in bc.items() if v > 0.8]
```

A) Nodos con degree muy bajo, porque hacen pocas transacciones.

B) Nodos con muy alta betweenness centrality, ya que actúan como intermediarios en un número inusualmente alto de flujos de dinero. ✅

C) Nodos que solo tienen aristas entrantes (in-degree > 0, out-degree == 0).

D) Nodos pertenecientes a la comunidad más grande de la red.

---

**Pregunta 26** *(U4)*

Construimos un sistema de resumen. ¿Qué diferencia hay entre un resumen **extractivo** y uno **abstractivo**?

A) El extractivo usa modelos de deep learning; el abstractivo usa reglas estadísticas.

B) El extractivo selecciona y devuelve oraciones del texto original; el abstractivo genera texto nuevo que puede no aparecer literalmente en el original. ✅

C) El extractivo resume textos cortos; el abstractivo solo funciona con documentos largos.

D) No hay diferencia práctica: ambos enfoques producen el mismo resultado.

---

**Pregunta 27** *(U1)*

Ejecutamos el siguiente fragmento con Polars. ¿Qué imprime `resultado`?

```python
import polars as pl

df = pl.DataFrame({
    'producto': ['A', 'B', 'A', 'C', 'B'],
    'unidades': [10, 5, 8, 12, 3]
})
resultado = df.group_by('producto').agg(pl.col('unidades').sum()).sort('unidades', descending=True)
print(resultado['producto'][0])
```

A) `'B'`

B) `'C'`

C) `'A'` ✅

D) Error: `group_by` y `sort` no pueden encadenarse en Polars.

---

**Pregunta 28** *(U3)*

Implementamos un pipeline completo de scraping y almacenamiento. ¿Qué problema puede surgir si no gestionamos el `time.sleep` entre peticiones?

```python
import requests
from bs4 import BeautifulSoup
import time

urls = [f"https://ejemplo.com/pagina/{i}" for i in range(1, 100)]

for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # ... extracción de datos
    # time.sleep(1)  # comentado
```

A) El scraper será más lento porque las peticiones se encolan.

B) El servidor puede detectar el tráfico automatizado y bloquear nuestra IP por exceso de peticiones. ✅

C) Los datos extraídos serán incorrectos porque las páginas no tendrán tiempo de cargarse.

D) No hay ningún problema: los servidores web están diseñados para gestionar peticiones masivas.

---

**Pregunta 29** *(U6)*

Usamos `Trainer` de Hugging Face para fine-tuning. ¿Qué hace el parámetro `evaluation_strategy='epoch'`?

```python
from transformers import TrainingArguments, Trainer

args = TrainingArguments(
    output_dir='./modelo',
    num_train_epochs=5,
    evaluation_strategy='epoch',
    save_strategy='epoch',
    load_best_model_at_end=True
)
```

A) Evalúa el modelo una única vez al final del entrenamiento completo.

B) Evalúa el modelo al final de cada época sobre el conjunto de validación. ✅

C) Evalúa el modelo cada 100 steps independientemente del número de epochs.

D) Error: `evaluation_strategy` y `save_strategy` no pueden tener el mismo valor.

---

**Pregunta 30** *(U2)*

Aplicamos regex con grupos de captura. ¿Qué devuelve `re.search` en el siguiente fragmento?

```python
import re

log = "2024-05-12 ERROR: conexión rechazada en puerto 8080"
match = re.search(r'(\d{4}-\d{2}-\d{2})\s+(ERROR|WARN|INFO):\s+(.+)', log)
print(match.group(2))
```

A) `'2024-05-12'`

B) `'ERROR'` ✅

C) `'conexión rechazada en puerto 8080'`

D) `'2024-05-12 ERROR: conexión rechazada en puerto 8080'`

---

**Pregunta 31** *(U5 — teórica)*

¿Qué mide el **coeficiente de clustering** de un nodo en una red?

A) El número de comunidades a las que pertenece el nodo.

B) La proporción de vecinos del nodo que también están conectados entre sí. ✅

C) La distancia media del nodo al resto de la red.

D) El número de aristas que conectan el nodo con nodos de otras comunidades.

---

**Pregunta 32** *(U4)*

Implementamos un pipeline de clasificación con TF-IDF y un clasificador. ¿Qué hace `TfidfVectorizer` en el siguiente fragmento?

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

corpus = ["el gato duerme", "el perro ladra", "el gato maúlla"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
```

A) Tokeniza el texto y devuelve una lista de listas de tokens.

B) Convierte cada documento en un vector numérico ponderando las palabras por su frecuencia en el documento y su rareza en el corpus. ✅

C) Genera embeddings densos de 300 dimensiones para cada documento.

D) Aplica stemming y elimina stopwords antes de vectorizar.

---

**Pregunta 33** *(U1)*

Creamos un decorador en Python. ¿Qué imprimirá el siguiente código?

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Finalizado {func.__name__}")
        return resultado
    return wrapper

@logger
def sumar(a, b):
    return a + b

sumar(3, 4)
```

A) Solo imprime `7`.

B) Imprime `Llamando a sumar`, luego `Finalizado sumar`. ✅

C) Error: los decoradores no pueden aplicarse a funciones con argumentos.

D) Imprime `Llamando a wrapper` y `Finalizado wrapper`.

---

**Pregunta 34** *(U3)*

Ejecutamos un job de PySpark con agregación sobre un corpus de noticias. ¿Qué diferencia hay entre `df.count()` y `df.collect()`?

A) `count()` devuelve una lista con todos los registros; `collect()` devuelve un entero.

B) No hay diferencia: ambos traen todos los datos al driver.

C) `count()` devuelve el número de filas sin traer datos al driver; `collect()` trae todos los registros al driver como lista de Python. ✅

D) `collect()` solo funciona con DataFrames de menos de 1 GB.

---

**Pregunta 35** *(U6)*

Comparamos el uso de CPU y GPU en un modelo Transformer. ¿Qué hace el siguiente fragmento para mover el modelo a GPU si está disponible?

```python
import torch
from transformers import AutoModelForSequenceClassification

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased')
model = model.to(device)
```

A) Descarga una versión del modelo optimizada para GPU desde el Hub.

B) Compila el modelo con TensorRT para acelerar la inferencia en GPU.

C) Mueve los tensores del modelo a la memoria de la GPU si hay una disponible, o los mantiene en CPU en caso contrario. ✅

D) Error: `.to(device)` solo está disponible en PyTorch >= 2.0.

---

**Pregunta 36** *(U2)*

Procesamos un corpus con Pandas y aplicamos minería de texto. ¿Qué hace `df['texto'].str.contains(r'\d+', regex=True)`?

A) Reemplaza todos los números del texto por un token especial.

B) Devuelve una Serie booleana indicando qué filas contienen al menos un número. ✅

C) Extrae todos los números de cada celda de texto.

D) Error: `.str.contains` no acepta expresiones regulares.

---

**Pregunta 37** *(U5)*

Construimos un sistema de recomendación basado en grafos. ¿Qué técnica usaríamos para recomendar productos a un usuario basándonos en lo que compraron usuarios similares?

A) Betweenness centrality sobre el grafo de productos.

B) Filtrado colaborativo mediante la similitud entre nodos-usuario en el grafo bipartito usuarios-productos. ✅

C) Detección de comunidades para agrupar productos del mismo tipo.

D) PageRank sobre el grafo de usuarios para identificar a los más influyentes.

---

**Pregunta 38** *(U4)*

Implementamos parsing con spaCy. ¿Qué representa `token.dep_` en el siguiente fragmento?

```python
import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("The cat sat on the mat")
for token in doc:
    print(token.text, token.dep_, token.head.text)
```

A) La categoría morfológica del token (sustantivo, verbo, etc.).

B) La etiqueta de dependencia sintáctica del token respecto a su cabeza (sujeto, objeto, etc.). ✅

C) La entidad nombrada a la que pertenece el token.

D) El lema del token en su forma canónica.

---

**Pregunta 39** *(U1)*

Tenemos el siguiente fragmento con manejo de excepciones. ¿Qué imprimirá si `valor = "texto"`?

```python
def convertir(valor):
    try:
        resultado = int(valor)
        return resultado
    except ValueError:
        print("No se puede convertir")
        return None
    finally:
        print("Proceso finalizado")

convertir("texto")
```

A) Solo `"No se puede convertir"`.

B) Solo `"Proceso finalizado"`.

C) `"No se puede convertir"` y luego `"Proceso finalizado"`. ✅

D) Error no capturado: `int("texto")` lanza TypeError, no ValueError.

---

**Pregunta 40** *(U3)*

Implementamos extracción de datos con la API de X usando paginación. ¿Qué hace `tweepy.Paginator` en el siguiente fragmento?

```python
import tweepy

client = tweepy.Client(bearer_token='...')
tweets = []
for respuesta in tweepy.Paginator(client.search_recent_tweets,
                                   query='#NLP lang:es',
                                   max_results=100).flatten(limit=500):
    tweets.append(respuesta.text)
```

A) Divide los tweets en páginas de 500 para almacenarlos más eficientemente.

B) Itera automáticamente sobre múltiples páginas de resultados hasta alcanzar los 500 tweets indicados en `limit`. ✅

C) Descarga los 500 tweets más recientes en una sola petición a la API.

D) Error: `flatten` no está disponible en `tweepy.Paginator`.

---

**Pregunta 41** *(U6 — teórica)*

¿Qué es el **tokenizador BPE** (Byte Pair Encoding) usado en modelos como GPT?

A) Un tokenizador que divide el texto en palabras completas usando espacios en blanco.

B) Un tokenizador basado en caracteres que representa cada letra por separado.

C) Un algoritmo que divide el texto en subpalabras frecuentes, fusionando iterativamente los pares de bytes más comunes del corpus de entrenamiento. ✅

D) Un tokenizador que asigna un ID único a cada oración del corpus.

---

**Pregunta 42** *(U4)*

Construimos un pipeline de análisis con TextBlob. ¿Qué devuelve `blob.noun_phrases`?

```python
from textblob import TextBlob

blob = TextBlob("The quick brown fox jumps over the lazy dog near the river bank")
print(blob.noun_phrases)
```

A) Una lista con todos los sustantivos del texto.

B) Una lista de frases nominales (grupos de palabras centrados en un sustantivo). ✅

C) Una lista con los adjetivos y sustantivos por separado.

D) Error: `noun_phrases` no está disponible en la versión estándar de TextBlob.

---

**Pregunta 43** *(U2)*

Usamos `re.sub` para limpiar texto. ¿Qué devuelve `resultado`?

```python
import re

texto = "   Hola   mundo   con   espacios   "
resultado = re.sub(r'\s+', ' ', texto).strip()
```

A) `"Holamundoconespacios"`

B) `"   Hola   mundo   con   espacios   "` (sin cambios)

C) `"Hola mundo con espacios"` ✅

D) Error: `\s+` no captura múltiples espacios seguidos.

---

**Pregunta 44** *(U5)*

Analizamos la red del caso Enron. ¿Qué indica un valor alto de **eigenvector centrality** en un nodo de la red de emails?

A) Que el nodo es un puente entre comunidades separadas.

B) Que el nodo tiene muchas conexiones con nodos que a su vez tienen muchas conexiones (influencia global en la red). ✅

C) Que el nodo ha enviado el mayor número total de emails.

D) Que el nodo pertenece a la comunidad con mayor densidad de conexiones.

---

**Pregunta 45** *(U3)*

Ejecutamos el siguiente job de PySpark sobre un log de errores. ¿Qué estructura de carpetas generará en `output_path`?

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = SparkSession.builder.appName("Logs").getOrCreate()
df = spark.read.json("hdfs://logs/*.json")
df = df.withColumn('fecha', to_date(col('timestamp')))
df.write.mode('overwrite').partitionBy('fecha').parquet(output_path)
spark.stop()
```

A) Un único archivo Parquet con todos los datos.

B) Una carpeta por cada valor único de `fecha`, con formato `fecha=YYYY-MM-DD/`, cada una con archivos part-*.parquet. ✅

C) Una carpeta llamada `timestamp/` con los datos agrupados por hora.

D) Error: `to_date` no es compatible con `partitionBy`.

---

*Fin del Modelo 3 — 45 preguntas*
