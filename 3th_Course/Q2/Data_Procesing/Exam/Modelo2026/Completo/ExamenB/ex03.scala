/*===============================================================================
EJERCICIO 3 (1.5 puntos) - SCALA AVANZADO: CASE CLASSES
=======================================================

TAREA:

Define:

case class Producto(
nombre:String,
categoria:String,
precio:Double,
stock:Int
)

Implementa:

1. Crear una lista de 6 productos

2. Usar for-comprehension para obtener:

   * Productos con precio > 50€
   * Productos con stock < 10

3. Usar pattern matching para clasificar stock:

   0        -> "Sin stock"
   1-10     -> "Stock bajo"
   11-50    -> "Stock medio"

   > 50      -> "Stock alto"

4. Calcular precio promedio por categoría usando foldLeft()

5. Encontrar producto más caro

EJEMPLO:

val productos = List(
Producto("Monitor","Electrónica",220,20),
Producto("Teclado","Electrónica",45,8),
Producto("Auriculares","Electrónica",65,15)
)

SALIDA ESPERADA:

=== CLASIFICACIÓN STOCK ===

Teclado: Stock bajo
Monitor: Stock medio
Auriculares: Stock medio

=== PROMEDIO POR CATEGORÍA ===

Electrónica: 110€

=== PRODUCTO MÁS CARO ===

Monitor: 220€

PISTAS:

* Case class con 4 campos
* Pattern matching por rangos
* FoldLeft para cálculos
*/

case class Producto(nombre: String, categoria: String, precio: Double, stock: Int)

val productos = List(
  Producto("Monitor", "Electrónica", 220, 20),
  Producto("Teclado", "Electrónica", 45, 8),
  Producto("Auriculares", "Electrónica", 65, 15),
  Producto("Silla", "Muebles", 150, 5),
  Producto("Mesa", "Muebles", 300, 12),
  Producto("Lámpara", "Decoración", 80, 0)
)

val productosPrecioMayor50 = for {
  producto <- productos
  if producto.precio > 50
} yield producto

val productosStockMenor10 = for {
  producto <- productos
  if producto.stock < 10
} yield producto

def clasificarStock(stock: Int): String = stock match {
  case 0 => "Sin stock"
  case s if s >= 1 && s <= 10 => "Stock bajo"
  case s if s >= 11 && s <= 50 => "Stock medio"
  case s if s > 50 => "Stock alto"
}

println("=== CLASIFICACIÓN STOCK ===")

productos.foreach { producto =>
  println(s"${producto.nombre}: ${clasificarStock(producto.stock)}")
}

println("\n=== PROMEDIO POR CATEGORÍA ===")

val categorias = productos.map(_.categoria).distinct

categorias.foreach { categoria =>
  val productosCategoria = productos.filter(_.categoria == categoria)
  val promedio = productosCategoria.foldLeft(0.0)((acum, p) => acum + p.precio) / productosCategoria.length
  println(s"$categoria: ${promedio.formatted("%.2f")}€")
}

println("\n=== PRODUCTO MÁS CARO ===")

val productoMasCaro = productos.reduceLeft((p1, p2) => if (p1.precio > p2.precio) p1 else p2)

println(s"${productoMasCaro.nombre}: ${productoMasCaro.precio.formatted("%.2f")}€")