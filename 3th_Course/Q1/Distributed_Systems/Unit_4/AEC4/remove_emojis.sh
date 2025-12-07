#!/bin/bash

# Script para eliminar todos los emojis de archivos .md y .sh

# Función para eliminar emojis de un archivo
remove_emojis() {
    local file="$1"
    # Crear backup
    cp "$file" "$file.bak"
    
    # Eliminar emojis comunes usando sed
    sed -i 's///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g' "$file"
    sed -i 's///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g' "$file"
    sed -i 's///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g' "$file"
    sed -i 's///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g' "$file"
    sed -i 's///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g' "$file"
    sed -i 's///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g; s///g' "$file"
    
    echo "Procesado: $file"
}

# Procesar todos los archivos .md
find . -name "*.md" -type f | while read -r file; do
    remove_emojis "$file"
done

# Procesar todos los archivos .sh
find . -name "*.sh" -type f | while read -r file; do
    remove_emojis "$file"
done

echo "Proceso completado. Los backups están en archivos .bak"
