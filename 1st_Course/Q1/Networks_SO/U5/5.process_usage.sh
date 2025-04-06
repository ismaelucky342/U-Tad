#!/bin/bash

# Función para ver el uso de recursos
view_resources_usage() {
    echo "Uso actual de recursos:"
    echo "----------------------------"
    echo "Uso de CPU y memoria por procesos:"
    top -bn1 | head -n 20
    echo "----------------------------"
}

# Función para mostrar los 10 procesos que más CPU y memoria están utilizando
top_processes() {
    echo "Los 10 procesos que más CPU están utilizando:"
    ps aux --sort=-%cpu | head -n 10
    echo "----------------------------"
    echo "Los 10 procesos que más memoria están utilizando:"
    ps aux --sort=-%mem | head -n 10
    echo "----------------------------"
}

# Función para matar un proceso específico
kill_process() {
    echo "Introduce el PID del proceso que deseas terminar:"
    read process_pid
    if kill -9 $process_pid 2>/dev/null; then
        echo "Proceso $process_pid terminado exitosamente."
    else
        echo "No se pudo terminar el proceso $process_pid."
    fi
}

# Función para verificar el uso de la memoria
check_memory_usage() {
    total_mem=$(free | grep Mem | awk '{print $2}')
    free_mem=$(free | grep Mem | awk '{print $4}')
    used_mem=$((total_mem - free_mem))
    used_percent=$((used_mem * 100 / total_mem))
    
    echo "Uso total de memoria: $((total_mem / 1024)) MB"
    echo "Memoria utilizada: $((used_mem / 1024)) MB"
    echo "Memoria libre: $((free_mem / 1024)) MB"
    echo "Porcentaje de memoria utilizada: $used_percent%"
    
    if [ $used_percent -gt 80 ]; then
        echo "¡Alerta! El uso de memoria es alto. Liberando memoria..."
        sudo sync && sudo echo 3 > /proc/sys/vm/drop_caches
        echo "Memoria liberada."
    fi
}

# Menú interactivo para el usuario
menu() {
    echo "----------------------------"
    echo "1. Ver uso de recursos"
    echo "2. Ver los 10 procesos que más CPU o memoria usan"
    echo "3. Matar un proceso"
    echo "4. Verificar el uso de memoria"
    echo "5. Salir"
    echo "----------------------------"
    echo "Elige una opción:"
    read option
    case $option in
        1) view_resources_usage ;;
        2) top_processes ;;
        3) kill_process ;;
        4) check_memory_usage ;;
        5) exit 0 ;;
        *) echo "Opción inválida, por favor elige una opción válida." ;;
    esac
}

# Ejecución del menú en bucle
while true; do
    menu
done
