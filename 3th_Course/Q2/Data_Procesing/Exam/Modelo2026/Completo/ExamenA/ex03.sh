# ===============================================================================
# EJERCICIO 4 (1.5 puntos) - KAFKA: CONCEPTOS Y CONFIGURACIÓN
# ===============================================================================
# 
# Se necesita configurar un sistema Kafka para procesar eventos de sensores IoT:
# - 100 sensores distribuidos geográficamente
# - Cada sensor envía un evento cada 5 segundos
# - Los sensores pueden fallar e intentar reconectarse
# 
# PREGUNTAS CONCEPTUALES (sinresponder código, solo explicación):
# 
# 4.1) ¿Cuántas particiones recomendarías para el topic "sensores"?
#      Justifica tu respuesta considerando: escalabilidad, latencia, consumidores.
# 
# 4.2) ¿Qué configuración de acks elegirías? (acks=0, acks=1, o acks=all)
#      ¿Por qué? ¿Qué tradeoff existe?
# 
# 4.3) Si un sensor falla, ¿cómo garantizarías que no se pierden sus eventos?
#      (Menciona configuración de Kafka y reintentos)
# 
# 4.4) ¿Cómo harías para que cada sensor SOLO consuma sus propios eventos?
#      (Menciona key, partición, consumer group)
# 
# COMANDOS ÚTILES (referencia):
# Crear topic:
# kafka-topics.sh --create --topic sensores --partitions 10 --replication-factor 3
# 
# Productor:
# kafka-console-producer.sh --broker-list localhost:9092 --topic sensores
# 
# Consumidor:
# kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sensores

# 4.1) Para el topic "sensores", recomendaría configurar al menos 10 particiones. 
# Esto permitiría distribuir la carga de eventos entre múltiples consumidores, 
# mejorando la escalabilidad y reduciendo la latencia. Con 100 sensores enviando eventos cada 5 segundos, 
# tener varias particiones permite que los consumidores procesen los eventos en paralelo, evitando cuellos de botella.

# 4.2) Para la configuración de acks, elegiría "acks=all".
# Esto garantiza que el productor recibirá una confirmación solo cuando todos los réplicas 
# hayan confirmado la recepción del mensaje, lo que proporciona la mayor durabilidad y evita la pérdida de eventos en caso de fallos.
# El tradeoff es que esto puede aumentar la latencia, ya que el productor debe esperar a que todas las réplicas confirmen.

# 4.3) Para garantizar que no se pierden los eventos de un sensor que falla, configuraría el productor con reintentos (retries) y un tiempo de espera (retry.backoff.ms).
# Además, usaría "acks=all" para asegurar que los eventos se confirmen correctamente. En caso de que un sensor falle, el productor intentará reenviar los eventos automáticamente, minimizando la pérdida de datos.     

# 4.4) Para que cada sensor solo consuma sus propios eventos, se puede usar la clave (key) en los mensajes enviados por cada sensor.
# Al asignar una clave única para cada sensor, Kafka garantizará que todos los eventos de ese sensor se envíen a la misma partición. Luego, cada consumidor puede suscribirse
# a esa partición específica para consumir solo los eventos de su sensor correspondiente. Además, se puede configurar un consumer group para cada sensor, asegurando que cada consumidor solo procese los eventos de su propio sensor.
