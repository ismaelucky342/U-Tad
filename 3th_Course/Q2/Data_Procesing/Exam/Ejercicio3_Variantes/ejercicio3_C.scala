//**VARIANTE 2: Sistema de Empleados y Cálculo de Bonus
//Apartado A: Jerarquías y "Pattern Matching" (0,75 pts)**
//1. Crea una estructura cerrada llamada `Empleado` usando `sealed trait`.
//2. Crea dos tipos de clases que hereden de ella usando `case class`:
//    ◦ `Desarrollador` con los campos `nombre: String` y `lenguaje: String`.
//    ◦ `Manager` con los campos `nombre: String` y `departamento: String`.
//3. Crea una instancia de `Desarrollador` con nombre "Carlos" y lenguaje "Scala", asignada a una variable de tipo base `Empleado` llamada `emp1`.
//4. Crea una instancia de `Manager` con nombre "Elena" y departamento "I+D", asignada también al tipo base `Empleado` llamada `emp2`.
//5. Diseña una función llamada `evaluarEmpleado` con **Pattern Matching** que:
//    ◦ Detecte específicamente si el empleado es un **Desarrollador cuyo lenguaje sea exactamente "Scala"** e imprima: *"¡Crack! [nombre] programa en Scala."*
//    ◦ Si es cualquier otro desarrollador, imprima un mensaje genérico con su nombre y su lenguaje.
//    ◦ Para cualquier otro caso (como los managers), imprima: *"Gestión o soporte."*
//**Apartado B: Orientación a Objetos vs. Programación Funcional (0,75 pts)**
//Vamos a calcular el bonus navideño de un empleado estándar basándonos en sus años de experiencia. La fórmula es $\text{años} \times 500$.
//• **B1 (Clásica - Orientada a Objetos):** Crea una clase tradicional llamada `Experiencia` que reciba en su constructor `val anos: Int`. Añade dentro de la clase un método `calcularBonus(): Int` que devuelva el resultado. Pruébalo instanciándolo con `new` para 4 años.
//• **B2 (Funcional - Con Objeto Compañero):** Separa los datos de la lógica. Crea una `case class ExperienciaFuncional(anos: Int)` (sin métodos dentro). Luego, crea un `object CalculadoraBonus` con una función pura que reciba una instancia de `ExperienciaFuncional` y devuelva el bonus. Pruébalo con 4 años.


// Apartado A: Jerarquías y "Pattern Matching"

sealed trait Empleado // 1. Declaramos el trait cerrado para los empleados

case class Desarrollador(nombre: String, lenguaje: String) extends Empleado // 2. Creamos la clase Desarrollador que extiende de Empleado
case class Manager(nombre: String, departamento: String) extends Empleado // 2. Creamos la clase Manager que extiende de Empleado

val emp1: Empleado = Desarrollador("Carlos", "Scala") // 3. Creamos una instancia de Desarrollador con nombre Carlos y lenguaje Scala
val emp2: Empleado = Manager("Elena", "I+D") // 4. Creamos una instancia de Manager con nombre Elena y departamento I+D

def evaluarEmpleado(empleado: Empleado): Unit = empleado match { // 5. Función con pattern matching para evaluar al empleado
  case Desarrollador(nombre, "Scala") => println(s"¡Crack! $nombre programa en Scala.") // Si es un desarrollador que programa en Scala, imprime el mensaje especial
  case Desarrollador(nombre, lenguaje) => println(s"$nombre es un desarrollador que programa en $lenguaje.") // Si es un desarrollador pero no programa en Scala, imprime un mensaje genérico
  case _ => println("Gestión o soporte.") // Para cualquier otro caso (como los managers), imprime el mensaje de gestión o soporte
}

evaluarEmpleado(emp1) // Probamos con el desarrollador Carlos
evaluarEmpleado(emp2) // Probamos con el manager Elena

// Apartado B: Orientación a Objetos vs. Programación Funcional

// B1 (Clásica - Orientada a Objetos): Clase Experiencia con método calcularBonus()

class Experiencia(val anos: Int) { // Creamos la clase Experiencia con un campo anos
  def calcularBonus(): Int = anos * 500 // Método para calcular el bonus basado en los años de experiencia
}

val experiencia1 = new Experiencia(4) // Creamos una instancia de Experiencia con 4 años
println(s"Bonus calculado (OO): ${experiencia1.calcularBonus()}") // Imprimimos el bonus calculado usando la clase orientada a objetos

// B2 (Funcional - Con Objeto Compañero): Case class para datos y objeto con función de cálculo

case class ExperienciaFuncional(anos: Int) // Case class que solo guarda los años de experiencia
object CalculadoraBonus { // Objeto contenedor para la lógica de cálculo
  def calcularBonus(experiencia: ExperienciaFuncional): Int = experiencia.anos * 500 // Función pura que calcula el bonus basado en los años de experiencia
}

val experienciaFuncional1 = ExperienciaFuncional(4) // Creamos una instancia de ExperienciaFuncional con 4 años
println(s"Bonus calculado (Funcional): ${CalculadoraBonus.calcularBonus(experienciaFuncional1)}") // Imprimimos el bonus calculado usando la calculadora funcional
