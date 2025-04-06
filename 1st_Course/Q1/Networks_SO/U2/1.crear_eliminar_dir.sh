#!/bin/bash

# Definir el nombre del directorio
directorio="test_directory"

# 1. Crear el directorio
mkdir $directorio
echo "Directorio '$directorio' creado."

# 2. Verificar si el directorio fue creado
if [ -d "$directorio" ]; then
  echo "El directorio '$directorio' existe."
else
  echo "El directorio '$directorio' no existe."
fi

# 3. Eliminar el directorio
rmdir $directorio
echo "Directorio '$directorio' eliminado."
