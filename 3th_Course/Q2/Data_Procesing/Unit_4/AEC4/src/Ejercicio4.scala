import org.apache.spark.sql.SparkSession

/**
 * Ejercicio 4 — Exploración inicial de los datos
 *
 * Una vez cargado el DataFrame desde CSV, se usan los métodos principales
 * para inspeccionar su contenido y estructura:
 *   - show()       muestra las primeras N filas
 *   - printSchema() imprime el árbol de tipos
 *   - columns      devuelve los nombres de columnas como Array[String]
 *   - dtypes       devuelve pares (nombre, tipo) como Array[(String, String)]
 *   - describe()   estadísticas descriptivas (count, mean, stddev, min, max)
 *   - count()      número total de filas
 */
object Ejercicio4 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio4 - Exploración inicial")
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

    println("=== Primeras 10 filas ===")
    df.show(10, truncate = false)

    println("=== Esquema del DataFrame ===")
    df.printSchema()

    println(s"Columnas : ${df.columns.mkString(", ")}")
    println(s"Tipos    : ${df.dtypes.map { case (c, t) => s"$c → $t" }.mkString(", ")}")
    println(s"Num filas: ${df.count()}")

    println("=== Estadísticas descriptivas de edad y salario ===")
    df.describe("edad", "salario").show(truncate = false)

    spark.stop()
  }
}
