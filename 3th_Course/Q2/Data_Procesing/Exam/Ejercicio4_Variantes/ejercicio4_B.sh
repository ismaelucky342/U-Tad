# EJERCICIO 4 B — Kafka con Claves y Tolerancia a Fallos (1,5 pts)
# 
# CONTEXTO:
# En una empresa de reparto, cada repartidor envía su ubicación en tiempo real. Para que el sistema no se sature, dividimos el tráfico. Sin embargo, nos interesa que los mensajes de un mismo repartidor vayan siempre a la misma partición para mantener el orden cronológico de su ruta.
# MONTAJE
# 
#     Paso 1 (0,25 pts): Crea un tópico llamado rutas-reparto con 3 particiones y un factor de replicación 1. Esta vez, el servidor de la universidad está en la IP 192.168.1.50:9092.
# 
#     Paso 2 (0,25 pts): Lanza un productor en una terminal, pero configurado para enviar Clave y Valor (separados por un guion -). Envía estos 4 mensajes exactamente:
# 
#         repartidorA-madrid
# 
#         repartidorB-barcelona
# 
#         repartidorA-toledo
# 
#         repartidorC-valencia
# 
#     Paso 3 (0,25 pts): En otra terminal, lanza el primer consumidor del grupo logistica.
# 
#     Paso 4 (0,25 pts): En una tercera terminal, lanza un segundo consumidor del mismo grupo logistica.
# 
# INTERPRETACIÓN Y PREGUNTAS
# 
#     Pregunta 1 (0,25 pts): Teniendo en cuenta que el tópico tiene 3 particiones y tienes 2 consumidores activos en el grupo logistica:
# 
#         ¿Cómo se reparten las 3 particiones entre los 2 consumidores?
# 
#         ¿Por qué los mensajes repartidorA-madrid y repartidorA-toledo van a caer obligatoriamente en la misma terminal (mismo consumidor)?
# 
#     Pregunta 2 (0,25 pts): Si el Consumidor 1 se rompe (se cae el proceso o pulsas Ctrl+C), ¿qué hace Kafka automáticamente con las particiones que tenía asignadas? ¿Se pierden esos mensajes?

# Paso 1: crear el tópico con 3 particiones y factor de replicación 1
kafka-topics.sh \
    --create \
    --topic rutas-reparto \
    --partitions 3 \
    --replication-factor 1 \
    --bootstrap-server

# Paso 2: enviar mensajes con clave y valor
kafka-console-producer.sh \
    --topic rutas-reparto \
    --bootstrap-server
    --property "parse.key=true" \
    --property "key.separator=-"
# (en el terminal del productor, escribir los mensajes uno a uno)
# repartidorA-madrid
# repartidorB-barcelona 
# repartidorA-toledo
# repartidorC-valencia


# Paso 3: lanzar el primer consumidor del grupo logistica
kafka-console-consumer.sh \
    --topic rutas-reparto \
    --bootstrap-server \
    --group logistica \
    --from-beginning

# Paso 4: lanzar el segundo consumidor del mismo grupo logistica
kafka-console-consumer.sh \
    --topic rutas-reparto \
    --bootstrap-server \
    --group logistica \
    --from-beginning

# Pregunta 1:
# - Con 3 particiones y 2 consumidores, Kafka asignará 2 particiones a un consumidor y 1 partición al otro. Por ejemplo, el Consumidor 1 podría recibir las particiones 0 y 1, mientras que el Consumidor 2 recibe la partición 2.
# - Los mensajes con clave "repartidorA" (madrid y toledo) van a la misma partición porque Kafka utiliza la clave para determinar a qué partición enviar el mensaje. Esto garantiza que todos los mensajes de "repartidorA" se mantengan en orden y se procesen por el mismo consumidor.    

# Pregunta 2:
# Si el Consumidor 1 se rompe, Kafka detectará que ya no está activo y reasignará automáticamente las particiones que tenía asignadas al Consumidor 2. Esto significa que el Consumidor 2 comenzará a recibir los mensajes de las particiones que antes manejaba el Consumidor 1. Los mensajes no se pierden, ya que Kafka almacena los mensajes en las particiones hasta que son consumidos y confirmados por los consumidores.    
