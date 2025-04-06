#!/bin/bash

# Función para mostrar el menú de opciones
show_menu() {
    echo "-----------------------------------------"
    echo "Gestor Avanzado de Archivos de Texto - Menú"
    echo "-----------------------------------------"
    echo "1. Buscar y reemplazar texto en archivos"
    echo "2. Contar palabras, líneas y caracteres en archivos"
    echo "3. Buscar archivos que contienen una palabra"
    echo "4. Crear un nuevo archivo de texto"
    echo "5. Editar archivo con nano"
    echo "6. Eliminar archivo de texto"
    echo "7. Realizar copias de seguridad"
    echo "8. Salir"
    echo "-----------------------------------------"
    echo "Elige una opción:"
}

# Función para buscar y reemplazar texto en múltiples archivos
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

# Función para contar palabras, líneas y caracteres de archivos
count_words_lines_chars() {
    echo "Introduce la ruta del directorio donde buscar (por defecto es el directorio actual):"
    read directory
    directory=${directory:-$(pwd)}

    echo "Contando palabras, líneas y caracteres en archivos .txt en el directorio: $directory"
    echo "--------------------------------------------------"
    
    # Contar palabras, líneas y caracteres
    for file in "$directory"/*.txt; do
        if [ -f "$file" ]; then
            echo "Archivo: $file"
            wc "$file"  # Muestra el conteo de líneas, palabras y caracteres
            echo "--------------------------------------------------"
        fi
    done
}

# Función para buscar archivos que contienen una palabra específica
search_files_with_word() {
    echo "Introduce la palabra que deseas buscar en los archivos:"
    read word

    echo "Introduce la ruta del directorio donde buscar (por defecto es el directorio actual):"
    read directory
    directory=${directory:-$(pwd)}

    echo "Buscando archivos que contienen la palabra '$word'..."
    grep -r -l "$word" "$directory"/*.txt
}

# Función para crear un nuevo archivo de texto
create_new_file() {
    echo "Introduce el nombre del nuevo archivo de texto (con extensión .txt):"
    read file_name

    if [ -f "$file_name" ]; then
        echo "El archivo '$file_name' ya existe. ¿Quieres sobrescribirlo? (y/n)"
        read overwrite
        if [ "$overwrite" != "y" ]; then
            echo "Cancelado. El archivo no se ha creado."
            return
        fi
    fi

    touch "$file_name"
    echo "Archivo '$file_name' creado."
    echo "Ahora puedes editarlo con un editor de tu elección (nano, vim, etc.)."
}

# Función para editar archivo con nano
edit_with_nano() {
    echo "Introduce el nombre del archivo para editar con nano:"
    read file
    if [ ! -f "$file" ]; then
        echo "El archivo no existe. Creando un nuevo archivo: $file"
        touch "$file"
    fi
    nano "$file"
}

# Función para eliminar archivo de texto
delete_file() {
    echo "Introduce el nombre del archivo que deseas eliminar:"
    read file

    if [ ! -f "$file" ]; then
        echo "El archivo '$file' no existe."
        return
    fi

    echo "¿Estás seguro de que deseas eliminar '$file'? (y/n)"
    read confirm_delete

    if [ "$confirm_delete" == "y" ]; then
        rm "$file"
        echo "El archivo '$file' ha sido eliminado."
    else
        echo "El archivo no ha sido eliminado."
    fi
}

# Función para realizar copias de seguridad de todos los archivos .txt
backup_files() {
    echo "Introduce la ruta del directorio donde buscar los archivos para realizar una copia de seguridad:"
    read directory
    directory=${directory:-$(pwd)}

    echo "Creando copias de seguridad de los archivos .txt en el directorio '$directory'..."
    
    for file in "$directory"/*.txt; do
        if [ -f "$file" ]; then
            cp "$file" "$file.bak"
            echo "Copia de seguridad creada: $file.bak"
        fi
    done
    echo "Copia de seguridad completada."
}

# Ciclo principal para el menú
while true; do
    show_menu
    read option
    case $option in
        1) search_and_replace ;;
        2) count_words_lines_chars ;;
        3) search_files_with_word ;;
        4) create_new_file ;;
        5) edit_with_nano ;;
        6) delete_file ;;
        7) backup_files ;;
        8) echo "Saliendo del script."; exit 0 ;;
        *) echo "Opción inválida, por favor elige una opción válida." ;;
    esac
done
