# Comandos para descargar y preparar los libros para Spark

# Descargar El Quijote (español)
wget http://www.gutenberg.org/cache/epub/2000/pg2000.txt -O quijote.txt

# Descargar Crimen y Castigo (inglés)
wget https://www.gutenberg.org/cache/epub/2554/pg2554.txt -O CrimenyCastigo.txt

# Subir ambos a HDFS (si usas HDFS)
hdfs dfs -mkdir -p /ebooks
hdfs dfs -put -f quijote.txt /ebooks/quijote.txt
hdfs dfs -put -f CrimenyCastigo.txt /ebooks/CrimenyCastigo.txt

# Si solo quieres trabajar en local, no necesitas los comandos de HDFS.
