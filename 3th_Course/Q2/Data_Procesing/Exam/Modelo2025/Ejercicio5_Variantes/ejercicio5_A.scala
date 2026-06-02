//## EJERCICIO 5 — Spark SQL + HDFS (2 puntos)
//
//**Enunciado general:**
//Vamos a trabajar con Spark SQL utilizando el dataset `dogs_breeds.csv` (sobre razas de perros) para realizar una serie de consultas. Para la entrega, es necesario generar un fichero con las sentencias utilizadas y adjuntar las capturas de pantalla de la ejecución.
//
//### Apartados del ejercicio
//
//* **Apartado 1 (0,1 pts):** Descargar el fichero `dogs_breeds.csv` y explorar su contenido en el sistema local (por ejemplo, utilizando el comando `head`).
//* **Apartado 2 (0,2 pts):** Arrancar el sistema de archivos distribuido HDFS y copiar el fichero `dogs_breeds.csv` desde el entorno local a la ruta `/data/breeds/` de HDFS.
//* **Apartado 3 (0,1 pts):** Comprobar mediante un comando nativo de `hdfs` que el fichero se ha creado correctamente en la ruta solicitada.
//* **Apartado 4 (0,2 pts):** Arrancar Spark y leer el fichero `dogs_breeds.csv` desde HDFS para almacenarlo en una variable de tipo RDD llamada `DogsRDD`.
//* *Nota:* La ruta del archivo es `hdfs://localhost:9000/data/breeds/dogs_breeds.csv` y el archivo contiene una línea de cabecera.
//
//
//* **Apartado 5 (0,4 pts):** Utilizando exclusivamente el RDD creado (`DogsRDD`) junto con sus transformaciones y acciones, responde a la siguiente pregunta: **¿cuántas razas hay por cada tamaño de perro?**
//* *Resultado esperado a obtener:*
//```text
//(Very Large,207)
//(Medium,79)
//(Large,65)
//(Very Small,5)
//(Small,35)
//
//```
//
//* **Apartado 6 (0,2 pts):** Cargar el mismo archivo CSV desde HDFS pero esta vez como un **DataFrame** (en una variable llamada `dfDogs`), configurándolo para que infiera automáticamente el tipo de datos y utilice la primera fila como cabecera.
//* **Apartado 7 (0,1 pts):** Registrar el DataFrame `dfDogs` como una tabla o vista temporal para poder realizar consultas SQL sobre ella. La tabla debe llamarse `breeds`.
//* **Apartado 8 (0,4 pts):** Ejecutar una **consulta SQL** (usando la tabla temporal `breeds`) para obtener las razas de tamaño pequeño (`Dog_Size = 'Small'`) que tengan un nivel de inteligencia mayor o igual a 4 ($\ge 4$). El resultado debe ordenarse por el nivel de inteligencia de forma descendente, guardarse en una variable llamada `inteligentesPequenos` y mostrarse por pantalla.
//* **Apartado 9 (0,3 pts):** Utilizando la **API de DataFrames** (no sentencias de texto SQL), obtener las razas pertenecientes al grupo de perros *"Hound Dogs"* cuyo peso medio sea superior a 25 kg. Muestra el resultado final por pantalla.
//


// Resolución del ejercicio:

// Apartado 1
// Descargar el fichero `dogs_breeds.csv` y explorar su contenido en el sistema local (por ejemplo, utilizando el comando `head`).
// Comando para descargar el fichero (ejemplo):
// wget https://example.com/dogs_breeds.csv
// Comando para explorar el contenido del fichero:
// head dogs_breeds.csv


// Apartado 2

// Arrancar el sistema de archivos distribuido HDFS y copiar el fichero `dogs_breeds.csv` desde el entorno local a la ruta `/data/breeds/` de HDFS.
// Comando para arrancar HDFS (ejemplo):
// start-dfs.sh
// Comando para copiar el fichero a HDFS:
// hdfs dfs -mkdir -p /data/breeds
// hdfs dfs -put dogs_breeds.csv /data/breeds/

// Apartado 3
// Comprobar mediante un comando nativo de `hdfs` que el fichero se ha creado correctamente en la ruta solicitada.
// Comando para comprobar la existencia del fichero en HDFS:
// hdfs dfs -ls /data/breeds/  
// Comando para mostrar el contenido del fichero en HDFS (opcional):
// hdfs dfs -cat /data/breeds/dogs_breeds.csv | head

// Apartado 4
// Arrancar Spark y leer el fichero `dogs_breeds.csv` desde HDFS para almacenarlo en una variable de tipo RDD llamada `DogsRDD`.
// Comando para arrancar Spark (ejemplo):
// spark-shell
// Comando para leer el fichero desde HDFS y almacenarlo en un RDD:
val DogsRDD = sc.textFile("hdfs://localhost:9000/data/breeds/dogs_breeds.csv")

// Apartado 5
// Utilizando exclusivamente el RDD creado (`DogsRDD`) junto con sus transformaciones y acciones, responde a la siguiente pregunta: **¿cuántas razas hay por cada tamaño de perro?**
// Comando para contar las razas por tamaño de perro:
val header = DogsRDD.first() // Obtener la cabecera
val breedsCount = DogsRDD
  .filter(line => line != header) // Filtrar la cabecera
  .map(line => line.split(",")(2)) // Suponiendo que el tamaño del perro está en la tercera columna (índice 2)
  .map(size => (size, 1)) // Crear tuplas (tamaño, 1)
  .reduceByKey(_ + _) // Sumar las tuplas por tamaño
breedsCount.collect().foreach(println)  

// Apartado 6
// Cargar el mismo archivo CSV desde HDFS pero esta vez como un **DataFrame** (en una variable llamada `dfDogs`), configurándolo para que infiera automáticamente el tipo de datos y utilice la primera fila como cabecera.
// Comando para cargar el archivo CSV como DataFrame:
val dfDogs = spark.read     
  .option("header", "true") // Indicar que la primera fila es la cabecera
  .option("inferSchema", "true") // Inferir automáticamente el tipo de datos
  .csv("hdfs://localhost:9000/data/breeds/dogs_breeds.csv")

// Apartado 7
// Registrar el DataFrame `dfDogs` como una tabla o vista temporal para poder realizar consultas SQL sobre ella. La tabla debe llamarse `breeds`.
// Comando para registrar el DataFrame como tabla temporal:
dfDogs.createOrReplaceTempView("breeds")

// Apartado 8
// Ejecutar una **consulta SQL** (usando la tabla temporal `breeds`) para obtener las razas de tamaño pequeño (`Dog_Size = 'Small'`) que tengan un nivel de inteligencia mayor o igual a 4 ($\ge 4$). El resultado debe ordenarse por el nivel de inteligencia de forma descendente, guardarse en una variable llamada `inteligentesPe  quenos` y mostrarse por pantalla.
// Comando para ejecutar la consulta SQL:
val inteligentesPequenos = spark.sql("""
  SELECT *
  FROM breeds   
  WHERE Dog_Size = 'Small' AND Intelligence_Level >= 4
  ORDER BY Intelligence_Level DESC
""")
inteligentesPequenos.show()

// Apartado 9
// Utilizando la **API de DataFrames** (no sentencias de texto SQL), obtener las razas pertenecientes al grupo de perros *"Hound Dogs"* cuyo peso medio sea superior a 25 kg. Muestra el resultado final por pantalla.
// Comando para obtener las razas  pertenecientes al grupo "Hound Dogs" con peso medio superior a 25 kg utilizando la API de DataFrames:
val houndDogs = dfDogs
  .filter($"Group" === "Hound Dogs" && $"Average_Weight" > 25) // Suponiendo que el peso medio está en la columna "Average_Weight"          
houndDogs.show()

