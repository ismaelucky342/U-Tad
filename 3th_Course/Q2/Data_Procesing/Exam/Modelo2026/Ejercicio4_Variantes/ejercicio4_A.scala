/*
Ejercicio 4_A - Kafka: EJECUCIÓN BÁSICA Y CONSUMO DE MENSAJES

Este ejercicio demuestra cómo ejecutar Kafka en local y procesar mensajes básicos.

REQUISITOS PREVIOS:
1. Tener Kafka descargado en ~/kafka_2.13-3.x.x (o similar)
2. Tener Java instalado
3. Las rutas deben ser absolutas o relativas según tu instalación

PASOS PARA EJECUTAR:

========== PASO 1: INICIAR ZOOKEEPER ==========
cd ~/kafka_2.13-3.x.x

./bin/zookeeper-server-start.sh ./config/zookeeper.properties

(En otra terminal continúa...)

========== PASO 2: INICIAR KAFKA SERVER ==========
cd ~/kafka_2.13-3.x.x

./bin/kafka-server-start.sh ./config/server.properties

(En otra terminal continúa...)

========== PASO 3: CREAR UN TOPIC ==========
cd ~/kafka_2.13-3.x.x

./bin/kafka-topics.sh --create \
  --bootstrap-server localhost:9092 \
  --topic sensores \
  --partitions 1 \
  --replication-factor 1

========== PASO 4: EJECUTAR PRODUCTOR (ENVIAR MENSAJES) ==========
cd ~/kafka_2.13-3.x.x

./bin/kafka-console-producer.sh --broker-list localhost:9092 --topic sensores

# Escribe mensajes (uno por línea):
sensorsensor1,temperatura,25.5
sensorsensor2,humedad,65
sensorsensor1,temperatura,26.0
sensorsensor3,presion,1013.25

========== PASO 5: LEER MENSAJES CON CONSUMIDOR ==========
# En otra terminal:
cd ~/kafka_2.13-3.x.x

./bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic sensores \
  --from-beginning

# Deberías ver:
# sensorsensor1,temperatura,25.5
# sensorsensor2,humedad,65
# sensorsensor1,temperatura,26.0
# sensorsensor3,presion,1013.25

========== INTERPRETACIÓN ==========
1. El productor envía mensajes al topic "sensores"
2. El consumidor los recibe en orden (si hay una sola partición)
3. Si ejecutas el consumidor con --from-beginning, recibe TODOS los mensajes desde el inicio
4. Si lo ejecutas sin --from-beginning, solo recibe nuevos mensajes
5. Kafka mantiene los mensajes almacenados según su configuración de retención

========== ANÁLISIS DE LOS MENSAJES ==========
Formato: id_sensor, tipo_lectura, valor

Análisis posible:
- sensor1 tiene múltiples lecturas de temperatura (25.5 y 26.0)
- Hay diferentes tipos de sensores (temperatura, humedad, presión)
- Los valores están en diferentes rangos y unidades

*/

// Código Scala para producir mensajes a Kafka (usando kafka-clients)
import org.apache.kafka.clients.producer.{KafkaProducer, ProducerRecord}
import java.util.Properties

val props = new Properties()
props.put("bootstrap.servers", "localhost:9092")
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")

val producer = new KafkaProducer[String, String](props)

// Enviar mensajes
val mensajes = List(
  "sensor1,temperatura,25.5",
  "sensor2,humedad,65",
  "sensor1,temperatura,26.0",
  "sensor3,presion,1013.25"
)

mensajes.foreach { msg =>
  val record = new ProducerRecord[String, String]("sensores", msg)
  producer.send(record)
  println(s"Enviado: $msg")
}

producer.close()
println("Productor cerrado")

// ========== CONSUMIDOR EN SCALA ==========

import org.apache.kafka.clients.consumer.{KafkaConsumer, ConsumerConfig}
import scala.collection.JavaConverters._

val consumerProps = new Properties()
consumerProps.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092")
consumerProps.put(ConsumerConfig.GROUP_ID_CONFIG, "grupo-sensores")
consumerProps.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer")
consumerProps.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer")
consumerProps.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest")

val consumer = new KafkaConsumer[String, String](consumerProps)
consumer.subscribe(java.util.Arrays.asList("sensores"))

var count = 0
while (count < 4) {
  val records = consumer.poll(java.time.Duration.ofMillis(100))
  records.asScala.foreach { record =>
    println(s"Recibido: ${record.value()}")
    count += 1
  }
}

consumer.close()
println("Consumidor cerrado")
