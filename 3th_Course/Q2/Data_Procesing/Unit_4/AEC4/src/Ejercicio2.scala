import org.apache.spark.sql.{Row, SparkSession}
import org.apache.spark.sql.types.{DoubleType, IntegerType, StringType, StructField, StructType}

/**
 * Ejercicio 2 — Esquema manual con StructType
 *
 * En el Ejercicio 1, Spark adivinaba los tipos. Aquí digo explícitamente:
 * "Esta columna es INT, esa es STRING, aquella DoubleType"
 *
 * ¿Cuándo lo necesito?
 *   - Cuando Spark adivinó mal (vio "123" como String en lugar de Int)
 *   - Cuando quiero asegurar que NO haya nulos en columnas críticas
 *   - Cuando importo datos heterogéneos de múltiples fuentes
 *
 * Después de definir el esquema, creo el DataFrame a partir de Rows.
 */
object Ejercicio2 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio2 - Esquema manual")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    // Mis datos como Rows (filas genéricas)
    val filas = Seq(
      Row(6,  "Avatar 2", 2022, "Sci-Fi", 350000000.0, 2320250281.0, "James Cameron"),
      Row(7,  "Avengers", 2012, "Accion", 220000000.0, 1520595760.0, "Joss Whedon"),
      Row(8,  "Inception", 2010, "Sci-Fi", 160000000.0, 839292587.0, "Christopher Nolan")
    )

    // Aquí defino explícitamente el esquema
    // Cada StructField especifica: nombre, tipo, ¿puede ser nulo?
    val esquema = StructType(Array(
      StructField("id",       IntegerType, nullable = false),  // ID no puede ser nulo
      StructField("titulo",   StringType,  nullable = false),  // Título siempre existe
      StructField("ano",      IntegerType, nullable = false),  // Año siempre existe
      StructField("genero",   StringType,  nullable = false),  // Género siempre existe
      StructField("presupuesto", DoubleType, nullable = true),   // PUEDE ser nulo (no siempre documentado)
      StructField("ingresos", DoubleType, nullable = true),    // PUEDE ser nulo (no siempre documentado)
      StructField("director", StringType, nullable = true)     // Director PUEDE ser nulo
    ))

    // Creo el DataFrame con el esquema explícito
    val dfConEsquema = spark.createDataFrame(
      spark.sparkContext.parallelize(filas),
      esquema
    )

    println("=== DataFrame con esquema manual (StructType) ===")
    dfConEsquema.show(truncate = false)

    println("\n=== Esquema definido manualmente ===")
    println("Fíjate que algunas columnas tienen nullable=false")
    println("Eso significa que Spark rechazará películas sin id o título")
    dfConEsquema.printSchema()

    println("\n✓ Conclusión:")
    println("  - Control total sobre tipos y nulabilidad")
    println("  - Útil cuando necesito restricciones específicas")
    println("  - Evita sorpresas después cuando tengo datos reales")

    spark.stop()
  }
}
