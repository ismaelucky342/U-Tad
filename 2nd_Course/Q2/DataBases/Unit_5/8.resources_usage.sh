#!/bin/bash

# Verificar el uso de conexiones en MySQL
mysql -u root -p -e "SHOW STATUS LIKE 'Threads_connected';"

# Consultar las variables de configuración del servidor
mysql -u root -p -e "SHOW VARIABLES LIKE 'max_connections';"

# Ver el uso de recursos de CPU y memoria en el sistema
top -n 1
