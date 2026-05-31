//MapReduce con RDD y El Quijote

//Descargar archivo:
//wget http://www.gutenberg.org/cache/epub/2000/pg2000.txt

//Cargar desde local:
//val quijoteRDD=sc.textFile("file:///home/bigdata/Descargas/pg2000.txt")

//Ver particiones:
//quijoteRDD.getNumPartitions

//Cargar desde HDFS con 10 particiones:
//val quijoteRDD=sc.textFile("hdfs://localhost:9000/ebooks/quijote.txt",10)

//Verificar particiones:
//quijoteRDD.getNumPartitions

//Consultas:
//Contar líneas con "molino".
//Contar palabras distintas.
//Obtener top 10 palabras (>3 letras).
//Contar apariciones de "hidalgo".
//Contar líneas totales.
//Contar líneas con más de 20 caracteres.
//Encontrar línea más larga y su tamaño.

// Paso 1: Contar líneas con "molino"
val molinoCount = quijoteRDD.filter(line => line.contains("molino")).count()

// Paso 2: Contar palabras distintas
val palabrasDistintas = quijoteRDD
    .flatMap(line => line.split("\\W+")) // Dividir por caracteres no alfanuméricos
    .filter(word => word.nonEmpty) // Filtrar palabras vacías
    .distinct() // Obtener palabras distintas
val numPalabrasDistintas = palabrasDistintas.count()

// Paso 3: Obtener top 10 palabras (>3 letras)
val topPalabras = quijoteRDD
    .flatMap(line => line.split("\\W+"))
    .filter(word => word.length > 3)
    .map(word => (word.toLowerCase, 1)) // Convertir a minúsculas para contar sin distinción de mayúsculas
    .reduceByKey(_ + _) // Contar apariciones
    .sortBy(_._2, ascending = false) // Ordenar por frecuencia
    .take(10) // Obtener top 10

// Paso 4: Contar apariciones de "hidalgo"
val hidalgoCount = quijoteRDD
    .flatMap(line => line.split("\\W+"))
    .filter(word => word.equalsIgnoreCase("hidalgo"))
    .count()

// Paso 5: Contar líneas totales
val totalLineas = quijoteRDD.count()

// Paso 6: Contar líneas con más de 20 caracteres
val lineasLargas = quijoteRDD.filter(line => line.length > 20).count()

