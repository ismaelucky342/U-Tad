//## EX06 — Spark SQL + HDFS Modelo Examen 
//
// Enunciado general:
//
// Vamos a trabajar con Spark SQL utilizando el dataset
// `video_games.csv` sobre videojuegos.
//
// El fichero contiene:
//
// Game_ID
// Title
// Genre
// Platform
// Rating
// Release_Year
//
// Para la entrega se pide guardar las sentencias utilizadas
// y adjuntar capturas de la ejecución.
//
// ### Apartados
//
// * Apartado 1 (0,1 pts):
// Descargar el fichero `video_games.csv` y explorar
// su contenido localmente utilizando algún comando
// del sistema.
//
// * Apartado 2 (0,2 pts):
// Arrancar HDFS y copiar el fichero a:
//
// /data/games/
//
// * Apartado 3 (0,1 pts):
// Comprobar mediante comandos HDFS que el fichero
// existe correctamente.
//
// * Apartado 4 (0,2 pts):
// Arrancar Spark y leer el fichero desde HDFS
// en un RDD llamado:
//
// GamesRDD
//
// Nota:
// El fichero contiene cabecera.
//
// * Apartado 5 (0,4 pts):
// Utilizando EXCLUSIVAMENTE transformaciones y acciones
// sobre GamesRDD:
//
// Obtener cuántos videojuegos existen por plataforma.
//
// Ejemplo:
//
// (PC,30)
// (PS5,18)
// (Xbox,25)
//
// Mostrar resultado por pantalla.
//
// * Apartado 6 (0,2 pts):
// Cargar el mismo archivo desde HDFS como DataFrame
// en una variable:
//
// dfGames
//
// Configuración:
//
// - inferSchema=true
// - header=true
//
// * Apartado 7 (0,1 pts):
// Registrar el DataFrame como vista temporal:
//
// games
//
// * Apartado 8 (0,4 pts):
// Utilizando Spark SQL:
//
// Obtener videojuegos cuyo:
//
// Rating >= 8
//
// y además:
//
// Genre='Action'
//
// Ordenar el resultado por Rating
// de forma descendente.
//
// Guardar resultado en:
//
// actionGames
//
// Mostrar resultado.
//
// * Apartado 9 (0,3 pts):
// Utilizando EXCLUSIVAMENTE la API de DataFrames:
//
// Obtener videojuegos pertenecientes a:
//
// Platform='PC'
//
// cuyo año de lanzamiento sea posterior a:
//
// 2018
//
// Mostrar:
//
// Title
// Rating
//
// Mostrar resultado final.
//
//

// Apartado 1 

// descarga del fichero
// wget -O video_games.csv https://example.com/video_games.csv

// exploramos el contenido 
// head video_games.csv

// Apartado 2

// Arrancar HDFS
// start-dfs.sh

// Crear directorio en HDFS y copiar el fichero
// hdfs dfs -mkdir -p /data/games
// hdfs dfs -put video_games.csv /data/games/

// Apartado 3

// Comprobar que el fichero existe en HDFS
// hdfs dfs -ls /data/games/
// hdfs dfs -cat /data/games/video_games.csv | head

// Apartado 4

val GamesRDD = sc.textFile("hdfs://localhost:9000/data/games/video_games.csv")

// Apartado 5

val header = GamesRDD.first() // Obtener la cabecera

val gamesCount = GamesRDD
  .filter(line => line != header) // Filtrar la cabecera
  .map(line => line.split(",")(3)) // Suponiendo que la plataforma está en la cuarta columna (índice 3)
  .map(platform => (platform, 1)) // Crear tuplas (plataforma, 1)
  .reduceByKey(_ + _) // Sumar las tuplas por plataforma

gamesCount.collect().foreach(println) // Mostrar resultado por pantalla

// Apartado 6

val dfGames = spark.read
    .option("header", "true") // Indicar que la primera fila es la cabecera
    .option("inferSchema", "true") // Inferir automáticamente el tipo de datos
    .csv("hdfs://localhost:9000/data/games/video_games.csv")

// Apartado 7

dfGames.createOrReplaceTempView("games")

// Apartado 8

val actionGames = spark.sql("""
    SELECT *
    FROM games
    WHERE Rating >= 8 AND Genre = 'Action'
    ORDER BY Rating DESC
""")

actionGames.show()

// Apartado 9

dfGames.filter(dfGames("Platform") === "PC" && dfGames("Release_Year") > 2018)
    .select("Title", "Rating")
    .show()


