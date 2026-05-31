// VARIANTE 3: Palabras que contienen al menos dos vocales distintas
//             (RDDs en Spark)
//
// Descarga un texto literario diferente, por ejemplo:
//
// wget https://www.gutenberg.org/files/84/84-0.txt
//
// Cárgalo en Spark:
//
// val texto = sc.textFile("84-0.txt")
//
// Queremos analizar el texto y quedarnos solo con las palabras
// que contengan al menos dos vocales distintas.
//
// Por ejemplo:
//
// "monster"  → no válida
// "house"    → válida (o, u, e)
// "quiet"    → válida (u, i, e)
// "sky"      → no válida
//
// Requisitos:
//
// - Convierte todo a minúsculas.
// - Elimina signos de puntuación y caracteres raros.
// - Separa el texto en palabras.
// - Elimina palabras vacías.
// - Filtra solo las palabras que contengan al menos
//   dos vocales distintas.
// - Cuenta cuántas veces aparece cada palabra válida.
// - Ordena el resultado por frecuencia descendente.
// - Muestra las 10 palabras más repetidas.
//
// Pistas:
//
// - Puedes usar un conjunto de vocales para comprobar
//   cuántas distintas aparecen en una palabra.
// - Te interesa practicar limpieza de texto,
//   filter(), flatMap(), map(), reduceByKey() y sortBy().

import scala.io.Source
import java.io.PrintWriter

val texto = sc.textFile("84-0.txt")

val vocales = Set('a', 'e', 'i', 'o', 'u')

val palabrasValidas = texto.map(linea => linea.toLowerCase.replaceAll("[^a-zA-Z\\s]", "")) // Limpiar y convertir a minúsculas
  .flatMap(linea => linea.split("\\s+")) // Separar en palabras
  .filter(palabra => palabra.nonEmpty) // Eliminar palabras vacías
  .filter(palabra => palabra.count(c => vocales.contains(c)) >= 2) // Filtrar palabras con al menos 2 vocales distintas
  .map(palabra => (palabra, 1)) // Crear tuplas (palabra, 1)
  .reduceByKey(_ + _) // Contar apariciones
  .sortBy({ case (_, count) => -count }) // Ordenar por frecuencia descendente
  .take(10) // Mostrar las 10 palabras más repetidas    
palabrasValidas.foreach { case (palabra, count) =>
  println(s"($palabra, $count)")
}