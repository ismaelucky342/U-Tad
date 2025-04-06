#!/bin/bash

# Verifica si el comando 'netstat' está disponible
if command -v netstat &>/dev/null; then
    echo "Conexiones de red activas:"
    netstat -tuln
else
    echo "'netstat' no está instalado. Intenta con 'ss' en su lugar."
    ss -tuln
fi
