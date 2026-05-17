//**VARIANTE: Gestión de Vehículos y Autonomía Eléctrica
//Apartado A: Jerarquías y "Pattern Matching" (0,75 pts)**
//1. Crea una estructura cerrada llamada `Vehiculo` usando `sealed trait`.
//2. Crea dos tipos de clases que hereden de ella usando `case class`:
//    ◦ `Coche` con los campos `modelo: String` y `motor: String` (por ejemplo: "eléctrico", "diésel").
//    ◦ `Moto` con los campos `modelo: String` y `cilindrada: Int`.
//3. Crea una instancia de `Coche` con modelo "Model 3" y motor "eléctrico", asignada a una variable de tipo base `Vehiculo` llamada `v1`.
//4. Crea una instancia de `Moto` con modelo "Ninja" y cilindrada `600`, asignada también al tipo base `Vehiculo` llamada `v2`.
//5. Diseña una función llamada `revisarVehiculo` con **Pattern Matching** que:
//    ◦ Detecte específicamente si el vehículo es un **Coche cuyo motor sea exactamente "eléctrico"** e imprima: *"Vehículo ECO detectado: [modelo]."*
//    ◦ Si es cualquier otro coche, imprima un mensaje genérico indicando su modelo y su tipo de motor.
//    ◦ Para cualquier otro caso (como las motos), imprima: *"Requiere revisión de dos ruedas o mecánica estándar."*
//**Apartado B: Orientación a Objetos vs. Programación Funcional (0,75 pts)**
//Vamos a calcular la autonomía estimada de una batería industrial basándonos en su capacidad en kWh. La fórmula de la autonomía es $\text{capacidad} \times 6.5$.
//• **B1 (Clásica - Orientada a Objetos):** Crea una clase tradicional llamada `Bateria` que reciba en su constructor `val capacidad: Double`. Añade dentro de la clase un método `autonomia(): Double` que devuelva el resultado. Pruébalo instanciándolo con `new` para una capacidad de 60.0 kWh.
//• **B2 (Funcional - Con Objeto Compañero):** Separa los datos de la lógica. Crea una `case class BateriaFuncional(capacidad: Double)` (sin métodos dentro). Luego, crea un `object EstimadorAutonomia` con una función pura que reciba una instancia de `BateriaFuncional` y devuelva la autonomía. Pruébalo para 60.0 kWh.

// Apartado A: Jerarquías y "Pattern Matching"

sealed trait Vehiculo // 1. Declaramos el trait cerrado para los vehículos

case class Coche(modelo: String, motor: String) extends Vehiculo // 2. Creamos la clase Coche que extiende de Vehiculo
case class Moto(modelo: String, cilindrada: Int) extends Vehiculo // 2. Creamos la clase Moto que extiende de Vehiculo

val v1: Vehiculo = Coche("Model 3", "eléctrico") // 3. Creamos una instancia de Coche con modelo "Model 3" y motor "eléctrico"
val v2: Vehiculo = Moto("Ninja", 600) // 4. Creamos una instancia de Moto con modelo "Ninja" y cilindrada 600

def revisarVehiculo(vehiculo: Vehiculo): Unit = vehiculo match { // 5. Función con pattern matching para revisar el vehículo
  case Coche(modelo, "eléctrico") => println(s"Vehículo ECO detectado: $modelo.") // Si es un coche con motor eléctrico, imprime el mensaje de vehículo ECO
  case Coche(modelo, motor) => println(s"Coche modelo $modelo con motor $motor.") // Si es un coche pero no eléctrico, imprime un mensaje genérico
  case _ => println("Requiere revisión de dos ruedas o mecánica estándar.") // Para cualquier otro caso (como las motos), imprime el mensaje de revisión estándar
}

revisarVehiculo(v1) // Probamos con el coche Model 3
revisarVehiculo(v2) // Probamos con la moto Ninja


// Apartado B: Orientación a Objetos vs. Programación Funcional

// B1 (Clásica - Orientada a Objetos): Clase Bateria con método autonomia()

class Bateria(val capacidad: Double) { // Creamos la clase Bateria con un campo capacidad
  def autonomia(): Double = capacidad * 6.5 // Método para calcular la autonomía basada en la capacidad
}

val bateria1 = new Bateria(60.0) // Creamos una instancia de Bateria con capacidad 60.0 kWh
println(s"Autonomía estimada (OO): ${bateria1.autonomia()} km") // Imprimimos la autonomía estimada usando la clase orientada a objetos


// B2 (Funcional - Con Objeto Compañero): Case class para datos y objeto con función de cálculo

case class BateriaFuncional(capacidad: Double) // Case class que solo guarda la capacidad
object EstimadorAutonomia { // Objeto contenedor para la lógica de cálculo
  def calcularAutonomia(bateria: BateriaFuncional): Double = bateria.capacidad * 6.5 // Función pura que calcula la autonomía basada en la capacidad
}   

val bateriaFuncional1 = BateriaFuncional(60.0) // Creamos una instancia de BateriaFuncional con capacidad 60.0 kWh
println(s"Autonomía estimada (Funcional): ${EstimadorAutonomia.calcularAutonomia(bateriaFuncional1)} km") // Imprimimos la autonomía estimada usando la calculadora funcional

