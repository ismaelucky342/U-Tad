//====================================================================================================//
//                                                                                                    //
//                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        //
//      AEC4 - PRDT                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       //
//                                                        ██║   ██║█████╗██║   ███████║██║  ██║       //
//      created:        21/04/2026  -  21:45:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       //
//      last change:    25/04/2026  -  00:55:42           ╚██████╔╝      ██║   ██║  ██║██████╔╝       //
//                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        //
//                                                                                                    //
//      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             //
//                                                                                                    //
//      Github:                                           https://github.com/ismaelucky342            //
//                                                                                                    //
//====================================================================================================//

import org.apache.spark.sql.{SparkSession, RDD}
import org.apache.spark.sql.functions._

// Creo sesion de Spark
val spark = SparkSession.builder()
  .appName("MovieAnalysis")
  .master("local[*]")
  .config("spark.sql.shuffle.partitions", "4")
  .getOrCreate()

import spark.implicits._

println("\n" + "="*80)
println("ANALISIS DE PELICULAS - AEC4")
println("="*80)

// --- PASO 1: Leo CSV como RDD ---
println("\n[1] Leyendo CSV como RDD...")
val filePath = "/home/nirmata/Documentos/University/U-Tad/3th_Course/Q2/Data_Procesing/Unit_4/AEC4/movies.csv"
val rawRDD = spark.sparkContext.textFile(filePath)
println(s"Particiones: ${rawRDD.getNumPartitions} | Total de lineas: ${rawRDD.count()}")

// --- PASO 2: Transformo con split, map, filter ---
println("\n[2] Transformando - split, map, filter...")
val header = rawRDD.first()
val dataRDD = rawRDD
  .filter(_ != header)
  .map(line => {
    val fields = line.split(",")
    (
      fields(0).toInt,
      fields(1),
      fields(2),
      fields(3).toLong,
      fields(4).toLong,
      fields(5).toInt,
      fields(6),
      fields(7).toDouble,
      fields(8).toDouble,
      fields(9).toInt
    )
  })
  .cache()
println(s"Registros parseados: ${dataRDD.count()}")
dataRDD.take(3).foreach(println)

// --- PASO 3: Convierto a DataFrame ---
println("\n[3] Convirtiendo RDD a DataFrame...")
val dfMovies = dataRDD.toDF(
  "id", "title", "release_date", "budget", "revenue", 
  "runtime", "genre", "vote_average", "popularity", "cast_size"
).cache()
println("OK - DataFrame listo")

// --- PASO 4: Estructura y metadatos ---
println("\n[4] Esquema y datos...")
dfMovies.printSchema()
dfMovies.show(3, truncate = false)
println(s"Total: ${dfMovies.count()} registros | Columnas: ${dfMovies.columns.length}")
println(s"Unicos: ${dfMovies.dropDuplicates().count()}")

// --- PASO 5: Estadisticas basicas ---
println("\n[5] Estadisticas basicas...")
dfMovies.describe("budget", "revenue", "runtime", "vote_average", "popularity", "cast_size").show()

println("\nAnalisis por genero:")
dfMovies.groupBy("genre").agg(
  count("*").as("cantidad"),
  avg("budget").as("budget_prom"),
  avg("revenue").as("revenue_prom"),
  avg("vote_average").as("rating_prom")
).orderBy(desc("cantidad")).show(truncate = false)

println("\nDetectando nulos...")
dfMovies.select(dfMovies.columns.map(col => sum(when(col(col).isNull, 1).otherwise(0)).as(col)): _*).show()

// Metodo extra: cuartiles
println("\nCuartiles de ingresos:")
val q = dfMovies.stat.approxQuantile("revenue", Array(0, 0.25, 0.5, 0.75, 1.0), 0.05)
println(s"Min: $${q(0).toLong} | Q1: $${q(1).toLong} | Med: $${q(2).toLong} | Q3: $${q(3).toLong} | Max: $${q(4).toLong}")

// --- PASO 6: DataFrame → RDD → DataFrame ---
println("\n[6] Convirtiendo DF→RDD→DF...")
val rddFromDF = dfMovies.rdd

println("Peliculas con revenue > 1B:")
val highRevenueRDD = rddFromDF
  .filter(row => row.getAs[Long]("revenue") > 1000000000)
  .map(row => s"${row.getAs[String]("title")} - $${row.getAs[Long]("revenue")/1000000}M")
println(s"Total encontradas: ${highRevenueRDD.count()}")
highRevenueRDD.take(3).foreach(println)

println("\nVolviendo a DataFrame...")
val dfHighBudget = rddFromDF
  .filter(row => row.getAs[Long]("budget") > 150000000)
  .toDF()
println(s"Peliculas con budget > 150M: ${dfHighBudget.count()}")
dfHighBudget.select("title", "budget", "revenue").show(3, truncate = false)

// --- PASO 7: Queries avanzadas ---
println("\n[7] Queries avanzadas...")
dfMovies.createOrReplaceTempView("movies")

// Query 1: Condicionales
println("\nQ1 - Peliculas Accion (budget > 100M && rating > 6.0):")
dfMovies
  .filter(col("genre") === "Action" && col("budget") > 100000000 && col("vote_average") > 6.0)
  .select("title", "budget", "revenue", "vote_average")
  .orderBy(desc("revenue"))
  .show(10, truncate = false)

// Query 2: Agrupacion multiple
println("\n--- QUERY 2: Análisis por Género y Año ---")
dfMovies
  .withColumn("year", year(col("release_date")))
  .groupBy("genre", "year")
  .agg(
    count("*").as("num_peliculas"),
    avg("revenue").as("ingresos_promedio"),
    max("revenue").as("ingresos_max"),
    min("budget").as("presupuesto_minimo")
  )
  .filter(col("num_peliculas") > 2)
  .orderBy(desc("ingresos_promedio"))
  .show(20, truncate = false)

// Query 3: SQL
println("\n--- QUERY 3: Top Géneros por ROI (SQL) ---")
spark.sql("""
  SELECT
    genre,
    COUNT(*) as num_peliculas,
    ROUND(AVG(revenue - budget) / AVG(budget) * 100, 2) as roi_promedio_percent,
    ROUND(AVG(revenue), 0) as ingresos_promedio,
    ROUND(AVG(vote_average), 2) as calificacion_promedio
  FROM movies
  GROUP BY genre
  ORDER BY roi_promedio_percent DESC
""").show(truncate = false)

// Query 4: UDF personalizado
println("\n=== QUERY 4: Clasificación de Películas por Rentabilidad (UDF Personalizado) ===")
val classifyRentability = udf((budget: Long, revenue: Long) => {
  if (budget == 0) "N/A"
  else {
    val roi = (revenue - budget).toDouble / budget
    if (roi > 5.0) "Extremadamente Rentable (ROI > 500%)"
    else if (roi > 2.0) "Muy Rentable (ROI > 200%)"
    else if (roi > 1.0) "Rentable (ROI > 100%)"
    else if (roi > 0.0) "Moderadamente Rentable"
    else "No Rentable (Pérdidas)"
  }
})

val rentabilityAnalysis = dfMovies
  .withColumn("rentability_class", classifyRentability(col("budget"), col("revenue")))
  .groupBy("rentability_class")
  .agg(
    count("*").as("cantidad"),
    round(avg("revenue"), 0).as("ingresos_promedio")
  )
  .orderBy(desc("cantidad"))

println("Distribución de películas por rentabilidad:")
rentabilityAnalysis.show(truncate = false)

// Query 5: UDAF
println("\n=== QUERY 5: Análisis de Popularidad por Género (UDAF) ===")
spark.sql("""
  SELECT
    genre,
    ROUND(AVG(popularity), 2) as popularidad_promedio,
    MAX(popularity) as popularidad_maxima,
    MIN(popularity) as popularidad_minima,
    PERCENTILE_APPROX(popularity, 0.5) as mediana_popularidad,
    COUNT(DISTINCT title) as num_peliculas
  FROM movies
  GROUP BY genre
  ORDER BY popularidad_promedio DESC
""").show(truncate = false)

println("\n" + "="*80)
println("Analisis completado")
println("="*80)
