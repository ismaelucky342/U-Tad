import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{avg, col, desc, round}

/**
 * Ejercicio 6 — Consultas sobre los datos con SQL y con la API de Spark
 *
 * Se realizan dos consultas equivalentes de dos formas distintas:
 *
 *   1. Usando spark.sql() sobre una vista global temporal creada con
 *      createGlobalTempView(). La vista es accesible desde cualquier
 *      SparkSession del mismo contexto con el prefijo "global_temp.".
 *
 *   2. Usando la API funcional de Spark (groupBy, agg, filter, select,
 *      orderBy) directamente sobre el DataFrame, sin SQL.
 *
 * Las dos consultas que se realizan son:
 *   - Salario medio por departamento (orden descendente)
 *   - Empleados con salario superior a 45 000 (orden descendente)
 */
object Ejercicio6 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio6 - Consultas SQL y API de Spark")
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

    // Registro de la vista global temporal
    df.createGlobalTempView("empleados")

    // ── Consultas con spark.sql() ─────────────────────────────────────────

    println("=== SQL: salario medio por departamento ===")
    spark.sql(
      """SELECT   departamento,
        |         ROUND(AVG(salario), 2) AS salario_medio
        |FROM     global_temp.empleados
        |GROUP BY departamento
        |ORDER BY salario_medio DESC""".stripMargin
    ).show(truncate = false)

    println("=== SQL: empleados con salario > 45 000 ===")
    spark.sql(
      """SELECT nombre, departamento, salario
        |FROM   global_temp.empleados
        |WHERE  salario > 45000
        |ORDER BY salario DESC""".stripMargin
    ).show(truncate = false)

    // ── Mismas consultas con la API de Spark ──────────────────────────────

    println("=== API de Spark: salario medio por departamento ===")
    df.groupBy("departamento")
      .agg(round(avg("salario"), 2).alias("salario_medio"))
      .orderBy(desc("salario_medio"))
      .show(truncate = false)

    println("=== API de Spark: empleados con salario > 45 000 ===")
    df.filter(col("salario") > 45000)
      .select("nombre", "departamento", "salario")
      .orderBy(desc("salario"))
      .show(truncate = false)

    spark.stop()
  }
}
