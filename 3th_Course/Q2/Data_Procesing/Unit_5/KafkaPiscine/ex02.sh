# =======================================
# Mini ejercicio Kafka 3
# =======================================
#
# Vas a simular un sistema de pedidos.
#
# Paso 1
#
# Crear un tópico:
#
# pedidos
#
# con:
#
# - 3 particiones
# - factor de replicación 1
#
# Paso 2
#
# Mostrar la información detallada
# del tópico.
#
# Paso 3
#
# Lanzar un productor y escribir:
#
# pedido1
# pedido2
# pedido3
# pedido4
# pedido5
# pedido6
# pedido7
# pedido8
#
# Paso 4
#
# Abrir DOS consumidores
# pertenecientes al grupo:
#
# clientes
#
# Paso 5
#
# Abrir un TERCER consumidor
# también perteneciente al grupo:
#
# clientes
#
# Paso 6
#
# Responder:
#
# a) ¿Cuántos consumidores pueden
# trabajar realmente al mismo tiempo?
#
# b) ¿Qué ocurriría si se añade
# un cuarto consumidor?
#
# c) Si uno de los consumidores
# se desconecta, ¿qué hará Kafka?
#
# =======================================

# paso 1: crear el tópico con 3 particiones y factor de replicación 1

kafka-topics.sh \
    --create \
    --topic pedidos \
    --partitions 3 \
    --replication-factor 1 \
    --bootstrap-server localhost:9092

# paso 2: mostrar la información detallada del tópico

kafka-topics.sh \
    --describe \
    --topic pedidos \
    --bootstrap-server localhost:9092

# paso 3: lanzar el productor para el tópico pedidos

kafka-console-producer.sh \
    --topic pedidos \
    --bootstrap-server localhost:9092

# paso 4: abrir dos consumidores del mismo grupo clientes

kafka-console-consumer.sh \
    --topic pedidos \
    --group clientes \
    --bootstrap-server localhost:9092 \
    --from-beginning

kafka-console-consumer.sh \
    --topic pedidos \
    --group clientes \
    --bootstrap-server localhost:9092 \
    --from-beginning

# paso 5: abrir un tercer consumidor del mismo grupo clientes

kafka-console-consumer.sh \
    --topic pedidos \
    --group clientes \
    --bootstrap-server localhost:9092 \
    --from-beginning

# paso 6: responder las preguntas

# a) Solo 3 consumidores pueden trabajar al mismo tiempo, porque el tópico tiene 3 particiones y cada partición solo puede ser consumida por un consumidor del mismo grupo.
# b) Si se añade un cuarto consumidor, este no recibirá mensajes mientras los otros 3 consumidores estén activos, porque no hay más particiones disponibles para asignar al cuarto consumidor.
# c) Si uno de los consumidores se desconecta, Kafka reasignará automáticamente las particiones que estaban asignadas a ese consumidor a los consumidores restantes del mismo grupo, permitiendo que elos consumidores restantes sigan recibiendo mensajes sin interrupción.        