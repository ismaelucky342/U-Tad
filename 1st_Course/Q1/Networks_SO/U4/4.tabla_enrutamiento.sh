#!/bin/bash

echo "Mostrando la tabla de enrutamiento..."
# Comando para mostrar la tabla de enrutamiento
route -n
if [ $? -eq 0 ]; then
    echo "La tabla de enrutamiento fue mostrada exitosamente."
else
    echo "Error al mostrar la tabla de enrutamiento."
fi