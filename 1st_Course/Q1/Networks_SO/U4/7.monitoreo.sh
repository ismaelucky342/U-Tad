#!/bin/bash

# Dirección del servidor a monitorear
SERVER="192.168.1.1"
EMAIL="admin@dominio.com"

# Número de pings
PING_COUNT=4

# Ejecutar el ping
ping -c $PING_COUNT $SERVER > /dev/null

# Verificar si el ping fue exitoso
if [ $? -eq 0 ]; then
    echo "El servidor $SERVER está disponible."
else
    # Enviar correo si el servidor no responde
    echo "El servidor $SERVER no responde. Enviando correo..." | mail -s "Alerta: Servidor $SERVER no disponible" $EMAIL
fi
