/*
Ejercicio 1_F - Scala simple: ESTUDIANTES CON MÚLTIPLES CÁLCULOS

Escribe un programa en Scala que lea un archivo de texto llamado
"estudiantes.txt" (formato: nombre,matematicas,ingles,historia),
calcule el promedio de cada estudiante y guarde únicamente aquellos
con promedio >= 7 en "output1.txt" (REPL) y "output2.txt" (compilado).

Se pide:
1. Código REPL (Modo Dinámico) - output1.txt
2. Código compilado .scala (Modo Estático) - output2.txt

Archivo de entrada: estudiantes.txt
Pedro,8,7,6
Laura,9,8.5,8
Marco,5,6,5.5
Iris,7.5,7.2,7.8
Alex,6.5,6,6.5

Salida esperada:
Pedro,7.0
Laura,8.5
Iris,7.5
*/

val ficheroEntrada = "estudiantes.txt"
val ficheroSalida1 = "output1.txt"
val ficheroSalida2 = "output2.txt"

// ============ MODO INTERACTIVO (REPL) ============

import scala.io.Source
import java.io.PrintWriter

val lineas = Source.fromFile(ficheroEntrada).getLines().toList
val procesadas = lineas.map { linea =>
  val Array(nombre, mat, ing, his) = linea.split(",")
  val promedio = (mat.toDouble + ing.toDouble + his.toDouble) / 3.0
  (nombre, promedio)
}.filter { case (_, promedio) => promedio >= 7 }

val writer1 = new PrintWriter(ficheroSalida1)
procesadas.foreach { case (nombre, promedio) =>
  writer1.println(s"$nombre,${promedio.formatted("%.1f")}")
}
writer1.close()

println("Archivo output1.txt generado con éxito.")

// ============ MODO COMPILADO (.scala) ============

import scala.io.Source
import java.io.PrintWriter

object ProcesarEstudiantes {
  def main(args: Array[String]): Unit = {
    val ficheroEntrada = "estudiantes.txt"
    val ficheroSalida = "output2.txt"

    val origen = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        val Array(nombre, mat, ing, his) = linea.split(",")
        val promedio = (mat.toDouble + ing.toDouble + his.toDouble) / 3.0
        if (promedio >= 7) {
          destino.println(s"$nombre,${promedio.formatted("%.1f")}")
        }
      }
    } finally {
      origen.close()
      destino.close()
    }

    println("Proceso finalizado con éxito.")
  }
}
