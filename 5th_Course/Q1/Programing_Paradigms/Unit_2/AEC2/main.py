"""Punto de entrada del chat reactivo con Kafka.

Uso:
    python main.py
    python main.py --bootstrap localhost:9092 --topic chat
"""

from __future__ import annotations

import argparse
import logging
import os
import tkinter as tk

from reactivex.scheduler import ThreadPoolScheduler

from chat.service import ChatService
from chat.tk_scheduler import TkScheduler
from chat.ui import ChatWindow


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Chat reactivo sobre Kafka")
    parser.add_argument(
        "--bootstrap",
        default=os.environ.get("KAFKA_BOOTSTRAP", "localhost:9092"),
        help="Dirección del bróker Kafka (por defecto localhost:9092).",
    )
    parser.add_argument(
        "--topic",
        default=os.environ.get("KAFKA_TOPIC", "chat"),
        help="Topic que se propone al abrir la ventana (por defecto chat).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    root = tk.Tk()
    ui_scheduler = TkScheduler(root)
    # Un pool pequeño basta: la lectura de Kafka usa su propio hilo y el
    # envío se serializa con observe_on.
    io_scheduler = ThreadPoolScheduler(max_workers=4)

    service = ChatService(args.bootstrap, io_scheduler)
    ChatWindow(root, service, ui_scheduler, io_scheduler, args.topic)
    root.mainloop()


if __name__ == "__main__":
    main()
