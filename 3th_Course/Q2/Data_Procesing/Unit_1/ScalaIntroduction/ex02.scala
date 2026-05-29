/*
Ejercicio 3 - Traits y polimorfismo

Conceptos:
- trait
- case class
- herencia
- polimorfismo
- pattern matching
- map
- foreach

Requisitos:

1. Crear un trait llamado Animal.
   Debe tener:
   - nombre
   - hacerSonido()

2. Crear:
   - Perro
   - Gato
   - Pajaro

3. Cada animal debe implementar
   su propio sonido.

4. Crear una lista con distintos animales.

5. Mostrar:
   - nombre
   - sonido

6. Usar pattern matching para mostrar:
   - "Es un perro"
   - "Es un gato"
   - "Es un pajaro"

Extra:
7. Obtener una lista solo con los perros.
*/

trait Animal {
  def nombre: String
  def hacerSonido(): String
}

case class Perro(nombre: String) extends Animal {
  def hacerSonido(): String = "Guau"
}

case class Gato(nombre: String) extends Animal {
  def hacerSonido(): String = "Miau"
}

case class Pajaro(nombre: String) extends Animal {
  def hacerSonido(): String = "Pio"
}

val animales: List[Animal] = List(
  Perro("Rex"),
  Gato("Mimi"),
  Pajaro("Tweety"),
  Perro("Fido")
)

animales.foreach { animal =>
  println(s"${animal.nombre} hace ${animal.hacerSonido()}")
}

ani
animales.foreach { animal =>
  val tipo = animal match {
    case _: Perro => "Es un perro"
    case _: Gato => "Es un gato"
    case _: Pajaro => "Es un pajaro"
    case _ => "Tipo desconocido"
  }
  println(s"${animal.nombre}: $tipo")
}

val perros = animales.collect { case p: Perro => p }
perros.foreach(p => println(s"Perro: ${p.nombre}"))