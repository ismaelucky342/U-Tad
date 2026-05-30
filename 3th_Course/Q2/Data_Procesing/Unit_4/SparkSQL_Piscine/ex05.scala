// =======================================
// EX05 — Primer contacto RDD
// =======================================
//
// Archivo: products.csv
//
// Columnas:
//
// product_id,name,category,price
//
// 1) Descarga el archivo y súbelo a:
//
// /data/products/
//
// 2) Carga el fichero desde HDFS
// como un RDD:
//
// productsRDD
//
// IMPORTANTE:
//
// El fichero tiene cabecera.
//
// 3) Usando SOLO transformaciones y acciones
// de RDD:
//
// Obtener cuántos productos hay
// por categoría.
//
// 4) Usando SOLO RDD:
//
// Obtener cuántos productos tienen
// precio > 100.
//
// 5) Cargar el mismo archivo como
// DataFrame:
//
// productsDF
//
// 6) Usando DataFrame:
//
// Mostrar name y price
// de productos con precio >100
//
// =======================================

// Apartado 1 

// wget https://example.com/products.csv
// con flags correctas seria wget -O products.csv https://example.com/products.csv porque el nombre del fichero no se corresponde con el final de la URL

// hdfs dfs -mkdir -p /data/products
// hdfs dfs -put products.csv /data/products/

// hdfs dfs -ls /data/products/
// hdfs dfs -cat /data/products/products.csv | head

// Apartado 2

val productsRDD = sc.textFile("hdfs://localhost:9000/data/products/products.csv")

// Apartado 3

val header = productsRDD.first() // Obtener la cabecera
val categoryCount = productsRDD
  .filter(line => line != header) // Filtrar la cabecera
  .map(line => line.split(",")(2)) // Suponiendo que la categoría está en la tercera columna (índice 2)
  .map(category => (category, 1)) // Crear tuplas (categoría, 1)
  .reduceByKey(_ + _) // Sumar las tuplas por categoría
categoryCount.collect().foreach(println)

// Apartado 4

val priceCount = productsRDD
  .filter(line => line != header) // Filtrar la cabecera
  .map(line => line.split(",")(3).toDouble) // Suponiendo que el precio está en la cuarta columna (índice 3)
  .filter(price => price > 100) // Filtrar productos con precio > 100
  .count() // Contar el número de productos que cumplen la condición
println(s"Número de productos con precio > 100: $priceCount")

// Apartado 5

val productsDF = spark.read
    .option("header", "true") // Indicar que la primera fila es la cabecera
    .option("inferSchema", "true") // Inferir automáticamente el tipo de datos
    .csv("hdfs://localhost:9000/data/products/products.csv")

// Apartado 6

productsDF.filter(productsDF("price") > 100).select("name", "price").show()
// productsDF.filter($"price" > 100).select("name", "price").show() // Usando la sintaxis de columnas con $