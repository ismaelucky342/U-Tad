"""Ventana Tkinter del chat. Solo reacciona a los flujos del servicio."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from reactivex import operators as ops
from reactivex.disposable import CompositeDisposable
from reactivex.scheduler.scheduler import Scheduler

from .service import ChatService
from .text_updater import TextUpdater
from .tk_scheduler import TkScheduler


class ChatWindow:
    """Interfaz gráfica: usuario, topic, historial y caja de envío."""

    def __init__(
        self,
        root: tk.Tk,
        service: ChatService,
        ui_scheduler: TkScheduler,
        io_scheduler: Scheduler,
        default_topic: str = "chat",
    ) -> None:
        self._root = root
        self._service = service
        self._ui_scheduler = ui_scheduler
        self._io_scheduler = io_scheduler
        self._disposables = CompositeDisposable()

        self._username_var = tk.StringVar()
        self._topic_var = tk.StringVar(value=default_topic)
        self._message_var = tk.StringVar()
        self._message_entry: ttk.Entry
        self._chat: tk.Text

        self._build_window()
        self._subscribe_to_streams()

        self._root.protocol("WM_DELETE_WINDOW", self._on_close)
        self._set_status("Introduce un usuario y un topic para empezar.")

    def _build_window(self) -> None:
        self._root.title("Chat reactivo con Kafka")
        self._root.geometry("780x560")
        self._root.minsize(600, 420)

        style = ttk.Style(self._root)
        if "clam" in style.theme_names():
            style.theme_use("clam")
        style.configure("Chat.TButton", padding=(10, 5))
        style.configure("Status.TLabel", foreground="#555555")

        contenedor = ttk.Frame(self._root, padding=12)
        contenedor.grid(row=0, column=0, sticky="nsew")
        self._root.rowconfigure(0, weight=1)
        self._root.columnconfigure(0, weight=1)
        contenedor.columnconfigure(1, weight=1)
        contenedor.rowconfigure(1, weight=1)

        # --- Cabecera: usuario, topic y conexión -------------------------
        cabecera = ttk.Frame(contenedor)
        cabecera.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        ttk.Label(cabecera, text="Usuario:").pack(side="left")
        self._username_entry = ttk.Entry(
            cabecera, textvariable=self._username_var, width=16
        )
        self._username_entry.pack(side="left", padx=(6, 16))

        ttk.Label(cabecera, text="Topic:").pack(side="left")
        self._topic_entry = ttk.Entry(cabecera, textvariable=self._topic_var, width=20)
        self._topic_entry.pack(side="left", padx=(6, 12))

        self._connect_button = ttk.Button(
            cabecera,
            text="Conectar",
            style="Chat.TButton",
            command=self._on_connect,
        )
        self._connect_button.pack(side="left")

        # --- Historial de chat -------------------------------------------
        self._chat = tk.Text(
            contenedor,
            height=18,
            width=80,
            wrap="word",
            state="disabled",
            font="TkFixedFont",
            background="#fbfbfb",
            relief="solid",
            borderwidth=1,
        )
        self._chat.grid(row=1, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(
            contenedor, orient="vertical", command=self._chat.yview
        )
        scrollbar.grid(row=1, column=1, sticky="ns")
        self._chat.configure(yscrollcommand=scrollbar.set)

        # --- Caja de envío ----------------------------------------------
        compositor = ttk.Frame(contenedor)
        compositor.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(10, 0))
        compositor.columnconfigure(1, weight=1)

        ttk.Label(compositor, text="Mensaje:").grid(row=0, column=0, padx=(0, 6))
        self._message_entry = ttk.Entry(compositor, textvariable=self._message_var)
        self._message_entry.grid(row=0, column=1, sticky="ew")
        self._message_entry.configure(state="disabled")

        self._send_button = ttk.Button(
            compositor,
            text="Enviar",
            style="Chat.TButton",
            command=self._on_send,
            state="disabled",
        )
        self._send_button.grid(row=0, column=2, padx=(10, 0))

        # --- Barra de estado --------------------------------------------
        self._status_label = ttk.Label(
            contenedor,
            text="",
            style="Status.TLabel",
            anchor="w",
        )
        self._status_label.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(8, 0))

        # Enter envía el mensaje; en la cabecera, Enter conecta.
        self._message_entry.bind("<Return>", self._on_send)
        self._username_entry.bind("<Return>", self._on_connect)
        self._topic_entry.bind("<Return>", self._on_connect)

    def _subscribe_to_streams(self) -> None:
        """La vista se suscribe a los flujos; nunca consulta al bróker."""
        mensajes = self._service.messages.pipe(ops.observe_on(self._ui_scheduler))
        self._disposables.add(mensajes.subscribe(TextUpdater(self._chat)))

        estados = self._service.status.pipe(ops.observe_on(self._ui_scheduler))
        self._disposables.add(
            estados.subscribe(
                on_next=self._set_status,
                on_error=lambda error: self._set_status(f"Error: {error}"),
            )
        )

    def _on_connect(self, event: tk.Event | None = None) -> str:
        if self._service.connected:
            self._service.disconnect()
            self._set_connected(False)
            return "break"

        username = self._username_var.get().strip()
        topic = self._topic_var.get().strip()
        if not username or not topic:
            self._set_status("El usuario y el topic son obligatorios.")
            return "break"

        try:
            self._service.connect(username, topic)
        except Exception as error:
            self._set_status(f"No se pudo conectar: {error}")
            return "break"

        self._set_connected(True)
        self._message_entry.focus_set()
        return "break"

    def _on_send(self, event: tk.Event | None = None) -> str:
        if self._service.send(self._message_var.get()):
            self._message_var.set("")
        self._message_entry.focus_set()
        return "break"

    def _set_connected(self, connected: bool) -> None:
        self._connect_button.configure(text="Desconectar" if connected else "Conectar")
        estado_campos = "disabled" if connected else "normal"
        self._username_entry.configure(state=estado_campos)
        self._topic_entry.configure(state=estado_campos)
        self._message_entry.configure(state="normal" if connected else "disabled")
        self._send_button.configure(state="normal" if connected else "disabled")

    def _set_status(self, text: str) -> None:
        self._status_label.configure(text=text)

    def _on_close(self) -> None:
        self._disposables.dispose()
        self._service.disconnect()
        try:
            self._ui_scheduler.stop()
        except Exception:
            pass
        try:
            self._io_scheduler.executor.shutdown(  # type: ignore[attr-defined]
                wait=False, cancel_futures=True
            )
        except Exception:
            pass
        self._root.destroy()
