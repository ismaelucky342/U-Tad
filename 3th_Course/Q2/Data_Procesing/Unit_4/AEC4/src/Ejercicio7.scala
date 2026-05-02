import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.Row
import org.apache.spark.sql.types.{IntegerType, StringType, DoubleType, StructField, StructType}
import org.apache.spark.sql.functions.col

/**
 * Ejercicio 7 — DataFrame → RDD → DataFrame (flujo completo)
 *
 * Aquí hago el ciclo completo:
 *   1. Cargo un DataFrame desde CSV
 *   2. Lo convierto a RDD
 *   3. Aplico una transformación en el RDD
 *   4. Vuelvo a convertir a DataFrame
 *
 * Esto muestra la relación bidireccional entre DataFrames y RDDs.
 *
 * Por qué importa:
 *   - Los RDDs son más "raw" y dan más control
 *   - A veces necesito bajar a RDD para operaciones específicas
 *   - Luego vuelvo a DataFrame para seguir con SQL/API
 */
object Ejercicio7 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio7 - DataFrame → RDD → DataFrame")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    val csvPath = if (args.nonEmpty) args(0) else "data/datos_peliculas.csv"

    // Paso 1: Cargar DataFrame desde CSV
    val dfOriginal = spark.read
      .option("header",      "true")
      .option("sep",         ";")
      .option("inferSchema", "true")
      .option("mode",        "DROPMALFORMED")
      .csv(csvPath)

    println("=== DataFrame original (primeras 10 películas) ===")
    dfOriginal.select("titulo", "ano", "presupuesto", "ingresos")
      .show(10, truncate = false)

    // Paso 2: Convertir a RDD
    val rdd = dfOriginal.rdd

    println("\n=== Información del RDD ===")
    println(f"Número de particiones: ${rdd.getNumPartitions}")
    println(f"Número de registros (RDD): ${rdd.count()}")

    // Paso 3: Transformación en el RDD
    // Voy a calcular si cada película fue rentable (ingresos > presupuesto)
    val rddTransformado = rdd.map { row =>
      val titulo = row.getAs[String]("titulo")
      val presupuesto = row.getAs[Double]("presupuesto")
      val ingresos = row.getAs[Double]("ingresos")
      
      val rentable = if (presupuesto > 0 && ingresos > 0) ingresos > presupuesto else false
      val ganancia = ingresos - presupuesto
      
      // Devolvemos: titulo, presupuesto, ingresos, rentable, ganancia
      (titulo, presupuesto, ingresos, rentable, ganancia)
    }

    println("\n=== Transformación aplicada: Cálculo de rentabilidad ===")
    println("Se ha calculado si cada película fue rentable y la ganancia neta")
    
    rddTransformado.take(5).foreach { case (titulo, presupuesto, ingresos, rentable, ganancia) =>
      val estado = if (rentable) "✓ RENTABLE" else "✗ NO RENTABLE"
      println(f"  $titulo%-40s | Ganancia: $$${ganancia%,.0f} [$estado]")
    }

    // Paso 4: Volver a DataFrame
    // Defino el esquema explícitamente
    val esquema = StructType(Array(
      StructField("titulo",      StringType,  nullable = true),
      StructField("presupuesto", DoubleType,  nullable = true),
      StructField("ingresos",    DoubleType,  nullable = true),
      StructField("rentable",    StringType,  nullable = true),
      StructField("ganancia",    DoubleType,  nullable = true)
    ))

    val rddRows = rddTransformado.map { case (titulo, presupuesto, ingresos, rentable, ganancia) =>
      Row(
        titulo,
        presupuesto,
        ingresos,
        if (rentable) "SÍ" else "NO",
        ganancia
      )
    }

    val dfResultado = spark.createDataFrame(rddRows, esquema)

    println("\n=== DataFrame resultado (primeras 10 películas con rentabilidad) ===")
    dfResultado.show(10, truncate = false)

    // Análisis: ¿Cuántas películas fueron rentables?
    val rentables = dfResultado.filter(col("rentable") === "SÍ").count()
    val noRentables = dfResultado.filter(col("rentable") === "NO").count()
    
    println(f"\n=== Resumen ===")
    println(f"Películas rentables: $rentables")
    println(f"Películas NO rentables: $noRentables")

    spark.stop()
  }
}
