#!/bin/bash

# Comprobar si el script se ejecuta como root
if [ "$(id -u)" -ne 0 ]; then
  echo "Este script debe ejecutarse como root."
  exit 1
fi

# Solicitar el archivo o directorio
read -p "Introduce el archivo o directorio para verificar permisos: " filepath

# Comprobar si el archivo o directorio existe
if [ ! -e "$filepath" ]; then
  echo "El archivo o directorio '$filepath' no existe."
  exit 1
fi

# Mostrar los permisos actuales
echo "Permisos actuales:"
ls -l "$filepath"

# Preguntar si desea cambiar los permisos
read -p "¿Deseas cambiar los permisos? (s/n): " change_permissions
if [ "$change_permissions" == "s" ]; then
  # Solicitar nuevos permisos
  read -p "Introduce los nuevos permisos (por ejemplo, 755): " permissions
  chmod "$permissions" "$filepath"
  echo "Permisos cambiados a:"
  ls -l "$filepath"
else
  echo "No se han realizado cambios en los permisos."
fi
echo "Verificación de permisos completada."