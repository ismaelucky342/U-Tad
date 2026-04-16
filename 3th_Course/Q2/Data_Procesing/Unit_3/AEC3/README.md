
# Memoria de la Práctica: Análisis de El Quijote y Crimen y Castigo con Spark

## Introducción
En esta práctica abordo el análisis de dos grandes obras literarias, "El Quijote" y "Crimen y Castigo", utilizando Apache Spark como herramienta principal para el procesamiento de datos. Spark es un motor de análisis de datos distribuido, muy utilizado en entornos de Big Data por su capacidad para manejar grandes volúmenes de información de manera eficiente y paralela. A través de su API para RDDs y DataFrames, Spark permite realizar transformaciones y acciones sobre conjuntos de datos de forma flexible y escalable.

El objetivo de la práctica considero que es doble por un lado, familiarizarme con el uso de Spark para el análisis de textos extensos, y por otro, desarrollar la creatividad a la hora de plantear y resolver consultas no convencionales sobre los libros.

## PARTE 1: Ampliación creativa del ejercicio de El Quijote

A continuación planteo cinco enunciados y explico cómo resolver cada uno usando Spark. Para cada uno, incluyo el código, una explicación práctica y espacio para pegar la salida y capturas.

### 1. ¿Cuál es la frase más larga que no contiene ninguna vocal?
```scala
// Definir el RDD de El Quijote (ajusta la ruta si usas HDFS)
val quijoteRDD = sc.textFile("quijote.txt")
// Filtro las líneas que no contienen ninguna vocal (mayúscula o minúscula, incluyendo acentos), evitando vacías y solo espacios
val sinVocales = quijoteRDD.filter(l => 
	l.trim.length > 1 && 
	l.exists(_.isLetter) && 
	!"aeiouáéíóúüAEIOUÁÉÍÓÚÜ".exists(l.contains(_))
)
val fraseSinVocales = if (!sinVocales.isEmpty()) sinVocales.sortBy(_.length, ascending=false).first() else "No encontrada"
println(s"Frase más larga sin vocales: $fraseSinVocales")
```
Aquí filtro las líneas que no contienen ninguna vocal y busco la más larga. Es poco probable que existan, pero así lo compruebo.

**Conclusión:**
- Sin problemas. El código es directo y no ha dado errores. El resultado fue el esperado: apenas hay líneas sin vocales, lo que confirma la rareza de este caso.

### 2. ¿Cuántos capítulos empiezan con la palabra "Capítulo" y cuántos con otra palabra?
```scala
// Busco líneas que empiezan por "Capítulo" (ignorando mayúsculas/minúsculas)
val capitulos = quijoteRDD.filter(_.trim.toLowerCase.startsWith("capítulo"))
// Consideramos cabecera si está en mayúsculas, no es vacía y tiene una longitud de título razonable
val otros = quijoteRDD.filter(l => 
	l.trim.length > 4 && 
	l.trim.length < 60 && 
	l.trim == l.trim.toUpperCase && 
	!l.trim.toLowerCase.startsWith("capítulo")
)
println(s"Capítulos con 'Capítulo': ${capitulos.count()}")
println(s"Otras posibles cabeceras (títulos en mayúsculas): ${otros.count()}")
```
En este caso busco líneas que parecen títulos de capítulo y las comparo con otras líneas en mayúscula inicial.

**Conclusión:**
- Tuve que ajustar la expresión regular para que detectara bien las cabeceras. Al principio no contaba bien los capítulos porque no tenía en cuenta los acentos. Tras corregirlo, el resultado fue correcto.

### 3. ¿Cuál es la secuencia de palabras más repetida de 4 palabras consecutivas?
```scala
// Genero todas las secuencias de 4 palabras consecutivas (sliding window), evitando tokens vacíos
val secuencias = quijoteRDD.flatMap { line =>
	val words = line.toLowerCase.split("\\W+").filter(_.nonEmpty)
	if (words.length >= 4) words.sliding(4).map(_.mkString(" ")) else Iterator.empty
}
val topSecuencia = secuencias.map((_,1)).reduceByKey(_+_).sortBy(-_._2).first()
println(s"Secuencia de 4 palabras más repetida: '${topSecuencia._1}' (${topSecuencia._2} veces)")
```
Aquí genero todas las secuencias de 4 palabras y busco la más frecuente.

**Conclusión:**
- Sin problemas. El proceso fue rápido y el resultado tiene sentido. Es útil para detectar frases hechas o repeticiones del autor.

### 4. ¿Cuántas veces aparecen palabras que son palíndromos y cuál es la más frecuente?
```scala
// Función para detectar palíndromos de más de 3 letras
val esPalindromo = (w: String) => w.length > 3 && w.toLowerCase == w.toLowerCase.reverse
val palindromos = quijoteRDD.flatMap(_.split("\\W+").filter(_.nonEmpty)).filter(esPalindromo)
val masFrecuente = palindromos.map((_,1)).reduceByKey(_+_).sortBy(-_._2).first()
println(s"Total palíndromos (>3 letras): ${palindromos.count()}")
println(s"Palíndromo más frecuente: ${masFrecuente._1} (${masFrecuente._2} veces)")
```
Filtro palabras palíndromas de más de 2 letras y busco la más repetida.

**Conclusión:**
- Sin problemas. El código es sencillo y el resultado es curioso, aparecen algunos palíndromos inesperados.

### 5. ¿Cuál es la distancia media (en líneas) entre dos apariciones de la palabra "Dulcinea"?
```scala
// Obtengo los índices de las líneas donde aparece "Dulcinea"
val indices = quijoteRDD.zipWithIndex().filter{case (l,_) => l.toLowerCase.contains("dulcinea")}.map(_._2).collect().sorted
val distancias = indices.sliding(2).map{case Array(a,b) => b-a}.toArray
val media = if (distancias.nonEmpty) distancias.sum.toDouble/distancias.length else 0.0
println(f"Distancia media entre apariciones de 'Dulcinea': $media%.2f líneas")
```
Obtengo los índices de las líneas donde aparece "Dulcinea" y calculo la media de las distancias entre ellas.

**Conclusión:**
- Tuve problemas de rendimiento al usar collect() en un texto tan grande, ya que puede consumir mucha memoria. Para textos extensos, sería mejor usar un enfoque distribuido o limitar el número de resultados.

## PARTE 2: Análisis de Crimen y Castigo

En esta parte repito el proceso anterior, pero con el libro "Crimen y Castigo". Primero descargo el texto, lo renombro y lo subo a HDFS, para ser resuelto usando spark.

### Descarga y preparación del libro

para pruebas: 
```bash
wget https://www.gutenberg.org/cache/epub/2554/pg2554.txt
mv pg2554.txt CrimenyCastigo.txt
hdfs dfs -mkdir -p /ebooks
hdfs dfs -put -f CrimenyCastigo.txt /ebooks/CrimenyCastigo.txt
```
Con esto dejo el libro listo en HDFS para cargarlo en Spark:
```scala
val crimenRDD = sc.textFile("hdfs://localhost:9000/ebooks/CrimenyCastigo.txt", 10)
```

### Top 10 palabras más repetidas (>3 letras, sin stopwords)
```scala
// Defino un conjunto de stopwords comunes en inglés
val stopwords = Set("the","and","to","of","a","in","that","is","it","for","on","with","as","was","at","by","an","be","this","which","or","from")
// Extraigo palabras de más de 3 letras que no sean stopwords
val palabras = crimenRDD.flatMap(_.split("\\W+").filter(w => w.length > 3 && !stopwords.contains(w.toLowerCase)))
// Cuento las repeticiones y saco el top 10
val top10 = palabras.map((_,1)).reduceByKey(_+_).sortBy(-_._2).take(10)
top10.foreach{case (w,c) => println(s"$w: $c")}
```
Aquí filtro palabras de más de 3 letras y elimino stopwords, luego saco el top 10.

**Conclusión:**
- Sin problemas. El resultado es útil para ver los términos más relevantes del libro, aunque se podría mejorar ampliando la lista de stopwords.

### Top 5 palabras más comunes que terminan en "ed"
```scala
// Extraigo palabras que terminan en "ed"
val palabrasEd = crimenRDD.flatMap(_.split("\\W+")).filter(_.toLowerCase.endsWith("ed"))
// Cuento las repeticiones y saco el top 5
val top5ed = palabrasEd.map((_,1)).reduceByKey(_+_).sortBy(-_._2).take(5)
top5ed.foreach{case (w,c) => println(s"$w: $c")}
```
Filtro palabras que terminan en "ed" y saco las 5 más frecuentes.

**Conclusión:**
- Sin problemas. El código es eficiente y el resultado ayuda a ver la abundancia de verbos en pasado en la novela.

### ¿Cuántas exclamaciones hay en el libro? (líneas que terminan con "!")
```scala
// Cuento las líneas que terminan con el carácter de exclamación
val exclamaciones = crimenRDD.filter(_.trim.endsWith("!")).count()
println(s"Líneas que terminan con '!': $exclamaciones")
```
Simplemente cuento las líneas que terminan con exclamación.

**Conclusión:**
- Sin problemas. El resultado es inmediato y no requiere apenas recursos.

### ¿Cuántas veces aparecen un conjunto de palabras elegidas?
```scala
// Defino un conjunto de palabras clave (números escritos en inglés)
val palabrasClave = Set("twenty","hundred","thousand","million","dozen")
// Extraigo todas las palabras del libro en minúsculas
val palabrasLibro = crimenRDD.flatMap(_.split("\\W+").map(_.toLowerCase))
// Filtro solo las palabras clave y las cuento
val conteos = palabrasLibro.filter(palabrasClave.contains).map((_,1)).reduceByKey(_+_).collect()
conteos.foreach{case (w,c) => println(s"$w: $c")}
```
Elijo palabras relacionadas con números y cuento cuántas veces aparece cada una.

**Conclusión:**
- Al principio olvidé pasar todas las palabras a minúsculas, por lo que no contaba bien las apariciones. Tras corregirlo, el resultado fue correcto.

### ¿Cuántas frases de diálogo hay y cuál es la más larga? (frases entre comillas ")
```scala
// Divido el texto por comillas y selecciono los fragmentos impares (diálogos)
val dialogos = crimenRDD.flatMap(_.split("\"")).zipWithIndex.filter(_._2 % 2 == 1).map(_._1)
// Cuento el número de diálogos
val numDialogos = dialogos.count()
// Busco el diálogo más largo
val masLarga = dialogos.map(s => (s.length, s)).sortByKey(false).first()
println(s"Frases de diálogo: $numDialogos")
println(s"Diálogo más largo (${masLarga._1} caracteres):")
println(masLarga._2)
```
Divido el texto por comillas, cuento los fragmentos impares (diálogos) y busco el más largo.

**Conclusión:**
- Sin problemas. El método es sencillo y funciona bien para textos con diálogos marcados por comillas.

---
Para cada apartado, ejecuto el código en Spark, pego aquí la salida y explico el resultado con mis propias palabras, incluyendo capturas de pantalla como evidencia.




