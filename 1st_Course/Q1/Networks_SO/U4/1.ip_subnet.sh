#!/bin/bash

echo "Verificando dirección IP y máscara de subred..."
# Comando para obtener dirección IP
ip addr show | grep inet
