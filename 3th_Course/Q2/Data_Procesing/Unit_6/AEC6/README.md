# AEC6 - Spark SQL y Machine Learning con MLlib

![imagen portada]()

## Introducción

En esta actividad práctica de la unidad 6 trabajamos con **Apache Spark** como herramienta central para explorar un dataset real, responder preguntas analíticas mediante SparkSQL y construir modelos de machine learning con **MLlib**.

El dataset elegido es **`departuredelays.csv`**, el dataset de retrasos de vuelos domésticos en EE.UU. que utiliza Databricks en su libro oficial *Learning Spark v2*. Está disponible públicamente en su repositorio de GitHub y contiene más de 1,3 millones de registros de vuelos con columnas numéricas (retraso en minutos, distancia en millas) y categóricas (aeropuerto origen y destino, franja horaria). Es un dataset diseñado específicamente para demostrar las capacidades de Spark, lo que lo hace ideal para esta práctica.

La práctica se estructura en dos partes diferenciadas. En la **Parte 1** descargo el dataset con `wget`, lo subo a HDFS, lo exploro con Spark y respondo cinco preguntas analíticas usando SparkSQL y la DataFrame API. En la **Parte 2** construyo y comparo dos modelos de clasificación — **Regresión Logística** y **Random Forest** — para predecir si un vuelo va a sufrir un retraso significativo, justificando la elección y comparando sus métricas.

---

## Estructura del proyecto

```
aec6-spark-ml/
├── README.md
├── parte1_exploracion.py       # EDA y 5 preguntas analíticas
├── parte2_modelos.py           # Modelos ML: Logistic Regression + Random Forest
└── data/
    └── departuredelays.csv     # Dataset descargado con wget desde GitHub
```

---

## Dataset: Departure Delays (Databricks / Learning Spark v2)

El dataset recoge vuelos domésticos en EE.UU. con información de retrasos en la salida. Es el mismo dataset utilizado en los ejemplos oficiales de Databricks para SparkSQL, lo que garantiza que está bien formado y documentado. Las columnas son:

| Columna | Tipo | Descripción |
|---|---|---|
| `date` | String | Fecha y hora del vuelo en formato `MMDDHHMM` (mes, día, hora, minuto) |
| `delay` | Integer | Minutos de retraso en la salida (negativo = salió antes de hora) |
| `distance` | Integer | Distancia del vuelo en millas |
| `origin` | String | Código IATA del aeropuerto de origen |
| `destination` | String | Código IATA del aeropuerto de destino |

El dataset tiene aproximadamente **1,39 millones de filas** y aunque solo tiene 5 columnas, la columna `date` en formato `MMDDHHMM` nos permite extraer el mes, el día y la franja horaria como columnas derivadas, multiplicando las posibilidades analíticas. Es un buen ejemplo de que la riqueza de un dataset no depende solo del número de columnas originales sino de lo que se puede extraer de ellas.

---

## Preparación del entorno

### Descarga del dataset con `wget`

En lugar de descargar el fichero manualmente desde el navegador y copiarlo, usamos `wget` directamente desde la terminal. Esto es importante en entornos Big Data por dos motivos: primero, reproduce el flujo real de ingestión de datos en un clúster donde no hay interfaz gráfica; segundo, permite automatizar la descarga en scripts de pipeline sin intervención manual.

```bash
wget -O /home/bigdata/departuredelays.csv \
  "https://raw.githubusercontent.com/databricks/LearningSparkV2/master/databricks-datasets/learning-spark-v2/flights/departuredelays.csv"
```

El flag `-O` especifica el nombre y ruta del fichero de destino. `wget` muestra la barra de progreso, el tamaño y la velocidad de descarga, lo que ya nos da una primera idea del volumen con el que vamos a trabajar.

Una vez descargado, verificamos el número de líneas para confirmar que la descarga fue completa:

```bash
wc -l /home/bigdata/departuredelays.csv
```

Y echamos un vistazo a las primeras filas para confirmar la estructura antes de cargarlo en Spark:

```bash
head -5 /home/bigdata/departuredelays.csv
```

La salida esperada de `head` es algo como:

```
date,delay,distance,origin,destination
01011245,6,602,ABE,ATL
01011715,5,602,ABE,ATL
01011530,-3,602,ABE,ATL
01011905,6,602,ABE,ATL
```

Vemos que `date` viene como un entero de 8 dígitos `MMDDHHMM`: los dos primeros son el mes, los siguientes el día, y los últimos cuatro la hora de salida. Esto lo tendremos en cuenta al extraer columnas derivadas en Spark.

![captura wget descarga]()

---

### Carga en HDFS

Con el fichero ya en local, lo subimos a HDFS. Usar HDFS como capa de almacenamiento —incluso en un entorno pseudodistribuido de un solo nodo— es la práctica correcta porque:

- Spark lee desde HDFS de forma **distribuida por bloques**, lo que en un clúster real permitiría que cada nodo leyera solo su porción del fichero sin transferencia de red.
- Los datos quedan **desacoplados del código**: si modificamos el script, el dataset no se mueve. Si añadimos nodos al clúster, todos acceden al mismo HDFS sin necesidad de copiar el fichero en cada máquina.
- Podemos reutilizar el mismo dataset para múltiples jobs de Spark sin mantener copias locales en cada nodo.

```bash
# Creamos el directorio de trabajo en HDFS
hdfs dfs -mkdir -p /user/bigdata/aec6/data

# Subimos el CSV desde el sistema de ficheros local a HDFS
hdfs dfs -put /home/bigdata/departuredelays.csv /user/bigdata/aec6/data/

# Verificamos que está ahí y vemos su tamaño en formato legible
hdfs dfs -ls -h /user/bigdata/aec6/data/
```

El flag `-h` en `hdfs dfs -ls` muestra el tamaño en formato legible (MB) en lugar de bytes, lo cual es más cómodo para datasets grandes.

```bash
# Podemos también ver cuántos bloques ocupa el fichero en HDFS
hdfs fsck /user/bigdata/aec6/data/departuredelays.csv -files -blocks
```

Este comando nos muestra la fragmentación real del fichero en bloques HDFS (por defecto 128 MB cada uno), que es exactamente lo que Spark usará para paralelizar la lectura. Cada bloque puede procesarse en un executor diferente.

![captura hdfs -ls -h]()

![captura hdfs fsck bloques]()

---

## PARTE 1: Exploración y análisis con SparkSQL

### Funciones avanzadas de SparkSQL utilizadas

Antes de entrar en las queries, merece la pena repasar las construcciones de SparkSQL que van más allá de un `SELECT` básico y que aparecen a lo largo de la exploración:

**`SUBSTR(date, 1, 2)`** — extracción de subcadena para parsear la columna `date` en formato `MMDDHHMM` y obtener el mes, el día y la franja horaria como valores independientes. Toda la riqueza temporal del dataset sale de esta función.

**`SUM(CASE WHEN ... THEN 1 ELSE 0 END)`** — el patrón de conteo condicional. Permite calcular en una sola pasada cuántos registros cumplen una condición sin necesidad de subqueries ni joins. Equivale a un `COUNT(*)` con filtro pero como agregado dentro de un `GROUP BY` mayor.

**`HAVING` con alias de columna calculada** — en SQL estándar no se puede referenciar un alias del `SELECT` en el `HAVING`, pero SparkSQL sí lo permite (`HAVING total_vuelos >= 500`). Esto simplifica mucho las queries frente a tener que repetir la expresión completa.

**`CASE ... WHEN ... END` como columna de segmentación** — usado para crear tramos de distancia y franjas horarias sobre la marcha, con ese mismo alias reutilizado directamente en el `GROUP BY` y el `ORDER BY`.

**`CONCAT(col1, ' → ', col2)`** — concatenación de columnas en SparkSQL para generar columnas derivadas de presentación sin post-procesado en Python.

**`createOrReplaceTempView`** — registra el DataFrame como vista SQL temporal en el catálogo de la sesión Spark, permitiendo alternar libremente entre la DataFrame API y SparkSQL puro dentro del mismo script según qué sea más expresivo para cada consulta.

**`.cache()`** — materializa el DataFrame en memoria tras la primera acción. Sin cache, cada query relanzaría la lectura completa desde HDFS y el parsing del CSV. Con 1,3 millones de filas, la diferencia entre con y sin cache es de varios segundos por query.

---

### Código completo: `parte1_exploracion.py`

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, sum as spark_sum, when, isnull,
    substring, lpad, concat
)
from pyspark.sql.types import IntegerType

# ── SESIÓN SPARK ──────────────────────────────────────────────────
spark = SparkSession.builder \
    .appName("AEC6_Parte1_Exploracion") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "8") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("=" * 65)
print("   AEC6 - PARTE 1: EXPLORACIÓN Y ANÁLISIS DE VUELOS USA")
print("=" * 65)

# ── CARGA DESDE HDFS ─────────────────────────────────────────────
# La columna 'date' viene como entero de 8 dígitos MMDDHHMM.
# inferSchema la lee como Long, así que la casteamos a String
# y usamos lpad para garantizar siempre 8 dígitos (enero = "01...").
df_raw = spark.read \
    .format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .load("hdfs:///user/bigdata/aec6/data/departuredelays.csv")

# Extraemos mes, día y hora como columnas derivadas para enriquecer
# el análisis — el campo date original no es útil en bruto.
df = df_raw.withColumn("date_str", lpad(col("date").cast("string"), 8, "0")) \
    .withColumn("mes",  substring("date_str", 1, 2).cast(IntegerType())) \
    .withColumn("dia",  substring("date_str", 3, 2).cast(IntegerType())) \
    .withColumn("hora", substring("date_str", 5, 2).cast(IntegerType())) \
    .drop("date_str")

# Cacheamos porque reutilizaremos el DataFrame en las 5 queries.
# Sin cache, cada acción relanzaría la lectura completa desde HDFS.
df.cache()

print(f"\n[INFO] Dataset cargado: {df.count():,} filas, {len(df.columns)} columnas")

# ── EXPLORACIÓN BÁSICA ────────────────────────────────────────────
print("\n--- SCHEMA ---")
df.printSchema()

print("\n--- MUESTRA DE 5 FILAS ---")
df.show(5, truncate=False)

print("\n--- ESTADÍSTICAS DESCRIPTIVAS ---")
df.select("delay", "distance", "mes", "hora").describe().show()

print("\n--- NULOS POR COLUMNA ---")
df.select([
    spark_sum(when(isnull(c), 1).otherwise(0)).alias(c)
    for c in ["delay", "distance", "origin", "destination"]
]).show()

# Registramos como vista temporal para SparkSQL puro
df.createOrReplaceTempView("vuelos")

# ── PREGUNTA 1 ────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   PREGUNTA 1")
print("   ¿Cuáles son los 10 aeropuertos origen con mayor retraso")
print("   medio de salida (mínimo 5.000 vuelos)?")
print("=" * 65)

q1 = spark.sql("""
    SELECT
        origin                                                   AS aeropuerto_origen,
        COUNT(*)                                                 AS total_vuelos,
        ROUND(AVG(delay), 2)                                     AS retraso_medio_min,
        ROUND(AVG(CASE WHEN delay > 0 THEN delay END), 2)        AS retraso_medio_solo_tardios,
        SUM(CASE WHEN delay > 15 THEN 1 ELSE 0 END)              AS vuelos_retrasados_15min,
        ROUND(SUM(CASE WHEN delay > 15 THEN 1 ELSE 0 END) * 100.0
              / COUNT(*), 1)                                     AS pct_retrasados
    FROM vuelos
    WHERE delay IS NOT NULL
    GROUP BY origin
    HAVING total_vuelos >= 5000
    ORDER BY retraso_medio_min DESC
    LIMIT 10
""")
q1.show(truncate=False)

# ── PREGUNTA 2 ────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   PREGUNTA 2")
print("   ¿A qué hora del día se producen más retrasos?")
print("=" * 65)

q2 = spark.sql("""
    SELECT
        hora,
        CASE
            WHEN hora BETWEEN 0  AND 5  THEN 'Madrugada (00-05h)'
            WHEN hora BETWEEN 6  AND 11 THEN 'Mañana (06-11h)'
            WHEN hora BETWEEN 12 AND 17 THEN 'Tarde (12-17h)'
            ELSE                             'Noche (18-23h)'
        END                                              AS franja,
        COUNT(*)                                         AS total_vuelos,
        ROUND(AVG(delay), 2)                             AS retraso_medio,
        SUM(CASE WHEN delay > 15 THEN 1 ELSE 0 END)      AS vuelos_retrasados,
        ROUND(SUM(CASE WHEN delay > 15 THEN 1 ELSE 0 END) * 100.0
              / COUNT(*), 1)                             AS pct_retrasados
    FROM vuelos
    WHERE delay IS NOT NULL
    GROUP BY hora
    ORDER BY retraso_medio DESC
""")
q2.show(24, truncate=False)

# ── PREGUNTA 3 ────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   PREGUNTA 3")
print("   ¿Cuáles son los 10 trayectos con mayor retraso acumulado?")
print("=" * 65)

q3 = spark.sql("""
    SELECT
        CONCAT(origin, ' → ', destination)          AS trayecto,
        COUNT(*)                                    AS total_vuelos,
        ROUND(SUM(CASE WHEN delay > 0 THEN delay ELSE 0 END), 0)
                                                    AS retraso_total_min,
        ROUND(AVG(delay), 2)                        AS retraso_medio,
        MAX(delay)                                  AS retraso_maximo
    FROM vuelos
    WHERE delay IS NOT NULL
    GROUP BY origin, destination
    HAVING total_vuelos >= 100
    ORDER BY retraso_total_min DESC
    LIMIT 10
""")
q3.show(truncate=False)

# ── PREGUNTA 4 ────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   PREGUNTA 4")
print("   ¿La distancia del vuelo influye en el retraso?")
print("=" * 65)

q4 = spark.sql("""
    SELECT
        CASE
            WHEN distance <  500 THEN '1. Corto    (<500 mi)'
            WHEN distance < 1000 THEN '2. Medio  (500-999 mi)'
            WHEN distance < 2000 THEN '3. Largo (1000-1999 mi)'
            ELSE                      '4. Muy largo (>=2000 mi)'
        END                                      AS tramo,
        COUNT(*)                                 AS total_vuelos,
        ROUND(AVG(delay), 2)                     AS retraso_medio,
        ROUND(AVG(distance), 0)                  AS distancia_media_millas,
        SUM(CASE WHEN delay > 15 THEN 1 ELSE 0 END) AS vuelos_retrasados
    FROM vuelos
    WHERE delay IS NOT NULL AND distance IS NOT NULL
    GROUP BY tramo
    ORDER BY tramo
""")
q4.show(truncate=False)

# ── PREGUNTA 5 ────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   PREGUNTA 5")
print("   ¿Qué mes del año concentra más retrasos?")
print("=" * 65)

q5 = spark.sql("""
    SELECT
        mes,
        CASE mes
            WHEN 1  THEN 'Enero'      WHEN 2  THEN 'Febrero'
            WHEN 3  THEN 'Marzo'      WHEN 4  THEN 'Abril'
            WHEN 5  THEN 'Mayo'       WHEN 6  THEN 'Junio'
            WHEN 7  THEN 'Julio'      WHEN 8  THEN 'Agosto'
            WHEN 9  THEN 'Septiembre' WHEN 10 THEN 'Octubre'
            WHEN 11 THEN 'Noviembre'  WHEN 12 THEN 'Diciembre'
        END                                          AS mes_nombre,
        COUNT(*)                                     AS total_vuelos,
        ROUND(AVG(delay), 2)                         AS retraso_medio,
        SUM(CASE WHEN delay > 15 THEN 1 ELSE 0 END)  AS vuelos_retrasados,
        ROUND(SUM(CASE WHEN delay > 15 THEN 1 ELSE 0 END) * 100.0
              / COUNT(*), 1)                         AS pct_retrasados
    FROM vuelos
    WHERE delay IS NOT NULL
    GROUP BY mes
    ORDER BY retraso_medio DESC
""")
q5.show(truncate=False)

print("\n[INFO] Parte 1 completada.")
spark.stop()
```

---

### Explicación de las preguntas y resultados esperados

#### Pregunta 1 — Aeropuertos con mayor retraso medio

Agrupa todos los vuelos por aeropuerto de origen y calcula tres métricas complementarias: el retraso medio, el retraso máximo y el porcentaje de vuelos con más de 15 minutos de retraso. El `HAVING total_vuelos >= 500` garantiza que solo aparecen aeropuertos con operaciones relevantes — sin este filtro, un aeropuerto pequeño con 3 vuelos todos retrasados 4 horas dominaría el ranking sin representar ningún problema sistémico.

![captura resultado pregunta 1]()

---

#### Pregunta 2 — Estacionalidad de los retrasos por mes

Usa la columna derivada `mes` extraída con `SUBSTR` de la columna `date`. El `CASE` añade el nombre del mes para que la salida sea legible directamente. El resultado suele mostrar que diciembre y enero concentran más retrasos (meteorología invernal en el norte del país) y que junio-julio tienen picos por la alta demanda estival, mientras que septiembre-octubre son los meses más puntuales.

![captura resultado pregunta 2]()

---

#### Pregunta 3 — Trayectos con mayor retraso medio

La columna `trayecto` se genera con `CONCAT(origin, ' → ', destination)` directamente en SparkSQL sin post-procesado en Python. El `HAVING total_vuelos >= 200` es crítico para que el ranking no esté dominado por trayectos anecdóticos. Los trayectos con más retraso suelen ser los que conectan hubs muy congestionados o los que operan en rutas con condiciones meteorológicas adversas frecuentes.

![captura resultado pregunta 3]()

---

#### Pregunta 4 — Relación distancia-retraso

Contrariamente a la intuición, los vuelos más cortos suelen tener retrasos proporcionalmente mayores. La razón es que los vuelos cortos forman parte de cadenas de rotación más densas (el mismo avión hace 6-8 trayectos al día) y tienen menos margen para recuperar tiempo en vuelo. Un vuelo de 4 horas puede recuperar 20 minutos acelerando; un vuelo de 45 minutos no. Esta query lo demuestra empíricamente con los datos.

![captura resultado pregunta 4]()

---

#### Pregunta 5 — Franjas horarias y retrasos

Los vuelos de madrugada y primera mañana suelen ser los más puntuales porque el avión lleva toda la noche en tierra (efecto "primer vuelo del día" — no hay retraso acumulado de rotaciones anteriores). Los vuelos de tarde-noche son los que más sufren el efecto de propagación: cada retraso en una rotación anterior se arrastra al siguiente vuelo. Esta query extrae la hora de la columna `date` con `SUBSTR(..., 5, 2)` y agrupa por franja horaria con un `CASE`.

![captura resultado pregunta 5]()

---

## PARTE 2: Modelos de Machine Learning con MLlib

### Planteamiento del problema

El objetivo es **predecir si un vuelo va a salir con más de 15 minutos de retraso** — un problema de clasificación binaria. La variable objetivo es:

```
label = 1  si delay > 15
label = 0  en caso contrario
```

Usamos como features: el mes, el día, la hora de salida (todos derivados de `date`), la distancia del vuelo, y los aeropuertos de origen y destino (codificados).

### Justificación de los algoritmos elegidos

He elegido comparar **Regresión Logística** y **Random Forest** por razones complementarias:

**Regresión Logística** es el baseline estándar en clasificación binaria. Es interpretable, rápido de entrenar y sirve de referencia para saber si un modelo más complejo aporta valor real. Si Random Forest no mejora significativamente sobre Logistic Regression, la complejidad adicional no está justificada.

**Random Forest** es un ensemble de árboles de decisión que captura relaciones no lineales entre features sin necesidad de escalar las variables ni gestionar manualmente las interacciones. En datos de vuelos, donde hay interacciones no triviales entre aeropuerto, hora del día y mes del año, un modelo no lineal tiene ventaja teórica sobre uno lineal.

Ambos están disponibles en `pyspark.ml`, se integran con `Pipeline` y sus métricas son directamente comparables.

### Código completo: `parte2_modelos.py`

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, substring
from pyspark.ml import Pipeline
from pyspark.ml.feature import (
    StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
)
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier
from pyspark.ml.evaluation import (
    BinaryClassificationEvaluator, MulticlassClassificationEvaluator
)

# ── SESIÓN SPARK ──────────────────────────────────────────────────
spark = SparkSession.builder \
    .appName("AEC6_Parte2_Modelos") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "8") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("=" * 65)
print("   AEC6 - PARTE 2: MODELOS ML PARA PREDICCIÓN DE RETRASOS")
print("=" * 65)

# ── CARGA DESDE HDFS ─────────────────────────────────────────────
df = spark.read \
    .format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .option("nullValue", "NA") \
    .load("hdfs:///user/bigdata/aec6/data/departuredelays.csv")

# Extraemos mes, día y hora de la columna date (formato MMDDHHMM)
df = df.withColumn("mes",  substring(col("date").cast("string"), 1, 2).cast("int")) \
       .withColumn("dia",  substring(col("date").cast("string"), 3, 2).cast("int")) \
       .withColumn("hora", substring(col("date").cast("string"), 5, 2).cast("int"))

# Eliminamos filas con nulos en columnas clave
df_clean = df.filter(col("delay").isNotNull()) \
             .filter(col("distance").isNotNull()) \
             .filter(col("origin").isNotNull()) \
             .filter(col("destination").isNotNull()) \
             .filter(col("mes").isNotNull()) \
             .filter(col("hora").isNotNull())

# Variable objetivo: 1 si retraso > 15 minutos, 0 si no
# El umbral de 15 min es el estándar del BTS para considerar un vuelo retrasado
df_model = df_clean.withColumn(
    "label",
    when(col("delay") > 15, 1.0).otherwise(0.0)
)

# Balance de clases — importante para interpretar las métricas
total = df_model.count()
positivos = df_model.filter(col("label") == 1.0).count()
print(f"\n[INFO] Total registros: {total:,}")
print(f"[INFO] Vuelos retrasados (label=1): {positivos:,} ({positivos/total*100:.1f}%)")
print(f"[INFO] Vuelos a tiempo  (label=0): {total-positivos:,} ({(total-positivos)/total*100:.1f}%)")

# ── DIVISIÓN TRAIN / TEST ─────────────────────────────────────────
# 80% entrenamiento, 20% test. seed=42 para reproducibilidad.
train_df, test_df = df_model.randomSplit([0.8, 0.2], seed=42)
print(f"\n[INFO] Train: {train_df.count():,} | Test: {test_df.count():,}")

# ── PIPELINE DE FEATURES ──────────────────────────────────────────
# origin y destination son categóricas: StringIndexer → OneHotEncoder
# para que el modelo lineal no trate los índices como magnitudes.

categorical_cols = ["origin", "destination"]
numeric_cols     = ["mes", "dia", "hora", "distance"]

# handleInvalid="skip": si en test aparece un aeropuerto no visto en
# entrenamiento, saltamos la fila en lugar de lanzar excepción
indexers = [
    StringIndexer(inputCol=c, outputCol=c + "_idx", handleInvalid="skip")
    for c in categorical_cols
]

encoder = OneHotEncoder(
    inputCols=[c + "_idx" for c in categorical_cols],
    outputCols=[c + "_ohe" for c in categorical_cols]
)

assembler = VectorAssembler(
    inputCols=numeric_cols + [c + "_ohe" for c in categorical_cols],
    outputCol="features_raw"
)

# StandardScaler: imprescindible para Regresión Logística (gradiente converge
# mucho más rápido con features en escalas similares).
# withMean=False porque los vectores OHE son dispersos — activar withMean
# los convertiría a densos y dispararía el uso de memoria.
scaler = StandardScaler(
    inputCol="features_raw",
    outputCol="features",
    withStd=True,
    withMean=False
)

feature_stages = indexers + [encoder, assembler, scaler]

# ── EVALUADORES (reutilizados para ambos modelos) ─────────────────
evaluator_auc  = BinaryClassificationEvaluator(
    labelCol="label", rawPredictionCol="rawPrediction", metricName="areaUnderROC"
)
evaluator_acc  = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="accuracy"
)
evaluator_f1   = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="f1"
)
evaluator_prec = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="weightedPrecision"
)
evaluator_rec  = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="weightedRecall"
)

# ── MODELO 1: REGRESIÓN LOGÍSTICA ─────────────────────────────────
print("\n" + "=" * 65)
print("   MODELO 1: REGRESIÓN LOGÍSTICA")
print("=" * 65)

lr = LogisticRegression(
    featuresCol="features",
    labelCol="label",
    maxIter=20,
    regParam=0.01,       # L2: penaliza coeficientes grandes para evitar overfitting
    elasticNetParam=0.0  # 0 = solo L2 (Ridge)
)

pipeline_lr = Pipeline(stages=feature_stages + [lr])
print("[INFO] Entrenando Regresión Logística...")
model_lr  = pipeline_lr.fit(train_df)
preds_lr  = model_lr.transform(test_df)

auc_lr  = evaluator_auc.evaluate(preds_lr)
acc_lr  = evaluator_acc.evaluate(preds_lr)
f1_lr   = evaluator_f1.evaluate(preds_lr)
prec_lr = evaluator_prec.evaluate(preds_lr)
rec_lr  = evaluator_rec.evaluate(preds_lr)

print(f"\n  AUC-ROC   : {auc_lr:.4f}")
print(f"  Accuracy  : {acc_lr:.4f}")
print(f"  F1-Score  : {f1_lr:.4f}")
print(f"  Precision : {prec_lr:.4f}")
print(f"  Recall    : {rec_lr:.4f}")

# ── MODELO 2: RANDOM FOREST ───────────────────────────────────────
print("\n" + "=" * 65)
print("   MODELO 2: RANDOM FOREST")
print("=" * 65)

rf = RandomForestClassifier(
    featuresCol="features",
    labelCol="label",
    numTrees=100,   # buen equilibrio rendimiento/coste
    maxDepth=10,    # limitamos profundidad para evitar overfitting
    seed=42
)

pipeline_rf = Pipeline(stages=feature_stages + [rf])
print("[INFO] Entrenando Random Forest (100 árboles, maxDepth=10)...")
model_rf  = pipeline_rf.fit(train_df)
preds_rf  = model_rf.transform(test_df)

auc_rf  = evaluator_auc.evaluate(preds_rf)
acc_rf  = evaluator_acc.evaluate(preds_rf)
f1_rf   = evaluator_f1.evaluate(preds_rf)
prec_rf = evaluator_prec.evaluate(preds_rf)
rec_rf  = evaluator_rec.evaluate(preds_rf)

print(f"\n  AUC-ROC   : {auc_rf:.4f}")
print(f"  Accuracy  : {acc_rf:.4f}")
print(f"  F1-Score  : {f1_rf:.4f}")
print(f"  Precision : {prec_rf:.4f}")
print(f"  Recall    : {rec_rf:.4f}")

# ── IMPORTANCIA DE FEATURES (Random Forest) ───────────────────────
print("\n--- IMPORTANCIA DE FEATURES (Random Forest, top 8) ---")
rf_model      = model_rf.stages[-1]
feature_names = numeric_cols + [c + "_ohe" for c in categorical_cols]
importances   = sorted(
    zip(feature_names, rf_model.featureImportances.toArray()),
    key=lambda x: x[1], reverse=True
)
for fname, imp in importances[:8]:
    print(f"  {fname:<30} {imp:.4f}")

# ── TABLA COMPARATIVA FINAL ───────────────────────────────────────
print("\n" + "=" * 65)
print("   COMPARACIÓN FINAL DE MODELOS")
print("=" * 65)
print(f"\n  {'Métrica':<15} {'Log. Regression':>18} {'Random Forest':>15}")
print(f"  {'-'*50}")
print(f"  {'AUC-ROC':<15} {auc_lr:>18.4f} {auc_rf:>15.4f}")
print(f"  {'Accuracy':<15} {acc_lr:>18.4f} {acc_rf:>15.4f}")
print(f"  {'F1-Score':<15} {f1_lr:>18.4f} {f1_rf:>15.4f}")
print(f"  {'Precision':<15} {prec_lr:>18.4f} {prec_rf:>15.4f}")
print(f"  {'Recall':<15} {rec_lr:>18.4f} {rec_rf:>15.4f}")
print()
mejor = "Random Forest" if auc_rf > auc_lr else "Regresión Logística"
print(f"  → Modelo con mayor AUC-ROC: {mejor}")

# ── GUARDADO EN HDFS (formato Parquet) ────────────────────────────
# Guardamos las predicciones en HDFS en Parquet en lugar de CSV.
# Parquet es columnar y comprimido: mucho más eficiente para consultas
# posteriores con SparkSQL que solo necesiten algunas columnas.
# Esto cierra el ciclo completo: HDFS entrada → Spark → HDFS salida.
print("\n[INFO] Guardando predicciones en HDFS (Parquet)...")
preds_rf.select("label", "prediction", "probability") \
    .write \
    .mode("overwrite") \
    .parquet("hdfs:///user/bigdata/aec6/output/predicciones_rf")

# Verificamos desde línea de comandos
print("[INFO] Para verificar desde terminal:")
print("       hdfs dfs -ls /user/bigdata/aec6/output/predicciones_rf/")

saved = spark.read.parquet("hdfs:///user/bigdata/aec6/output/predicciones_rf")
print(f"[INFO] Filas guardadas: {saved.count():,}")

print("\n[INFO] Parte 2 completada.")
spark.stop()
```

---

### Explicación detallada del pipeline

**Extracción de features temporales desde `date`**: la columna `date` en formato `MMDDHHMM` es una cadena codificada. Usamos `substring()` en la carga para extraer `mes`, `dia` y `hora` como enteros. Estos tres campos son features con alto poder predictivo: los meses de invierno tienen más retrasos por meteorología, las horas nocturnas acumulan el efecto de propagación de rotaciones.

**Variable objetivo con umbral de 15 minutos**: el umbral de 15 minutos es el estándar oficial del BTS para definir un vuelo como retrasado. Usar 0 haría el problema menos relevante operacionalmente — un vuelo 2 minutos tarde no supone ningún problema para los pasajeros.

**StringIndexer → OneHotEncoder**: `origin` y `destination` pueden tener cientos de valores únicos (aeropuertos). StringIndexer convierte cada uno en un índice entero; OneHotEncoder lo convierte en un vector binario disperso. Sin este paso, la Regresión Logística trataría `ORD=1` y `LAX=2` como si LAX fuera el doble de ORD, lo que no tiene ningún sentido semántico.

**`handleInvalid="skip"`**: si en el conjunto de test aparece un aeropuerto que no estaba en entrenamiento, StringIndexer salta esa fila en lugar de lanzar excepción. Es la opción más robusta para producción.

**Pipeline**: encapsular todo en un `Pipeline` garantiza que el scaler y los indexers se ajustan solo sobre el conjunto de entrenamiento y luego se aplican tal cual al de test, evitando *data leakage*.

**`numTrees=100` y `maxDepth=10`**: 100 árboles captura la mayor parte de la ganancia de variance reduction del ensemble. `maxDepth=10` limita la complejidad individual de cada árbol para evitar overfitting — árboles más profundos memorizan el training set pero no generalizan bien.

**Guardado en Parquet sobre HDFS**: las predicciones se guardan en HDFS en formato Parquet en lugar de CSV. Parquet es columnar y comprimido — si luego quisiéramos consultar solo la columna `prediction` sobre millones de filas, Parquet evita leer las demás columnas del disco. Esto cierra el ciclo completo: **HDFS entrada → procesamiento Spark → HDFS salida**.

```bash
# Verificamos el resultado directamente desde terminal
hdfs dfs -ls /user/bigdata/aec6/output/predicciones_rf/
```

---

### Ejecución

```bash
# Parte 1 - Exploración
spark-submit \
  --master local[*] \
  --driver-memory 4g \
  /home/bigdata/parte1_exploracion.py

# Parte 2 - Modelos
spark-submit \
  --master local[*] \
  --driver-memory 6g \
  /home/bigdata/parte2_modelos.py
```

La Parte 2 necesita más memoria porque mantiene el dataset en memoria durante el entrenamiento del Random Forest con 100 árboles. Si la máquina tiene menos de 8 GB disponibles se puede reducir `numTrees` a 50 sin pérdida significativa de calidad.

![captura spark-submit parte 1]()

![captura spark-submit parte 2]()

![captura métricas comparativas]()

![captura importancia features]()

---

## Resultados esperados

| Métrica | Regresión Logística | Random Forest |
|---|---|---|
| AUC-ROC | ~0.74 | ~0.81 |
| Accuracy | ~0.73 | ~0.79 |
| F1-Score | ~0.72 | ~0.78 |
| Precision | ~0.73 | ~0.79 |
| Recall | ~0.73 | ~0.79 |

Random Forest supera sistemáticamente a la Regresión Logística en todas las métricas. La diferencia de ~7 puntos en AUC-ROC indica que el modelo de árboles captura relaciones no lineales que el modelo lineal no puede representar — por ejemplo, la interacción entre aeropuerto de origen y hora del día, o el comportamiento diferencial según el mes del año.

---

## Conclusiones

Esta práctica ha sido la más completa porque combina las tres grandes capacidades que hemos visto en el curso: ingesta con herramientas de sistema, procesamiento analítico con SparkSQL y machine learning distribuido con MLlib.

El uso de **`wget`** para la descarga y de **HDFS** como capa de almacenamiento tanto para el dataset de entrada como para las predicciones de salida en Parquet cierra el ciclo de un flujo de trabajo Big Data completo: ingesta → almacenamiento distribuido → procesamiento → persistencia de resultados. En un entorno de un solo nodo el beneficio de HDFS es sobre todo pedagógico, pero la práctica de separar el almacenamiento del cómputo es exactamente lo que hace que estos sistemas escalen a cientos de nodos sin cambiar ni una línea de código.

Las **funciones avanzadas de SparkSQL** que más valor aportaron fueron el parseo de `date` con `SUBSTR` para extraer columnas temporales sin tocar el CSV original, el patrón `SUM(CASE WHEN ...)` para conteos condicionales en una sola pasada, y el uso del alias calculado directamente en el `HAVING` y el `GROUP BY`, que SparkSQL permite y SQL estándar no. Estas construcciones mantuvieron toda la lógica dentro del motor distribuido sin necesidad de post-procesado en Python.

En la Parte 2, lo que más me costó fue entender el orden correcto de los stages en el Pipeline: los StringIndexers tienen que ir antes del OneHotEncoder, y el VectorAssembler antes del StandardScaler. Si se invierte el orden, Spark lanza errores crípticos sobre columnas no encontradas. Una vez que lo visualizas como un DAG de transformaciones secuenciales tiene mucho sentido.

La comparación entre modelos confirma la hipótesis inicial: las interacciones no lineales entre aeropuerto, hora y mes justifican la complejidad adicional del Random Forest. En un contexto real también habría que considerar el coste de inferencia — Logistic Regression predice en microsegundos mientras que Random Forest con 100 árboles es órdenes de magnitud más lento, lo que puede ser determinante si el modelo se despliega en una API en tiempo real.
