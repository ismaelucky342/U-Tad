# Dockerfile para docManager
FROM ubuntu:24.04

# Instalar dependencias básicas si fueran necesarias
RUN apt-get update && apt-get install -y \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio donde se montará el volumen
RUN mkdir -p /docDir

# Copiar el ejecutable 
COPY serverDocManager /usr/local/bin/serverDocManager
RUN chmod +x /usr/local/bin/serverDocManager

# Declarar el volumen (opcional, ayuda a documentar)
VOLUME ["/docDir"]

# Comando por defecto
CMD ["/usr/local/bin/serverDocManager"]
