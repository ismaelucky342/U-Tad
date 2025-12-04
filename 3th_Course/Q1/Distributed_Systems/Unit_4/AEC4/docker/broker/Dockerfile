# Dockerfile para brokerFileManager
# Puerto: 32002

FROM ubuntu:20.04

# Evitar interacción durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Actualizar e instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar el ejecutable del broker
# NOTA: Debes colocar el archivo brokerFileManager en este directorio
COPY brokerFileManager /app/

# Dar permisos de ejecución
RUN chmod +x /app/brokerFileManager

# Exponer el puerto del broker
EXPOSE 32002

# Comando para ejecutar el broker
CMD ["./brokerFileManager"]
