/*
Ejercicio 2_B - Scala + Spark Básico: CONTEO DE PALABRAS

Dado un RDD de texto que contiene palabras separadas por espacios:
val palabras = sc.parallelize(List("hello world", "spark rdd transformation", "hello spark"))

Se pide procesar el RDD para contar cuántas veces aparece cada palabra.

Resultado esperado (en la consola o en un resultado visible):
hello: 2
world: 1
spark: 2
rdd: 1
transformation: 1

Se pide:
1. Versión A: Utiliza map(), flatMap() y countByValue()
2. Versión B: Utiliza flatMap(), map() y reduceByKey()

IMPORTANTE: Entregar código bien comentado y pantallazo de ambas ejecuciones.
*/

// ============ VERSIÓN A: flatMap(), map() y countByValue() ============

val palabras = sc.parallelize(List("hello world", "spark rdd transformation", "hello spark"))

// Paso 1: Dividimos cada línea en palabras individuales (flatMap + split)
val palabrasSeparadas = palabras.flatMap(linea => linea.split(" "))

// Paso 2: Convertimos cada palabra a una tupla (palabra, 1)
val paresPalabras = palabrasSeparadas.map(palabra => (palabra, 1))

// Paso 3: Usamos countByValue() que automáticamente agrupa y cuenta
val conteo = palabrasSeparadas.countByValue()

conteo.foreach { case (palabra, cantidad) =>
  println(s"$palabra: $cantidad")
}


// ============ VERSIÓN B: flatMap(), map() y reduceByKey() ============

val palabras = sc.parallelize(List("hello world", "spark rdd transformation", "hello spark"))

// Paso 1: Dividimos cada línea en palabras individuales
val palabrasSeparadas = palabras.flatMap(linea => linea.split(" "))

// Paso 2: Convertimos cada palabra a una tupla (palabra, 1) para poder contar
val paresPalabras = palabrasSeparadas.map(palabra => (palabra, 1))

// Paso 3: Usamos reduceByKey para agrupar por palabra y sumar los conteos
val conteo = paresPalabras.reduceByKey((a, b) => a + b)

// Paso 4: Recogemos el resultado con collect() para verlo
val resultado = conteo.collect()
resultado.foreach { case (palabra, cantidad) =>
  println(s"$palabra: $cantidad")
}
