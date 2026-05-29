/*
Ejercicio 1 - Gestión básica de estudiantes

Objetivo:
Practicar elementos básicos de Scala y operaciones funcionales
sobre colecciones.

Conceptos:
- val
- tipos básicos
- case class
- List
- map
- filter
- foreach
- sortBy

--------------------------------------------------

Requisitos:

1. Crear una case class llamada Estudiante con:
   - nombre
   - edad
   - nota

2. Crear una lista con al menos 5 estudiantes.

3. Mostrar todos los estudiantes usando foreach.

4. Obtener los estudiantes aprobados
   (nota mayor o igual a 5).

5. Obtener una lista con los nombres
   de los aprobados en mayúsculas.

6. Ordenar los estudiantes por nota descendente.

7. Calcular la nota media de todos los estudiantes.


Extra opcional:

8. Agrupar estudiantes en:
   - Aprobados
   - Suspensos


Ejemplo esperado aproximado:

Ana - 7.5
Luis - 4.0

Aprobados:
ANA
MARTA

Media:
6.8
*/

val estudiantes = List(
  Estudiante("Ana", 20, 7.5),
  Estudiante("Luis", 22, 4.0),
  Estudiante("Marta", 19, 8.2),
  Estudiante("Carlos", 21, 6.8),
  Estudiante("Lucia", 20, 9.1)
)

estudiantes.foreach(e => println(s"${e.nombre} - ${e.nota}"))

val aprobados = estudiantes.filter(_.nota >= 5)

val nombresAprobados = aprobados.map(_.nombre.toUpperCase)

val estudiantesOrdenados = estudiantes.sortBy(_.nota)(Ordering.Double.reverse)

val notaMedia = estudiantes.map(_.nota).sum / estudiantes.length

println("Aprobados:")
nombresAprobados.foreach(println)

println(s"Media: $notaMedia")

val estudiantesOrdenados = estudiantes.sortBy(_.nota)(Ordering.Double.reverse)

val agrupados = estudiantes.groupBy(e => if (e.nota >= 5) "Aprobados" else "Suspensos")