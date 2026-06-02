/*
Ejercicio 2_A - Scala + Spark Básico: SUMAS EN RDD
(Modelo Original)

Dado el siguiente RDD en Spark:
val data = sc.parallelize(List("1,2,3", "4,5", "6,7,8,9"))

Cada elemento es una cadena que representa una lista de números separados por comas.

Aplica transformaciones (utilizando funciones superiores sobre colecciones — 
por ejemplo, map, flatMap, fold, etc.) para procesar el RDD, y una acción 
para obtener el siguiente resultado: "Suma total: 45"

Se pide:
1. Versión A: Utiliza exclusivamente map() y sum()
2. Versión B: Utiliza exclusivamente flatMap(), map() y fold()

IMPORTANTE: Entregar código bien comentado y pantallazo de ambas ejecuciones.
*/

// ============ VERSIÓN A: map() y sum() ============

val data = sc.parallelize(List("1,2,3", "4,5", "6,7,8,9"))

// Paso 1: convertimos cada String en una lista de números
val numeros = data.map(linea => linea.split(",").map(_.toInt).sum)
// con esto el conjunto queda como [6, 9, 30] porque cada línea se convierte en la suma de sus números

// Paso 2: sumamos los totales de cada línea
val sumaTotal = numeros.sum()
// sumaTotal ahora es 45 (6 + 9 + 30)

println(s"Suma total: $sumaTotal")


// ============ VERSIÓN B: flatMap(), map() y fold() ============

val data = sc.parallelize(List("1,2,3", "4,5", "6,7,8,9"))

// Paso 1: Usamos flatMap para convertir cada String en una lista de números individuales
val numeros = data.flatMap(linea => linea.split(",").map(_.toInt))

// Paso 2: Usamos fold para sumar todos los números, empezando desde 0
val sumaTotal = numeros.fold(0)((acc, num) => acc + num)

println(s"Suma total: $sumaTotal")
