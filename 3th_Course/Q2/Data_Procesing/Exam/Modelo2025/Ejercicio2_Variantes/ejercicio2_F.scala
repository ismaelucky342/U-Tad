// VARIANTE 6: Palabras largas en un texto descargado (RDDs en Spark)
//
// Descarga el siguiente texto usando wget:
//
// wget https://www.gutenberg.org/files/2000/2000-0.txt
//
// Cárgalo en Spark utilizando:
//
// val texto = sc.textFile("2000-0.txt")
//
// Queremos analizar el texto y averiguar cuántas palabras
// largas aparecen.
//
// Consideraremos palabra larga cualquier palabra
// con más de 7 caracteres.
//
// Requisitos:
//
// Implementa dos versiones:
//
// Versión A:
//
// - Convierte todas las líneas a minúsculas.
// - Elimina signos de puntuación (. , ; : ! ? " ( ) etc.).
// - Utiliza flatMap() para separar el texto en palabras.
// - Utiliza filter() para quedarte únicamente con palabras
//   cuya longitud sea mayor que 7.
// - Transforma cada palabra en una tupla (palabra,1).
// - Utiliza reduceByKey() para contar apariciones.
// - Muestra las 10 palabras largas más repetidas.
//
//
//
// Versión B:
//
// - Realiza limpieza y separación dentro de un único flatMap().
// - Genera directamente tuplas (palabra,1).
// - Utiliza groupByKey() seguido de mapValues()
//   para contar ocurrencias.
// - Ordena el resultado por frecuencia descendente.
// - Muestra las 10 palabras más repetidas.
//
// El resultado esperado tendrá un formato parecido a:
//
// (something,34)
// (important,28)
// (understand,21)
// ...

// Version A: Usando `flatMap()`, `filter()`, `map()` y `reduceByKey()`

import scala.io.Source
import java.io.PrintWriter

val texto = sc.textFile("2000-0.txt")

val palabrasLargas = texto.map(linea => linea.toLowerCase.replaceAll("[^a-zA-Z\\s]", "")) // Limpiar y convertir a minúsculas
  .flatMap(linea => linea.split("\\s+")) // Separar en palabras
  .filter(palabra => palabra.length > 7) // Filtrar palabras largas
  .map(palabra => (palabra, 1)) // Crear tuplas (palabra, 1)
  .reduceByKey(_ + _) // Contar apariciones por palabra
  .takeOrdered(10)(Ordering[Int].reverse.on(_._2)) // Obtener las 10 más repetidas

palabrasLargas.foreach { case (palabra, count) =>
  println(s"($palabra, $count)")
}

// Versión B: Usando un único `flatMap()`, `groupByKey()` y `mapValues()`

val texto = sc.textFile("2000-0.txt")

val palabrasLargas = texto.flatMap(linea => {
  val limpia = linea.toLowerCase.replaceAll("[^a-zA-Z\\s]", "") // Limpiar y convertir a minúsculas
  limpia.split("\\s+").filter(palabra => palabra.length > 7).map(palabra => (palabra, 1)) // Separar, filtrar y crear tuplas
}).groupByKey() // Agrupar por palabra
  .mapValues(contadores => contadores.size) // Contar ocurrencias por palabra
  .takeOrdered(10)(Ordering[Int].reverse.on(_._2)) // Obtener las 10 más repetidas

palabrasLargas.foreach { case (palabra, count) =>
  println(s"($palabra, $count)")
}

