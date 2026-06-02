/*
Ejercicio 1_A - Scala simple: NOTAS (Modelo Original)

Escribe un programa en Scala que lea un archivo de texto llamado
"notas.txt", calcule la nota final aplicando un incremento del 10%
a cada alumno y guarde únicamente aquellos alumnos cuya nota final
sea mayor o igual a 5 en un nuevo archivo llamado "output1.txt"
para la opción 1 y "output2.txt" para la opción 2.

Se pide:
1. Código REPL (Modo Dinámico) - output1.txt
2. Código compilado .scala (Modo Estático) - output2.txt

Archivo de entrada: notas.txt
Juan,4
Ana,8
Pedro,3
Marta,7
Luis,5

Salida esperada:
Ana,8.8
Marta,7.7
Luis,5.5
*/

val ficheroEntrada = "notas.txt"
val ficheroSalida1 = "output1.txt"
val ficheroSalida2 = "output2.txt"

// ============ MODO INTERACTIVO (REPL) ============

import scala.io.Source
import java.io.PrintWriter

val lineas = Source.fromFile(ficheroEntrada).getLines().toList
val procesadas = lineas.map { linea =>
  val Array(nombre, notaStr) = linea.split(",")
  val nota = notaStr.toDouble
  val notaFinal = nota * 1.10
  (nombre, notaFinal)
}.filter { case (_, notaFinal) => notaFinal >= 5 }

val writer1 = new PrintWriter(ficheroSalida1)
procesadas.foreach { case (nombre, notaFinal) =>
  writer1.println(s"$nombre,${notaFinal.formatted("%.1f")}")
}
writer1.close()

println("Archivo output1.txt generado con éxito.")

// ============ MODO COMPILADO (.scala) ============

import scala.io.Source
import java.io.PrintWriter

object ProcesarNotas {
  def main(args: Array[String]): Unit = {
    val ficheroEntrada = "notas.txt"
    val ficheroSalida = "output2.txt"

    val origen = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        val Array(nombre, notaStr) = linea.split(",")
        val nota = notaStr.toDouble
        val notaFinal = nota * 1.10
        if (notaFinal >= 5) {
          destino.println(s"$nombre,${notaFinal.formatted("%.1f")}")
        }
      }
    } finally {
      origen.close()
      destino.close()
    }

    println("Proceso finalizado con éxito.")
  }
}
