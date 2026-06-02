/*
Ejercicio 2_C - Scala + Spark Básico: FILTRADO Y TRANSFORMACIÓN DE PRECIOS

Dado un RDD que contiene productos con precios:
val productos = sc.parallelize(List("laptop,1200", "mouse,25", "teclado,80", "monitor,350"))

Se pide procesar el RDD para:
1. Filtrar únicamente productos con precio > 50
2. Aplicar un descuento del 10% a los precios
3. Contar cuántos productos quedan tras el filtrado

Resultado esperado:
laptop: 1080.0
teclado: 72.0
monitor: 315.0
Total de productos con descuento: 3

Se pide:
1. Versión A: Utiliza map() y filter()
2. Versión B: Utiliza flatMap() y fold()

IMPORTANTE: Entregar código bien comentado y pantallazo de ambas ejecuciones.
*/

// ============ VERSIÓN A: map() y filter() ============

val productos = sc.parallelize(List("laptop,1200", "mouse,25", "teclado,80", "monitor,350"))

// Paso 1: Convertimos cada producto a una tupla (nombre, precio)
val productosTupla = productos.map { linea =>
  val Array(nombre, precioStr) = linea.split(",")
  (nombre, precioStr.toDouble)
}

// Paso 2: Filtramos productos con precio > 50 y aplicamos descuento
val productosFiltrados = productosTupla
  .filter { case (_, precio) => precio > 50 }
  .map { case (nombre, precio) => (nombre, precio * 0.9) }

// Paso 3: Mostramos resultados
val resultado = productosFiltrados.collect()
resultado.foreach { case (nombre, precioFinal) =>
  println(s"$nombre: $precioFinal")
}

println(s"Total de productos con descuento: ${resultado.length}")


// ============ VERSIÓN B: flatMap() y fold() ============

val productos = sc.parallelize(List("laptop,1200", "mouse,25", "teclado,80", "monitor,350"))

// Paso 1: Convertimos a tuplas y filtramos
val productosFiltrados = productos.flatMap { linea =>
  val Array(nombre, precioStr) = linea.split(",")
  val precio = precioStr.toDouble
  if (precio > 50) List((nombre, precio * 0.9)) else List()
}

// Paso 2: Recogemos y mostramos
val resultado = productosFiltrados.collect()
resultado.foreach { case (nombre, precioFinal) =>
  println(s"$nombre: $precioFinal")
}

println(s"Total de productos con descuento: ${resultado.length}")
