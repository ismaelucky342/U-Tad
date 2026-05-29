/*
 * EX05 - groupByKey vs reduceByKey
 *
 * OBJETIVO:
 * - Entender la diferencia entre groupByKey y reduceByKey
 * - Practicar groupByKey para obtener todas las valores de una clave
 * - Entender performance: reduceByKey es más eficiente (shuffle)
 *
 * ENUNCIADO:
 *
 * 1. Crea un Pair RDD con: (categoría, valor):
 *    ("A", 5), ("B", 2), ("A", 3), ("C", 8), ("B", 1), ("A", 7)
 *
 * 2. Usa groupByKey para agrupar valores por categoría
 *
 * 3. Mapea para calcular suma, promedio y máximo de cada grupo
 *
 * 4. Imprime estadísticas de cada categoría
 *
 * CONCEPTOS:
 * - groupByKey: agrupa valores con la misma clave en iterables
 * - Diferencia: reduceByKey es más eficiente (shuffle menor)
 * - groupByKey es útil cuando necesitas TODOS los valores, no solo agregarlos
 *
 */

import org.apache.spark.{SparkConf, SparkContext}

object EjercicioSpark05 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark05").setMaster("local[*]")
    val sc = new SparkContext(conf)

    // 1. Pair RDD
    val datos = sc.parallelize(List(
      ("A", 5),
      ("B", 2),
      ("A", 3),
      ("C", 8),
      ("B", 1),
      ("A", 7),
      ("C", 4)
    ))

    // 2. groupByKey
    val agrupado = datos.groupByKey()

    // 3. Mapea para calcular estadísticas
    val estadisticas = agrupado.map { case (categoria, valores) =>
      val lista = valores.toList
      val suma = lista.sum
      val promedio = suma.toDouble / lista.length
      val maximo = lista.max
      (categoria, lista, suma, promedio, maximo)
    }

    // 4. Imprime resultados
    println("Datos originales:")
    datos.collect().foreach { case (cat, val) =>
      println(s"  ($cat, $val)")
    }

    println("\nAgrupado por categoría:")
    agrupado.collect().foreach { case (cat, vals) =>
      println(s"  $cat: ${vals.toList}")
    }

    println("\nEstadísticas:")
    estadisticas.collect().foreach { case (cat, lista, suma, prom, max) =>
      println(s"  Categoría $cat:")
      println(s"    Valores: $lista")
      println(s"    Suma: $suma, Promedio: $prom, Máximo: $max")
    }

    sc.stop()
  }
}
