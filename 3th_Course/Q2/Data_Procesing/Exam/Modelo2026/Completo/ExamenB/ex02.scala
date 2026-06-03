/*

===============================================================================
EJERCICIO 2 (1.5 puntos) - SPARK RDD: ANÁLISIS DE VIAJES
========================================================

Se proporciona un archivo "viajes.txt" con registros:

usuario_id,distancia_km

TAREA:

1. Cargar datos usando:

   sc.textFile()

2. Filtrar viajes mayores a 10 km

3. Calcular kilómetros totales por usuario

4. Obtener:

   * Promedio de kilómetros por usuario
   * Usuario con mayor distancia recorrida
   * Número total de usuarios únicos

EJEMPLO DE ENTRADA (viajes.txt):

U001,5
U002,12
U001,8
U003,25
U002,7
U001,15

SALIDA ESPERADA:

U001 -> 23 km
U002 -> 12 km
U003 -> 25 km

Promedio: 20 km
Usuario top: U003
Usuarios únicos: 3

PISTAS:

* Usa reduceByKey()
* Usa distinct()
* Usa max()
*/

// Paso 1: Cargar datos
val viajes = sc.textFile("viajes.txt") // esto asume que el archivo está en el directorio de trabajo de Spark

// Paso 2: Filtrar viajes mayores a 10 km

val viajesFiltrados = viajes.filter { linea =>
  val Array(_, distancia) = linea.split(",")
  distancia.toDouble > 10


// Paso 3: Calcular kilómetros totales por usuario
val kilometrosPorUsuario = viajesFiltrados.map { linea =>
  val Array(usuario, distancia) = linea.split(",")
  (usuario, distancia.toDouble)
}.reduceByKey(_ + _)

// Paso 4: Obtener resultados

// Mostrar kilómetros totales por usuario
kilometrosPorUsuario.collect().foreach { case (usuario, totalKm) =>
  println(s"$usuario -> $totalKm km")
}

// Calcular promedio de kilómetros por usuario
val totalUsuarios = kilometrosPorUsuario.count()
val totalKilometros = kilometrosPorUsuario.map { case (_, km) => km }.sum()
val promedio = totalKilometros / totalUsuarios
println(s"Promedio: ${promedio.formatted("%.2f")} km")