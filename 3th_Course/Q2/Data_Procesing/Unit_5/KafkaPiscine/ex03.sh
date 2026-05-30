# Ejercicio de Errores comunes 

# =======================================
# EJERCICIO 1 — Kafka (debug básico)
# =======================================
#
# Se ejecuta lo siguiente:

kafka-topics.sh \
  --create \
  --topic logs \
  --partitions 2 \
  --replication-factor 2 \
  --bootstrap-server localhost:9092

# ¿que problema hay en este comando?

# el problema es que el factor de replicación no puede ser mayor que el número de brokers disponibles, y en este caso solo tenemos un broker, por lo que el factor de replicación debe ser 1.
# llamamos broker a cada instancia de Kafka que se ejecuta en un servidor. El factor de replicación indica cuántas copias de cada partición se deben mantener en diferentes brokers para garantizar la disponibilidad y tolerancia a fallos. Si el factor de replicación es mayor que el número de brokers, no se podrán crear las copias necesarias y el comando fallará.

# =======================================
# EJERCICIO 2 — consumidores
# =======================================
#
# Se crea un tópico:

kafka-topics.sh \
  --create \
  --topic eventos \
  --partitions 1 \
  --replication-factor 1 \
  --bootstrap-server localhost:9092

  # Luego se ejecutan DOS consumidores:

  kafka-console-consumer.sh \
  --topic eventos \
  --group g1 \
  --bootstrap-server localhost:9092

  kafka-console-consumer.sh \
  --topic eventos \
  --group g1 \
  --bootstrap-server localhost:9092

# ¿Qué comportamiento esperas ver y qué error conceptual hay en el planteamiento del ejercicio?

# El error conceptual es que ambos consumidores pertenecen al mismo grupo de consumidores (g1), 
# por lo que Kafka asignará la partición del tópico eventos a uno de los consumidores, 
# y el otro consumidor no recibirá ningún mensaje. En este caso, solo uno de los consumidores
# podrá consumir mensajes del tópico eventos, mientras que el otro permanecerá inactivo esperando
# a que se le asigne una partición. Para que ambos consumidores puedan recibir mensajes, deberían
# pertenecer a grupos de consumidores diferentes o el tópico debería tener más particiones para que Kafka
# pueda asignar una partición a cada consumidor dentro del mismo grupo.

# Solo Uno de los consumidores sera ACTIVO el otro estara en estado IDLE esperando a que se le asigne una particion, pero como solo hay una particion, el segundo consumidor no recibira ningun mensaje.

# =======================================
# EJERCICIO 3 — productor/consumidor
# =======================================
#
# Se lanza un consumidor:

kafka-console-consumer.sh \
  --topic mensajes \
  --group grupoA \
  --bootstrap-server localhost:9092

# Luego se lanza un productor y se envian mensajes 
kafka-console-producer.sh \
  --topic mensajes \
  --bootstrap-server localhost:9092

# hola 
# que tal 
# adios

# Aqui eñ alumno dice que no ve ningun mensaje del consumidor, da 2 posibles causas del problema y como solucionarlas.

# Posible causa 1: El tópico mensajes no existe. Solución: Crear el tópico mensajes antes de lanzar el productor y el consumidor.
# Posible causa 2: El consumidor se lanzó antes de que el productor enviara los mensajes, y no se usó la opción --from-beginning. Solución: Volver a lanzar el consumidor con la opción --from-beginning para que pueda leer los mensajes desde el inicio del tópico, incluso si fueron enviados antes de que el consumidor se iniciara.

