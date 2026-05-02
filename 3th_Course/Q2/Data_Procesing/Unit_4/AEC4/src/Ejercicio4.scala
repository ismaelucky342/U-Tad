import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.{col, count, when}

/**
 * Ejercicio 4 — Exploración inicial de los datos
 *
 * Una vez cargado el DataFrame desde CSV, lo primero es MIRARLO:
 * ¿Cuántas filas hay? ¿Qué tipos de datos? ¿Hay nulos?
 *
 * Métodos principales:
 *   - show()       muestra las primeras N filas
 *   - printSchema() imprime el árbol de tipos
 *   - columns      devuelve los nombres de columnas
 *   - dtypes       devuelve pares (nombre, tipo)
 *   - describe()   estadísticas (count, mean, stddev, min, max)
 *   - count()      número total de filas
 *   - isNull()     detecta valores nulos
 */
object Ejercicio4 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio4 - Exploración inicial")
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

    println("=== Primeras 10 películas ===")
    df.show(10, truncate = false)

    println("\n=== Esquema del DataFrame ===")
    df.printSchema()

    println(f"\nColumnas: ${df.columns.mkString(", ")}")
    println(f"Tipos    : ${df.dtypes.map { case (c, t) => s"$c → $t" }.mkString(", ")}")
    println(f"Total de registros: ${df.count()}")

    println("\n=== Estadísticas descriptivas de columnas numéricas ===")
    df.describe("ano", "presupuesto", "ingresos").show(truncate = false)

    // Aquí es donde entra lo NUEVO: detectar valores nulos
    println("\n=== Detección de valores nulos por columna ===")
    println("¿Cuántos valores nulos hay en cada columna?")
    
    df.select(df.columns.map(c => count(when(col(c).isNull, 1)).alias(s"nulos_$c")): _*)
      .collect()
      .head
      .getValuesMap[Long](df.columns.map(c => s"nulos_$c"))
      .foreach { case (columna, cantidad) =>
        val porcentaje = (cantidad.toDouble / df.count()) * 100
        println(f"  $columna%-20s: $cantidad registros nulos (${porcentaje}%.2f%%)")
      }

    // También podemos ver qué películas tienen presupuesto faltante
    println("\n=== Películas con datos incompletos (sin presupuesto o ingresos) ===")
    val incompletas = df.filter(col("presupuesto").isNull || col("ingresos").isNull)
    println(f"Total de películas incompletas: ${incompletas.count()}")
    incompletas.select("titulo", "ano", "presupuesto", "ingresos")
      .show(5, truncate = false)

    spark.stop()
  }
}
