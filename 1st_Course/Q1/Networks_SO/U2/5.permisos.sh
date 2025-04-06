#!/bin/bash

# Definir el archivo
archivo="archivo_origen.txt"

# 1. Crear un archivo de prueba
echo "Este archivo tendrá permisos modificados." > $archivo

# 2. Mostrar los permisos actuales del archivo
echo "Permisos actuales del archivo $archivo:"
ls -l $archivo

# 3. Cambiar los permisos del archivo
chmod 755 $archivo
echo "Permisos cambiados a 755."

# 4. Mostrar los permisos después de la modificación
echo "Permisos después de cambiar:"
ls -l $archivo
