# Dockerfile para serverFileManager
# Puerto: 32001
# Parámetros: IP del broker

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN mkdir -p /app/FileManagerDir

COPY serverFileManager /app/

RUN chmod +x /app/serverFileManager

EXPOSE 32001

ENV BROKER_IP=""

ENTRYPOINT ["./serverFileManager"]
