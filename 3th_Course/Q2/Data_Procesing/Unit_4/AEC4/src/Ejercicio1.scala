import org.apache.spark.sql.SparkSession

/**
 * Ejercicio 1 — DataFrame desde una lista de Scala
 *
 * Aquí hago el ejemplo más simple: tengo datos en memoria (una lista de tuplas)
 * y quiero convertirlos en un DataFrame Spark.
 *
 * ¿Por qué empiezo aquí?
 *   - Es lo más básico: sin archivos, sin bases de datos, solo código
 *   - Muestra cómo Spark es flexible: acepta datos de cualquier lado
 *   - Aprendo el patrón: datos → DataFrame → procesamiento
 *
 * Lo importante: `toDF()` con nombres de column, y Spark adivina los tipos
 */
object Ejercicio1 {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Ejercicio1 - DataFrame desde lista")
      .master("local[*]")
      .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    import spark.implicits._

    // Tengo datos en una lista (tuplas)
    // Cada tupla representa una película: id, título, año, género, presupuesto, ingresos, director
    val peliculasLista = Seq(
      (1, "Avatar", 2009, "Sci-Fi", 237000000.0, 2923706994.0, "James Cameron"),
      (2, "Titanic", 1997, "Drama", 200000000.0, 2257843092.0, "James Cameron"),
      (3, "Inception", 2010, "Sci-Fi", 160000000.0, 839292587.0, "Christopher Nolan"),
      (4, "The Dark Knight", 2008, "Accion", 185000000.0, 1005045668.0, "Christopher Nolan"),
      (5, "Interstellar", 2014, "Sci-Fi", 165000000.0, 731200000.0, "Christopher Nolan")
    )

    // Convierto a DataFrame: nombre cada columna explícitamente
    val dfPeliculas = peliculasLista.toDF("id", "titulo", "ano", "genero", "presupuesto", "ingresos", "director")

    println("=== DataFrame creado desde una lista de Scala ===")
    println("Datos cargados:")
    dfPeliculas.show(truncate = false)

    println("\n=== Esquema (tipos de datos) ===")
    println("Spark infirió automáticamente los tipos:")
    dfPeliculas.printSchema()

    println("\n✓ Conclusión:")
    println("  - Tenía tuplas, ahora tengo un DataFrame que puedo procesar con Spark")
    println("  - Los tipos se detectan solos: Int, String, Double")
    println("  - Puedo hacer cualquier operación SQL/API sobre esto")

    spark.stop()
  }
}
