/*
 * EX06 - Acciones: collect, count, take, first
 *
 * OBJETIVO:
 * - Entender LA DIFERENCIA entre acciones y transformaciones
 * - Practicar principales acciones
 * - Entender cuáles son CARAS (collect en RDD grande)
 *
 * ENUNCIADO:
 *
 * 1. Crea un RDD con 100 números aleatorios (0-1000)
 *
 * 2. Filtra números mayores a 500
 *
 * 3. Usa acciones para:
 *    - count(): contar cuántos hay
 *    - take(5): tomar los 5 primeros
 *    - first(): obtener el primero
 *    - collect(): traer TODOS (¡cuidado con RDDs grandes!)
 *
 * 4. Refleja sobre el costo de cada acción
 *
 * CONCEPTOS:
 * - Acciones: FUERZAN ejecución del DAG y devuelven valores al driver
 * - collect(): CARA, trae TODO al driver
 * - count(): más barata (distributed)
 * - take(): obtiene solo los primeros N
 * - primera vez que se ejecuta el DAG: en la primera acción
 *
 */

import org.apache.spark.{SparkConf, SparkContext}
import scala.util.Random

object EjercicioSpark06 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark06").setMaster("local[*]")
    val sc = new SparkContext(conf)

    // 1. RDD con 100 números aleatorios
    val random = new Random(42)
    val datos = sc.parallelize(1 to 100).map(_ => random.nextInt(1001))

    // 2. Filtra mayores a 500
    val mayoresA500 = datos.filter(_ > 500)

    println("=== ACCIONES EN SPARK ===\n")

    // 3. Diferentes acciones
    println("1. count() - contar elementos:")
    val contador = mayoresA500.count()
    println(s"   Total de números > 500: $contador")

    println("\n2. take(5) - tomar primeros 5:")
    val primeros5 = mayoresA500.take(5)
    println(s"   Primeros 5: ${primeros5.mkString(", ")}")

    println("\n3. first() - obtener el primero:")
    val primero = mayoresA500.first()
    println(s"   Primer número: $primero")

    println("\n4. collect() - traer TODOS (¡cuidado con RDDs grandes!):")
    val todos = mayoresA500.collect()
    println(s"   Total elementos: ${todos.length}")
    println(s"   Primeros 10: ${todos.take(10).mkString(", ")}")
    println(s"   Últimos 10: ${todos.takeRight(10).mkString(", ")}")

    println("\n=== REFLEXIÓN ===")
    println("- count(): Operación distributed, NO trae datos al driver")
    println("- take(n): Solo trae n elementos, eficiente")
    println("- first(): Equivalent a take(1).head")
    println("- collect(): TRAE TODOS los datos al driver (¡puede haber out of memory!)")

    sc.stop()
  }
}
