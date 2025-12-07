#!/bin/bash

# Script de construcción de imágenes Docker
# Uso: ./build-images.sh <docker-hub-username>

if [ -z "$1" ]; then
    echo "Error: Debes proporcionar tu usuario de Docker Hub"
    echo "Uso: ./build-images.sh <docker-hub-username>"
    exit 1
fi

DOCKER_USER=$1
BROKER_IMAGE="${DOCKER_USER}/broker-filemanager:latest"
SERVER_IMAGE="${DOCKER_USER}/server-filemanager:latest"

echo "======================================"
echo "Construcción de Imágenes Docker"
echo "Usuario: $DOCKER_USER"
echo "======================================"

# Verificar que los ejecutables existan
echo ""
echo "Verificando archivos..."
if [ ! -f "docker/broker/brokerFileManager" ]; then
    echo "[ERROR] No se encuentra docker/broker/brokerFileManager"
    echo "Copia el ejecutable a docker/broker/"
    exit 1
fi

if [ ! -f "docker/server/serverFileManager" ]; then
    echo "[ERROR] No se encuentra docker/server/serverFileManager"
    echo "Copia el ejecutable a docker/server/"
    exit 1
fi

echo "[OK] Archivos encontrados"

# Construir imagen del broker
echo ""
echo "======================================"
echo "Construyendo imagen del Broker..."
echo "======================================"
cd docker/broker/ || exit
docker build -t "$BROKER_IMAGE" .
if [ $? -ne 0 ]; then
    echo "[ERROR] Error al construir imagen del broker"
    exit 1
fi
echo "[OK] Imagen del broker construida: $BROKER_IMAGE"
cd ../..

# Construir imagen del servidor
echo ""
echo "======================================"
echo "Construyendo imagen del Server..."
echo "======================================"
cd docker/server/ || exit
docker build -t "$SERVER_IMAGE" .
if [ $? -ne 0 ]; then
    echo "[ERROR] Error al construir imagen del servidor"
    exit 1
fi
echo "[OK] Imagen del servidor construida: $SERVER_IMAGE"
cd ../..

# Mostrar imágenes construidas
echo ""
echo "======================================"
echo "Imágenes Docker construidas:"
echo "======================================"
docker images | grep "$DOCKER_USER"

echo ""
echo "======================================"
echo "¿Deseas subir las imágenes a Docker Hub? (y/n)"
echo "======================================"
read -r PUSH_IMAGES

if [ "$PUSH_IMAGES" = "y" ] || [ "$PUSH_IMAGES" = "Y" ]; then
    echo ""
    echo "Iniciando sesión en Docker Hub..."
    docker login
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "Subiendo imagen del broker..."
        docker push "$BROKER_IMAGE"
        
        echo ""
        echo "Subiendo imagen del servidor..."
        docker push "$SERVER_IMAGE"
        
        echo ""
        echo "[OK] Imagenes subidas correctamente!"
        echo ""
        echo "Actualiza los archivos YAML con:"
        echo "  image: $BROKER_IMAGE"
        echo "  image: $SERVER_IMAGE"
    else
        echo "[ERROR] Error al iniciar sesion en Docker Hub"
        exit 1
    fi
else
    echo ""
    echo "Imágenes NO subidas a Docker Hub"
    echo "Recuerda subirlas antes de desplegar en Kubernetes:"
    echo "  docker push $BROKER_IMAGE"
    echo "  docker push $SERVER_IMAGE"
fi

echo ""
echo "======================================"
echo "[OK] Proceso completado"
echo "======================================"
