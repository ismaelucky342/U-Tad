"""Servicio de chat: une la interfaz con los flujos reactivos de Kafka."""

from __future__ import annotations

import logging
from datetime import datetime
from uuid import uuid4

from reactivex import empty, merge
from reactivex import operators as ops
from reactivex.disposable import CompositeDisposable
from reactivex.scheduler.scheduler import Scheduler
from reactivex.subject import Subject

from .kafka_receiver import KafkaReceiver
from .kafka_sender import KafkaSender
from .messages import ChatMessage, format_message, message_from_payload

LOGGER = logging.getLogger(__name__)


class ChatService:
    """Coordina recepción, envío y presentación mediante flujos de ReactiveX.

    Flujos principales:

    * ``_outgoing`` recibe los ``ChatMessage`` que produce la interfaz.
    * ``messages`` emite las líneas ya formateadas que debe mostrar la vista.
    * ``status`` emite avisos para la barra de estado.
    """

    def __init__(
        self,
        bootstrap_servers: str,
        io_scheduler: Scheduler,
    ) -> None:
        self.bootstrap_servers = bootstrap_servers
        self._io_scheduler = io_scheduler

        self._outgoing: Subject[ChatMessage] = Subject()
        self.messages: Subject[str] = Subject()
        self.status: Subject[str] = Subject()

        self._subscriptions = CompositeDisposable()
        self._sender: KafkaSender | None = None
        self._sender_id = ""
        self._username = ""
        self._connected = False

    @property
    def connected(self) -> bool:
        return self._connected

    @property
    def username(self) -> str:
        return self._username

    def connect(self, username: str, topic: str) -> None:
        """Prepara los pipelines de recepción y envío para un topic.

        No lanza la lectura de Kafka en el hilo de la interfaz: el receptor
        arranca su propio hilo y el envío se programa con ``observe_on``.
        """
        username = username.strip()
        topic = topic.strip()
        if not username or not topic:
            raise ValueError("El usuario y el topic no pueden estar vacíos.")

        self.disconnect()

        self._username = username
        self._sender_id = uuid4().hex
        receiver = KafkaReceiver(topic, self.bootstrap_servers)
        sender = KafkaSender(
            topic,
            self.bootstrap_servers,
            on_error=self._report_send_error,
        )
        self._sender = sender

        # Recepción: payload -> ChatMessage -> se descartan los ecos propios.
        # El pipe también da el formato final antes de notificar a la vista.
        incoming = receiver.as_observable().pipe(
            ops.do_action(on_error=self._report_receive_error),
            ops.on_error_resume_next(empty()),
            ops.map(message_from_payload),
            ops.filter(lambda message: message.id_cliente != self._sender_id),
        )

        # La vista recibe los mensajes recibidos y los enviados (eco local).
        display = merge(incoming, self._outgoing).pipe(
            ops.map(format_message),
        )

        # Envío: el Subject avisa a KafkaSender de cada mensaje pendiente.
        # observe_on traslada la escritura a un hilo de E/S.
        sending = self._outgoing.pipe(ops.observe_on(self._io_scheduler))

        self._subscriptions = CompositeDisposable()
        self._subscriptions.add(
            display.subscribe(
                on_next=self.messages.on_next,
                on_error=self._report_receive_error,
            )
        )
        self._subscriptions.add(sending.subscribe(sender))

        self._connected = True
        self.status.on_next(f"Escuchando el topic «{topic}» como {username}")

        # Crea el productor fuera del hilo de Tkinter para avisar pronto de
        # cualquier problema de conexión con el bróker.
        self._io_scheduler.schedule(lambda *_: sender.prepare())

    def send(self, text: str) -> bool:
        """Emite un mensaje al flujo de salida; el envío real es asíncrono."""
        text = text.strip()
        if not self._connected or not text:
            return False

        self._outgoing.on_next(
            ChatMessage(
                usuario=self._username,
                texto=text,
                enviado_en=datetime.now(),
                id_cliente=self._sender_id,
            )
        )
        return True

    def disconnect(self) -> None:
        """Cancela los pipelines y cierra el consumidor y el productor."""
        was_connected = self._connected
        self._connected = False
        self._subscriptions.dispose()
        self._subscriptions = CompositeDisposable()

        sender, self._sender = self._sender, None
        self._sender_id = ""
        if sender is not None:
            # Cerrar el productor puede tardar; se hace en el hilo de E/S.
            try:
                self._io_scheduler.schedule(lambda *_: sender.close())
            except RuntimeError:
                sender.close()

        if was_connected:
            self.status.on_next("Desconectado")

    def _report_send_error(self, error: Exception) -> None:
        LOGGER.error("Error al enviar: %s", error)
        self.status.on_next(f"Error al enviar: {error}")

    def _report_receive_error(self, error: Exception) -> None:
        LOGGER.error("Error al recibir: %s", error)
        self.status.on_next(f"Error al recibir: {error}")
