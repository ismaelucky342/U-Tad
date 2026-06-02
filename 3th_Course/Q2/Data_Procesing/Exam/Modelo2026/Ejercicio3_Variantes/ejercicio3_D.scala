/*
Ejercicio 3_D - Scala Avanzado: RECURSIÓN, LAZY EVALUATION Y FUNCIONES PURAS

Se pide implementar un programa Scala que demuestre:
1. Recursión con tail recursion (@tailrec)
2. Lazy evaluation para eficiencia
3. Funciones puras sin efectos secundarios
4. Currying y partially applied functions

Caso: Algoritmos funcionales para procesamiento de datos

Requisitos:
- Implementar función recursiva con @tailrec
- Usar lazy evaluation
- Demostrar currying
- Combinar técnicas para procesamiento eficiente
*/

import scala.annotation.tailrec
import scala.math.BigInt

// Función 1: Recursión con tail recursion
// Calcula factorial de forma eficiente
@tailrec
def factorial(n: Int, acumulador: BigInt = 1): BigInt = {
  if (n <= 1) acumulador
  else factorial(n - 1, acumulador * n)
}

println(s"Factorial de 20: ${factorial(20)}")

// Función 2: Lazy evaluation
// Solo se calcula cuando se accede
lazy val valoresGrandes = (1 to 1000000).map(x => x * x).toList
println("Valores lazy creados (no calculados aún)")
// println(valoresGrandes.head) // Ahora se calcula

// Función 3: Funciones puras
// Sin efectos secundarios, mismo input = mismo output
def fibonacci(n: Int): Int = {
  @tailrec
  def fib(n: Int, a: Int = 0, b: Int = 1): Int = {
    if (n <= 0) a
    else fib(n - 1, b, a + b)
  }
  fib(n)
}

println(s"Fibonacci(10): ${fibonacci(10)}")

// Función 4: Currying
// Convertir función de múltiples parámetros en funciones anidadas
def suma(a: Int)(b: Int)(c: Int): Int = a + b + c

val sumaDos = suma(10)
val sumaUno = sumaDos(5)
val resultado = sumaUno(3)

println(s"Suma curried: 10 + 5 + 3 = $resultado")

// Partially applied function
val sumaConDiez = suma(10)(5)
println(s"Suma partial (10 + 5 + c): 10 + 5 + 7 = ${sumaConDiez(7)}")

// Función 5: Función de orden superior que combina técnicas
def aplicarOperacion(operacion: (Int, Int) => Int)(valores: List[Int]): Int = {
  @tailrec
  def procesar(lista: List[Int], acum: Int): Int = {
    lista match {
      case Nil => acum
      case x :: xs => procesar(xs, operacion(acum, x))
    }
  }
  procesar(valores, 0)
}

val numeros = List(1, 2, 3, 4, 5)
println(s"Suma usando HOF: ${aplicarOperacion(_+_)(numeros)}")
println(s"Multiplicación usando HOF: ${aplicarOperacion(_*_)(List(1, 2, 3, 4, 5).drop(1))}")

// Función 6: Lazy streams para eficiencia
def lazyRange(from: Int, until: Int): LazyList[Int] = {
  if (from >= until) LazyList()
  else from #:: lazyRange(from + 1, until)
}

val lazyNumeros = lazyRange(1, 100)
println(s"Primeros 5 números de LazyList(1 a 100): ${lazyNumeros.take(5).toList}")

// Función 7: Composición de funciones
def componer[A, B, C](f: B => C, g: A => B): A => C = {
  x => f(g(x))
}

val doble = (x: Int) => x * 2
val cuadrado = (x: Int) => x * x

val dobleDelCuadrado = componer(doble, cuadrado)
println(s"Composición de funciones: doble(cuadrado(5)) = ${dobleDelCuadrado(5)}")
