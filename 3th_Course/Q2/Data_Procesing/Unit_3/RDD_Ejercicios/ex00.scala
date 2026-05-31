// VARIANTE 1: Palabras con más consonantes que vocales (RDDs en Spark)
//
// Descarga un texto utilizando wget:
//
// wget https://www.gutenberg.org/files/2000/2000-0.txt
//
// Cárgalo en Spark:
//
// val texto = sc.textFile("2000-0.txt")
//
// Queremos encontrar cuántas veces aparecen las palabras
// que tienen más consonantes que vocales.
//
// Consideraciones:
//
// - Ignora mayúsculas/minúsculas.
// - Elimina signos de puntuación.
// - Considera las vocales:
//   a,e,i,o,u,á,é,í,ó,ú
//
// Ejemplo:
//
// "casa" → 2 vocales, 3 consonantes → válida
// "aire" → 4 vocales, 1 consonante → no válida
//
// Implementa dos versiones:
//
// Versión A:
//
// - Convierte el texto a minúsculas.
// - Limpia caracteres especiales.
// - Utiliza flatMap() para separar palabras.
// - Utiliza filter() para quedarte únicamente
//   con las palabras donde:
//
//      nº consonantes > nº vocales
//
// - Convierte cada palabra a (palabra,1)
// - Utiliza reduceByKey() para contar ocurrencias.
//
//
//
// Versión B:
//
// - Realiza limpieza y generación de tuplas
//   directamente dentro de un único flatMap().
//
// - Utiliza groupByKey().
//
// - Utiliza mapValues() para contar apariciones.
//
// - Ordena el resultado por frecuencia descendente.
//
// - Muestra las 10 palabras más repetidas.
//
// Resultado esperado (ejemplo):
//
// (nombre,45)
// (tiempo,37)
// (mancha,25)
// ...

// Versión A: Usando `flatMap()`, `filter()`, `map()` y `reduceByKey()`

import scala.io.Source
import java.io.PrintWriter

val texto = sc.textFile("2000-0.txt")

val palabrasConMasConsonantes = texto.map(linea => linea.toLowerCase.replaceAll("[^a-záéíóú\\s]", "")) // Limpiar y convertir a minúsculas
  .flatMap(linea => linea.split("\\s+")) // Separar en palabras
  .filter(palabra => {
    val vocales = "aeiouáéíóú"
    val numVocales = palabra.count(c => vocales.contains(c))
    val numConsonantes = palabra.length - numVocales
    numConsonantes > numVocales // Filtrar palabras con más consonantes que vocales
  })
  .map(palabra => (palabra, 1)) // Crear tuplas (palabra, 1)
  .reduceByKey(_ + _) // Contar apariciones por palabra
  .takeOrdered(10)(Ordering[Int].reverse.on(_._2)) // Obtener las 10 más repetidas

palabrasConMasConsonantes.foreach { case (palabra, count) =>
  println(s"($palabra, $count)")
}

// Versión B: Usando un único `flatMap()`, `groupByKey()` y `mapValues()`

val texto = sc.textFile("2000-0.txt")

val palabrasConMasConsonantes = texto.flatMap(linea => {
  val limpia = linea.toLowerCase.replaceAll("[^a-záéíóú\\s]", "") // Limpiar y convertir a minúsculas
  limpia.split("\\s+").filter(palabra => {
    val vocales = "aeiouáéíóú"
    val numVocales = palabra.count(c => vocales.contains(c))
    val numConsonantes = palabra.length - numVocales
    numConsonantes > numVocales // Filtrar palabras con más consonantes que vocales
  }).map(palabra => (palabra, 1)) // Generar tuplas (palabra, 1) directamente
}).groupByKey() // Agrupar por palabra
  .mapValues(contadores => contadores.size) // Contar ocurrencias por palabra
  .takeOrdered(10)(Ordering[Int].reverse.on(_._2)) // Obtener las 10 más repetidas
palabrasConMasConsonantes.foreach { case (palabra, count) =>
  println(s"($palabra, $count)")
}