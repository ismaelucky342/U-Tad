import scala.util.{Try, Success, Failure}

case class Venta(producto: String, unidades: Int, precio: Double)

object Bloque2:

  def ingresos(v: Venta): Double = v.unidades * v.precio

  // Ejercicio 1
  def unidadesPorProducto(ventas: List[Venta]): Map[String, Int] =
    // TODO
    Map.empty

  def ingresosPorProducto(ventas: List[Venta]): Map[String, Double] =
    // TODO
    Map.empty

  // Ejercicio 2
  def topKUnidades(unidades: Map[String, Int], k: Int): List[(String, Int)] =
    // TODO
    Nil

  // Ejercicio 3
  def totalUnidadesFold(ventas: List[Venta]): Int =
    // TODO
    0

  def totalIngresosFold(ventas: List[Venta]): Double =
    // TODO
    0.0

  // Ejercicio 4
  def etiqueta(v: Venta): String =
    // TODO (pattern matching)
    "TODO"

  // Ejercicio 5
  def parsePositivo(s: String): Either[String, Int] =
    // TODO
    Left("TODO")

  def parseDoubleE(s: String): Either[String, Double] =
    // TODO
    Left("TODO")

  def parseVentaE(line: String): Either[String, Venta] =
    // TODO
    Left("TODO")

  def separarResultados[A](xs: List[Either[String, A]]): (List[A], List[String]) =
    // TODO: (validos, errores)
    (Nil, Nil)

  // Ejercicio 6
  def parseIntOpt(s: String): Option[Int] =
    // TODO
    None

  def parseIntTry(s: String): Try[Int] =
    // TODO
    Try(0)

  // Ejercicio 7
  def dividirE(a: String, b: String): Either[String, Double] =
    // TODO (for-comprehension sobre Either)
    Left("TODO")

@main def mainBloque2(): Unit =
  val ventas = List(
    Venta("A", 2, 10.0),
    Venta("B", 1, 15.0),
    Venta("A", 1, 10.0),
    Venta("C", 10, 1.25),
    Venta("B", 7, 2.0)
  )

  // Ejercicio 1
  val u = Bloque2.unidadesPorProducto(ventas)
  val i = Bloque2.ingresosPorProducto(ventas)
  println(s"unidadesPorProducto=$u")
  println(s"ingresosPorProducto=$i")

  // Ejercicio 2
  val top3 = Bloque2.topKUnidades(u, 3)
  println(s"top3=$top3")

  // Ejercicio 3
  println(s"totalUnidadesFold=${Bloque2.totalUnidadesFold(ventas)}")
  println(s"totalIngresosFold=${Bloque2.totalIngresosFold(ventas)}")

  // Ejercicio 4
  ventas.foreach(v => println(s"${v.producto} => ${Bloque2.etiqueta(v)}"))

  // Ejercicio 5
  val lineas = List(
    "A,2,10.0",
    "B,1,15.0",
    "A,0,10.0",
    "A,x,10.0",
    "MALFORMADA"
  )

  val parsed = lineas.map(Bloque2.parseVentaE)
  val (validas, errores) = Bloque2.separarResultados(parsed)
  println(s"validas=$validas")
  println(s"errores=$errores")

  // Ejercicio 6
  println(Bloque2.parseIntOpt("10"))
  println(Bloque2.parseIntOpt("x"))

  val t1 = Bloque2.parseIntTry("10")
  val t2 = Bloque2.parseIntTry("x")
  println(s"try10=$t1")
  println(s"tryX=$t2")

  val vOpt = Bloque2.parseIntOpt("x").getOrElse(-1)
  val vTry = Bloque2.parseIntTry("x").getOrElse(-1)
  println(s"defaults opt=$vOpt try=$vTry")

  val msgTry = Bloque2.parseIntTry("x") match
    case Success(n) => s"ok: $n"
    case Failure(e) => s"error: ${e.getMessage}"
  println(msgTry)

  // Ejercicio 7
  println(Bloque2.dividirE("10", "2"))
  println(Bloque2.dividirE("10", "0"))
  println(Bloque2.dividirE("x", "2"))
