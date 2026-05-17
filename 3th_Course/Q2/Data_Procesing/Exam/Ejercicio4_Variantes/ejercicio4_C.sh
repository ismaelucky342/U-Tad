# EJERCICIO 4 — Kafka Avanzado: Rebalanceo, Modificación y Retención (2,0 pts)
# 
# CONTEXTO:
# Estás administrando el sistema de mensajería de una aplicación de mapas. El tráfico ha crecido de golpe debido a una hora punta de tráfico y necesitas escalar el sistema en caliente (sin apagar los servidores) mientras monitorizas cómo Kafka redistribuye los datos.
# MONTAJE (6 Apartados)
# 
#     Paso 1: Crea un tópico llamado trafico-tiempo-real con 3 particiones y factor de replicación 1. El servidor está en localhost:9092.
# 
#     Paso 2: Lanza tres consumidores en paralelo (Terminales 2, 3 y 4) dentro del mismo grupo llamado servicios-mapa.
# 
#     Paso 3: Abre otra terminal (Terminal 5) y lanza un productor de consola. Envía 6 mensajes seguidos (m1, m2, ..., m6).
# 
#     Paso 4 (Modificación en caliente): Resulta que el servidor se está saturando. Abre otra terminal y ejecuta el comando necesario para escalar el tópico a 6 particiones (en lugar de las 3 iniciales).
# 
#     Paso 5: Vuelve a la terminal del productor (Terminal 5) y envía otros 6 mensajes nuevos (m7, m8, ..., m12).
# 
#     Paso 6 (Monitorización): Abre una última terminal y ejecuta el comando para describir el estado del grupo de consumidores servicios-mapa. Necesitamos ver el LAG (el retraso de mensajes) y qué consumidor tiene asignada cada partición.
# 
# INTERPRETACIÓN 
# 
#     Pregunta 1 (La trampa del orden): En el Paso 3 enviamos los mensajes m1 al m6 usando Round-Robin (reparto equitativo). Cuando escalamos el tópico a 6 particiones en el Paso 4 e insertamos los mensajes m7 al m12 en el Paso 5:
# 
#         ¿Por qué cambiar el número de particiones a mitad de camino rompe totalmente el orden global de lectura si estuviéramos usando claves (keys)? ¿Qué problema causa esto a nivel de arquitectura?
# 
#     Pregunta 2 (El Rebalanceo "Eager" vs "Cooperative"): Al pasar de 3 particiones a 6 particiones en un grupo de 3 consumidores activos:
# 
#         ¿Qué ocurre internamente en Kafka con el grupo de consumo? Explica el concepto de Rebalanceo y qué implicación tiene que los consumidores tengan que detener momentáneamente su lectura (Stop-the-world).
# 
#     Pregunta 3 (La persistencia de Kafka): Si cerramos absolutamente todas las terminales de los consumidores y las dejamos apagadas durante dos semanas, y el productor sigue metiendo datos:
# 
#         ¿Cuándo volvamos a encender un consumidor, leerá los mensajes antiguos del primer día? ¿De qué parámetro o política de Kafka depende que esos mensajes sigan ahí o se hayan borrado automáticamente?


# Paso 1: crear el tópico con 3 particiones y factor de replicación 1
kafka-topics.sh \
    --create \
    --topic trafico-tiempo-real \
    --partitions 3 \
    --replication-factor 1 \
    --bootstrap-server localhost:9092

# Paso 2: lanzar tres consumidores en paralelo dentro del mismo grupo servicios-mapa
kafka-console-consumer.sh \
    --topic trafico-tiempo-real \
    --bootstrap-server localhost:9092 \
    --group servicios-mapa \
    --from-beginning

# Paso 3: lanzar el productor de consola y enviar mensajes m1 a m6
kafka-console-producer.sh \
    --topic trafico-tiempo-real \
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
    --topic trafico-tiempo-real \
    --partitions 6 \
    --bootstrap-server localhost:9092

# Paso 5: enviar mensajes m7 a m12
# (en el terminal del productor, escribir los mensajes uno a uno)
# m7
# m8
# m9
# m10
# m11
# m12

# Paso 6: describir el estado del grupo de consumidores servicios-mapa
kafka-consumer-groups.sh \
    --describe \
    --group servicios-mapa \
    --bootstrap-server localhost:9092

# Pregunta 1:
# - Cambiar el número de particiones a mitad de camino rompe el orden global de lectura
#   porque los mensajes nuevos (m7 a m12) se repartirán entre las nuevas particiones (3 a 5) de forma independiente a las anteriores (0 a 2). Esto causa un problema de arquitectura porque los consumidores podrían leer mensajes relacionados (por ejemplo, de un mismo repartidor) en orden diferente, lo que dificulta el procesamiento correcto de la información.

# Pregunta 2:
# - Al pasar de 3 particiones a 6 particiones, Kafka inicia un proceso de Rebalanceo, donde los consumidores del grupo servicios-mapa deben detener momentáneamente su lectura para redistribuir las particiones entre ellos. Esto se conoce como "Stop-the-world" porque durante el rebalanceo, los consumidores no pueden procesar mensajes, lo que puede causar retrasos y afectar la experiencia del usuario. El rebalanceo es necesario para asegurar que cada partición esté  asignada a un consumidor activo, pero puede ser disruptivo si ocurre con frecuencia.            
# Pregunta 3:
# - Si las terminales de los consumidores están apagadas durante dos semanas, los mensajes antiguos del primer día podrían seguir ahí o haberse borrado automáticamente dependiendo de la política de retención configurada en Kafka. Si la política de retención es por tiempo (por ejemplo, 7 días), los mensajes se eliminarán automáticamente después de ese período. Si la política es por tamaño (por ejemplo, 1 GB), los mensajes se eliminarán cuando el tamaño total de los mensajes en el tópico supere ese límite. Por lo tanto, la persistencia de los mensajes depende de la configuración de retención del tópico en Kafka.       
