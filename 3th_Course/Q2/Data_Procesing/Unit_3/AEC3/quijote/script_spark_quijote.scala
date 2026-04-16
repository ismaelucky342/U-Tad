// Script Spark para responder a todas las preguntas del ejercicio
// Ejecutar en spark-shell con :load script_spark_quijote.scala

// Cargar el archivo desde HDFS con 10 particiones
val quijoteRDD = sc.textFile("hdfs://localhost:9000/ebooks/quijote.txt", 10)

// 1. ¿En cuántas líneas aparece la palabra "molino"?
val numLineasMolino = quijoteRDD.filter(_.toLowerCase.contains("molino")).count()
println(s"Líneas con 'molino': $numLineasMolino")

// 2. ¿Cuántas palabras distintas aparecen en el texto?
val palabras = quijoteRDD.flatMap(_.split("\\W+").filter(_.nonEmpty).map(_.toLowerCase))
val numPalabrasDistintas = palabras.distinct().count()
println(s"Palabras distintas: $numPalabrasDistintas")

// 3. Top 10 palabras más repetidas (>3 letras)
val top10 = palabras.filter(_.length > 3)
  .map(p => (p, 1L)).reduceByKey(_ + _)
  .sortBy(-_._2).take(10)
println("Top 10 palabras (>3 letras):")
top10.foreach{case (pal, cnt) => println(s"$pal: $cnt")}

// 4. ¿Cuántas veces aparece la palabra "hidalgo"?
val numHidalgo = palabras.filter(_ == "hidalgo").count()
println(s"Veces 'hidalgo': $numHidalgo")

// 5. ¿Cuántas líneas tiene el texto?
val numLineas = quijoteRDD.count()
println(s"Total líneas: $numLineas")

// 6. ¿Cuántas líneas tienen más de 20 caracteres?
val numLineas20 = quijoteRDD.filter(_.length > 20).count()
println(s"Líneas >20 caracteres: $numLineas20")

// 7. ¿Cuál es la línea más larga y cuántos caracteres tiene?
val lineaMasLarga = quijoteRDD.map(l => (l.length, l)).sortByKey(false).first()
println(s"Línea más larga (${lineaMasLarga._1} caracteres):")
println(lineaMasLarga._2)
