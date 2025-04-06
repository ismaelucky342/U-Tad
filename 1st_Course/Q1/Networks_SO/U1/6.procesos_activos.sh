#!/bin/bash

# Mostrar los procesos activos
ps aux
# Mostrar el uso de CPU y memoria
echo "Uso de CPU y memoria:"
ps aux --sort=-%mem | awk 'NR<=10{print $1, $2, $3, $4, $11}'
# Mostrar el uso de disco
echo "Uso de disco:"
df -h
# Mostrar el uso de red
echo "Uso de red:"
if command -v ifstat &>/dev/null; then
    ifstat -t
else
    echo "'ifstat' no está instalado. Intenta con 'nload' en su lugar."
    nload
fi
