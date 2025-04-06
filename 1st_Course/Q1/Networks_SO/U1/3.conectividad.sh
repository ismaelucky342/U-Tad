#!/bin/bash

# Verifica si el usuario ha proporcionado una dirección IP o dominio
if [ -z "$1" ]; then
    echo "Por favor, proporciona una dirección IP o un dominio para verificar."
    exit 1
fi

# Realiza un ping a la dirección IP o dominio proporcionado
ping -c 4 "$1"
