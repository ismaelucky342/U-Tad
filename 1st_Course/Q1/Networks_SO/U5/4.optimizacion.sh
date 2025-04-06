#!/bin/bash

# Umbral de uso de memoria
MEMORY_THRESHOLD=80

# Función para comprobar el uso de memoria
check_memory_usage() {
    echo "Comprobando el uso de memoria..."
    free -h
}

# Función para verificar si el uso de memoria supera el umbral
check_threshold() {
    used_memory_percentage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
    echo "Uso de memoria: $used_memory_percentage%"
    
    if (( $(echo "$used_memory_percentage > $MEMORY_THRESHOLD" | bc -l) )); then
        echo "El uso de memoria es alto. Liberando caché de memoria..."
        free_memory_cache
    else
        echo "El uso de memoria está dentro de los límites."
    fi
}

# Función para liberar caché de memoria
free_memory_cache() {
    echo "Liberando caché de memoria..."
    sudo sync && sudo echo 3 > /proc/sys/vm/drop_caches
    echo "Caché de memoria liberado."
}

# Función principal que ejecuta la verificación periódica de memoria
monitor_memory() {
    while true; do
        check_memory_usage
        check_threshold
        sleep 300  # Verifica cada 5 minutos
    done
}

# Ejecutar el monitoreo
monitor_memory
