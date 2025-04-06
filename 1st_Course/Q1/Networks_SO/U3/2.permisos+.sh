#!/bin/bash

# Comprobar si el script se ejecuta como root
if [ "$(id -u)" -ne 0 ]; then
  echo "Este script debe ejecutarse como root."
  exit 1
fi

# Solicitar el archivo o directorio
read -p "Introduce el archivo o directorio para modificar permisos: " filepath

# Comprobar si el archivo o directorio existe
if [ ! -e "$filepath" ]; then
  echo "El archivo o directorio '$filepath' no existe."
  exit 1
fi

# Solicitar los nuevos permisos (en formato octal)
read -p "Introduce los nuevos permisos (por ejemplo, 755): " permissions

# Modificar los permisos
chmod "$permissions" "$filepath"

# Verificar los nuevos permisos
ls -l "$filepath"
echo "Permisos de '$filepath' modificados a $permissions."
