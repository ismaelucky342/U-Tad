//VARIANTE 2: Conteo de palabras y frecuencias (Tuplas en Spark)
//
//Dado el siguiente RDD que representa líneas de un registro de errores o logs:
//Scala
//
//val logs = sc.parallelize(List("ERROR:404", "INFO:200", "ERROR:500", "ERROR:404", "INFO:200"))
//
//Queremos saber cuántas veces aparece cada tipo de mensaje (ERROR o INFO), ignorando el código numérico. El resultado final debe ser una lista o mapa con: (ERROR, 3) e (INFO, 2).
//
//Implementa dos versiones diferentes:
//
//    Versión A: Utiliza map() para limpiar el texto y quedarte solo con la palabra (ERROR o INFO), luego otro map() para transformarlo en una tupla clave-valor (tipo, 1), y finalmente reduceByKey() para sumar los contadores.
//
//    Versión B: Utiliza un único map() para hacer la limpieza y crear la tupla (tipo, 1) a la vez, y luego utiliza groupByKey() seguido de un mapValues() para contar cuántos elementos hay en cada grupo (simulando lo que haría el reduce).

// Versión A: Usando `map()` y `reduceByKey()`

val logs = sc.parallelize(List("ERROR:404", "INFO:200", "ERROR:500", "ERROR:404", "INFO:200"))

val tipoContador = logs.map(log => {
  val tipo = log.split(":")(0) // Extraer la parte antes de los dos puntos
  (tipo, 1) // Crear una tupla (tipo, 1)
}).reduceByKey(_ + _) // Sumar los contadores por tipo

tipoContador.collect().foreach { case (tipo, count) =>
  println(s"$tipo: $count")
}

// Versión B: Usando `map()`, `groupByKey()` y `mapValues()`

val logs = sc.parallelize(List("ERROR:404", "INFO:200", "ERROR:500", "ERROR:404", "INFO:200"))

val tipoContador = logs.map(log => {
  val tipo = log.split(":")(0) // Extraer la parte antes de los dos puntos
  (tipo, 1) // Crear una tupla (tipo, 1)
}).groupByKey() // Agrupar por tipo
  .mapValues(contadores => contadores.size) // Contar cuántos elementos hay en cada grupo

tipoContador.collect().foreach { case (tipo, count) =>
  println(s"$tipo: $count")
}

