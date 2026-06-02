/*
Ejercicio 4_B - Kafka: PROCESAMIENTO DE EVENTOS Y PARTICIONES

Este ejercicio demuestra:
1. Creación de topics con múltiples particiones
2. Distribución de mensajes por partición
3. Consumo desde múltiples particiones
4. Interpretación de logs de Kafka

REQUISITOS: Kafka ejecutándose en localhost:9092

========== PASO 1: CREAR TOPIC CON MÚLTIPLES PARTICIONES ==========
cd ~/kafka_2.13-3.x.x

./bin/kafka-topics.sh --create \
  --bootstrap-server localhost:9092 \
  --topic eventos_usuarios \
  --partitions 3 \
  --replication-factor 1

Verificar:
./bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic eventos_usuarios

========== PASO 2: ENVIAR MENSAJES CON CLAVES (PARA PARTICIONAR) ==========
./bin/kafka-console-producer.sh \
  --broker-list localhost:9092 \
  --topic eventos_usuarios \
  --property "parse.key=true" \
  --property "key.separator=:"

Enviar (con clave:valor):
usuario1:login
usuario2:logout
usuario1:click
usuario3:login
usuario2:click

========== PASO 3: CONSUMIDOR DESDE PARTICIÓN ESPECÍFICA ==========
./bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic eventos_usuarios \
  --from-beginning \
  --partition 0

O leer desde todas las particiones (por defecto):
./bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic eventos_usuarios \
  --from-beginning

========== INTERPRETACIÓN ==========

1. PARTICIONES: Con 3 particiones, Kafka distribuye los mensajes
2. CLAVES: La clave determina a qué partición va el mensaje
3. ORDEN: Los mensajes se ordenan POR PARTICIÓN, no globalmente
4. ESCALABILIDAD: Múltiples consumidores pueden leer diferentes particiones

PATRÓN DE DISTRIBUCIÓN:
- Mensajes con la misma clave van a la misma partición (garantiza orden para esa clave)
- Mensajes sin clave se distribuyen round-robin
- La partición se elige usando: particion = hash(clave) % num_particiones

*/

import org.apache.kafka.clients.producer.{KafkaProducer, ProducerRecord}
import java.util.Properties
import scala.collection.JavaConverters._

// ========== PRODUCTOR CON CLAVES ==========

val productorProps = new Properties()
productorProps.put("bootstrap.servers", "localhost:9092")
productorProps.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
productorProps.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")

val productor = new KafkaProducer[String, String](productorProps)

// Eventos de usuario con clave = usuario_id
val eventos = List(
  ("usuario1", "login"),
  ("usuario2", "logout"),
  ("usuario1", "click"),
  ("usuario3", "login"),
  ("usuario2", "click"),
  ("usuario1", "compra")
)

println("=== ENVIANDO EVENTOS ===")
eventos.foreach { case (usuario, evento) =>
  val record = new ProducerRecord[String, String]("eventos_usuarios", usuario, evento)
  val metadata = productor.send(record).get()
  println(s"Usuario: $usuario, Evento: $evento -> Partición: ${metadata.partition()}")
}

productor.close()

// ========== CONSUMIDOR AGRUPADO ==========

import org.apache.kafka.clients.consumer.{KafkaConsumer, ConsumerConfig}
import scala.util.Using

val consumidorProps = new Properties()
consumidorProps.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092")
consumidorProps.put(ConsumerConfig.GROUP_ID_CONFIG, "grupo-eventos")
consumidorProps.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer")
consumidorProps.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer")
consumidorProps.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest")

val consumidor = new KafkaConsumer[String, String](consumidorProps)
consumidor.subscribe(java.util.Arrays.asList("eventos_usuarios"))

println("\n=== CONSUMIENDO EVENTOS ===")
var eventosConsumidos = 0
while (eventosConsumidos < 6) {
  val records = consumidor.poll(java.time.Duration.ofMillis(100))
  records.asScala.foreach { record =>
    println(s"Usuario: ${record.key()}, Evento: ${record.value()}, " +
            s"Partición: ${record.partition()}, Offset: ${record.offset()}")
    eventosConsumidos += 1
  }
}

consumidor.close()

println("\n=== ANÁLISIS ===")
println("Nótese que aunque enviamos eventos de usuarios alternos,")
println("todos los eventos del mismo usuario van a la misma partición")
println("Esto garantiza que se procesan en orden para ese usuario")
