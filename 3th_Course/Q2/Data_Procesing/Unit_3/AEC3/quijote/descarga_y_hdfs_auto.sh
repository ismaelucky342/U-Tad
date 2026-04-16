#!/bin/bash
# Script para verificar e instalar Hadoop si es necesario, y cargar El Quijote en HDFS

# Verificar si el comando hdfs está disponible
echo "Verificando Hadoop (hdfs)..."
if ! command -v hdfs &> /dev/null; then
    echo "Hadoop no está instalado. Instalando Hadoop..."
    # Detectar sistema operativo
    if [ -f /etc/arch-release ]; then
        # Arch Linux
        sudo pacman -Sy --noconfirm hadoop
    elif [ -f /etc/debian_version ]; then
        # Debian/Ubuntu
        sudo apt-get update
        sudo apt-get install -y hadoop
    else
        echo "Distribución no soportada para instalación automática. Instala Hadoop manualmente."
        exit 1
    fi
else
    echo "Hadoop ya está instalado."
fi

# Descargar el texto si no existe
echo "Descargando El Quijote..."
if [ ! -f pg2000.txt ]; then
    wget http://www.gutenberg.org/cache/epub/2000/pg2000.txt
fi

# Crear directorio en HDFS si no existe
echo "Creando directorio en HDFS..."
hdfs dfs -mkdir -p /ebooks

# Subir el archivo a HDFS
echo "Subiendo el archivo a HDFS..."
hdfs dfs -put -f pg2000.txt /ebooks/quijote.txt

echo "Archivo cargado en HDFS en /ebooks/quijote.txt"
