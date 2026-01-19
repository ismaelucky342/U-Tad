# Dockerfile mínimo para Modelo C (collector)
FROM alpine:latest
LABEL version="1.0"
LABEL description="Collector service minimal image"
LABEL maintainer="tu_email@ejemplo.com"

RUN apk update && apk add --no-cache curl
WORKDIR /app
COPY ./README.md /app/README.md
EXPOSE 7070
CMD ["sh", "-c", "echo 'Collector container started'; sleep 3600"]
