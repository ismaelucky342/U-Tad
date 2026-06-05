// =================================================================================================== //
//                                                                                                     //
//                                                       ██╗   ██╗   ████████╗ █████╗ ██████╗          //
//     Procesamiento de datos - Examen Final             ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗         //
//                                                       ██║   ██║█████╗██║   ███████║██║  ██║         //
//     created:        05/06/2026  -  9:10:00            ██║   ██║╚════╝██║   ██╔══██║██║  ██║         //
//     last change:    05/06/2026  -  10:58:00           ╚██████╔╝      ██║   ██║  ██║██████╔╝         //
//                                                        ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝          //
//                                                                                                     //
//     Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com               //
//                                                                                                     // 
//     Github:                                           https://github.com/ismaelucky342              // 
//                                                                                                     // 
// =================================================================================================== // 

/*
 *Vamos a trabajar con Spark SQL utilizando el dataset earthquakes_2023.csv, que contiene información sobre terremotos registrados en el año 2023.

El objetivo del ejercicio es cargar el fichero en HDFS, leerlo desde Spark, registrarlo como tabla temporal y realizar varias consultas sencillas utilizando principalmente Spark SQL.

Se pide entregar un fichero con las sentencias utilizadas y capturas de la ejecución.
 *
 * */


// hacer un head a earthquakes_2023.csv 
//
// head earthquakes_2023.csv

// arranque de hdfs y copia de  earthquakes_2023.csv a /data/earthquakes 

// start-dfs.sh
// hdfs dfs -mkdir -p /data/earthquakes
// hdfs dfs -put earthquakes_2023.csv /data/earthquakes

// comprobacion
// hdfs dfs -ls /data/earthquakes

// spark cargar desde hdfs en data frame 

import org.apache.spark.sql.SparkSession

// inicio spark session
val spark = SparkSession
  .builder()
  .appName("Earthquakes")
  .getOrCreate()

// cargo el data frame
val dfEarthquakes = spark.read
  .format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("hdfs://localhost:9000/data/earthquakes/earthquakes_2023.csv")

// compruebo
println("=== DATOS ORIGINALES ===")
dfEarthquakes.show()

// muestro la estrucutra, nombre de columnas y tipo de dato 
println("=== ESTRUCTURA DEL DATAFRAME ===")
dfEarthquakes.printSchema()

// 5 primeras filas sin truncar columnas 
dfEarthquakes.show(5, false)

// ponemos el data frame como tambla temporal earthquakestab

dfEarthquakes.createOrReplaceTempView("earthquakestab")

// comprobacion mediante consulta sql mostrando las 5 primeras filas sin truncar 
spark.sql("SELECT * FROM earthquakestab").show(5, false)


