/*
Ejercicio 1_B - Scala simple: TEMPERATURAS

Escribe un programa en Scala que lea un archivo de texto llamado
"temperaturas.txt", convierta cada temperatura de Celsius a Fahrenheit
usando la fórmula: F = C * 9/5 + 32, y guarde únicamente aquellas
temperaturas finales mayores a 60°F en "output1.txt" (REPL) y 
"output2.txt" (compilado).

Se pide:
1. Código REPL (Modo Dinámico) - output1.txt
2. Código compilado .scala (Modo Estático) - output2.txt

Archivo de entrada: temperaturas.txt
Madrid,25
Barcelona,22
Sevilla,28
Bilbao,18
Valencia,26

Salida esperada:
Madrid,77.0
Barcelona,71.6
Sevilla,82.4
Valencia,78.8
*/

val ficheroEntrada = "temperaturas.txt"
val ficheroSalida1 = "output1.txt"
val ficheroSalida2 = "output2.txt"

// ============ MODO INTERACTIVO (REPL) ============

import scala.io.Source
import java.io.PrintWriter

val lineas = Source.fromFile(ficheroEntrada).getLines().toList
val procesadas = lineas.map { linea =>
  val Array(ciudad, tempStr) = linea.split(",")
  val tempC = tempStr.toDouble
  val tempF = tempC * 9.0 / 5.0 + 32.0
  (ciudad, tempF)
}.filter { case (_, tempF) => tempF > 60 }

val writer1 = new PrintWriter(ficheroSalida1)
procesadas.foreach { case (ciudad, tempF) =>
  writer1.println(s"$ciudad,${tempF.formatted("%.1f")}")
}
writer1.close()

println("Archivo output1.txt generado con éxito.")

// ============ MODO COMPILADO (.scala) ============

import scala.io.Source
import java.io.PrintWriter

object ProcesarTemperaturas {
  def main(args: Array[String]): Unit = {
    val ficheroEntrada = "temperaturas.txt"
    val ficheroSalida = "output2.txt"

    val origen = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        val Array(ciudad, tempStr) = linea.split(",")
        val tempC = tempStr.toDouble
        val tempF = tempC * 9.0 / 5.0 + 32.0
        if (tempF > 60) {
          destino.println(s"$ciudad,${tempF.formatted("%.1f")}")
        }
      }
    } finally {
      origen.close()
      destino.close()
    }

    println("Proceso finalizado con éxito.")
  }
}
