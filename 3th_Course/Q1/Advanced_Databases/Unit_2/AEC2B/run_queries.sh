#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC2 - ABDS                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        23/10/2025  -  23:00:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    04/11/2025  -  18:55:40           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================#

#!/bin/bash

DB_NAME="bookstores_db"
COLLECTION="bookstores"
JSON_FILE="bookstores.json"
QUERIES_FILE="queries.js"
OUTPUT_FILE="query_results.txt"

echo "========================================="
echo "MongoDB Bookstores - Ejecución Automática"
echo "========================================="
echo ""

if [ ! -f "$JSON_FILE" ]; then
    echo "Error: No se encuentra el archivo $JSON_FILE"
    exit 1
fi

echo "Archivo de datos encontrado: $JSON_FILE"

echo ""
echo "Importando datos a MongoDB..."
mongoimport --db "$DB_NAME" --collection "$COLLECTION" --file "$JSON_FILE" --jsonArray --drop

if [ $? -eq 0 ]; then
    echo "Datos importados correctamente"
else
    echo "Error al importar datos"
    exit 1
fi

echo ""
echo "Ejecutando consultas"
mongosh "$DB_NAME" < "$QUERIES_FILE" > "$OUTPUT_FILE" 2>&1

if [ $? -eq 0 ]; then
    echo "Consultas ejecutadas correctamente"
    echo "Resultados guardados en: $OUTPUT_FILE"
else
    echo "Error al ejecutar consultas"
    exit 1
fi


echo "DEBUG: FUnsiona"

