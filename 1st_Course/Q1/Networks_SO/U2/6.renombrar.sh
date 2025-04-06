#!/bin/bash

# Definir nombres de archivo
archivo_original="archivo_origen.txt"
archivo_renombrado="archivo_renombrado.txt"

# 1. Crear un archivo de prueba
echo "Este archivo será renombrado" > $archivo_original

# 2. Renombrar el archivo
mv $archivo_original $archivo_renombrado
echo "Archivo renombrado a '$archivo_renombrado'"

# 3. Verificar el cambio
ls -l $archivo_renombrado
