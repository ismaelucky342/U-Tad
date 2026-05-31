class Rectangle(val width: Double, val height: Double) {
  // Método para calcular el área
  def area(): Double = {
    return width * height
  }
}

// Llamada en Scala (versión traducida)
val rect = new Rectangle(5.0, 10.0)
println(s"Area: ${rect.area()}")


// en scala puro

class Rectangle(val width: Double, val height: Double) {
  // Método para calcular el área (sin return)
  def area: Double = width * height
}

// Llamada en Scala (versión idiomática)
val rect = new Rectangle(5.0, 10.0)
println(s"Area: ${rect.area}")