#!/bin/bash

# Verificar que se pase exactamente un parámetro
if [ "$#" -ne 1 ]; then
    echo "Error: Sólo se admite un parámetro."
    exit 1
fi

# Convertir el parámetro a minúsculas para mayor flexibilidad
param=$(echo "$1" | tr '[:upper:]' '[:lower:]')

# Manejar las opciones
case "$param" in
    c|corta)
        date '+%d/%m/%Y'
        ;;
    l|larga)
        date '+Hoy es el día %d del mes %m del año %Y.'
        ;;
    *)
        echo "Error: Opción incorrecta."
        exit 2
        ;;
esac
