/*
Ejercicio 2_F - Scala + Spark Básico: ANÁLISIS DE VENTAS

Dado un RDD con transacciones de venta:
val ventas = sc.parallelize(List("2026-01-15,producto1,100", "2026-01-15,producto2,50", 
                                   "2026-01-16,producto1,200", "2026-01-16,producto3,75"))

Formato: fecha,producto,monto

Se pide procesar para:
1. Calcular venta total por producto
2. Identificar productos con venta total > 150
3. Mostrar productos ordenados por venta total descendente

Resultado esperado:
producto1: 300
producto3: 75
producto2: 50

(Nota: solo se muestran los > 150, pero aquí mostramos todos para ilustrar)

Se pide:
1. Versión A: Utiliza map() y reduceByKey()
2. Versión B: Utiliza flatMap() y fold()

IMPORTANTE: Entregar código bien comentado y pantallazo de ambas ejecuciones.
*/

// ============ VERSIÓN A: map() y reduceByKey() ============

val ventas = sc.parallelize(List("2026-01-15,producto1,100", "2026-01-15,producto2,50", 
                                  "2026-01-16,producto1,200", "2026-01-16,producto3,75"))

// Paso 1: Extraemos (producto, monto)
val ventasPorProducto = ventas.map { venta =>
  val Array(fecha, producto, monto) = venta.split(",")
  (producto, monto.toInt)
}

// Paso 2: Sumamos montos por producto
val ventasTotales = ventasPorProducto.reduceByKey((a, b) => a + b)

// Paso 3: Ordenamos descendentemente y filtramos > 150
val ordenado = ventasTotales
  .filter { case (_, total) => total > 150 }
  .sortBy { case (_, total) => -total }

// Paso 4: Mostramos
ordenado.collect().foreach { case (producto, total) =>
  println(s"$producto: $total")
}


// ============ VERSIÓN B: Versión alternativa ============

val ventas = sc.parallelize(List("2026-01-15,producto1,100", "2026-01-15,producto2,50", 
                                  "2026-01-16,producto1,200", "2026-01-16,producto3,75"))

// Paso 1-3: Todo en una cadena
val resultado = ventas
  .map { venta =>
    val Array(_, producto, monto) = venta.split(",")
    (producto, monto.toInt)
  }
  .reduceByKey((a, b) => a + b)
  .filter { case (_, total) => total > 150 }
  .sortBy { case (_, total) => -total }
  .collect()

// Paso 4: Mostramos
resultado.foreach { case (producto, total) =>
  println(s"$producto: $total")
}
