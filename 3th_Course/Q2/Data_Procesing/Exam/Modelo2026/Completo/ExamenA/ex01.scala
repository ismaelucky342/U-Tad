/*
===============================================================================
EJERCICIO 2 (1.5 puntos) - SPARK RDD: TRANSFORMACIONES Y ACCIONES
===============================================================================

Se proporciona un archivo "productos.txt" con datos de ventas en formato:
producto_id,cantidad,precio_unitario

TAREA:
Implementa un programa Spark que:
1. Cargue los datos con sc.textFile()
2. Calcule el monto total de cada producto (cantidad * precio)
3. Use reduceByKey() para sumar montos por producto_id
4. Muestre los 5 productos con mayor monto de ventas
5. Calcula el monto total de TODAS las ventas

EJEMPLO DE ENTRADA (productos.txt):
A001,5,10.50
B002,3,20.00
A001,2,10.50
C003,7,15.00
B002,1,20.00

SALIDA ESPERADA:
Producto A001: $105.00 (7 unidades)
Producto C003: $105.00 (7 unidades)
Producto B002: $80.00 (4 unidades)
Monto total de ventas: $290.00

PISTAS:
- Parse cada línea: split(",") y conversión a tipos numéricos
- Crea tuplas (producto_id, monto)
- Use reduceByKey() para agregar por producto
- Use sortBy() para ordenar descendente

*/

val productos = sc.textFile("productos.txt")

val montosProducto = productos.map { linea =>
  val Array(productoId, cantidadStr, precioStr) = linea.split(",")
  val cantidad = cantidadStr.toInt
  val precioUnitario = precioStr.toDouble
  (productoId, cantidad * precioUnitario)
}

val ventasTotales = montosProducto.reduceByKey((a, b) => a + b)

val topProductos = ventasTotales.sortBy({ case (_, monto) => -monto }).take(5)

topProductos.foreach { case (productoId, monto) =>
  println(s"Producto $productoId: $$${monto.formatted("%.2f")}")
}

val montoTotalVentas = ventasTotales.map { case (_, monto) => monto }.sum()

println(s"Monto total de ventas: $$${montoTotalVentas.formatted("%.2f")}")

