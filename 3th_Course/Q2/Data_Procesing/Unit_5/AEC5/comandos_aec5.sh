#!/bin/bash
# =============================================================
#  AEC5 - COMANDOS PARA EJECUTAR Y HACER CAPTURAS
#  Ejecuta cada bloque por separado, no todo de golpe.
#  Antes de cada comando se indica qué captura hacer.
# =============================================================

# ─────────────────────────────────────────────
#  REQUISITO PREVIO: Levantar Confluent/Kafka
# ─────────────────────────────────────────────
# Si usas Confluent local:
confluent local services start

# Si usas kafka directamente:
# zookeeper-server-start $KAFKA_HOME/config/zookeeper.properties &
# kafka-server-start $KAFKA_HOME/config/server.properties &


# ════════════════════════════════════════════
#  EJERCICIO 1 - KAFKA
# ════════════════════════════════════════════

# ── PASO 1: Crear tópico ventas ──────────────────────────────
# CAPTURA: resultado del comando (debería decir "Created topic ventas.")
kafka-topics --create \
  --bootstrap-server localhost:9092 \
  --topic ventas \
  --partitions 4 \
  --replication-factor 1

# ── PASO 2: Listar tópicos ───────────────────────────────────
# CAPTURA: listado completo de tópicos, verificar que "ventas" aparece
kafka-topics --list \
  --bootstrap-server localhost:9092

# ── PASO 3: Describir tópico ventas ─────────────────────────
# CAPTURA: salida completa con particiones, líderes e ISR
kafka-topics --describe \
  --bootstrap-server localhost:9092 \
  --topic ventas

# ── PASO 4: Crear el fichero ventas.json ────────────────────
# CAPTURA: captura del editor con el contenido del fichero
gedit /home/bigdata/confluent-7.5.1/console-consumer-primitive-keys-values/ventas.json
# Pega este contenido y guarda:
# {
#   "type": "record",
#   "name": "Venta",
#   "namespace": "com.empresa.ventas",
#   "fields": [
#     {"name": "id_venta",  "type": "long"},
#     {"name": "producto",  "type": "string"},
#     {"name": "cantidad",  "type": "int"},
#     {"name": "precio",    "type": "double"},
#     {"name": "tienda",    "type": "string"}
#   ]
# }

# También puedes crearlo directamente con cat:
cat > /home/bigdata/confluent-7.5.1/console-consumer-primitive-keys-values/ventas.json << 'EOF'
{
  "type": "record",
  "name": "Venta",
  "namespace": "com.empresa.ventas",
  "fields": [
    {"name": "id_venta",  "type": "long"},
    {"name": "producto",  "type": "string"},
    {"name": "cantidad",  "type": "int"},
    {"name": "precio",    "type": "double"},
    {"name": "tienda",    "type": "string"}
  ]
}
EOF

# Verificar que se creó bien:
cat /home/bigdata/confluent-7.5.1/console-consumer-primitive-keys-values/ventas.json

# ── PASO 5: Consumidor con clave y valor (grupo_ventas) ──────
# CAPTURA: terminal con el consumidor esperando mensajes (o leyendo si hay)
# Ejecutar en una terminal APARTE y dejarla abierta
kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic ventas \
  --group grupo_ventas \
  --property print.key=true \
  --property key.separator=: \
  --from-beginning

# ── PASO 6: Consumidor partición 2, offset 0 ────────────────
# CAPTURA: terminal con mensajes de la partición 2 (puede estar vacía al principio)
# Ejecutar en otra terminal APARTE
kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic ventas \
  --partition 2 \
  --offset earliest

# ── PASO 7: Crear fichero de datos y producir 12 mensajes ────
# Crear el fichero de datos:
cat > /home/bigdata/confluent-7.5.1/ventas_datos.txt << 'EOF'
1:{"id_venta":1,"producto":"Laptop","cantidad":2,"precio":999.99,"tienda":"Madrid"}
2:{"id_venta":2,"producto":"Monitor","cantidad":1,"precio":349.50,"tienda":"Barcelona"}
3:{"id_venta":3,"producto":"Teclado","cantidad":3,"precio":79.99,"tienda":"Valencia"}
4:{"id_venta":4,"producto":"Raton","cantidad":5,"precio":49.99,"tienda":"Sevilla"}
5:{"id_venta":5,"producto":"Auriculares","cantidad":2,"precio":199.00,"tienda":"Madrid"}
6:{"id_venta":6,"producto":"Webcam","cantidad":1,"precio":89.99,"tienda":"Bilbao"}
7:{"id_venta":7,"producto":"SSD","cantidad":4,"precio":129.99,"tienda":"Barcelona"}
8:{"id_venta":8,"producto":"RAM","cantidad":2,"precio":59.99,"tienda":"Madrid"}
9:{"id_venta":9,"producto":"Laptop","cantidad":1,"precio":1299.00,"tienda":"Valencia"}
10:{"id_venta":10,"producto":"Monitor","cantidad":3,"precio":299.99,"tienda":"Sevilla"}
11:{"id_venta":11,"producto":"Tablet","cantidad":2,"precio":449.99,"tienda":"Madrid"}
12:{"id_venta":12,"producto":"Smartphone","cantidad":1,"precio":699.99,"tienda":"Barcelona"}
EOF

# CAPTURA: que los mensajes se producen correctamente (el consumidor del paso 5
#          debería mostrarlos con clave:valor)
kafka-console-producer \
  --bootstrap-server localhost:9092 \
  --topic ventas \
  --property parse.key=true \
  --property key.separator=: \
  < /home/bigdata/confluent-7.5.1/ventas_datos.txt

# ── PASO 8: Generar 25 mensajes con datagen ──────────────────
# Opción A - si tienes kafka-producer-perf-test:
# CAPTURA: salida del perf-test con estadísticas de envío
kafka-producer-perf-test \
  --topic ventas \
  --num-records 25 \
  --throughput 5 \
  --record-size 100 \
  --producer-props bootstrap.servers=localhost:9092

# Opción B - si tienes el conector datagen de Confluent, crear config:
cat > /home/bigdata/confluent-7.5.1/datagen-ventas.json << 'EOF'
{
  "name": "datagen-ventas",
  "config": {
    "connector.class": "io.confluent.kafka.connect.datagen.DatagenConnector",
    "kafka.topic": "ventas",
    "schema.filename": "/home/bigdata/confluent-7.5.1/console-consumer-primitive-keys-values/ventas.json",
    "schema.keyfield": "id_venta",
    "max.interval": 200,
    "iterations": 25
  }
}
EOF

confluent local services connect connector load datagen-ventas \
  --config /home/bigdata/confluent-7.5.1/datagen-ventas.json

# ── PASO 9: Describir consumer group grupo_ventas ────────────
# CAPTURA: tabla completa con CURRENT-OFFSET, LOG-END-OFFSET y LAG por partición
kafka-consumer-groups \
  --bootstrap-server localhost:9092 \
  --describe \
  --group grupo_ventas

# ── PASO 10: Offsets por partición ───────────────────────────
# CAPTURA: offsets de cada partición (número de mensajes producidos en cada una)
kafka-get-offsets \
  --bootstrap-server localhost:9092 \
  --topic ventas

# También puedes verlo con:
kafka-run-class kafka.tools.GetOffsetShell \
  --broker-list localhost:9092 \
  --topic ventas \
  --time -1


# ════════════════════════════════════════════
#  EJERCICIO 2 - SPARK STREAMING
# ════════════════════════════════════════════

# ── Crear directorio para el stream ─────────────────────────
mkdir -p /tmp/temperatura_stream

# ── Crear el script generador ────────────────────────────────
cat > /home/bigdata/generar_temperatura.py << 'PYEOF'
import time
import random
import os

OUTPUT_DIR = "/tmp/temperatura_stream"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sensores = ["sensor_01", "sensor_02", "sensor_03", "sensor_04", "sensor_05"]

batch = 0
while True:
    batch += 1
    filename = f"{OUTPUT_DIR}/batch_{batch:04d}.txt"
    
    lecturas = []
    for _ in range(random.randint(5, 10)):
        sensor = random.choice(sensores)
        temp = round(random.gauss(30, 8), 2)
        lecturas.append(f"{sensor},{temp}")
    
    with open(filename, "w") as f:
        f.write("\n".join(lecturas) + "\n")
    
    print(f"[generador] Batch {batch} escrito con {len(lecturas)} lecturas en {filename}")
    time.sleep(2)
PYEOF

# ── Crear el script de Spark Streaming ──────────────────────
cat > /home/bigdata/streaming_temperatura.py << 'PYEOF'
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
PYEOF

# ── EJECUCIÓN: Terminal 1 - Generador de datos ───────────────
# CAPTURA: generador corriendo, mostrando los batches que va escribiendo
python3 /home/bigdata/generar_temperatura.py

# ── EJECUCIÓN: Terminal 2 - Spark Streaming ──────────────────
# CAPTURA 1: primera salida de las medias por sensor (tras ~30 segundos)
# CAPTURA 2: alguna alerta de temperatura alta
# CAPTURA 3: tabla de actividad por sensor (tras ~60 segundos)
spark-submit \
  --master local[*] \
  /home/bigdata/streaming_temperatura.py

# ── LIMPIEZA (opcional, al terminar) ────────────────────────
# rm -rf /tmp/temperatura_stream
