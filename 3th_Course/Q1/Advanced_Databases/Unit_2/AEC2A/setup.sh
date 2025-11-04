#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC2 - ABDS                                       ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        23/10/2025  -  23:00:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    03/11/2025  -  02:55:40           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================#

#!/bin/bash

echo "============================================"
echo "Importando datos de restaurantes..."
echo "============================================"

# hay que añdir--drop para evitar duplicados al ejecutar otra vez
mongoimport --db restaurantesNY --collection restaurants --file restaurants.json --drop

echo "============================================"
echo "Datos importados exitosamente"
echo "Total de documentos:"
mongosh restaurantesNY --eval "db.restaurants.countDocuments()"
echo "============================================"

echo "Creando índices..."
mongosh restaurantesNY --eval "db.restaurants.createIndex({ borough: 1 })"
mongosh restaurantesNY --eval "db.restaurants.createIndex({ cuisine: 1 })"
mongosh restaurantesNY --eval "db.restaurants.createIndex({ 'grades.grade': 1 })"
mongosh restaurantesNY --eval "db.restaurants.createIndex({ 'address.zipcode': 1 })"

echo "¡DEBGU: todo OK!"
