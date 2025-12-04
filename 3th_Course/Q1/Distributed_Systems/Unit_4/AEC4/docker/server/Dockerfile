# Dockerfile para serverFileManager
# Puerto: 32001
# Parámetros: IP del broker

FROM ubuntu:20.04

# Evitar interacción durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Actualizar e instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Crear directorio para archivos gestionados
RUN mkdir -p /app/FileManagerDir

# Copiar el ejecutable del servidor
# NOTA: Debes colocar el archivo serverFileManager en este directorio
COPY serverFileManager /app/

# Dar permisos de ejecución
RUN chmod +x /app/serverFileManager

# Exponer el puerto del servidor
EXPOSE 32001

# Variable de entorno para la IP del broker (se puede sobrescribir)
ENV BROKER_IP=""

# El comando se ejecutará con la IP del broker como parámetro
# Ejemplo: ./serverFileManager <broker_ip>
# Esto se configurará en el deployment de Kubernetes
ENTRYPOINT ["./serverFileManager"]
