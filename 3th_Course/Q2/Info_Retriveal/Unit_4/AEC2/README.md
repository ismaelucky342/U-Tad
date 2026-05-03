# AEC2 – Análisis de Sentimiento y Tendencias en Twitter

## Introducción

En esta actividad se nos pide realizar un análisis completo de tweets, extrayendo datos directamente desde una API en tiempo real, procesándolos, y luego ejecutando varias técnicas de procesamiento de lenguaje natural para descubrir patrones, sentimientos y temas principales. Lo interesante de este proyecto es que combina varias disciplinas: obtención de datos (API), limpieza y normalización, estadística básica con hashtags, machine learning con modelado de tópicos (LDA), análisis de sentimiento, y finalmente generación de resúmenes automáticos.

Mi enfoque fue crear una clase única y centralizada llamada `DataExtractor` que encapsule todo el pipeline de principio a fin. De esta forma, el usuario puede simplemente cargar datos (desde API o desde un CSV local), y luego llamar a métodos para cada análisis sin tener que preocuparse por detalles de implementación. Esto hace que el código sea mantenible, reutilizable, y fácil de entender para alguien que no sabe Python profundamente.

El proyecto tiene dos modos de operación: modo "tiempo real" donde extraemos tweets directamente desde la API de RapidAPI, y modo "local" donde usamos un dataset descargado de Kaggle. Esto es importante porque las APIs gratuitas siempre tienen límites de rate limiting, así que poder trabajar con datos locales es fundamental para desarrollo y pruebas.

## Selección del Dataset y Fuentes de Datos

Para esta práctica decidí trabajar con tweets sobre Bitcoin porque es un dominio activo en redes sociales, con mucha variabilidad de sentimientos (optimismo, miedo, especulación), y con una comunidad muy vocal. Esto hace que sea ideal para demostrar técnicas de análisis de sentimiento y extracción de tendencias.

Tengo dos opciones de datos:

1. **API en tiempo real** — Usando `twitter-api45` disponible en RapidAPI. Esta es la forma más realista de trabajar con Twitter, pero tiene limitaciones: la clave gratuita devuelve alrededor de 100-200 tweets por consulta, hay límites de requests por hora, y el formato puede variar. Por eso creé un parser robusto que maneja múltiples formatos de respuesta.

2. **Dataset estático** — He usado también el dataset de Kaggle "Bitcoin Tweets" que tiene miles de tweets ya descargados. Esto es útil para pruebas rápidas y para evitar agotarse la cuota de la API durante el desarrollo.

La estructura es flexible: puedes comenzar con datos locales para desarrollo, y una vez que todo funciona bien, cambiar a la API real.

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

## El Pipeline Completo: De Tweets Crudos a Insights

He diseñado un flujo que transforme tweets crudos en información útil. Aunque podría hacerlo todo en scripts separados, decidí unificarlo en una clase porque así el usuario tiene un interfaz limpio y consistente.

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

```python
# Lo que hace internamente:
# "Check out $BTC 🚀 #bitcoin https://t.co/xyz @coinbase" 
# se convierte en:
# "check out btc #bitcoin"
```

Conservo los hashtags porque son fundamentales para el análisis posterior. Convierto todo a minúsculas, elimino URLs con regex, elimino menciones, y elimino emojis.

### Paso 3: Análisis de Hashtags — Viendo el Momento

Los hashtags son el termómetro de la conversación en Twitter. El método `extract_hashtags()` los extrae usando regex, y luego `analytics_hashtags_extended()` los analiza desde tres ángulos diferentes:

- **Vista global** — Cuáles son los hashtags más usados en todo el dataset
- **Vista por usuario** — Cuáles usuarios usan hashtags de forma masiva (potencial indicador de bots)
- **Vista por fecha** — Cómo cambian las tendencias día a día

Esto me permite responder preguntas como: ¿Cuáles son los hashtags trending? ¿Hay usuarios spam que repiten los mismos hashtags? ¿Cómo cambian las conversaciones en el tiempo?

El método también genera una nube de palabras con `generate_hashtag_wordcloud()` para visualizar rápidamente cuáles son los términos dominantes.

### Paso 4: Modelado de Tópicos con LDA

Aquí es donde comienza lo interesante. LDA (Latent Dirichlet Allocation) es un algoritmo probabilístico que descubre los temas ocultos en un corpus de texto. Durante el desarrollo original, noté que los tópicos salían muy ruidosos: aparecían palabras como "el", "a", "de", números, y hashtags sin formato. Por eso decidí implementar un filtrado agresivo:

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

Originalmente el ratio estaba en 0.3 (30%), lo que producía resúmenes demasiado largos. Lo reduje a 0.05 (5%) y añadí un límite de 500 palabras máximo. De esta forma los resúmenes son compactos pero completos.

```python
resumen = ext.parse_and_summarize(summary_ratio=0.05, max_length=500)
# Resultado: resumen conciso de max 500 palabras
```

### Paso 7: Exportar Resultados

Finalmente, `export_results()` guarda todo a archivos:

- Tweets limpios + análisis en CSV
- Análisis de hashtags en CSV
- Tópicos en archivo de texto
- Sentimientos en CSV

De esta forma tienes los datos listos para importar en Excel, PowerPoint, o cualquier otra herramienta.

## Instalación y Configuración

### Paso 1: Clonar y crear entorno virtual

```bash
cd /3th_Course/Q2/Info_Retriveal/Unit_4/AEC2
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### Paso 2: Configurar la Clave de API

Esta es la parte crítica. Para usar `load_data_api()` necesitas una clave de RapidAPI:

1. Ve a [rapidapi.com](https://rapidapi.com) y crea una cuenta gratuita
2. Busca "twitter-api45" en el marketplace
3. Suscríbete al plan gratuito
4. Copia tu clave de API (debería estar en tu dashboard)
5. Copia `.env.example` a `.env`:
   ```bash
   cp .env.example .env
   ```
6. Abre `.env` y reemplaza `your_rapidapi_key_here` con tu clave real

**Importante:** Nunca hardcodees la clave en el código. Nunca la commites a Git. Usa `.env` y asegúrate de que `.gitignore` incluye `.env`.

### Paso 3: Verificar que todo funciona

```bash
python test_api.py
```

Este script ejecuta 5 pruebas:
1. Parser maneja múltiples formatos de API response
2. CSV load funciona correctamente
3. Análisis de sentimiento funciona
4. Resumen extractivo funciona
5. Limpieza de texto funciona

Si todas pasan, estás listo.

## Ejemplo de Uso Completo

```python
from data_extractor import DataExtractor

# Crear instancia
ext = DataExtractor()

# Opción A: API en tiempo real
ext.load_data_api(query="#bitcoin", max_results=100, output_file="tweets.csv")

# Opción B: Dataset local
# ext = DataExtractor(source="Bitcoin_tweets.csv")
# ext.load_data()

# Análisis de hashtags
print("=== ANÁLISIS DE HASHTAGS ===")
analytics = ext.analytics_hashtags_extended()
print(f"Hashtags únicos: {len(analytics['overall'])}")
ext.generate_hashtag_wordcloud(overall_df=analytics['overall'])

# Modelado de tópicos
print("\n=== TÓPICOS DESCUBIERTOS ===")
topics = ext.model_topics(num_topics=5, passes=10)
for i, topic in enumerate(topics, 1):
    print(f"Tópico {i}: {', '.join(topic)}")

# Sentimiento
print("\n=== SENTIMIENTO ===")
df_sentiment = ext.analyze_sentiment(method='textblob')
print(df_sentiment[['clean_text', 'sentiment_polarity', 'sentiment_subjectivity']].head(10))

# Resumen
print("\n=== RESUMEN ===")
resumen = ext.parse_and_summarize(summary_ratio=0.05, max_length=500)
print(resumen)

# Exportar
print("\n=== EXPORTANDO RESULTADOS ===")
ext.export_results(output_dir="results")
```

## Decisiones Técnicas y Tradeoffs

### Por qué Python y no otra cosa?

Python tiene el mejor ecosistema para NLP: NLTK, spaCy, gensim, TextBlob son librerías maduras y bien documentadas. Además, para un proyecto académico es rápido de desarrollar.

### Por qué LDA y no redes neuronales?

LDA es interpretable: ves exactamente qué palabras forman cada tópico. Las redes neuronales (como transformers) pueden hacer análisis más sofisticados, pero es overkill para esta tarea y mucho más lento. LDA es el estándar de la industria para topic modeling.

### Por qué TextBlob para sentimiento?

TextBlob usa diccionarios pre-entrenados (VADER, que es excelente para redes sociales). Para un análisis rápido es suficiente. Si necesitaras precisión extrema, usarías un modelo fine-tuned en datos de Twitter, pero eso es mucho más complejo.

### Por qué extraer a CSV local después de la API?

Rate limiting. La API gratuita tiene límites bajos. Si guargas localmente después de extraer, puedes hacer pruebas sin quemar tu cuota.

## Dependencias Principales

| Librería | Razón |
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

## Referencias y Inspiración

He usado ideas de varios proyectos de referencia en NLP y procesamiento de redes sociales. La estructura del código está inspirada en patrones profesionales de data science: separación de concerns, métodos pequeños y focalizados, manejo consistente de errores.

