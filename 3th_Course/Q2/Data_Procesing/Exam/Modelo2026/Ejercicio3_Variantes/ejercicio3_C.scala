/*
Ejercicio 3_C - Scala Avanzado: IMPLICIT PARAMETERS Y TRAITS

Se pide implementar un programa Scala que demuestre:
1. Type classes mediante implicits
2. Traits para definir comportamientos
3. Pattern matching con tipos complejos
4. Métodos extension (implícitos)

Caso: Sistema de validación genérico

Requisitos:
- Crear un trait Validador[T] con implicits
- Implementar validadores para diferentes tipos
- Usar pattern matching para procesar resultados
- Aplicar validaciones a datos

Estructura propuesta:
- Trait Validador con método validate
- Case classes para resultados
- Validadores implícitos para String, Int, etc.
*/

// Trait que define el comportamiento de validación
trait Validador[T] {
  def validate(valor: T): Boolean
  def mensaje: String
}

// Case classes para resultados
case class ResultadoValidacion[T](valor: T, esValido: Boolean, razon: String)

// Validadores implícitos para diferentes tipos
implicit val validadorEmail: Validador[String] = new Validador[String] {
  def validate(email: String): Boolean = email.contains("@") && email.contains(".")
  def mensaje = "Formato de email inválido"
}

implicit val validadorEdad: Validador[Int] = new Validador[Int] {
  def validate(edad: Int): Boolean = edad >= 18 && edad <= 120
  def mensaje = "Edad debe estar entre 18 y 120"
}

implicit val validadorNombre: Validador[String] = new Validador[String] {
  def validate(nombre: String): Boolean = nombre.nonEmpty && nombre.length >= 3
  def mensaje = "Nombre debe tener al menos 3 caracteres"
}

// Función genérica que usa validadores implícitos
def validar[T](valor: T)(implicit validador: Validador[T]): ResultadoValidacion[T] = {
  val esValido = validador.validate(valor)
  val razon = if (esValido) "OK" else validador.mensaje
  ResultadoValidacion(valor, esValido, razon)
}

// Clase para trabajar con múltiples datos
case class Usuario(nombre: String, email: String, edad: Int)

def validarUsuario(usuario: Usuario): Unit = {
  val r1 = validar(usuario.nombre)
  val r2 = validar(usuario.email)
  val r3 = validar(usuario.edad)
  
  println(s"Usuario: ${usuario.nombre}")
  println(s"  Nombre: ${if (r1.esValido) "✓" else "✗"} (${r1.razon})")
  println(s"  Email: ${if (r2.esValido) "✓" else "✗"} (${r2.razon})")
  println(s"  Edad: ${if (r3.esValido) "✓" else "✗"} (${r3.razon})")
  
  val todosValidos = r1.esValido && r2.esValido && r3.esValido
  println(s"  Estado: ${if (todosValidos) "VÁLIDO" else "INVÁLIDO"}\n")
}

// Ejemplo de uso
val usuario1 = Usuario("María", "maria@example.com", 25)
val usuario2 = Usuario("Jo", "joemail.com", 17)
val usuario3 = Usuario("Pedro López", "pedro@test.org", 150)

validarUsuario(usuario1)
validarUsuario(usuario2)
validarUsuario(usuario3)

// Pattern matching en lista de usuarios
val usuarios = List(usuario1, usuario2, usuario3)

usuarios.foreach { usuario =>
  usuario match {
    case Usuario(nombre, email, edad @ 18 | altura if altura >= 18) =>
      println(s"$nombre es mayor de edad y puede registrarse")
    case Usuario(nombre, _, edad) if edad < 18 =>
      println(s"$nombre es menor de edad")
    case _ =>
      println(s"Usuario: ${usuario.nombre}")
  }
}
