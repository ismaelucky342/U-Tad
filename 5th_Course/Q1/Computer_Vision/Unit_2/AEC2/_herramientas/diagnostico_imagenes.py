"""Diagnóstico de las tres imágenes de partida y versión de trabajo.

Genera:
    _trabajo/diagnostico_originales.csv
    _trabajo/manifest_imagenes.json
    _trabajo/versiones_trabajo/IMG_0x_trabajo.png
    _trabajo/imagenes_candidatas/contacto_originales.jpg
    _trabajo/imagenes_candidatas/contacto_trabajo.jpg

Uso:
    _trabajo/venv/bin/python _herramientas/diagnostico_imagenes.py
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import cv2
import numpy as np
import pandas as pd
from skimage.measure import shannon_entropy

from hoja_contacto import hoja_contacto

RAIZ = Path(__file__).resolve().parents[1]
ENT = RAIZ / "U2_Practica_Hernandez_Ismael"
DATA = ENT / "data"
OUT = ENT / "outputs"
TRABAJO = RAIZ / "_trabajo"
VERSIONES = TRABAJO / "versiones_trabajo"
CANDIDATAS = TRABAJO / "imagenes_candidatas"

LADO_MAYOR = 512
KERNEL_LAPLACIANO = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]], dtype=np.float64)
UMBRAL_GRADIENTE = 10.0

FUENTES = {
    "IMG_01.jpg": {
        "rol": "textura_fina",
        "titulo": "Close up of dense green foliage hedge",
        "autor": "A S M Jobaer",
        "licencia": "CC BY-SA 4.0",
        "ficha": "https://commons.wikimedia.org/wiki/File:Close_up_of_dense_green_foliage_hedge.jpg",
        "url_original": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Close_up_of_dense_green_foliage_hedge.jpg",
    },
    "IMG_02.jpg": {
        "rol": "regiones_uniformes",
        "titulo": "Apple With White Background",
        "autor": "Karl Thomas Moore (Karlfonza)",
        "licencia": "CC BY-SA 4.0",
        "ficha": "https://commons.wikimedia.org/wiki/File:Apple_With_White_Background.jpg",
        "url_original": "https://upload.wikimedia.org/wikipedia/commons/1/13/Apple_With_White_Background.jpg",
    },
    "IMG_03.jpg": {
        "rol": "ruido_real",
        "titulo": "Image noise in low light sample (Canon 100D) at ISO 6400",
        "autor": "Rodrigo.Argenton",
        "licencia": "CC BY-SA 4.0",
        "ficha": "https://commons.wikimedia.org/wiki/File:Image_noise_in_low_light_sample_(Canon_100D)_at_ISO_6400.jpg",
        "url_original": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Image_noise_in_low_light_sample_%28Canon_100D%29_at_ISO_6400.jpg",
    },
}


def sha256(ruta: Path) -> str:
    digest = hashlib.sha256()
    with ruta.open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            digest.update(bloque)
    return digest.hexdigest()


def a_gris(img: np.ndarray) -> np.ndarray:
    if img.ndim == 2:
        return img.astype(np.uint8, copy=False)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def version_trabajo(gris: np.ndarray) -> tuple[np.ndarray, float]:
    alto, ancho = gris.shape
    escala = LADO_MAYOR / max(alto, ancho)
    if escala >= 1.0:
        return gris.copy(), 1.0
    nuevo = (max(1, round(ancho * escala)), max(1, round(alto * escala)))
    return cv2.resize(gris, nuevo, interpolation=cv2.INTER_AREA), escala


def diagnostico(gris: np.ndarray) -> dict[str, float]:
    gx = cv2.Sobel(gris, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(gris, cv2.CV_64F, 0, 1, ksize=3)
    magnitud = np.hypot(gx, gy)

    laplaciano = cv2.filter2D(
        gris.astype(np.float64),
        cv2.CV_64F,
        KERNEL_LAPLACIANO,
        borderType=cv2.BORDER_REFLECT_101,
    )
    sigma_mad = float(np.median(np.abs(laplaciano)) / (0.6745 * 6.0))

    return {
        "gradiente_medio": float(magnitud.mean()),
        "gradiente_p95": float(np.percentile(magnitud, 95)),
        "densidad_gradiente": float((magnitud > UMBRAL_GRADIENTE).mean()),
        "sigma_laplaciano_mad": sigma_mad,
        "entropia": float(shannon_entropy(gris)),
        "frac_saturados": float(((gris == 0) | (gris == 255)).mean()),
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    VERSIONES.mkdir(parents=True, exist_ok=True)
    CANDIDATAS.mkdir(parents=True, exist_ok=True)

    filas = []
    manifiesto = {
        "semilla": 20260101,
        "version_trabajo": {
            "lado_mayor": LADO_MAYOR,
            "interpolacion": "INTER_AREA",
            "espacio_de_color": "gris uint8",
            "umbral_densidad_gradiente": UMBRAL_GRADIENTE,
            "estimador_ruido": "median(|Laplaciano|) / (0.6745 * 6)",
        },
        "imagenes": [],
    }
    rutas_originales = []
    rutas_trabajo = []

    for nombre, fuente in FUENTES.items():
        ruta = DATA / nombre
        if not ruta.exists():
            raise FileNotFoundError(f"Falta {ruta}")
        original = cv2.imread(str(ruta), cv2.IMREAD_UNCHANGED)
        if original is None:
            raise ValueError(f"No se puede leer {ruta}")
        gris = a_gris(original)
        trabajo, escala = version_trabajo(gris)
        ruta_trabajo = VERSIONES / f"{Path(nombre).stem}_trabajo.png"
        cv2.imwrite(str(ruta_trabajo), trabajo)
        rutas_originales.append(ruta)
        rutas_trabajo.append(ruta_trabajo)

        diag_original = diagnostico(gris)
        diag_trabajo = diagnostico(trabajo)
        for version, datos, ancho, alto in (
            ("original", diag_original, gris.shape[1], gris.shape[0]),
            ("trabajo", diag_trabajo, trabajo.shape[1], trabajo.shape[0]),
        ):
            fila = {
                "imagen": nombre,
                "version": version,
                "rol": fuente["rol"],
                "ancho": ancho,
                "alto": alto,
                "gradiente_medio": round(datos["gradiente_medio"], 4),
                "gradiente_p95": round(datos["gradiente_p95"], 4),
                "densidad_gradiente": round(datos["densidad_gradiente"], 6),
                "sigma_laplaciano_mad": round(datos["sigma_laplaciano_mad"], 4),
                "entropia": round(datos["entropia"], 4),
                "frac_saturados": round(datos["frac_saturados"], 6),
            }
            filas.append(fila)

        manifiesto["imagenes"].append(
            {
                "archivo": nombre,
                **fuente,
                "sha256": sha256(ruta),
                "tamano_original": [gris.shape[1], gris.shape[0]],
                "tamano_trabajo": [trabajo.shape[1], trabajo.shape[0]],
                "escala_trabajo": round(escala, 6),
                "diagnostico_original": {k: round(v, 6) for k, v in diag_original.items()},
                "diagnostico_trabajo": {k: round(v, 6) for k, v in diag_trabajo.items()},
            }
        )

    df = pd.DataFrame(filas)
    df.to_csv(TRABAJO / "diagnostico_originales.csv", index=False)
    (TRABAJO / "manifest_imagenes.json").write_text(
        json.dumps(manifiesto, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    hoja_contacto(
        rutas_originales,
        CANDIDATAS / "contacto_originales.jpg",
        titulos=[f"{n}\n{FUENTES[n]['rol']}" for n in FUENTES],
    )
    hoja_contacto(
        rutas_trabajo,
        CANDIDATAS / "contacto_trabajo.jpg",
        titulos=[f"{n} · trabajo" for n in FUENTES],
    )

    print(df.to_string(index=False))
    print(f"\nManifiesto: {TRABAJO / 'manifest_imagenes.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
