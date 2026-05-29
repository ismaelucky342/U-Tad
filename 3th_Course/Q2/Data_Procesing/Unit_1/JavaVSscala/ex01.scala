// contraparte de la clase para modelar rectangulo en scala

class Rectangulo(val ancho: Double, val alto: Double) {
  // metodos area y perimetro
  def area(): Double = 
  {
     return ancho * alto
  }
  def perimetro(): Double = 
  {
    return 2 * (ancho + alto)
  }
}

// Llamada en Scala (versión traducida)
val rect = new Rectangulo(5.0, 10.0)
println(s"Area: ${rect.area()}")
println(s"Perimetro: ${rect.perimetro()}")

// con estilo scala puro

case class Rectangulo(ancho: Double, alto: Double) {
  def area: Double = ancho * alto
  def perimetro: Double = 2 * (ancho + alto) // sin return
}

// Llamada en Scala (versión traducida)
val rect = Rectangulo(5.0, 10.0)
println(s"Area: ${rect.area}")
println(s"Perimetro: ${rect.perimetro}")