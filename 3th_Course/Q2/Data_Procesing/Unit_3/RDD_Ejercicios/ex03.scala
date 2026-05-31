// VARIANTE 4: Análisis completo de reseñas de películas (RDDs en Spark)
//
// Descarga el siguiente archivo de texto:
//
// wget https://www.gutenberg.org/files/11/11-0.txt
//
// Carga el texto:
//
// val texto = sc.textFile("11-0.txt")
//
// Queremos realizar un pequeño análisis del contenido.
//
// Requisitos:
//
// 1. Convierte todo el texto a minúsculas.
//
// 2. Elimina signos de puntuación y caracteres especiales.
//
// 3. Separa el texto en palabras.
//
// 4. Elimina palabras vacías.
//
// 5. Elimina palabras muy cortas
//    (menos de 4 caracteres).
//
// 6. Calcula cuántas palabras distintas existen.
//
// 7. Obtén las 15 palabras más repetidas.
//
// 8. Calcula cuántas palabras empiezan por cada letra.
//
// Ejemplo:
//
// a → 450
// b → 233
// c → 621
//
// 9. Obtén la longitud media de las palabras.
//
// 10. Muestra las 10 palabras más largas del texto
//     sin repetirlas.
//
// Resultado esperado:
//
// Número de palabras distintas: XXXX
//
// Top palabras:
//
// (alice,230)
// (rabbit,190)
// ...
//
// Frecuencia por inicial:
//
// (a,450)
// (b,233)
// ...
//
// Longitud media:
//
// 6.42
//
// Top palabras largas:
//
// (extraordinary)
// (conversation)
// ...

import scala.io.Source
import java.io.PrintWriter

val texto = sc.textFile("11-0.txt")

// 1. Convierte todo el texto a minúsculas.

val textoMinusculas = texto.map(linea => linea.toLowerCase)

// 2. Elimina signos de puntuación y caracteres especiales.

val textoLimpio = textoMinusculas.map(linea => linea.replaceAll("[^a-zA-Z\\s]", ""))

// 3. Separa el texto en palabras.

val palabras = textoLimpio.flatMap(linea => linea.split("\\s+"))

// 4. Elimina palabras vacías.

val palabrasSinVacias = palabras.filter(palabra => palabra.nonEmpty)

// 5. Elimina palabras muy cortas
//    (menos de 4 caracteres).

val palabrasLargas = palabrasSinVacias.filter(palabra => palabra.length >= 4)

// 6. Calcula cuántas palabras distintas existen.

val palabrasDistintas = palabrasLargas.distinct.count
println(s"Número de palabras distintas: $palabrasDistintas")

// 7. Obtén las 15 palabras más repetidas.

val palabrasContadas = palabrasLargas.map(palabra => (palabra, 1)).reduceByKey(_ + _)
val topPalabras = palabrasContadas.takeOrdered(15)(Ordering[Int].reverse.on(_._2))
println("Top palabras:")
topPalabras.foreach { case (palabra, count) =>
  println(s"($palabra, $count)")
}

// 8. Calcula cuántas palabras empiezan por cada letra.

val frecuenciaPorInicial = palabrasLargas.map(palabra => (palabra.charAt(0), 1)).reduceByKey(_ + _)
println("Frecuencia por inicial:")
frecuenciaPorInicial.collect().foreach { case (inicial, count) =>
  println(s"($inicial, $count)")
}

// 9. Obtén la longitud media de las palabras.

val longitudMedia = palabrasLargas.map(palabra => palabra.length).mean()
println(s"Longitud media: $longitudMedia")

// 10. Muestra las 10 palabras más largas del texto
//     sin repetirlas.

val topPalabrasLargas = palabrasLargas.distinct.takeOrdered(10)(Ordering[Int].reverse.on(_.length))
println("Top palabras largas:")
topPalabrasLargas.foreach { palabra =>
  println(s"($palabra)")
}
