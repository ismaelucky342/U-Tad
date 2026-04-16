#!/bin/bash
# Script para descargar El Quijote y cargarlo en HDFS

# Descargar el texto si no existe
echo "Descargando El Quijote..."
if [ ! -f pg2000.txt ]; then
    wget http://www.gutenberg.org/cache/epub/2000/pg2000.txt
fi

# Crear directorio en HDFS si no existe
echo "Creando directorio en HDFS..."
hdfs dfs -mkdir -p /ebooks

# Subir el archivo a HDFS
echo "Subiendo el archivo a HDFS..."
hdfs dfs -put -f pg2000.txt /ebooks/quijote.txt

echo "Archivo cargado en HDFS en /ebooks/quijote.txt"
