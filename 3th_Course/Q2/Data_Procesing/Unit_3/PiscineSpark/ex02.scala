/*
 * EX02 - map, filter y transformaciones encadenadas
 *
 * OBJETIVO:
 * - Dominar map y filter en RDDs
 * - Entender transformaciones lazy
 * - Practicar encadenamiento
 *
 * ENUNCIADO:
 *
 * 1. Crea un RDD con números del 1 al 20
 * 2. Filtra números pares
 * 3. Multiplica cada uno por su índice (aquí deberás usar zipWithIndex)
 * 4. Imprime solo los que sean mayores a 100
 *
 * CONCEPTOS:
 * - map: transforma cada elemento
 * - filter: mantiene solo elementos que cumplen condición
 * - zipWithIndex: agrega índice a cada elemento
 * - Lazy evaluation: las transformaciones no se ejecutan hasta una acción
 *
 */

import org.apache.spark.{SparkConf, SparkContext}

object EjercicioSpark02 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark02").setMaster("local[*]")
    val sc = new SparkContext(conf)

    // 1. Crear RDD con números del 1 al 20
    val rdd = sc.parallelize(1 to 20)

    // 2. Filtra números pares
    val pares = rdd.filter(x => x % 2 == 0)

    // 3. Usa zipWithIndex para agregar índices
    val conIndices = pares.zipWithIndex.map { case (valor, indice) =>
      valor * (indice + 1)
    }

    // 4. Filtra mayores a 100
    val mayoresA100 = conIndices.filter(x => x > 100)

    // Imprime resultados
    println("Números pares originales: " + pares.collect().mkString(", "))
    println("Después de zipWithIndex y multiplicar: " + conIndices.collect().mkString(", "))
    println("Mayores a 100: " + mayoresA100.collect().mkString(", "))
    
    sc.stop()
  }
}
