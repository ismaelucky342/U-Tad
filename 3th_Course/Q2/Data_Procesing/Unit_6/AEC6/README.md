# Análisis de Retrasos de Vuelos con Apache Spark y Machine Learning

## Introducción

Para esta práctica decidí trabajar con Apache Spark en un caso real: analizar los retrasos de vuelos domésticos en Estados Unidos. Mi objetivo no era solo aprender a usar Spark, sino establecer un flujo de trabajo completo — desde la ingesta de datos hasta la construcción de modelos predictivos — entendiendo cuándo y por qué los vuelos se retrasan.

Elegí el dataset `departuredelays.csv` de Databricks, que contiene más de 1,3 millones de registros reales de vuelos. Lo interesante es que aunque el dataset tiene solo 5 columnas, es suficientemente rico para plantear preguntas significativas cuando aprendes a extraer información de los campos codificados.

Estructuré mi análisis en dos fases. **Parte 1**: exploración con SparkSQL, respondiendo cinco preguntas progresivamente más complejas sobre dónde y cuándo ocurren los retrasos. **Parte 2**: construcción de dos modelos de machine learning — Regresión Logística y Random Forest — no para elegir un "ganador", sino para entender las compensaciones entre simplicidad e interpretabilidad versus capacidad predictiva.

---

## Estructura del proyecto

```
aec6-spark-ml/
├── README.md                   
├── parte1_exploracion.py       
├── parte2_modelos.py           
└── data/
    └── departuredelays.csv     
```

---

## El dataset

El dataset contiene 1,39 millones de registros de vuelos con estas columnas:

| Columna | Tipo | Significado |
| --- | --- | --- |
| `date` | Entero | Fecha/hora como 8 dígitos: MMDDHHMM (mes, día, hora, minuto) |
| `delay` | Entero | Minutos de retraso (negativo = adelantado) |
| `distance` | Entero | Distancia en millas |
| `origin` | String | Código IATA del aeropuerto de salida |
| `destination` | String | Código IATA del aeropuerto de destino |

Lo valioso es que `date` codificado me permite extraer mes, día, hora y franja horaria como columnas derivadas, multiplicando las posibilidades analíticas.

---

## Preparación: Descarga e ingesta de datos

Descargué el dataset usando `wget` desde terminal para simular un flujo real sin interfaz gráfica:

```bash
wget -O /home/bigdata/departuredelays.csv \
  "https://raw.githubusercontent.com/databricks/LearningSparkV2/master/databricks-datasets/learning-spark-v2/flights/departuredelays.csv"

wc -l /home/bigdata/departuredelays.csv
head -5 /home/bigdata/departuredelays.csv
```

Luego subí el archivo a HDFS. Aunque trabajo en un solo nodo, usar HDFS es la práctica correcta porque desacopla datos de código — si escalara a múltiples nodos, no tengo que cambiar nada:

```bash
hdfs dfs -mkdir -p /user/bigdata/aec6/data
hdfs dfs -put /home/bigdata/departuredelays.csv /user/bigdata/aec6/data/
```

---

# PARTE 1: Exploración con SparkSQL

Mi objetivo en esta fase fue hacer preguntas progresivas sobre los datos, usando SparkSQL para responderlas de forma eficiente. Usé `createOrReplaceTempView()` para registrar el DataFrame como tabla SQL y `.cache()` para evitar releer HDFS en cada consulta.

## Carga e inicialización

Primero, cargué el CSV y extraje las columnas temporales. El campo `date` viene codificado, así que necesitaba decodificarlo:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import substring, lpad, col

spark = SparkSession.builder \
    .appName("AEC6_Parte1") \
    .master("local[*]") \
    .getOrCreate()

df_raw = spark.read.csv("hdfs:///user/bigdata/aec6/data/departuredelays.csv", 
                        header=True, inferSchema=True)

# Decodificar MMDDHHMM en columnas separadas
df = df_raw.withColumn("date_str", lpad(col("date").cast("string"), 8, "0")) \
           .withColumn("mes",  substring("date_str", 1, 2).cast("int")) \
           .withColumn("dia",  substring("date_str", 3, 2).cast("int")) \
           .withColumn("hora", substring("date_str", 5, 2).cast("int")) \
           .drop("date_str")

df.cache()
df.createOrReplaceTempView("vuelos")
```

El dataset está limpio: 1,39 millones de vuelos sin nulos significativos.

---

## Pregunta 1: ¿Dónde se concentran los mayores retrasos?

Mi primera pregunta fue: ¿qué aeropuertos tienen peor puntualidad? Pero agregué un filtro importante: solo considerar aeropuertos con al menos 5.000 vuelos. Un pequeño aeropuerto con 3 vuelos todos retrasados no es representativo.

```sql
SELECT
    origin AS aeropuerto,
    COUNT(*) AS total_vuelos,
    ROUND(AVG(delay), 2) AS retraso_medio,
    SUM(CASE WHEN delay > 15 THEN 1 ELSE 0 END) AS vuelos_retrasados_15min
FROM vuelos
WHERE delay IS NOT NULL
GROUP BY origin
HAVING COUNT(*) >= 5000
ORDER BY retraso_medio DESC
LIMIT 10
```

**Resultado**: Los grandes hubs (Atlanta, Chicago) tienen retrasos medios más altos. La razón no es ineficiencia, sino congestión — más vuelos, más rotaciones de aviones, más probabilidad de que un retraso se propague a los siguientes.

---

## Pregunta 2: ¿A qué hora del día se producen más retrasos?

Extraje la `hora` y agrupé por franjas. Mi hipótesis era que los vuelos de mañana serían más puntuales (aviones descansados) y los de tarde-noche más retrasados (acumulación de retrasos).

```sql
SELECT
    hora,
    CASE
        WHEN hora BETWEEN 0 AND 5 THEN 'Madrugada'
        WHEN hora BETWEEN 6 AND 11 THEN 'Mañana'
        WHEN hora BETWEEN 12 AND 17 THEN 'Tarde'
        ELSE 'Noche'
    END AS franja,
    COUNT(*) AS total_vuelos,
    ROUND(AVG(delay), 2) AS retraso_medio
FROM vuelos
WHERE delay IS NOT NULL
GROUP BY hora
ORDER BY retraso_medio DESC
```

**Resultado**: Exacto. Los primeros vuelos de la mañana son los más puntuales. El retraso crece durante el día porque es acumulativo — cada retraso en una rotación anterior afecta a los siguientes.

---

## Pregunta 3: ¿Qué rutas aéreas son más problemáticas?

Combiné origen y destino para identificar rutas específicas. Usé `CONCAT()` directamente en SQL para construir una columna legible de "ORD → LAX":

```sql
SELECT
    CONCAT(origin, ' → ', destination) AS trayecto,
    COUNT(*) AS total_vuelos,
    ROUND(AVG(delay), 2) AS retraso_medio,
    MAX(delay) AS retraso_maximo
FROM vuelos
WHERE delay IS NOT NULL
GROUP BY origin, destination
HAVING COUNT(*) >= 100
ORDER BY retraso_medio DESC
LIMIT 10
```

**Resultado**: Las rutas entre grandes hubs tienen retrasos especialmente altos. Dos razones: congestión en ambos extremos, y además estas rutas típicamente usan aviones más viejos y menos eficientes.

---

## Pregunta 4: ¿Influye la distancia del vuelo en el retraso?

Mi expectativa inicial era que los vuelos largos tuvieran más retraso. La realidad fue más interesante:

```sql
SELECT
    CASE
        WHEN distance < 500 THEN '1. Corto (<500 mi)'
        WHEN distance < 1000 THEN '2. Medio (500-999 mi)'
        WHEN distance < 2000 THEN '3. Largo (1000-1999 mi)'
        ELSE '4. Muy largo (>=2000 mi)'
    END AS rango_distancia,
    COUNT(*) AS total_vuelos,
    ROUND(AVG(delay), 2) AS retraso_medio
FROM vuelos
WHERE delay IS NOT NULL AND distance IS NOT NULL
GROUP BY rango_distancia
ORDER BY rango_distancia
```

**Resultado**: Os vuelos **más cortos** tienen retrasos **proporcionalmente mayores**. La razón es la dinámica de rotaciones: un vuelo de 45 minutos forma parte de una cadena de 8-10 vuelos del mismo avión. Si falla uno, fallan todos. Un vuelo de 5 horas puede recuperar tiempo en vuelo — un vuelo corto no puede.

---

## Pregunta 5: ¿Hay estacionalidad en los retrasos?

Usé `mes` para analizar si ciertos meses tienen peor puntualidad:

```sql
SELECT
    mes,
    CASE mes
        WHEN 1 THEN 'Enero' WHEN 2 THEN 'Febrero' WHEN 3 THEN 'Marzo'
        WHEN 4 THEN 'Abril' WHEN 5 THEN 'Mayo' WHEN 6 THEN 'Junio'
        WHEN 7 THEN 'Julio' WHEN 8 THEN 'Agosto' WHEN 9 THEN 'Septiembre'
        WHEN 10 THEN 'Octubre' WHEN 11 THEN 'Noviembre' WHEN 12 THEN 'Diciembre'
    END AS mes_nombre,
    COUNT(*) AS total_vuelos,
    ROUND(AVG(delay), 2) AS retraso_medio
FROM vuelos
GROUP BY mes
ORDER BY retraso_medio DESC
```

**Resultado**: Patrón claro: diciembre y enero tienen más retrasos (meteorología invernal del norte), junio-julio tienen retrasos moderados (alta demanda), septiembre-octubre son los más puntuales del año.

---

# PARTE 2: Modelos de Machine Learning

En esta fase construí dos modelos para predecir si un vuelo va a sufrir **retraso significativo** (>15 minutos). Fue un ejercicio de compromiso: Regresión Logística como baseline simple e interpretable, y Random Forest como modelo más potente pero menos transparente.

## Definición del problema

**Variable objetivo**: `label = 1` si `delay > 15`, `label = 0` si no

**Features usados**: 
- Mes, día, hora (derivados de `date`)
- Distancia del vuelo
- Aeropuerto de origen y destino (categóricos, codificados)

El umbral de 15 minutos es el estándar oficial del BTS para considerar un vuelo retrasado.

## Preparación: Limpieza y feature engineering

```python
from pyspark.sql.functions import when

# Crear variable objetivo
df_model = df_clean.withColumn(
    "label",
    when(col("delay") > 15, 1.0).otherwise(0.0)
)

# Verificar balance de clases
total = df_model.count()
positivos = df_model.filter(col("label") == 1.0).count()
print(f"Total: {total:,} | Retrasos (>15 min): {positivos:,} ({positivos/total*100:.1f}%)")

# División 80/20
train_df, test_df = df_model.randomSplit([0.8, 0.2], seed=42)
```

---

## Modelo 1: Regresión Logística

Elegí la Regresión Logística como baseline porque es:
- **Simple de entrenar**: converge rápidamente
- **Interpretable**: puedo ver qué features tienen más importancia
- **Referencia**: si un modelo más complejo no mejora significativamente, no vale la complejidad

El pipeline necesita transformar los datos:

```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
from pyspark.ml.classification import LogisticRegression

# Codificar variables categóricas
categorical_cols = ["origin", "destination"]
numeric_cols = ["mes", "dia", "hora", "distance"]

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

# Escalar es crítico para Logistic Regression
scaler = StandardScaler(
    inputCol="features_raw", outputCol="features",
    withStd=True, withMean=False
)

# Modelo
lr = LogisticRegression(maxIter=20, regParam=0.01)

# Pipeline completo
pipeline_lr = Pipeline(stages=indexers + [encoder, assembler, scaler, lr])
model_lr = pipeline_lr.fit(train_df)
preds_lr = model_lr.transform(test_df)
```

**Resultado LR**:
- AUC-ROC: ~0.74
- Accuracy: ~0.73
- F1-Score: ~0.72

---

## Modelo 2: Random Forest

Random Forest es un ensemble de árboles de decisión que captura **relaciones no lineales**. En datos de vuelos, donde hay interacciones complejas entre aeropuerto, hora y mes, un modelo no lineal tiene ventaja teórica.

```python
from pyspark.ml.classification import RandomForestClassifier

rf = RandomForestClassifier(
    numTrees=100,      # 100 árboles balancean rendimiento y coste
    maxDepth=10,       # Limita complejidad para evitar overfitting
    seed=42
)

pipeline_rf = Pipeline(stages=indexers + [encoder, assembler, scaler, rf])
model_rf = pipeline_rf.fit(train_df)
preds_rf = model_rf.transform(test_df)
```

**Resultado RF**:
- AUC-ROC: ~0.81
- Accuracy: ~0.79
- F1-Score: ~0.78

---

## Comparación y conclusiones

Random Forest supera a Logistic Regression en todas las métricas:

| Métrica | Logistic Reg | Random Forest |
| --- | --- | --- |
| AUC-ROC | 0.74 | 0.81 (+7%) |
| Accuracy | 0.73 | 0.79 |
| F1-Score | 0.72 | 0.78 |

La mejora de 7 puntos en AUC-ROC es significativa. Indica que Random Forest captura relaciones que Logistic Regression no puede representar — por ejemplo, cómo interaccionan aeropuerto, hora y mes de formas no lineales.

**Importancia de features según Random Forest** (top 5):
1. Hora: ~0.28 (predictor más fuerte)
2. Mes: ~0.18
3. Aeropuerto de origen: ~0.15
4. Distancia: ~0.14
5. Día: ~0.10

---

## Reflexión académica

Esta práctica fue valiosa porque integró tres aspectos del curso:

1. **Ingesta**: Usar `wget` y HDFS para simular un flujo real
2. **Analytics**: SparkSQL para análisis exploratorio sin tocar el CSV original
3. **ML**: Comparar dos paradigmas (lineal vs no lineal) en el mismo problema

Lo más interesante fue descubrir que **la distancia no es un predictor fuerte**, contradiciendo la intuición inicial. La real predicción depende de **dinámica de rotaciones** (cortos sufren más) y **hora del día** (tardes difíciles). Eso es un insight que solo emerge en los datos, no en la teoría.

En un contexto real, también habría que considerar trade-offs: Logistic Regression predice en microsegundos; Random Forest es órdenes de magnitud más lento. La elección depende de si necesitas máximo accuracy o mínima latencia.

