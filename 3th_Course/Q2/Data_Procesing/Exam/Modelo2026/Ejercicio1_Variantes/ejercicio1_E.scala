/*
Ejercicio 1_E - Scala simple: LOGS DE APLICACIÓN

Escribe un programa en Scala que lea un archivo de texto llamado
"server_logs.txt" (formato: IP,timestamp,respuesta_code), filtre
únicamente los logs con código de respuesta >= 400 (errores) y 
guarde los resultados en "output1.txt" (REPL) y "output2.txt" 
(compilado).

Se pide:
1. Código REPL (Modo Dinámico) - output1.txt
2. Código compilado .scala (Modo Estático) - output2.txt

Archivo de entrada: server_logs.txt
192.168.1.1,2026-06-02T10:30,200
192.168.1.2,2026-06-02T10:31,404
192.168.1.3,2026-06-02T10:32,200
192.168.1.4,2026-06-02T10:33,500
192.168.1.5,2026-06-02T10:34,403

Salida esperada:
192.168.1.2,2026-06-02T10:31,404
192.168.1.4,2026-06-02T10:33,500
192.168.1.5,2026-06-02T10:34,403
*/

val ficheroEntrada = "server_logs.txt"
val ficheroSalida1 = "output1.txt"
val ficheroSalida2 = "output2.txt"

// ============ MODO INTERACTIVO (REPL) ============

import scala.io.Source
import java.io.PrintWriter

val lineas = Source.fromFile(ficheroEntrada).getLines().toList
val procesadas = lineas.map { linea =>
  val Array(ip, timestamp, codigo) = linea.split(",")
  val codigoInt = codigo.toInt
  (ip, timestamp, codigoInt)
}.filter { case (_, _, codigo) => codigo >= 400 }

val writer1 = new PrintWriter(ficheroSalida1)
procesadas.foreach { case (ip, timestamp, codigo) =>
  writer1.println(s"$ip,$timestamp,$codigo")
}
writer1.close()

println("Archivo output1.txt generado con éxito.")

// ============ MODO COMPILADO (.scala) ============

import scala.io.Source
import java.io.PrintWriter

object ProcesarLogs {
  def main(args: Array[String]): Unit = {
    val ficheroEntrada = "server_logs.txt"
    val ficheroSalida = "output2.txt"

    val origen = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        val Array(ip, timestamp, codigo) = linea.split(",")
        val codigoInt = codigo.toInt
        if (codigoInt >= 400) {
          destino.println(s"$ip,$timestamp,$codigo")
        }
      }
    } finally {
      origen.close()
      destino.close()
    }

    println("Proceso finalizado con éxito.")
  }
}
