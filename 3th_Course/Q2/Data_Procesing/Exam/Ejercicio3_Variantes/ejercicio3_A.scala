//## Ejercicio 3: Modelo 24/25
//**Enunciado:** Dada una jerarquía de animales usando `sealed trait`, usa pattern matching para detectar si un animal es un **Gato de raza “persa”** e imprimir su nombre.
//
//**Pasos:**
//- Se declara un *sealed trait* Animal, que actúa como supertipo común para una jerarquía cerrada de clases. La sentencia en concreto a usar es `sealed trait Animal`
//- Se declaran las clases Perro y Gato que extienden este trait e incorporan dos campos (nombre y raza).
//- Se crea una instancia de Gato con nombre “Misu” y raza “persa”, asignada a una variable de tipo Animal. La llamaremos **`a`**.
//- Se instancia un Perro con nombre “Micki” y raza “bulldog”, también asignado al tipo base Animal. La llamaremos **`b`**.
//- Se aplica pattern matching primeramente sobre **`a`** para comprobar si es un Gato de raza “persa” y luego sobre **`b`**.
//
//### Apartado A: Jerarquías y "Pattern Matching" (0,75 pts)
//
//1. Crea una estructura cerrada llamada `Animal` (usando `sealed trait`).
//2. Crea dos tipos de animales que hereden de ella: `Perro` y `Gato`, ambos con los campos `nombre` y `raza`.
//3. Crea un gato llamado "Misu" de raza "persa" y un perro llamado "Micki" de raza "bulldog". Ambos deben estar guardados en variables de tipo genérico `Animal`.
//4. Diseña una función con **Pattern Matching** que identifique específicamente si el animal es un **Gato persa** e imprima su nombre. Si es otro gato u otro animal, debe mostrar un mensaje genérico.
//
//### Apartado B: Orientación a Objetos vs. Programación Funcional (0,75 pts)
//
//* **B1 (Clásica):** Crea una clase `Circulo` tradicional con un campo `radio`. La propia clase debe tener un método `area()` que calcule su superficie ($\pi \times \text{radio}^2$). Pruébalo con radio 3.0.
//* **B2 (Funcional):** Separa los datos de la lógica. Crea una `case class` que **solo** guarde el `radio` (sin métodos). Después, crea un objeto contenedor (`object CalculadoraCirculo`) que tenga una función que reciba el círculo y devuelva el área.
//
//---
//

// Apartado A: Jerarquías y "Pattern Matching"

sealed trait Animal // 1. Declaramos el trait cerrado lo cual garantiza que solo se pueden extender dentro de este archivo

case class Perro(nombre: String, raza: String) extends Animal // 2. Creamos la clase Perro que extiende de Animal
case class Gato(nombre: String, raza: String) extends Animal // 2. Creamos la clase Gato que extiende de Animal

val a: Animal = Gato("Misu", "persa") // 3. Creamos un gato llamado Misu de raza persa
val b: Animal = Perro("Micki", "bulldog") // 3. Creamos un perro llamado Micki de raza bulldog

def identificarAnimal(animal: Animal): Unit = animal match { // 4. Función con pattern matching para identificar si es un gato persa
  case Gato(nombre, "persa") => println(s"¡Es un gato persa llamado $nombre!") // Si es un gato de raza persa, imprime su nombre
  case Gato(nombre, _) => println(s"Es un gato llamado $nombre, pero no es persa.") // Si es un gato pero no persa
  case _ => println("No es un gato.") // Para cualquier otro caso (perro u otro animal)
}

identificarAnimal(a) // Probamos con el gato Misu 
identificarAnimal(b) // Probamos con el perro Micki

// Apartado B: Orientación a Objetos vs. Programación Funcional

// B1 (Clásica): Clase Circulo con método area()

class Circulo(val radio: Double) { // Creamos la clase Circulo con un campo radio
  def area(): Double = math.Pi * math.pow(radio, 2) // Método para calcular el área del círculo
}

val circulo1 = new Circulo(3.0) // Creamos una instancia de Circulo con radio 3.0
println(s"Área del círculo con radio 3.0: ${circulo1.area()}") // Imprimimos el área del círculo

// B2 (Funcional): Case class para datos y objeto con función de cálculo

case class CirculoFuncional(radio: Double) // Case class que solo guarda el radio
object CalculadoraCirculo { // Objeto contenedor para la lógica de cálculo
  def area(circulo: CirculoFuncional): Double = math.Pi * math.pow(circulo.radio, 2) // Función que calcula el área del círculo
}

val circuloFuncional1 = CirculoFuncional(3.0) // Creamos una instancia de CirculoFuncional con radio 3.0
println(s"Área del círculo funcional con radio 3.0: ${CalculadoraCirculo.area(circuloFuncional1)}") // Imprimimos el área del círculo usando la calculadora funcional

