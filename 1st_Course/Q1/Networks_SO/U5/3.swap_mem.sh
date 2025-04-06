#!/bin/bash

# Función para verificar el uso de swap
check_swap_usage() {
    swap_used=$(free | grep Swap | awk '{print $3}')
    swap_total=$(free | grep Swap | awk '{print $2}')
    swap_percentage=$((swap_used * 100 / swap_total))
    
    echo "Uso de Swap: $swap_percentage% ($swap_used de $swap_total KB)"
    
    if [ $swap_percentage -gt 50 ]; then
        echo "Alerta: El uso de swap es superior al 50%. Liberando swap..."
        free_swap
    fi
}

# Función para liberar el espacio de swap
free_swap() {
    echo "Desactivando el espacio de swap..."
    sudo swapoff -a
    echo "Reactivando swap..."
    sudo swapon -a
    echo "Swap liberado exitosamente."
}

# Ejecutar la verificación y liberación de swap cada 10 minutos
while true; do
    check_swap_usage
    sleep 600  # Verificar cada 10 minutos
done
