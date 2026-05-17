//# VARIANTE 1: Filtrado y Multiplicación de elementos con separador alternativo
//
//Dado el siguiente RDD en Spark:
//
//```scala
//val dataset = sc.parallelize(List("2;3;4", "1;5", "6;2"))
//
//```
//
//Cada elemento es una cadena que representa números separados por **puntos y comas (`;`)**.
//Aplica transformaciones de Spark y colecciones de Scala para obtener el **producto (multiplicación) total de todos los números que sean mayores o iguales a 2**. El resultado final esperado es **288** (ya que el `1` debe quedar excluido del cálculo: $2 \times 3 \times 4 \times 5 \times 6 \times 2 = 288$).
//
//Implementa **dos versiones diferentes** para resolverlo:
//
//* **Versión A:** Utiliza exclusivamente `flatMap()`, `filter()`, `map()` y la acción `reduce()` de Spark.
//* **Versión B:** Utiliza exclusivamente `map()` (donde harás el procesamiento por línea usando funciones de Scala como `split`, `filter`, `map` y `product`) y finalmente la acción `reduce()` de Spark para combinar los resultados de las líneas.
//
//---

// Versión A: Usando `flatMap()`, `filter()`, `map()` y `reduce()`

val dataset = sc.parallelize(List("2;3;4", "1;5", "6;2"))

val numeros = dataset.flatMap(linea => linea.split(";") // Convertir cada línea en números individuales
                     .map(_.toInt) // Convertir a enteros
                     .filter(_ >= 2) // Filtrar números menores que 2
                     .reduce(_ * _) // Multiplicar todos los números restantes

println(s"Producto total: $numeros")


// Versión B: Usando `map()` y funciones de Scala

val dataset = sc.parallelize(List("2;3;4", "1;5", "6;2"))

val productosPorLinea = dataset.map(linea => {
  val numeros = linea.split(";").map(_.toInt).filter(_ >= 2) // Procesar cada línea: convertir a números, filtrar y obtener el producto
  if (numeros.nonEmpty) numeros.product else 1 // Si no hay números válidos, devolver 1 para no afectar el producto final
})

val productoTotal = productosPorLinea.reduce(_ * _) // Multiplicar los productos de cada línea

println(s"Producto total: $productoTotal")