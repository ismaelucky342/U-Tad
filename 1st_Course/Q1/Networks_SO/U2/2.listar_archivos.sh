#!/bin/bash

# Definir el directorio
directorio="/home/usuario"

# 1. Listar los archivos en el directorio
echo "Archivos en el directorio '$directorio':"
ls -l $directorio

# 2. Verificar si los archivos son directorios o archivos comunes
echo -e "\nVerificando los tipos de archivos:"
for archivo in $directorio/*; do
  if [ -d "$archivo" ]; then
    echo "$archivo es un directorio"
  elif [ -f "$archivo" ]; then
    echo "$archivo es un archivo regular"
  else
    echo "$archivo es otro tipo de archivo"
  fi
done
