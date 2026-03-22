# AEC1 – Analisis de Sentimiento y Tendencias en Redes Sociales

---

## Introducción

Este proyecto es un gran punto de partida para explorar las técnicas básicas de extracción, limpieza y análisis de texto aplicadas a un conjunto de tweets sobre Bitcoin. 

El objetivo es demostrar un flujo reproducible en el que extraer datos, limpiar y normalizar texto, extraer entidades, y producir métricas y visualizaciones que permitan interpretar tendencias y detectar patrones. 

El repositorio incluye el notebook con la implementación principal, un mini-dashboard opcional para visualización interactiva y ejemplos de salida (gráficos y wordclouds). En la sección de ejecución se indican las dependencias y los pasos mínimos para reproducir los resultados localmente.


## Estructura del proyecto

```
AEC1/
├── AEC1_DataExtractor.ipynb   # Notebook principal con toda la implementacion
├── dashboard.py               # (Bonus) Mini-dashboard interactivo con Streamlit
├── Bitcoin_tweets_dataset_2.csv   # Dataset original (no incluido en el repo – ver abajo)
├── Bitcoin_tweets_cleaned.csv     # Dataset procesado generado por el notebook
├── wordcloud_hashtags.png     # Wordcloud de hashtags (output)
├── wordcloud_words.png        # Wordcloud de palabras (output)
├── top20_hashtags.png         # Barplot top 20 hashtags (output)
├── hashtag_evolution.png      # Evolucion temporal hashtags (output)
└── README.md                  # Este archivo
```


---

## Flujo 

### 1. Extraccion de datos

Cargo el CSV con `pandas.read_csv` usando:
- `chunksize=100_000` para leer por bloques.
- `low_memory=False` para evitar tipos raros.
- `lineterminator='\n'` para normalizar finales de linea.
- `encoding='utf-8'` para asegurar codificacion correcta.

Luego concateno los chunks y lo guardo en `self.data`.

### 2. Almacenamiento

Guardo el resultado en `Bitcoin_tweets_cleaned.csv` con UTF-8. Elegi CSV porque es mas ligero que JSON para datos tabulares y se abre en cualquier sitio (pandas, Excel, SQL, etc.).

### 3. Limpieza y normalizacion (`clean_text`)

En esta etapa preparo el texto para que el análisis funcione de forma fiable: quito ruido, unifico formatos y dejo sólo lo que aporta valor. Personalmente lo hago así:

- Paso 1 — minúsculas: convierto todo a minúsculas con `str.lower()` para que "Bitcoin" y "bitcoin" se traten igual y no se fraccione el conteo.
- Paso 2 — eliminar URLs: borro enlaces porque suelen ser identificadores largos que no ayudan al análisis semántico y ensucian las nubes de palabras.
- Paso 3 — eliminar menciones: quito los `@usuario` para centrarme en el mensaje, no en quién lo escribió.
- Paso 4 — quitar emojis y símbolos no textuales: empleo las categorías Unicode (So, Sk, Cs) para filtrar pictogramas que interfieren con la tokenización.
- Paso 5 — limpiar caracteres especiales pero conservar `#`: elimino signos y puntuación que no aportan, pero mantengo los hashtags porque son las entidades que quiero extraer.
- Paso 6 — normalizar espacios: colapso múltiples espacios en uno solo para que la tokenización sea consistente.

Cada paso está diseñado para reducir el ruido y facilitar las siguientes fases (extracción de hashtags y agregaciones). Si quieres, puedo incluir ejemplos concretos antes/después para cada transformación.

### 4. Extraccion de hashtags (`extract_hashtags`)

Regex: `#(\w+)`. Devuelvo todo en minusculas y deduplico manteniendo el orden.

### 5. Analisis extendido (`analytics_hashtags_extended`)

1. Aplico `clean_text` y `extract_hashtags`.
2. Convierto `date` a `datetime` y me quedo con la fecha.
3. Exploto la lista de hashtags (1 fila por hashtag).
4. Calculo tres agregaciones:
   - **overall**: frecuencia global.
   - **by_user**: frecuencia por usuario.
   - **by_date**: frecuencia por dia.

### 6. Posibles bots

Miro cuanto del uso total de hashtags viene del top 1% de usuarios. Si concentran demasiado, puede ser actividad automatizada.

---

## Instrucciones de ejecucion

### Requisitos

```bash
pip install pandas wordcloud matplotlib seaborn streamlit
```

### Notebook principal

1. Descarga `Bitcoin_tweets_dataset_2.csv` desde Kaggle y colocalo en este directorio.
2. Abre `AEC1_DataExtractor.ipynb` en VS Code, JupyterLab o Google Colab.
3. Ejecuta las celdas en orden (`Run All`).

### Dashboard interactivo (Bonus)

```bash
streamlit run dashboard.py
```

Luego abre `http://localhost:8501`.

---

## Visualizaciones generadas

| Archivo | Descripcion |
|---------|-------------|
| `top20_hashtags.png` | Barplot horizontal con los 20 hashtags mas frecuentes |
| `hashtag_evolution.png` | Evolucion temporal (diaria) de los top 5 hashtags |
| `wordcloud_hashtags.png` | Wordcloud de hashtags |
| `wordcloud_words.png` | Wordcloud de palabras generales (sin hashtags ni stopwords) |

---

## Referencias y recursos

1. 42 AI (organizacion oficial): proyectos de IA/DS, con ejemplos de limpieza, parsing y pipelines.
   https://github.com/42-AI
   https://42-ai.github.io/
2. 42 School: proyectos y ramas con foco en parsing/limpieza de texto y pipelines de datos (inspiracion metodologica).
3. Kaggle Dataset: Bitcoin Tweets Dataset 2.  
   https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets/data?select=Bitcoin_tweets_dataset_2.csv
4. pandas: `read_csv` y lectura por chunks.  
   https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
5. pandas: `to_datetime` para normalizar fechas.  
   https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
6. W3Schools: Regex y manejo de strings en Python (repaso rapido).  
   https://www.w3schools.com/python/python_regex.asp
7. WordCloud (lib oficial): generacion de nubes de palabras.  
   https://amueller.github.io/word_cloud/
8. Matplotlib: graficos basicos (barh, figuras y estilos).  
   https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html
