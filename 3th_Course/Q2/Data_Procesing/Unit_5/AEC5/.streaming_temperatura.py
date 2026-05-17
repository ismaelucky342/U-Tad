from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, avg, stddev, count, max as spark_max,
    window, lit, current_timestamp
)
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

spark = SparkSession.builder \
    .appName("MonitorizacionTemperatura") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("="*60)
print("   SISTEMA DE MONITORIZACIÓN DE TEMPERATURA")
print("   Umbral de alerta: 40 grados")
print("="*60)

INPUT_DIR = "/tmp/temperatura_stream"
UMBRAL = 40.0

schema = StructType([
    StructField("sensor_id", StringType(), True),
    StructField("temperatura", DoubleType(), True)
])

raw_stream = spark.readStream \
    .format("csv") \
    .schema(schema) \
    .option("header", False) \
    .load(INPUT_DIR)

stream_con_tiempo = raw_stream.withColumn("event_time", current_timestamp())

# Query 1: media por sensor en ventana de 1 minuto
media_por_sensor = stream_con_tiempo \
    .withWatermark("event_time", "1 minute") \
    .groupBy(
        window(col("event_time"), "1 minute"),
        col("sensor_id")
    ) \
    .agg(
        avg("temperatura").alias("temp_media"),
        stddev("temperatura").alias("temp_desviacion"),
        count("*").alias("num_lecturas"),
        spark_max("temperatura").alias("temp_maxima")
    )

query_medias = media_por_sensor.writeStream \
    .outputMode("update") \
    .format("console") \
    .option("truncate", False) \
    .option("numRows", 20) \
    .trigger(processingTime="30 seconds") \
    .start()

# Query 2: alertas por temperatura alta
alertas = stream_con_tiempo \
    .filter(col("temperatura") > UMBRAL) \
    .select(
        col("sensor_id"),
        col("temperatura"),
        col("event_time").alias("timestamp_alerta"),
        lit(f"ALERTA: temperatura supera {UMBRAL} grados").alias("mensaje")
    )

query_alertas = alertas.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .trigger(processingTime="10 seconds") \
    .start()

# Query 3 (analisis propio): sensor mas activo y desviacion
actividad_sensores = stream_con_tiempo \
    .groupBy("sensor_id") \
    .agg(
        count("*").alias("total_lecturas"),
        avg("temperatura").alias("media_global"),
        stddev("temperatura").alias("desviacion_global")
    ) \
    .orderBy(col("total_lecturas").desc())

query_actividad = actividad_sensores.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .trigger(processingTime="60 seconds") \
    .start()

print("\n[INFO] Queries activas. Esperando datos en", INPUT_DIR)
print("[INFO] Ctrl+C para detener\n")

spark.streams.awaitAnyTermination()
