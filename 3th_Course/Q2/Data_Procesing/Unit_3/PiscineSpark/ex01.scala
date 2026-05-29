/*
 * EX01 - Transformaciones encadenadas + acciones (RDDs)
 *
 * OBJETIVO:
 * - Practicar transformaciones múltiples en RDD
 * - Introducir filter + map encadenados
 * - Entender que las transformaciones son lazy (no se ejecutan)
 * - Forzar ejecución con acciones
 *
 * ENUNCIADO:
 *
 * 1. Crea un RDD a partir de la lista:
 *    List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
 *
 * 2. Aplica las siguientes transformaciones en orden:
 *
 *    a) Multiplica cada elemento por 2
 *    b) Filtra solo los valores mayores que 10
 *
 * 3. Obtén el resultado final con collect()
 *
 * 4. Imprime el resultado en formato:
 *    "Resultado final: x, y, z, ..."
 *
 * 5. Calcula cuántos elementos quedan usando count()
 *
 * 6. (IMPORTANTE) Reflexiona:
 *    - ¿cuándo se ejecuta realmente el DAG?
 *    - ¿cuántas transformaciones hay antes de la acción?
 *
 * BONUS:
 * - Intenta reescribirlo en una sola línea encadenando transformaciones
 *
 */

// Solución en spark-shell (modo interactivo)

val rdd = sc.parallelize(List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

val resultado = rdd.map(x => x * 2).filter(x => x > 10).collect()

println(s"Resultado final: ${resultado.mkString(", ")}")

val count = rdd.map(x => x * 2).filter(x => x > 10).count()

println(s"Cantidad de elementos mayores que 10: $count")

// Solución en aplicación Scala completa

import org.apache.spark.{SparkConf, SparkContext}

object EjercicioSpark {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark").setMaster("local[*]")
    val sc = new SparkContext(conf)

    val rdd = sc.parallelize(List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    val resultado = rdd.map(x => x * 2).filter(x => x > 10).collect()
    println(s"Resultado final: ${resultado.mkString(", ")}")

    val count = rdd.map(x => x * 2).filter(x => x > 10).count()
    println(s"Cantidad de elementos mayores que 10: $count")

    sc.stop()
  }
}