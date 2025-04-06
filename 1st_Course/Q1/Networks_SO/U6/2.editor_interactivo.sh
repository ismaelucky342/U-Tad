#!/bin/bash

# Función para mostrar el menú de opciones
show_menu() {
    echo "-------------------------------"
    echo "Editor de texto con Bash - Menú"
    echo "-------------------------------"
    echo "1. Editar archivo con nano"
    echo "2. Editar archivo con vim"
    echo "3. Salir"
    echo "-------------------------------"
    echo "Elige una opción:"
}

# Función para crear una copia de seguridad antes de editar
backup_file() {
    echo "Creando una copia de seguridad de $1..."
    cp "$1" "$1.bak"
    echo "Copia de seguridad guardada como $1.bak"
}

# Función para editar con nano
edit_with_nano() {
    echo "Introduce el nombre del archivo para editar con nano:"
    read file
    if [ ! -f "$file" ]; then
        echo "El archivo no existe. Creando un nuevo archivo: $file"
        touch "$file"
    fi
    backup_file "$file"
    nano "$file"
}

# Función para editar con vim
edit_with_vim() {
    echo "Introduce el nombre del archivo para editar con vim:"
    read file
    if [ ! -f "$file" ]; then
        echo "El archivo no existe. Creando un nuevo archivo: $file"
        touch "$file"
    fi
    backup_file "$file"
    vim "$file"
}

# Ciclo principal para el menú
while true; do
    show_menu
    read option
    case $option in
        1) edit_with_nano ;;
        2) edit_with_vim ;;
        3) echo "Saliendo del script."; exit 0 ;;
        *) echo "Opción inválida, por favor elige una opción válida." ;;
    esac
done
