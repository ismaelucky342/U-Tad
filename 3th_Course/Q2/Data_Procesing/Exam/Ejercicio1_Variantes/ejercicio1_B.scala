/*ENUNCIADO (Variante 1)

Se desea implementar un programa en Scala que permita realizar una limpieza básica de un fichero de texto con frases.

El fichero de entrada se denominará frases.txt y contendrá varias líneas de texto sin un formato fijo, pudiendo incluir espacios en blanco, signos de puntuación y líneas vacías.

El objetivo del programa es normalizar el contenido del fichero, realizando las siguientes operaciones:

Eliminar todas las líneas vacías o que contengan únicamente espacios.
Convertir todo el texto a minúsculas.

Eliminar los siguientes caracteres de puntuación:

. , ; : ! ?
Guardar el resultado final en un fichero de salida llamado clean_output.txt.

La ruta de los ficheros de entrada y salida deberá definirse mediante variables inmutables (val).

📌 Requisitos de entrega

El alumno deberá demostrar el correcto funcionamiento del programa en dos modos:

1. Modo interactivo (REPL)
Ejecución directa en consola Scala.
Captura de pantalla de la ejecución.
Fichero clean_output.txt generado.
2. Modo compilado (programa Scala)
Código fuente en un fichero .scala.
Ejecución mediante compilación.
Captura de pantalla de ejecución.
Fichero clean_output.txt generado.
📊 Ejemplo de entrada (frases.txt)
Hola Mundo!!!
  
Scala es, sin duda; potente.

Programar es divertido??*/

// Versión interactiva:

import scala.io.Source
import java.io.PrintWriter

val ficheroEntrada = "frases.txt"
val ficheroSalida  = "clean_output.txt"

val lineas     = Source.fromFile(ficheroEntrada).getLines().toList

val procesadas = lineas.filter(_.trim.nonEmpty) // Eliminar líneas vacías o con solo espacios
                          .map(_.toLowerCase)    // Convertir a minúsculas
                          .map(_.replaceAll("[.,;:!?]", "")) // Eliminar signos de puntuación   

val writer = new PrintWriter(ficheroSalida)
procesadas.foreach(writer.println)
writer.close()
println("Archivo clean_output.txt generado con éxito.")

// Versión compilada:

import scala.io.Source
import java.io.PrintWriter

object LimpiarFrases {
  def main(args: Array[String]): Unit = {

    val ficheroEntrada = "frases.txt"
    val ficheroSalida  = "clean_output.txt"

    val origen  = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        if (linea.trim.nonEmpty) { // Eliminar líneas vacías o con solo espacios
          val lineaProcesada = linea.toLowerCase.replaceAll("[.,;:!?]", "") // Convertir a minúsculas y eliminar signos de puntuación
          destino.println(lineaProcesada)
        }
      }
    } finally {
      origen.close()
      destino.close()
    }

    println("Archivo clean_output.txt generado con éxito.")
  }
}

