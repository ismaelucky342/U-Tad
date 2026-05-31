//Key-Value RDDs en Spark

//RDD base:
//val rdd=sc.parallelize(Seq((1,2),(3,4),(3,6)))

//reduceByKey:
//Obtener nº de particiones por defecto.
//Analizar impacto en rendimiento.
//Calcular valor máximo por clave.

//groupByKey:
//Agrupar valores y obtener mínimo por clave.

//mapValues:
//Multiplicar por 3 valores múltiplos de 3.

//combineByKey:
//Calcular salario máximo por departamento.

//flatMapValues:
//Descomponer listas y obtener máximo por grupo.

//Ordenar salarios:
//Ordenar de mayor a menor.

//leftOuterJoin:
//Calcular suma por clave.

//Filtrar claves:
//Mantener claves con dos o más valores.

//Notas alumnos:
//Nota=10%Asistencia+20%Parcial+20%Práctica+50%Examen
//Filtrar no Erasmus y examen>=4

//Clase:
//val clase1=sc.parallelize(Seq(("Juanito",Seq(10,5,9,3)),("Pepito",Seq(8,8,5,8)),("Manolito",Seq(7,3,9,4))))

//HDFS:
//Iniciar HDFS.
//Guardar resultado:
//saveAsTextFile("/ejercicios/ejercicio9")

//Comprobar nº de archivos generados.

// paso 1: crear un RDD de pares (clave-valor)

val rdd = sc.parallelize(Seq(("a", 1), ("b", 2), ("a", 3), ("c", 4)))

// paso 2: aplicar reduceByKey para sumar valores por clave

val rddSuma = rdd.reduceByKey(_ + _)

// paso 3: aplicar groupByKey para agrupar valores por clave

val rddAgrupado = rdd.groupByKey()

// paso 4: aplicar mapValues para multiplicar por 3 valores múltiplos de 3

val rddMapValues = rdd.mapValues(x => if (x % 3 == 0) x * 3 else x)

// paso 5: aplicar combineByKey para calcular salario máximo por departamento
val salarios = sc.parallelize(Seq(("HR", 3000), ("IT", 4000), ("HR", 3500), ("IT", 4500)))

// paso 6: aplicar flatMapValues para descomponer listas y obtener máximo por grupo
val rddListas = sc.parallelize(Seq(("grupo1", Seq(1, 2, 3)), ("grupo2", Seq(4, 5))))

// paso 7: ordenar salarios de mayor a menor
val rddOrdenado = salarios.sortBy(_._2, ascending = false)

// paso 8: aplicar leftOuterJoin para calcular suma por clave
val rdd1 = sc.parallelize(Seq(("a", 1), ("b", 2)))
val rdd2 = sc.parallelize(Seq(("a", 3), ("c", 4)))
val rddJoin = rdd1.leftOuterJoin(rdd2).mapValues {
  case (v1, Some(v2)) => v1 + v2
  case (v1, None) => v1
}

// paso 9: filtrar claves con dos o más valores
val rddFiltrado = rdd.groupByKey().filter { case (_, values) => values.size >= 2 }

// paso 10: calcular nota de alumnos y filtrar no Erasmus con examen >= 4
val alumnos = sc.parallelize(Seq(("Juanito", Seq(10, 5, 9, 3), false), ("Pepito", Seq(8, 8, 5, 8), true), ("Manolito", Seq(7, 3, 9, 4), false)))    



