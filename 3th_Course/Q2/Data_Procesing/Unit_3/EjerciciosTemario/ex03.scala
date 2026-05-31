//Transformaciones y acciones con RDDs

//Crear RDD de números y contar elementos.
//Crear RDD de texto y números repetidos.

//map y flatMap:
//Transformar líneas en palabras individuales.

//filter:
//Filtrar elementos por condición.

//Comparar:
//flatMap+filter y filter+flatMap.

//distinct:
//Eliminar duplicados.

//countByValue:
//Contar ocurrencias.

//sample y takeSample:
//Extraer muestras con/sin reemplazo.

//Operaciones entre RDD:
//union,intersection,subtract,cartesian.

//Ordenación:
//sortByKey ascendente y descendente.

//Palabras:
//Aplicar countByValue para frecuencia.

//top y takeOrdered:
//Obtener valores mayores o menores.

//reduce:
//Calcular suma y multiplicación.

//fold:
//Probar distintos valores iniciales.

//aggregate:
//Procesar y combinar particiones.

//reduceByKey:
//Sumar valores por clave.

//map:
//Generar mensajes con interpolación.

//Particiones:
//Verificar cantidad de particiones.
//Usar repartition y coalesce.

//Contar palabras:
//"Spark" y "Scala" con reduceByKey.

//Agrupar números:
//0-99 por resto/3 y sumar valores.

// Paso 1: Crear RDD de números y contar elementos

val numerosRDD = sc.parallelize(1 to 100)
val cantidadNumeros = numerosRDD.count()

// Paso 2: Crear RDD de texto y números repetidos
val textoNumerosRDD = sc.parallelize(Seq("uno", "dos", "tres", "uno", "dos", "cuatro"))
val cantidadTextosNumeros = textoNumerosRDD.count()

// Paso 3: Transformar líneas en palabras individuales usando map y flatMap

val lineasRDD = sc.parallelize(Seq("Hola mundo", "Spark es genial"))
val palabrasMap = lineasRDD.map(line => line.split(" "))
val palabrasFlatMap = lineasRDD.flatMap(line => line.split(" "))

// Paso 4: Filtrar elementos por condición
val numerosPares = numerosRDD.filter(num => num % 2 == 0)
val palabrasConO = textoNumerosRDD.filter(word => word.contains("o"))

// Paso 5: Comparar flatMap+filter y filter+flatMap
val palabrasConOFlatMapFilter = lineasRDD.flatMap(line => line.split(" ")).filter(word => word.contains("o"))
val palabrasConOFilterFlatMap = lineasRDD.filter(line => line.contains("o")).flatMap(line => line.split(" "))   

// Paso 6: Eliminar duplicados con distinct
val palabrasDistintas = textoNumerosRDD.distinct()

// Paso 7: Contar ocurrencias con countByValue
val conteoPalabras = textoNumerosRDD.countByValue()

// Paso 8: Extraer muestras con/sin reemplazo usando sample y takeSample
val muestraSinReemplazo = numerosRDD.sample(false, 0.1).collect()
val muestraConReemplazo = numerosRDD.sample(true, 0.1).collect()

// Paso 9: Operaciones entre RDD: union, intersection, subtract, cartesian
val rddA = sc.parallelize(Seq(1, 2, 3, 4))
val rddB = sc.parallelize(Seq(3, 4, 5, 6))
val unionRDD = rddA.union(rddB)
val intersectionRDD = rddA.intersection(rddB)
val subtractRDD = rddA.subtract(rddB)
val cartesianRDD = rddA.cartesian(rddB)

// Paso 10: Ordenación con sortByKey ascendente y descendente
val rddClaveValor = sc.parallelize(Seq(("a", 3), ("b", 1), ("c", 2)))
val ordenAscendente = rddClaveValor.sortByKey(ascending = true)
val ordenDescendente = rddClaveValor.sortByKey(ascending = false)

// Paso 11: Aplicar countByValue para frecuencia de palabras
val frecuenciaPalabras = lineasRDD.flatMap(line => line.split(" ")).countByValue()

// Paso 12: Obtener valores mayores o menores con top y takeOrdered
val numerosTop = numerosRDD.top(5)
val numerosMenores = numerosRDD.takeOrdered(5)

// Paso 13: Calcular suma y multiplicación con reduce
val sumaNumeros = numerosRDD.reduce((a, b) => a + b)
val multiplicacionNumeros = numerosRDD.reduce((a, b) => a * b)

// Paso 14: Probar distintos valores iniciales con fold
val sumaConValorInicial = numerosRDD.fold(100)((a, b) => a + b)
val multiplicacionConValorInicial = numerosRDD.fold(1)((a, b) => a * b)

// Paso 15: Procesar y combinar particiones con aggregate
val sumaParticiones = numerosRDD.aggregate(0)((acc, num) => acc + num, (acc1, acc2) => acc1 + acc2) 
val multiplicacionParticiones = numerosRDD.aggregate(1)((acc, num) => acc * num, (acc1, acc2) => acc1 * acc2)

// Paso 16: Sumar valores por clave con reduceByKey
val rddClaveValor2 = sc.parallelize(Seq(("a", 1), ("b", 2), ("a", 3), ("c", 4)))
val sumaPorClave = rddClaveValor2.reduceByKey((a, b) => a + b)

// Paso 17: Generar mensajes con interpolación usando map
val mensajes = numerosRDD.map(num => s"El número es: $num")

