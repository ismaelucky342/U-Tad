# EJERCICIO 4 (Variante 3) — Kafka Avanzado: Alta Disponibilidad, Tolerancia a Fallos y Semántica de Entrega (2,0 pts)
# 
# CONTEXTO:
# Estás diseñando la arquitectura de Kafka para una aplicación bancaria que procesa transferencias de dinero en tiempo real. Debido a la naturaleza crítica de los datos, no puedes permitirte perder ni un solo mensaje, incluso si un servidor físico de Kafka (un bróker) se quema o se desconecta de la red. Tienes un clúster compuesto por 3 brókers (localhost:9092, localhost:9093, localhost:9094).
# MONTAJE (6 Apartados)
# 
#     Paso 1: Crea un tópico llamado transferencias-urgentes con 3 particiones. Como el dinero no se puede perder, esta vez exige un factor de replicación de 3 (--replication-factor 3).
# 
#     Paso 2: Configura el tópico a nivel de parámetros para que exija un mínimo de 2 réplicas sincronizadas para aceptar escrituras (min.insync.replicas=2).
# 
#     Paso 3: Lanza un consumidor de consola en la Terminal 2 escuchando el tópico bajo el grupo validador-bancario.
# 
#     Paso 4 (Configuración del Productor): Abre la Terminal 3 y lanza un productor de consola. Para asegurar que el banco no pierda datos, configúralo explícitamente con la máxima garantía de entrega (acks=all). Envía 3 transacciones de prueba:
#     Plaintext
# 
#     t1: 100EUR
#     t2: 250EUR
#     t3: 50EUR
# 
#     Paso 5 (Simulación de Catástrofe): Ve a la terminal del sistema operativo y apaga repentinamente dos de los tres brókers de Kafka (por ejemplo, mata los procesos de los brókers 9093 y 9094), dejando vivo únicamente al bróker 9092.
# 
#     Paso 6 (Intento de Escritura en Crisis): Vuelve a la terminal del productor (Terminal 3) e intenta enviar una cuarta transferencia crucial:
# 
# Plaintext
# 
#     t4: 5000EUR
#     ```
#     Observa el comportamiento o el error que devuelve la consola.
# 
# ---
# 
# ## INTERPRETACIÓN
# 
# ### Pregunta 1 (El concepto de ISR y la Elección de Líder)
# Cuando el sistema funcionaba con los 3 brókers vivos, cada partición tenía un bróker "Líder" y dos "Seguidores" (Followers) formando el conjunto ISR (*In-Sync Replicas*).
# * Al apagar los dos brókers en el Paso 5, ¿qué ocurre con las particiones cuyos líderes estaban en los servidores que acaban de morir? ¿Qué pasa si el único bróker que queda vivo (9092) no estaba sincronizado con el líder anterior en el momento de la caída?
# 
# ### Pregunta 2 (La Resistencia del Productor: `acks=all` vs `min.insync.replicas`)
# En el Paso 6, intentaste enviar la transferencia `t4` teniendo 2 de los 3 brókers caídos. 
# * ¿Aceptará Kafka el mensaje `t4` y confirmará la escritura, o lanzará un error? Justifica tu respuesta relacionando el comportamiento del productor (`acks=all`) con la regla que pusiste en el tópico (`min.insync.replicas=2`). ¿Qué error específico de Kafka se genera en esta situación?
# 
# ### Pregunta 3 (Disponibilidad de Lectura vs Escritura)
# Con dos brókers caídos y el clúster en un estado degradado:
# * Si el consumidor del grupo `validador-bancario` sigue encendido en la Terminal 2, ¿podrá seguir leyendo los mensajes antiguos (`t1`, `t2`, `t3`) que ya habían sido confirmados antes de la caída? Explica la diferencia en Kafka entre la "Disponibilidad de Escritura" y la "Disponibilidad de Lectura" ante fallos masivos de infraestructura.
# 
# ---

# Paso 1: crear el tópico con 3 particiones y factor de replicación 3

kafka-topics.sh \
    --create \
    --topic transferencias-urgentes \
    --partitions 3 \
    --replication-factor 3 \
    --bootstrap-server localhost:9092,localhost:9093,localhost:9094


# Paso 2: configurar el tópico para exigir un mínimo de 2 réplicas sincronizadas

kafka-configs.sh \
    --bootstrap-server localhost:9092,localhost:9093,localhost:9094 \
    --entity-type topics \
    --entity-name transferencias-urgentes \
    --alter \
    --add-config min.insync.replicas=2

# Paso 3: lanzar un consumidor de consola en la Terminal 2 escuchando el tópico bajo el grupo validador-bancario

kafka-console-consumer.sh \
    --topic transferencias-urgentes \
    --bootstrap-server localhost:9092,localhost:9093,localhost:9094 \
    --group validador-bancario \
    --from-beginning

# Paso 4: lanzar el productor de consola y enviar mensajes t1 a t3 con acks=all

kafka-console-producer.sh \
    --topic transferencias-urgentes \
    --bootstrap-server localhost:9092,localhost:9093,localhost:9094 \
    --producer-property acks=all

# (en el terminal del productor, escribir los mensajes uno a uno)
# t1: 100EUR
# t2: 250EUR
# t3: 50EUR


# Paso 5: apagar dos de los tres brókers de Kafka (por ejemplo, matar los procesos de los brókers 9093 y 9094)
# (en la terminal del sistema operativo, ejecutar comandos para matar los procesos de los brókers 9093 y 9094, por ejemplo:)
# kill $(lsof -t -i:9093)
# kill $(lsof -t -i:9094) 

# Paso 6: intentar enviar una cuarta transferencia crucial t4: 5000EUR
# (en el terminal del productor, escribir el mensaje)
# t4: 5000EUR


# Pregunta 1:
# - Al apagar los dos brókers, las particiones cuyos líderes estaban en esos servidores se vuelven inaccesibles, ya que el líder de cada partición es el encargado de coordinar las escrituras y lecturas. Si el único bróker que queda vivo (9092) no estaba sincronizado con el líder anterior en el momento de la caída, entonces esas particiones   no tendrán un líder disponible, lo que resultará en una pérdida de disponibilidad para esas particiones. En este caso, el clúster no podrá aceptar escrituras ni lecturas para esas particiones hasta que se recupere el líder o se elija un nuevo líder entre las réplicas sincronizadas.      

# Pregunta 2:
# - Kafka no aceptará el mensaje `t4` y lanzará un error. Esto se debe a que el productor está configurado con `acks=all`, lo que significa que requiere que todas las réplicas sincronizadas confirmen la escritura antes de considerar el mensaje como exitos amente enviado. Sin embargo, con dos de los tres brókers caídos, solo queda un bróker vivo, lo que no cumple con la regla de `min.insync.replicas=2` que se estableció en el tópico. Por lo tanto, Kafka generará un error específico de Kafka llamado `NotEnoughReplicasException`, indicando que no hay suficientes réplicas sincronizadas para aceptar la escritura. 

# Pregunta 3:
# - Con dos brókers caídos, el consumidor del grupo `validador-bancario` podrá seguir leyendo los mensajes antiguos (`t1`, `t2`, `t3`) que ya habían sido confirmados antes de la caída, siempre y cuando esos mensajes hayan sido replicados y confirmados en el bróker que sigue vivo (9092). La "Disponibilidad de Escritura" se refiere a la capacidad del clúster para aceptar nuevas escrituras, lo que en este caso está comprometida debido a la falta de réplicas sincronizadas. Por otro lado, la "Disponibilidad de Lectura" se refiere a la capacidad del clúster para permitir a los consumidores leer mensajes que ya han sido confirmados. En este escenario, aunque la disponibilidad de escritura está afectada, la disponibilidad de lectura puede mantenerse para los mensajes que ya fueron confirmados antes de la caída, siempre y cuando esos mensajes estén disponibles en el bróker que sigue vivo. Sin embargo, si los mensajes no estaban completamente replicados antes de la caída, entonces esos mensajes podrían no estar disponibles para lectura, lo que también afectaría la disponibilidad de lectura. 


