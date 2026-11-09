"""Comprueba que el entorno de la práctica U2 tiene lo necesario.

Uso:
    _trabajo/venv/bin/python _herramientas/verificar_entorno.py
"""

from __future__ import annotations

import sys

import cv2
import numpy as np
import skimage
from skimage.metrics import peak_signal_noise_ratio, structural_similarity


def main() -> int:
    print(f"Python      {sys.version.split()[0]}")
    print(f"numpy       {np.__version__}")
    print(f"OpenCV      {cv2.__version__}")
    print(f"scikit-image {skimage.__version__}")

    fallos = []
    for nombre, constructor in (
        ("SIFT", cv2.SIFT_create),
        ("ORB", cv2.ORB_create),
        ("FAST", cv2.FastFeatureDetector_create),
    ):
        try:
            detector = constructor()
            print(f"{nombre:11s} OK  {type(detector).__name__}")
        except Exception as exc:  # noqa: BLE001
            fallos.append(f"{nombre}: {exc!r}")
            print(f"{nombre:11s} FALLO  {exc!r}")

    img = np.zeros((64, 64), np.uint8)
    img[20:40, 20:40] = 255
    try:
        assert peak_signal_noise_ratio(img, img, data_range=255) == float("inf")
        assert abs(structural_similarity(
            img,
            img,
            data_range=255,
            gaussian_weights=True,
            sigma=1.5,
            use_sample_covariance=False,
        ) - 1.0) < 1e-12
        print("métricas    OK  PSNR(inf) y SSIM(1) en la identidad")
    except Exception as exc:  # noqa: BLE001
        fallos.append(f"métricas: {exc!r}")
        print(f"métricas    FALLO  {exc!r}")

    if fallos:
        print("\nFallos:")
        for fallo in fallos:
            print(f"  - {fallo}")
        return 1
    print("\nEntorno listo.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
