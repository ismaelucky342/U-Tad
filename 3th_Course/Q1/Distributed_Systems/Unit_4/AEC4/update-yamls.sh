#!/bin/bash

# Script de actualización de archivos YAML con tu usuario de Docker Hub
# Uso: ./update-yamls.sh <docker-hub-username>

if [ -z "$1" ]; then
    echo "Error: Debes proporcionar tu usuario de Docker Hub"
    echo "Uso: ./update-yamls.sh <docker-hub-username>"
    exit 1
fi

DOCKER_USER=$1

echo "======================================"
echo "Actualizando archivos YAML"
echo "Usuario: $DOCKER_USER"
echo "======================================"

# Buscar y reemplazar en archivos YAML
find kubernetes/ -name "*.yaml" -type f -exec sed -i "s|<tu-usuario>|${DOCKER_USER}|g" {} +

echo ""
echo "✅ Archivos actualizados:"
grep -r "image:" kubernetes/ | grep "$DOCKER_USER"

echo ""
echo "======================================"
echo "✅ Proceso completado"
echo "======================================"
echo ""
echo "Ahora puedes desplegar con:"
echo "  kubectl apply -f kubernetes/broker/deployment.yaml"
echo "  kubectl apply -f kubernetes/server/deployment-basic.yaml"
