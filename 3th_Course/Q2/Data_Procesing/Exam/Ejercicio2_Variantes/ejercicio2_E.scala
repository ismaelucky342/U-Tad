// VARIANTE 5: Conteo de vocales (RDDs en Spark)
//
// Dado el siguiente RDD que representa líneas de texto:
//
// val texto = sc.parallelize(List(
//   "En un lugar de la Mancha",
//   "de cuyo nombre no quiero acordarme",
//   "no ha mucho tiempo que vivía"
// ))
//
// Queremos saber cuántas veces aparece cada vocal
// (a, e, i, o, u) en todo el texto.
//
// Requisitos:
//
// Implementa dos versiones diferentes:
//
// Versión A:
// - Utiliza flatMap() para separar cada línea en caracteres.
// - Convierte todas las letras a minúsculas.
// - Utiliza filter() para quedarte únicamente con las vocales.
// - Transforma cada vocal a una tupla (vocal,1).
// - Utiliza reduceByKey() para obtener el número total de apariciones.
//
// Versión B:
// - Utiliza un único flatMap() que directamente genere las tuplas (vocal,1).
// - Utiliza groupByKey() y posteriormente mapValues()
//   para calcular el total de apariciones.
//
// El resultado esperado debería tener un formato similar a:
//
// (a, X)
// (e, X)
// (i, X)
// (o, X)
// (u, X)
//
// donde X es el número de veces que aparece cada vocal.

// Versión A: Usando `flatMap()`, `filter()`, `map()` y `reduceByKey()`
import scala.io.Source
import java.io.PrintWriter

val texto = sc.parallelize(List(
  "En un lugar de la Mancha",
  "de cuyo nombre no quiero acordarme",
  "no ha mucho tiempo que vivía"
))

val vocales = texto.flatMap(linea => linea.toLowerCase.toCharArray) // Separar en caracteres y convertir a minúsculas
  .filter(c => "aeiou".contains(c)) // Filtrar solo las vocales
  .map(vocal => (vocal, 1)) // Crear tuplas (vocal, 1)
  .reduceByKey(_ + _) // Sumar los contadores por vocal

vocales.collect().foreach { case (vocal, count) =>
  println(s"($vocal, $count)")
}

// Versión B: Usando un único `flatMap()`, `groupByKey()` y `mapValues()`

val texto = sc.parallelize(List(
  "En un lugar de la Mancha",
  "de cuyo nombre no quiero acordarme",
  "no ha mucho tiempo que vivía"
))

val vocales = texto.flatMap(linea => {
  linea.toLowerCase.toCharArray.filter(c => "aeiou".contains(c)).map(vocal => (vocal, 1))
}) // Generar tuplas (vocal, 1) directamente
.groupByKey() // Agrupar por vocal
.mapValues(contadores => contadores.size) // Contar cuántos elementos hay en cada grupo

vocales.collect().foreach { case (vocal, count) =>
  println(s"($vocal, $count)")
}

