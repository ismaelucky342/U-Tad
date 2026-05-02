import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{avg, col, desc, round}

/**
 * Ejercicio 6 — SQL vs API de Spark (el mismo resultado, dos caminos)
 *
 * Spark es flexible: puedo hacer LO MISMO de dos formas:
 *   1. SQL puro: para los que vienen de MySQL/PostgreSQL
 *   2. API de Spark: para los que prefieren código funcional
 *
 * ¿Cuál es mejor? AMBAS generan exactamente el mismo plan de ejecución.
 * Solo elige la que te resulte más cómoda.
 *
 * Aquí muestro dos queries reales sobre películas:
 *   - Query 1: promedio de ingresos por género
 *   - Query 2: películas baratas pero rentables (presupuesto < 50M, ingresos > 500M)
 */
object Ejercicio6 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio6 - SQL vs API de Spark")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    val csvPath = if (args.nonEmpty) args(0) else "data/datos_peliculas.csv"

    val df = spark.read
      .option("header",      "true")
      .option("sep",         ";")
      .option("inferSchema", "true")
      .option("mode",        "DROPMALFORMED")
      .csv(csvPath)

    // Registro el DataFrame como vista para usar SQL
    df.createGlobalTempView("peliculas")

    println("=" * 60)
    println("QUERY 1: Ingresos promedio por género")
    println("=" * 60)

    // ─────────────────────────────────────────────────────
    // OPCIÓN A: SQL
    // ─────────────────────────────────────────────────────
    
    println("\n--- Versión SQL ---\n")
    
    spark.sql("""
      SELECT 
        genero,
        ROUND(AVG(ingresos), 0) AS ingresos_promedio,
        COUNT(*) AS cantidad
      FROM global_temp.peliculas
      WHERE ingresos > 0
      GROUP BY genero
      ORDER BY ingresos_promedio DESC
    """).show(truncate = false)

    // ─────────────────────────────────────────────────────
    // OPCIÓN B: API de Spark (funcional)
    // ─────────────────────────────────────────────────────
    
    println("--- Versión API de Spark ---\n")
    
    df.filter(col("ingresos") > 0)
      .groupBy("genero")
      .agg(
        round(avg("ingresos"), 0).alias("ingresos_promedio"),
        col("*").count().alias("cantidad")
      )
      .orderBy(desc("ingresos_promedio"))
      .show(truncate = false)

    println("\n" + "=" * 60)
    println("QUERY 2: Películas 'sorpresas' (presupuesto bajo, ingresos altos)")
    println("=" * 60)

    // ─────────────────────────────────────────────────────
    // OPCIÓN A: SQL
    // ─────────────────────────────────────────────────────
    
    println("\n--- Versión SQL ---\n")
    
    spark.sql("""
      SELECT 
        titulo,
        ano,
        genero,
        presupuesto,
        ingresos,
        ROUND((ingresos - presupuesto) / presupuesto, 2) AS roi
      FROM global_temp.peliculas
      WHERE presupuesto > 0 AND presupuesto < 50000000 AND ingresos > 500000000
      ORDER BY roi DESC
    """).show(10, truncate = false)

    // ─────────────────────────────────────────────────────
    // OPCIÓN B: API de Spark
    // ─────────────────────────────────────────────────────
    
    println("--- Versión API de Spark ---\n")
    
    df.filter((col("presupuesto") > 0) && (col("presupuesto") < 50000000) && (col("ingresos") > 500000000))
      .select(
        col("titulo"),
        col("ano"),
        col("genero"),
        col("presupuesto"),
        col("ingresos"),
        round((col("ingresos") - col("presupuesto")) / col("presupuesto"), 2).alias("roi")
      )
      .orderBy(desc("roi"))
      .show(10, truncate = false)

    println("\n" + "=" * 60)
    println("CONCLUSIÓN")
    println("=" * 60)
    println("""
    Ambas versiones:
      ✓ Generan el MISMO plan de ejecución
      ✓ Tienen la MISMA performance
      ✓ El resultado es IDÉNTICO
    
    La diferencia es solo ESTILO. Elige la que:
      - Entiendas mejor
      - Te resulte más cómoda
      - Vaya mejor con el resto de tu código
    """)

    spark.stop()
  }
}
