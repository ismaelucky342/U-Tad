#!/bin/bash

# Comprobar si el script se ejecuta como root
if [ "$(id -u)" -ne 0 ]; then
  echo "Este script debe ejecutarse como root."
  exit 1
fi

# Solicitar el archivo o directorio
read -p "Introduce el archivo o directorio para cambiar propietario y grupo: " filepath

# Comprobar si el archivo o directorio existe
if [ ! -e "$filepath" ]; then
  echo "El archivo o directorio '$filepath' no existe."
  exit 1
fi

# Solicitar el nuevo propietario y grupo
read -p "Introduce el nuevo propietario: " new_owner
read -p "Introduce el nuevo grupo: " new_group

# Cambiar el propietario y grupo
chown "$new_owner":"$new_group" "$filepath"

# Verificar el cambio
ls -l "$filepath"
echo "Propietario y grupo de '$filepath' cambiados a '$new_owner' y '$new_group'."