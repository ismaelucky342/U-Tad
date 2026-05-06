#!/bin/bash

# ============================================================================
# EJERCICIO 1: APACHE KAFKA - Script de Ejecución
# ============================================================================
# Este script ejecuta todos los pasos del Ejercicio 1

set -e

KAFKA_HOME="${KAFKA_HOME:=/opt/kafka}"
KAFKA_BIN="$KAFKA_HOME/bin"
BOOTSTRAP_SERVER="${BOOTSTRAP_SERVER:=localhost:9092}"
TOPIC_NAME="ventas"
GROUP_NAME="grupo_ventas"

echo ""
echo "============================================================================"
echo "EJERCICIO 1: APACHE KAFKA - GESTIÓN DE TÓPICOS Y MENSAJES"
echo "============================================================================"
echo ""

# ============================================================================
# PASO 1: Crear tópico ventas
# ============================================================================
echo "[PASO 1] Crear tópico 'ventas' con 4 particiones y replicación 1..."
echo "---"

$KAFKA_BIN/kafka-topics.sh --create \
  --topic $TOPIC_NAME \
  --partitions 4 \
  --replication-factor 1 \
  --bootstrap-server $BOOTSTRAP_SERVER \
  --if-not-exists

echo "✓ Tópico creado exitosamente"
echo ""

# ============================================================================
# PASO 2: Listar tópicos existentes
# ============================================================================
echo "[PASO 2] Listar tópicos existentes..."
echo "---"

$KAFKA_BIN/kafka-topics.sh --list \
  --bootstrap-server $BOOTSTRAP_SERVER

echo "✓ Listado completado"
echo ""

# ============================================================================
# PASO 3: Describir el tópico ventas
# ============================================================================
echo "[PASO 3] Describir el tópico 'ventas'..."
echo "---"

$KAFKA_BIN/kafka-topics.sh --describe \
  --topic $TOPIC_NAME \
  --bootstrap-server $BOOTSTRAP_SERVER

echo "✓ Descripción completada"
echo ""

# ============================================================================
# PASO 5: Lanzar consumidor con visualización de clave y valor
# ============================================================================
echo "[PASO 5] Iniciando consumidor (grupo_ventas)..."
echo "Escuchando mensajes en el tópico $TOPIC_NAME..."
echo "Presiona Ctrl+C para detener"
echo "---"

# Lanzar en background
$KAFKA_BIN/kafka-console-consumer.sh \
  --topic $TOPIC_NAME \
  --from-beginning \
  --property print.key=true \
  --property print.value=true \
  --property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \
  --property value.deserializer=org.apache.kafka.common.serialization.StringDeserializer \
  --group $GROUP_NAME \
  --bootstrap-server $BOOTSTRAP_SERVER &

CONSUMER_PID=$!
echo "✓ Consumidor iniciado (PID: $CONSUMER_PID)"
echo ""

sleep 2

# ============================================================================
# PASO 7: Insertar mensajes desde archivo
# ============================================================================
echo "[PASO 7] Insertando 12 mensajes desde archivo..."
echo "---"

# Crear archivo temporal con datos
cat > /tmp/ventas_datos.txt << 'EOF'
1:{"id_venta":1,"producto":"Laptop","cantidad":1,"precio":899.99,"tienda":"Madrid"}
2:{"id_venta":2,"producto":"Mouse","cantidad":5,"precio":15.50,"tienda":"Barcelona"}
3:{"id_venta":3,"producto":"Teclado","cantidad":3,"precio":45.00,"tienda":"Valencia"}
4:{"id_venta":4,"producto":"Monitor","cantidad":2,"precio":299.99,"tienda":"Sevilla"}
5:{"id_venta":5,"producto":"Webcam","cantidad":1,"precio":79.99,"tienda":"Madrid"}
6:{"id_venta":6,"producto":"Auriculares","cantidad":4,"precio":35.50,"tienda":"Barcelona"}
7:{"id_venta":7,"producto":"Hub USB","cantidad":6,"precio":25.00,"tienda":"Bilbao"}
8:{"id_venta":8,"producto":"SSD","cantidad":2,"precio":149.99,"tienda":"Valencia"}
9:{"id_venta":9,"producto":"RAM","cantidad":3,"precio":89.99,"tienda":"Madrid"}
10:{"id_venta":10,"producto":"CPU","cantidad":1,"precio":499.99,"tienda":"Barcelona"}
11:{"id_venta":11,"producto":"GPU","cantidad":1,"precio":699.99,"tienda":"Sevilla"}
12:{"id_venta":12,"producto":"Fuente","cantidad":2,"precio":199.99,"tienda":"Madrid"}
EOF

cat /tmp/ventas_datos.txt | $KAFKA_BIN/kafka-console-producer.sh \
  --topic $TOPIC_NAME \
  --property parse.key=true \
  --property key.separator=: \
  --bootstrap-server $BOOTSTRAP_SERVER

echo "✓ 12 mensajes insertados"
echo ""
sleep 1

# ============================================================================
# PASO 8: Generar 25 mensajes aleatorios
# ============================================================================
echo "[PASO 8] Generando 25 mensajes aleatorios (datagen)..."
echo "---"

PRODUCTOS=("Laptop" "Mouse" "Teclado" "Monitor" "Webcam" "Auriculares" "Hub_USB" "SSD" "RAM" "CPU" "GPU" "Fuente" "Cámara" "Disco" "Cable")
TIENDAS=("Madrid" "Barcelona" "Valencia" "Sevilla" "Bilbao" "Zaragoza" "Málaga" "Córdoba")

for i in {13..37}; do
  ID_VENTA=$i
  PRODUCTO=${PRODUCTOS[$((RANDOM % ${#PRODUCTOS[@]}))]}
  CANTIDAD=$((RANDOM % 10 + 1))
  PRECIO=$(echo "scale=2; $((RANDOM % 900 + 100))" | bc)
  TIENDA=${TIENDAS[$((RANDOM % ${#TIENDAS[@]}))]}
  
  MENSAJE="{\"id_venta\":$ID_VENTA,\"producto\":\"$PRODUCTO\",\"cantidad\":$CANTIDAD,\"precio\":$PRECIO,\"tienda\":\"$TIENDA\"}"
  
  echo "$ID_VENTA:$MENSAJE" | $KAFKA_BIN/kafka-console-producer.sh \
    --topic $TOPIC_NAME \
    --property parse.key=true \
    --property key.separator=: \
    --bootstrap-server $BOOTSTRAP_SERVER
  
  sleep 0.1
done

echo "✓ 25 mensajes aleatorios generados"
echo ""
sleep 2

# ============================================================================
# PASO 6: Consumidor restringido a partición 2
# ============================================================================
echo "[PASO 6] Leyendo desde partición 2 (offset 0)..."
echo "---"

$KAFKA_BIN/kafka-console-consumer.sh \
  --topic $TOPIC_NAME \
  --partition 2 \
  --offset 0 \
  --property print.key=true \
  --property print.value=true \
  --property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \
  --property value.deserializer=org.apache.kafka.common.serialization.StringDeserializer \
  --bootstrap-server $BOOTSTRAP_SERVER \
  --max-messages 100

echo "✓ Lectura de partición 2 completada"
echo ""
sleep 2

# ============================================================================
# PASO 9: Describir consumer group
# ============================================================================
echo "[PASO 9] Estado del consumer group '$GROUP_NAME'..."
echo "---"

$KAFKA_BIN/kafka-consumer-groups.sh \
  --describe \
  --group $GROUP_NAME \
  --bootstrap-server $BOOTSTRAP_SERVER

echo "✓ Descripción del consumer group completada"
echo ""

# ============================================================================
# PASO 10: Análisis de mensajes por partición
# ============================================================================
echo "[PASO 10] Análisis de mensajes por partición..."
echo "---"

for partition in {0..3}; do
  echo -n "Partición $partition: "
  $KAFKA_BIN/kafka-console-consumer.sh \
    --topic $TOPIC_NAME \
    --partition $partition \
    --from-beginning \
    --max-messages 1000000 \
    --timeout-ms 1000 \
    --bootstrap-server $BOOTSTRAP_SERVER 2>/dev/null | wc -l
done

echo ""
echo "✓ Análisis completado"
echo ""

# ============================================================================
# Detener consumidor
# ============================================================================
echo "Deteniendo consumidor de fondo..."
kill $CONSUMER_PID 2>/dev/null || true
sleep 1

echo ""
echo "============================================================================"
echo "✓ EJERCICIO 1 COMPLETADO"
echo "============================================================================"
echo ""
