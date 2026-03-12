// =================================================================================================== //
//                                                                                                     //
//                                                       ██╗   ██╗   ████████╗ █████╗ ██████╗          //
//     Procesamiento de datos - AEC1                     ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗         //
//                                                       ██║   ██║█████╗██║   ███████║██║  ██║         //
//     created:        01/03/2026  -  10:00:00           ██║   ██║╚════╝██║   ██╔══██║██║  ██║         //
//     last change:    07/03/2026  -  18:35:50           ╚██████╔╝      ██║   ██║  ██║██████╔╝         //
//                                                        ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝          //
//                                                                                                     //
//     Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com               //
//                                                                                                     // 
//     Github:                                           https://github.com/ismaelucky342              // 
//                                                                                                     // 
// =================================================================================================== // 

// Programa 1: gestión de notas de una clase usando programación funcional en Scala.
// La idea es trabajar con una lista de notas y hacer distintas operaciones sobre ella
// sin tocar el estado original, solo transformaciones.

object Programa1 {

  // devuelve la media de la lista; si llega vacía devuelve 0 para no petar con división por cero
  def calcularMedia(lista: List[Double]): Double =
    if (lista.isEmpty) 0.0
    else lista.sum / lista.length

  // convierte una nota numérica en su calificación textual
  // uso pattern matching con guards porque queda mucho más limpio que un if anidado
  def clasificarNota(nota: Double): String = nota match {
    case n if n >= 9.0             => "Sobresaliente"
    case n if n >= 7.0 && n < 9.0 => "Notable"
    case n if n >= 5.0 && n < 7.0 => "Aprobado"
    case _                         => "Suspenso"
  }

  // recibe Any porque quiero demostrar que Scala puede manejar cualquier tipo en la misma lista
  // luego con pattern matching identificamos qué tipo es realmente cada elemento
  def describir(valor: Any): String = valor match {
    case i: Int    => s"Entero:   $i"
    case d: Double => s"Decimal:  $d"
    case s: String => s"Texto:    \"$s\""
    case b: Boolean => s"Booleano: $b"
    case l: List[_] => s"Lista:    ${l.mkString("[", ", ", "]")}"
    case _          => s"Tipo desconocido: $valor"
  }

  // función de orden superior: le paso una transformación y la aplica a todas las notas
  // así puedo reutilizarla para cualquier operación sin duplicar código
  def transformarNotas(notas: List[Double], f: Double => Double): List[Double] =
    notas.map(f)

  def main(args: Array[String]): Unit = {

    println("=" * 55)
    println("  PROGRAMA 1 - Gestión de notas en Scala")
    println("=" * 55)

    // val para que sea inmutable, no tiene sentido modificar las notas originales
    val notas: List[Double] = List(8.5, 7.0, 9.2, 6.3, 5.8, 8.1, 7.7, 4.5, 6.0, 9.8)

    println(s"\nNotas originales: ${notas.mkString(", ")}")

    // filter devuelve una nueva lista con los que superan el 5, sin modificar notas
    val aprobados: List[Double] = notas.filter(_ >= 5.0)
    println(s"\nAprobados (>= 5.0): ${aprobados.mkString(", ")}")

    // uso transformarNotas para añadir 0.5 de bono a cada nota (sin pasarse de 10)
    val notasConBono: List[Double] = transformarNotas(notas, n => Math.min(n + 0.5, 10.0))
    println(s"Notas con bono +0.5 (max 10): ${notasConBono.mkString(", ")}")

    // map para generar una lista de tuplas (nota, calificacion)
    val notasConCalificacion: List[(Double, String)] =
      notas.map(n => (n, clasificarNota(n)))

    println("\nCalificaciones:")
    notasConCalificacion.foreach { case (nota, cal) =>
      println(f"  $nota%4.1f  ->  $cal")
    }

    // foldLeft recorre la lista acumulando la suma, empezando en 0.0
    val sumaTotal: Double = notas.foldLeft(0.0)(_ + _)
    val media: Double     = calcularMedia(notas)

    println(s"\nSuma total  : $sumaTotal")
    println(f"Media       : $media%.2f")

    // groupBy agrupa las notas por su calificación, genera un Map de golpe
    val agrupadas: Map[String, List[Double]] = notas.groupBy(clasificarNota)

    println("\nAgrupacion por calificacion:")
    // los Map no garantizan orden, así que ordeno por clave antes de imprimir
    agrupadas.toSeq.sortBy(_._1).foreach { case (cal, lista) =>
      println(s"  $cal: ${lista.mkString(", ")}")
    }

    // sortBy con negativo para ordenar de mayor a menor
    val notasOrdenadas: List[Double] = notas.sortBy(-_)
    println(s"\nRanking (de mayor a menor): ${notasOrdenadas.mkString(", ")}")

    // partition separa en dos listas según el predicado, devuelve una tupla
    val (suspensos, noSuspensos) = notas.partition(_ < 5.0)
    println(s"Suspensos   : ${suspensos.mkString(", ")}")
    println(s"No suspensos: ${noSuspensos.mkString(", ")}")

    // --- tipo Any ---
    // meto distintos tipos en la misma lista, posible porque Any es el supertipo de todo en Scala
    val elementosMixtos: List[Any] = List(42, "Scala", 3.14, true, List(1, 2, 3))
    println("\n--- Lista con tipo Any ---")
    elementosMixtos.foreach(e => println(s"  ${describir(e)}"))

    println("\nPrograma 1 completado.")
  }
}
