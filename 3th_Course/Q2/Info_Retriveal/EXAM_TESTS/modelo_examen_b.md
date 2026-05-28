# Modelo de Examen — Modelo 2
## Ingeniería de Datos y NLP con Python
### 45 preguntas tipo test · Una sola respuesta correcta

---

**Pregunta 1** *(U6)*

Cargamos un pipeline de generación de texto con Hugging Face. ¿Qué ocurre al ejecutar este fragmento?

```python
from transformers import pipeline

generador = pipeline('text-generation', model='gpt2')
resultado = generador("En el futuro, la inteligencia artificial", max_new_tokens=50)
print(type(resultado))
```

A) Imprime `<class 'str'>` porque el pipeline devuelve texto plano.

B) Imprime `<class 'list'>` porque el pipeline devuelve una lista de diccionarios con el texto generado. ✅

> El pipeline de Hugging Face devuelve siempre una estructura de datos consistente: en generación de texto, es una lista de diccionarios. Cada diccionario contiene el texto generado bajo la clave 'generated_text'.

C) Error: GPT-2 no soporta texto en español.

D) Imprime `<class 'dict'>` con las claves `input` y `output`.

---

**Pregunta 2** *(U2)*

Procesamos texto con expresiones regulares. ¿Qué devuelve `resultado`?

```python
import re

texto = "Contacto: info@empresa.com y soporte@web.org"
resultado = re.findall(r'[\w.-]+@[\w.-]+\.\w+', texto)
```

A) `['Contacto']`

B) `['info@empresa.com', 'soporte@web.org']` ✅

> El regex busca el patrón: `[\w.-]+` (un o más word chars o puntos/guiones) + `@` + `[\w.-]+` (palabra) + `.` + `\w+` (extensión). Encuentra ambos emails completos.

C) `['empresa.com', 'web.org']`

D) `[]` porque el patrón no es válido en Python.

---

**Pregunta 3** *(U5)*

Calculamos métricas sobre una red de colaboración. ¿Qué nodo tiene mayor **degree centrality** en este grafo?

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([('A','B'), ('A','C'), ('A','D'), ('B','C'), ('D','E')])
dc = nx.degree_centrality(G)
print(max(dc, key=dc.get))
```

A) 'B'

B) 'E'

C) 'D'

D) 'A' ✅

> **Degree centrality** mide el número de conexiones directas de cada nodo. A tiene grado 3 (conecta con B, C, D); B tiene grado 2; D tiene grado 2; E tiene grado 1. A es el nodo más conectado.

---

**Pregunta 4** *(U1 — teórica)*

¿Qué es un entorno virtual en Python?

A) Una máquina virtual que emula otro sistema operativo para ejecutar Python.

B) Un directorio aislado con su propio intérprete y dependencias, evitando conflictos entre proyectos. ✅

> Un entorno virtual es un mecanismo de Python que crea un aislamiento de paquetes. Permite instalar versiones diferentes de librerías para distintos proyectos sin conflictos en el sistema global.

C) Un IDE online para programar Python sin instalación local.

D) Un contenedor Docker con Python preinstalado.

---

**Pregunta 5** *(U4)*

Evaluamos la calidad de un modelo LDA entrenado con Gensim. ¿Qué mide la **coherencia** del modelo?

A) El tiempo de entrenamiento en segundos por epoch.

B) El número de tópicos que el modelo ha descubierto.

C) Qué tan semánticamente relacionadas están las palabras dentro de cada tópico. ✅

> **Coherencia** es una métrica que calcula qué tan bien las top-k palabras de un tópico se relacionan semánticamente. Valores altos indican tópicos más interpretables y significativos.

D) La proporción de documentos asignados al tópico mayoritario.

---

**Pregunta 6** *(U3)*

Hacemos scraping con BeautifulSoup. ¿Qué contiene `titulos` tras ejecutar el código?

```python
from bs4 import BeautifulSoup

html = """
<ul>
  <li class="item">Manzana</li>
  <li class="item">Pera</li>
  <li class="otro">Tomate</li>
  <li class="item">Naranja</li>
</ul>
"""
soup = BeautifulSoup(html, 'html.parser')
titulos = [li.text for li in soup.find_all('li', class_='item')]
```

A) `['Manzana', 'Pera', 'Tomate', 'Naranja']`

B) `['Manzana', 'Pera', 'Naranja']` ✅

> `find_all('li', class_='item')` selecciona solo elementos `<li>` con `class="item"`. Tomate tiene `class="otro"`, por lo que se excluye. Quedan los 3 items.

C) `['Tomate']`

D) Error: `find_all` no acepta el parámetro `class_`.

---

**Pregunta 7** *(U6)*

Implementamos fine-tuning con PyTorch. ¿Qué hace `loss.backward()` en el siguiente bucle?

```python
for epoch in range(3):
    for batch in train_loader:
        input_ids = batch['input_ids']
        labels = batch['labels']
        outputs = model(input_ids, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
```

A) Actualiza los pesos del modelo usando el optimizador.

B) Calcula los gradientes de la función de pérdida respecto a todos los parámetros del modelo. ✅

> `.backward()` es el paso de retropropagación (backpropagation). Computa los gradientes para cada parámetro usando la regla de la cadena. Luego `optimizer.step()` actualiza los parámetros basado en estos gradientes.

C) Evalúa el modelo en el conjunto de validación.

D) Reinicia la pérdida a cero antes del siguiente batch.

---

**Pregunta 8** *(U2 — teórica)*

¿Qué es la lematización en NLP?

A) Eliminar las stopwords de un texto.

B) Reducir una palabra a su raíz morfológica mediante truncamiento por reglas fijas.

C) Transformar una palabra a su forma canónica de diccionario (lema), preservando el significado. ✅

> **Lematización** usa diccionarios y análisis morfológico para mapear formas conjugadas/flexionadas a su forma base: "corriendo" → "correr", "gatos" → "gato". Preserva el significado léxico.

D) Convertir el texto a una representación vectorial numérica.

---

**Pregunta 9** *(U1)*

Analizamos un pipeline de datos con Pandas. ¿Qué devuelve `resumen`?

```python
import pandas as pd

df = pd.DataFrame({
    'categoria': ['A', 'B', 'A', 'B', 'A'],
    'ventas': [100, 200, 150, 80, 120]
})
resumen = df.groupby('categoria')['ventas'].agg(['sum', 'mean']).reset_index()
```

A) Un DataFrame con el total de filas por categoría.

B) Un DataFrame con la suma y la media de ventas por categoría. ✅

> `.groupby('categoria')['ventas'].agg(['sum', 'mean'])` agrega aplicando dos funciones. Para A: sum=350, mean=125; para B: sum=280, mean=140. El resultado es un DataFrame con columnas 'sum' y 'mean'.

C) Una Serie con el valor máximo de ventas por categoría.

D) Error: `agg` no acepta una lista de funciones en Pandas.

---

**Pregunta 10** *(U4)*

Aplicamos análisis de sentimiento con TextBlob. ¿Qué imprime el siguiente fragmento?

```python
from textblob import TextBlob

frases = ["I love this!", "This is terrible.", "It is what it is."]
for f in frases:
    p = TextBlob(f).sentiment.polarity
    etiqueta = "pos" if p > 0 else ("neg" if p < 0 else "neu")
    print(f"{etiqueta}", end=' ')
```

A) `pos pos neu`

B) `pos neg pos`

C) `pos neg neu` ✅

> "I love this!" es positivo (polarity > 0). "This is terrible." es negativo (polarity < 0). "It is what it is." es neutral (polarity == 0). La lógica condición determina: pos/neg/neu según sea >, <, o ==.

D) `neu neg neu`

---

**Pregunta 11** *(U3)*

Procesamos un gran volumen de datos con PySpark. ¿Qué hace `partitionBy` en el siguiente fragmento?

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("App").getOrCreate()
df = spark.read.csv("hdfs://datos/logs.csv", header=True)
df.write.mode('overwrite').partitionBy('pais').parquet('hdfs://output/logs')
spark.stop()
```

A) Divide el DataFrame en memoria en particiones para un procesamiento más rápido.

B) Guarda el Parquet creando subcarpetas separadas por cada valor único de la columna 'pais'. ✅

> `partitionBy('pais')` es una optimización de almacenamiento. Crea subcarpetas `pais=DE/`, `pais=US/`, etc., permitiendo lectura más rápida al filtrar por país y paralelización en escritura.

C) Filtra el DataFrame para conservar solo las filas donde 'pais' no es nulo.

D) Error: `partitionBy` solo está disponible para formato ORC, no Parquet.

---

**Pregunta 12** *(U5)*

Detectamos comunidades en una red con NetworkX. ¿Qué representa `len(comunidades)` tras ejecutar el código?

```python
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

G = nx.karate_club_graph()
comunidades = list(greedy_modularity_communities(G))
print(len(comunidades))
```

A) El número total de nodos del grafo.

B) El número de aristas del grafo.

C) El número de comunidades detectadas por el algoritmo. ✅

> `greedy_modularity_communities()` devuelve un generador de comunidades. Los convertimos a lista y contamos cuántas comunidades encontró el algoritmo. No es el número de nodos ni aristas.

D) El número de nodos del grafo que pertenecen a más de una comunidad.

---

**Pregunta 13** *(U2)*

Aplicamos spaCy para reconocimiento de entidades nombradas. ¿Qué imprime el siguiente fragmento?

```python
import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for ent in doc.ents:
    print(ent.text, ent.label_)
```

A) Solo imprime las palabras en mayúscula con su etiqueta POS.

B) Imprime cada entidad reconocida (persona, organización, lugar, dinero, etc.) con su etiqueta de tipo. ✅

> **NER** (Named Entity Recognition) identifica entidades en el texto. El modelo `en_core_web_sm` tiene este componente activado por defecto. Imprime: "Apple" (ORG), "U.K." (GPE), "1 billion" (MONEY).

C) Error: `en_core_web_sm` no tiene el componente NER activado por defecto.

D) Imprime todos los tokens del documento con su etiqueta de dependencia.

---

**Pregunta 14** *(U6 — teórica)*

¿Qué es el mecanismo de **self-attention** en los Transformers?

A) Un método para reducir el vocabulario del modelo durante el entrenamiento.

B) Un mecanismo por el que cada token pondera la relevancia del resto de tokens de la secuencia al generar su representación. ✅

> **Self-attention** es el corazón de los Transformers. Cada token aprende pesos (attention weights) que indican cuánto debe «atender» a los otros tokens para actualizar su representación contextual.

C) Una técnica de regularización equivalente al dropout aplicada a las capas de atención.

D) Un algoritmo de búsqueda en haz (beam search) para la generación de texto.

---

**Pregunta 15** *(U1)*

Leemos un fichero JSON con Pandas. ¿Qué ocurre al ejecutar el siguiente código?

```python
import pandas as pd

datos = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": None},
    {"nombre": "Mar", "edad": 25}
]
df = pd.DataFrame(datos)
print(df['edad'].mean())
```

A) Lanza un error porque hay un valor `None` en la columna.

B) Devuelve 0.0 porque `None` se trata como 0.

C) Devuelve 27.5, ignorando el `None` en el cálculo de la media. ✅

> Pandas trata `None`/`NaN` como datos faltantes y los **ignora automáticamente** en funciones de agregación. De (30, 25) se calcula mean = 55/2 = 27.5. El `None` no es tratado como 0.

D) Devuelve NaN porque hay valores nulos en la columna.

---

**Pregunta 16** *(U4)*

Construimos un pipeline de resumen extractivo. ¿Cuántas oraciones devolverá `resumir(texto)` si el texto tiene solo 2 oraciones?

```python
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

def resumir(texto, n=3):
    oraciones = sent_tokenize(texto)
    palabras = word_tokenize(texto.lower())
    freq = FreqDist(palabras)
    puntuaciones = {s: sum(freq[w] for w in word_tokenize(s.lower())) for s in oraciones}
    return sorted(oraciones, key=lambda s: puntuaciones[s], reverse=True)[:n]

texto = "Python es genial. NLP es fascinante."
print(len(resumir(texto)))
```

A) 3, porque `n=3` por defecto.

B) 0, porque el texto es demasiado corto.

C) 2, porque el slicing `[:3]` sobre una lista de 2 elementos devuelve los 2 disponibles. ✅

> El texto sólo tiene 2 oraciones. Aunque `n=3`, el slicing `[:3]` en una lista de 2 elementos simplemente devuelve esos 2. No lanza error; Python maneja silenciosamente índices fuera de rango en slicing.

D) Error: `sent_tokenize` necesita al menos 3 oraciones.

---

**Pregunta 17** *(U3)*

Usamos Selenium para scraping dinámico. ¿Cuándo es imprescindible Selenium frente a BeautifulSoup + requests?

A) Cuando la página tiene más de 100 elementos HTML.

B) Cuando el contenido que queremos extraer se genera mediante JavaScript tras la carga inicial de la página. ✅

> BeautifulSoup + requests solo recibe el HTML inicial. JavaScript ejecutado por el navegador no afecta a requests. **Selenium** emula un navegador real que ejecuta JS, permitiendo extraer contenido dinámico.

C) Siempre que la página use HTTPS en lugar de HTTP.

D) Cuando queremos extraer tablas HTML.

---

**Pregunta 18** *(U5 — teórica)*

¿Qué diferencia a un grafo **dirigido** de uno **no dirigido**?

A) Un grafo dirigido no puede tener ciclos.

B) En un grafo dirigido, las aristas tienen dirección (origen → destino); en uno no dirigido, la conexión es bidireccional. ✅

> **Grafo dirigido** (DiGraph): A → B y B → A son aristas distintas. **Grafo no dirigido** (Graph): A-B es una sola arista en ambas direcciones. Los ciclos sí pueden existir en ambos tipos.

C) Un grafo dirigido solo puede tener nodos numéricos.

D) Los grafos no dirigidos no pueden tener pesos en las aristas.

---

**Pregunta 19** *(U6)*

Implementamos inferencia con un modelo BERT para obtener embeddings. ¿Qué representa `last_hidden_state` en el siguiente fragmento?

```python
from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

inputs = tokenizer("Hello world", return_tensors='pt')
with torch.no_grad():
    outputs = model(**inputs)

print(outputs.last_hidden_state.shape)
```

A) Un vector único de dimensión 768 que representa toda la frase.

B) Un tensor de forma `(1, num_tokens, 768)` con la representación contextual de cada token. ✅

> `last_hidden_state` es la salida de la filtima capa de BERT: `(batch_size, seq_length, hidden_size)`. Cada token tiene un vector de 768 dimensiones. Estos embeddings contextuales son ideales para extraer representaciones de tokens.

C) La probabilidad de cada token del vocabulario como siguiente token.

D) Error: `BertModel` no devuelve `last_hidden_state`, solo `pooler_output`.

---

**Pregunta 20** *(U2)*

Procesamos texto con NLTK. ¿Qué hace `nltk.corpus.stopwords.words('spanish')`?

A) Descarga automáticamente un corpus de texto en español.

B) Devuelve una lista de palabras vacías (artículos, preposiciones, etc.) en español que suelen eliminarse en preprocesado. ✅
> **Stopwords** son palabras muy frecuentes pero con bajo contenido semántico: "el", "de", "y", "a", etc. Eliminarlas reduce ruido y mejora modelos de NLP. NLTK tiene stopwords para más de 20 idiomas.
C) Tokeniza un texto en español por stopwords.

D) Lanza un error porque NLTK no tiene stopwords en español.

---

**Pregunta 21** *(U1)*

Implementamos una función de carga y limpieza de datos. ¿Qué devuelve `df.shape` tras ejecutar el código?

```python
import pandas as pd

data = {
    'id': [1, 2, 2, 3, 4],
    'valor': [10, 20, 20, 30, None]
}
df = pd.DataFrame(data)
df = df.drop_duplicates()
df = df.dropna()
```

A) `(5, 2)`

B) `(4, 2)`

C) `(3, 2)` ✅

> Inicialmente: (5 filas, 2 columnas). `drop_duplicates()`: la fila 2 se repite, quedan 4 filas. `dropna()`: la fila con valor None se elimina, quedan 3 filas. Resultado: (3, 2).

D) `(2, 2)`

---

**Pregunta 22** *(U4)*

Preparamos datos para LDA. ¿Qué hace `corpora.Dictionary.filter_extremes` en el siguiente fragmento?

```python
from gensim import corpora

dictionary = corpora.Dictionary(documentos)
dictionary.filter_extremes(no_below=5, no_above=0.5)
```

A) Elimina las palabras que aparecen en más de 5 documentos o en menos del 50% del corpus.

B) Elimina las palabras que aparecen en menos de 5 documentos o en más del 50% del corpus. ✅

> `no_below=5`: elimina palabras que aparecen en < 5 documentos (palabras raras). `no_above=0.5`: elimina palabras en > 50% de documentos (palabras muy comunes). Esto optimiza el vocabulario para LDA.

C) Ordena el vocabulario por frecuencia y conserva solo los 5 primeros.

D) Filtra los documentos que tienen menos de 5 tokens.

---

**Pregunta 23** *(U3)*

Usamos PySpark para contar palabras en un corpus distribuido. ¿Qué contiene `top5` tras ejecutar el código?

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, lower, col

spark = SparkSession.builder.appName("WordCount").getOrCreate()
df = spark.read.text("hdfs://corpus/*.txt")

palabras = df.select(explode(split(lower(col('value')), r'\W+')).alias('palabra'))
top5 = palabras.groupBy('palabra').count().orderBy('count', ascending=False).limit(5)
top5.show()
spark.stop()
```

A) Las 5 palabras más largas del corpus.

B) Las 5 palabras más frecuentes del corpus. ✅

> El pipeline: 1) Lee archivos de texto; 2) `explode(split(...))` divide por no-word y crea una fila por palabra; 3) `groupBy.count()` cuenta frecuencias; 4) `orderBy(..., descending=True)` ordena de mayor a menor; 5) `limit(5)` devuelve las top 5.

C) Los 5 documentos con más palabras.

D) Error: `explode` no está disponible en PySpark DataFrames.

---

**Pregunta 24** *(U6)*

Comparamos Keras y PyTorch para un proyecto de NLP. ¿Cuál de estas afirmaciones es correcta?

A) Keras solo puede usarse con TensorFlow; PyTorch tiene su propia API de alto nivel llamada Lightning. ✅

> Keras es la API de alto nivel de TensorFlow. PyTorch Lightning (libreria separada) proporciona abstracciones similares para PyTorch. Ambos frameworks soportan GPU y son compatibles con Transformers.

B) PyTorch no soporta entrenamiento en GPU.

C) Keras usa grafos dinámicos por defecto; PyTorch usa grafos estáticos.

D) Ambos frameworks son incompatibles con Hugging Face Transformers.

---

**Pregunta 25** *(U5)*

Analizamos la centralidad de una red. ¿Qué representa el **PageRank** de un nodo?

A) El número de conexiones directas que tiene el nodo.

B) La distancia media del nodo al resto de nodos de la red.

C) Una medida de importancia basada en la cantidad y calidad de los nodos que apuntan hacia él. ✅

> **PageRank** es un algoritmo que propaga importancia a través del grafo. Un nodo es importante si tiene muchos enlaces entrantes, especialmente de nodos importantes. Base del algoritmo original de Google.

D) El número de comunidades a las que pertenece el nodo.

---

**Pregunta 26** *(U2)*

Usamos la librería `re` para extraer información. ¿Qué imprime el código?

```python
import re

texto = "Fecha: 2024-03-15 y también 2023-11-02"
fechas = re.findall(r'\d{4}-\d{2}-\d{2}', texto)
print(len(fechas))
```

A) 0

B) 1

C) 2 ✅

> El regex `\d{4}-\d{2}-\d{2}` coincide con el patrón YYYY-MM-DD. En el texto hay: "2024-03-15" y "2023-11-02". `findall` devuelve una lista con 2 coincidencias.

D) Error: `\d` no es un metacarácter válido en Python.

---

**Pregunta 27** *(U1 — teórica)*

¿Qué ventaja principal ofrece el formato **Avro** frente a JSON para almacenamiento de datos?

A) Avro es más legible por humanos que JSON.

B) Avro incluye el schema junto con los datos y tiene serialización binaria compacta, lo que reduce el tamaño y mejora el rendimiento. ✅

> **Avro** es un formato binario con schema embebido. Ventajas: serialización compacta, cambio de schema compatible hacia adelante/atrás. **JSON** es texto plano, más legible pero más grande y más lento de parsear.

C) Avro solo puede usarse con PySpark; JSON es más universal.

D) Avro no soporta tipos anidados como listas o diccionarios.

---

**Pregunta 28** *(U4)*

Implementamos NER con spaCy. ¿Qué imprime el siguiente código si `doc` contiene las entidades "Madrid" (GPE) y "Google" (ORG)?

```python
import spacy

nlp = spacy.load('es_core_news_sm')
doc = nlp("Google abrirá una nueva oficina en Madrid el próximo año.")
entidades = [(ent.text, ent.label_) for ent in doc.ents]
print(entidades)
```

A) `[('Google', 'PERSON'), ('Madrid', 'LOC')]`

B) `[('Google', 'ORG'), ('Madrid', 'GPE')]` ✅

> El modelo `es_core_news_sm` reconoce entidades en español. **ORG** = Organización (Google), **GPE** = Entidad Geopolítica (Madrid). Otros tags: PERSON, LOC, etc.

C) `[]` porque spaCy en español no tiene NER activado.

D) Error: `es_core_news_sm` no reconoce organizaciones tecnológicas.

---

**Pregunta 29** *(U3)*

Realizamos un join en PySpark. ¿Cuántas filas tendrá `df_join` si `df_usuarios` tiene 1000 filas, `df_pedidos` tiene 5000 filas, y solo 800 usuarios tienen pedidos?

```python
df_join = df_usuarios.join(df_pedidos, on='user_id', how='inner')
```

A) 6000 filas.

B) 1000 filas.

C) Las filas correspondientes a los 800 usuarios que tienen al menos un pedido en `df_pedidos`. ✅

> `join(..., how='inner')` conserva solo las filas donde la clave (user_id) existe en ambos DataFrames. 800 usuarios tienen pedidos, así que esas 800 filas se mantienen. El número exacto de filas resultado depende cuántos pedidos tiene cada usuario.

D) 800 filas exactamente, una por usuario con pedidos.

---

**Pregunta 30** *(U6 — teórica)*

¿Qué es el **fine-tuning** de un LLM preentrenado?

A) Comprimir el modelo para reducir su tamaño sin reentrenarlo.

B) Continuar el entrenamiento del modelo sobre un dataset específico de la tarea para adaptar sus pesos al dominio concreto. ✅
> **Fine-tuning** es el proceso de reutilizar un modelo preentrenado en datos generales y reentrenarlo sobre datos de una tarea específica. Mantiene los pesos preentrenados pero los adapta. Acelera conversión y mejora resultados.
C) Cambiar la arquitectura del modelo añadiendo nuevas capas de atención.

D) Exportar el modelo a un formato optimizado para inferencia (ONNX, TensorRT).

---

**Pregunta 31** *(U2)*

Aplicamos un pipeline de minería de texto con Pandas. ¿Qué hace `df['tokens'].explode()`?

```python
import pandas as pd
from nltk.tokenize import word_tokenize

df = pd.DataFrame({'texto': ['hola mundo', 'python nlp']})
df['tokens'] = df['texto'].apply(word_tokenize)
df_exploded = df['tokens'].explode()
print(df_exploded.shape)
```

A) Convierte cada token en una columna separada del DataFrame.

B) Convierte cada lista de tokens en filas individuales, una por token. ✅

> `.explode()` transforma cada elemento (lista) en una fila separada. Si una celda tiene `['hola', 'mundo']`, se genera una fila con 'hola' y otra con 'mundo'. Aumenta el número de filas.

C) Aplana el DataFrame eliminando la columna 'texto'.

D) Error: `explode` no está disponible en versiones de Pandas < 2.0.

---

**Pregunta 32** *(U5)*

Construimos una red de co-ocurrencias de palabras. ¿Qué representa una arista con peso alto entre dos nodos-palabra?

A) Que ambas palabras son sinónimos.

B) Que ambas palabras aparecen frecuentemente en el mismo contexto o documento. ✅

> En una red de co-ocurrencias, la fuerza de una arista (peso) refleja cuán a menudo dos palabras co-aparecen. Peso alto = alta co-frecuencia = probablemente relacionadas temáticamente o semánticamente.

C) Que una palabra es antónima de la otra.

D) Que una de las dos palabras es una stopword.

---

**Pregunta 33** *(U1)*

Usamos Polars para una transformación de datos. ¿Qué hace el siguiente fragmento?

```python
import polars as pl

df = pl.read_csv('productos.csv')
resultado = (
    df
    .filter(pl.col('stock') > 0)
    .with_columns((pl.col('precio') * 0.9).alias('precio_oferta'))
    .select(['nombre', 'precio', 'precio_oferta'])
)
```

A) Elimina productos con stock y aplica un incremento del 10% al precio.

B) Filtra productos con stock disponible, calcula un precio con 10% de descuento y selecciona tres columnas. ✅

> Pipeline: 1) `filter(stock > 0)` conserva productos con stock; 2) `with_columns(...*0.9)` crea nueva columna con precio rebajado 10%; 3) `select()` elige 3 columnas finales. Polars permite encadenar estas operaciones.

C) Error: no se puede encadenar `filter`, `with_columns` y `select` en Polars.

D) Agrupa los productos por nombre y suma los precios.

---

**Pregunta 34** *(U4)*

Calculamos TF-IDF sobre un corpus para un modelo de recuperación de información. ¿Qué penaliza el componente **IDF**?

A) Las palabras que aparecen pocas veces en un documento.

B) Las palabras muy largas o con muchas sílabas.

C) Las palabras que aparecen en muchos documentos del corpus (palabras poco discriminativas). ✅

> **IDF** (Inverse Document Frequency) penaliza palabras muy comunes. Si una palabra aparece en el 90% de documentos, su IDF es bajo, reduciendo su importancia en TF-IDF. Palabras raras tienen IDF alto.

D) Las palabras que no están en el vocabulario del modelo.

---

**Pregunta 35** *(U3 — teórica)*

¿Qué es el archivo `robots.txt` de un sitio web y por qué es relevante para el web scraping?

A) Un archivo que lista los endpoints de la API REST del sitio web.

B) Un archivo que indica a los scrapers y bots qué rutas del sitio están permitidas o prohibidas para el rastreo automatizado. ✅

> `robots.txt` es un estándar que lista reglas de acceso para bots. Especifica rutas permitidas/prohibidas vía directives `Allow` y `Disallow`. Los scrapers responsables lo respetan; es ubicación: sitio.com/robots.txt

C) Un archivo de configuración del servidor que bloquea automáticamente todo tráfico no humano.

D) Un archivo que define los selectores CSS de los elementos con datos interesantes.

---

**Pregunta 36** *(U6)*

Implementamos un modelo de clasificación de texto con Keras. ¿Qué hace la capa `GlobalAveragePooling1D` en el siguiente modelo?

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense

model = Sequential([
    Embedding(input_dim=10000, output_dim=64),
    GlobalAveragePooling1D(),
    Dense(3, activation='softmax')
])
```

A) Selecciona el embedding del primer token de la secuencia como representación global.

B) Promedia los embeddings de todos los tokens de la secuencia para obtener un vector de longitud fija. ✅

> `GlobalAveragePooling1D()` permuta sobre la dimensión temporal (seq_length). Convierte (batch, seq_length, dim) → (batch, dim). Promediando todos los embeddings de tokens se obtiene una representación global de la secuencia.

C) Aplica max-pooling sobre la dimensión temporal de los embeddings.

D) Concatena los embeddings de todos los tokens en un único vector largo.

---

**Pregunta 37** *(U2)*

Generamos una nube de palabras a partir de un DataFrame. ¿Qué hace el siguiente fragmento?

```python
import pandas as pd
from wordcloud import WordCloud

df = pd.read_csv('noticias.csv')
texto_completo = ' '.join(df['titular'].dropna().tolist())
wc = WordCloud(stopwords={'de','la','el','en','y'}, max_words=50).generate(texto_completo)
```

A) Genera una nube con todas las palabras del corpus sin filtrar.

B) Genera una nube con las 50 palabras más frecuentes, excluyendo las stopwords indicadas. ✅

> `stopwords={...}` excluye esas 5 palabras. `max_words=50` limita a las 50 palabras más frecuentes tras eliminar stopwords. `.generate()` construye la nube aplicando el texto preprocesado.

C) Error: `stopwords` debe ser una lista, no un set.

D) Genera una nube de solo 5 palabras porque `stopwords` tiene 5 elementos.

---

**Pregunta 38** *(U5)*

Analizamos la red del caso Enron. ¿Qué mide la **closeness centrality** de un nodo?

A) Cuántas veces aparece el nodo en los caminos más cortos de la red.

B) Cuántas conexiones directas tiene el nodo.

C) Lo cerca que está un nodo de todos los demás, medido como el inverso de la suma de distancias más cortas. ✅

> **Closeness centrality** = 1 / (suma de distancias geodésicas a todos los nodos). Nodos con alta closeness están bien conectados globalmente, cerca de todos los demás promedio.

D) El peso total de todas las aristas que inciden en el nodo.

---

**Pregunta 39** *(U4)*

Implementamos un clasificador de reseñas. Si de 500 reseñas, 200 tienen `polarity > 0`, 150 tienen `polarity < 0` y 150 tienen `polarity == 0`, ¿qué porcentaje marcará la etiqueta "positive"?

```python
df["sentiment"] = df["polarity"].apply(lambda p: "positive" if p >= 0 else "negative")
```

A) 40%

B) 30%

C) 70% ✅

> Total de etiquetas "positive": aquellas con `polarity >= 0`, que son 200 (positivas) + 150 (neutrales con polarity==0) = 350. De 500 total: 350/500 = 70%.

D) 50%

---

**Pregunta 40** *(U1)*

Leemos un archivo Parquet con Pandas y aplicamos una agregación. ¿Qué hace el siguiente fragmento?

```python
import pandas as pd

df = pd.read_parquet('transacciones.parquet')
resultado = df[df['importe'] > 500].groupby('cliente_id')['importe'].sum().nlargest(3)
```

A) Devuelve los 3 clientes con mayor número de transacciones superiores a 500€.

B) Devuelve los 3 clientes con mayor importe total acumulado en transacciones superiores a 500€. ✅

> Pipeline: 1) Filtra transacciones > 500€; 2) Agrupa por cliente_id; 3) Suma por grupo; 4) .nlargest(3) devuelve los 3 clientes con mayor suma. Responde: qué clientes gastaron más en transacciones grandes.

C) Devuelve las 3 transacciones individuales de mayor importe.

D) Error: `nlargest` no está disponible sobre el resultado de un `groupby`.

---

**Pregunta 41** *(U6)*

Subimos y usamos un modelo desde Hugging Face Hub. ¿Qué hace `AutoTokenizer.from_pretrained`?

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
```

A) Descarga y carga el tokenizador específíico asociado al modelo indicado desde el Hub. ✅

> `AutoTokenizer.from_pretrained()` detecta automáticamente el tipo de tokenizador (BertTokenizer, GPT2Tokenizer, etc.) basado en el archive `tokenizer_config.json` del modelo y lo descarga del Hub.

B) Crea un tokenizador genérico de subpalabras sin descargar nada.

C) Error: hay que indicar el tipo de tokenizador explícitamente (BertTokenizer, GPT2Tokenizer…).

D) Carga el modelo completo incluyendo sus pesos, ignorando el tokenizador.

---

**Pregunta 42** *(U3)*

Usamos la API de X (Twitter) con `tweepy`. ¿Qué representa el siguiente bucle?

```python
import tweepy

client = tweepy.Client(bearer_token='...')
respuesta = client.search_recent_tweets(query='#Python lang:es', max_results=100)
for tweet in respuesta.data:
    print(tweet.text)
```

A) Busca los 100 usuarios más activos con el hashtag #Python en español.

B) Descarga los 100 tweets más recientes en español que contengan el hashtag #Python. ✅

> `.search_recent_tweets()` busca tweets recientes. `query='#Python lang:es'` filtra por hashtag y idioma. `max_results=100` limita a 100 resultados. Itera sobre `respuesta.data` para procesar cada tweet.

C) Devuelve los 100 tweets con más likes que contengan #Python.

D) Error: `search_recent_tweets` no acepta el filtro `lang:es` dentro de `query`.

---

**Pregunta 43** *(U2 — teórica)*

¿Cuál es la diferencia entre las librerías `re` y `regex` en Python?

A) `re` es más rápida que `regex` en todos los casos.

B) `regex` es una versión mejorada de `re` que añade soporte para grupos de captura, Unicode extendido y operadores avanzados no disponibles en `re`. ✅

> **`re`** es la libreria estándar de Python con regex básicas. **`regex`** es un módulo de terceros más poderoso: atomic groups, lookahead genlizado, Unicode properties, named groups más flexibles, etc.

C) `regex` solo funciona en Python 3.10 o superior.

D) No hay diferencia funcional: `regex` es solo un alias de `re`.

---

**Pregunta 44** *(U5)*

Implementamos un sistema de detección de fraude con grafos. ¿Por qué los grafos son útiles para este caso de uso?

A) Porque los grafos permiten almacenar más datos que una base de datos relacional.

B) Porque los grafos permiten detectar patrones de comportamiento anómalo analizando las conexiones entre entidades (cuentas, transacciones, dispositivos). ✅

> Los grafos modelan relaciones complejas. En fraude, detectar centros de conexiones densas, ciclos rápidos de dinero, patrones de suplantación (identidades compartidas) es más natural con grafos que filas de datos.

C) Porque los grafos comprimen automáticamente los datos de transacciones.

D) Porque los grafos son más rápidos que los modelos de machine learning para cualquier tarea de clasificación.

---

**Pregunta 45** *(U4)*

Construimos un pipeline de modelización. ¿Qué imprime el siguiente código si `modelo.get_topic_terms(0, topn=3)` devuelve `[(15, 0.08), (42, 0.06), (7, 0.05)]`?

```python
from gensim.models import LdaModel

# modelo ya entrenado, dictionary ya construido
terminos = modelo.get_topic_terms(0, topn=3)
palabras = [dictionary[tid] for tid, prob in terminos]
print(palabras)
```

A) `[0.08, 0.06, 0.05]`

B) `[(15, 0.08), (42, 0.06), (7, 0.05)]`

C) Las 3 palabras del vocabulario correspondientes a los IDs 15, 42 y 7. ✅

> `get_topic_terms()` devuelve `(word_id, probability)`. El list comprehension `[dictionary[tid] ...]` busca en el diccionario de Gensim cada ID y obtiene su string: dictonary[15]="python", dictionary[42]="modelo", etc.

D) Error: `dictionary` no acepta enteros como índice.

---

*Fin del Modelo 2 — 45 preguntas*
