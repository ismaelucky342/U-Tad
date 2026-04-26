import org.apache.spark.sql.SparkSession

/**
 * Ejercicio 3 — Lectura de datos desde un archivo CSV con configuraciones
 *
 * Se utiliza spark.read con varias opciones:
 *   - header:      la primera fila contiene los nombres de columna
 *   - sep:         el delimitador es punto y coma (;)
 *   - inferSchema: Spark deduce los tipos de datos automáticamente
 *   - mode:        DROPMALFORMED descarta filas con formato incorrecto
 *
 * La ruta del CSV puede pasarse como argumento o usa la ruta por defecto.
 */
object Ejercicio3 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio3 - Lectura CSV")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    val csvPath = if (args.nonEmpty) args(0) else "data/datos_empleados.csv"

    val dfCsv = spark.read
      .option("header",      "true")
      .option("sep",         ";")
      .option("inferSchema", "true")
      .option("mode",        "DROPMALFORMED")
      .csv(csvPath)

    println("=== DataFrame leído desde CSV ===")
    dfCsv.show(truncate = false)

    println("=== Esquema inferido desde el CSV ===")
    dfCsv.printSchema()

    println(s"Columnas: ${dfCsv.columns.mkString(", ")}")
    println(s"Tipos   : ${dfCsv.dtypes.map { case (c, t) => s"$c → $t" }.mkString(", ")}")

    spark.stop()
  }
}
