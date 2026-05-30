# =======================================
# Mini ejercicio Kafka 1
# =======================================
#
# 1) Crear un tópico llamado:
#
# pruebas
#
# con:
#
# - 1 partición
# - factor de replicación 1
#
# 2) Mostrar la lista de tópicos existentes.
#
# 3) Lanzar un productor para el tópico:
#
# pruebas
#
# 4) Escribir 5 mensajes:
#
# hola1
# hola2
# hola3
# hola4
# hola5
#
# 5) Abrir otro terminal y lanzar
# un consumidor que lea desde el inicio.
#
# 6) Responder:
#
# ¿Para qué sirve la opción:
#
# --from-beginning
#
# =======================================

# paso 1: crear el tópico con 1 partición y factor de replicación 1
kafka-topics.sh \
    --create \
    --topic pruebas \
    --partitions 1 \
    --replication-factor 1 \
    --bootstrap-server localhost:9092

# paso 2: mostrar la lista de tópicos existentes
kafka-topics.sh \
    --list \
    --bootstrap-server localhost:9092

# paso 3: lanzar el productor para el tópico pruebas
kafka-console-producer.sh \
    --topic pruebas \
    --bootstrap-server localhost:9092

# paso 4: escribir los mensajes uno a uno
# hola1
# hola2
# hola3
# hola4
# hola5

# paso 5: lanzar el consumidor para leer desde el inicio
kafka-console-consumer.sh \
    --topic pruebas \
    --bootstrap-server localhost:9092 \
    --from-beginning

# paso 6: responder a la pregunta
# La opción --from-beginning hace que el consumidor lea todos los mensajes desde el offset inicial,
# en lugar de solo los nuevos mensajes que lleguen después de que el consumidor se haya iniciado. 
# Sin esta opción, el consumidor solo recibiría los mensajes que se publiquen después de su inicio, 
# y no los mensajes que ya estaban en el tópico.          