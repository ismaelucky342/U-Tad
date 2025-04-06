#!/bin/bash

# Función para mostrar el menú de opciones
show_menu() {
    echo "------------------------------"
    echo "Editor de texto con Bash - Menú"
    echo "------------------------------"
    echo "1. Buscar y reemplazar texto en archivos"
    echo "2. Salir"
    echo "------------------------------"
    echo "Elige una opción:"
}

# Función para buscar y reemplazar texto en todos los archivos .txt dentro de un directorio
search_and_replace() {
    echo "Introduce la ruta del directorio donde buscar (por defecto es el directorio actual):"
    read directory
    directory=${directory:-$(pwd)}

    echo "Introduce el texto que quieres buscar:"
    read search_text

    echo "Introduce el texto con el que deseas reemplazar:"
    read replace_text

    echo "¿Deseas realizar una vista previa de los cambios? (y/n)"
    read preview

    if [ "$preview" == "y" ]; then
        echo "Vista previa de los cambios:"
        grep -r "$search_text" "$directory"/*.txt
    fi

    echo "¿Deseas aplicar los cambios? (y/n)"
    read apply_changes

    if [ "$apply_changes" == "y" ]; then
        # Realizar el reemplazo con sed en todos los archivos .txt
        find "$directory" -type f -name "*.txt" | while read file; do
            echo "Reemplazando en: $file"
            sed -i "s/$search_text/$replace_text/g" "$file"
        done
        echo "Reemplazo completado."
    else
        echo "No se realizaron cambios."
    fi
}

# Ciclo principal para el menú
while true; do
    show_menu
    read option
    case $option in
        1) search_and_replace ;;
        2) echo "Saliendo del script."; exit 0 ;;
        *) echo "Opción inválida, por favor elige una opción válida." ;;
    esac
done
