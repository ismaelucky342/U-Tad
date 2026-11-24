"""Recepción no bloqueante de mensajes desde un topic de Kafka."""

from __future__ import annotations

import logging
import threading
from uuid import uuid4

from kafka import KafkaConsumer
from reactivex import Observable, create
from reactivex.disposable import Disposable

LOGGER = logging.getLogger(__name__)


class KafkaReceiver:
    """Envoltorio de ``KafkaConsumer`` convertido en un Observable de ReactiveX.

    ``as_observable`` devuelve un flujo que emite cada payload recibido. La
    lectura se hace en un hilo daemon independiente, de modo que el hilo
    principal de Tkinter nunca se queda esperando al bróker.
    """

    def __init__(self, topic: str, bootstrap_servers: str = "localhost:9092") -> None:
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers

    def as_observable(self) -> Observable:
        return create(self._subscribe)

    def _subscribe(self, observer, scheduler) -> Disposable:
        """Arranca el hilo de escucha y devuelve cómo cancelarlo."""
        stopped = threading.Event()
        consumer_ref: list[KafkaConsumer | None] = [None]

        def listen() -> None:
            consumer: KafkaConsumer | None = None
            try:
                # ``group_id=None`` hace que cada instancia reciba todos los
                # mensajes del topic, en lugar de repartirlos con otra instancia
                # del mismo grupo. Es imprescindible para el chat entre dos apps.
                consumer = KafkaConsumer(
                    self.topic,
                    bootstrap_servers=self.bootstrap_servers,
                    auto_offset_reset="latest",
                    enable_auto_commit=True,
                    group_id=None,
                    client_id=f"chat-receptor-{uuid4().hex[:8]}",
                    bootstrap_timeout_ms=5_000,
                    request_timeout_ms=10_000,
                )
                consumer_ref[0] = consumer

                if stopped.is_set():
                    return

                for record in consumer:
                    if stopped.is_set():
                        break
                    if record.value is not None:
                        observer.on_next(record.value)
            except Exception as error:  # bróker caído, topic borrado, etc.
                if not stopped.is_set():
                    LOGGER.error("Error al recibir mensajes de Kafka: %s", error)
                    observer.on_error(error)
            finally:
                if consumer is not None:
                    try:
                        consumer.close()
                    except Exception:
                        LOGGER.debug("No se pudo cerrar el consumidor", exc_info=True)

        def dispose() -> None:
            stopped.set()
            consumer = consumer_ref[0]
            if consumer is not None:
                try:
                    consumer.wakeup()  # desbloquea el bucle de poll()
                except Exception:
                    LOGGER.debug("No se pudo despertar al consumidor", exc_info=True)

        threading.Thread(
            target=listen,
            name=f"kafka-receptor-{self.topic}",
            daemon=True,
        ).start()

        return Disposable(dispose)
