/*
Ejercicio 6_C - Spark SQL + HDFS: WINDOW FUNCTIONS Y PARTICIONAMIENTO

ENUNCIADO:
Tienes datos de ventas diarias en HDFS.
Debes:
1. Leer datos con particionamiento temporal
2. Usar window functions (RANK, DENSE_RANK, ROW_NUMBER)
3. Calcular promedios móviles
4. Guardar resultados particionados

DATOS EJEMPLO:
========== sales.csv ==========
fecha,producto,categoria,monto
2026-01-10,Laptop,Electrónica,1200
2026-01-10,Mouse,Electrónica,25
2026-01-10,Escritorio,Muebles,800
2026-01-11,Laptop,Electrónica,1100
2026-01-11,Silla,Muebles,150
2026-01-12,Teclado,Electrónica,80
2026-01-12,Laptop,Electrónica,1200
2026-01-13,Mouse,Electrónica,30
2026-01-13,Escritorio,Muebles,900
*/

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.sql.expressions.Window

val spark = SparkSession.builder()
  .appName("SalesAnalysisWindows")
  .getOrCreate()

// ========== PASO 1: LEER CSV ==========

val sales = spark.read
  .format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("hdfs://localhost:9000/data/sales.csv")

println("=== DATOS ORIGINALES ===")
sales.show()

sales.createOrReplaceTempView("sales")

// ========== PASO 2: WINDOW FUNCTIONS - RANKING ==========

println("\n=== RANKING DE VENTAS POR PRODUCTO ===")
spark.sql("""
  SELECT fecha,
         producto,
         categoria,
         monto,
         ROW_NUMBER() OVER (PARTITION BY fecha ORDER BY monto DESC) as row_num,
         RANK() OVER (PARTITION BY fecha ORDER BY monto DESC) as rank,
         DENSE_RANK() OVER (PARTITION BY fecha ORDER BY monto DESC) as dense_rank
  FROM sales
  ORDER BY fecha, rank
""").show()

// ========== PASO 3: TOP PRODUCTOS POR CATEGORÍA ==========

println("\n=== TOP 2 VENTAS POR CATEGORÍA Y FECHA ===")
val top_por_cat = spark.sql("""
  SELECT fecha,
         categoria,
         producto,
         monto,
         ROW_NUMBER() OVER (PARTITION BY fecha, categoria ORDER BY monto DESC) as posicion
  FROM sales
  WHERE ROW_NUMBER() OVER (PARTITION BY fecha, categoria ORDER BY monto DESC) <= 2
""")

// Alternative use CTEs
spark.sql("""
  WITH ranked_sales AS (
    SELECT fecha,
           categoria,
           producto,
           monto,
           ROW_NUMBER() OVER (PARTITION BY fecha, categoria ORDER BY monto DESC) as rank
    FROM sales
  )
  SELECT * FROM ranked_sales WHERE rank <= 2
""").show()

// ========== PASO 4: PROMEDIOS Y TOTALES ACUMULATIVOS ==========

println("\n=== TOTALES POR FECHA (ACUMULATIVO) ===")
spark.sql("""
  SELECT fecha,
         producto,
         monto,
         SUM(monto) OVER (ORDER BY fecha) as total_acumulado,
         SUM(monto) OVER (PARTITION BY fecha) as total_fecha,
         AVG(monto) OVER (PARTITION BY fecha) as promedio_fecha,
         SUM(monto) OVER (PARTITION BY categoria ORDER BY fecha) as total_categoria
  FROM sales
  ORDER BY fecha, producto
""").show()

// ========== PASO 5: LAG Y LEAD (COMPARAR CON DÍAS ANTERIORES) ==========

println("\n=== LAG/LEAD: COMPARAR CON DÍA ANTERIOR ===")
spark.sql("""
  SELECT fecha,
         producto,
         monto,
         LAG(monto) OVER (PARTITION BY producto ORDER BY fecha) as venta_anterior,
         LEAD(monto) OVER (PARTITION BY producto ORDER BY fecha) as venta_proxima,
         monto - LAG(monto) OVER (PARTITION BY producto ORDER BY fecha) as diferencia
  FROM sales
  ORDER BY producto, fecha
""").show()

// ========== PASO 6: PERCENTILES Y QUANTILES ==========

println("\n=== PERCENTILES POR CATEGORÍA ===")
spark.sql("""
  SELECT fecha,
         categoria,
         monto,
         PERCENT_RANK() OVER (PARTITION BY categoria ORDER BY monto) as percent_rank,
         NTILE(4) OVER (PARTITION BY categoria ORDER BY monto) as cuartil
  FROM sales
  ORDER BY categoria, fecha
""").show()

// ========== PASO 7: PARTICIONAMIENTO Y ESCRITURA EN HDFS ==========

// Crear tabla particionada por fecha
sales
  .repartition(col("fecha"))
  .write
  .format("parquet")
  .mode("overwrite")
  .partitionBy("fecha")
  .save("hdfs://localhost:9000/data/sales_partitioned")

println("\n✓ Datos particionados por fecha guardados en Parquet")

// ========== PASO 8: LEER DATOS PARTICIONADOS ==========

val sales_part = spark.read.parquet("hdfs://localhost:9000/data/sales_partitioned")

println("\n=== LECTURA SELECTIVA (solo 2026-01-12) ===")
sales_part
  .filter(col("fecha") === "2026-01-12")
  .show()

// ========== PASO 9: RESUMEN COMPLETO GUARDADO ==========

val resumen = spark.sql("""
  WITH ranked AS (
    SELECT fecha,
           categoria,
           producto,
           monto,
           ROW_NUMBER() OVER (PARTITION BY fecha, categoria ORDER BY monto DESC) as rank,
           SUM(monto) OVER (PARTITION BY fecha) as total_fecha,
           AVG(monto) OVER (PARTITION BY categoria) as promedio_categoria
    FROM sales
  )
  SELECT fecha,
         categoria,
         producto,
         monto,
         rank,
         total_fecha,
         promedio_categoria
  FROM ranked
""")

resumen.write
  .format("csv")
  .option("header", "true")
  .mode("overwrite")
  .save("hdfs://localhost:9000/data/sales_analysis")

println("\n✓ Análisis completo guardado en HDFS")

// ========== PASO 10: CONVERSIÓN RDD -> DATAFRAME ==========

val rddVentas = sales.rdd

// Convertir RDD a DataFrame con esquema
val dfDesdeRDD = spark.createDataFrame(
  rddVentas,
  sales.schema
)

println("\n=== CONVERSIÓN RDD A DATAFRAME ===")
dfDesdeRDD.show(3)

spark.stop()

println("""
╔═══════════════════════════════════════════════════════════════╗
║           WINDOW FUNCTIONS - CONCEPTOS CLAVE                ║
╚═══════════════════════════════════════════════════════════════╝

ROW_NUMBER()     → Secuencia única (1,2,3...)
RANK()           → Mismo rank para empates (1,2,2,4...)
DENSE_RANK()     → Denso sin saltos (1,2,2,3...)

LAG/LEAD         → Acceso a filas anteriores/posteriores
FIRST_VALUE      → Primer valor de ventana
LAST_VALUE       → Último valor de ventana

SUM/AVG OVER     → Agregaciones con ventana
PERCENT_RANK()   → Rango como porcentaje
NTILE()          → Dividir en N cuantiles

PARTICIONAMIENTO EN HDFS:
- Beneficio: Queries selectivas solo leen particiones necesarias
- Riesgo: Demasiadas particiones = overhead
- Mejor: Particionar por fecha/región si los queries son selectivos
""")
