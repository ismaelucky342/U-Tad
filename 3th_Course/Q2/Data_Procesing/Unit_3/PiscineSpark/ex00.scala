 /*
  * EX00 - Primer ejercicio Spark (RDD básico)
  *
  * OBJETIVO:
  * - Crear un programa Spark básico
  * - Trabajar con RDDs desde una colección local
  * - Aplicar una transformación simple
  * - Ejecutar una acción para obtener resultados
  *
  * ENUNCIADO:
  *
  * 1. Crea un RDD a partir de la siguiente lista:
  *    List(1, 2, 3, 4, 5)
  *
  * 2. Aplica una transformación que multiplique cada elemento por 2
  *
  * 3. Obtén el resultado final usando una acción (collect)
  *
  * 4. Imprime por pantalla el resultado en formato:
  *    "Resultado: x, y, z, ..."
  *
  * 5. Cierra correctamente el SparkContext si estás usando app completa
  *
  * BONUS (opcional):
  * - Usa count() para mostrar cuántos elementos hay en el RDD final
  *
  * NOTA:
  * Este ejercicio debe hacerse en dos modos:
  *   A) spark-shell (modo interactivo)
  *   B) Aplicación Scala completa (main + SparkContext)
  *
  */

// Solución en spark-shell (modo interactivo)

val rdd = sc.parallelize(List(1, 2, 3, 4, 5))

val rddMult = rdd.map(x => x * 2)

val resultado = rddMult.collect()

println(s"Resultado: ${resultado.mkString(", ")}")

// Solución en aplicación Scala completa

import org.apache.spark.{SparkConf, SparkContext}

object EjercicioSpark {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark").setMaster("local[*]")
    val sc = new SparkContext(conf)

    val rdd = sc.parallelize(List(1, 2, 3, 4, 5))
    val rddMult = rdd.map(x => x * 2)
    val resultado = rddMult.collect()

    println(s"Resultado: ${resultado.mkString(", ")}")

    // BONUS
    println(s"Cantidad de elementos en el RDD final: ${rddMult.count()}")

    sc.stop()
  }
}