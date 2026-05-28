#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC2 - PRDT                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        19/05/2026  -  21:45:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    22/05/2026  -  00:55:42           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================#

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, isnull, substring, lpad
from pyspark.sql.types import IntegerType
from pyspark.ml import Pipeline
from pyspark.ml.feature import (
    StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
)
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier
from pyspark.ml.evaluation import (
    BinaryClassificationEvaluator, MulticlassClassificationEvaluator
)

# ── SESIÓN SPARK ──────────────────────────────────────────────────────────────
spark = SparkSession.builder \
    .appName("AEC6_Parte2_Modelos") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "8") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("=" * 65)
print("   AEC6 - PARTE 2: MODELOS ML PARA PREDICCIÓN DE RETRASOS")
print("=" * 65)

# ── CARGA Y PREPARACIÓN ───────────────────────────────────────────────────────
df_raw = spark.read \
    .format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .load("hdfs:///user/bigdata/aec6/data/departuredelays.csv")

# Extraemos mes, día y hora del campo date (MMDDHHMM) para usarlos
# como features temporales. lpad garantiza 8 dígitos si el valor
# empieza por cero (meses de enero a septiembre).
df = df_raw.withColumn("date_str", lpad(col("date").cast("string"), 8, "0")) \
    .withColumn("mes",  substring("date_str", 1, 2).cast(IntegerType())) \
    .withColumn("dia",  substring("date_str", 3, 2).cast(IntegerType())) \
    .withColumn("hora", substring("date_str", 5, 2).cast(IntegerType())) \
    .drop("date", "date_str") \
    .filter(col("delay").isNotNull()) \
    .filter(col("distance").isNotNull())

# Variable objetivo: 1 si el vuelo sale con más de 15 min de retraso
# El umbral de 15 minutos es el estándar del BTS para clasificar
# un vuelo como oficialmente retrasado.
df_model = df.withColumn(
    "label",
    when(col("delay") > 15, 1.0).otherwise(0.0)
).drop("delay")

# Balance de clases — importante antes de entrenar cualquier clasificador
total      = df_model.count()
positivos  = df_model.filter(col("label") == 1.0).count()
print(f"\n[INFO] Total registros:          {total:,}")
print(f"[INFO] Vuelos retrasados (label=1): {positivos:,} ({positivos/total*100:.1f}%)")
print(f"[INFO] Vuelos a tiempo   (label=0): {total-positivos:,} ({(total-positivos)/total*100:.1f}%)")

# ── DIVISIÓN TRAIN / TEST ─────────────────────────────────────────────────────
# 80% entrenamiento, 20% test. seed=42 para reproducibilidad.
train_df, test_df = df_model.randomSplit([0.8, 0.2], seed=42)
print(f"\n[INFO] Train: {train_df.count():,} | Test: {test_df.count():,}")

# ── PIPELINE DE FEATURES ──────────────────────────────────────────────────────
# Columnas categóricas: origin y destination (códigos IATA de aeropuertos)
# Columnas numéricas: distance más las extraídas de date (mes, dia, hora)
categorical_cols = ["origin", "destination"]
numeric_cols     = ["distance", "mes", "dia", "hora"]

# StringIndexer: string → índice entero (necesario antes del OHE)
# handleInvalid="skip": si en test aparece un aeropuerto no visto en
# entrenamiento, salta la fila en lugar de lanzar excepción
indexers = [
    StringIndexer(inputCol=c, outputCol=c + "_idx", handleInvalid="skip")
    for c in categorical_cols
]

# OneHotEncoder: índice → vector binario disperso
# Evita que el modelo lineal interprete los índices como magnitudes
encoder = OneHotEncoder(
    inputCols=[c + "_idx" for c in categorical_cols],
    outputCols=[c + "_ohe" for c in categorical_cols]
)

# VectorAssembler: combina todas las features en un único vector
assembler = VectorAssembler(
    inputCols=numeric_cols + [c + "_ohe" for c in categorical_cols],
    outputCol="features_raw"
)

# StandardScaler: normaliza las features para la Regresión Logística.
# withMean=False porque los vectores OHE son dispersos — activar withMean
# los convertiría a densos y dispararía el uso de memoria.
scaler = StandardScaler(
    inputCol="features_raw",
    outputCol="features",
    withStd=True,
    withMean=False
)

feature_stages = indexers + [encoder, assembler, scaler]

# ── EVALUADORES (reutilizados para ambos modelos) ─────────────────────────────
evaluator_auc  = BinaryClassificationEvaluator(
    labelCol="label", rawPredictionCol="rawPrediction", metricName="areaUnderROC")
evaluator_acc  = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="accuracy")
evaluator_f1   = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="f1")
evaluator_prec = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="weightedPrecision")
evaluator_rec  = MulticlassClassificationEvaluator(
    labelCol="label", predictionCol="prediction", metricName="weightedRecall")

# ── MODELO 1: REGRESIÓN LOGÍSTICA ─────────────────────────────────────────────
print("\n" + "=" * 65)
print("   MODELO 1: REGRESIÓN LOGÍSTICA")
print("=" * 65)

lr = LogisticRegression(
    featuresCol="features",
    labelCol="label",
    maxIter=20,
    regParam=0.01,       # Regularización L2 para evitar overfitting
    elasticNetParam=0.0  # 0.0 = Ridge (solo L2), 1.0 = Lasso (solo L1)
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

# ── MODELO 2: RANDOM FOREST ───────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   MODELO 2: RANDOM FOREST")
print("=" * 65)

rf = RandomForestClassifier(
    featuresCol="features",
    labelCol="label",
    numTrees=100,   # 100 árboles: buen equilibrio rendimiento/coste
    maxDepth=10,    # Limitamos profundidad para evitar overfitting
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

# ── IMPORTANCIA DE FEATURES (Random Forest) ───────────────────────────────────
print("\n--- IMPORTANCIA DE FEATURES (Random Forest, top 10) ---")
rf_model      = model_rf.stages[-1]
feature_names = numeric_cols + [c + "_ohe" for c in categorical_cols]
importances   = sorted(
    zip(feature_names, rf_model.featureImportances.toArray()),
    key=lambda x: x[1], reverse=True
)
for fname, importance in importances[:10]:
    print(f"  {fname:<30} {importance:.4f}")

# ── TABLA COMPARATIVA FINAL ───────────────────────────────────────────────────
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

# ── GUARDADO DE PREDICCIONES EN HDFS ──────────────────────────────────────────
# Guardamos en Parquet sobre HDFS: formato columnar y comprimido,
# más eficiente que CSV para consultas analíticas posteriores con SparkSQL.
# Cierra el ciclo completo: HDFS entrada → Spark → HDFS salida.
print("\n[INFO] Guardando predicciones en HDFS (formato Parquet)...")
preds_rf.select("label", "prediction", "probability") \
    .write \
    .mode("overwrite") \
    .parquet("hdfs:///user/bigdata/aec6/output/predicciones_rf")

# Verificamos desde la terminal
# hdfs dfs -ls /user/bigdata/aec6/output/predicciones_rf/
saved = spark.read.parquet("hdfs:///user/bigdata/aec6/output/predicciones_rf")
print(f"[INFO] Filas guardadas en HDFS: {saved.count():,}")

print("\n[INFO] Parte 2 completada.")
spark.stop()
