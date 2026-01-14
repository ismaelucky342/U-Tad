#!/bin/bash

# Script para crear paquetes ZIP de funciones Lambda
# Mini Twitter - AWS Practice

echo "======================================"
echo "Mini Twitter - Lambda Package Builder"
echo "======================================"
echo ""

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Directorio base
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAMBDA_DIR="$BASE_DIR/lambda"
OUTPUT_DIR="$BASE_DIR/lambda-packages"

# Crear directorio de salida
mkdir -p "$OUTPUT_DIR"

echo -e "${YELLOW}Directorio base:${NC} $BASE_DIR"
echo -e "${YELLOW}Directorio de salida:${NC} $OUTPUT_DIR"
echo ""

# Funciones Lambda a procesar
FUNCTIONS=("twitterPost" "twitterRead" "userLogin" "userRegister" "searchByUser")

# Función para crear paquete
create_package() {
    local func_name=$1
    local func_dir="$LAMBDA_DIR/$func_name"
    
    echo -e "${YELLOW}Procesando:${NC} $func_name"
    
    # Verificar que existe el directorio
    if [ ! -d "$func_dir" ]; then
        echo -e "${RED}✗ Error: No se encuentra el directorio $func_dir${NC}"
        return 1
    fi
    
    # Ir al directorio de la función
    cd "$func_dir"
    
    # Instalar dependencias
    echo "  → Instalando dependencias..."
    npm install --production > /dev/null 2>&1
    
    if [ $? -ne 0 ]; then
        echo -e "${RED}  ✗ Error al instalar dependencias${NC}"
        cd "$BASE_DIR"
        return 1
    fi
    
    # Crear ZIP
    echo "  → Creando archivo ZIP..."
    zip -r "$OUTPUT_DIR/${func_name}.zip" . -x "*.git*" -x "README.md" > /dev/null 2>&1
    
    if [ $? -eq 0 ]; then
        # Obtener tamaño del archivo
        size=$(ls -lh "$OUTPUT_DIR/${func_name}.zip" | awk '{print $5}')
        echo -e "${GREEN}  ✓ Paquete creado: ${func_name}.zip ($size)${NC}"
    else
        echo -e "${RED}  ✗ Error al crear ZIP${NC}"
        cd "$BASE_DIR"
        return 1
    fi
    
    # Volver al directorio base
    cd "$BASE_DIR"
    echo ""
}

# Procesar todas las funciones
echo "Iniciando creación de paquetes..."
echo ""

success_count=0
fail_count=0

for func in "${FUNCTIONS[@]}"; do
    if create_package "$func"; then
        ((success_count++))
    else
        ((fail_count++))
    fi
done

# Resumen
echo "======================================"
echo "Resumen:"
echo -e "${GREEN}✓ Exitosos: $success_count${NC}"
if [ $fail_count -gt 0 ]; then
    echo -e "${RED}✗ Fallidos: $fail_count${NC}"
fi
echo ""
echo "Paquetes guardados en: $OUTPUT_DIR"
echo ""

# Listar archivos creados
if [ $success_count -gt 0 ]; then
    echo "Archivos creados:"
    ls -lh "$OUTPUT_DIR"/*.zip 2>/dev/null | awk '{print "  - " $9 " (" $5 ")"}'
    echo ""
    echo -e "${YELLOW}Siguiente paso:${NC}"
    echo "1. Ve a AWS Lambda Console"
    echo "2. Para cada función, sube su archivo .zip correspondiente"
    echo "3. Configura las variables de entorno según aws_config.md"
fi

echo ""
echo "======================================"
