//ENUNCIADO — Variante 6 (Inversión del orden de palabras)
//
//Se desea desarrollar un programa en Scala que procese un fichero de texto llamado frases.txt.
//
//El fichero contiene varias frases, una por línea.
//
//El objetivo del programa es invertir el orden de las palabras de cada línea manteniendo intactos los caracteres de cada palabra.
//
//🔹 Transformación a realizar
//
//Para cada línea del fichero:
//
//Eliminar espacios sobrantes al inicio y final de la línea.
//Dividir la línea en palabras separadas por espacios.
//Invertir el orden de las palabras.
//Reconstruir la línea separando las palabras mediante un único espacio.
//Guardar el resultado en un fichero llamado reversed_words.txt.
//Requisitos
//Las rutas del fichero de entrada y salida deberán definirse mediante variables inmutables (val).
//Si una línea está vacía, deberá mantenerse vacía en el fichero de salida.
//El programa debe funcionar tanto en modo interactivo como en modo compilado.
//Ejemplo de entrada (frases.txt)
//Scala es muy potente
//Hola mundo
//IA transforma empresas
//Ejemplo de salida (reversed_words.txt)
//potente muy es Scala
//mundo Hola
//empresas transforma IA

// version interactiva; 

import scala.io.Source
import java.io.PrintWriter

val ficheroEntrada = "frases.txt"
val ficheroSalida  = "reversed_words.txt"

val lineas     = Source.fromFile(ficheroEntrada).getLines().toList
val procesadas = lineas.map { linea =>
  val palabras = linea.trim.split("\\s+")
  palabras.reverse.mkString(" ")
}

val writer = new PrintWriter(ficheroSalida)
procesadas.foreach(writer.println)
writer.close()

println("Archivo reversed_words.txt generado con éxito.")

// version compilada:

import scala.io.Source
import java.io.PrintWriter

object InvertirPalabras {
  def main(args: Array[String]): Unit = {

    val ficheroEntrada = "frases.txt"
    val ficheroSalida  = "reversed_words.txt"

    val origen  = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        val palabras = linea.trim.split("\\s+")
        val lineaProcesada = palabras.reverse.mkString(" ")
        destino.println(lineaProcesada)
      }
    } finally {
      origen.close()
      destino.close()
    }

    println("Archivo reversed_words.txt generado con éxito.")
  }
}