/*
Ejercicio 2_E - Scala + Spark Básico: PROCESAMIENTO DE EVENTOS

Dado un RDD con eventos de usuario:
val eventos = sc.parallelize(List("user1,login", "user2,logout", "user1,click", "user2,login", "user1,logout"))

Formato: usuario,tipo_evento

Se pide procesar para:
1. Contar eventos por usuario
2. Filtrar usuarios que tengan más de 1 evento
3. Mostrar resultado en formato usuario: cantidad_eventos

Resultado esperado:
user1: 3
user2: 2

Se pide:
1. Versión A: Utiliza map(), reduceByKey() y filter()
2. Versión B: Utiliza flatMap() y groupByKey()

IMPORTANTE: Entregar código bien comentado y pantallazo de ambas ejecuciones.
*/

// ============ VERSIÓN A: map(), reduceByKey() y filter() ============

val eventos = sc.parallelize(List("user1,login", "user2,logout", "user1,click", "user2,login", "user1,logout"))

// Paso 1: Extraemos usuario y mapeamos a (usuario, 1) para contar
val usuariosConteo = eventos.map { evento =>
  val Array(usuario, _) = evento.split(",")
  (usuario, 1)
}

// Paso 2: Sumamos conteos por usuario con reduceByKey
val usuariosAgrupados = usuariosConteo.reduceByKey((a, b) => a + b)

// Paso 3: Filtramos usuarios con más de 1 evento
val usuariosConEventos = usuariosAgrupados.filter { case (_, cantidad) => cantidad > 1 }

// Paso 4: Mostramos resultados
usuariosConEventos.collect().foreach { case (usuario, cantidad) =>
  println(s"$usuario: $cantidad")
}


// ============ VERSIÓN B: map() y groupByKey() ============

val eventos = sc.parallelize(List("user1,login", "user2,logout", "user1,click", "user2,login", "user1,logout"))

// Paso 1: Extraemos usuario y tipo_evento como tuplas
val eventosMap = eventos.map { evento =>
  val Array(usuario, tipoEvento) = evento.split(",")
  (usuario, tipoEvento)
}

// Paso 2: Agrupamos eventos por usuario
val eventosAgrupados = eventosMap.groupByKey()

// Paso 3: Contamos eventos por usuario
val usuariosConteo = eventosAgrupados.map { case (usuario, eventos) =>
  (usuario, eventos.toList.length)
}

// Paso 4: Filtramos y mostramos
usuariosConteo.filter { case (_, cantidad) => cantidad > 1 }
  .collect()
  .foreach { case (usuario, cantidad) =>
    println(s"$usuario: $cantidad")
  }
