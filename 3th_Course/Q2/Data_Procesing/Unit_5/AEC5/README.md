# AEC5 - Spark Streaming

## INTRODUCCIÓN

En esta práctica he trabajado con dos tecnologías fundamentales para procesamiento de datos en tiempo real: Apache Kafka para gestión de streams de mensajes, y Spark Streaming para análisis en tiempo real. El objetivo principal era comprender cómo funcionan estas plataformas en un entorno real, desde la creación de tópicos hasta el consumo y análisis de datos.

La actividad constaba de dos ejercicios bien diferenciados. En el primero, trabajo con Kafka realizando todas las operaciones de gestión de tópicos, producción de mensajes desde ficheros, consumo de datos y análisis de consumer groups. En el segundo, implemento un analizador de logs web en tiempo real usando Spark Streaming, eligiendo la variante 3 (análisis de logs) por su aplicabilidad práctica en entornos reales de monitoreo de infraestructuras.

---

## EJERCICIO 1: APACHE KAFKA

### ¿Por qué Kafka?

Kafka es mucho más que una aplicación de mensajería simple. Es una plataforma de streaming distribuida diseñada para manejar millones de eventos por segundo. Lo importante a entender es que los datos no son estáticos sino que fluyen continuamente, y necesitamos arquitecturas que puedan capturar, almacenar y procesar ese flujo de manera escalable y tolerante a fallos.

En este ejercicio implementé todos los pasos necesarios para trabajar con Kafka en un escenario real: crear la infraestructura (tópicos), producir datos (desde ficheros y generadores), consumir datos de formas múltiples, y analizar el estado del sistema.

### Paso 1: Crear el tópico "ventas"

El primer paso es crear el tópico que va a contener todos nuestros mensajes de ventas. He elegido 4 particiones específicamente porque es un número que permite paralelismo real en equipos modernos sin ser excesivo para esta práctica.

```bash
kafka-topics.sh --create \
  --topic ventas \
  --partitions 4 \
  --replication-factor 1 \
  --bootstrap-server localhost:9092
```

**Razonamiento:** La clave de entender particiones es que cada partición es una réplica independiente que se puede procesar en paralelo. Con 4 particiones, podemos distribuir la carga entre múltiples productores sin competencia. El factor de replicación 1 es el mínimo - en un entorno de producción sería mayor para garantizar disponibilidad.

**Resultado:**
```
Created topic ventas.
```

### Paso 2: Listar los tópicos existentes

Después de crear el tópico, verifico que efectivamente se ha creado correctamente listando todos los tópicos del broker:

```bash
kafka-topics.sh --list --bootstrap-server localhost:9092
```

**Por qué este paso importa:** Cuando trabajas con múltiples tópicos en Kafka, perder el track de cuál existe y cuál no es fácil. Este comando es fundamental para debugging y verificación de que el sistema está en el estado esperado.

**Resultado:**
```
__consumer_offsets
ventas
```

El tópico `__consumer_offsets` es interno de Kafka para rastrear offsets de consumidores.

### Paso 3: Describir el tópico "ventas"

Una vez creado, necesito ver los detalles internos del tópico: cómo están distribuidas las particiones, qué broker es líder de cada una, etc.

```bash
kafka-topics.sh --describe --topic ventas --bootstrap-server localhost:9092
```

**Explicación detallada del output:**

```
Topic: ventas    PartitionCount: 4    ReplicationFactor: 1
    Topic: ventas    Partition: 0    Leader: 0    Replicas: 0    Isr: 0
    Topic: ventas    Partition: 1    Leader: 0    Replicas: 0    Isr: 0
    Topic: ventas    Partition: 2    Leader: 0    Replicas: 0    Isr: 0
    Topic: ventas    Partition: 3    Leader: 0    Replicas: 0    Isr: 0
```

- **Leader:** Broker que es responsable de esta partición
- **Replicas:** Todos los brokers que tienen una copia (en este caso solo el broker 0)
- **Isr:** In-Sync Replicas - brokers que están sincronizados con el líder

Con factor de replicación 1, cada réplica tiene solamente una copia, así que si el broker 0 cae, esa partición es inaccesible. Esto es aceptable para desarrollo, pero inaceptable en producción.

### Paso 4: Definir esquema Avro

El esquema define la estructura de los datos que se transmiten. En un caso real, esto es más importante que simplemente enviar datos en formato libre - el esquema garantiza que todos los productores envían datos con la misma estructura.

**Ubicación:** `/home/bigdata/confluent-7.5.1/console-consumer-primitive-keys-values/ventas.json`

**Contenido:**
```json
{
  "type": "record",
  "name": "Venta",
  "namespace": "com.tienda.ventas",
  "fields": [
    {
      "name": "id_venta",
      "type": "long",
      "doc": "Identificador único de la venta"
    },
    {
      "name": "producto",
      "type": "string",
      "doc": "Nombre del producto"
    },
    {
      "name": "cantidad",
      "type": "int",
      "doc": "Cantidad vendida"
    },
    {
      "name": "precio",
      "type": "double",
      "doc": "Precio unitario"
    },
    {
      "name": "tienda",
      "type": "string",
      "doc": "Ubicación de la tienda"
    }
  ]
}
```

**Por qué este esquema:** He elegido tipos específicos por una razón:
- `id_venta` como `long` porque necesita ser identificador único distribuido
- `producto` como `string` porque es texto variable
- `cantidad` como `int` porque raramente vendemos más de millones de unidades
- `precio` como `double` para precisión decimal en operaciones monetarias
- `tienda` como `string` para flexibilidad en nombres de ubicaciones

### Paso 5: Consumidor con visualización de clave y valor

Ahora lanzo un consumidor que lee todos los mensajes desde el principio, mostrando tanto clave como valor:

```bash
kafka-console-consumer.sh \
  --topic ventas \
  --group grupo_ventas \
  --from-beginning \
  --property print.key=true \
  --property print.value=true \
  --property key.separator=: \
  --bootstrap-server localhost:9092
```

**Explicación desde el razonamiento del negocio:**

La clave es importante porque permite ordenamiento y particionamiento. En nuestro caso, usamos `id_venta` como clave - esto significa que todas las ventas del mismo ID siempre van a la misma partición, permitiendo procesamiento secuencial de eventos relacionados.

**Resultado esperado:**
```
1:{"id_venta":1,"producto":"Laptop","cantidad":1,"precio":899.99,"tienda":"Madrid"}
2:{"id_venta":2,"producto":"Mouse","cantidad":5,"precio":15.50,"tienda":"Barcelona"}
...
```

El consumer group `grupo_ventas` es fundamental - Kafka rastrea qué offset ha consumido este grupo, permitiendo que múltiples consumidores del mismo grupo cooperen sin duplicar trabajo.

### Paso 6: Consumidor restringido a una partición

A veces necesitamos leer solo de una partición específica, especialmente para debugging o reprocesamiento:

```bash
kafka-console-consumer.sh \
  --topic ventas \
  --partition 2 \
  --offset 0 \
  --property print.key=true \
  --property print.value=true \
  --property key.separator=: \
  --bootstrap-server localhost:9092
```

**Diferencias clave respecto al paso anterior:**
- No especificamos `--group`, es un consumidor independiente
- `--partition 2` fuerza lectura únicamente de la partición 2
- `--offset 0` comienza desde el principio, no desde donde estaba el consumer group

**Uso práctico:** Si sospechamos que la partición 2 tiene datos corruptos o queremos verificar el contenido de una partición específica sin afectar al tracking del group.

### Paso 7: Insertar 12 mensajes desde archivo

Ahora producimos nuestros primeros 12 mensajes desde un archivo predefinido:

```bash
cat ventas_datos.txt | kafka-console-producer.sh \
  --topic ventas \
  --property parse.key=true \
  --property key.separator=: \
  --bootstrap-server localhost:9092
```

**Archivo ventas_datos.txt:**
```
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
```

**Importancia del formato:** La clave (ID de venta) y el valor (JSON completo) están separados por `:`. Kafka usa la clave para determinar a qué partición enviar el mensaje. Este es un concepto crítico - los mensajes con la misma clave siempre van a la misma partición.

### Paso 8: Generar 25 mensajes aleatorios

Para simular un escenario más realista, genero 25 mensajes aleatorios usando la herramienta datagen:

```bash
kafka-datagen.sh \
  --topic ventas \
  --schemaFile ventas.json \
  --records 25 \
  --bootstrap-server localhost:9092
```

**Razonamiento:** Después de los 12 mensajes controlados, necesito datos más realistas que reflejen variabilidad. Kafka datagen genera valores aleatorios respetando el esquema Avro definido en ventas.json.

**Resultado:** El sistema ahora tiene 12 + 25 = 37 mensajes distribuidos entre las 4 particiones.

### Paso 9: Describir el consumer group

Aquí es donde la práctica se vuelve interesante - ver qué está pasando realmente con los consumidores:

```bash
kafka-consumer-groups.sh \
  --group grupo_ventas \
  --describe \
  --bootstrap-server localhost:9092
```

**Salida esperada:**
```
TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG  CONSUMER-ID
ventas          0          10              10              0    ...
ventas          1          8               8               0    ...
ventas          2          10              10              0    ...
ventas          3          9               9               0    ...
```

**Análisis detallado de cada columna:**

- **CURRENT-OFFSET:** Último offset que el consumer group consumió. Si vemos múltiples líneas, hay múltiples consumidores en el group coordinándose.
- **LOG-END-OFFSET:** El offset del último mensaje en esa partición - el "final" actual del log.
- **LAG:** La diferencia entre LOG-END-OFFSET y CURRENT-OFFSET. Si es 0, estamos al día. Si es mayor, hay mensajes sin consumir.

Este output es la herramienta de debugging número 1 cuando algo funciona lentamente en Kafka - el LAG te dice inmediatamente si los consumidores están rezagados.

### Paso 10: Contar mensajes por partición

El último paso es analizar la distribución de mensajes:

```bash
# Ver el número total de mensajes por partición
kafka-consumer-groups.sh --group grupo_ventas --describe --bootstrap-server localhost:9092
```

**Análisis e interpretación:**

La forma en que Kafka distribuye mensajes entre particiones está determinada por la clave. Como cada `id_venta` es única, los mensajes se distribuyen aproximadamente uniformemente (aunque nunca exactamente, porque el hash de las claves no es perfecto).

Con 37 mensajes y 4 particiones:
- Partición 0: ~9 mensajes
- Partición 1: ~9 mensajes  
- Partición 2: ~10 mensajes
- Partición 3: ~9 mensajes

If all LAG values are 0, significa que el consumer group `grupo_ventas` ya consumió todos los mensajes - no hay colas pendientes.

---

## EJERCICIO 2: SPARK STREAMING - ANÁLISIS DE LOGS WEB

### Variante Elegida: Análisis de Logs Web

He elegido la variante 3 (análisis de logs web) porque es la que mejor refleja un caso de uso real en infraestructuras modernas. En cualquier sitio web o servicio en línea, entender qué está sucediendo en tiempo real es crítico para detección temprana de problemas, identificación de patrones de ataque, y optimización de recursos.

### ¿Por qué Spark Streaming para logs?

Spark Streaming es particularmente bueno para esto porque:
1. **Expresiones regulares:** Los logs web son semiestructurados - necesitamos parsearlos con regex
2. **Agregaciones en tiempo real:** Queremos saber "top 10 IPs" dinámicamente, sin recargar toda la BD
3. **Ventanas temporales:** Podemos detectar "30 IPs diferentes en los últimos 5 minutos" que indique ataque

### La Arquitectura

El flujo es simple pero poderoso:
1. Los logs llegan desde archivos o socket
2. Spark los parsea línea por línea
3. Se aplican transformaciones (extraer IP, usuario, etc.)
4. Se agrupan por ventanas temporales
5. Se muestran resultados en tiempo real en la consola

### Formato de Datos - Logs Web

Los logs web siguen un formato estándar que viene del servidor Apache hace décadas:

```
IP - USUARIO [TIMESTAMP] "METODO RUTA PROTOCOLO" CODIGO_ESTADO TAMAÑO "REFERRER" "USER-AGENT"

Ejemplo real:
192.168.1.100 - admin [06/May/2026:10:15:30] "GET /admin HTTP/1.1" 200 1234 "-" "Mozilla/5.0"
```

Este formato es casi un estándar de la industria, lo que lo hace perfecto para esta práctica.

### Implementación: Archivo Principal

El script `spark_streaming_logs.py` implementa dos modos de consumo:

**Modo 1: Desde Directorio**
```bash
python3 spark_streaming_logs.py --directory logs_input
```

Spark monitorea el directorio y procesa nuevos archivos conforme aparecen. Este es el modo más común en infraestructuras.

**Modo 2: Desde Socket (TCP)**
```bash
python3 spark_streaming_logs.py --socket localhost:9999
```

Conexión directa TCP para streams en vivo. Usado cuando tienes aplicaciones enviando logs en tiempo real.

### Los Análisis Realizados

#### 1. Top 10 IPs más activas

```python
parsed.groupBy("ip").agg(count("*").alias("accesos")).orderBy(desc("accesos"))
```

**Por qué importa:** Si una IP hace 1000 requests en 10 segundos, algo sospechoso está pasando. Las IPs con más actividad son candidatas para investigación de seguridad.

**Resultado esperado:**
```
192.168.1.100       25 accesos
203.0.113.50        18 accesos
192.168.1.101       15 accesos
```

#### 2. Top 10 Usuarios más activos

```python
parsed.filter(col("user") != "-") \
    .groupBy("user").agg(count("*").alias("accesos")) \
    .orderBy(desc("accesos"))
```

**Interpretación:** Un usuario haciendo 100 requests por minuto a `/checkout` probablemente está atacando, o hay un error en su cliente. Un usuario hace 50 GET a `/api/data` regularmente es probable que sea legítimo.

**Resultado esperado:**
```
admin           32 accesos
user1           28 accesos
guest           15 accesos
```

#### 3. Distribución de códigos HTTP (Análisis Adicional)

```python
parsed.groupBy("status_code").agg(count("*").alias("cantidad")).orderBy(col("status_code"))
```

**Significado de los códigos:**
- **200:** Éxito - la solicitud fue procesada correctamente
- **404:** Not Found - cliente pidió un recurso inexistente (común en ataques)
- **500:** Error del servidor - algo falló internamente
- **301/302:** Redireccionamientos - pueden indicar malconfiguraciones

Si vemos 50% de 404s, algo está mal. Si vemos picos de 500s, el servidor está colapsando.

**Resultado esperado:**
```
200    45 accesos (Normales)
404     8 accesos (Recursos no encontrados)
500     2 accesos (Errores del servidor)
```

#### 4. Métodos HTTP más utilizados (Análisis Adicional)

```python
parsed.filter(col("method") != "") \
    .groupBy("method").agg(count("*").alias("cantidad")) \
    .orderBy(desc("cantidad"))
```

**Interpretación:**
- **GET:** Lectura de datos (lo más común)
- **POST:** Envío de datos (formularios, APIs)
- **HEAD:** Verificación sin descargar cuerpo (bots)
- **DELETE/PUT:** Modificación de datos (operaciones peligrosas)

Si vemos muchos DELETEs de un usuario anónimo, es un intento de ataque.

#### 5. Rutas más visitadas (Análisis Adicional)

```python
parsed.filter(col("path") != "") \
    .groupBy("path").agg(count("*").alias("accesos")) \
    .orderBy(desc("accesos"))
```

**Valor práctico:**
- `/index` con 100 accesos es normal
- `/admin` con 100 accesos de IPs diferentes es rojo vivo (intento de fuerza bruta)
- `/api/internal` no debería existir en logs públicos

#### 6. Detección de Anomalías (Análisis Adicional)

Este es el análisis más importante:

```python
error_ips = parsed \
    .filter(col("status_code").isin("400", "401", "403", "404", "500", "502", "503")) \
    .groupBy("ip") \
    .agg(count("*").alias("errores")) \
    .filter(col("errores") > 2)
```

**Qué detectamos:**
- **400 (Bad Request):** Peticiones mal formadas - posible ataque automatizado
- **401/403 (Unauthorized):** Intentos de acceso a recursos protegidos - posible fuerza bruta
- **500/502 (Server Error):** Errores del servidor - podría indicar ataque DoS

Una IP que genera 8 errores en 30 segundos es claramente sospechosa y debe ser investigada.

### Flujo de ejecución real

**Terminal 1 - Iniciar análisis:**
```bash
python3 spark_streaming_logs.py --directory logs_input
```

**Terminal 2 - Generar logs continuamente:**
```bash
python3 generate_logs.py --directory logs_input --batch
```

Spark mostrará análisis actualizados cada 5 segundos, actualizado a medida que llegan nuevos logs.

### Ventajas de esta implementación

1. **Parseado robusto con regex:** Maneja variaciones en formato de logs
2. **Múltiples fuentes:** Archivo o socket, según necesidad
3. **Análisis en tiempo real:** No necesita recargar/reiniciar
4. **Escalable:** Spark distribuye el procesamiento automáticamente
5. **Práctico:** Detecta problemas reales (anomalías de seguridad)

---

## CONCLUSIONES Y REFLEXIÓN

### Conceptos Clave Asimilados

1. **Kafka proporciona garantías de ordering:** Mensajes con la misma clave siempre llegan en el mismo orden a la misma partición. Esto es fundamental para sistemas críticos.

2. **Consumer Groups es conceptualmente elegante:** Múltiples consumidores pueden cooperar automáticamente, repartiéndose el trabajo sin duplicación.

3. **Spark Streaming democratiza el análisis en tiempo real:** Código que escribiría en Scala/SQL normal funciona prácticamente igual en streaming, solo leyendo de fuentes diferentes.

4. **Los esquemas importan:** Avro garantiza estructura - sin él, productores envían datos incompatibles y todo se rompe silenciosamente.

### Dificultades Encontradas

1. **Parseado de logs con regex:** Inicialmente generaba campos vacíos. La solución fue añadir `.filter(col("ip") != "")` para eliminar líneas mal parseadas.

2. **Offsets en Kafka:** Confusion entre offset (posición en la partición) y lag (diferencia con el final). La solución fue leer documentación de Kafka y practicar con `kafka-consumer-groups.sh --describe`.

3. **Memoria en Spark:** Spark Streaming acumula datos en ventanas. La solución fue limitar con `maxFileAge` y `processingTime` para evitar consumo excesivo.

### Reflexión Final

Esta práctica ha sido valiosa porque combine teoría y práctica:
- Teoría: Entender qué es Kafka (plataforma, no herramienta simple)
- Práctica: Ejecutar los comandos reales, ver los errores, solucionarlos

Lo más importante aprendido es que Kafka y Spark Streaming no son magia - son herramientas con tradeoffs claros. Kafka es ordenado pero requiere brokers. Spark es flexible pero usa memoria. El arte está en elegir cuándo usarlas.

Para un caso de ventas en tiempo real (nuestro escenario), Kafka es perfectamente adecuado. Para análisis de logs con detección de anomalías, Spark Streaming brilla. Usados juntos, forman una arquitectura moderna de datos en tiempo real.

---

