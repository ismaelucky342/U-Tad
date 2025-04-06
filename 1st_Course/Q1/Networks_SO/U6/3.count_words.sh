#!/bin/bash

# Función para contar palabras, líneas y caracteres de archivos .txt
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

# Ejecutar el conteo
count_words_lines_chars
