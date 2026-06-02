/* original modelo 24/25
 Vamos a crear un ejemplo sencillo en Scala para demostrar que **el alumno sabe ejecutar un código Scala tanto en Ejecución interact 
 Escribe un programa en Scala que **lea un archivo de texto llamado `frasescelebres.txt`, convierta cada línea a minúsculas, invierta el orden de los caracteres de cada línea y guarde el resultado en un nuevo archivo llamado `output.txt`** para la opción 1 que se comenta abajo y `output2.txt` para la opción 2. **La ruta y nombre de los ficheros de entrada y salida tienen que ser variables de tipo `val`.**
 
 **Pista:** usa las funciones `toLowerCase` para convertir a minúsculas y `reverse` para invertir el orden de los caracteres en cada línea.
 
 **Se pide:**
 1. Líneas de código y pantallazo de la ejecución del código en la consola REPL (Modo Dinámico). También el fichero salida `output1.txt`
 2. Fichero `.scala` y pantallazo de la ejecución en modo compilado (Modo Estático). También el fichero salida `output2.txt`
 
 **Ejemplo de salida esperada en ambos casos:**
 
 ```
 nonnel nhoj - .senalp sorto odneicah odapuco satse sartneim asap euq ol se adiv ali
 hdnag amtaham - .onimac le se zap al ,zap al arap onimac yah on
 sletotsira -.neib le recah ne etsisnoc dadicilef aredadrev al
 sboj evets - .secah euq ol rama se ojabart narg nu recah ed odom ocinu le
 ```
 */
 
// modo interactivo: 

import scala.io.Source
import java.io.PrintWriter

val ficheroEntrada = "frasescelebres.txt"
val ficheroSalida  = "output1.txt"

val lineas     = Source.fromFile(ficheroEntrada).getLines().toList
val procesadas = lineas.map(l => l.toLowerCase.reverse)

val writer = new PrintWriter(ficheroSalida)
procesadas.foreach(writer.println)
writer.close()

println("Archivo output1.txt generado con éxito.")

// modo compilado:
import scala.io.Source
import java.io.PrintWriter

object ProcesarFrases {
  def main(args: Array[String]): Unit = {

    // Rutas declaradas como val, tal como exige el enunciado
    val ficheroEntrada = "frasescelebres.txt"
    val ficheroSalida  = "output2.txt"

    val origen  = Source.fromFile(ficheroEntrada)
    val destino = new PrintWriter(ficheroSalida)

    try {
      for (linea <- origen.getLines()) {
        val lineaProcesada = linea.toLowerCase.reverse
        destino.println(lineaProcesada)
      }
    } finally {
      // finally se ejecuta SIEMPRE, aunque haya un error
      origen.close()
      destino.close()
    }

    println("Proceso finalizado con éxito.")
  }
}