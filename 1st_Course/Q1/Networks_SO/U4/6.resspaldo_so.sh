#!/bin/bash

# Directorio de respaldo
BACKUP_DIR="/backups"
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="backup_$DATE.tar.gz"

# Directorios a excluir
EXCLUDE_DIRS=("/dev" "/proc" "/sys" "/tmp" "/run" "/mnt")

# Crear el directorio de respaldo si no existe
mkdir -p $BACKUP_DIR

# Realizar el respaldo
echo "Iniciando el respaldo completo del sistema..."
tar --exclude=${EXCLUDE_DIRS[@]} -czf $BACKUP_DIR/$BACKUP_FILE / 

# Verificar si el respaldo se completó correctamente
if [ $? -eq 0 ]; then
    echo "Respaldo completado con éxito: $BACKUP_DIR/$BACKUP_FILE"
else
    echo "Error en el proceso de respaldo."
fi
