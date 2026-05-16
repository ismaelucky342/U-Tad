/*ENUNCIADO — Variante 5 (Frecuencia de palabras)

Se desea desarrollar un programa en Scala que procese un fichero de texto llamado frases.txt.

El fichero contiene varias frases, una por línea, sin formato fijo.

El objetivo del programa es analizar la frecuencia de aparición de palabras en todo el fichero, aplicando el siguiente procesamiento:

🔹 Transformación a realizar

El programa deberá:

Leer todas las líneas del fichero.
Eliminar espacios sobrantes.
Convertir todo el texto a minúsculas.
Dividir el texto en palabras.
Ignorar líneas vacías.
Calcular cuántas veces aparece cada palabra en todo el fichero.
Generar un fichero de salida llamado frequencies.txt con el siguiente formato:
palabra1 => frecuencia
palabra2 => frecuencia
...

Requisitos
Las rutas del fichero de entrada y salida deberán definirse mediante variables inmutables (val).
El programa debe ignorar signos de puntuación básicos:
.,;:!?
El orden de salida puede ser cualquiera (no es necesario ordenar).

Ejemplo de entrada (frases.txt)
Hola mundo mundo
Scala es potente
Mundo de datos

Ejemplo de salida (frequencies.txt)
hola => 1
mundo => 3
scala => 1
es => 1
potente => 1
de => 1
datos => 1*/ 

// Versión interactiva:

import scala.io.Source
import java.io.PrintWriter

val ficheroEntrada = "frases.txt"
val ficheroSalida  = "frequencies.txt"

val lineas = Source.fromFile(ficheroEntrada).getLines().toList

val palabras = lineas.filter(_.trim.nonEmpty) // Eliminar líneas vacías
                     .flatMap(_.trim.toLowerCase.replaceAll("[.,;:!?]", "").split("\\s+")) // Eliminar espacios sobrantes, convertir a minúsculas, eliminar signos de puntuación y dividir en palabras

val frecuencia = palabras.groupBy(identity).view.mapValues(_.size).toMap
val writer = new PrintWriter(ficheroSalida)
frecuencia.foreach { case (palabra, freq) =>
  writer.println(s"$palabra => $freq")
}
writer.close()
println("Archivo frequencies.txt generado con éxito.")


// Versión compilada:

import scala.io.Source
import java.io.PrintWriter

object ContarFrecuencias {
  def main(args: Array[String]): Unit = {

    val ficheroEntrada = "frases.txt"
    val ficheroSalida  = "frequencies.txt"

    val origen = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      val lineas = origen.getLines().toList
      val palabras = lineas.filter(_.trim.nonEmpty)
                           .flatMap(_.trim.toLowerCase.replaceAll("[.,;:!?]", "").split("\\s+"))
      val frecuencia = palabras.groupBy(identity).view.mapValues(_.size).toMap
      frecuencia.foreach { case (palabra, freq) =>
        destino.println(s"$palabra => $freq")
      }
    } finally {
      origen.close()
      destino.close()
    }
    println("Archivo frequencies.txt generado con éxito.")
  }
}

