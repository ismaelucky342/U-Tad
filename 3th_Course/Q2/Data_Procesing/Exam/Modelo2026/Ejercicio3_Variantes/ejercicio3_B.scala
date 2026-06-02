/*
Ejercicio 3_B - Scala Avanzado: FOR-COMPREHENSIONS Y MONADS

Se pide implementar un programa Scala que demuestre:
1. For-comprehensions (cartesiano de colecciones)
2. Option type para manejo de valores nulos
3. Pattern matching con guards
4. Funciones de orden superior

Caso: Sistema de recomendaciones de películas

Requisitos:
- Crear case classes Pelicula, Genero, Puntuacion
- Usar Option para puntuaciones que pueden no existir
- Usar for-comprehension para generar recomendaciones
- Usar pattern matching con guards para filtrar

Estructura de datos:
case class Pelicula(titulo: String, genero: String, duracion: Int)
case class Puntuacion(pelicula: String, calificacion: Double)

Objetivo:
Recomendar películas del mismo género que una película puntuada,
pero que no haya sido puntuada aún, ordenadas por duración.
*/

case class Pelicula(titulo: String, genero: String, duracion: Int)
case class Puntuacion(pelicula: String, calificacion: Double)

val peliculas = List(
  Pelicula("Matrix", "Ciencia Ficción", 136),
  Pelicula("Inception", "Ciencia Ficción", 148),
  Pelicula("Nolan", "Ciencia Ficción", 130),
  Pelicula("Interstellar", "Ciencia Ficción", 169),
  Pelicula("Titanic", "Romance", 194),
  Pelicula("Avatar", "Acción", 162)
)

val puntuaciones = List(
  Puntuacion("Matrix", 9.0),
  Puntuacion("Titanic", 7.5),
  Puntuacion("Avatar", 8.5)
)

// Versión 1: For-comprehension con Option
val peliculasPuntuadas = puntuaciones.map(_.pelicula)

val recomendaciones = for {
  pelicula <- peliculas
  puntuacion <- puntuaciones
  if pelicula.genero == puntuacion.pelicula || 
     (for { p <- peliculas if p.titulo == puntuacion.pelicula } yield p.genero).contains(pelicula.genero)
  if !peliculasPuntuadas.contains(pelicula.titulo)
} yield pelicula

recomendaciones
  .sortBy(_.duracion)
  .foreach(p => println(s"${p.titulo} (${p.duracion} min)"))

// Versión 2: Usando groupBy y Option
val peliculasGenero = peliculas.groupBy(_.genero)
val puntuacionMasBuena = puntuaciones.maxBy(_.calificacion)

val paisGenero: Option[String] = peliculas
  .find(_.titulo == puntuacionMasBuena.pelicula)
  .map(_.genero)

paisGenero match {
  case Some(genero) =>
    println(s"\nPelículas recomendadas del género $genero:")
    peliculasGenero(genero)
      .filterNot(p => peliculasPuntuadas.contains(p.titulo))
      .sortBy(_.duracion)
      .foreach(p => println(s"  ${p.titulo} (${p.duracion} min)"))
  case None =>
    println("No se encontró película")
}

// Versión 3: Combinación de todas las técnicas
val recomendacionesAvanzadas = for {
  puntuation <- puntuaciones
  peliOriginal <- peliculas if peliOriginal.titulo == puntuation.pelicula
  peliRecomendada <- peliculas 
  if peliRecomendada.genero == peliOriginal.genero && 
     !peliculasPuntuadas.contains(peliRecomendada.titulo)
} yield peliRecomendada

println("\nRecomendaciones avanzadas:")
recomendacionesAvanzadas
  .distinct
  .sortBy(_.duracion)
  .foreach(p => println(s"${p.titulo}"))
