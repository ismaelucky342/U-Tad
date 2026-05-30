# =======================================
# EJERCICIO 4 — Kafka con Claves (1 pt)
# =======================================
#
# CONTEXTO:
#
# En un sistema de gestión de usuarios, queremos mantener
# la integridad de los datos asociados a cada usuario.
# Para ello, utilizamos CLAVES en Kafka, que garantizan
# que todos los mensajes de un mismo usuario vayan siempre
# a la misma partición, manteniendo el orden.
#
# ---
#
# ENUNCIADO:
#
# Vas a simular un sistema de actualizaciones de perfil
# de usuario, donde es crítico que los cambios de un mismo
# usuario mantengan el orden cronológico.
#
# ---
#
# MONTAJE:
#
# Paso 1 (0,15 pts): Crear un tópico llamado:
#
#   usuarios
#
# con:
#
#   - 3 particiones
#   - factor de replicación 1
#
# Paso 2 (0,15 pts): Mostrar los detalles del tópico creado.
#
# Paso 3 (0,25 pts): Lanzar un productor configurado para
# enviar mensajes con CLAVE y VALOR (separados por guion -).
# Enviar exactamente estos 6 mensajes:
#
#   usuario1-cambio_email
#   usuario2-cambio_password
#   usuario1-cambio_nombre
#   usuario3-eliminar_cuenta
#   usuario2-cambio_foto
#   usuario1-cambio_pais
#
# Paso 4 (0,25 pts): Abrir DOS consumidores
# pertenecientes al grupo:
#
#   sistemas
#
# ---
#
# INTERPRETACIÓN Y PREGUNTAS:
#
# Pregunta 1 (0,1 pts): ¿Por qué los cambios de usuario1
# (cambio_email, cambio_nombre y cambio_pais) llegan
# al MISMO consumidor, en ese MISMO ORDEN?
#
# Pregunta 2 (0,1 pts): ¿Qué ventaja tiene usar claves
# en lugar de enviar solo valores sin clave?
#
# =======================================

# Paso 1: crear el tópico con 3 particiones y factor de replicación 1

kafka-topics.sh \
    --create \
    --topic usuarios \
    --partitions 3 \
    --replication-factor 1 \
    --bootstrap-server localhost:9092

# Paso 2: mostrar los detalles del tópico creado

kafka-topics.sh \
    --describe \
    --topic usuarios \
    --bootstrap-server localhost:9092

# Paso 3: lanzar el productor para el tópico usuarios
# con soporte para CLAVE-VALOR separados por guion

kafka-console-producer.sh \
    --topic usuarios \
    --bootstrap-server localhost:9092 \
    --property "parse.key=true" \
    --property "key.separator=-"

# (en el terminal del productor, escribir los mensajes uno a uno)
# usuario1-cambio_email
# usuario2-cambio_password
# usuario1-cambio_nombre
# usuario3-eliminar_cuenta
# usuario2-cambio_foto
# usuario1-cambio_pais

# Paso 4: abrir DOS consumidores del grupo sistemas

kafka-console-consumer.sh \
    --topic usuarios \
    --group sistemas \
    --bootstrap-server localhost:9092 \
    --from-beginning

kafka-console-consumer.sh \
    --topic usuarios \
    --group sistemas \
    --bootstrap-server localhost:9092 \
    --from-beginning

# ---
#
# RESPUESTAS:
#
# Pregunta 1:
# Los cambios de usuario1 llegan al MISMO consumidor
# en el MISMO ORDEN porque Kafka utiliza la CLAVE
# (usuario1) para determinar a qué PARTICIÓN enviar
# el mensaje. Todos los mensajes con la misma clave
# van siempre a la misma partición, y dentro de una
# partición se mantiene el orden FIFO (First In, First Out).
# Como los 3 cambios de usuario1 van a la misma partición,
# un consumidor del grupo es asignado a esa partición,
# recibiendo los mensajes en orden: cambio_email, cambio_nombre, cambio_pais.
#
# Pregunta 2:
# Usar claves es fundamental para mantener el orden
# dentro de un usuario específico. Sin claves, Kafka
# distribuiría los mensajes de usuario1 de forma aleatoria
# entre las particiones, perdiendo el orden cronológico.
# Con claves, se garantiza que:
#   - Todos los cambios de un usuario van a la misma partición
#   - Se mantiene el orden de los cambios
#   - Se preserva la integridad de los datos del usuario
#   - Los consumidores procesan los eventos en el orden correcto
#
# =======================================
