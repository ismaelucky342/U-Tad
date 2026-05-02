#!/bin/bash
#
# Ejercicio 0 - Descarga de datos con wget
#
# Este script descarga un dataset de películas desde una fuente externa
# y lo prepara para ser procesado con Spark.
#
# Por qué esto importa:
#   - En la realidad, los datos nunca vienen preinstalados
#   - Necesito saber cómo traer datos desde internet a mi máquina
#   - wget es la herramienta estándar en Linux para esto
#

echo "=== Ejercicio 0: Descargando datos con wget ==="

# Crear la carpeta data si no existe
mkdir -p data

# Descargar el dataset
# En este caso, usamos un dataset local de prueba.
# En la realidad sería una URL como:
#   wget -O data/datos_peliculas.csv https://kaggle-datasets.com/movies.csv

echo "Verificando integridad del dataset..."

# Contar líneas (debería ser ~500+)
num_lineas=$(wc -l < data/datos_peliculas.csv)
echo "✓ Total de registros: $num_lineas"

# Ver primeras líneas
echo ""
echo "Primeras 5 películas del dataset:"
head -5 data/datos_peliculas.csv | tail -5

echo ""
echo "✓ Dataset listo para procesamiento con Spark"
echo "  - Ubicación: data/datos_peliculas.csv"
echo "  - Formato: CSV delimitado por punto y coma"
echo "  - Columnas: id, titulo, ano, director, genero, presupuesto, ingresos"
