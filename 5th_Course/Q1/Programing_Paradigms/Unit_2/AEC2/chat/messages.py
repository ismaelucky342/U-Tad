"""Modelo y funciones puras para serializar y formatear los mensajes de chat."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime

#: Formato solicitado en el enunciado: "fecha-hora usuario: mensaje".
FORMATO_FECHA = "%d/%m/%Y %H:%M:%S"


@dataclass(frozen=True)
class ChatMessage:
    """Mensaje inmutable que viaja por los observables.

    ``id_cliente`` identifica la instancia que escribió el mensaje. Se usa para
    no mostrar dos veces los mensajes propios: la interfaz los pinta en cuanto
    se envían y, además, el consumidor de Kafka los vuelve a recibir.
    """

    usuario: str
    texto: str
    enviado_en: datetime
    id_cliente: str = ""

    def to_payload(self) -> bytes:
        """Convierte el mensaje en el JSON que se publica en Kafka."""
        return json.dumps(
            {
                "usuario": self.usuario,
                "texto": self.texto,
                "enviado_en": self.enviado_en.isoformat(),
                "id_cliente": self.id_cliente,
            },
            ensure_ascii=False,
        ).encode("utf-8")


def format_message(message: ChatMessage) -> str:
    """Función pura que da el formato final que se muestra en el widget Text."""
    fecha = message.enviado_en.strftime(FORMATO_FECHA)
    return f"{fecha} {message.usuario}: {message.texto}"


def _parse_datetime(value: object) -> datetime:
    """Recupera la marca de tiempo del JSON; si no es válida, usa la actual."""
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value)
        except ValueError:
            pass
    return datetime.now()


def message_from_payload(payload: bytes | str) -> ChatMessage:
    """Convierte el payload recibido del bróker en un ``ChatMessage``.

    El formato normal es el JSON que genera :meth:`ChatMessage.to_payload`.
    Si otro productor escribe texto plano en el topic, el mensaje no se pierde:
    se muestra como texto con el usuario ``desconocido`` y la hora de recepción.
    """
    if isinstance(payload, bytes):
        payload = payload.decode("utf-8", errors="replace")

    texto_plano = payload.strip()
    try:
        data = json.loads(texto_plano)
    except (TypeError, ValueError):
        data = None

    if isinstance(data, dict):
        return ChatMessage(
            usuario=str(data.get("usuario") or "desconocido"),
            texto=str(data.get("texto") or ""),
            enviado_en=_parse_datetime(data.get("enviado_en")),
            id_cliente=str(data.get("id_cliente") or ""),
        )

    return ChatMessage(
        usuario="desconocido",
        texto=texto_plano,
        enviado_en=datetime.now(),
        id_cliente="",
    )
