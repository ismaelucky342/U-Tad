#!/bin/bash

echo "Mostrando servidores DNS configurados..."
# Comando para mostrar servidores DNS
nmcli dev show | grep DNS
if [ $? -eq 0 ]; then
    echo "Los servidores DNS fueron mostrados exitosamente."
else
    echo "Error al mostrar los servidores DNS."
fi
