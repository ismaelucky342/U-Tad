// EX00 - HDFS + Spark básico
// Dispones del fichero:
//
// movies.csv
//
// con las columnas:
//
// movie_id
// title
// genre
// duration
// rating
//
// ---------------------------------------
//
// Apartado 1
//
// Carga el fichero como DataFrame.
//
// Requisitos:
//
// - inferSchema = true
// - header = true
//
// Guardar en:
//
// moviesDF
//
// ---------------------------------------
//
// Apartado 2
//
// Muestra:
//
// - Las primeras filas
// - El esquema del DataFrame
//
// ---------------------------------------
//
// Apartado 3
//
// Obtén el número total de películas.
//
// ---------------------------------------
//
// Apartado 4
//
// Obtén únicamente los nombres de las columnas.
//
// =======================================

// cargamos el fichero como DataFrame
val moviesDF = spark.read
    .option("header", "true") // Indicar que la primera fila es la cabecera
    .option("inferSchema", "true") // Inferir automáticamente el tipo de datos
    .csv("hdfs://localhost:9000/data/movies.csv")

// mostramos las primeras filas del DataFrame
moviesDF.show()

// mostramos el esquema del DataFrame
moviesDF.printSchema()

// obtenemos el número total de películas
val totalMovies = moviesDF.count()
println(s"Total de películas: $totalMovies")

// obtenemos los nombres de las columnas
val columnNames = moviesDF.columns
println("Nombres de las columnas:")
columnNames.foreach(println) // esta linea lo q hace es imprimir cada nombre de columna en una nueva línea

