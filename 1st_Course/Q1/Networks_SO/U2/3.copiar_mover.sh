#!/bin/bash

# Definir nombres de archivo y directorios
archivo_origen="archivo_origen.txt"
archivo_destino="archivo_destino.txt"
directorio_destino="/home/usuario/destino"

# 1. Crear un archivo de prueba
echo "Este es un archivo de prueba" > $archivo_origen

# 2. Copiar el archivo al directorio de destino
cp $archivo_origen $directorio_destino
echo "Archivo copiado a $directorio_destino"

# 3. Mover el archivo a otro lugar
mv $archivo_origen $directorio_destino
echo "Archivo movido a $directorio_destino"

# 4. Verificar que el archivo se movió correctamente
ls $directorio_destino
