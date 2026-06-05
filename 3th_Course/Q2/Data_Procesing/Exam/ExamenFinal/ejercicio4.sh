# =================================================================================================== #
#                                                                                                     #
#                                                       ██╗   ██╗   ████████╗ █████╗ ██████╗          #
#     Procesamiento de datos - Examen Final             ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗         #
#                                                       ██║   ██║█████╗██║   ███████║██║  ██║         #
#     created:        05/06/2026  -  9:10:00            ██║   ██║╚════╝██║   ██╔══██║██║  ██║         #
#     last change:    05/06/2026  -  10:57:23           ╚██████╔╝      ██║   ██║  ██║██████╔╝         #
#                                                        ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝          #
#                                                                                                     #
#     Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com               #
#                                                                                                     # 
#     Github:                                           https://github.com/ismaelucky342              # 
#                                                                                                     # 
# =================================================================================================== #

#Paso 1: Crear un tópico con particiones (0.25ptos)
#Crea un tópico llamado ejercicio4a con 2 particiones y un factor de replicación 1 en tu clú#ster local de Kafka.
#Paso 2: Enviar mensajes (0.25ptos)
#Utiliza un productor para enviar al menos 10 líneas de texto al tópico. Pueden ser mensajes como:
#mensaje 1
#mensaje 2
#mensaje 3

#mensaje 10

#Paso 3: Lanzar el primer consumidor (0.25ptos)
#En otro terminal, lanza un consumidor que lea del tópico ejercicio4a usando el grupo grupoA
#Abre otro terminal  más y lanza un segundo consumidor leyendo del mismo tópico, pero usando el grupo grupoB.

#INTERRETACIÓN:
#Pregunta 1 — 0,25 puntos
#¿Por qué los consumidores de grupoA y grupoB pueden recibir los mismos mensajes aunque estén leyendo del mismo tópico?
#Pregunta 2 — 0,25 puntos
#¿Qué diferencia habría si ambos consumidores pertenecieran al mismo grupo de consumo?

# Creo el topico 
kafka-topics.sh --create --topic ejercicio4a --partitions 2 --replication-factor 1 --bootstrap-server localhost:9092

# Creo un productor 
kafka-console-producer.sh --topic ejercicio4a --bootstrap-server localhost:9092

# Crear Consumidor 1 
kafka-console-consumer.sh --topic ejercicio4a --bootstrap-server localhost:9092 --group grupoA --from-beginning

# Crear Consumidor 2
kafka-console-consumer.sh --topic ejercicio4a --bootstrap-server localhost:9092 --group grupoB --from-beginning

# Pregunta 1: 
# Pueden recibir los mismos mensajes porque pertenecen a grupos de consumo diferentes. Cada grupo de consumo recibe una copia completa de los mensajes del tópico, por lo que ambos consumidores pueden leer todos los mensajes independientemente del grupo al que pertenezcan.

# Pregunta 2: 
# Si pertenecieran al mismo grupo basicamente se repartirían los mensajes entre ellos, es decir, cada mensaje sería procesado por solo uno de los consumidores. 
# Esto es porque Kafka asigna cada partición a un solo consumidor dentro de un grupo, lo que permite distribuir la carga de trabajo entre los consumidores del mismo grupo.
