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

echo "Exportando los resultados..."

# Ejercicio 1
mongoexport --db=restaurantesNY --collection=restaurants \
  --query='{"grades.score": {"$gt": 80, "$lt": 100}}' \
  --out=ejercicio1_resultados.json \
  --jsonArray

# Ejercicio 6
mongoexport --db=restaurantesNY --collection=restaurants \
  --query='{"grades.grade": "A", "grades.grade": {"$nin": ["B", "C"]}}' \
  --out=ejercicio6_resultados.json \
  --jsonArray

# Ejercicio 13
mongoexport --db=restaurantesNY --collection=restaurants \
  --query='{"borough": {"$in": ["Manhattan", "Brooklyn"]}, "grades.score": {"$not": {"$lte": 5}}}' \
  --out=ejercicio13_resultados.json \
  --jsonArray

echo "DEBUG: Exportación OK. Archivos generados:"
echo "- ejercicio1_resultados.json"
echo "- ejercicio6_resultados.json"
echo "- ejercicio13_resultados.json"
