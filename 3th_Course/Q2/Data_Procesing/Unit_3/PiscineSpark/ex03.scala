/*
 * EX03 - flatMap y transformaciones complejas
 *
 * OBJETIVO:
 * - Entender flatMap vs map
 * - Trabajar con colecciones anidadas
 * - Aplicar múltiples transformaciones
 *
 * ENUNCIADO:
 *
 * 1. Crea un RDD con palabras:
 *    List("hola mundo", "scala spark", "big data")
 *
 * 2. Usa flatMap para dividir cada línea en palabras individuales
 *
 * 3. Mapea cada palabra a (palabra, 1)
 *
 * 4. Filtra palabras con más de 3 caracteres
 *
 * 5. Imprime los resultados
 *
 * CONCEPTOS:
 * - flatMap: map + flatten (cada elemento genera múltiples elementos)
 * - Diferencia entre map(_.split(" ")) vs flatMap(_.split(" "))
 *
 */

import org.apache.spark.{SparkConf, SparkContext}

object EjercicioSpark03 {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("EjercicioSpark03").setMaster("local[*]")
    val sc = new SparkContext(conf)

    // 1. RDD con frases
    val lineas = sc.parallelize(List(
      "hola mundo",
      "scala spark",
      "big data processing"
    ))

    // 2. flatMap para dividir en palabras
    val palabras = lineas.flatMap(linea => linea.split(" "))

    // 3. Mapea a (palabra, 1)
    val palabraConUno = palabras.map(palabra => (palabra, 1))

    // 4. Filtra palabras con más de 3 caracteres
    val palabrasLargas = palabraConUno.filter { case (palabra, _) => palabra.length > 3 }

    // 5. Imprime resultados
    println("Palabras iniciales (map vs flatMap):")
    println("  Con map: " + lineas.map(_.split(" ")).collect().map(_.mkString("[", ",", "]")).mkString(", "))
    println("  Con flatMap: " + palabras.collect().mkString(", "))
    println("\nPalabras con (palabra, 1): " + palabraConUno.collect().mkString(", "))
    println("Palabras largas (>3 caracteres): " + palabrasLargas.collect().mkString(", "))

    sc.stop()
  }
}
