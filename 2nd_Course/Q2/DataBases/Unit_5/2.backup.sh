#!/bin/bash

# Realizar una copia de seguridad de una base de datos
# Copiar la base de datos 'test_db' a un archivo de volcado
mysqldump -u root -p --databases test_db > /path/to/backup/test_db_backup.sql

# Restaurar la base de datos desde el archivo de volcado
mysql -u root -p < /path/to/backup/test_db_backup.sql
