# Documentación del Proyecto: Análisis de Sentimiento y Tendencias en Twitter

## 1. Estructura y Centralización
Toda la lógica de extracción, limpieza y análisis está centralizada en la clase `DataExtractor` (ver `data_extractor.py`). Esta clase permite:
- Cargar datos desde archivo local o desde la API de Twitter (RapidAPI).
- Limpiar y normalizar texto.
- Extraer hashtags y analizar su frecuencia global, por usuario y por fecha.
- Generar WordCloud de hashtags.
- Modelar tópicos con LDA (gensim).
- Analizar sentimiento (TextBlob o spaCy).
- Parsing y resumen extractivo (NLTK).

## 2. Métodos y Técnicas Aplicadas

### 2.1 Extracción de datos vía API
- Método: `load_data_api()`
- Conexión segura usando variable de entorno `RAPIDAPI_KEY`.
- Adaptación de columnas mínimas: `user_name`, `date`, `text`.
- Manejo robusto de errores y guardado en CSV.

### 2.2 Limpieza y normalización
- Método: `clean_text()`
- Elimina URLs, menciones, símbolos y normaliza espacios.
- Mantiene hashtags para análisis posterior.

### 2.3 Extracción y análisis de hashtags
- Método: `extract_hashtags()` y `analytics_hashtags_extended()`
- Extrae hashtags únicos por tweet.
- Calcula frecuencias globales, por usuario y por fecha.

### 2.4 WordCloud
- Método: `generate_hashtag_wordcloud()`
- Visualiza los hashtags más frecuentes.

### 2.5 Modelado de tópicos (LDA)
- Método: `model_topics()`
- Tokeniza texto limpio y aplica LDA con gensim.
- Devuelve lista de tópicos (palabras clave por tópico).

### 2.6 Análisis de sentimiento
- Método: `analyze_sentiment()`
- Usa TextBlob (por defecto) o spaCy+spacytextblob.
- Calcula polaridad y subjetividad para cada tweet.

### 2.7 Parsing y resumen extractivo
- Método: `parse_and_summarize()`
- Tokeniza oraciones y palabras (NLTK).
- Calcula frecuencia de palabras y selecciona oraciones más relevantes.
- Devuelve resumen extractivo del corpus.

## 3. Reproducibilidad
- Todas las rutas y claves se gestionan por variables de entorno o argumentos.
- El código es modular y reutilizable en scripts, notebooks o dashboards.
- Se recomienda usar entorno virtual y requirements.txt para dependencias.

## 4. Ejecución rápida
```bash
# Activar entorno virtual
source .venv/bin/activate
# Instalar dependencias
pip install -r requirements.txt
# Exportar clave de API
export RAPIDAPI_KEY="tu_clave"
# Usar DataExtractor en notebook o script
```

## 5. Resultados esperados
- Tablas y gráficos de hashtags, usuarios y evolución temporal.
- WordCloud visual.
- Lista de tópicos extraídos.
- Distribución de sentimiento y ejemplos de resúmenes.

## 6. Referencias
- RapidAPI, Gensim, TextBlob, spaCy, NLTK, WordCloud, Pandas, Matplotlib.

---

**Para más detalles, consulta el código fuente y los ejemplos de uso en el notebook/script principal.**
