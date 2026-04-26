import org.apache.spark.sql.SparkSession

/**
 * Ejercicio 5 — Conversión entre DataFrame y RDD
 *
 * Un DataFrame puede convertirse en un RDD de objetos Row mediante .rdd.
 * A continuación se aplica .map() para extraer los campos de cada fila
 * y transformarlos en tuplas tipadas, más convenientes para operaciones
 * funcionales sobre RDDs.
 *
 * Este flujo es útil cuando se necesita usar la API de bajo nivel de Spark
 * (transformaciones funcionales, acceso a particiones, etc.).
 */
object Ejercicio5 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio5 - Conversión DataFrame a RDD")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    val csvPath = if (args.nonEmpty) args(0) else "data/datos_empleados.csv"

    val df = spark.read
      .option("header",      "true")
      .option("sep",         ";")
      .option("inferSchema", "true")
      .option("mode",        "DROPMALFORMED")
      .csv(csvPath)

    // Conversión a RDD de tuplas (id, nombre, departamento, salario)
    val rddEmpleados = df.rdd.map(row => (
      row.getAs[Int]("id"),
      row.getAs[String]("nombre"),
      row.getAs[String]("departamento"),
      row.getAs[Double]("salario")
    ))

    println("=== RDD obtenido desde el DataFrame ===")
    rddEmpleados.collect().foreach { case (id, nombre, depto, salario) =>
      println(f"  id=$id%-3d  nombre=$nombre%-10s  depto=$depto%-12s  salario=$salario%.2f")
    }

    println(s"\nNúmero de particiones del RDD: ${rddEmpleados.getNumPartitions}")

    spark.stop()
  }
}
