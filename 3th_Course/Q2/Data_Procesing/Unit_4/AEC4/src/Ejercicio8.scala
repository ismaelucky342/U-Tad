import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{
  udf, col, avg, count, desc, round, when, lit
}

/**
 * Ejercicio 8 — Problema analítico con UDF y groupBy avanzado
 *
 * PROBLEMA REAL:
 * "¿Cuáles son los géneros más rentables en años recientes?
 *  ¿Qué combinación de género+año tiene mejor ROI?"
 *
 * Esto demuestra:
 *   ✓ UDF (User Defined Function) para cálculos personalizados
 *   ✓ Condicionales con .filter()
 *   ✓ GroupBy por múltiples columnas
 *   ✓ Queries con SQL vs API
 *   ✓ Análisis exploratorio real
 */
object Ejercicio8 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio8 - Análisis con UDF y groupBy")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    import spark.implicits._

    val csvPath = if (args.nonEmpty) args(0) else "data/datos_peliculas.csv"

    val df = spark.read
      .option("header",      "true")
      .option("sep",         ";")
      .option("inferSchema", "true")
      .option("mode",        "DROPMALFORMED")
      .csv(csvPath)

    // ─────────────────────────────────────────────────────────
    // PASO 1: Definir UDF para calcular ROI (Return on Investment)
    // ─────────────────────────────────────────────────────────
    
    val calcularROI = udf { (ingresos: Double, presupuesto: Double) =>
      if (presupuesto > 0 && ingresos > 0) {
        ((ingresos - presupuesto) / presupuesto) * 100
      } else {
        0.0
      }
    }

    // Añadimos la columna ROI al DataFrame
    val dfConROI = df.withColumn("roi", calcularROI(col("ingresos"), col("presupuesto")))

    println("=== Datos con ROI calculado ===")
    dfConROI.select("titulo", "genero", "ano", "presupuesto", "ingresos", "roi")
      .filter(col("roi") > 0)
      .orderBy(desc("roi"))
      .show(5, truncate = false)

    // ─────────────────────────────────────────────────────────
    // PASO 2: Filtrar películas de años recientes (2015+)
    // ─────────────────────────────────────────────────────────
    
    val dfRecientes = dfConROI.filter(col("ano") >= 2015)

    println("\n=== Películas recientes (2015 en adelante) ===")
    println(f"Total de películas recientes: ${dfRecientes.count()}")

    // ─────────────────────────────────────────────────────────
    // PASO 3: QUERY CON API DE SPARK
    // GroupBy: género Y año (múltiples columnas)
    // ─────────────────────────────────────────────────────────
    
    println("\n=== CONSULTA 1: API de Spark ===")
    println("Rentabilidad promedio por género Y año (películas recientes)")
    println("(Solo años con 2+ películas)")
    
    val resultadoAPI = dfRecientes
      .groupBy("genero", "ano")
      .agg(
        round(avg("roi"), 2).alias("roi_promedio"),
        count("*").alias("cantidad"),
        round(avg("presupuesto"), 0).alias("presupuesto_medio")
      )
      .filter(col("cantidad") >= 2)  // Solo grupos con 2+ películas
      .orderBy(desc("roi_promedio"))

    resultadoAPI.show(15, truncate = false)

    // ─────────────────────────────────────────────────────────
    // PASO 4: Registrar como vista temporal y QUERY CON SQL
    // ─────────────────────────────────────────────────────────
    
    dfRecientes.createGlobalTempView("peliculas_recientes")

    println("\n=== CONSULTA 2: SQL ===")
    println("Mejor ROI promedio por género (últimos 3 años)")
    
    val resultadoSQL = spark.sql("""
      SELECT 
        genero,
        MAX(ano) AS ano_maximo,
        ROUND(AVG(roi), 2) AS roi_promedio,
        COUNT(*) AS cantidad_peliculas,
        ROUND(AVG(presupuesto), 0) AS presupuesto_medio
      FROM global_temp.peliculas_recientes
      WHERE ano >= 2021
      GROUP BY genero
      ORDER BY roi_promedio DESC
    """)

    resultadoSQL.show(10, truncate = false)

    // ─────────────────────────────────────────────────────────
    // PASO 5: UDAF (User Defined Aggregate Function) personalizado
    // Para contar películas rentables por género
    // ─────────────────────────────────────────────────────────
    
    println("\n=== ANÁLISIS ADICIONAL: Películas rentables por género ===")
    
    val peliculasRentables = dfConROI
      .filter(col("roi") > 50)  // Considero rentable si ROI > 50%
      .groupBy("genero")
      .agg(
        count("*").alias("rentables_50plus"),
        round(avg("roi"), 2).alias("roi_promedio_alto")
      )
      .orderBy(desc("rentables_50plus"))

    peliculasRentables.show(10, truncate = false)

    // ─────────────────────────────────────────────────────────
    // Sección final: Interpretación de resultados
    // ─────────────────────────────────────────────────────────
    
    println("\n=== CONCLUSIONES ===")
    println("1. ¿Qué géneros son más rentables?")
    println("   → Ver tabla de ROI promedio por género y año")
    println("")
    println("2. ¿Cuántas películas alcanzan ROI > 50%?")
    println("   → Ver tabla de 'Películas rentables por género'")
    println("")
    println("3. ¿Tendencia por años?")
    println("   → Los años recientes muestran cambios en rentabilidad")

    spark.stop()
  }
}
