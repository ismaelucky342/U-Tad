//VARIANTE 3: El "Join" manual y filtrado (Nivel Avanzado)
//
//ejercicio donde tenemos datos de dos fuentes distintas o necesitas "cruzar" información de manera sencilla.
//
//Dado el siguiente RDD con datos de usuarios y sus compras:
//Scala
//
//val compras = sc.parallelize(List("user1:100", "user2:50", "user1:20", "user3:300", "user2:15"))
//
//Cada elemento es "usuario:importe_gasto". Queremos obtener el gasto total por usuario, pero solo para aquellos usuarios que hayan gastado en total más de 100€. El resultado esperado debería ser únicamente (user3, 300) y (user1, 120) (el user2 se descarta porque suma 65€).
//
//Implementa una única versión que encadene los siguientes pasos de Spark de forma limpia:
//
//    Un map() para convertir el String en una tupla (Usuario, GastoEntero).
//
//    Una acción o transformación para combinar y sumar los gastos de cada usuario.
//
//    Un filter() (¡ojo, que aquí operas sobre tuplas!) para quedarte solo con los que superen los 100€.


// Versión A: Usando `map()`, `reduceByKey()` y `filter()`

val compras = sc.parallelize(List("user1:100", "user2:50", "user1:20", "user3:300", "user2:15"))

val gastosPorUsuario = compras.map(compra => {
  val partes = compra.split(":")
  val usuario = partes(0)
  val gasto = partes(1).toInt
  (usuario, gasto) // Crear una tupla (usuario, gasto)
}).reduceByKey(_ + _) // Sumar los gastos por usuario
    .filter { case (_, gastoTotal) => gastoTotal > 100 } // Filtrar solo los usuarios con gasto total mayor a 100

gastosPorUsuario.collect().foreach { case (usuario, gastoTotal) =>
  println(s"$usuario: $gastoTotal")
}


// Versión B: Usando `map()`, `groupByKey()` y `mapValues()`

val compras = sc.parallelize(List("user1:100", "user2:50", "user1:20", "user3:300", "user2:15"))

// el objetivo aqui es hacer el "join" manual, es decir, agrupar por usuario y luego sumar los gastos de cada usuario antes de filtrar
val gastosPorUsuario = compras.map(compra => {
  val partes = compra.split(":")
  val usuario = partes(0)
  val gasto = partes(1).toInt
  (usuario, gasto) // Crear una tupla (usuario, gasto)
}
}).groupByKey() // Agrupar por usuario
  .mapValues(gastos => gastos.sum) // Sumar los gastos de cada usuario
  .filter { case (_, gastoTotal) => gastoTotal > 100 } // Filtrar solo los usuarios con gasto total mayor a 100

gastosPorUsuario.collect().foreach { case (usuario, gastoTotal) =>
    println(s"$usuario: $gastoTotal")
}

