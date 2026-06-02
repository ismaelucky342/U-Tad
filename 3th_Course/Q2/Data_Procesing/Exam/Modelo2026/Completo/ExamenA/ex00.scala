/*
===============================================================================
EJERCICIO 1 (1.5 puntos) - SCALA BÁSICO: PROCESAMIENTO DE ARCHIVOS
===============================================================================

Se proporciona un archivo "temperaturas.txt" con lecturas de temperatura en 
grados Celsius, una temperatura por línea.

TAREA:
Implementa un programa Scala que:
1. Lea todas las temperaturas del archivo
2. Convierta cada temperatura de Celsius a Fahrenheit (F = C * 9/5 + 32)
3. Guarde el resultado en "temperaturas_fahrenheit.txt" con el formato:
   "X°C = Y°F" (una conversión por línea)
4. Mostrar en consola: temperatura mínima, máxima y promedio en Fahrenheit

EJEMPLO DE ENTRADA (temperaturas.txt):
20
25
15
30

EJEMPLO DE SALIDA (temperaturas_fahrenheit.txt):
20°C = 68.0°F
25°C = 77.0°F
15°C = 59.0°F
30°C = 86.0°F

Consola:
Mín: 59.0°F, Máx: 86.0°F, Promedio: 72.5°F

PISTAS:
- Usa scala.io.Source.fromFile() para leer
- Usa map() para transformar
- No olvides cerrar los recursos
*/
val ficheroEntrada = "temperaturas.txt"

import scala.io.Source
import java.io.PrintWriter

val lineas = Source.fromFile(ficheroEntrada).getLines().toList
val temperaturasF = lineas.map { linea =>
  val tempC = linea.toDouble
  val tempF = tempC * 9.0 / 5.0 + 32.0
  (tempC, tempF)
}

val writer = new PrintWriter("temperaturas_fahrenheit.txt")
temperaturasF.foreach { case (tempC, tempF) =>
  writer.println(s"$tempC°C = ${tempF.formatted("%.1f")}°F")
}
writer.close()

val tempFValues = temperaturasF.map(_._2)
val minTempF = tempFValues.min
val maxTempF = tempFValues.max
val avgTempF = tempFValues.sum / tempFValues.size

println(s"Mín: ${minTempF.formatted("%.1f")}°F, Máx: ${maxTempF.formatted("%.1f")}°F, Promedio: ${avgTempF.formatted("%.1f")}°F")