//## EX07 — Spark SQL + HDFS Modelo 2 Examen
//
// Enunciado general:
//
// Vamos a trabajar con Spark SQL utilizando
// el dataset `movies_platforms.csv`.
//
// El fichero contiene:
//
// Movie_ID
// Title
// Genre
// Platform
// Duration
// Score
//
// ### Apartados
//
// * Apartado 1 (0,1 pts):
// Descargar el fichero y explorar su contenido
// localmente.
//
// * Apartado 2 (0,2 pts):
// Copiar el fichero a:
//
// /data/movies/
//
// dentro de HDFS.
//
// * Apartado 3 (0,1 pts):
// Verificar que el fichero existe.
//
// * Apartado 4 (0,2 pts):
// Leer el fichero desde HDFS como RDD:
//
// MoviesRDD
//
// El archivo contiene cabecera.
//
// * Apartado 5 (0,4 pts):
// Utilizando SOLO RDD:
//
// Obtener cuántas películas existen
// por plataforma.
//
// Mostrar resultado.
//
// * Apartado 6 (0,2 pts):
// Cargar el fichero como DataFrame:
//
// dfMovies
//
// * Apartado 7 (0,1 pts):
// Registrar el DataFrame como:
//
// movies
//
// * Apartado 8 (0,4 pts):
// Utilizando SQL:
//
// Obtener películas con:
//
// Score >= 8
//
// y:
//
// Duration >120
//
// Ordenarlas por Score descendente.
//
// Guardar resultado en:
//
// topMovies
//
// * Apartado 9 (0,3 pts):
// Utilizando API DataFrame:
//
// Obtener películas cuyo:
//
// Genre='Drama'
//
// Crear una nueva columna:
//
// duration_label
//
// Reglas:
//
// Duration <90 -> "short"
// Duration >=90 -> "long"
//
// Mostrar:
//
// Title
// Duration
// duration_label
//

// Apartado 1: Descargar el fichero y explorar su contenido localmente

// wget -O movies_platforms.csv https://example.com/movies_platforms.csv

// head movies_platforms.csv

// Apartado 2: Copiar el fichero a HDFS

// arrancar HDFS

// start-dfs.sh

// crear directorio en HDFS y copiar el fichero

// hdfs dfs -mkdir -p /data/movies
// hdfs dfs -put movies_platforms.csv /data/movies/

// Apartado 3: Verificar que el fichero existe

// hdfs dfs -ls /data/movies/
// hdfs dfs -cat /data/movies/movies_platforms.csv | head

// Apartado 4: Leer el fichero desde HDFS como RDD

val MoviesRDD = sc.textFile("hdfs://localhost:9000/data/movies/movies_platforms.csv")

// Apartado 5: Utilizando SOLO RDD, obtener cuántas películas existen por plataforma

val header = MoviesRDD.first() // Obtener la cabecera
val platformCount = MoviesRDD
    .filter(line => line != header) // Filtrar la cabecera
    .map(line => line.split(",")(3)) // Suponiendo que la plataforma está en la cuarta columna (índice 3)
    .map(platform => (platform, 1)) // Crear tuplas (plataforma, 1)
    .reduceByKey(_ + _) // Sumar las tuplas por plataforma
platformCount.collect().foreach(println) // Mostrar resultado

// Apartado 6: Cargar el fichero como DataFrame

val dfMovies = spark.read
    .option("header", "true") // Indicar que la primera fila es la cabecera
    .option("inferSchema", "true") // Inferir automáticamente el tipo de datos
    .csv("hdfs://localhost:9000/data/movies/movies_platforms.csv")

// Apartado 7: Registrar el DataFrame como vista temporal

dfMovies.createOrReplaceTempView("movies")

// Apartado 8: Utilizando SQL, obtener películas con Score >= 8 y Duration >120, ordenarlas por Score descendente

val topMovies = spark.sql("""
    SELECT *
    FROM movies
    WHERE Score >= 8 AND Duration > 120
    ORDER BY Score DESC
""")

topMovies.show() // Mostrar resultado