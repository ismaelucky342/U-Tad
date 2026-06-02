/*
Ejercicio 6_D - Spark SQL + HDFS: ETL COMPLETO Y OPTIMIZACIONES

ENUNCIADO:
Construir un pipeline ETL completo que:
1. Lea múltiples fuentes (CSV, JSON, Parquet)
2. Limpie y valide datos
3. Enriquezca con transformaciones
4. Guarde en formato optimizado

Este es el tipo de proyecto real que pedirían en un examen avanzado.

ESQUEMA DE DATOS:
- users.json: userId, userName, país
- transactions.csv: transactionId, userId, monto, tipo, fecha
- productos.parquet: productId, nombre, categoría, precio
- Target: Crear tabla de usuarios con estadísticas de transacciones
*/

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions.Window

val spark = SparkSession.builder()
  .appName("CompleteETL")
  .config("spark.sql.adaptive.enabled", "true")
  .getOrCreate()

// ========== PASO 1: LECTURA DE MÚLTIPLES FUENTES ==========

// Leer JSON con usuarios
val users = spark.read
  .format("json")
  .load("hdfs://localhost:9000/data/users.json")

// Leer CSV con transacciones
val transactions = spark.read
  .format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("hdfs://localhost:9000/data/transactions.csv")

// Leer Parquet con productos
val products = spark.read
  .parquet("hdfs://localhost:9000/data/products.parquet")

println("=== USUARIOS (JSON) ===")
users.show(3)

println("\n=== TRANSACCIONES (CSV) ===")
transactions.show(3)

println("\n=== PRODUCTOS (PARQUET) ===")
products.show(3)

// ========== PASO 2: LIMPIEZA Y VALIDACIÓN ==========

// Limpiar usuarios
val users_clean = users
  .na.fill("Unknown", Seq("country"))
  .withColumn("userId", col("userId").cast("Long"))
  .filter(col("userId").isNotNull)

// Validar transacciones
val transactions_clean = transactions
  .withColumn("monto", col("monto").cast("Decimal(10, 2)"))
  .withColumn("fecha", to_date(col("fecha"), "yyyy-MM-dd"))
  .filter(col("monto") > 0)  // Rechazar transacciones con monto negativo
  .filter(col("userId").isNotNull)

users_clean.createOrReplaceTempView("users_clean")
transactions_clean.createOrReplaceTempView("transactions_clean")
products.createOrReplaceTempView("products")

// ========== PASO 3: TRANSFORMACIONES Y ENRIQUECIMIENTO ==========

// Crear vista con estadísticas de transacciones por usuario
val user_stats = spark.sql("""
  SELECT u.userId,
         u.userName,
         u.country,
         COUNT(t.transactionId) as num_transacciones,
         SUM(t.monto) as total_gastado,
         AVG(t.monto) as promedio_transaccion,
         MIN(t.monto) as min_transaccion,
         MAX(t.monto) as max_transaccion,
         COUNT(DISTINCT DATE_TRUNC('month', t.fecha)) as meses_activo,
         MAX(t.fecha) as ultima_transaccion,
         MIN(t.fecha) as primera_transaccion
  FROM users_clean u
  LEFT JOIN transactions_clean t ON u.userId = t.userId
  GROUP BY u.userId, u.userName, u.country
""")

user_stats.createOrReplaceTempView("user_stats")

println("\n=== ESTADÍSTICAS POR USUARIO ===")
user_stats.show()

// ========== PASO 4: ANÁLISIS AVANZADO ==========

// Ranking de usuarios por gasto
val user_ranking = spark.sql("""
  WITH ranked_users AS (
    SELECT *,
           RANK() OVER (ORDER BY total_gastado DESC) as rank_gasto,
           PERCENT_RANK() OVER (ORDER BY total_gastado DESC) as percentil,
           NTILE(10) OVER (ORDER BY total_gastado DESC) as decil
    FROM user_stats
  )
  SELECT userid,
         userName,
         country,
         total_gastado,
         num_transacciones,
         rank_gasto,
         ROUND(percentil * 100, 2) as percentil_num,
         decil
  FROM ranked_users
  WHERE rank_gasto <= 20
  ORDER BY rank_gasto
""")

println("\n=== TOP 20 USUARIOS POR GASTO ===")
user_ranking.show()

// ========== PASO 5: SEGMENTACIÓN ==========

// Segmentar usuarios por valor (RFM análisis simple)
val user_segments = spark.sql("""
  SELECT userId,
         userName,
         country,
         num_transacciones,
         total_gastado,
         DATEDIFF(CURRENT_DATE(), ultima_transaccion) as dias_inactividad,
         CASE 
           WHEN total_gastado > 10000 THEN 'VIP'
           WHEN total_gastado > 1000 THEN 'Premium'
           WHEN total_gastado > 100 THEN 'Regular'
           ELSE 'Bajo'
         END as segmento,
         CASE
           WHEN DATEDIFF(CURRENT_DATE(), ultima_transaccion) <= 30 THEN 'Activo'
           WHEN DATEDIFF(CURRENT_DATE(), ultima_transaccion) <= 90 THEN 'Dormido'
           ELSE 'Inactivo'
         END as estado
  FROM user_stats
""")

user_segments.createOrReplaceTempView("user_segments")

println("\n=== SEGMENTACIÓN DE USUARIOS ===")
spark.sql("SELECT segmento, COUNT(*) as cantidad FROM user_segments GROUP BY segmento").show()

spark.sql("SELECT estado, COUNT(*) as cantidad FROM user_segments GROUP BY estado").show()

// ========== PASO 6: VALIDACIÓN DE DATOS ==========

// Detectar anomalías
val anomalies = spark.sql("""
  WITH stats AS (
    SELECT AVG(monto) as avg_monto,
           STDDEV(monto) as stddev_monto
    FROM transactions_clean
  )
  SELECT t.*,
         ROUND((t.monto - s.avg_monto) / s.stddev_monto, 2) as z_score
  FROM transactions_clean t,
       stats s
  WHERE (t.monto - s.avg_monto) / s.stddev_monto > 3
""")

println("\n=== TRANSACCIONES ANÓMALAS (Z-SCORE > 3) ===")
anomalies.show()

// ========== PASO 7: GUARDAR RESULTADOS OPTIMIZADOS ==========

// Guardar tabla principal en Parquet particionada
user_segments.write
  .format("parquet")
  .mode("overwrite")
  .partitionBy("pais")
  .save("hdfs://localhost:9000/data/warehouse/user_segments")

// Guardar en tabla Hive persistente
user_stats.write
  .format("csv")
  .option("header", "true")
  .mode("overwrite")
  .save("hdfs://localhost:9000/data/warehouse/user_statistics")

// Guardar tabla de anomalías
anomalies.write
  .format("parquet")
  .mode("overwrite")
  .save("hdfs://localhost:9000/data/warehouse/anomalies")

println("\n✓ Todas las tablas guardadas en HDFS")

// ========== PASO 8: METADATOS Y DOCUMENTACIÓN ==========

println("\n=== ESQUEMAS FINALES ===")
println("\nuser_segments:")
user_segments.printSchema()

println("\nuser_ranking:")
user_ranking.printSchema()

// ========== STEP 9: VERIFICACIÓN DE INTEGRIDAD ==========

val count_users_original = users.count()
val count_users_processed = user_stats.count()

println(s"\n=== CONTROL DE CALIDAD ===")
println(s"Usuarios originales: $count_users_original")
println(s"Usuarios procesados: $count_users_processed")
println(s"Diferencia: ${count_users_original - count_users_processed} (usuarios sin transacciones)")

spark.stop()

println("""
╔═══════════════════════════════════════════════════════════════╗
║              RESUMEN DEL PIPELINE ETL                        ║
╚═══════════════════════════════════════════════════════════════╝

FASES:
1. ✓ EXTRACT: Lectura desde JSON, CSV, Parquet (multisource)
2. ✓ TRANSFORM:
   - Limpieza (null handling, tipo casting)
   - Validación (filtros negativos
, anomalías)
   - Enriquecimiento (aggregaciones, ranking, segmentación)
3. ✓ LOAD: Guardado en Parquet particionado + warehouse

PATRONES APLICADOS:
- Window functions para ranking
- Case statements para lógica de negocio
- Z-score para detección de anomalías
- Particionamiento por país para queries selectivos

OPTIMIZACIONES:
- Parquet: 10-100x más rápido que CSV
- Particionamiento: Queries selectivos solo leen particiones necesarias
- Adaptive Query Execution: Spark optimiza en tiempo de ejecución
- Broadcast small tables automáticamente

SIGUIENTES PASOS EN PRODUCCIÓN:
1. Programar pipeline con Airflow/Spark Structured Streaming
2. Agregar data quality checks
3. Implementar SCD (Slowly Changing Dimensions)
4. Conectar a BI tools (Tableau, Looker)
""")
