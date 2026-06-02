/*
Ejercicio 1_C - Scala simple: VENTAS CON DESCUENTO

Escribe un programa en Scala que lea un archivo de texto llamado
"ventas.txt", aplique un descuento del 15% a cada venta y guarde 
únicamente aquellas ventas con precio final mayor a 50 euros en
"output1.txt" (REPL) y "output2.txt" (compilado).

Se pide:
1. Código REPL (Modo Dinámico) - output1.txt
2. Código compilado .scala (Modo Estático) - output2.txt

Archivo de entrada: ventas.txt
Producto1,80
Producto2,40
Producto3,120
Producto4,35
Producto5,70

Salida esperada:
Producto1,68.0
Producto3,102.0
Producto5,59.5
*/

val ficheroEntrada = "ventas.txt"
val ficheroSalida1 = "output1.txt"
val ficheroSalida2 = "output2.txt"

// ============ MODO INTERACTIVO (REPL) ============

import scala.io.Source
import java.io.PrintWriter

val lineas = Source.fromFile(ficheroEntrada).getLines().toList
val procesadas = lineas.map { linea =>
  val Array(producto, precioStr) = linea.split(",")
  val precio = precioStr.toDouble
  val precioConDescuento = precio * 0.85
  (producto, precioConDescuento)
}.filter { case (_, precioFinal) => precioFinal > 50 }

val writer1 = new PrintWriter(ficheroSalida1)
procesadas.foreach { case (producto, precioFinal) =>
  writer1.println(s"$producto,${precioFinal.formatted("%.1f")}")
}
writer1.close()

println("Archivo output1.txt generado con éxito.")

// ============ MODO COMPILADO (.scala) ============

import scala.io.Source
import java.io.PrintWriter

object ProcesarVentas {
  def main(args: Array[String]): Unit = {
    val ficheroEntrada = "ventas.txt"
    val ficheroSalida = "output2.txt"

    val origen = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        val Array(producto, precioStr) = linea.split(",")
        val precio = precioStr.toDouble
        val precioConDescuento = precio * 0.85
        if (precioConDescuento > 50) {
          destino.println(s"$producto,${precioConDescuento.formatted("%.1f")}")
        }
      }
    } finally {
      origen.close()
      destino.close()
    }

    println("Proceso finalizado con éxito.")
  }
}
