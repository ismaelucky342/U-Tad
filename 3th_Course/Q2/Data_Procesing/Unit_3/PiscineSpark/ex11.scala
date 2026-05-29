/*
 * EX11 - SparkSession vs SparkContext
 *
 * OBJETIVO:
 * - Entender SparkSession (v2.0+)
 * - Transición de SparkContext a SparkSession
 * - Ventajas: DataFrames, SQL, mejor abstracción
 *
 * ENUNCIADO:
 *
 * 1. Crea un SparkSession (unificado)
 *
 * 2. Crea datos con:
 *    - sparkContext (RDD)
 *    - DataFrame (SQL)
 *
 * 3. Convierte RDD <-> DataFrame
 *
 * 4. Usa Spark SQL sobre los datos
 *
 * 5. Compara rendimiento RDD vs DataFrame
 *
 * CONCEPTOS:
 * - SparkSession: punto de entrada unificado (v2.0+)
 * - sparkContext: aún disponible dentro de SparkSession
 * - DataFrame: abstracción sobre RDD (optimizado)
 * - SQL: queries directo
 * - Catalyst optimizer: optimizaciones automáticas
 *
 */

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.Row
import org.apache.spark.sql.types._

object EjercicioSpark11 {
  def main(args: Array[String]): Unit = {
    
    // 1. Crear SparkSession (unificado)
    val spark = SparkSession.builder()
      .appName("EjercicioSpark11")
      .master("local[*]")
      .getOrCreate()

    println("=== SPARKSESSION vs SPARKCONTEXT ===\n")

    // Acceso a SparkContext desde SparkSession
    val sc = spark.sparkContext
    println(s"SparkContext desde SparkSession: $sc")
    println(s"SparkSession: $spark\n")

    // 2. Crear datos de ejemplo
    val estudiantes = spark.sparkContext.parallelize(List(
      ("Ana", 20, 7.5),
      ("Luis", 22, 4.0),
      ("Marta", 19, 8.2),
      ("Carlos", 21, 6.8),
      ("Lucia", 20, 9.1)
    ))

    // 3. Convertir RDD a DataFrame
    val estudiantesDF = spark.createDataFrame(estudiantes)
      .toDF("nombre", "edad", "nota")

    println("DataFrame creado:")
    estudiantesDF.show()

    println("\nEsquema del DataFrame:")
    estudiantesDF.printSchema()

    // 4. Usar SQL sobre el DataFrame
    estudiantesDF.createOrReplaceTempView("estudiantes")

    println("\nConsulta SQL: SELECT * WHERE nota >= 5")
    val aprobados = spark.sql("SELECT * FROM estudiantes WHERE nota >= 5.0")
    aprobados.show()

    println("\nConsulta SQL: Promedio de notas por edad")
    spark.sql("""
      SELECT edad, AVG(nota) as promedio_nota
      FROM estudiantes
      GROUP BY edad
      ORDER BY promedio_nota DESC
    """).show()

    // 5. Operaciones con DataFrame
    println("\nOperaciones con DataFrame API:")
    
    import spark.implicits._

    estudiantesDF
      .filter($"nota" >= 5.0)
      .select($"nombre", $"nota")
      .orderBy($"nota".desc)
      .show()

    // Conversión de vuelta a RDD
    println("\nConversión DataFrame -> RDD:")
    val rddDeVuelta = estudiantesDF.rdd
      .map { case Row(nombre: String, edad: Int, nota: Double) =>
        s"$nombre ($edad años): $nota"
      }
      .collect()
      .foreach(println)

    // Performance comparison (conceptual)
    println("\n=== DIFERENCIAS ===")
    println("RDD:")
    println("  - API de bajo nivel")
    println("  - Transformaciones funcionales")
    println("  - Sin optimizaciones automáticas")
    println("\nDataFrame:")
    println("  - API de alto nivel")
    println("  - Schema definido")
    println("  - Catalyst optimizations automáticas")
    println("  - SQL queries nativas")
    println("  - Mejor rendimiento para datos estructurados")

    spark.stop()
  }
}
