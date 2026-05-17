//# EJERCICIO 2 — Colecciones con Función Superior en Spark *(1 pt)*
//
//---
//
//> **ENUNCIADO ORIGINAL**
//> 
//> 
//> Dado el siguiente RDD en Spark:
//> 
//> ```scala
//> val data = sc.parallelize(List("1,2,3", "4,5", "6,7,8,9"))
//> ```
//> 
//> Cada elemento es una cadena que representa una lista de números separados por comas.
//> 
//> Aplica transformaciones (utilizando **funciones superiores** sobre colecciones — por ejemplo, `map`, `flatMap`, `fold`, etc.) para procesar el RDD, y una acción para obtener el siguiente resultado: **“Suma total: 45”**
//> 
//> Implementa **dos versiones diferentes** que obtengan dicho resultado:
//> 
//> - **A)** En la **primera versión**, utiliza exclusivamente las funciones **`map()`** y **`sum()`** para calcular la suma total. *(0,5 pts)*
//> - **B)** En la **segunda versión**, realiza la suma utilizando exclusivamente las funciones **`flatMap()`**, **`map()`** y **`fold()`**. *(0,5 pts)*
//> 
//> **Se pide entregar el código bien pegado como respuesta o en un fichero `.txt`. También hay que incluir pantallazo de ambas ejecuciones.**
//> 
//
//---
//
//## Contexto previo: ¿Qué es un RDD y cuál es el problema?
//
//Un **RDD (Resilient Distributed Dataset)** es la estructura de datos fundamental de Spark. Imagínalo como una lista que puede estar repartida entre varios nodos de un clúster y que se procesa en paralelo.
//
//El truco de este ejercicio está en que los datos son **Strings** (texto), no números:
//
//```
//RDD inicial: ["1,2,3",  "4,5",  "6,7,8,9"]
//                 ↑         ↑        ↑
//              String    String   String   ← ¡Son texto! No se pueden sumar directamente
//```
//
//Antes de poder sumar, hay que “extraer” los números del texto. Las dos versiones resuelven esto de formas distintas.
//
//---

// Versión A: Usando `map()` y `sum()`

val data = sc.parallelize(List("1,2,3", "4,5", "6,7,8,9"))

// Paso 1: convertis cada String en una lista de números

val numeros = data.map(linea => linea.split(",").map(_.toInt).sum)
// con esto el conjunto queda como [6, 9, 30] porque cada línea se convierte en la suma de sus números

// Paso 2: sumamos los totales de cada línea
val sumaTotal = numeros.sum()
// sumaTotal ahora es 45 (6 + 9 + 30)

println(s"Suma total: $sumaTotal")


// Versión B: Usando `flatMap()`, `map()` y `fold()`

val data = sc.parallelize(List("1,2,3", "4,5", "6,7,8,9"))

// Paso 1: Usamos flatMap para convertir cada String en una lista de números individuales
val numeros = data.flatMap(linea => linea.split(",").map(_.toInt))

// Paso 2: Usamos fold para sumar todos los números, empezando desde 0
val sumaTotal = numeros.fold(0)((acc, num) => acc + num)

println(s"Suma total: $sumaTotal") 

