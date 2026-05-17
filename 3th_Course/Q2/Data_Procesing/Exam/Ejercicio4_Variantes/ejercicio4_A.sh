## EJERCICIO 4 — Kafka con Particiones *(1,5 pts)*
#
#---
#
#> ** ENUNCIADO ORIGINAL**
#> 
#> 
#> Vas a simular cómo Kafka reparte mensajes entre múltiples consumidores dentro de un **mismo grupo de consumo** utilizando **particiones**. Esta pregunta tiene dos partes: la primera trata de montar la simulación y la segunda de interpretarla. Hay que entregar las líneas ejecutadas, un pantallazo final de la ejecución y responder a las preguntas.
#> 
#> **MONTAJE:**
#> 
#> **Paso 1 *(0,25 pts)*:** Crea un tópico llamado `ejercicio3` con **2 particiones** y un **factor de replicación 1** en tu clúster local de Kafka.
#> 
#> **Paso 2 *(0,25 pts)*:** Utiliza un productor para enviar al menos 10 líneas de texto al tópico (`mensaje 1`, `mensaje 2`, …, `mensaje 10`).
#> 
#> **Paso 3 *(0,25 pts)*:** En otro terminal, lanza un consumidor del grupo `grupo3` que lea del tópico `ejercicio3`.
#> 
#> **Paso 4 *(0,25 pts)*:** Abre otro terminal y lanza un **segundo consumidor** del **mismo grupo `grupo3`**, también leyendo del mismo tópico.
#> 
#> **INTERPRETACIÓN:**
#> 
#> Comprueba cómo **cada consumidor recibe mensajes diferentes**, porque Kafka los reparte automáticamente **según las particiones.**
#> 
#> **Pregunta 1 *(0,25 pts)*:** ¿Por qué los dos consumidores reciben mensajes diferentes en lugar de todos?
#> 
#> **Pregunta 2 *(0,25 pts)*:** ¿Qué pasaría si se lanza un tercer consumidor en el mismo grupo `grupo3`, siendo el tópico de solo 2 particiones?
#> 
#
#---
#
### Contexto previo: ¿Qué es Kafka y para qué sirven las particiones?
#
#**Apache Kafka** es un sistema de mensajería distribuida de alto rendimiento. Los mensajes se organizan en **tópicos** (como canales temáticos), y cada tópico se divide en **particiones** para permitir procesamiento en paralelo.
#
#```
#Tópico: ejercicio3
#  ├── Partición 0: [mensaje 1, mensaje 3, mensaje 5, mensaje 7, mensaje 9]
#  └── Partición 1: [mensaje 2, mensaje 4, mensaje 6, mensaje 8, mensaje 10]
#```
#
#Cuando existe un **grupo de consumidores**, Kafka asigna cada partición a exactamente un consumidor del grupo.

# paso 1: crear el tópico con 2 particiones y factor de replicación 1
kafka-topics.sh \
    --create \
    --topic ejercicio3 \
    --partitions 2 \
    --replication-factor 1 \
    --bootstrap-server localhost:9092 

# paso 2: enviar mensajes al tópico
kafka-console-producer.sh \
    --topic ejercicio3 \
    --bootstrap-server localhost:9092
# (en el terminal del productor, escribir los mensajes uno a uno)
# mensaje 1
# mensaje 2
# mensaje 3
# mensaje 4 
# mensaje 5
# mensaje 6
# mensaje 7
# mensaje 8
# mensaje 9
# mensaje 10

# paso 3: lanzar el primer consumidor del grupo grupo3
kafka-console-consumer.sh \
    --topic ejercicio3 \
    --group grupo3 \
    --bootstrap-server localhost:9092 \
    --from-beginning

# paso 4: lanzar el segundo consumidor del mismo grupo grupo3
kafka-console-consumer.sh \
    --topic ejercicio3 \
    --group grupo3 \
    --bootstrap-server localhost:9092 \
    --from-beginning

# Pregunta 1: ¿Por qué los dos consumidores reciben mensajes diferentes en lugar de todos?
# Respuesta: Porque Kafka reparte las particiones entre los consumidores del mismo grupo. Cada consumidor recibe los mensajes de las particiones que le han sido asignadas, por lo que no reciben los mismos mensajes.

# Pregunta 2: ¿Qué pasaría si se lanza un tercer consumidor en el mismo grupo grupo3, siendo el tópico de solo 2 particiones?
# Respuesta: Si se lanza un tercer consumidor en el mismo grupo grupo3, Kafka no podrá asignarle una partición porque solo hay 2 particiones disponibles. Por lo tanto,el tercer consumidor no recibirá ningún mensaje hasta que una partición quede libre (por ejemplo, si uno de los consumidores actuales se desconecta).    
