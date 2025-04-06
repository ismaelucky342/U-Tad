#!/bin/bash

# Definir el nombre del archivo a buscar
archivo="archivo_origen.txt"

# 1. Buscar el archivo en el sistema
echo "Buscando '$archivo' en el sistema..."
find / -name $archivo 2>/dev/null

# Si se encuentra el archivo, se mostrará la ruta completa.
