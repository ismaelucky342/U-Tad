/*
 * EX07 - saveAsTextFile y I/O
 *
 * OBJETIVO:
 * - Guardar RDDs a disco/HDFS
 * - Entender saveAsTextFile como acción
 * - Practicar lectura/escritura de datos
 *
 * ENUNCIADO:
 *
 * 1. Crea un Pair RDD con datos de estudiantes:
 *    (nombre, calificación)
 *
 * 2. Filtra aprobados (>=5)
 *
 * 3. Ordena por calificación descendente
 *
 * 4. Guarda en archivo: /tmp/aprobados.txt
 *
 * 5. Lee el archivo de vuelta y verifica
 *
 * CONCEPTOS:
 * - saveAsTextFile(): acción que escribe en archivos (HDFS, local, S3, etc.)
 * - textFile(): carga un archivo de texto como RDD
 * - Crea un directorio con múltiples archivos (one per partition)
 *
 */

import org.apache.spark.{SparkConf, SparkContext}
import scala.io.Source

object EjercicioSpark07 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark07").setMaster("local[*]")
    val sc = new SparkContext(conf)

    // 1. Pair RDD con estudiantes
    val estudiantes = sc.parallelize(List(
      ("Ana", 7.5),
      ("Luis", 4.0),
      ("Marta", 8.2),
      ("Carlos", 6.8),
      ("Lucia", 9.1),
      ("Pedro", 3.5),
      ("Sofia", 5.5)
    ))

    // 2. Filtra aprobados
    val aprobados = estudiantes.filter { case (_, calif) => calif >= 5 }

    // 3. Ordena por calificación descendente
    val ordenado = aprobados.sortBy(_._2, ascending = false)

    // 4. Mapea a formato legible y guarda
    val formateado = ordenado.map { case (nombre, calif) => s"$nombre: $calif" }

    val outputPath = "/tmp/aprobados_spark"
    formateado.saveAsTextFile(outputPath)
    println(s"Datos guardados en: $outputPath")

    // 5. Lee de vuelta y verifica
    println("\n=== Verificación ===")
    val archivosTxt = scala.io.Source.fromFile(s"$outputPath/part-00000").getLines()
    println("Contenido del archivo:")
    archivosTxt.foreach(println)

    // También puedes cargar con Spark
    val lectura = sc.textFile(s"$outputPath/part-*").collect()
    println("\nLeído con Spark:")
    lectura.foreach(println)

    sc.stop()
  }
}
