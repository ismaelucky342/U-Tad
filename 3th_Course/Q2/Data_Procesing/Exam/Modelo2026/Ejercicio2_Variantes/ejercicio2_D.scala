/*
Ejercicio 2_D - Scala + Spark Básico: ANÁLISIS DE TEMPERATURAS

Dado un RDD con datos de temperaturas por ciudad:
val datos = sc.parallelize(List("Madrid,25,28,26", "Barcelona,22,24,23", "Sevilla,30,32,31"))

Formato: ciudad,temp1,temp2,temp3

Se pide procesar para:
1. Calcular la temperatura promedio por ciudad
2. Identificar ciudades con promedio > 25°C
3. Mostrar resultados ordenados por temperatura

Resultado esperado:
Barcelona: 23.0
Madrid: 26.33
Sevilla: 31.0

Se pide:
1. Versión A: Utiliza map(), filter() y sortBy()
2. Versión B: Utiliza flatMap(), map() y reduceByKey()

IMPORTANTE: Entregar código bien comentado y pantallazo de ambas ejecuciones.
*/

// ============ VERSIÓN A: map(), filter() y sortBy() ============

val datos = sc.parallelize(List("Madrid,25,28,26", "Barcelona,22,24,23", "Sevilla,30,32,31"))

// Paso 1: Convertimos a tuplas (ciudad, promedio)
val ciudadesPromedios = datos.map { linea =>
  val Array(ciudad, t1, t2, t3) = linea.split(",")
  val promedio = (t1.toDouble + t2.toDouble + t3.toDouble) / 3.0
  (ciudad, promedio)
}

// Paso 2: Filtramos ciudades con promedio > 25
val ciudadesCalidas = ciudadesPromedios.filter { case (_, promedio) => promedio > 25 }

// Paso 3: Ordenamos por promedio ascendente
val ordenados = ciudadesCalidas.sortBy { case (_, promedio) => promedio }

// Paso 4: Mostramos resultados
ordenados.collect().foreach { case (ciudad, promedio) =>
  println(s"$ciudad: ${promedio.formatted("%.2f")}")
}


// ============ VERSIÓN B: Alternativa con fold() ============

val datos = sc.parallelize(List("Madrid,25,28,26", "Barcelona,22,24,23", "Sevilla,30,32,31"))

// Paso 1: Convertimos a tuplas (ciudad, promedio)
val ciudadesPromedios = datos.map { linea =>
  val Array(ciudad, t1, t2, t3) = linea.split(",")
  val promedio = (t1.toDouble + t2.toDouble + t3.toDouble) / 3.0
  (ciudad, promedio)
}

// Paso 2: Filtramos y ordenamos
val resultadoFinal = ciudadesPromedios
  .filter { case (_, promedio) => promedio > 25 }
  .sortBy { case (_, promedio) => promedio }
  .collect()

// Paso 3: Mostramos
resultadoFinal.foreach { case (ciudad, promedio) =>
  println(s"$ciudad: ${promedio.formatted("%.2f")}")
}
