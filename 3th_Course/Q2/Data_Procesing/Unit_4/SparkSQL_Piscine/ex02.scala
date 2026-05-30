// =======================================
//  ex02 — HDFS + Spark básico
// =======================================
//
// Archivo: books.csv
//
// Columnas:
//
// book_id,title,author,pages,score
//
// 1) Descarga el fichero usando wget.
//
// 2) Crea en HDFS:
//
// /data/books/
//
// y copia el fichero dentro.
//
// 3) Comprueba desde HDFS que el fichero existe.
//
// 4) Carga el fichero desde HDFS en un DataFrame:
//
// booksDF
//
// usando:
//
// - header=true
// - inferSchema=true
//
// 5) Muestra:
//
// - primeras filas
// - esquema
//
// 6) Mostrar únicamente:
//
// title
// score
//
// 7) Mostrar libros con score > 8
//
// 8) Ordenar libros por score descendente
//
// =======================================


// descarga del fichero 

//wget https://example.com/books.csv
// con flags correctas seria wget -O books.csv https://example.com/books.csv porque el nombre del fichero no se corresponde con el final de la URL

// creación del directorio en HDFS y copia del fichero

// hdfs dfs -mkdir -p /data/books
// hdfs dfs -put books.csv /data/books/

// comprobación de la existencia del fichero en HDFS

// hdfs dfs -ls /data/books/
// hdfs dfs -cat /data/books/books.csv | head

// carga del fichero desde HDFS en un DataFrame

val booksDF = spark.read
    .option("header", "true") // Indicar que la primera fila es la cabecera
    .option("inferSchema", "true") // Inferir automáticamente el tipo de datos
    .csv("hdfs://localhost:9000/data/books/books.csv")  

// mostrar las primeras filas del DataFrame

booksDF.show()

// mostrar el esquema del DataFrame

booksDF.printSchema()

// Mostrar únicamente title y score

booksDF.select("title", "score").show()

// Mostrar libros con score > 8

booksDF.filter(booksDF("score") > 8).show()
// booksDF.filter($"score" > 8).show() // Usando la sintaxis de columnas con $

// Ordenar libros por score descendente

booksDF.orderBy(booksDF("score").desc).show()

