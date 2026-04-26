import org.apache.spark.sql.SparkSession

/**
 * Ejercicio 1 — Creación de un DataFrame desde una lista de datos en Scala
 *
 * Se define una secuencia de tuplas con datos de empleados y se convierte
 * en un DataFrame usando toDF(). Se imprimen el contenido y el esquema
 * inferido automáticamente por Spark.
 */
object Ejercicio1 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio1 - DataFrame desde lista")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    import spark.implicits._

    // Secuencia de tuplas: (id, nombre, edad, departamento, salario)
    val empleadosLista = Seq(
      (1, "Ana",    29, "Ventas",    42000.0),
      (2, "Pedro",  34, "Marketing", 39000.0),
      (3, "Lucía",  27, "IT",        54000.0),
      (4, "Miguel", 41, "Finanzas",  61000.0),
      (5, "Sara",   31, "Ventas",    47000.0)
    )

    // Conversión a DataFrame con nombre de columnas explícito
    val dfEmpleados = empleadosLista.toDF("id", "nombre", "edad", "departamento", "salario")

    println("=== DataFrame creado desde una lista de Scala ===")
    dfEmpleados.show(truncate = false)

    println("=== Esquema inferido por Spark ===")
    dfEmpleados.printSchema()

    spark.stop()
  }
}
