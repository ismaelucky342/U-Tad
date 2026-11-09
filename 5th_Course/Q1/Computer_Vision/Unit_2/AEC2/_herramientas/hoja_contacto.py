"""Hoja de contacto para revisar resultados de un vistazo.

Uso como función desde el banco de pruebas:

    hoja_contacto(
        [ruta_a, ruta_b, ...],
        "outputs/montaje.png",
        titulos=["media 3x3", "mediana 3x3"],
        recorte=(x0, y0, x1, y1),
    )

Uso desde la terminal:

    _trabajo/venv/bin/python _herramientas/hoja_contacto.py salida.png img1 img2 ...
"""

from __future__ import annotations

import sys
from pathlib import Path

import cv2
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def _leer_para_mostrar(ruta: str | Path, recorte: tuple[int, int, int, int] | None) -> np.ndarray:
    img = cv2.imread(str(ruta), cv2.IMREAD_UNCHANGED)
    if img is None:
        raise FileNotFoundError(f"No se puede leer {ruta}")
    if recorte is not None:
        x0, y0, x1, y1 = recorte
        img = img[y0:y1, x0:x1]
    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def hoja_contacto(
    imagenes: list[str | Path],
    salida: str | Path,
    titulos: list[str] | None = None,
    columnas: int = 3,
    ancho_celda: float = 4.2,
    recorte: tuple[int, int, int, int] | None = None,
    dpi: int = 130,
) -> Path:
    """Monta varias imágenes en una rejilla con título y las guarda en PNG."""
    if titulos is None:
        titulos = [Path(p).name for p in imagenes]
    if len(titulos) != len(imagenes):
        raise ValueError("El número de títulos no coincide con el de imágenes")

    filas = int(np.ceil(len(imagenes) / columnas))
    fig, axes = plt.subplots(filas, columnas, figsize=(ancho_celda * columnas, ancho_celda * filas))
    axes = np.atleast_1d(axes).ravel()

    for ax, ruta, titulo in zip(axes, imagenes, titulos):
        img = _leer_para_mostrar(ruta, recorte)
        ax.imshow(img, cmap="gray" if img.ndim == 2 else None)
        ax.set_title(titulo, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])

    for ax in axes[len(imagenes):]:
        ax.axis("off")

    fig.tight_layout()
    salida = Path(salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(salida, dpi=dpi, bbox_inches="tight")
    plt.close(fig)
    return salida


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 1
    hoja_contacto(argv[2:], argv[1])
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
