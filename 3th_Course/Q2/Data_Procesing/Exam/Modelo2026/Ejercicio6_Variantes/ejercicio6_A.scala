/*
Ejercicio 6_A - Spark SQL + HDFS: LECTURA Y TRANSFORMACIÓN DE DATOS

ENUNCIADO:
Tienes un archivo CSV en HDFS con datos de ventas.
Necesitas:
1. Leer archivo CSV desde HDFS
2. Crear DataFrame con esquema
3. Hacer queries SQL
4. Guardar resultado en HDFS

SETUP PREVIO (en HD FS):
========== Crear archivo en HDFS ==========
hdfs dfs -mkdir -p /data/ventas

echo "producto,categoria,precio,cantidad,fecha
Laptop,Electrónica,1200,5,2026-01-15
Mouse,Electrónica,25,50,2026-01-15
Escritorio,Muebles,800,3,2026-01-16
Silla,Muebles,150,10,2026-01-16
Teclado,Electrónica,80,20,2026-01-17" > ventas.csv

hdfs dfs -put ventas.csv /data/ventas/

========== VERIFICAR ==========
hdfs dfs -cat /data/ventas/ventas.csv
*/

import org.apache.spark.sql.SparkSession

val spark = SparkSession
  .builder()
  .appName("VentasAnalysis")
  .getOrCreate()

// ========== PASO 1: LEER CSV DE HDFS ==========

val df = spark.read
  .format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("hdfs://localhost:9000/data/ventas/ventas.csv")

println("=== DATOS ORIGINALES (desde HDFS) ===")
df.show()

// ========== PASO 2: CREAR VISTA TEMPORAL ==========

df.createOrReplaceTempView("ventas")

// ========== PASO 3: QUERIES SQL ==========

println("\n=== QUERY 1: Total por categoría ===")
spark.sql("""
  SELECT categoria, 
         COUNT(*) as productos,
         SUM(precio * cantidad) as total_venta
  FROM ventas
  GROUP BY categoria
  ORDER BY total_venta DESC
""").show()

println("\n=== QUERY 2: Productos caros (>150) ===")
spark.sql("""
  SELECT producto, 
         categoria, 
         precio,
         cantidad,
         precio * cantidad as total
  FROM ventas
  WHERE precio > 150
  ORDER BY precio DESC
""").show()

// ========== PASO 4: TRANSFORMACIONES Y GUARDAR EN HDFS ==========

val resultados = spark.sql("""
  SELECT categoria,
         COUNT(*) as num_productos,
         SUM(precio * cantidad) as ingresos_totales,
         AVG(precio) as precio_promedio,
         ROUND(SUM(precio * cantidad) / COUNT(*), 2) as ingreso_por_producto
  FROM ventas
  GROUP BY categoria
""")

println("\n=== RESUMEN POR CATEGORÍA ===")
resultados.show()

// Guardar en HDFS
resultados.write
  .format("csv")
  .option("header", "true")
  .mode("overwrite")
  .save("hdfs://localhost:9000/data/resultados/resumen_ventas")

println("\n✓ Archivo guardado en HDFS: /data/resultados/resumen_ventas")

// ========== PASO 5: LECTURA DESDE HIVE (OPCIONAL) ==========

// Crear tabla persistente en Hive
df.write.mode("overwrite").option("path", "hdfs://localhost:9000/hive/ventas_table").saveAsTable("ventas_hive")

spark.sql("SELECT * FROM ventas_hive WHERE categoria = 'Electrónica'").show()

spark.stop()
