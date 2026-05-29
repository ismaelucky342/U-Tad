/*
Ejercicio 2 - Búsqueda segura de estudiantes

Objetivo:
Practicar funciones, Option y búsquedas seguras.

Conceptos:
- funciones
- Option
- Some
- None
- find
- map
- getOrElse
- pattern matching

--------------------------------------------------

Requisitos:

1. Crear una case class llamada Estudiante con:
   - nombre
   - edad
   - nota

2. Crear una lista con varios estudiantes.

3. Crear una función:

   buscarEstudiante(nombre: String)

La función debe:
- buscar un estudiante por nombre
- devolver Option[Estudiante]

--------------------------------------------------

4. Buscar un estudiante existente.

5. Buscar un estudiante que no exista.

--------------------------------------------------

6. Mostrar resultados usando match:

Ejemplo:

"Estudiante encontrado: Ana"
"No existe el estudiante"

--------------------------------------------------

7. Obtener la nota del estudiante usando:
   - map
   - getOrElse

Ejemplo:

val nota = resultado.map(_.nota).getOrElse(0.0)

--------------------------------------------------

Extra opcional:

8. Crear una función que devuelva:
   - "Aprobado"
   - "Suspenso"

según la nota del estudiante.

--------------------------------------------------

Pistas:

find devuelve:
- Some(valor)
- None

Ejemplo:

lista.find(_.nombre == "Ana")

--------------------------------------------------

Objetivo importante:

Evitar usar null.
Scala usa Option para representar
valores que pueden no existir.
*/

val Estudiante = case class(nombre: String, edad: Int, nota: Double)

val estudiantes = List(
  Estudiante("Ana", 20, 7.5),
  Estudiante("Luis", 22, 4.0),
  Estudiante("Marta", 19, 8.2),
  Estudiante("Carlos", 21, 6.8),
  Estudiante("Lucia", 20, 9.1)
)

def buscarEstudiante(nombre: String): Option[Estudiante] = {
  estudiantes.find(_.nombre == nombre)
}

val resultado1 = buscarEstudiante("Ana")
val resultado2 = buscarEstudiante("Pedro")

resultado1 match {
  case Some(estudiante) => println(s"Estudiante encontrado: ${estudiante.nombre}")
  case None => println("No existe el estudiante")
}

resultado2 match {
  case Some(estudiante) => println(s"Estudiante encontrado: ${estudiante.nombre}")
  case None => println("No existe el estudiante")
}

val notaAna = resultado1.map(_.nota).getOrElse(0.0)
val notaPedro = resultado2.map(_.nota).getOrElse(0.0)

println(s"Nota de Ana: $notaAna")
println(s"Nota de Pedro: $notaPedro")

def estadoEstudiante(nombre: String): String = {
  buscarEstudiante(nombre) match {
    case Some(estudiante) => if (estudiante.nota >= 5) "Aprobado" else "Suspenso"
    case None => "No existe el estudiante"
  }
}

println(s"Estado de Ana: ${estadoEstudiante("Ana")}")
println(s"Estado de Pedro: ${estadoEstudiante("Pedro")}")

