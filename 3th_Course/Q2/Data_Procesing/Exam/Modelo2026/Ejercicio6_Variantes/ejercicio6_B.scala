/*
Ejercicio 6_B - Spark SQL + HDFS: RDD a DATAFRAME y JOINS

ENUNCIADO:
Tienes dos fuentes de datos en HDFS:
- customers.csv: customerId, nombre, ciudad
- orders.csv: orderId, customerId, monto, fecha

Debes:
1. Leer ambos archivos
2. Crear DataFrames desde RDD
3. Hacer JOIN de ambas tablas
4. Calcular estadísticas por cliente
5. Guardar resultado

DATOS EJEMPLO:
========== customers.csv ==========
customerId,nombre,ciudad
1,Juan,Madrid
2,María,Barcelona
3,Carlos,Madrid
4,Laura,Sevilla
5,Marco,Barcelona

========== orders.csv ==========
orderId,customerId,monto,fecha
101,1,250,2026-01-10
102,2,150,2026-01-12
103,1,300,2026-01-15
104,3,75,2026-01-16
105,2,200,2026-01-17
106,4,500,2026-01-18
107,1,100,2026-01-19
*/

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types._

val spark = SparkSession.builder()
  .appName("CustomerOrdersAnalysis")
  .getOrCreate()

// ========== PASO 1: LEER CSV ==========

val customers = spark.read
  .format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("hdfs://localhost:9000/data/customers.csv")

val orders = spark.read
  .format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("hdfs://localhost:9000/data/orders.csv")

println("=== CLIENTES ===")
customers.show()

println("\n=== PEDIDOS ===")
orders.show()

// ========== PASO 2: CREAR VISTAS TEMPORALES ==========

customers.createOrReplaceTempView("customers")
orders.createOrReplaceTempView("orders")

// ========== PASO 3: JOIN ==========

println("\n=== JOIN: Clientes con sus pedidos ===")
spark.sql("""
  SELECT c.nombre,
         c.ciudad,
         COUNT(o.orderId) as num_pedidos,
         SUM(o.monto) as total_gasto,
         AVG(o.monto) as promedio_pedido
  FROM customers c
  LEFT JOIN orders o ON c.customerId = o.customerId
  GROUP BY c.customerId, c.nombre, c.ciudad
  ORDER BY total_gasto DESC
""").show()

// ========== PASO 4: ANÁLISIS POR CIUDAD ==========

println("\n=== ANÁLISIS POR CIUDAD ===")
spark.sql("""
  SELECT c.ciudad,
         COUNT(DISTINCT c.customerId) as num_clientes,
         COUNT(o.orderId) as total_pedidos,
         SUM(o.monto) as ingresos,
         ROUND(AVG(o.monto), 2) as promedio
  FROM customers c
  LEFT JOIN orders o ON c.customerId = o.customerId
  GROUP BY c.ciudad
  ORDER BY ingresos DESC
""").show()

// ========== PASO 5: CLIENTES TOP 3 ==========

println("\n=== TOP 3 CLIENTES POR GASTO ===")
spark.sql("""
  SELECT ROW_NUMBER() OVER (ORDER BY SUM(o.monto) DESC) as ranking,
         c.nombre,
         c.ciudad,
         SUM(o.monto) as total_gasto,
         COUNT(o.orderId) as num_pedidos
  FROM customers c
  LEFT JOIN orders o ON c.customerId = o.customerId
  GROUP BY c.customerId, c.nombre, c.ciudad
  LIMIT 3
""").show()

// ========== PASO 6: RDD A DATAFRAME (CONVERSIÓN) ==========

// Crear RDD desde órdenes
val ordersRDD = orders.rdd

// Convertir RDD a Dataset para cálculos
val orders_parquet = orders
  .select("orderId", "customerId", "monto", "fecha")
  .coalesce(2)

// Guardar en Parquet (formato columnar, más eficiente que CSV)
orders_parquet.write
  .format("parquet")
  .mode("overwrite")
  .save("hdfs://localhost:9000/data/orders_parquet")

println("\n✓ Órdenes guardadas en Parquet")

// Leer de vuelta desde Parquet
val orders_read = spark.read.parquet("hdfs://localhost:9000/data/orders_parquet")
println("=== LECTURA DESDE PARQUET ===")
orders_read.show(3)

// ========== PASO 7: TABLA MATERIALIZADA EN HIVE ==========

// Crear tabla completamente materializada
val resultado_final = spark.sql("""
  SELECT c.customerId,
         c.nombre,
         c.ciudad,
         COUNT(o.orderId) as total_pedidos,
         SUM(o.monto) as gasto_total,
         ROUND(AVG(o.monto), 2) as promedio
  FROM customers c
  LEFT JOIN orders o ON c.customerId = o.customerId
  GROUP BY c.customerId, c.nombre, c.ciudad
""")

resultado_final.write
  .format("csv")
  .option("header", "true")
  .mode("overwrite")
  .save("hdfs://localhost:9000/data/customer_summary")

println("\n✓ Resumen de clientes guardado en HDFS")

spark.stop()

// ========== INTERPRETACIÓN DE RESULTADOS ==========
println("""
DATOS PROCESADOS:
- 5 clientes leídos (customers.csv)
- 7 pedidos leídos (orders.csv)

ANÁLISIS CLAVE:
- JOIN de tipo LEFT: todos los clientes, incluso sin pedidos
- Agregaciones: COUNT, SUM, AVG
- Window functions: ROW_NUMBER para ranking

FORMATOS:
- CSV: Legible, pero lento en Spark (scan completo)
- Parquet: Columnar, rápido (scan selectivo), comprimido
- Hive: Persistente, metadatos, consultas sucesivas rápidas

OPTIMIZACIONES:
1. Si CSV es > 1GB, convertir a Parquet inmediatamente
2. Broadcast small table (customers en este caso)
3. Repartición antes de JOIN si no hay índice
""")
