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
from pyspark.sql.functions import (
    col, count, avg, round as spark_round, sum as spark_sum,
    when, isnull, desc, abs as spark_abs,
    expr, substring, lpad, concat, lit
)
from pyspark.sql.types import IntegerType

# ── SESIÓN SPARK ──────────────────────────────────────────────────────────────
spark = SparkSession.builder \
    .appName("AEC6_Parte1_Exploracion") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "8") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("=" * 65)
print("   AEC6 - PARTE 1: EXPLORACIÓN Y ANÁLISIS DE VUELOS USA")
print("=" * 65)

# ── CARGA DESDE HDFS ──────────────────────────────────────────────────────────
# Leemos desde HDFS. La columna 'date' viene como entero MMDDHHMM:
#   - MM   → mes      (posiciones 1-2)
#   - DD   → día      (posiciones 3-4)
#   - HH   → hora     (posiciones 5-6)
#   - MM   → minuto   (posiciones 7-8)
# La tratamos como String para poder hacer substring sobre ella.
df_raw = spark.read \
    .format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .load("data/departuredelays.csv")

# Casteamos 'date' a String (inferSchema lo lee como Long) y extraemos
# mes, día y hora como columnas derivadas para enriquecer el análisis.
# Usamos lpad para garantizar que siempre tenemos 8 dígitos aunque el
# valor empiece por cero (ej: enero = mes "01").
df = df_raw.withColumn("date_str", lpad(col("date").cast("string"), 8, "0")) \
    .withColumn("mes",  substring("date_str", 1, 2).cast(IntegerType())) \
    .withColumn("dia",  substring("date_str", 3, 2).cast(IntegerType())) \
    .withColumn("hora", substring("date_str", 5, 2).cast(IntegerType())) \
    .drop("date_str")

# Cacheamos porque reutilizaremos el DataFrame en las 5 queries.
# Sin cache cada acción relanzaría la lectura completa desde HDFS.
df.cache()

print(f"\n[INFO] Dataset cargado: {df.count():,} filas, {len(df.columns)} columnas")

# ── EXPLORACIÓN BÁSICA ────────────────────────────────────────────────────────
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

# ── PREGUNTA 1 ────────────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   PREGUNTA 1")
print("   ¿Cuáles son los 10 aeropuertos origen con mayor retraso")
print("   medio de salida (mínimo 5.000 vuelos)?")
print("=" * 65)

# Filtramos vuelos con retraso > 0 para calcular solo la media de los
# que realmente se retrasaron (los negativos son adelantos y bajarían
# artificialmente el promedio, ocultando aeropuertos problemáticos).
# Usamos HAVING con alias calculado, que SparkSQL permite pero SQL estándar no.
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

# ── PREGUNTA 2 ────────────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   PREGUNTA 2")
print("   ¿A qué hora del día se producen más retrasos?")
print("   (franja horaria de salida)")
print("=" * 65)

# Agrupamos por la hora extraída del campo date (MMDDHHMM).
# Añadimos una columna de franja legible con CASE para no tener
# que postprocesar en Python — toda la lógica queda dentro de Spark.
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

# ── PREGUNTA 3 ────────────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   PREGUNTA 3")
print("   ¿Cuáles son los 10 trayectos con mayor retraso acumulado?")
print("=" * 65)

# El retraso acumulado (suma total de minutos perdidos) es una métrica
# distinta a la media: un trayecto con pocos vuelos muy retrasados puede
# tener alta media pero poco impacto total. Con SUM vemos el impacto real.
# CONCAT con el símbolo → hace la salida directamente legible.
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

# ── PREGUNTA 4 ────────────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   PREGUNTA 4")
print("   ¿La distancia del vuelo influye en el retraso?")
print("=" * 65)

# Segmentamos por tramos de distancia con CASE en el SELECT.
# El alias 'tramo' se usa directamente en GROUP BY y ORDER BY —
# SparkSQL lo resuelve en el plan lógico sin coste adicional.
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

# ── PREGUNTA 5 ────────────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print("   PREGUNTA 5")
print("   ¿Qué mes del año concentra más retrasos?")
print("=" * 65)

# Usamos la columna 'mes' derivada del campo date con substring.
# El CASE para el nombre del mes hace la salida autoexplicativa
# sin necesidad de cruzar con ninguna tabla de referencia.
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
