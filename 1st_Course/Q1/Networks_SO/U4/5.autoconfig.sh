#!/bin/bash

# Solicitar la interfaz de red
echo "Ingrese la interfaz de red (por ejemplo, eth0 o enp3s0):"
read INTERFACE

# Solicitar la dirección IP estática
echo "Ingrese la dirección IP estática (por ejemplo, 192.168.1.100):"
read STATIC_IP

# Solicitar la máscara de subred
echo "Ingrese la máscara de subred (por ejemplo, 255.255.255.0):"
read SUBNET_MASK

# Solicitar la puerta de enlace predeterminada
echo "Ingrese la puerta de enlace predeterminada (por ejemplo, 192.168.1.1):"
read GATEWAY

# Establecer la IP estática
echo "Configurando la IP estática..."
sudo ip addr add $STATIC_IP/$SUBNET_MASK dev $INTERFACE

# Activar la interfaz de red
echo "Activando la interfaz de red..."
sudo ip link set $INTERFACE up

# Configurar la puerta de enlace predeterminada
echo "Configurando la puerta de enlace predeterminada..."
sudo ip route add default via $GATEWAY

# Verificar la configuración de red
echo "Verificando la configuración de red..."
ip addr show $INTERFACE
ip route show
