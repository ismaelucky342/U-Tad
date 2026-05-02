import org.apache.spark.sql.SparkSession

/**
 * Ejercicio 3 — Leer un CSV del mundo real
 *
 * Aquí es donde empieza lo "real": tengo un archivo CSV en mi disco
 * y necesito cargarlo. El CSV tiene delimitadores, headers, etc.
 *
 * Spark.read es mi navaja suiza:
 *   - .option("header", "true")      → Primera línea son nombres de columnas
 *   - .option("sep", ";")            → El delimitador es punto y coma (NO coma)
 *   - .option("inferSchema", "true") → Spark adivina los tipos
 *   - .option("mode", "DROPMALFORMED") → Si una línea está rota, ignorarla
 *
 * La ruta puede pasarse como argumento o usar una por defecto
 */
object Ejercicio3 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio3 - Lectura CSV")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    // Ruta del CSV (puede pasarse como argumento)
    val csvPath = if (args.nonEmpty) args(0) else "data/datos_peliculas.csv"

    println(f"Leyendo CSV desde: $csvPath\n")

    // Configurar spark.read con las opciones necesarias
    val dfCsv = spark.read
      .option("header",      "true")          // Primera fila = nombres de columna
      .option("sep",         ";")             // Delimitador es punto y coma
      .option("inferSchema", "true")          // Spark deduce tipos
      .option("mode",        "DROPMALFORMED") // Descartar líneas malformadas
      .csv(csvPath)

    println("✓ CSV cargado exitosamente\n")

    println("=== Primeras 5 películas ===")
    dfCsv.show(5, truncate = false)

    println("\n=== Esquema inferido automáticamente ===")
    dfCsv.printSchema()

    println(f"\nNombres de columnas: ${dfCsv.columns.mkString(", ")}")
    
    println("\nTipos de datos:")
    dfCsv.dtypes.foreach { case (columnaNombre, tipoSpark) =>
      println(f"  $columnaNombre → $tipoSpark")
    }

    println(f"\n✓ Total de películas cargadas: ${dfCsv.count()}")

    spark.stop()
  }
}
