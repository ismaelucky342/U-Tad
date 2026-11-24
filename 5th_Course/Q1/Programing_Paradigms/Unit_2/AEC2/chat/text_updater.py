"""Observer que vuelca las líneas del chat en un widget ``Text`` de Tkinter."""

from __future__ import annotations

import logging
import tkinter as tk

from reactivex.observer import Observer

LOGGER = logging.getLogger(__name__)


class TextUpdater(Observer[str]):
    """Añade cada mensaje recibido al final del historial."""

    def __init__(self, text_widget: tk.Text) -> None:
        super().__init__()
        self._text = text_widget

    def on_next(self, line: str) -> None:
        self._text.configure(state="normal")
        self._text.insert("end", f"{line}\n")
        self._text.see("end")
        self._text.configure(state="disabled")

    def on_error(self, error: Exception) -> None:
        LOGGER.error("Error en el flujo de mensajes: %s", error)

    def on_completed(self) -> None:
        LOGGER.debug("Historial de chat completado")
