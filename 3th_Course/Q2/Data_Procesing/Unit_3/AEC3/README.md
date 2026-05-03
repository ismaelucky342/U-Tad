## Introducción

En esta práctica abordo el análisis de dos grandes obras literarias, “El Quijote” y “Crimen y Castigo”, utilizando Apache Spark como herramienta principal para el procesamiento de datos. Spark es un motor de análisis de datos distribuido y a través de su API para RDDs y DataFrames, permite realizar transformaciones y acciones sobre conjuntos de datos de forma flexible y escalable.

El objetivo de la práctica considero que es doble por un lado, familiarizarme con el uso de Spark para el análisis de textos extensos, y por otro, desarrollar la creatividad a la hora de plantear y resolver consultas no convencionales sobre los libros.

## PARTE 1: Ampliación del ejercicio de El Quijote

A continuación planteo cinco enunciados y explico cómo resolver cada uno y que dificultades técnicas he tenido con la mayoría de ellos. 

### Enunciado 1. ¿Cuál es la frase más larga que no contiene ninguna vocal?

```scala
// Filtro las líneas que no contienen ninguna vocal (mayúscula o minúscula, incluyendo acentos)
val quijoteRDD = sc.textFile("hdfs://localhost:9000/ebooks/quijote.txt")
val sinVocales = quijoteRDD.filter(l => l.trim.length > 1 && l.exists(_.isLetter) && !"aeiouáéíóúüAEIOUÁÉÍÓÚÜ".exists(l.contains(_)))
// Ordeno por longitud descendente y tomo la más larga
val fraseSinVocales = if (!sinVocales.isEmpty()) sinVocales.sortBy(_.length, ascending=false).first() else "No encontrada"
println(s"Frase más larga sin vocales: $fraseSinVocales")
```

Aquí filtro las líneas que no contienen ninguna vocal y busco la más larga. Es poco probable que existan, pero así lo compruebo.

![image.png](attachment:51e9ecd4-472a-408b-b0ce-fe960a135e9b:image.png)

**Conclusión:**
El resultado ha sido o una cadena como "1.F." , o incluso una línea vacía. Esto ocurre porque en los textos originales hay líneas con numeraciones, metadatos o ruido que no contienen vocales pero tampoco son frases literarias. Por eso, se añadieron filtros para descartar líneas vacías y exigir que la línea tenga al menos una letra. Aun así, seguimos teniendo ese 1.F. 

### Enunciado 2. ¿Cuántos capítulos empiezan con la palabra “Capítulo” y cuántos con otra palabra?

```scala
// Busco líneas que empiezan por "Capítulo" (ignorando mayúsculas/minúsculas)
val capitulosCount = quijoteRDD.filter(_.trim.toLowerCase.startsWith("capítulo")).count()

// Busco otras líneas que parecen cabeceras (empiezan por mayúscula pero no por "Capítulo")
val otrosCount = quijoteRDD.filter(l => l.trim.length > 4 && l.trim.length < 60 && l.trim == l.trim.toUpperCase && !l.trim.toLowerCase.startsWith("capítulo")).count()
println(s"Capítulos con 'Capítulo': $capitulosCount")
println(s"Otras posibles cabeceras: $otrosCount")
```

En este caso busco líneas que parecen títulos de capítulo y las comparo con otras líneas en mayúscula inicial.

![image.png](attachment:2fc7b0bc-67a3-4da6-9b3a-541d34d0efdb:image.png)

**Conclusión:**
El número de cabeceras detectadas puede ser bajo si el texto no sigue un formato homogéneo o si hay líneas en mayúsculas que no son títulos reales. Aádí filtros de longitud y mayúsculas para evitar falsos positivos, pero aún así pueden aparecer títulos poco representativos si el texto contiene ruido o metadatos en mayúsculas.

### Enunciado 3. ¿Cuál es la secuencia de palabras más repetida de 4 palabras consecutivas?

```scala
// Genero todas las secuencias de 4 palabras consecutivas (sliding window)
val secuencias = quijoteRDD.flatMap(_.split("\\W+").sliding(4).map(_.mkString(" ").toLowerCase))
// Cuento las repeticiones y saco la más frecuente
val topSecuencia = quijoteRDD.flatMap { line =>
    val words = line.toLowerCase.split("\\W+").filter(_.nonEmpty)
    if (words.length >= 4) words.sliding(4).map(_.mkString(" ")) else Iterator.empty
}.map((_,1)).reduceByKey(_+_).sortBy(-_._2).first()
println(s"Secuencia de 4 palabras más repetida: '${topSecuencia._1}' (${topSecuencia._2} veces)")
```

Aquí genero todas las secuencias de 4 palabras y busco la más frecuente.

![image.png](attachment:55f0a238-fde9-4d83-a376-b5823c226182:image.png)

**Conclusión:**
La secuencia más repetida puede ser una combinación poco literaria (por ejemplo, "se or don quijote") debido a problemas de tokenización con la letra ñ o a la presencia de palabras cortadas por saltos de línea o caracteres especiales. Aqui se me ocurrió meter filtros para evitar tokens vacíos, pero la tokenización simple con split("\W+") puede separar mal palabras con tildes o signos de puntuación. Para resultados más literarios, creo que sería recomendable usar una tokenización más avanzada.

### Enunciado 4. ¿Cuántas veces aparecen palabras que son palíndromos y cuál es la más frecuente?

```scala
val palindromosRDD = quijoteRDD.flatMap(_.split("\\W+").filter(_.nonEmpty)).filter(w => w.length > 3 && w.toLowerCase == w.toLowerCase.reverse)
//validación de mas frecuente
val masFrecuentePal = palindromosRDD.map((_,1)).reduceByKey(_+_).sortBy(-_._2).first()
println(s"Total palíndromos: ${palindromosRDD.count()}")

println(s"Palíndromo más frecuente: ${masFrecuentePal._1}")
```

Filtro palabras palíndromas de más de 3 letras y busco la más repetida.

![image.png](attachment:7d700ee2-7ad0-4619-b353-10594d786363:image.png)

**Conclusión:**
Aquí me he topado con que el palíndromo más frecuente no siempre es una palabra real, sino una secuencia de letras o una palabra cortada (por ejemplo, "sus"). Esto ocurre por la tokenización simple y porque en el texto pueden aparecer fragmentos o palabras incompletas. Directamente aumenté la longitud mínima a más de 3 letras para evitar falsos positivos, aunque lo mas repetido ahora es “conoc” habría que hacer un analizador morfologico mas exaustivo.

### Enunciado 5. ¿Cuál es la distancia media (en líneas) entre dos apariciones de la palabra “Dulcinea”?

```scala
// Obtengo los índices de las líneas donde aparece "Dulcinea"
val indicesD = quijoteRDD.zipWithIndex().filter{case (l,_) => l.toLowerCase.contains("dulcinea")}.map(_._2).collect().sorted
// Calculo la distancia entre apariciones consecutivas
val distanciasD = indicesD.sliding(2).map{case Array(a,b) => b-a}.toArray
// Calculo la media de las distancias
val mediaD = if (distanciasD.nonEmpty) distanciasD.sum.toDouble/distanciasD.length else 0.0
println(f"Distancia media 'Dulcinea': $mediaD%.2f líneas")
```

Obtengo los índices de las líneas donde aparece “Dulcinea” y calculo la media de las distancias entre ellas.

![image.png](attachment:dcc1addc-c3d3-43d2-bb01-52e25194c62a:image.png)

**Conclusión:**
- Tuve problemas de rendimiento al usar collect() en un texto tan grande, ya que puede consumir mucha memoria y la primera vez bloqueó la terminal spark directamente porque tenía una instalación en paralelo. Para textos extensos, sería mejor usar un enfoque distribuido o limitar el número de resultados.

## PARTE 2: Análisis de Crimen y Castigo

En esta parte repito el proceso anterior, pero con el libro “Crimen y Castigo”. Primero descargo el texto, lo renombro y lo subo a HDFS, para ser resuelto usando spark.

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
val stopwords = Set(
    "the","and","to","of","a","in","that","is","it","for","on","with","as","was","at","by","an","be","this","which","or","from", 
    "they", "them", "their", "what", "have", "there", "your", "been", "would", "will", "about", "know", "said", "could", "come", 
    "some", "very", "more", "then", "were", "when", "upon", "into", "even"
)
// Extraigo palabras de más de 3 letras que no sean stopwords
// Cuento las repeticiones y saco el top 10
val resultadosTop10 = crimenRDD.flatMap(_.split("\\W+")).filter(w => w.length > 3 && !stopwords.contains(w.toLowerCase)).map(w => (w.toLowerCase, 1)).reduceByKey(_+_).sortBy(-_._2).take(10)

println("Top 10 palabras en Crimen y Castigo:")
resultadosTop10.foreach{ case (w, c) => println(s" - $w: $c") }
```

Aquí filtro palabras de más de 3 letras y elimino stopwords, luego saco el top 10.

![image.png](attachment:2aaa0352-2761-4e32-82cd-19cad4c11d04:image.png)

**Conclusión:**
Este Top 10 puede incluir palabras que no son relevantes literariamente (como "were", "your", etc.) si el set de stopwords no es suficientemente amplio. Por eso sencillamente amplié la lista de stopwords.

### Top 5 palabras más comunes que terminan en “ed”

```scala
// Extraigo palabras que terminan en "ed"
val palabrasEd = crimenRDD.flatMap(_.split("\\W+")).filter(_.toLowerCase.endsWith("ed"))
// Cuento las repeticiones y saco el top 5
val top5ed = palabrasEd.map((_,1)).reduceByKey(_+_).sortBy(-_._2).take(5)
top5ed.foreach{case (w,c) => println(s"$w:$c")}
```

Filtro palabras que terminan en “ed” y saco las 5 más frecuentes.

![image.png](attachment:9e98d265-6b81-4c10-8c63-0c56e90f350b:image.png)

**Conclusión:**
- Sin problemas. El código es eficiente y el resultado ayuda a ver la abundancia de verbos en pasado en la novela.

### ¿Cuántas exclamaciones hay en el libro? (líneas que terminan con “!”)

```scala
// Cuento las líneas que terminan con el carácter de exclamación
val exclamaciones = crimenRDD.filter(_.trim.endsWith("!")).count()
println(s"Líneas que terminan con '!':$exclamaciones")
```

Simplemente cuento las líneas que terminan con exclamación.

![image.png](attachment:2ebe1692-1ff3-4864-a74a-4508d0eb6d21:image.png)

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
conteos.foreach{case (w,c) => println(s"$w:$c")}
```

Elijo palabras relacionadas con números y cuento cuántas veces aparece cada una.

![image.png](attachment:b3dd4905-b241-4d4a-909b-85f173c703a7:image.png)

**Conclusión:**
- Al principio olvidé pasar todas las palabras a minúsculas, por lo que no contaba bien las apariciones. Tras corregirlo, el resultado fue correcto.

### ¿Cuántas frases de diálogo hay y cuál es la más larga? (frases entre comillas “)

```scala
// Cargamos el RDD con índices para saber el número de línea
val conIndice = sc.textFile("hdfs://localhost:9000/ebooks/CrimenyCastigo.txt").zipWithIndex()

// Identificamos las líneas de corte de Project Gutenberg
val inicio = conIndice.filter(_._1.contains("*** START")).map(_._2).first()
val fin = conIndice.filter(_._1.contains("*** END")).map(_._2).first()

// RDD PUro (solo el contenido del libro)
val crimenLibro = conIndice.filter{ case (_, idx) => idx > inicio && idx < fin }.map(_._1)

// ahora sí, extraemos diálogos del libro real
val dialogosRDD = crimenLibro.flatMap(_.split("\"")).zipWithIndex.filter(_._2 % 2 == 1).map(_._1).filter(_.length > 10)
val masLargaD = dialogosRDD.map(s => (s.length, s)).sortBy(-_._1).first()

println(s"Frases de diálogo reales: ${dialogosRDD.count()}")
println(s"Diálogo más largo real: ${masLargaD._2.trim}")
```

Divido el texto por comillas, cuento los fragmentos impares (diálogos) y busco el más largo.

![image.png](attachment:8147f4b4-1e99-4495-af52-133a43de548c:image.png)

**Conclusión:**
Al principio, el conteo de diálogos y la frase más larga me daban resultados que no tenían nada que ver con la literatura. Me salían frases sobre impuestos y licencias legales de Project Gutenberg. El problema es que el código hacía lo que yo le pedía (buscar texto entre comillas), pero no distinguía entre un diálogo de Raskolnikov y el contrato legal que viene al final del archivo.

Para solucionarlo, primero intenté filtrar por palabras clave como Gutenberg y poner una longitud mínima, pero el ruido seguía ahí porque el texto legal es enorme y tiene de todo. Al final, la solución de verdad fue cortar el libro por donde empieza y termina. Usé zipwithindex para identificar las líneas de "START" y "END" y creé un RDD con el contenido "puro".