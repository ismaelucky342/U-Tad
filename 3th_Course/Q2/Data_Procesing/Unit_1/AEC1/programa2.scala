// ===================================================================================================
//                                                                                                   
//                                                       ██╗   ██╗   ████████╗ █████╗ ██████╗       
//     Procesamiento de datos - AEC1                     ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗      
//                                                       ██║   ██║█████╗██║   ███████║██║  ██║      
//     created:        01/03/2026  -  10:00:00           ██║   ██║╚════╝██║   ██╔══██║██║  ██║      
//     last change:    07/03/2026  -  18:35:50           ╚██████╔╝      ██║   ██║  ██║██████╔╝      
//                                                        ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝       
//                                                                                                   
//     Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com            
//                                                                                                   
//     Github:                                           https://github.com/ismaelucky342           
//                                                                                                   
// ===================================================================================================

// Programa 2: modelado de estudiantes con case class, lectura de fichero y filtrado.
// Lo he organizado para cubrir todos los requisitos del ejercicio 3 de la práctica.

import scala.io.Source
import scala.util.Try
import java.io.{File, PrintWriter}

// defino la case class fuera del objeto para que sea accesible desde cualquier parte
// tiene 5 atributos de tipos distintos como pide el enunciado
// la ventaja de case class es que ya nos da toString, equals y copy sin escribir nada
case class Estudiante(
  id:     Int,
  nombre: String,
  edad:   Int,
  nota:   Double,
  curso:  String
)

object Programa2 {

  // intenta convertir una línea de texto en un Estudiante
  // devuelve Option para no reventar si la línea está mal formada
  // el separador viene como parámetro para que sea reutilizable con distintos formatos
  def parsearLinea(linea: String, separador: String): Option[Estudiante] = {
    val partes = linea.split(separador)
    if (partes.length == 5) {
      // Try para capturar errores de conversión (p.ej. si la nota no es un número)
      // toOption convierte el resultado en Some o None directamente
      Try(
        Estudiante(
          id     = partes(0).trim.toInt,
          nombre = partes(1).trim,
          edad   = partes(2).trim.toInt,
          nota   = partes(3).trim.toDouble,
          curso  = partes(4).trim
        )
      ).toOption
    } else {
      None
    }
  }

  // versión imperativa: uso var y un bucle para construir el Map manualmente
  // la incluyo para comparar con la versión funcional y ver la diferencia de código
  def agruparPorCursoImperativo(es: List[Estudiante]): Map[String, List[Estudiante]] = {
    var resultado = Map[String, List[Estudiante]]()
    for (e <- es) {
      val listaActual = resultado.getOrElse(e.curso, List())
      resultado = resultado + (e.curso -> (listaActual :+ e))
    }
    resultado
  }

  // versión funcional: una línea, sin estado mutable, mucho más limpio
  def agruparPorCursoFuncional(es: List[Estudiante]): Map[String, List[Estudiante]] =
    es.groupBy(_.curso)

  // escribe la lista de estudiantes en un fichero con el mismo formato ';' del de entrada
  def escribirFichero(estudiantes: List[Estudiante], ruta: String): Unit = {
    val pw = new PrintWriter(new File(ruta))
    pw.println("# filtrado: nota >= 7.0 y edad <= 22")
    pw.println("# id;nombre;edad;nota;curso")
    estudiantes.foreach(e =>
      pw.println(s"${e.id};${e.nombre};${e.edad};${e.nota};${e.curso}")
    )
    pw.close()
    println(s"  -> escrito en: $ruta")
  }

  def main(args: Array[String]): Unit = {

    println("=" * 55)
    println("  PROGRAMA 2 - Estudiantes, ficheros y case class")
    println("=" * 55)

    val cursos = List("Matematicas", "Fisica", "Informatica", "Quimica", "Historia")

    // genero 10 instancias automáticamente usando un Range y map
    // los valores son consecutivos: edades de 19 a 28, notas crecientes
    val estudiantesGenerados: List[Estudiante] = (1 to 10).map { i =>
      Estudiante(
        id     = i,
        nombre = s"Estudiante_$i",
        edad   = 18 + i,
        nota   = Math.min(4.5 + i * 0.55, 10.0),
        curso  = cursos((i - 1) % cursos.length)
      )
    }.toList

    println(s"\n[1] Estudiantes generados (${estudiantesGenerados.length}):")
    estudiantesGenerados.foreach(e =>
      println(f"  ${e.id}%2d | ${e.nombre}%-15s | edad ${e.edad} | nota ${e.nota}%4.2f | ${e.curso}")
    )

    // el separador va como parámetro para que parsearLinea sea flexible
    val separador   = ";"
    val rutaEntrada = "estudiantes.txt"

    println(s"\n[2] Leyendo: $rutaEntrada")

    // cadena funcional sobre el iterador de líneas:
    // eliminamos comentarios, líneas vacías y las que no parsean bien
    val estudiantesArchivo: List[Estudiante] =
      Source.fromFile(rutaEntrada)
        .getLines()
        .filterNot(_.startsWith("#"))
        .filter(_.trim.nonEmpty)
        .flatMap(linea => parsearLinea(linea, separador))
        .toList

    println(s"  leidos del fichero: ${estudiantesArchivo.length}")

    // junto los dos grupos con ++
    val todosEstudiantes: List[Estudiante] = estudiantesGenerados ++ estudiantesArchivo
    println(s"  total: ${todosEstudiantes.length}")

    println("\n[3] Agrupacion por curso:")

    val agrupacionFuncional  = agruparPorCursoFuncional(todosEstudiantes)
    val agrupacionImperativa = agruparPorCursoImperativo(todosEstudiantes)

    agrupacionFuncional.toSeq.sortBy(_._1).foreach { case (curso, lista) =>
      println(s"  $curso (${lista.length}): ${lista.map(_.nombre).mkString(", ")}")
    }

    // compruebo que las dos implementaciones llegan al mismo resultado
    println(s"\n  implementaciones equivalentes: ${agrupacionFuncional == agrupacionImperativa}")

    // filtro con dos condiciones: nota buena Y estudiante joven
    println("\n[4] Filtrado: nota >= 7.0 AND edad <= 22")

    val filtrados: List[Estudiante] =
      todosEstudiantes.filter(e => e.nota >= 7.0 && e.edad <= 22)

    println(s"  cumplen ambas condiciones: ${filtrados.length}")
    filtrados.foreach(e =>
      println(f"  ${e.id}%2d | ${e.nombre}%-15s | edad ${e.edad} | nota ${e.nota}%4.2f | ${e.curso}")
    )

    println(s"\n[5] Escribiendo resultado:")
    escribirFichero(filtrados, "estudiantes_filtrados.txt")

    println("\nPrograma 2 completado.")
    println("=" * 55)
  }
}
