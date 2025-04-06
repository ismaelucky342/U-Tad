#!/bin/bash

# Comprobar si el script se ejecuta como root
if [ "$(id -u)" -ne 0 ]; then
  echo "Este script debe ejecutarse como root."
  exit 1
fi

# Solicitar el nombre del usuario a eliminar
read -p "Introduce el nombre del usuario a eliminar: " username

# Eliminar al usuario y su directorio personal
userdel -r "$username"

# Comprobar si la eliminación fue exitosa
if [ $? -eq 0 ]; then
  echo "El usuario '$username' y su directorio personal han sido eliminados."
else
  echo "Error al eliminar el usuario."
  exit 1
fi

if id "$username" &>/dev/null; then
  echo "El usuario '$username' todavía existe."
else
  echo "El usuario '$username' ha sido eliminado correctamente."
fi
