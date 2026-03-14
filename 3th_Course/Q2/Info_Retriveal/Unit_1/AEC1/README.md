# AEC1 – Analisis de Sentimiento y Tendencias en Redes Sociales
## Extraccion y Tratamiento de Datos – Bitcoin Tweets

**Asignatura:** Information Retrieval | **Curso:** 3er Curso – Q2  
**Entrega:** AEC1 – Fase inicial del proyecto

---

## Fuente de datos (lo que use y por que)

| Campo | Detalle |
|-------|---------|
| Dataset | Bitcoin Tweets Dataset 2 |
| Origen | [Kaggle – kaushiksuresh147](https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets/data?select=Bitcoin_tweets_dataset_2.csv) |
| Archivo | `Bitcoin_tweets_dataset_2.csv` |
| Formato | CSV (separador `,`, fin de linea `\n`, codificacion UTF-8) |
| Columnas clave | `date`, `user_name`, `text` |

Lo eligi porque ya viene bien estructurado, tiene volumen suficiente para analizar hashtags y me permite trabajar con chunks sin petar memoria. Ademas, en Kaggle es facil reproducir y compartir.

---

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

> **Nota:** El CSV original no se sube por tamano. Descargalo desde Kaggle y colocalo en este directorio antes de ejecutar el notebook.

---

## Metodologia (como lo hice)

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

Uso regex y normalizo el texto. En resumen:

| Paso | Regex / Funcion | Resultado |
|------|-----------------|-----------|
| Lowercase | `str.lower()` | Normalizo mayusculas |
| Eliminar URLs | `https?://\S+\|www\.\S+` | Quito enlaces |
| Eliminar menciones | `@\w+` | Quito `@usuario` |
| Eliminar emojis | `unicodedata.category` | Filtro `So`, `Sk`, `Cs` |
| Eliminar especiales | `[^\w\s#]` | Conservo `#` y alfanumericos |
| Colapsar espacios | `\s+` → ` ` | Un solo espacio entre tokens |

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

## Referencias y recursos (lo que consulte)

1. Kaggle Dataset: Bitcoin Tweets Dataset 2.  
   https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets/data?select=Bitcoin_tweets_dataset_2.csv
2. pandas: `read_csv` y lectura por chunks.  
   https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
3. pandas: `to_datetime` para normalizar fechas.  
   https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
4. W3Schools: Regex y manejo de strings en Python (repaso rapido).  
   https://www.w3schools.com/python/python_regex.asp
5. WordCloud (lib oficial): generacion de nubes de palabras.  
   https://amueller.github.io/word_cloud/
6. Matplotlib: graficos basicos (barh, figuras y estilos).  
   https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html
7. 42 AI (organizacion oficial): proyectos de IA/DS, con ejemplos de limpieza, parsing y pipelines.
   https://github.com/42-AI
8. 42 School: proyectos y ramas con foco en parsing/limpieza de texto y pipelines de datos (inspiracion metodologica).
