// ============================================================================
// ANÁLISIS DE PELÍCULAS CON SPARK - PART 1: RDDs y DataFrames
// ============================================================================
// Actividad AEC4: Ejercicio 1 - Análisis con DataFrames y RDDs
// Dataset: Movie Industry (250 películas con 10 columnas)
// ============================================================================

import org.apache.spark.sql.{SparkSession, RDD, Row}
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import scala.io.Source

// ============================================================================
// PASO 1: Inicialización de Spark Session
// ============================================================================
val spark = SparkSession.builder()
  .appName("MovieAnalysis")
  .master("local[*]")
  .config("spark.sql.shuffle.partitions", "4")
  .getOrCreate()

import spark.implicits._

println("\n" + "="*80)
println("ANÁLISIS DE DATOS DE PELÍCULAS - AEC4")
println("="*80)

// ============================================================================
// PASO 2: LECTURA DE DATOS COMO RDD
// ============================================================================
println("\n[PASO 1] Leyendo datos como RDD...")

val filePath = "/home/nirmata/Descargas/movies.csv"
val rawRDD = spark.sparkContext.textFile(filePath)

// Verificar número de particiones y registros
println(s"Número de particiones del RDD: ${rawRDD.getNumPartitions}")
println(s"Total de líneas (incluyendo header): ${rawRDD.count()}")

// ============================================================================
// PASO 3: TRANSFORMACIONES BÁSICAS EN RDD (Split, Map, Filter)
// ============================================================================
println("\n[PASO 2] Aplicando transformaciones RDD...")

// Separar header del resto de datos
val header = rawRDD.first()
println(s"Header: $header")

// Eliminar header y hacer split de cada línea
val dataRDD = rawRDD
  .filter(_ != header)  // Filtrar header
  .map(line => {
    val fields = line.split(",")
    (
      fields(0).toInt,              // id
      fields(1),                     // title
      fields(2),                     // release_date
      fields(3).toLong,              // budget
      fields(4).toLong,              // revenue
      fields(5).toInt,               // runtime
      fields(6),                     // genre
      fields(7).toDouble,            // vote_average
      fields(8).toDouble,            // popularity
      fields(9).toInt                // cast_size
    )
  })
  .cache()  // Cache para reutilizar

// Verificar datos parseados
println(s"Total de registros parseados: ${dataRDD.count()}")
println("Primeros 5 registros del RDD:")
dataRDD.take(5).foreach(println)

// ============================================================================
// PASO 4: CONVERSIÓN DE RDD A DATAFRAME
// ============================================================================
println("\n[PASO 3] Convirtiendo RDD a DataFrame...")

// Convertir RDD a DataFrame usando toDF con nombres de columnas
val dfMovies = dataRDD.toDF(
  "id", "title", "release_date", "budget", "revenue", 
  "runtime", "genre", "vote_average", "popularity", "cast_size"
)
  .cache()

// Alternatively, podríamos usar schema manual (comentado):
/*
val schema = StructType(Array(
  StructField("id", IntegerType, true),
  StructField("title", StringType, true),
  StructField("release_date", StringType, true),
  StructField("budget", LongType, true),
  StructField("revenue", LongType, true),
  StructField("runtime", IntegerType, true),
  StructField("genre", StringType, true),
  StructField("vote_average", DoubleType, true),
  StructField("popularity", DoubleType, true),
  StructField("cast_size", IntegerType, true)
))
val dfMovies = spark.createDataFrame(dataRDD.map(row => 
  Row(row._1, row._2, row._3, row._4, row._5, row._6, row._7, row._8, row._9, row._10)
), schema).cache()
*/

println("✓ DataFrame creado exitosamente")

// ============================================================================
// PASO 5: MOSTRAR ESTRUCTURA DE DATOS Y METADATOS
// ============================================================================
println("\n[PASO 4] Estructura y Metadatos del DataFrame...")
println("\n--- Schema del DataFrame ---")
dfMovies.printSchema()

println(f"\n--- Muestra de Datos (primeros 5 registros) ---")
dfMovies.show(5, truncate = false)

println(f"\n--- Información General ---")
println(s"Total de registros: ${dfMovies.count()}")
println(s"Total de columnas: ${dfMovies.columns.length}")
println(s"Nombres de columnas: ${dfMovies.columns.mkString(", ")}")

println(f"\n--- Registros Distintos ---")
println(s"Registros únicos (por todas las columnas): ${dfMovies.dropDuplicates().count()}")

// ============================================================================
// PASO 6: ANÁLISIS EXPLORATORIO
// ============================================================================
println("\n[PASO 5] Análisis Exploratorio Detallado...")

println("\n--- Estadísticas Básicas (columnas numéricas) ---")
dfMovies.describe("budget", "revenue", "runtime", "vote_average", "popularity", "cast_size").show()

println("\n--- Análisis por Género (usando groupBy y agg) ---")
dfMovies.groupBy("genre").agg(
  count("*").as("cantidad"),
  avg("budget").as("presupuesto_promedio"),
  avg("revenue").as("ingresos_promedio"),
  avg("vote_average").as("calificacion_promedio")
).orderBy(desc("cantidad")).show(truncate = false)

println("\n--- Detección de Valores Nulos ---")
dfMovies.select(dfMovies.columns.map(col => sum(when(col(col).isNull, 1).otherwise(0)).as(col)): _*).show()

// Método adicional NO visto en el material: Quartile Analysis
println("\n--- Análisis de Cuartiles (Método Adicional - Quartile Analysis) ---")
println("Distribución de Ingresos por Cuartiles:")
val revenuePercentiles = dfMovies.stat.approxQuantile("revenue", Array(0, 0.25, 0.5, 0.75, 1.0), 0.05)
println(s"Min: ${revenuePercentiles(0).toLong}")
println(s"Q1 (25%): ${revenuePercentiles(1).toLong}")
println(s"Q2 (50% - Mediana): ${revenuePercentiles(2).toLong}")
println(s"Q3 (75%): ${revenuePercentiles(3).toLong}")
println(s"Max: ${revenuePercentiles(4).toLong}")

println("\n--- Correlación entre variables numéricas ---")
dfMovies.select("budget", "revenue", "vote_average").corr("budget", "revenue").asInstanceOf[Double]
println(s"Correlación Budget-Revenue: ${dfMovies.select("budget", "revenue").corr("budget", "revenue")}")

// ============================================================================
// PASO 7: CONVERSIÓN DE DATAFRAME A RDD Y TRANSFORMACIONES
// ============================================================================
println("\n[PASO 6] Conversión DataFrame → RDD → DataFrame...")

// Convertir DataFrame a RDD
val rddFromDF = dfMovies.rdd
println(s"Tipo de elementos en RDD: ${rddFromDF.first().getClass}")

// Aplicar transformación: Filtrar películas con revenue > 1,000,000,000 y mapear a nuevo formato
println("\n--- Transformación 1: Películas de Alto Presupuesto (> $150M) ---")
val highBudgetRDD = rddFromDF
  .filter(row => row.getAs[Long]("revenue") > 1000000000)  // Revenue > $1B
  .map(row => {
    val title = row.getAs[String]("title")
    val revenue = row.getAs[Long]("revenue")
    val rating = row.getAs[Double]("vote_average")
    s"$title - Revenue: $$${revenue/1000000}M - Rating: $rating"
  })

println(s"Películas con revenue > $1B: ${highBudgetRDD.count()}")
println("Ejemplos:")
highBudgetRDD.take(3).foreach(println)

// Volver a convertir RDD a DataFrame
println("\n--- Conversión de vuelta a DataFrame ---")
val dfHighBudget = rddFromDF
  .filter(row => row.getAs[Long]("budget") > 150000000)
  .toDF()
  .cache()

println(s"Películas con presupuesto > $150M: ${dfHighBudget.count()}")
dfHighBudget.select("title", "budget", "revenue").show(5, truncate = false)

/*
EXPLICACIÓN DE POR QUÉ SE USÓ RDD EN ESTE PUNTO:
- Los RDDs ofrecen más flexibilidad para transformaciones complejas
- Permitió realizar filtrado y transformación de datos en una sola operación
- Los RDDs son más eficientes para operaciones de bajo nivel
- DataFrame proporciona abstracciones de alto nivel más optimizadas
*/

// ============================================================================
// PASO 8: PLANTEAMIENTO DE PROBLEMA Y ANÁLISIS PERSONALIZADO
// ============================================================================
println("\n[PASO 7] Análisis Personalizado - Problema a Resolver...")
println("\n*** PROBLEMA: Identificar películas rentables por género")
println("    ¿Cuáles son los géneros más rentables? ¿Qué películas generan mayor ROI?")

// QUERY 1: Películas por género con filtros (condicionales)
println("\n--- Query 1: Películas de Acción con Budget > $100M y Rating > 6.0 (API DataFrame) ---")
dfMovies
  .filter(col("genre") === "Action" && col("budget") > 100000000 && col("vote_average") > 6.0)
  .select("title", "budget", "revenue", "vote_average")
  .orderBy(desc("revenue"))
  .show(10, truncate = false)

// QUERY 2: Agrupación por dos columnas (género + año de lanzamiento)
println("\n--- Query 2: Análisis por Género y Año de Lanzamiento (Agrupación múltiple) ---")
dfMovies
  .withColumn("year", year(col("release_date")))
  .groupBy("genre", "year")
  .agg(
    count("*").as("num_peliculas"),
    avg("revenue").as("ingresos_promedio"),
    max("revenue").as("ingresos_max"),
    min("budget").as("presupuesto_minimo")
  )
  .filter(col("num_peliculas") > 2)  // Solo años con +2 películas
  .orderBy(desc("ingresos_promedio"))
  .show(20, truncate = false)

// QUERY 3: Utilizando SQL
println("\n--- Query 3: Top 5 Géneros por ROI Promedio (SQL) ---")
dfMovies.createOrReplaceTempView("movies")

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

// QUERY 4: Usando UDF personalizado para clasificar películas por rentabilidad
println("\n--- Query 4: Clasificación de Películas por Rentabilidad (UDF personalizado) ---")

// Definir UDF para clasificar rentabilidad
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

// UDAF: Suma y promedio de ingresos por categoría
val revenueStats = dfMovies
  .withColumn("rentability_class", classifyRentability(col("budget"), col("revenue")))
  .groupBy("rentability_class")
  .agg(
    count("*").as("cantidad"),
    round(avg("revenue"), 0).as("ingresos_promedio"),
    round(sum("revenue"), 0).as("ingresos_totales")
  )
  .orderBy(desc("cantidad"))

println("Distribución de películas por rentabilidad:")
revenueStats.show(truncate = false)

// QUERY 5: UDAF adicional - Análisis de popularidad por género
println("\n--- Query 5: Análisis de Popularidad por Género (UDAF) ---")
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

// ============================================================================
// RESUMEN FINAL
// ============================================================================
println("\n" + "="*80)
println("RESUMEN DEL ANÁLISIS")
println("="*80)

val summary = spark.sql("""
  SELECT 
    'Total de Películas' as Metrica, CAST(COUNT(*) as STRING) as Valor FROM movies
  UNION ALL
  SELECT 'Géneros Únicos', CAST(COUNT(DISTINCT genre) as STRING) FROM movies
  UNION ALL
  SELECT 'Ingresos Totales', CONCAT('$', CAST(ROUND(SUM(revenue)/1000000000, 2) as STRING), 'B')
    FROM movies
  UNION ALL
  SELECT 'Presupuesto Promedio', CONCAT('$', CAST(ROUND(AVG(budget)/1000000, 1) as STRING), 'M')
    FROM movies
  UNION ALL
  SELECT 'Calificación Promedio', CAST(ROUND(AVG(vote_average), 2) as STRING)
    FROM movies
""")

summary.show(truncate = false)

println("\n" + "="*80)
println("✓ Análisis completado exitosamente")
println("="*80)

// ============================================================================
// LIMPIAR RECURSOS
// ============================================================================
// En caso de necesitar cerrar la sesión:
// spark.stop()
