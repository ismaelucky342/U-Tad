# AEC5 - Kafka y Spark Streaming

![imagen portada]()

## Introducción

En esta actividad práctica de la unidad 5 trabajamos con dos tecnologías clave del ecosistema Big Data: **Apache Kafka** para mensajería distribuida y **Apache Spark Streaming** para procesamiento de datos en tiempo real.

La práctica se divide en dos ejercicios bien diferenciados. En el primero trabajo con Kafka: creo tópicos, defino esquemas Avro, lanzo productores y consumidores, y analizo el estado de los consumer groups. En el segundo elijo implementar **Variante 2: Monitorización de temperatura**, donde simulo un stream de sensores, calculo medias por ventana de tiempo y lanzo alertas cuando se superan umbrales definidos.

---

## EJERCICIO 1: Apache Kafka

### 1. Crear el tópico `ventas` con 4 particiones y replicación 1

Lo primero es crear el tópico sobre el que vamos a trabajar. Usamos `kafka-topics` con los flags `--create`, `--partitions 4` y `--replication-factor 1`:

```bash
kafka-topics --create \
  --bootstrap-server localhost:9092 \
  --topic ventas \
  --partitions 4 \
  --replication-factor 1
```

`--bootstrap-server` indica a qué broker conectarnos. Las 4 particiones nos permiten paralelizar la lectura/escritura. La replicación 1 significa que no hay réplicas (suficiente para entorno local de desarrollo).

![captura creación tópico]()

---

### 2. Listar los tópicos existentes

Una vez creado, verificamos que aparece en el listado junto con los tópicos que ya existieran en el broker:

```bash
kafka-topics --list \
  --bootstrap-server localhost:9092
```

Este comando nos devuelve todos los tópicos registrados en el broker. Es útil para confirmar que el tópico se ha creado correctamente antes de seguir.

![captura listado tópicos]()

---

### 3. Describir el tópico `ventas`

Con `--describe` obtenemos información detallada del tópico: número de particiones, factor de replicación, qué broker es el líder de cada partición, etc.:

```bash
kafka-topics --describe \
  --bootstrap-server localhost:9092 \
  --topic ventas
```

La salida nos muestra una línea resumen del tópico y luego una línea por cada partición indicando su líder, réplicas y réplicas sincronizadas (ISR). Con replicación 1 todas las particiones tendrán el mismo broker como líder y sin réplicas adicionales.

![captura describe tópico]()

---

### 4. Definir el esquema Avro para `ventas.json`

Avro es un sistema de serialización de datos que requiere definir un esquema antes de producir mensajes. Tomamos como referencia el fichero `primitives.json` del directorio de ejemplos de Confluent y creamos nuestro propio esquema.

Abrimos el editor para crear el fichero:

```bash
gedit /home/bigdata/confluent-7.5.1/console-consumer-primitive-keys-values/ventas.json
```

El contenido del fichero `ventas.json` queda así:

```json
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
```

El `"type": "record"` indica que es un registro estructurado (equivalente a una fila). Cada campo tiene un nombre y un tipo Avro: `long` para IDs, `string` para textos, `int` para enteros, `double` para decimales. Este esquema es lo que después usaríamos con el Schema Registry de Confluent para validar que todos los mensajes producidos respetan esta estructura.

![captura fichero ventas.json]()

---

### 5. Lanzar consumidor sobre `ventas` mostrando clave y valor

Lanzamos un consumidor que pertenezca al grupo `grupo_ventas`, visualizando tanto la clave como el valor de cada mensaje y usando `:` como separador:

```bash
kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic ventas \
  --group grupo_ventas \
  --property print.key=true \
  --property key.separator=: \
  --from-beginning
```

`--property print.key=true` activa la impresión de la clave junto al valor. `key.separator=:` define el carácter que separa ambos en la salida. `--from-beginning` hace que lea desde el offset 0 en lugar de esperar solo mensajes nuevos. El `--group` asocia este consumidor al consumer group que luego analizaremos.

![captura consumidor con clave y valor]()

---

### 6. Consumidor restringido a la partición 2 desde offset 0

Este consumidor solo lee mensajes de la partición 2, empezando desde el principio:

```bash
kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic ventas \
  --partition 2 \
  --offset earliest
```

`--partition 2` restringe la lectura a esa partición concreta. `--offset earliest` equivale a offset 0, es decir, lee todos los mensajes almacenados en esa partición desde el inicio. Esto es útil para inspeccionar qué mensajes han caído en una partición específica, ya que Kafka distribuye los mensajes entre particiones según la clave del mensaje.

> **Nota:** Al especificar `--partition` directamente, este consumidor **no pertenece a ningún consumer group**, ya que la gestión de offsets por grupo no es compatible con asignación manual de partición.

![captura consumidor partición 2]()

---

### 7. Insertar 12 mensajes desde fichero usando `id_venta` como clave

Primero creamos el fichero de datos. Cada línea tiene el formato `clave:valor`:

```bash
gedit /home/bigdata/confluent-7.5.1/ventas_datos.txt
```

Contenido del fichero `ventas_datos.txt`:

```
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
```

Ahora lanzamos el productor apuntando a ese fichero:

```bash
kafka-console-producer \
  --bootstrap-server localhost:9092 \
  --topic ventas \
  --property parse.key=true \
  --property key.separator=: \
  < /home/bigdata/confluent-7.5.1/ventas_datos.txt
```

`parse.key=true` le indica al productor que cada línea viene con clave. `key.separator=:` define el separador que usamos para dividir clave y valor. La redirección `<` hace que el productor lea del fichero en lugar de esperar input de teclado. Cada `id_venta` se usa como clave, lo que determina en qué partición acaba cada mensaje (Kafka hace hash de la clave para asignar partición).

![captura producción desde fichero]()

---

### 8. Generar 25 mensajes aleatorios con `datagen`

La herramienta `datagen` de Confluent permite generar datos aleatorios respetando un esquema Avro. Lo lanzamos como productor apuntando al esquema que definimos antes:

```bash
kafka-producer-perf-test \
  --topic ventas \
  --num-records 25 \
  --throughput 5 \
  --producer-props bootstrap.servers=localhost:9092 \
  --payload-file /home/bigdata/confluent-7.5.1/console-consumer-primitive-keys-values/ventas.json
```

O si tenemos disponible el conector datagen de Confluent:

```bash
confluent local services connect connector load datagen-ventas \
  --config /home/bigdata/confluent-7.5.1/datagen-ventas.json
```

Con el fichero de configuración `datagen-ventas.json`:

```json
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
```

Esto genera 25 registros con valores aleatorios para cada campo del esquema, usando `id_venta` como clave. Es la forma más cómoda de poblar un tópico con datos de prueba realistas sin tener que escribirlos a mano.

![captura datagen]()

---

### 9. Describir el consumer group `grupo_ventas`

Una vez que el consumidor del paso 5 ha procesado mensajes, podemos analizar el estado del grupo:

```bash
kafka-consumer-groups \
  --bootstrap-server localhost:9092 \
  --describe \
  --group grupo_ventas
```

La salida muestra una tabla con columnas `TOPIC`, `PARTITION`, `CURRENT-OFFSET`, `LOG-END-OFFSET`, `LAG`, `CONSUMER-ID`, `HOST`, `CLIENT-ID`. Lo más importante es el campo `LAG`, que indica cuántos mensajes hay pendientes de consumir en cada partición. Si el consumidor del paso 5 se lanzó con `--from-beginning` y procesó todos los mensajes, el lag debería ser 0.

![captura describe consumer group]()

---

### 10. Mensajes producidos por partición y mensajes pendientes

Para ver cuántos mensajes hay en cada partición usamos `kafka-get-offsets` o bien leemos el `LOG-END-OFFSET` del describe anterior:

```bash
kafka-get-offsets \
  --bootstrap-server localhost:9092 \
  --topic ventas
```

Este comando nos devuelve el offset del último mensaje en cada partición. Como hemos producido 12 mensajes desde fichero + 25 con datagen = **37 mensajes en total**, estos se distribuirán entre las 4 particiones según el hash del campo `id_venta` usado como clave. La distribución no tiene por qué ser exactamente uniforme.

Respecto al `LAG`: si el consumidor del paso 5 lleva tiempo activo y procesó todos los mensajes antes de llegar los del datagen, habrá mensajes pendientes en las particiones donde datagen haya producido mensajes nuevos que el consumidor no haya consumido todavía. Esto se refleja en un `LAG > 0`.

![captura offsets por partición]()

---

## EJERCICIO 2: Spark Streaming — Monitorización de Temperatura (Variante 2)

Para este ejercicio he elegido la **Variante 2** porque creo que es la más cercana a un caso de uso real: en entornos industriales y de IoT es muy habitual tener sensores enviando lecturas constantemente y necesitar detectar anomalías en tiempo real.

### Descripción del caso práctico

El escenario es el siguiente: tenemos un conjunto de sensores de temperatura distribuidos en diferentes zonas. Cada registro tiene un `sensor_id` y una `temperatura`. El sistema debe:

1. Calcular la **temperatura media por sensor** en ventanas de 1 minuto
2. Detectar lecturas que **superen un umbral** (en este caso 40°C) y mostrar alertas
3. Como análisis adicional propio, identificar el **sensor más activo** (el que más mensajes envía) y calcular la **desviación estándar** de temperaturas por sensor para detectar sensores con lecturas inestables

### Generación de datos de prueba

Hay dos formas de alimentar el stream: desde consola o desde fichero. Yo voy a usar un **script Python que genera datos aleatorios** y los escribe en un directorio que Spark monitoriza. Esto es más cómodo porque no hay que ir escribiendo a mano.

El script generador (`generar_temperatura.py`):

```python
import time
import random
import os

# Directorio donde Spark leerá los ficheros
OUTPUT_DIR = "/tmp/temperatura_stream"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sensores = ["sensor_01", "sensor_02", "sensor_03", "sensor_04", "sensor_05"]

batch = 0
while True:
    batch += 1
    filename = f"{OUTPUT_DIR}/batch_{batch:04d}.txt"
    
    # Generamos entre 5 y 10 lecturas por batch
    lecturas = []
    for _ in range(random.randint(5, 10)):
        sensor = random.choice(sensores)
        # La mayoría de lecturas normales, pero ocasionalmente alguna alta
        temp = round(random.gauss(30, 8), 2)
        lecturas.append(f"{sensor},{temp}")
    
    with open(filename, "w") as f:
        f.write("\n".join(lecturas) + "\n")
    
    print(f"[generador] Batch {batch} escrito con {len(lecturas)} lecturas")
    time.sleep(2)  # Un fichero nuevo cada 2 segundos
```

Este script simula sensores con temperaturas con distribución gaussiana centrada en 30°C y desviación de 8°C, lo que hace que de vez en cuando aparezcan lecturas por encima de 40°C de forma natural.

### Código principal de Spark Streaming (`streaming_temperatura.py`)

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, avg, stddev, count, max as spark_max,
    window, split, explode, lit, current_timestamp
)
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Creamos la sesión de Spark. La configuración de checkpointLocation
# es obligatoria para el streaming con estado (windowed aggregations)
spark = SparkSession.builder \
    .appName("MonitorizacionTemperatura") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

# Silenciamos logs INFO para que la salida sea más legible
spark.sparkContext.setLogLevel("WARN")

print("="*60)
print("   SISTEMA DE MONITORIZACIÓN DE TEMPERATURA")
print("   Umbral de alerta: 40°C")
print("="*60)

# Directorio donde el generador va escribiendo los ficheros
INPUT_DIR = "/tmp/temperatura_stream"
UMBRAL = 40.0

# Definimos el esquema explícitamente para que Spark no tenga
# que inferirlo en cada micro-batch (más eficiente)
schema = StructType([
    StructField("sensor_id", StringType(), True),
    StructField("temperatura", DoubleType(), True)
])

# ── STREAM DE ENTRADA ──────────────────────────────────────────
# readStream con formato csv monitoriza el directorio continuamente.
# Cada vez que aparece un fichero nuevo, lo incorpora al stream.
raw_stream = spark.readStream \
    .format("csv") \
    .schema(schema) \
    .option("header", False) \
    .load(INPUT_DIR)

# Añadimos timestamp de procesamiento para las ventanas de tiempo
stream_con_tiempo = raw_stream.withColumn("event_time", current_timestamp())


# ── QUERY 1: MEDIA POR SENSOR EN VENTANA DE 1 MINUTO ──────────
# groupBy con window() crea ventanas deslizantes.
# watermark(1 minuto) le dice a Spark cuánto tiempo esperar
# datos tardíos antes de cerrar la ventana.
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


# ── QUERY 2: ALERTAS POR TEMPERATURA ALTA ─────────────────────
# Filtramos directamente sobre el stream sin agrupar.
# Modo append porque cada alerta es un evento nuevo, no una actualización.
alertas = stream_con_tiempo \
    .filter(col("temperatura") > UMBRAL) \
    .select(
        col("sensor_id"),
        col("temperatura"),
        col("event_time").alias("timestamp_alerta"),
        lit(f"⚠️ ALERTA: temperatura supera {UMBRAL}°C").alias("mensaje")
    )

query_alertas = alertas.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .trigger(processingTime="10 seconds") \
    .start()


# ── QUERY 3 (ANÁLISIS PROPIO): SENSOR MÁS ACTIVO ──────────────
# Contamos cuántos mensajes ha enviado cada sensor en total.
# Esto nos permite identificar si algún sensor está enviando
# datos con una frecuencia anormalmente alta (posible fallo).
actividad_sensores = stream_con_tiempo \
    .groupBy("sensor_id") \
    .agg(
        count("*").alias("total_lecturas"),
        avg("temperatura").alias("media_global")
    ) \
    .orderBy(col("total_lecturas").desc())

query_actividad = actividad_sensores.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .trigger(processingTime="60 seconds") \
    .start()


print("\n[INFO] Tres queries de streaming activas. Esperando datos en", INPUT_DIR)
print("[INFO] Ctrl+C para detener\n")

# awaitAnyTermination() mantiene el programa vivo hasta que
# alguna de las queries se detenga (o Ctrl+C)
spark.streams.awaitAnyTermination()
```

### Explicación detallada del código

**Sesión Spark y configuración**: `local[*]` usa todos los cores disponibles. `shuffle.partitions=4` reduce el número de particiones de shuffle (por defecto 200) para que la salida no sea excesivamente fragmentada en local.

**Schema explícito**: aunque Spark puede inferir el esquema, hacerlo en cada micro-batch tiene coste. Definirlo explícitamente con `StructType` es la práctica recomendada para streaming.

**readStream con CSV y directorio**: Spark monitoriza `INPUT_DIR` y cada vez que detecta un fichero nuevo lo procesa como un micro-batch. Es la forma más sencilla de simular un stream sin necesidad de Kafka.

**Watermark**: le indicamos a Spark que espere hasta 1 minuto datos tardíos antes de cerrar una ventana. Sin watermark, Spark tendría que mantener el estado de todas las ventanas indefinidamente.

**window()**: agrupa eventos en ventanas temporales de 1 minuto. Esto es lo que nos permite calcular medias "por minuto" en lugar de sobre todo el histórico.

**Tres outputModes distintos**:
- `update`: para agregaciones con ventana, solo emite las filas que han cambiado
- `append`: para filtros sin agregación, cada fila nueva se emite una vez
- `complete`: para agregaciones sin ventana, emite el estado completo en cada trigger

**Análisis adicional propio**: la Query 3 añade algo no pedido en el enunciado — rastrear la actividad por sensor permite detectar comportamientos anómalos como un sensor que emite datos 10 veces más rápido de lo normal (posible bucle de error en el firmware).

### Ejecución

Abrimos dos terminales. En la primera lanzamos el generador:

```bash
python3 /home/bigdata/generar_temperatura.py
```

En la segunda lanzamos el job de Spark:

```bash
spark-submit \
  --master local[*] \
  /home/bigdata/streaming_temperatura.py
```

![captura generador corriendo]()

![captura salida query medias]()

![captura salida alertas temperatura alta]()

![captura salida actividad sensores]()

---

## Conclusiones

Esta práctica ha sido bastante densa pero muy completa. En Kafka lo que más me costó fue entender bien la diferencia entre asignar una partición manualmente (paso 6) y pertenecer a un consumer group: cuando especificas `--partition` directamente, Kafka no gestiona el offset automáticamente y el consumidor queda fuera del grupo. Esto me generó confusión al principio porque esperaba ver ese consumidor en el describe del grupo_ventas y no aparecía.

La parte del esquema Avro la entiendo conceptualmente pero sin el Schema Registry levantado no llegué a validar los mensajes contra él. En un entorno real el Schema Registry es imprescindible para garantizar compatibilidad hacia atrás cuando el esquema evoluciona.

En Spark Streaming lo más complejo fue gestionar los `outputMode`: la combinación de `update` con ventanas y `append` con filtros no es obvia al principio. También tuve que ajustar el watermark porque inicialmente ponía valores muy bajos y las ventanas se cerraban antes de recibir todos los datos del micro-batch.

En general, la experiencia de ver las alertas aparecer en tiempo real según el generador producía temperaturas altas es bastante satisfactoria — es el tipo de caso de uso que entiendes por qué tiene sentido en producción.
