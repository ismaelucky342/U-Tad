import scala.util.Try

case class Venta(producto: String, unidades: Int, precio: Double)

object Bloque1:

  // Ejercicio 2
  def inc(x: Int): Int =
    // TODO
    x

  def doble(x: Int): Int =
    // TODO
    x

  def clamp(x: Int, min: Int, max: Int): Int =
    // TODO
    x

  // Ejercicio 3
  def ingresos(v: Venta): Double =
    // TODO
    0.0

  // Ejercicio 4
  def parseInt(s: String): Option[Int] =
    // TODO
    None

  def parseDouble(s: String): Option[Double] =
    // TODO
    None

  // Ejercicio 5
  def dividir(a: String, b: String): Option[Double] =
    // TODO (usa for-comprehension con Option)
    None

  // Ejercicio 7
  def parseVenta(line: String): Option[Venta] =
    // TODO (split + pattern matching + parseos)
    None

@main def mainBloque1(): Unit =
  // Ejercicio 1 — Variables y tipos
  val nombre: String = "TODO"
  val anioNacimiento: Int = 0
  var visitasPerfil: Int = 0

  // TODO incrementa 3 veces

  val edadAprox = 2026 - anioNacimiento
  println(s"nombre=$nombre edadAprox=$edadAprox visitas=$visitasPerfil")

  // Ejercicio 2 — pruebas rápidas
  assert(Bloque1.inc(4) == 5)
  assert(Bloque1.doble(7) == 14)
  assert(Bloque1.clamp(5, 0, 10) == 5)
  assert(Bloque1.clamp(-2, 0, 10) == 0)
  assert(Bloque1.clamp(99, 0, 10) == 10)

  // Ejercicio 3 — case class + ingresos
  val ventas = List(
    Venta("A", 2, 10.0),
    Venta("B", 1, 15.0),
    Venta("A", 1, 10.0),
    Venta("C", 10, 1.25)
  )

  ventas.foreach { v =>
    val ing = Bloque1.ingresos(v)
    println(s"$v => ingresos=$ing")
  }

  val vMod = ventas.head.copy(unidades = ventas.head.unidades + 1)
  println(s"copy: $vMod => ingresos=${Bloque1.ingresos(vMod)}")

  // Ejercicio 4 — Option parse
  assert(Bloque1.parseInt("10") == Some(10))
  assert(Bloque1.parseInt("x").isEmpty)
  assert(Bloque1.parseDouble("1.5").contains(1.5))

  // Ejercicio 5 — dividir con Option
  assert(Bloque1.dividir("10", "2").contains(5.0))
  assert(Bloque1.dividir("10", "0").isEmpty)
  assert(Bloque1.dividir("x", "2").isEmpty)

  // Ejercicio 6 — transformaciones
  val nombres = List("  Ana ", "", "Pepe", "  maria", "MARIA ")
  val normalizados =
    // TODO: trim + lower + no vacíos + distinct + sorted
    List.empty[String]

  println(s"normalizados=$normalizados")
  assert(normalizados == List("ana", "maria", "pepe"))

  // Ejercicio 7 — mini CSV
  val lineas = List(
    "A,2,10.0",
    "B,1,15.0",
    "A,x,10.0",
    "MALFORMADA"
  )

  val ventasValidas = lineas.flatMap(Bloque1.parseVenta)
  val totalIngresos = ventasValidas.map(v => v.unidades * v.precio).sum

  println(s"ventasValidas=$ventasValidas")
  println(s"totalIngresos=$totalIngresos")
