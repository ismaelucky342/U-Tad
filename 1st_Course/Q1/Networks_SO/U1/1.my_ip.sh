#!/bin/bash

# Verifica si el comando 'ifconfig' está disponible
if command -v ifconfig &>/dev/null; then
    echo "Dirección IP usando ifconfig:"
    ifconfig | grep inet | grep -v inet6 | awk '{print $2}'
# Si no está disponible, usa el comando 'ip'
elif command -v ip &>/dev/null; then
    echo "Dirección IP usando ip:"
    ip a | grep inet | grep -v inet6 | awk '{print $2}'
else
    echo "Ninguno de los comandos necesarios está instalado."
fi
