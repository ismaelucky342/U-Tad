#!/bin/bash

# Comprobar si el script se ejecuta como root
if [ "$(id -u)" -ne 0 ]; then
  echo "Este script debe ejecutarse como root."
  exit 1
fi

# Solicitar el nombre del usuario y grupo
read -p "Introduce el nombre del usuario: " username
read -p "Introduce el nombre del grupo: " groupname

# Verificar si el grupo existe
if ! grep -q "^$groupname:" /etc/group; then
  echo "El grupo '$groupname' no existe."
  exit 1
fi

# Añadir el usuario al grupo
usermod -aG "$groupname" "$username"

# Comprobar si el usuario fue añadido correctamente
if [ $? -eq 0 ]; then
  echo "El usuario '$username' ha sido añadido al grupo '$groupname'."
else
  echo "Error al añadir el usuario al grupo."
  exit 1
fi
