#!/bin/bash

# Comprobar si el script se ejecuta como root
if [ "$(id -u)" -ne 0 ]; then
  echo "Este script debe ejecutarse como root."
  exit 1
fi

# Solicitar el nombre del usuario
read -p "Introduce el nombre del nuevo usuario: " username

# Solicitar el nombre del grupo
read -p "Introduce el nombre del grupo al que se asignará el usuario: " groupname

# Crear un nuevo usuario con su directorio personal
useradd -m -G "$groupname" "$username"

# Comprobar si la creación del usuario fue exitosa
if [ $? -eq 0 ]; then
  echo "Usuario '$username' creado y agregado al grupo '$groupname'."
else
  echo "Error al crear el usuario."
  exit 1
fi

# Establecer contraseña para el usuario
passwd "$username"

# Verificar el grupo al que pertenece el usuario
groups "$username"
