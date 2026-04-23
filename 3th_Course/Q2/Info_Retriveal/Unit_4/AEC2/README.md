# AEC2 – Análisis Avanzado de Sentimiento y Tendencias en Twitter

## Introducción

Partiendo de la clase `DataExtractor` que desarrollé en la anterior actividad, aquí la amplío con funcionalidades nuevas: conexión en tiempo real a la API de Twitter, modelado de tópicos con LDA, análisis de sentimiento, parsing y resumen extractivo. Todo sigue centralizado en la misma clase para que sea fácil de reutilizar.

El dataset base que uso es el de tweets de Bitcoin disponible en Kaggle, pero el flujo funciona igual con datos extraídos de la API.

---

## Estructura del proyecto

```
.
├── data_extractor.py        # Clase principal con toda la lógica
├── AEC1_DataExtractor.ipynb # Notebook base de la AEC1 (carga, limpieza, hashtags)
├── dashboard.py             # Dashboard interactivo con Streamlit (opcional)
├── test_api.py              # Script de prueba para la conexión a la API
├── requirements.txt         # Dependencias
├── README.md                # Este archivo
└── DOCUMENTACION.md         # Documentación técnica detallada
```

---

## Flujo Principal

### 1. Conexión a la API de Twitter (`load_data_api`)
Me conecto a la API de Twitter a través de RapidAPI usando `requests`. La clave la gestiono con una variable de entorno (`RAPIDAPI_KEY`) para no exponerla en el código. Los tweets los guardo en un CSV local para poder reutilizarlos luego con el resto de métodos.

```python
from data_extractor import DataExtractor

ext = DataExtractor()
ext.load_data_api(query="#bitcoin", max_results=100, output_file="tweets_api.csv")
```

> Las APIs gratuitas de RapidAPI devuelven pocos resultados por llamada. Si necesito más volumen, encadeno varias llamadas o uso directamente el dataset CSV de Kaggle.

### 2. Limpieza y normalización (`clean_text`)
Bajo el texto a minúsculas, elimino URLs, menciones, emojis y caracteres raros. Los hashtags los conservo porque son la base del análisis.

### 3. Extracción y análisis de hashtags (`extract_hashtags`, `analytics_hashtags_extended`)
Extraigo hashtags por tweet con regex y calculo tres vistas: frecuencia global, por usuario y por fecha. Esto me permite ver tendencias y detectar posibles bots (usuarios que usan hashtags de forma masiva y repetitiva).

### 4. WordCloud (`generate_hashtag_wordcloud`)
Visualizo los hashtags más frecuentes en una nube de palabras. Rápido y efectivo para hacerse una idea del vocabulario dominante.

### 5. Modelado de tópicos con LDA (`model_topics`)
Aplico Latent Dirichlet Allocation con gensim para descubrir los temas principales del corpus. Cada tópico se representa como una lista de las palabras más relevantes.

```python
topics = ext.model_topics(num_topics=5, passes=10)
for i, t in enumerate(topics):
    print(f"Tópico {i+1}: {t}")
```

### 6. Análisis de sentimiento (`analyze_sentiment`)
Calculo la polaridad y subjetividad de cada tweet. Soporto dos métodos: TextBlob (más rápido) y spaCy con spacytextblob (más preciso). El resultado se añade como columnas al DataFrame.

```python
df_sent = ext.analyze_sentiment(method='textblob')
```

### 7. Parsing y resumen extractivo (`parse_and_summarize`)
Con NLTK tokenizo el corpus completo en oraciones, las puntúo por frecuencia de palabras clave y selecciono las más relevantes. Devuelvo un resumen extractivo compacto del dataset.

```python
resumen = ext.parse_and_summarize(summary_ratio=0.3)
print(resumen)
```

---

## Set up del proyecto 

### Instalación

```bash
git clone https://github.com/U-Tad/
cd /3th_Course/Q2/Info_Retriveal/Unit_4/AEC2
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### Configurar la clave de API

```bash
export RAPIDAPI_KEY="clavedetwiter"   
set RAPIDAPI_KEY=clavedetwiter        
```

### Flujo completo de ejemplo

```python
from data_extractor import DataExtractor

ext = DataExtractor()

# Opción A: extraer de la API en tiempo real
ext.load_data_api(query="#bitcoin", max_results=100)

# Opción B: cargar desde CSV local (dataset Kaggle)
# ext = DataExtractor(source="Bitcoin_tweets_dataset_2.csv")
# ext.load_data()

# Análisis de hashtags
analytics = ext.analytics_hashtags_extended()
ext.generate_hashtag_wordcloud(overall_df=analytics['overall'])

# Tópicos
topics = ext.model_topics(num_topics=5)

# Sentimiento
df_sent = ext.analyze_sentiment(method='textblob')
print(df_sent[['clean_text', 'sentiment_polarity', 'sentiment_subjectivity']].head())

# Resumen extractivo
resumen = ext.parse_and_summarize(summary_ratio=0.3)
print(resumen)
```

### Dashboard interactivo (opcional)

```bash
streamlit run dashboard.py
```

Luego subo el CSV desde la barra lateral y exploro los hashtags visualmente.

---

## Dependencias

| Librería | uso |
|---|---|
| pandas | Carga y manipulación de datos |
| requests | Llamadas a la API de Twitter |
| matplotlib | Gráficos y visualizaciones |
| wordcloud | Nube de palabras |
| gensim | Modelado LDA |
| textblob | Análisis de sentimiento (método rápido) |
| spacy + spacytextblob | Análisis de sentimiento (método preciso) |
| nltk | Tokenización y resumen extractivo |
| streamlit | Dashboard interactivo |

---

## Fuente de datos

- **API en tiempo real**: [twitter-api45 en RapidAPI](https://rapidapi.com/alexanderxbx/api/twitter-api45) — gratuita con límite de peticiones
- **Dataset estático**: [Bitcoin Tweets – Kaggle](https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets)

---

## Referencias

### Comunidad y aprendizaje
- **[42 AI](https://42-ai.github.io/)** — organización estudiantil del campus de París de la escuela 42, creada por y para estudiantes de IA. He usado ejercicios de esta organización que han servido como referencia metodológica para estructurar el pipeline de este proyecto.

### Extracción de datos y APIs
- **[RapidAPI](https://rapidapi.com/)** — plataforma de marketplace de APIs que usé para conectarme a la API de Twitter (`twitter-api45`) y extraer tweets en tiempo real desde `load_data_api()`.

### Manipulación y análisis de datos
- **[Pandas](https://pandas.pydata.org/docs/)** — librería principal para carga, limpieza y transformación del dataset. Usé `read_csv` con `chunksize` para manejar el dataset de Bitcoin sin problemas de memoria.
- **[NumPy](https://numpy.org/)** — operaciones numéricas de apoyo en visualizaciones y cálculos intermedios.

### Procesamiento del lenguaje natural (NLP)
- **[NLTK](https://www.nltk.org/)** — tokenización de oraciones y palabras, eliminación de stopwords y generación del resumen extractivo en `parse_and_summarize()`.
- **[TextBlob](https://textblob.readthedocs.io/)** — análisis de sentimiento rápido en `analyze_sentiment()`, calcula polaridad y subjetividad por tweet.
- **[spaCy](https://spacy.io/)** — análisis sintáctico y parsing de dependencias, con árbol de dependencias generado con `displacy`. También como alternativa a TextBlob via `spacytextblob`.
- **[Gensim](https://radimrehurek.com/gensim/)** — modelado de tópicos con LDA en `model_topics()`, descubrimiento de los temas principales del corpus.

### Visualización
- **[Matplotlib](https://matplotlib.org/stable/users/index.html)** — todos los gráficos del proyecto: barras, histogramas, scatter, líneas temporales.
- **[Seaborn](https://seaborn.pydata.org/)** — estilos visuales y gráficos estadísticos complementarios.
- **[WordCloud](https://amueller.github.io/word_cloud/)** — generación de nubes de palabras a partir de frecuencias de hashtags en `generate_hashtag_wordcloud()`.

### Dashboard interactivo
- **[Streamlit](https://streamlit.io/)** — framework con el que construí el dashboard (`dashboard.py`) para explorar los resultados de forma interactiva desde el navegador.

