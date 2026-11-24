"""Scheduler de ReactiveX que ejecuta las notificaciones en el hilo de Tkinter.

Tkinter no es seguro entre hilos: solo el hilo que ejecuta ``mainloop`` puede
tocar los widgets. Este scheduler recibe las acciones desde cualquier hilo,
las guarda en una cola y las ejecuta con ``root.after``, es decir, dentro del
hilo principal. Así los operadores ``observe_on`` pueden actualizar la interfaz
sin bloquearla ni provocar errores de concurrencia.
"""

from __future__ import annotations

import heapq
import itertools
import threading
import time
import tkinter as tk
import traceback
from collections.abc import Callable
from datetime import datetime, timezone
from typing import Any

from reactivex.disposable import Disposable, SingleAssignmentDisposable
from reactivex.scheduler.scheduler import Scheduler

Action = Callable[[Scheduler, Any], Any]


class TkScheduler(Scheduler):
    """Ejecuta las acciones pendientes en el hilo que creó la ventana Tk."""

    def __init__(self, root: tk.Misc, tick_ms: int = 20) -> None:
        self._root = root
        self._tick_ms = tick_ms
        self._heap: list[tuple[float, int, Callable[[], None]]] = []
        self._counter = itertools.count()
        self._lock = threading.Lock()
        self._running = True
        self._after_id: str | None = self._root.after(tick_ms, self._drain)

    def schedule(self, action: Action, state: Any = None) -> Disposable:
        return self._enqueue(0.0, action, state)

    def schedule_relative(
        self, duetime: Any, action: Action, state: Any = None
    ) -> Disposable:
        return self._enqueue(max(0.0, self.to_seconds(duetime)), action, state)

    def schedule_absolute(
        self, duetime: Any, action: Action, state: Any = None
    ) -> Disposable:
        if isinstance(duetime, datetime):
            momento = duetime
            if momento.tzinfo is None:
                momento = momento.replace(tzinfo=timezone.utc)  # noqa: UP017
            delay = (momento - self.now).total_seconds()
        else:
            delay = float(duetime) - self.now.timestamp()
        return self._enqueue(max(0.0, delay), action, state)

    def stop(self) -> None:
        """Detiene el temporizador; se llama al cerrar la ventana."""
        self._running = False
        if self._after_id is not None:
            try:
                self._root.after_cancel(self._after_id)
            except tk.TclError:
                pass
            self._after_id = None

    def _enqueue(self, delay: float, action: Action, state: Any) -> Disposable:
        cancelable = SingleAssignmentDisposable()

        def run() -> None:
            if cancelable.is_disposed:
                return
            cancelable.disposable = self.invoke_action(action, state)

        with self._lock:
            heapq.heappush(
                self._heap,
                (time.monotonic() + delay, next(self._counter), run),
            )
        return cancelable

    def _drain(self) -> None:
        ahora = time.monotonic()
        listas: list[Callable[[], None]] = []
        with self._lock:
            while self._heap and self._heap[0][0] <= ahora:
                listas.append(heapq.heappop(self._heap)[2])

        for run in listas:
            try:
                run()
            except Exception:  # una acción rota no debe parar la interfaz
                traceback.print_exc()

        if not self._running:
            return
        try:
            self._after_id = self._root.after(self._tick_ms, self._drain)
        except tk.TclError:
            self._running = False
