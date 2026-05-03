# AEC2 – Análisis de Sentimiento y Tendencias en Twitter

## Introducción

En esta actividad se nos pide realizar un análisis completo de tweets, extrayendo datos directamente desde una API en tiempo real, procesándolos, y luego ejecutando varias técnicas de procesamiento de NPL para descubrir patrones, sentimientos y temas principales. 

El enfoque es el de crear una clase única y centralizada llamada `DataExtractor` que encapsule todo el pipeline de principio a fin. De esta forma, el usuario puede simplemente cargar datos (desde API o desde un CSV local), y luego llamar a métodos para cada análisis sin tener que preocuparse por detalles de implementación. Esto hace que el código sea mantenible, reutilizable, y fácil de entender para alguien que no sabe Python profundamente.

El proyecto tiene dos modos de operación, en tiempo real donde extraemos tweets directamente desde la API de RapidAPI, y modo local donde usamos un dataset descargado de Kaggle. Esto es importante porque las APIs gratuitas siempre tienen límites de rate limiting, así que poder trabajar con datos locales es fundamental para desarrollo y pruebas.

## Selección del Dataset y Fuentes de Datos

Para esta práctica igual que en la anterior decidí trabajar con tweets sobre Bitcoin porque es un dominio activo en redes sociales, con mucha variabilidad de sentimientos (optimismo, miedo, especulación), y con una comunidad muy vocal. Esto hace que sea ideal para demostrar técnicas de análisis de sentimiento y extracción de tendencias.

Tengo dos opciones de datos:

1. **API en tiempo real** — Usando twitter-api45 disponible en RapidAPI. Esta es la forma más realista de trabajar con Twitter, pero tengo limitaciones ya que la clave gratuita devuelve alrededor de 100-200 tweets por consulta, hay límites de requests por hora, y el formato puede variar. Por eso creé un parser robusto que maneja múltiples formatos de respuesta.

2. **Dataset estático** — Como especificaba el enunciado he usado también el dataset de Kaggle utilizado en la anterior actividad  "Bitcoin Tweets" que tiene miles de tweets ya descargados. Esto es útil para pruebas rápidas y para evitar agotarse la cuota de la API durante el desarrollo.

## Estructura del Proyecto

```
AEC2/
├── data_extractor.py        # Clase principal: toda la lógica del pipeline
├── AEC2_DataExtractor.ipynb # Notebook Jupyter con ejemplos y visualizaciones
├── dashboard.py             # Dashboard interactivo con Streamlit (opcional)
├── requirements.txt         # Lista de librerías necesarias
├── .env.example             # Plantilla para configurar RAPIDAPI_KEY
└── README.md                # Este archivo
```

## El Pipeline

He diseñado un flujo que transforme tweets crudos en información útil. 

### Paso 1: Carga de Datos — Dos Caminos Posibles

La clase soporta dos métodos de carga:

**Desde API (tiempo real):**
```python
ext = DataExtractor()
ext.load_data_api(query="#bitcoin", max_results=100, output_file="tweets.csv")
```

Este método se conecta a RapidAPI usando la clave almacenada en `.env`, realiza la consulta, y guarda el resultado en CSV. Aquí es donde todo comienza. La API devuelve JSON con tweets, y aunque el endpoint dice "twitter-api45", en realidad devuelve un objeto con clave `timeline` (no `tweets` o `data` como esperarías). Esto fue un descubrimiento que tomó tiempo debuggear.

**Desde archivo local:**
```python
ext = DataExtractor(source="Bitcoin_tweets.csv")
ext.load_data()
```

Para esto uso pandas con `chunksize` para manejar archivos grandes sin cargar todo en memoria de una vez. Esto es importante si trabajas con millones de tweets.

### Paso 2: Limpieza y Normalización

Los tweets crudos son un desastre: tienen URLs, menciones, emojis, caracteres especiales, y todo mezclado. El método `clean_text()` normaliza esto:

Conservo los hashtags porque son fundamentales para el análisis posterior. Convierto todo a minúsculas, elimino URLs con regex, elimino menciones, y elimino emojis.

### Paso 3: Análisis de Hashtags — Viendo el Momento

Los hashtags son el termómetro de la conversación en Twitter. El método `extract_hashtags()` los extrae usando regex, y luego `analytics_hashtags_extended()` los analiza desde tres ángulos diferentes:

- **Vista global** — Cuáles son los hashtags más usados en todo el dataset
- **Vista por usuario** — Cuáles usuarios usan hashtags de forma masiva (potencial indicador de bots)
- **Vista por fecha** — Cómo cambian las tendencias día a día

Esto me permite responder preguntas como: ¿Cuáles son los hashtags trending? ¿Hay usuarios spam que repiten los mismos hashtags? ¿Cómo cambian las conversaciones en el tiempo?

El método también genera una nube de palabras con `generate_hashtag_wordcloud()` para visualizar rápidamente cuáles son los términos dominantes.

### Paso 4: Modelado de Tópicos con LDA

Aquí es donde entra LDA (Latent Dirichlet Allocation) que es un algoritmo probabilístico que descubre los temas ocultos en un corpus de texto. Durante el desarrollo original, noté que los tópicos salían muy ruidosos: aparecían palabras como "el", "a", "de", números, y hashtags sin formato. Por eso decidí implementar un filtrado un poco mas agresivo:

```python
# Filtrado aplicado:
# - Eliminar stopwords en inglés (the, a, an, etc)
# - Eliminar palabras muy cortas (menos de 3 caracteres)
# - Eliminar números puros
# - Eliminar hashtags (se analizan por separado)
```

Con este filtrado, los tópicos ahora son mucho más interpretables. En lugar de obtener "bitcoin the crypto mining", obtengo "bitcoin cryptocurrency ethereum mining", que es claramente más útil.

El método `model_topics(num_topics=5, passes=10)` ejecuta LDA con 5 tópicos habituales y 10 pasadas del algoritmo para convergencia. Ajustar `passes` es un tradeoff: más pasadas = mejor calidad pero más lento.

### Paso 5: Análisis de Sentimiento

El método `analyze_sentiment()` calcula dos métricas por tweet:

- **Polaridad** — Qué tan positivo o negativo es (-1 a +1). Una polaridad de 0.8 significa que el tweet es muy positivo.
- **Subjetividad** — Qué tan opinión es vs hecho (0 a 1). Una subjetividad de 0.9 significa que es muy opinión, mientras que 0.1 es muy factual.

Tengo dos implementaciones:
- **TextBlob** — Rápido, basado en diccionarios pre-entrenados
- **spaCy + spacytextblob** — Más lento pero más preciso

Para la mayoría de casos, TextBlob está bien. La idea es ver cómo reacciona la comunidad: en alcistas (bull markets), la polaridad promedio sube; en pánico (bear markets), baja.

### Paso 6: Resumen Extractivo — Lo Importante en Pocas Palabras

El método `parse_and_summarize()` resume automáticamente el corpus completo. No genera texto nuevo (eso sería abstractivo), sino que selecciona las oraciones más relevantes del original (extractivo).

El algoritmo que uso funciona así:

1. Tokenizo todo el corpus en oraciones
2. Calculo una puntuación para cada oración basándome en la frecuencia de palabras significativas
3. Selecciono las oraciones con mayor puntuación hasta alcanzar el ratio o límite de palabras


### Paso 7: Exportar Resultados

Finalmente, `export_results()` guarda todo a archivos:

- Tweets limpios + análisis en CSV
- Análisis de hashtags en CSV
- Tópicos en archivo de texto
- Sentimientos en CSV

De esta forma tienes los datos listos para importar en Excel, PowerPoint, o cualquier otra herramienta.

## Dependencias Principales

| Librería | Uso |
|---|---|
| pandas | Manejo eficiente de datos tabulares |
| requests | Llamadas HTTP a la API |
| nltk | Tokenización, análisis sintáctico básico |
| textblob | Análisis de sentimiento rápido |
| gensim | Modelado LDA (con fallback si Python 3.14+) |
| spacy | NLP más avanzado, análisis de dependencias |
| wordcloud | Visualización de hashtags |
| matplotlib | Gráficos estáticos |

## Solución de Problemas

**Problema:** "ImportError: No module named gensim"  
**Solución:** Gensim tiene problemas con Python 3.14+. El código tiene un try-except que lo maneja gracefully, pero si necesitas LDA, usa Python 3.11-3.13.

**Problema:** "RAPIDAPI_KEY not found in environment"  
**Solución:** Verifica que tu `.env` está en la misma carpeta que `data_extractor.py` y que Python puede leerlo con `load_dotenv()`.

**Problema:** "Los tópicos son ruidosos o no tiene sentido"  
**Solución:** Aumenta `min_word_len` en `model_topics()` a 4 o 5 para filtrado más agresivo.

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