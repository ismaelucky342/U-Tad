/*
 * EX04 - Pair RDD y reduceByKey
 *
 * OBJETIVO:
 * - Familiarizarse con Pair RDD (clave-valor)
 * - Entender reduceByKey vs map/filter
 * - Practicar word count (ejercicio clásico)
 *
 * ENUNCIADO:
 *
 * 1. Realiza word count sobre el texto:
 *    "scala spark scala big data spark big"
 *
 * 2. Convierte a Pair RDD: (palabra, 1)
 *
 * 3. Usa reduceByKey para contar ocurrencias
 *
 * 4. Ordena por frecuencia descendente
 *
 * 5. Muestra el resultado y la palabra más frecuente
 *
 * CONCEPTOS:
 * - Pair RDD: RDD[(K, V)]
 * - reduceByKey: suma valores con la misma clave (más eficiente que groupByKey)
 * - sortBy: ordenar elementos
 * - take(n): obtener primeros n elementos (acción)
 *
 */

import org.apache.spark.{SparkConf, SparkContext}

object EjercicioSpark04 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark04").setMaster("local[*]")
    val sc = new SparkContext(conf)

    // 1. Texto
    val texto = "scala spark scala big data spark big data spark"

    // 2. Crear RDD y dividir en palabras
    val palabras = sc.parallelize(texto.split(" "))

    // 3. Convertir a Pair RDD: (palabra, 1)
    val pairRDD = palabras.map(palabra => (palabra, 1))

    // 4. Usar reduceByKey para contar
    val conteoPalabras = pairRDD.reduceByKey(_ + _)

    // 5. Ordenar por frecuencia descendente
    val ordenado = conteoPalabras.sortBy(_._2, ascending = false)

    // Acciones para ver resultados
    println("Pair RDD original: " + pairRDD.take(5).mkString(", "))
    println("\nConteo de palabras: " + conteoPalabras.collect().mkString(", "))
    println("\nOrdenado por frecuencia:")
    ordenado.collect().foreach { case (palabra, freq) =>
      println(s"  $palabra: $freq")
    }

    println(s"\nPalabra más frecuente: ${ordenado.first()}")
    println(s"Total de palabras únicas: ${conteoPalabras.count()}")

    sc.stop()
  }
}
