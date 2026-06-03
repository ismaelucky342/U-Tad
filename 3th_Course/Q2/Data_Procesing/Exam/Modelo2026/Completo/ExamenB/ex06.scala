/*
===============================================================================
EJERCICIO 6 (2 puntos) - SPARK + HDFS: ETL DISTRIBUIDO
======================================================

DATOS EN HDFS:

1. /data/usuarios.csv

   user_id,nombre,pais

2. /data/ordenes.json

   orden_id,user_id,fecha

3. /data/productos.parquet

   producto_id,orden_id,nombre_producto,unidades,precio

TAREA:

1. LEER DATOS DESDE HDFS

* usuarios.csv
* ordenes.json
* productos.parquet

2. TRANSFORMAR

* Join usuarios con ordenes
* Join resultado con productos

Crear:

importe_total = unidades × precio

3. Crear vista temporal:

"ordenes_completas"

Campos:

orden_id
fecha
nombre
pais
nombre_producto
unidades
precio
importe_total

4. Ejecutar SQL:

a) Top 5 países por ventas

b) Top 10 productos más vendidos

c) Número de órdenes por país

5. Guardar resultados:

ventas_pais.parquet

productos_top.csv

ordenes_pais.json

6. Guardar dataset completo:

hdfs://namenode:8020/processed/ordenes_completas

Condiciones:

* Particionado por país
* Formato Parquet
* Compresión Snappy
*/

// leer los datos en hdfs

// Extra: subir los datos a hdfs usando:

// hdfs dfs -put usuarios.csv /data/
// hdfs dfs -put ordenes.json /data/
// hdfs dfs -put productos.parquet /data/

// Comprobar:
// hdfs dfs -ls /data/

// Paso 1: Cargar datos

val usuarios = spark.read.option("header", "true").csv("hdfs://namenode:8020/data/usuarios.csv")

val ordenes = spark.read.json("hdfs://namenode:8020/data/ordenes.json")

val productos = spark.read.parquet("hdfs://namenode:8020/data/productos.parquet")

// Paso 2: Transformar

val ordenesUsuarios = ordenes.join(usuarios, "user_id")

val ordenesCompletas = ordenesUsuarios.join(productos, "orden_id")

val ordenesConImporte = ordenesCompletas.withColumn("importe_total", col("unidades") * col("precio"))

// Paso 3: Crear vista temporal

ordenesConImporte.createOrReplaceTempView("ordenes_completas")

// Paso 4: Ejecutar SQL

// a) Top 5 países por ventas

val ventasPais = spark.sql("""
  SELECT pais, SUM(importe_total) AS total_ventas
  FROM ordenes_completas
  GROUP BY pais
  ORDER BY total_ventas DESC
  LIMIT 5
""")

// b) Top 10 productos más vendidos

val productosTop = spark.sql("""
  SELECT nombre_producto, SUM(unidades) AS total_unidades
  FROM ordenes_completas
  GROUP BY nombre_producto
  ORDER BY total_unidades DESC
  LIMIT 10
""")

// c) Número de órdenes por país

val ordenesPais = spark.sql("""
  SELECT pais, COUNT(DISTINCT orden_id) AS num_ordenes
  FROM ordenes_completas
  GROUP BY pais
""")

// Paso 5: Guardar resultados

ventasPais.write.mode("overwrite").parquet("hdfs://namenode:8020/processed/ventas_pais.parquet")

productosTop.write.mode("overwrite").option("header", "true").csv("hdfs://namenode:8020/processed/productos_top.csv")

ordenesPais.write.mode("overwrite").json("hdfs://namenode:8020/processed/ordenes_pais.json")

// Paso 6: Guardar dataset completo
ordenesConImporte.write.mode("overwrite").parquet("hdfs://namenode:8020/processed/ordenes_completas")