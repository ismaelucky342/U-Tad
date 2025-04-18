#!/bin/bash

# Crear un backup comprimido de la base de datos
mysqldump -u root -p test_db | gzip > /path/to/backup/test_db_backup.sql.gz

# Restaurar una base de datos desde un archivo comprimido
gunzip < /path/to/backup/test_db_backup.sql.gz | mysql -u root -p test_db
