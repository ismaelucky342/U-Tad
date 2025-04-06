#!/bin/bash

# Función para mostrar el uso de la memoria
check_memory() {
    echo "Chequeando el uso de la memoria..."
    # Mostrar estadísticas de memoria
    free -h
    # Verificar el uso de la memoria swap
    echo "Uso de Swap:"
    swapon --show
}

# Función para encontrar los procesos que más memoria están usando
check_top_processes() {
    echo "Procesos que más memoria están usando:"
    ps aux --sort=-%mem | head -n 10
}

# Función para encontrar los procesos que más CPU están usando
check_cpu_processes() {
    echo "Procesos que más CPU están usando:"
    ps aux --sort=-%cpu | head -n 10
}

# Función para monitorear el uso de la memoria en tiempo real
monitor_memory() {
    while true; do
        # Comprobar el uso de la memoria
        total_memory=$(free | grep Mem | awk '{print $2}')
        free_memory=$(free | grep Mem | awk '{print $4}')
        used_memory=$((total_memory - free_memory))

        echo "Memoria total: $((total_memory / 1024)) MB"
        echo "Memoria usada: $((used_memory / 1024)) MB"
        echo "Memoria libre: $((free_memory / 1024)) MB"
        
        if [ $free_memory -lt 50000 ]; then  # Si hay menos de 50MB de memoria libre
            echo "¡Alerta! Memoria muy baja."
        fi

        sleep 5
    done
}

# Función para matar un proceso por nombre o PID
kill_process() {
    echo "Introduce el PID o nombre del proceso que deseas matar:"
    read process
    if [[ $process =~ ^[0-9]+$ ]]; then
        kill -9 $process
        echo "Proceso $process terminado."
    else
        pid=$(pgrep $process)
        if [ -z "$pid" ]; then
            echo "No se encontró el proceso $process."
        else
            kill -9 $pid
            echo "Proceso $process (PID: $pid) terminado."
        fi
    fi
}

# Menú para interactuar con el script
while true; do
    echo "----------------------------"
    echo "1. Chequear uso de memoria"
    echo "2. Ver procesos que más memoria usan"
    echo "3. Ver procesos que más CPU usan"
    echo "4. Monitorear memoria en tiempo real"
    echo "5. Matar un proceso"
    echo "6. Salir"
    echo "----------------------------"
    echo "Elige una opción:"
    read option
    case $option in
        1) check_memory ;;
        2) check_top_processes ;;
        3) check_cpu_processes ;;
        4) monitor_memory ;;
        5) kill_process ;;
        6) exit 0 ;;
        *) echo "Opción inválida, por favor elige una opción válida." ;;
    esac
done
