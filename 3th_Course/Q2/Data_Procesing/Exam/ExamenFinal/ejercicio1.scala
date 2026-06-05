// =================================================================================================== //
//                                                                                                     //
//                                                       ██╗   ██╗   ████████╗ █████╗ ██████╗          //
//     Procesamiento de datos - Examen Final             ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗         //
//                                                       ██║   ██║█████╗██║   ███████║██║  ██║         //
//     created:        05/06/2026  -  9:10:00            ██║   ██║╚════╝██║   ██╔══██║██║  ██║         //
//     last change:    05/06/2026  -  10:51:34           ╚██████╔╝      ██║   ██║  ██║██████╔╝         //
//                                                        ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝          //
//                                                                                                     //
//     Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com               //
//                                                                                                     // 
//     Github:                                           https://github.com/ismaelucky342              // 
//                                                                                                     // 
// =================================================================================================== //

/*Escribe un programa en Scala que lea un archivo de texto llamado misfrases.txt, calcule el número de caracteres de cada línea y guarde en un nuevo archivo el resultado con el siguiente formato:



La vida es bella -> 16 caracteres



(suponiendo que la frase original disponible en el fichero fuera: La vida es bella)

 *Ejemplo de salida esperada en ambos casos:



Scala -> 5 caracteres

La vida es bella -> 16 caracteres

Aprender lleva tiempo -> 21 caracteres

Datos -> 5 caracteres *
Ejemplo de salida esperada en ambos casos:
*/

// modo interactivo 

import scala.io.Source 
import java.io.PrintWriter

// lectura del fichero de entrada
val ficheroEntrada = "misfrases.txt"

val ficheroSalida = "output.txt"

val lineas = scala.io.Source.fromFile(ficheroEntrada).getLines().toList

val procesadas = lineas.map { linea =>
  s"$linea -> ${linea.length} caracteres"
}

// escritura del fichero de salida
val writer = new PrintWriter(ficheroSalida)

procesadas.foreach(writer.println)

writer(close)

println("Archivo output.txt generado con éxito.")


// Modo compilado 

import scala.io.Source
import java.io.PrintWriter

object ProcesarFrases {
  def main(args: Array[String]): Unit = {
    val ficheroEntrada = "misfrases.txt"
    val ficheroSalida  = "output2.txt"

    val origen  = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        val lineaProcesada = s"$linea -> ${linea.length} caracteres"
        destino.println(lineaProcesada)
      }
    } finally {
      origen.close()
      destino.close()
    }

    println("Archivo output2.txt generado con éxito.")
  }
}


