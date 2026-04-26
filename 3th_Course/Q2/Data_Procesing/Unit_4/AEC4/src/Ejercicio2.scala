import org.apache.spark.sql.{Row, SparkSession}
import org.apache.spark.sql.types.{DoubleType, IntegerType, StringType, StructField, StructType}

/**
 * Ejercicio 2 — Creación de un DataFrame con esquema estructurado manual
 *
 * En lugar de dejar que Spark infiera los tipos, se define explícitamente
 * el esquema usando StructType y StructField. Esto da control total sobre
 * los tipos de datos y la nullabilidad de cada columna.
 */
object Ejercicio2 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio2 - DataFrame con esquema manual")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    // Filas de datos como objetos Row
    val filas = Seq(
      Row(6,  "Raúl",  36, "IT",        57000.0),
      Row(7,  "Clara", 28, "Marketing", 43000.0),
      Row(8,  "Nuria", 38, "Finanzas",  62000.0)
    )

    // Definición explícita del esquema con tipos y nullabilidad
    val esquema = StructType(Array(
      StructField("id",           IntegerType, nullable = false),
      StructField("nombre",       StringType,  nullable = false),
      StructField("edad",         IntegerType, nullable = false),
      StructField("departamento", StringType,  nullable = false),
      StructField("salario",      DoubleType,  nullable = false)
    ))

    // Creación del DataFrame a partir del RDD de filas y el esquema
    val dfConEsquema = spark.createDataFrame(
      spark.sparkContext.parallelize(filas),
      esquema
    )

    println("=== DataFrame creado con esquema manual ===")
    dfConEsquema.show(truncate = false)

    println("=== Esquema definido manualmente ===")
    dfConEsquema.printSchema()

    spark.stop()
  }
}
