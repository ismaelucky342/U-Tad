// EX01 — HDFS + Spark básico
// Seguimos usando:
//
// moviesDF
//
// Columnas:
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
// Mostrar únicamente:
//
// title
// rating
//
// ---------------------------------------
//
// Apartado 2
//
// Mostrar únicamente las películas
// con rating superior a 8.
//
// ---------------------------------------
//
// Apartado 3
//
// Contar cuántas películas tienen
// rating superior a 8.
//
// ---------------------------------------
//
// Apartado 4
//
// Mostrar las películas ordenadas
// por rating de mayor a menor.
//
// =======================================

// Cargamos el fichero como DataFrame
val moviesDF = spark.read
    .option("header", "true") // Indicar que la primera fila es la cabecera
    .option("inferSchema", "true") // Inferir automáticamente el tipo de datos
    .csv("hdfs://localhost:9000/data/movies.csv")

// Apartado 1: Mostrar únicamente title y rating

moviesDF.select("title", "rating").show()

// Apartado 2: Mostrar únicamente las películas con rating superior a 8

moviesDF.filter(moviesDF("rating") > 8).show()
// moviesDF.filter($"rating" > 8).show() // Usando la sintaxis de columnas con $

// Apartado 3: Contar cuántas películas tienen rating superior a 8

val countHighRating = moviesDF.filter(moviesDF("rating") > 8).count()
println(s"Número de películas con rating superior a 8: $countHighRating")

// Apartado 4: Mostrar las películas ordenadas por rating de mayor a menor
moviesDF.orderBy(moviesDF("rating").desc).show()

