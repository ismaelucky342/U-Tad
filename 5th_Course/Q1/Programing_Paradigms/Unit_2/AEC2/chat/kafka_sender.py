"""Envío de mensajes a Kafka como Observer de ReactiveX."""

from __future__ import annotations

import logging
import threading
from collections.abc import Callable

from kafka import KafkaProducer
from reactivex.observer import Observer

from .messages import ChatMessage

LOGGER = logging.getLogger(__name__)


class KafkaSender(Observer[ChatMessage]):
    """Observer que recibe los mensajes pendientes y los publica en Kafka.

    El productor se crea de forma perezosa dentro del hilo de envío: así el
    constructor no bloquea la interfaz aunque el bróker tarde en responder.
    """

    def __init__(
        self,
        topic: str,
        bootstrap_servers: str = "localhost:9092",
        on_error: Callable[[Exception], None] | None = None,
    ) -> None:
        super().__init__()
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers
        self._on_error = on_error or (lambda error: LOGGER.error("%s", error))
        self._producer: KafkaProducer | None = None
        self._lock = threading.Lock()

    def prepare(self) -> None:
        """Crea el productor con antelación, fuera del hilo de la interfaz."""
        try:
            with self._lock:
                self._get_producer()
        except Exception as error:
            self._on_error(error)

    def on_next(self, message: ChatMessage) -> None:
        """Publica el mensaje y espera la confirmación del bróker."""
        try:
            producer = self._get_producer()
            future = producer.send(self.topic, message.to_payload())
            future.get(timeout=10)  # equivale al flush(): fuerza el envío ahora
            LOGGER.debug("Mensaje enviado a %s", self.topic)
        except Exception as error:
            # Un fallo de envío no debe cancelar el flujo de mensajes pendientes.
            self._on_error(error)

    def on_error(self, error: Exception) -> None:
        self._on_error(error)
        self.close()

    def on_completed(self) -> None:
        self.close()

    def close(self) -> None:
        with self._lock:
            producer, self._producer = self._producer, None
        if producer is None:
            return
        try:
            producer.flush(timeout=5)
        except Exception:
            LOGGER.debug("No se pudo vaciar el productor", exc_info=True)
        try:
            producer.close(timeout=5)
        except Exception:
            LOGGER.debug("No se pudo cerrar el productor", exc_info=True)

    def _get_producer(self) -> KafkaProducer:
        """Crea el ``KafkaProducer`` la primera vez que se necesita."""
        if self._producer is None:
            self._producer = KafkaProducer(
                bootstrap_servers=self.bootstrap_servers,
                value_serializer=lambda value: (
                    value if isinstance(value, bytes) else str(value).encode("utf-8")
                ),
                acks="all",
                retries=3,
                linger_ms=0,
                request_timeout_ms=10_000,
                max_block_ms=10_000,
                bootstrap_timeout_ms=5_000,
            )
        return self._producer
