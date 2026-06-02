/*===============================================================================
EJERCICIO 3 (1.5 puntos) - SCALA AVANZADO: CASE CLASSES Y PATTERN MATCHING
===============================================================================

TAREA:
Define un case class "Venta" con: producto (String), cantidad (Int), precio (Double)

Implementa funciones que:
1. Cree una lista de 5 ventas de productos variados
2. Use un for-comprehension con filter para obtener:
   - Todas las ventas con cantidad > 3
   - Todas las ventas con monto_total (cantidad * precio) > 100
3. Implementa una función que use pattern matching para clasificar ventas:
   - "Venta pequeña" si monto < 50
   - "Venta normal" si 50 <= monto < 200
   - "Venta grande" si monto >= 200
4. Calcula el promedio de precio usando foldLeft()

EJEMPLO:
val ventas = List(
  Venta("Laptop", 1, 800.0),
  Venta("Monitor", 2, 150.0),
  Venta("Teclado", 5, 30.0),
  ...
)

SALIDA ESPERADA:
Venta grande: Laptop ($800.00)
Venta normal: Monitor ($300.00)
Venta normal: Teclado ($150.00)
Promedio de precio: $293.33

PISTAS:
- Case class syntax: case class Nombre(campo1: Tipo, campo2: Tipo, ...)
- Pattern matching con match/case
- FoldLeft para reducción: lista.foldLeft(inicial)((acum, elem) => ...)
*/

case class Venta(producto: String, cantidad: Int, precio: Double)

// Paso 1: Crear lista de ventas

val ventas = List(
  Venta("Laptop", 1, 800.0),
  Venta("Monitor", 2, 150.0),
  Venta("Teclado", 5, 30.0),
  Venta("Mouse", 10, 20.0),
  Venta("Impresora", 3, 120.0)
)

// Paso 2: Filtrar ventas
val ventasCantidadMayor3 = for {
  venta <- ventas
  if venta.cantidad > 3
} yield venta

val ventasMontoMayor100 = for {
  venta <- ventas
  if venta.cantidad * venta.precio > 100
} yield venta

// Paso 3: Clasificar ventas con pattern matching
def clasificarVenta(venta: Venta): String = {
  val montoTotal = venta.cantidad * venta.precio
  montoTotal match {
    case m if m < 50 => s"Venta pequeña: ${venta.producto} ($${m.formatted("%.2f")})"
    case m if m >= 50 && m < 200 => s"Venta normal: ${venta.producto} ($${m.formatted("%.2f")})"
    case m if m >= 200 => s"Venta grande:
    ${venta.producto} ($${m.formatted("%.2f")})"
    }
}

ventas.foreach(venta => println(clasificarVenta(venta)))

// Paso 4: Calcular promedio de precio
val promedioPrecio = ventas.foldLeft(0.0)((acum, venta) => acum + venta.precio) / ventas.length

println(s"Promedio de precio: $${promedioPrecio.formatted("%.2f")}")

