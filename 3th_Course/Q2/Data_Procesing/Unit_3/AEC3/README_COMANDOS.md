# Guía rápida de comandos para la práctica

Este README resume todos los comandos necesarios para preparar, probar y ejecutar los análisis de El Quijote y Crimen y Castigo con Spark.

## 1. Descargar los libros

```bash
# Descargar El Quijote (español)
wget http://www.gutenberg.org/cache/epub/2000/pg2000.txt -O quijote.txt

# Descargar Crimen y Castigo (inglés)
wget https://www.gutenberg.org/cache/epub/2554/pg2554.txt -O CrimenyCastigo.txt
```

## 2. Subir los libros a HDFS (opcional)

```bash
hdfs dfs -mkdir -p /ebooks
hdfs dfs -put -f quijote.txt /ebooks/quijote.txt
hdfs dfs -put -f CrimenyCastigo.txt /ebooks/CrimenyCastigo.txt
```

## 3. Lanzar Spark Shell

```bash
spark-shell
```

## 4. Cargar y ejecutar el análisis completo

En el prompt de Spark, carga el script con:

```
:load ejecucion_spark.scala
```

Esto ejecutará todos los análisis de la práctica y mostrará la salida en la terminal.

## 5. Consejos
- Puedes ejecutar los bloques de código de forma individual copiando y pegando en spark-shell.
- Haz capturas de pantalla de la salida para documentar la memoria.
- Si no usas HDFS, puedes cargar los archivos locales con:

```scala
val quijoteRDD = sc.textFile("quijote.txt")
val crimenRDD = sc.textFile("CrimenyCastigo.txt")
```

---

Con estos pasos tendrás todo listo para probar y documentar tu práctica.
