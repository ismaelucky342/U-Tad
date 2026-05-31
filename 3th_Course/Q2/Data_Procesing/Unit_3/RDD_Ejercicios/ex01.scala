// VARIANTE 2: Top palabras que empiezan por cada letra (RDDs en Spark)
//
// Descarga un texto usando wget:
//
// wget https://www.gutenberg.org/files/2000/2000-0.txt
//
// Carga el archivo:
//
// val texto = sc.textFile("2000-0.txt")
//
// Queremos obtener, para cada letra inicial,
// la palabra más repetida del texto.
//
// Ejemplo:
//
// Si aparecen:
//
// casa
// coche
// casa
// cielo
// coche
// coche
// árbol
// amigo
// amigo
//
// El resultado sería:
//
// (c,coche,3)
// (a,amigo,2)
//
// Requisitos:
//
// - Ignora mayúsculas/minúsculas.
// - Elimina signos de puntuación.
// - Elimina palabras vacías.
// - Considera letras con acento.
//
// - Separa el texto en palabras.
//
// - Cuenta cuántas veces aparece cada palabra.
//
// - A partir del resultado anterior, agrupa por
//   la primera letra de la palabra.
//
// - Para cada letra inicial, conserva únicamente
//   la palabra con más apariciones.
//
// Resultado esperado (ejemplo):
//
// (a,acordarme,57)
// (b,bueno,23)
// (c,capitán,45)
// ...

import scala.io.Source
import java.io.PrintWriter

val texto = sc.textFile("2000-0.txt")

val palabras = texto.map(linea => linea.toLowerCase.replaceAll("[^a-zA-ZáéíóúÁÉÍÓÚ\\s]", "")) // Limpiar y convertir a minúsculas
  .flatMap(linea => linea.split("\\s+")) // Separar en palabras
  .filter(palabra => palabra.nonEmpty) // Eliminar palabras vacías
  .map(palabra => (palabra, 1)) // Crear tuplas (palabra, 1)
  .reduceByKey(_ + _) // Contar apariciones por palabra
  .map { case (palabra, count) => (palabra.charAt(0), (palabra, count)) } // Agrupar por letra inicial
  .groupByKey() // Agrupar por letra inicial
  .mapValues(iter => iter.maxBy(_._2)) // Obtener la palabra más repetida para cada letra

palabras.collect().foreach { case (letra, (palabra, count)) =>
  println(s"($letra, $palabra, $count)")
}