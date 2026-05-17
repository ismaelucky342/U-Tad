//## VARIANTE 1: Gestión de Paquetes de Envíos (Jerarquías + OO vs Funcional)
//
//Para cambiar de aires, en lugar de animales vamos a modelar un sistema logístico de **Paquetes** (`Package`).
//
//### Apartado A: Jerarquías y Extracción Avanzada
//
//1. Crea una estructura cerrada llamada `Paquete` (usando `sealed trait`).
//2. Crea dos tipos de paquetes que la extiendan:
//* `Sobre(destinatario: String, urgente: Boolean)`
//* `Caja(destinatario: String, peso: Double, frágil: Boolean)`
//
//
//3. Crea un método o función llamado `procesarEnvio` que reciba un `Paquete` y use **Pattern Matching** para:
//* Si es una `Caja` que pesa **más de 20.0** kilos, debe imprimir: *"Alerta: Caja pesada para [destinatario] ([peso] kg)"*. (Pista: tendrás que usar un filtro `if` o guardar la variable del peso).
//* Si es un `Sobre` que es **urgente**, debe imprimir: *"Envío prioritario para [destinatario]"*.
//* Para cualquier otro paquete, debe imprimir: *"Envío estándar"*.
//
//
//
//### Apartado B: El truco del "Invertido" (OO vs Funcional)
//
//Vamos a calcular el precio de envío de un documento rectangular (un sobre plano). El precio base es $Ancho \times Alto \times 0.1$.
//
//* **B1 (Clásica):** Crea una clase estándar `Documento` que reciba en su constructor `val ancho: Double` y `val alto: Double`. Ponle un método `precio()` dentro que calcule el coste. Pruébalo instanciándolo (con `new`) para un tamaño de $10 \times 5$.
//* **B2 (Funcional):** Haz lo contrario. Crea una `case class DocumentoFuncional(ancho: Double, alto: Double)`. Y ahora, crea un `object Tarificador` con una función pura que calcule el precio recibiendo ese documento.
//
//---

// Apartado A: Jerarquías y Extracción Avanzada

scaled trait Paquete // 1. Declaramos el trait cerrado para los paquetes

case class Sobre(destinatario: String, urgente: Boolean) extends Paquete // 2. Creamos la clase Sobre que extiende de Paquete
case class Caja(destinatario: String, peso: Double, frágil: Boolean) extends Paquete // 2. Creamos la clase Caja que extiende de Paquete

def procesarEnvio(paquete: Paquete): Unit = paquete match { // 3. Función con pattern matching para procesar el envío
  case Caja(destinatario, peso, _) if peso > 20.0 => println(s"Alerta: Caja pesada para $destinatario ($peso kg)") // Si es una caja pesada, imprime la alerta
  case Sobre(destinatario, urgente) if urgente => println(s"Envío prioritario para $destinatario") // Si es un sobre urgente, imprime el mensaje de envío prioritario
  case _ => println("Envío estándar") // Para cualquier otro caso, imprime que es un envío estándar
}

// Probamos la función con diferentes paquetes
val paquete1 = Caja("Juan", 25.0, frágil = true)
val paquete2 = Sobre("María", urgente = true)
val paquete3 = Caja("Ana", 15.0, frágil = false)

procesarEnvio(paquete1) // Debería alertar por caja pesada
procesarEnvio(paquete2) // Debería indicar envío prioritario
procesarEnvio(paquete3) // Debería indicar envío estándar

// Apartado B: El truco del "Invertido" (OO vs Funcional)

// B1 (Clásica): Clase Documento con método precio()

class Documento(val ancho: Double, val alto: Double) { // Creamos la clase Documento con campos ancho y alto
  def precio(): Double = ancho * alto * 0.1 // Método para calcular el precio del envío
}

val documento1 = new Documento(10.0, 5.0) // Creamos una instancia de Documento con ancho 10 y alto 5
println(s"Precio del documento clásico: ${documento1.precio()}") // Imprimimos el precio del documento clásico


// B2 (Funcional): Case class para datos y objeto con función de cálculo

case class DocumentoFuncional(ancho: Double, alto: Double) // Case class que solo guarda el ancho y alto
object Tarificador { // Objeto contenedor para la lógica de cálculo
  def calcularPrecio(documento: DocumentoFuncional): Double = documento.ancho * documento.alto * 0.1 // Función pura que calcula el precio del envío
}

val documentoFuncional1 = DocumentoFuncional(10.0, 5.0) // Creamos una instancia de DocumentoFuncional con ancho 10 y alto 5
println(s"Precio del documento funcional: ${Tarificador.calcularPrecio(documentoFuncional1)}") // Imprimimos el precio del documento funcional usando el tarificador
