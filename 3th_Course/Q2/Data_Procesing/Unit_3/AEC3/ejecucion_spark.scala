// ========== CARGA DE DATOS ==========
val quijoteRDD = sc.textFile("hdfs://localhost:9000/ebooks/quijote.txt")
val crimenRaw = sc.textFile("hdfs://localhost:9000/ebooks/CrimenyCastigo.txt")
val crimenRDD = crimenRaw.filter(l => !l.contains("Project Gutenberg") && !l.contains("License") && !l.contains("http"))

// ========== PARTE 1: El Quijote ==========

// 1. Frase más larga sin vocales
val sinVocales = quijoteRDD.filter(l => l.trim.length > 1 && l.exists(_.isLetter) && !"aeiouáéíóúüAEIOUÁÉÍÓÚÜ".exists(l.contains(_)))
val fraseSinVocales = if (!sinVocales.isEmpty()) sinVocales.sortBy(_.length, ascending=false).first() else "No encontrada"
println(s"Frase más larga sin vocales: $fraseSinVocales")

// 2. Capítulos y Cabeceras
val capitulosCount = quijoteRDD.filter(_.trim.toLowerCase.startsWith("capítulo")).count()
val otrosCount = quijoteRDD.filter(l => l.trim.length > 4 && l.trim.length < 60 && l.trim == l.trim.toUpperCase && !l.trim.toLowerCase.startsWith("capítulo")).count()
println(s"Capítulos con 'Capítulo': $capitulosCount")
println(s"Otras posibles cabeceras: $otrosCount")

// 3. Secuencia de 4 palabras
val topSecuencia = quijoteRDD.flatMap { line =>
    val words = line.toLowerCase.split("\\W+").filter(_.nonEmpty)
    if (words.length >= 4) words.sliding(4).map(_.mkString(" ")) else Iterator.empty
}.map((_,1)).reduceByKey(_+_).sortBy(-_._2).first()
println(s"Secuencia de 4 palabras más repetida: '${topSecuencia._1}' (${topSecuencia._2} veces)")

// 4. Palíndromos
val palindromosRDD = quijoteRDD.flatMap(_.split("\\W+").filter(_.nonEmpty)).filter(w => w.length > 3 && w.toLowerCase == w.toLowerCase.reverse)
val masFrecuentePal = palindromosRDD.map((_,1)).reduceByKey(_+_).sortBy(-_._2).first()
println(s"Total palíndromos: ${palindromosRDD.count()}")
println(s"Palíndromo más frecuente: ${masFrecuentePal._1}")

// 5. Distancia Dulcinea
val indicesD = quijoteRDD.zipWithIndex().filter{case (l,_) => l.toLowerCase.contains("dulcinea")}.map(_._2).collect().sorted
val distanciasD = indicesD.sliding(2).map{case Array(a,b) => b-a}.toArray
val mediaD = if (distanciasD.nonEmpty) distanciasD.sum.toDouble/distanciasD.length else 0.0
println(f"Distancia media 'Dulcinea': $mediaD%.2f líneas")


// ========== PARTE 2: Crimen y Castigo ==========

val stopwords = Set("the","and","to","of","a","in","that","is","it","for","on","with","as","was","at","by","an","be","this","which","or","from", "they", "them", "their", "what", "have", "there")

// a) Top 10 palabras (Aseguramos que sea Array para el foreach)
val resultadosTop10 = crimenRDD.flatMap(_.split("\\W+")).filter(w => w.length > 3 && !stopwords.contains(w.toLowerCase)).map(w => (w.toLowerCase, 1)).reduceByKey(_+_).sortBy(-_._2).take(10)
println("Top 10 palabras en Crimen y Castigo:")
resultadosTop10.foreach{ case (w, c) => println(s" - $w: $c") }

// b) Top 5 "ed"
val resultadosTop5ed = crimenRDD.flatMap(_.split("\\W+")).filter(w => w.length > 3 && w.toLowerCase.endsWith("ed")).map(w => (w.toLowerCase, 1)).reduceByKey(_+_).sortBy(-_._2).take(5)
println("Top 5 palabras terminadas en 'ed':")
resultadosTop5ed.foreach{ case (w, c) => println(s" - $w: $c") }

// c) Exclamaciones
println(s"Líneas que terminan con '!': ${crimenRDD.filter(_.trim.endsWith("!")).count()}")

// d) Palabras clave
val palabrasClave = Set("twenty","hundred","thousand","million","dozen")
val resultadosConteos = crimenRDD.flatMap(_.split("\\W+").map(_.toLowerCase)).filter(palabrasClave.contains).map((_,1)).reduceByKey(_+_).collect()
println("Conteo de palabras clave:")
resultadosConteos.foreach{ case (w, c) => println(s" - $w: $c") }

// e) Diálogos (Limpiando mejor las comillas de la licencia)
val dialogosRDD = crimenRDD.filter(l => !l.contains("Gutenberg")).flatMap(_.split("\"")).zipWithIndex.filter(_._2 % 2 == 1).map(_._1).filter(_.length > 10)
val masLargaD = dialogosRDD.map(s => (s.length, s)).sortBy(-_._1).first()
println(s"Frases de diálogo: ${dialogosRDD.count()}")
println("Diálogo más largo:")
println(masLargaD._2.trim)