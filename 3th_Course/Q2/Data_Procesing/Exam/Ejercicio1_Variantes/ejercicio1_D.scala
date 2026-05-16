/*ENUNCIADO — Variante 4 (Análisis de palabras por línea)

Se desea desarrollar un programa en Scala que procese un fichero de texto llamado frases.txt.

El fichero contiene varias frases, una por línea, sin formato fijo.

El objetivo del programa es analizar cada línea y generar estadísticas básicas, realizando el siguiente procesamiento:

Transformación a realizar

Para cada línea del fichero:

Eliminar espacios sobrantes al inicio y al final.
Dividir la línea en palabras (separadas por uno o varios espacios).
Contar el número de palabras de la línea.
Convertir la línea a minúsculas.
Generar una salida con el siguiente formato:
<LÍNEA_PROCESADA> => <NÚMERO_DE_PALABRAS>
Requisitos
Las rutas del fichero de entrada y salida deberán definirse mediante variables inmutables (val).
Las líneas vacías deben ignorarse.
La salida debe guardarse en un fichero llamado stats.txt.
 Ejemplo de entrada (frases.txt)
Hola mundo que tal
Scala es muy potente

IA transforma el mundo
Ejemplo de salida (stats.txt)
hola mundo que tal => 4
scala es muy potente => 4
ia transforma el mundo => 4*/

// Versión interactiva:

import scala.io.source
import java.io.PrintWriter

val ficheroEntrada = "frases.txt"
val ficheroSalida = "stats.txt"

val lineas = Source.fromFile(ficheroEntrada).getLines().toList
val procesadas = lineas.filter(_.trim.nonEmpty) // Eliminar líneas vacías
                          .map(_.trim.toLowerCase) // Eliminar espacios sobrantes y convertir a minúsculas
                          .map(linea => s"$linea => ${linea.split("\\s+").length}") // Contar palabras y formatear salida
val writer = new PrintWriter(ficheroSalida)
procesadas.foreach(writer.println)
writer.close()
println("Archivo stats.txt generado con éxito.")

// Versión compilada:
import scala.io.Source
import java.io.PrintWriter
object AnalizarFrases {
  def main(args: Array[String]): Unit = {

    val ficheroEntrada = "frases.txt"
    val ficheroSalida = "stats.txt"

    val origen = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        val lineaProcesada = linea.trim.toLowerCase
        if (lineaProcesada.nonEmpty) {
          val numeroPalabras = lineaProcesada.split("\\s+").length
          destino.println(s"$lineaProcesada => $numeroPalabras")
        }
      }
    } finally {
      origen.close()
      destino.close()
    }
    println("Archivo stats.txt generado con éxito.")
  }
}

