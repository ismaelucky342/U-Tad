#!/bin/bash

echo "Introduzca una URL o dirección IP para hacer ping:"
read destination

# Comando para hacer ping
ping -c 4 $destination
if [ $? -eq 0 ]; then
    echo "El ping a $destination fue exitoso."
else
    echo "El ping a $destination falló."
fi
