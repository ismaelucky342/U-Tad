# =======================================
# Mini ejercicio Kafka 2
# =======================================
#
# 1) Crear un tópico:
#
# mensajes
#
# con:
#
# - 2 particiones
# - factor de replicación 1
#
# 2) Mostrar los detalles del tópico
# creado (no solo listarlo).
#
# 3) Lanzar un productor y enviar:
#
# texto1
# texto2
# texto3
# texto4
# texto5
# texto6
#
# 4) Abrir DOS consumidores
# pertenecientes al grupo:
#
# grupoA
#
# 5) Responder:
#
# a) ¿Por qué los consumidores
# no reciben exactamente los
# mismos mensajes?
#
# b) ¿Qué ocurriría si el tópico
# tuviera una sola partición?
#
# =======================================

# paso 1: crear el tópico con 2 particiones y factor de replicación 1

kafka-topics.sh \
    --create \
    --topic mensajes \
    --partitions 2 \
    --replication-factor 1 \
    --bootstrap-server localhost:9092

# paso 2: mostrar los detalles del tópico creado

kafka-topics.sh \
    --describe \
    --topic mensajes \
    --bootstrap-server localhost:9092

# paso 3: lanzar el productor para el tópico mensajes

kafka-console-producer.sh \
    --topic mensajes \
    --bootstrap-server localhost:9092

# paso 4: abrir dos consumidores del mismo grupo grupoA

kafka-console-consumer.sh \
    --topic mensajes \
    --group grupoA \
    --bootstrap-server localhost:9092 \
    --from-beginning

kafka-console-consumer.sh \
    --topic mensajes \
    --group grupoA \
    --bootstrap-server localhost:9092 \
    --from-beginning

# paso 5: responder a las preguntas

#a) Los consumidores no reciben exactamente los mismos mensajes porque Kafka
# reparte automáticamente los mensajes entre las particiones. Cada consumidor del mismo grupo 
# se le asigna una o varias particiones, por lo que cada consumidor recibe solo los mensajes 
# de las particiones que le han sido asignadas.
#
#b) Si el tópico tuviera una sola partición,
# solo un consumidor del grupo recibiría mensajes.
# Los demás consumidores quedarían inactivos,
# porque una partición solo puede asignarse
# a un consumidor dentro del mismo grupo.