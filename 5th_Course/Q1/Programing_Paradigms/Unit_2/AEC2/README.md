# Chat reactivo sobre Apache Kafka

**Autor:** Ismael Hernández  
**Asignatura:** Programación, paradigmas  
**Curso:** 5.º de Ingeniería Informática · U-tad

Aplicación de chat con interfaz Tkinter que envía y recibe mensajes a través de
un topic de Kafka. La recepción, el formato del historial y el envío se
implementan con flujos de **ReactiveX** (`Subject`, `Observable`, `Observer`,
`pipe`, `map`, `filter`, `merge` y `observe_on`), sin bloquear el hilo de la
interfaz.

## Estructura

```text
AEC2/
├── main.py                     # arranque de la aplicación
├── chat/
│   ├── messages.py             # ChatMessage, serialización JSON y formato
│   ├── kafka_receiver.py       # KafkaConsumer -> Observable (hilo propio)
│   ├── kafka_sender.py         # Observer que publica en Kafka
│   ├── service.py              # pipelines de recepción, envío y eco local
│   ├── tk_scheduler.py         # scheduler de Rx que ejecuta en el hilo de Tk
│   ├── text_updater.py         # Observer que escribe en el widget Text
│   └── ui.py                   # ventana Tkinter
├── requirements.txt
├── explicacion_programacion_reactiva.pdf
└── README.md
```

## Requisitos e instalación

Se necesita Python 3.10 o superior y un bróker Kafka accesible en
`localhost:9092`.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Dependencias:

- `reactivex`, para los observables, subjects y operadores.
- `kafka-python`, para el productor y el consumidor de Kafka.
- `tkinter`, incluido en la instalación estándar de Python.

## Arrancar Kafka

La forma más rápida es Docker:

```bash
docker run -d --name kafka -p 9092:9092 apache/kafka:4.1.0
docker exec -it kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 --create --topic chat --if-not-exists
```

También sirve cualquier instalación local de Kafka escuchando en
`localhost:9092`. El topic puede crearse a mano o dejar que Kafka lo cree al
publicar el primer mensaje.

## Ejecución

```bash
python main.py
```

Parámetros opcionales:

```bash
python main.py --bootstrap localhost:9092 --topic chat
```

También se pueden fijar con las variables de entorno `KAFKA_BOOTSTRAP` y
`KAFKA_TOPIC`.

Para probar el chat hay que abrir **dos instancias** de la aplicación:

```bash
# Terminal 1
python main.py --topic chat

# Terminal 2
python main.py --topic chat
```

En cada ventana se escribe un nombre de usuario distinto, el mismo topic, y se
pulsa **Conectar**. A partir de ahí, los mensajes enviados desde una instancia
aparecen en las dos con el formato:

```text
18/11/2026 18:12:24 alice: hola desde alice
18/11/2026 18:12:26 bob: hola desde bob
```

## Cómo se aplica la programación reactiva

### 1. Recepción de mensajes

`KafkaReceiver.as_observable()` envuelve el consumidor en un `Observable` creado
con `reactivex.create`. Al suscribirse arranca un hilo daemon que recorre
`KafkaConsumer` y llama a `observer.on_next(payload)` por cada mensaje. El hilo
de Tkinter no participa en esa espera. El `Disposable` que devuelve la
suscripción marca el hilo como detenido y llama a `consumer.wakeup()` para
desbloquear el `poll()`.

En `ChatService.connect` se construye el pipe de recepción:

```python
incoming = receiver.as_observable().pipe(
    ops.do_action(on_error=self._report_receive_error),
    ops.on_error_resume_next(empty()),
    ops.map(message_from_payload),
    ops.filter(lambda message: message.id_cliente != self._sender_id),
)
```

- `map(message_from_payload)` convierte el JSON de Kafka en un `ChatMessage`.
- `filter` descarta el eco del propio cliente: el mensaje ya se pintó al
  enviarlo y el consumidor lo vuelve a recibir del bróker.
- `do_action` + `on_error_resume_next` informan de un error de recepción sin
  cancelar el flujo de la interfaz.

Después, el pipe de presentación añade el formato solicitado antes de notificar
a la vista:

```python
display = merge(incoming, self._outgoing).pipe(ops.map(format_message))
```

`merge` une los mensajes recibidos y los enviados localmente, de modo que el
historial muestra ambos. `format_message` es una función pura que produce
`"fecha-hora usuario: mensaje"`. Finalmente, `ChatService.messages` (un
`Subject`) notifica al observer `TextUpdater`, que escribe en el widget `Text`.

La vista se suscribe con `observe_on(TkScheduler)`:

```python
mensajes = service.messages.pipe(ops.observe_on(ui_scheduler))
mensajes.subscribe(TextUpdater(text_widget))
```

`TkScheduler` guarda las acciones en una cola segura entre hilos y las ejecuta
con `root.after`, dentro del hilo de `mainloop`. Así se cumple la regla de
Tkinter de tocar los widgets solo desde el hilo principal.

### 2. Envío de mensajes

La interfaz no escribe en Kafka directamente. Al pulsar **Enviar**, `send()`
crea un `ChatMessage` y lo emite en el `Subject` `_outgoing`:

```python
self._outgoing.on_next(ChatMessage(...))
```

Dos pipelines se suscriben a ese Subject:

```python
# Envío real, fuera del hilo de la interfaz
sending = self._outgoing.pipe(ops.observe_on(io_scheduler))
sending.subscribe(sender)

# Eco local para que el mensaje aparezca inmediatamente
display = merge(incoming, self._outgoing).pipe(ops.map(format_message))
```

`KafkaSender` es un `Observer[ChatMessage]`: ReactiveX le notifica cada mensaje
pendiente mediante `on_next`. Dentro de ese método crea (la primera vez) el
`KafkaProducer` y publica el payload; `future.get()` espera la confirmación del
bróker, igual que el `flush()` del enunciado. Como la suscripción usa
`observe_on(ThreadPoolScheduler)`, esa espera ocurre en un hilo de E/S y la
ventana sigue respondiendo. `prepare()` crea el productor al conectar, también
en segundo plano, para detectar antes los problemas de conexión.

Cada mensaje incluye un `id_cliente` aleatorio por instancia y la marca de
tiempo. El receptor descarta los mensajes con su propio `id_cliente`, de modo
que el eco local no se duplica cuando Kafka devuelve el mensaje.

## Formato del mensaje en Kafka

El payload es un JSON en UTF-8:

```json
{
  "usuario": "alice",
  "texto": "hola",
  "enviado_en": "2026-11-18T18:12:24.123456",
  "id_cliente": "3f2c..."
}
```

Si otro productor escribe texto plano en el topic, el receptor no falla: lo
muestra con el usuario `desconocido` y la hora de recepción.

## Decisiones y limitaciones

- El consumidor usa `group_id=None` para que **cada instancia reciba todos los
  mensajes**; con un grupo compartido, Kafka repartiría las particiones entre
  las dos ventanas.
- `auto_offset_reset="latest"` hace que solo se muestren los mensajes que llegan
  después de conectar.
- No se gestionan nombres de usuario repetidos, mensajes muy largos ni
  caracteres no ASCII, tal como indica el enunciado.
- Si el bróker no está disponible, la barra de estado muestra el error; el resto
  de la interfaz sigue funcionando y se puede reintentar la conexión.
