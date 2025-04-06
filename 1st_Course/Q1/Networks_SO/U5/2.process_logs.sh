#!/bin/bash

# Archivo de log para almacenar los resultados
log_file="/var/log/procesos_memoria.log"
cpu_limit=80  # Límite de uso de CPU para generar alerta
mem_limit=75  # Límite de uso de memoria para generar alerta

# Función para obtener estadísticas del sistema
log_system_stats() {
    echo "Obteniendo estadísticas del sistema..."
    echo "Fecha: $(date)" >> $log_file
    echo "----------------------------" >> $log_file
    echo "Uso de memoria:" >> $log_file
    free -h >> $log_file
    echo "Uso de Swap:" >> $log_file
    swapon --show >> $log_file
    echo "----------------------------" >> $log_file
    echo "Uso de CPU:" >> $log_file
    top -bn1 | grep "Cpu(s)" >> $log_file
    echo "----------------------------" >> $log_file
    echo "Procesos más intensivos en CPU:" >> $log_file
    ps aux --sort=-%cpu | head -n 10 >> $log_file
    echo "----------------------------" >> $log_file
    echo "Procesos más intensivos en Memoria:" >> $log_file
    ps aux --sort=-%mem | head -n 10 >> $log_file
    echo "----------------------------" >> $log_file
}

# Función para generar una alerta si el uso de CPU o Memoria es alto
generate_alert() {
    echo "Generando alerta si el uso es alto..."
    # Verificar uso de CPU
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    if (( $(echo "$cpu_usage > $cpu_limit" | bc -l) )); then
        echo "ALERTA: Uso de CPU alto ($cpu_usage%)" | mail -s "Alerta de CPU Alta" admin@dominio.com
    fi

    # Verificar uso de memoria
    mem_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
    if (( $(echo "$mem_usage > $mem_limit" | bc -l) )); then
        echo "ALERTA: Uso de memoria alto ($mem_usage%)" | mail -s "Alerta de Memoria Alta" admin@dominio.com
    fi
}

# Función para matar un proceso que esté utilizando demasiada CPU o memoria
kill_high_usage_process() {
    echo "Matando procesos con uso alto de recursos..."
    # Encontrar y matar procesos que estén usando más CPU o memoria
    high_cpu_pid=$(ps aux --sort=-%cpu | head -n 2 | tail -n 1 | awk '{print $2}')
    high_mem_pid=$(ps aux --sort=-%mem | head -n 2 | tail -n 1 | awk '{print $2}')
    echo "Matando proceso de alto uso de CPU (PID: $high_cpu_pid)..."
    kill -9 $high_cpu_pid
    echo "Matando proceso de alto uso de memoria (PID: $high_mem_pid)..."
    kill -9 $high_mem_pid
}

# Función principal que ejecuta el monitoreo y registro
monitor_and_log() {
    while true; do
        log_system_stats
        generate_alert
        kill_high_usage_process
        sleep 300  # Espera de 5 minutos antes de realizar el siguiente chequeo
    done
}

# Ejecutar la función de monitoreo
monitor_and_log
