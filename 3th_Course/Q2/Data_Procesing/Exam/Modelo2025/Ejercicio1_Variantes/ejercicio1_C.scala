/*ENUNCIADO — Variante 3 (Rotación de palabras)

Se desea desarrollar un programa en Scala que procese un fichero de texto denominado frases.txt.

El fichero contiene varias frases, una por línea, sin formato fijo.

El objetivo del programa es reorganizar el contenido de cada línea mediante una rotación de palabras, aplicando el siguiente procedimiento:

🔹 Transformación a realizar

Para cada línea del fichero:

Dividir la línea en palabras (separadas por espacios).
Rotar el orden de las palabras una posición a la izquierda:
La primera palabra pasa a ser la última.
El resto de palabras se desplazan una posición hacia la izquierda.
Unir nuevamente las palabras en una única línea.
Guardar el resultado en un fichero de salida llamado shifted.txt.
Consideraciones
Las rutas del fichero de entrada y salida deberán definirse mediante variables inmutables (val).
Se debe contemplar que una línea puede contener una sola palabra (en cuyo caso no se modifica).
Se deben eliminar espacios sobrantes antes de procesar cada línea.

Ejemplo de entrada (frases.txt)
Hola mundo que tal
Scala es muy potente
IA transforma el mundo*/

// Versión interactiva:

import scala.io.Source
import java.io.PrintWriter

val ficheroEntrada = "frases.txt"
val ficheroSalida  = "shifted.txt"

val lineas     = Source.fromFile(ficheroEntrada).getLines().toList

val procesadas = lineas.map { linea =>
  val palabras = linea.trim.split("\\s+")
  if (palabras.length <= 1) linea.trim
  else (palabras.tail :+ palabras.head).mkString(" ")
}

val writer = new PrintWriter(ficheroSalida)
procesadas.foreach(writer.println)
writer.close()
println("Archivo shifted.txt generado con éxito.")


// Versión compilada:

import scala.io.Source
import java.io.PrintWriter

object RotarPalabras {
    def main(args: Array[String]): Unit = {
    
        val ficheroEntrada = "frases.txt"
        val ficheroSalida  = "shifted.txt"
    
        val origen  = Source.fromFile(ficheroEntrada)
        val destino = new PrintWriter(ficheroSalida)
    
        try {
            for (linea <- origen.getLines()) {
                val palabras = linea.trim.split("\\s+")
                val lineaProcesada = if (palabras.length <= 1) linea.trim
                                    else (palabras.tail :+ palabras.head).mkString(" ")
                destino.println(lineaProcesada)
            }
        } finally {
            origen.close()
            destino.close()
        }
    
        println("Archivo shifted.txt generado con éxito.")
    }
}