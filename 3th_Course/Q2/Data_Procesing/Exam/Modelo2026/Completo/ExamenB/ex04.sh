# EJERCICIO 4 (1.5 puntos) - KAFKA: ESCALADO Y CONSUMO
#
#Una aplicación de mensajería instantánea utiliza Kafka para procesar mensajes en tiempo real.
#
#TAREA:
#
#4.1 Crear un tópico llamado:
#
#mensajes-chat
#
#Con:
#
#* 3 particiones
#* replication-factor = 1
#* localhost:9092
#
#4.2 Lanzar dos consumidores dentro del grupo:
#
#chat-grupo
#
#4.3 Crear un productor y enviar:
#
#m1
#m2
#m3
#m4
#m5
#m6
#
#4.4 El tráfico aumenta y se necesita escalar el tópico.
#
#Modificar el tópico para tener:
#
#6 particiones
#
#4.5 Mostrar el estado del grupo de consumidores indicando:
#
#* particiones asignadas
#* offsets
#* LAG
#
#PREGUNTAS:
#
#a) Al pasar de 3 a 6 particiones con consumidores activos:
#
#¿Qué proceso ejecuta Kafka internamente y qué efecto tiene?
#
#b) Si lanzamos 8 consumidores dentro del mismo grupo y el tópico tiene 6 particiones:
#
#¿Los 8 consumidores procesarán mensajes? Justifica.
#
#c) Si todos los mensajes de un usuario utilizan la misma key:
#
#¿Qué problema puede aparecer al aumentar el número de particiones?
#
#PISTAS:
#
#* kafka-topics.sh
#* kafka-console-producer.sh
#* kafka-console-consumer.sh
#* kafka-consumer-groups.sh
#

# Paso 1: crear el tópico con 3 particiones y factor de replicación 1
kafka-topics.sh \
    --create \
    --topic mensajes-chat \
    --partitions 3 \
    --replication-factor 1 \
    --bootstrap-server localhost:9092

# Paso 2: lanzar dos consumidores en paralelo dentro del mismo grupo chat-grupo
kafka-console-consumer.sh \
    --topic mensajes-chat \
    --bootstrap-server localhost:9092 \
    --group chat-grupo \
    --from-beginning

# Paso 3: lanzar el productor de consola y enviar mensajes m1 a m6
kafka-console-producer.sh \
    --topic mensajes-chat \
    --bootstrap-server localhost:9092
# (en el terminal del productor, escribir los mensajes uno a uno)
# m1
# m2
# m3

# m4
# m5
# m6    

# Paso 4: escalar el tópico a 6 particiones
kafka-topics.sh \
    --alter \
    --topic mensajes-chat \
    --partitions 6 \
    --bootstrap-server localhost:9092

# Paso 5: mostrar el estado del grupo de consumidores chat-grupo
kafka-consumer-groups.sh \
    --describe \
    --group chat-grupo \
    --bootstrap-server localhost:9092

#a) Al pasar de 3 a 6 particiones con consumidores activos:
#¿Qué proceso ejecuta Kafka internamente y qué efecto tiene?




#b) Si lanzamos 8 consumidores dentro del mismo grupo y el tópico tiene 6 particiones:
#
#¿Los 8 consumidores procesarán mensajes? Justifica.
#
#c) Si todos los mensajes de un usuario utilizan la misma key:
#
#¿Qué problema puede aparecer al aumentar el número de particiones?
