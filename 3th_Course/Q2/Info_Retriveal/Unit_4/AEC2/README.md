# AEC2 - Análisis Avanzado de Sentimiento y Tendencias en Twitter

## Introducción

Este proyecto implementa un pipeline avanzado para la extracción, limpieza y análisis de tweets, integrando:
- Extracción en tiempo real desde la API de Twitter (RapidAPI)
- Modelado de tópicos (LDA)
- Análisis de sentimiento (TextBlob/spaCy)
- Parsing y resumen extractivo (NLTK)
- Visualización avanzada (WordCloud, gráficos)

Toda la lógica está centralizada en la clase `DataExtractor` para máxima reutilización y reproducibilidad.

## Extracción de datos

Puedes trabajar tanto con datasets locales (CSV/JSON) como extraer tweets en tiempo real usando la API de Twitter vía RapidAPI. La autenticación se gestiona mediante la variable de entorno `RAPIDAPI_KEY`.

**Ejemplo de uso API:**
```python
from data_extractor import DataExtractor
ext = DataExtractor()
ext.load_data_api(query="#bitcoin", max_results=100)
```

## Técnicas aplicadas

- **Carga y limpieza:**
    - Carga eficiente con pandas (chunksize).
    - Limpieza de texto: minúsculas, eliminación de URLs, menciones, símbolos, normalización de espacios.
- **Extracción y análisis de hashtags:**
    - Extracción con regex, eliminación de duplicados.
    - Métricas globales, por usuario y por fecha.
- **Modelado de tópicos (LDA):**
    - Descubrimiento de temas con gensim.
- **Análisis de sentimiento:**
    - Polaridad y subjetividad con TextBlob o spaCy.
- **Parsing y resumen extractivo:**
    - Selección de oraciones clave con NLTK.
- **Visualización:**
    - WordCloud, gráficos de evolución y tablas resumen.

## Implementación y reproducibilidad

Toda la lógica está encapsulada en la clase `DataExtractor` (`data_extractor.py`). El flujo es independiente del entorno y puede usarse en scripts, notebooks o dashboards. Se recomienda usar entorno virtual y requirements.txt para instalar dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejemplo de flujo completo

```python
from data_extractor import DataExtractor
ext = DataExtractor()
# Extraer datos de la API o cargar CSV
ext.load_data_api(query="#bitcoin", max_results=100)
# Análisis de hashtags
analytics = ext.analytics_hashtags_extended()
# WordCloud
ext.generate_hashtag_wordcloud()
# Modelado de tópicos
topics = ext.model_topics(num_topics=5)
print("Tópicos:", topics)
# Análisis de sentimiento
df_sent = ext.analyze_sentiment(method='textblob')
# Resumen extractivo
summary = ext.parse_and_summarize(summary_ratio=0.3)
print("Resumen:", summary)
```

## Visualización y dashboard (opcional)

Se incluye un ejemplo de dashboard en Streamlit (`dashboard.py`) para explorar los resultados de forma interactiva. No es obligatorio, pero demuestra la reutilización de la lógica y facilita la exploración visual.

## Referencias

- RapidAPI: https://rapidapi.com/
- Gensim: https://radimrehurek.com/gensim/
- TextBlob: https://textblob.readthedocs.io/
- spaCy: https://spacy.io/
- NLTK: https://www.nltk.org/
- WordCloud: https://amueller.github.io/word_cloud/
- Pandas: https://pandas.pydata.org/
- Matplotlib: https://matplotlib.org/
- Streamlit: https://streamlit.io/
- spacytextblob: https://spacytextblob.github.io/

## Referencias

- 42 AI Bootcamp (Organización orientada a IA dentro de 42 Paris creada por estudiantes):
    
    https://42-ai.github.io/
    
    https://github.com/42-AI
    
- Kaggle dataset:
    
    https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets
    
- Pandas documentation:
    
    https://pandas.pydata.org/docs/user_guide/index.html
    
- Matplotlib documentation:
    
    https://matplotlib.org/stable/users/index.html
    
- Seaborn tutorial:
    
    https://seaborn.pydata.org/tutorial.html
    
- WordCloud documentation:
    
    https://amueller.github.io/word_cloud/
    
- Regex tester:
    
    https://regex101.com/
    
- Unicode standard (TR44):
    
    https://unicode.org/reports/tr44/