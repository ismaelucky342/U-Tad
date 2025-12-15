# Dockerfile para brokerFileManager
# Puerto: 32002

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY brokerFileManager /app/

RUN chmod +x /app/brokerFileManager

EXPOSE 32002

CMD ["./brokerFileManager"]
