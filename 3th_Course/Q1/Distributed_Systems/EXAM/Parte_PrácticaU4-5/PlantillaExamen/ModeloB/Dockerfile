# Dockerfile para sensorServer
FROM ubuntu:24.04

# Instalar dependencias básicas si fueran necesarias
RUN apt-get update && apt-get install -y \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio donde se montará el volumen
RUN mkdir -p /sensorData

# Copiar el ejecutable del servidor (solo si construyes tu propia imagen)
COPY sensorServer /usr/local/bin/sensorServer
RUN chmod +x /usr/local/bin/sensorServer

# Declarar el volumen (opcional, ayuda a documentar)
VOLUME ["/sensorData"]

# Comando por defecto
CMD ["/usr/local/bin/sensorServer"]
