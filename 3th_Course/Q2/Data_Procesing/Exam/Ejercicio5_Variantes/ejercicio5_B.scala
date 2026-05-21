//## EJERCICIO 5 (VARIANTE) — Spark SQL + HDFS (2 puntos)
//
//**Enunciado general:**
//Vamos a trabajar con Spark SQL utilizando el dataset `movies_catalog.csv` (sobre catálogo de películas) para realizar una serie de consultas. Debes escribir el código limpio en tu archivo `.scala` (recordando comentar los comandos de terminal).
//
//### Apartados del ejercicio
//
//* **Apartado 1 (0,1 pts):** Descargar el fichero `movies_catalog.csv` y explorar su contenido en el sistema local (por ejemplo, con el comando `head`).
//* **Apartado 2 (0,2 pts):** Arrancar HDFS y copiar el fichero `movies_catalog.csv` desde el entorno local a la ruta `/data/movies/` de HDFS.
//* **Apartado 3 (0,1 pts):** Comprobar con un comando nativo de `hdfs` que el fichero está correctamente creado en la ruta pedida.
//* **Apartado 4 (0,2 pts):** Arrancar Spark y leer el fichero `movies_catalog.csv` de HDFS en una variable RDD llamada `MoviesRDD`.
//* *Nota:* La ruta en HDFS es `hdfs://localhost:9000/data/movies/movies_catalog.csv` y el archivo tiene cabecera.
//
//
//* **Apartado 5 (0,4 pts):** Usando exclusivamente el RDD creado (`MoviesRDD`), sus transformaciones y acciones, responde a la siguiente pregunta: **¿cuántas películas hay por cada año de lanzamiento (`Release_Year`)?**
//* *Resultado esperado (ejemplo de formato):*
//```text
//(2020,45)
//(2019,120)
//(2021,8)
//...
//
//```
//
//
//
//
//* **Apartado 6 (0,2 pts):** Cargar el mismo CSV desde HDFS como un **DataFrame** (en una variable llamada `dfMovies`), infiriendo automáticamente el tipo de datos y usando la primera fila como cabecera.
//* **Apartado 7 (0,1 pts):** Registrar el DataFrame `dfMovies` como una tabla/vista temporal para consultas SQL llamada `movies`.
//* **Apartado 8 (0,4 pts):** Realizar una **consulta SQL** (sobre la tabla `movies`) para obtener las películas del género Acción (`Genre = 'Action'`) que tengan una nota/puntuación mayor o igual a 8 (`Rating >= 8`). El resultado debe ordenarse por la nota de forma descendente, guardarse en la variable `mejoresAccion` y mostrarse por pantalla.
//* **Apartado 9 (0,3 pts):** Usando la **API de DataFrames** (no SQL), obtener las películas de la productora *"Warner Bros"* (`Studio`) cuya duración media (`Duration_Min`) sea superior a 120 minutos. Muestra el resultado final por pantalla.


// Resolución del ejercicio:

// Apartado 1
// Descargar el fichero `movies_catalog.csv` y explorar su contenido en el sistema local (ejemplo):
// wget https://example.com/movies_catalog.csv
// head movies_catalog.csv

// Apartado 2
// Arrancar HDFS y copiar el fichero `movies_catalog.csv` desde el entorno local a la ruta `/data/movies/` de HDFS (ejemplo):
// start-dfs.sh
// hdfs dfs -mkdir -p /data/movies
// hdfs dfs -put movies_catalog.csv /data/movies/  

// Apartado 3
// Comprobar con un comando nativo de `hdfs` que el fichero está correctamente creado en la ruta pedida (ejemplo):
// hdfs dfs -ls /data/movies
// hdfs dfs -cat /data/movies/movies_catalog.csv | head

// Apartado 4 (cuidado con los filtrados agresivos para eliminar la cabecera, es mejor usar un filtrado seguro)
// Arrancar Spark y leer el fichero `movies_catalog.csv` de HDFS en una variable RDD llamada `MoviesRDD` (ejemplo):
val MoviesRDD = sc.textFile("hdfs://localhost:9000/data/movies/movies_catalog.csv")
val header = MoviesRDD.first()
val datos = MoviesRDD.filter(linea => linea != header) // Filtrado seguro para eliminar la cabecera del RDD

// Apartado 5
// Usando exclusivamente el RDD creado (`MoviesRDD`), sus transformaciones y acciones, responde a la siguiente pregunta: **¿cuántas películas hay por cada año de lanzamiento (`Release_Year`)?** (ejemplo):
val moviesByYear = datos.map(line => line.split(",")(0)) // Asumiendo que el año de lanzamiento está en la primera columna
  .map(year => (year, 1))
  .reduceByKey((a, b) => a + b)
moviesByYear.collect().foreach(println) 

// *Resultado esperado a obtener (ejemplo de formato):*
//(2020,45)
//(2019,120)
//(2021,8)
//...

// Apartado 6
// Cargar el mismo CSV desde HDFS como un **DataFrame** (en una variable llamada `dfMovies`), infiriendo automáticamente el tipo de datos y usando la primera fila como cabecera (ejemplo):
val dfMovies = spark.read.option("header", "true").option("inferSchema", "true").csv("hdfs://localhost:9000/data/movies/movies_catalog.csv")    

// Apartado 7
// Registrar el DataFrame `dfMovies` como una tabla/vista temporal para consultas SQL llamada `movies` (ejemplo):
dfMovies.createOrReplaceTempView("movies")

// Apartado 8
// Realizar una **consulta SQL** (sobre la tabla `movies`) para obtener las películas del género Acción (`Genre = 'Action'`) que tengan una nota/puntuación mayor o igual a 8 (`Rating >= 8`), ordenadas por la nota de forma descendente, guardadas en la variable `mejoresAccion` y mostradas por pantalla (ejemplo):
val mejoresAccion = spark.sql("SELECT * FROM movies WHERE Genre = 'Action' AND Rating >= 8 ORDER BY Rating DESC")
mejoresAccion.show()

// Apartado 9
// Usando la **API de DataFrames** (no SQL), obtener las películas de la productora *"Warner Bros"* (`Studio`) cuya duración media (`Duration_Min`) sea superior a 120 minutos, y mostrar el resultado final por pantalla (ejemplo):
val warnerMovies = dfMovies.filter($"Studio" === "Warner Bros" && $"Duration_Min" > 120)
warnerMovies.show() 