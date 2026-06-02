/*
Ejercicio 1_D - Scala simple: CALIFICACIONES CON MÚLTIPLES CAMPOS

Escribe un programa en Scala que lea un archivo de texto llamado
"calificaciones.txt" (formato: nombre,edad,nota), calcule una 
calificación final multiplicando la nota por 1.15 y guarde únicamente
aquellos registros donde la nota final sea >= 6 Y la edad >= 18 en
"output1.txt" (REPL) y "output2.txt" (compilado).

Se pide:
1. Código REPL (Modo Dinámico) - output1.txt
2. Código compilado .scala (Modo Estático) - output2.txt

Archivo de entrada: calificaciones.txt
Maria,19,6
Juan,17,7
Ana,21,5
Carlos,20,4
Sofia,22,6

Salida esperada:
Maria,19,6.9
Carlos,20,4.6
Sofia,22,6.9

Nota: Se incluyen solo mayores de edad con nota final >= 6
*/

val ficheroEntrada = "calificaciones.txt"
val ficheroSalida1 = "output1.txt"
val ficheroSalida2 = "output2.txt"

// ============ MODO INTERACTIVO (REPL) ============

import scala.io.Source
import java.io.PrintWriter

val lineas = Source.fromFile(ficheroEntrada).getLines().toList
val procesadas = lineas.map { linea =>
  val Array(nombre, edadStr, notaStr) = linea.split(",")
  val edad = edadStr.toInt
  val nota = notaStr.toDouble
  val notaFinal = nota * 1.15
  (nombre, edad, notaFinal)
}.filter { case (_, edad, notaFinal) => edad >= 18 && notaFinal >= 6 }

val writer1 = new PrintWriter(ficheroSalida1)
procesadas.foreach { case (nombre, edad, notaFinal) =>
  writer1.println(s"$nombre,$edad,${notaFinal.formatted("%.1f")}")
}
writer1.close()

println("Archivo output1.txt generado con éxito.")

// ============ MODO COMPILADO (.scala) ============

import scala.io.Source
import java.io.PrintWriter

object ProcesarCalificaciones {
  def main(args: Array[String]): Unit = {
    val ficheroEntrada = "calificaciones.txt"
    val ficheroSalida = "output2.txt"

    val origen = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        val Array(nombre, edadStr, notaStr) = linea.split(",")
        val edad = edadStr.toInt
        val nota = notaStr.toDouble
        val notaFinal = nota * 1.15
        if (edad >= 18 && notaFinal >= 6) {
          destino.println(s"$nombre,$edad,${notaFinal.formatted("%.1f")}")
        }
      }
    } finally {
      origen.close()
      destino.close()
    }

    println("Proceso finalizado con éxito.")
  }
}
