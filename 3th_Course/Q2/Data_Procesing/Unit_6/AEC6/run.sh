#!/bin/bash

# Script para ejecutar los análisis de AEC6

echo "================================"
echo "Ejecutando AEC6 - Spark ML"
echo "================================"

cd "$(dirname "$0")" || exit

echo ""
echo "▶ Ejecutando Parte 1: Exploración..."
echo "================================"
spark-submit parte1_exploracion.py

echo ""
echo "▶ Ejecutando Parte 2: Modelos..."
echo "================================"
spark-submit parte2_modelos.py

echo ""
echo "✓ Ejecución completada"
