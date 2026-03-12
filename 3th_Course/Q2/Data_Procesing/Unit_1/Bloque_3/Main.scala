import scala.io.Source
import scala.concurrent.{ExecutionContext, Future}

case class Venta(producto: String, unidades: Int, precio: Double)

object Bloque3:

  def parsePositivoInt(s: String): Either[String, Int] =
    // TODO
    Left("TODO")

  def parsePrecio(s: String): Either[String, Double] =
    // TODO
    Left("TODO")

  // Ejercicio 1
  def parseVenta(line: String): Either[String, Venta] =
    // TODO (trim, validación, mensajes útiles)
    Left("TODO")

  def ingresos(v: Venta): Double = v.unidades * v.precio

  // Ejercicio 2
  def totalIngresos(ventas: List[Venta]): Double =
    // TODO
    0.0

  def ingresosPorProductoOrdenado(ventas: List[Venta]): List[(String, Double)] =
    // TODO (desc)
    Nil

  def productoTopUnidades(ventas: List[Venta]): Option[(String, Int)] =
    // TODO
    None

  // Ejercicio 3
  def renderInforme(ventasValidas: List[Venta], errores: List[String], totalLineas: Int): String =
    // TODO
    "TODO"

  // Ejercicio 4
  def procesar(lineas: List[String]): (List[Venta], List[String]) =
    // TODO: parsear todo a Either y separar
    (Nil, Nil)

  // Ejercicio 5 (opcional)
  def leerLineas(path: String): Either[String, List[String]] =
    // TODO (cerrar fichero)
    Left("TODO")

  // Ejercicio 6 (opcional)
  def procesarAsync(lineas: List[String])(using ec: ExecutionContext): Future[String] =
    // TODO
    Future.successful("TODO")

@main def mainBloque3(): Unit =
  val lineas = List(
    "A,2,10.0",
    "B,1,15.0",
    "A,3,10.0",
    "C,10,1.25",
    "A,x,10.0",
    "MALFORMADA"
  )

  val (ventasValidas, errores) = Bloque3.procesar(lineas)
  val informe = Bloque3.renderInforme(ventasValidas, errores, totalLineas = lineas.size)

  println(informe)

  // Opcional: ejemplo de async
  given ExecutionContext = ExecutionContext.global
  Bloque3.procesarAsync(lineas).foreach(println)
