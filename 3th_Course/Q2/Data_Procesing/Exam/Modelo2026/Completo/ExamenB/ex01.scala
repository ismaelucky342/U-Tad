/*===============================================================================
EJERCICIO 1 (1.5 puntos) - SCALA: PROCESAMIENTO DE ARCHIVOS
===========================================================

Se proporciona un archivo "temperaturas.txt" con temperaturas en grados
Celsius, una temperatura por línea.

TAREA:
Implementa un programa Scala que:

1. Lea todas las temperaturas desde el archivo

2. Convierta cada temperatura a Fahrenheit usando:

   F = (C × 1.8) + 32

3. Guarde los resultados en:

   "temperaturas_convertidas.txt"

   Formato:
   "Celsius: X -> Fahrenheit: Y"

4. Mostrar por consola:

   * Temperatura media
   * Temperatura máxima
   * Cuántas temperaturas superan los 30°C
   * Cuántas temperaturas están por debajo de 20°C

EJEMPLO DE ENTRADA (temperaturas.txt):

21.5
18.0
35.2
27.3
15.6

EJEMPLO DE SALIDA (temperaturas_convertidas.txt):

Celsius: 21.5 -> Fahrenheit: 70.7
Celsius: 18.0 -> Fahrenheit: 64.4
Celsius: 35.2 -> Fahrenheit: 95.36
Celsius: 27.3 -> Fahrenheit: 81.14
Celsius: 15.6 -> Fahrenheit: 60.08

Consola:

Media: 23.52°C
Máxima: 35.2°C
Mayores de 30°C: 1
Menores de 20°C: 2

PISTAS:

* Usa scala.io.Source.fromFile()
* Usa map(), count() y sum()
* Convierte String → Double
*/

val ficheroEntrada = "temperaturas.txt"
val ficheroSalida = "temperaturas_convertidas.txt"

import scala.io.Source
import java.io.PrintWriter

val lineas = Source.fromFile(ficheroEntrada).getLines().toList
val temperaturasC = lineas.map(_.toDouble)
val temperaturasF = temperaturasC.map(c => c * 1.8 + 32) 

val writer = new PrintWriter(ficheroSalida)
temperaturasC.zip(temperaturasF).foreach { case (c, f) =>
  writer.println(s"Celsius: $c -> Fahrenheit: ${f.formatted("%.2f")}")
}
writer.close()

val media = temperaturasC.sum / temperaturasC.size
val maxima = temperaturasC.max
val mayores30 = temperaturasC.count(_ > 30)
val menores20 = temperaturasC.count(_ < 20)

println(f"Media: ${media.formatted("%.2f")}°C")
println(f"Máxima: ${maxima.formatted("%.2f")}°C")
println(s"Mayores de 30°C: $mayores30")
println(s"Menores de 20°C: $menores20")