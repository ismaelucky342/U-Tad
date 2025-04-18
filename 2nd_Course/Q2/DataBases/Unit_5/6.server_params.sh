#!/bin/bash

# Modificar max_connections y otros parámetros en my.cnf
echo "[mysqld]" >> /etc/mysql/mysql.conf.d/mysqld.cnf
echo "max_connections = 200" >> /etc/mysql/mysql.conf.d/mysqld.cnf
echo "query_cache_size = 16M" >> /etc/mysql/mysql.conf.d/mysqld.cnf
echo "sort_buffer_size = 4M" >> /etc/mysql/mysql.conf.d/mysqld.cnf

# Reiniciar el servicio de MySQL para aplicar los cambios
systemctl restart mysql
