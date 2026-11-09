# %% [markdown]
# # Medir el filtrado y la repetibilidad de los detectores
#
# Este es mi banco de pruebas de la práctica individual de Visión por Computador (U2).
# El cuaderno y el script son el mismo código; las celdas escriben los CSV y las figuras en
# `outputs/`. Busco la raíz desde el directorio actual o desde sus padres, así que me funciona
# tanto desde la raíz de la entrega como desde `codigo/`.
#
# **Requisitos:** dejo las versiones fijadas en `codigo/requirements.txt`. No instalo nada dentro
# del cuaderno. La ejecución completa me tarda alrededor de un minuto y medio y no toca `data/`.
#
# **Orden:** primero defino el núcleo compartido; después, las celdas de cada ejercicio; al final,
# una única celda lanza todo el banco y muestra las formas de las tablas que he generado.

"""Banco de pruebas de la práctica U2.

Aquí reúno las funciones y, más abajo, las celdas que generan mis resultados.
Lo puedo ejecutar como script desde la carpeta de la entrega o abrir como
cuaderno; las dos vías comparten este mismo código.
"""

# %%
from __future__ import annotations

import hashlib
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from skimage.metrics import peak_signal_noise_ratio, structural_similarity


def _detectar_raiz() -> Path:
    candidatos = [Path.cwd().resolve(), (Path.cwd() / "U2_Practica_Hernandez_Ismael").resolve()]
    for candidato in candidatos:
        if (candidato / "data").is_dir() and (candidato / "codigo").is_dir():
            return candidato
    for base in [Path.cwd(), *Path.cwd().parents]:
        if (base / "data").is_dir() and (base / "codigo").is_dir():
            return base
    try:
        aqui = Path(__file__).resolve()
    except NameError:
        aqui = None
    if aqui is not None:
        for padre in [aqui.parent, *aqui.parents]:
            if (padre / "data").is_dir() and (padre / "codigo").is_dir():
                return padre
    raise RuntimeError("No encuentro la raíz de la entrega (data/ y codigo/).")


BASE = _detectar_raiz()
DATA = BASE / "data"
OUT = BASE / "outputs"

SEMILLA = 20260101
SEMILLA_AUX = 20260102
IMAGENES = ["IMG_01.jpg", "IMG_02.jpg", "IMG_03.jpg"]
KERNEL_LAPLACIANO = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]], dtype=np.float64)


def sigma_laplaciano(img: np.ndarray) -> float:
    laplaciano = cv2.filter2D(
        img.astype(np.float64), cv2.CV_64F, KERNEL_LAPLACIANO, borderType=BORDE
    )
    return float(np.median(np.abs(laplaciano)) / (0.6745 * 6.0))
BORDE = cv2.BORDER_REFLECT_101
LADO_MAYOR = 512
TOL_CANNY = 2
TOL_REPETIBILIDAD = 3.0

HASHES = {
    "IMG_01.jpg": "348fd88c0e99ab0ee66a5fe01c3d662646354712a4b353dc2c06a24cbc70ba4b",
    "IMG_02.jpg": "f739e66c8ab29da3848c5bcf1218fd42ffe13ab0cb5eebdb4cbdb338ad54a00b",
    "IMG_03.jpg": "050b7bcabe09732e7aa3141c863d04f8692002cf36977da435c6e39456a6f0ff",
}


def sha256(ruta: Path) -> str:
    digest = hashlib.sha256()
    with Path(ruta).open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            digest.update(bloque)
    return digest.hexdigest()


def verificar_hashes(data_dir: Path = DATA) -> None:
    for nombre, esperado in HASHES.items():
        ruta = Path(data_dir) / nombre
        if not ruta.exists():
            raise FileNotFoundError(f"Falta {ruta}")
        obtenido = sha256(ruta)
        if obtenido != esperado:
            raise ValueError(f"Hash distinto para {nombre}: {obtenido} != {esperado}")


def cargar_gris(ruta: Path, lado_mayor: int = LADO_MAYOR) -> np.ndarray:
    img = cv2.imread(str(ruta), cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"No se puede leer {ruta}")
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    alto, ancho = gris.shape
    escala = lado_mayor / max(alto, ancho)
    if escala < 1.0:
        nuevo = (max(1, round(ancho * escala)), max(1, round(alto * escala)))
        gris = cv2.resize(gris, nuevo, interpolation=cv2.INTER_AREA)
    return gris


def recorte_cuadrado(img: np.ndarray) -> np.ndarray:
    alto, ancho = img.shape[:2]
    lado = min(alto, ancho)
    y0 = (alto - lado) // 2
    x0 = (ancho - lado) // 2
    return img[y0:y0 + lado, x0:x0 + lado]


def rng_celda(semilla: int, idx_imagen: int, idx_condicion: int) -> np.random.Generator:
    return np.random.default_rng(np.random.SeedSequence([semilla, idx_imagen, idx_condicion]))


def ruido_sal_pimienta(img: np.ndarray, p: float, rng: np.random.Generator) -> np.ndarray:
    out = img.copy()
    n = int(p * img.size)
    filas = rng.integers(0, img.shape[0], n)
    cols = rng.integers(0, img.shape[1], n)
    out[filas, cols] = rng.choice([0, 255], size=n)
    return out


def ruido_gaussiano(img: np.ndarray, sigma: float, rng: np.random.Generator) -> np.ndarray:
    perturbacion = rng.normal(0, sigma, img.shape)
    return np.clip(img.astype(np.float32) + perturbacion, 0, 255).astype(np.uint8)


def ruido_gaussiano_con_detalle(
    img: np.ndarray, sigma: float, rng: np.random.Generator
) -> tuple[np.ndarray, float, float]:
    perturbacion = rng.normal(0, sigma, img.shape)
    sin_recortar = img.astype(np.float32) + perturbacion
    out = np.clip(sin_recortar, 0, 255).astype(np.uint8)
    sigma_empirico = float((out.astype(np.float32) - img.astype(np.float32)).std())
    fraccion_recortada = float(((sin_recortar < 0) | (sin_recortar > 255)).mean())
    return out, sigma_empirico, fraccion_recortada


def psnr(referencia: np.ndarray, salida: np.ndarray) -> float:
    if np.array_equal(referencia, salida):
        return float("inf")
    return float(peak_signal_noise_ratio(referencia, salida, data_range=255))


def ssim(referencia: np.ndarray, salida: np.ndarray) -> float:
    return float(
        structural_similarity(
            referencia,
            salida,
            data_range=255,
            gaussian_weights=True,
            sigma=1.5,
            use_sample_covariance=False,
        )
    )


def _ventanas(img: np.ndarray, k: int) -> np.ndarray:
    r = k // 2
    pad = np.pad(img, r, mode="reflect")
    return np.lib.stride_tricks.sliding_window_view(pad, (k, k))


def mediana_propia(img: np.ndarray, k: int) -> np.ndarray:
    win = _ventanas(img, k)
    return np.median(win, axis=(-1, -2)).astype(np.uint8)


def mediana_hibrida(img: np.ndarray, k: int) -> np.ndarray:
    r = k // 2
    win = _ventanas(img, k)
    fila = win[:, :, r, :]
    columna = win[:, :, :, r]
    cruz = np.concatenate([fila, columna], axis=-1)
    diag1 = np.stack([win[:, :, i, i] for i in range(k)], axis=-1)
    diag2 = np.stack([win[:, :, i, k - 1 - i] for i in range(k)], axis=-1)
    diagonales = np.concatenate([diag1, diag2], axis=-1)
    m_cruz = np.median(cruz, axis=-1)
    m_diag = np.median(diagonales, axis=-1)
    centro = win[:, :, r, r]
    out = np.median(np.stack([m_cruz, m_diag, centro], axis=-1), axis=-1)
    return np.rint(out).astype(np.uint8)


def media_recortada(img: np.ndarray, k: int, alpha: float) -> np.ndarray:
    win = _ventanas(img, k)
    plano = win.reshape(img.shape[0], img.shape[1], k * k)
    plano = np.sort(plano, axis=-1)
    m = int(np.floor(alpha * k * k))
    if k * k - 2 * m < 1:
        raise ValueError(f"Recorte demasiado agresivo: k={k}, alpha={alpha}")
    out = plano[:, :, m:k * k - m].mean(axis=-1)
    return np.rint(out).astype(np.uint8)


def mediana_truncada_literal(img: np.ndarray, k: int, alpha: float) -> np.ndarray:
    win = _ventanas(img, k)
    plano = win.reshape(img.shape[0], img.shape[1], k * k)
    plano = np.sort(plano, axis=-1)
    m = int(np.floor(alpha * k * k))
    out = np.median(plano[:, :, m:k * k - m], axis=-1)
    return np.rint(out).astype(np.uint8)


def filtro_media(img: np.ndarray, k: int) -> np.ndarray:
    return cv2.blur(img, (k, k), borderType=BORDE)


def filtro_gaussiano(img: np.ndarray, sigma: float, k: int) -> np.ndarray:
    return cv2.GaussianBlur(img, (k, k), sigmaX=sigma, sigmaY=sigma, borderType=BORDE)


def filtro_bilateral(img: np.ndarray, d: int, sigma_color: float, sigma_space: float) -> np.ndarray:
    return cv2.bilateralFilter(img, d, sigma_color, sigma_space, borderType=BORDE)


def aplicar_filtro(nombre: str, img: np.ndarray, parametros: dict) -> np.ndarray:
    if nombre == "media":
        return filtro_media(img, int(parametros["k"]))
    if nombre == "gaussiano":
        return filtro_gaussiano(img, float(parametros["sigma"]), int(parametros["k"]))
    if nombre == "mediana":
        return mediana_propia(img, int(parametros["k"]))
    if nombre == "mediana_hibrida":
        return mediana_hibrida(img, int(parametros["k"]))
    if nombre == "mediana_truncada":
        return media_recortada(img, int(parametros["k"]), float(parametros["alpha"]))
    if nombre == "bilateral_A" or nombre == "bilateral_B":
        return filtro_bilateral(
            img,
            int(parametros["d"]),
            float(parametros["sigma_color"]),
            float(parametros["sigma_space"]),
        )
    raise ValueError(f"Filtro desconocido: {nombre}")


def texto_parametros(nombre: str, parametros: dict) -> str:
    if nombre == "media":
        return f"k={parametros['k']}"
    if nombre == "gaussiano":
        return f"sigma={parametros['sigma']:.1f};k={parametros['k']}"
    if nombre in ("mediana", "mediana_hibrida"):
        return f"k={parametros['k']}"
    if nombre == "mediana_truncada":
        return f"k={parametros['k']};alpha={parametros['alpha']:.1f}"
    if nombre in ("bilateral_A", "bilateral_B"):
        return (
            f"d={parametros['d']};sc={parametros['sigma_color']:.0f};"
            f"ss={parametros['sigma_space']:.0f}"
        )
    return ""


def medir_tiempo(fn, repeticiones: int = 5) -> tuple[float, np.ndarray]:
    fn()
    tiempos = []
    salida = None
    for _ in range(repeticiones):
        t0 = time.perf_counter()
        salida = fn()
        tiempos.append((time.perf_counter() - t0) * 1000.0)
    return float(np.median(tiempos)), salida


def perfil_radial(espectro: np.ndarray) -> np.ndarray:
    alto, ancho = espectro.shape
    cy, cx = alto // 2, ancho // 2
    y, x = np.indices((alto, ancho))
    radio = np.sqrt((x - cx) ** 2 + (y - cy) ** 2).astype(int)
    suma = np.bincount(radio.ravel(), weights=espectro.ravel())
    cuenta = np.bincount(radio.ravel())
    return suma / np.maximum(cuenta, 1)


def espectro_imagen(img: np.ndarray) -> np.ndarray:
    cuadrado = recorte_cuadrado(img).astype(np.float32)
    lado = cuadrado.shape[0]
    ventana = np.outer(np.hanning(lado), np.hanning(lado))
    return np.abs(np.fft.fftshift(np.fft.fft2(cuadrado * ventana)))


def espectro_respuesta(nombre: str, parametros: dict, lado: int) -> np.ndarray:
    delta = np.zeros((lado, lado), dtype=np.float32)
    delta[lado // 2, lado // 2] = 1.0
    respuesta = aplicar_filtro(nombre, delta, parametros)
    return np.abs(np.fft.fftshift(np.fft.fft2(respuesta)))


def frecuencia_corte(perfil: np.ndarray, lado: int) -> float:
    if perfil[0] == 0:
        return float("nan")
    p = perfil / perfil[0]
    indices = np.where(p < 0.5)[0]
    if len(indices) == 0:
        return float("nan")
    i1 = int(indices[0])
    if i1 == 0:
        return 0.0
    i0 = i1 - 1
    p0, p1 = float(p[i0]), float(p[i1])
    if p0 == p1:
        return i1 / lado
    r = i0 + (0.5 - p0) * (i1 - i0) / (p1 - p0)
    return float(r / lado)


def contar_rebotes(perfil: np.ndarray, epsilon: float) -> int:
    if perfil[0] == 0:
        return 0
    p = perfil / perfil[0]
    indices = np.where(p < 0.5)[0]
    if len(indices) == 0:
        return 0
    segmento = p[int(indices[0]):]
    picos, _ = find_peaks(segmento, prominence=epsilon)
    return int(len(picos))


def puntuar_bordes(deteccion: np.ndarray, referencia: np.ndarray, tol: int = TOL_CANNY) -> tuple[float, float, float, int]:
    det = deteccion.astype(bool)
    ref = referencia.astype(bool)
    px = int(det.sum())
    if px == 0:
        return 0.0, 0.0, 0.0, 0
    if ref.sum() == 0:
        return 0.0, 0.0, 0.0, px
    dist_ref = cv2.distanceTransform((1 - ref).astype(np.uint8), cv2.DIST_L2, 5)
    precision = float((det & (dist_ref <= tol)).sum() / px)
    dist_det = cv2.distanceTransform((1 - det).astype(np.uint8), cv2.DIST_L2, 5)
    recall = float((ref & (dist_det <= tol)).sum() / ref.sum())
    f1 = 0.0 if precision + recall == 0 else float(2 * precision * recall / (precision + recall))
    return precision, recall, f1, px


def crear_escena_sintetica() -> tuple[np.ndarray, np.ndarray]:
    lado = 512
    img = np.full((lado, lado), 128, dtype=np.uint8)
    referencia = np.zeros((lado, lado), dtype=np.uint8)
    nucleo = np.ones((3, 3), np.uint8)

    def pintar(mask: np.ndarray, intensidad: int) -> None:
        borde = mask & ~cv2.erode(mask, nucleo)
        img[mask == 1] = intensidad
        referencia[:] |= borde

    mask = np.zeros_like(img)
    cv2.rectangle(mask, (50, 50), (190, 170), 1, -1)
    pintar(mask, 210)

    mask = np.zeros_like(img)
    cv2.rectangle(mask, (300, 60), (470, 150), 1, -1)
    pintar(mask, 50)

    mask = np.zeros_like(img)
    cv2.rectangle(mask, (220, 240), (290, 300), 1, -1)
    pintar(mask, 150)

    mask = np.zeros_like(img)
    cv2.circle(mask, (130, 350), 65, 1, -1)
    pintar(mask, 230)

    mask = np.zeros_like(img)
    cv2.circle(mask, (380, 340), 50, 1, -1)
    pintar(mask, 70)

    mask = np.zeros_like(img)
    cv2.line(mask, (40, 470), (240, 430), 1, 3, cv2.LINE_8)
    pintar(mask, 240)

    mask = np.zeros_like(img)
    cv2.line(mask, (280, 480), (480, 440), 1, 3, cv2.LINE_8)
    pintar(mask, 20)

    return img, referencia


def homografia_rotacion(lado: int, grados: float, centro_pixel: bool = True) -> np.ndarray:
    cx = (lado - 1) / 2.0 if centro_pixel else lado / 2.0
    cy = (lado - 1) / 2.0 if centro_pixel else lado / 2.0
    traslacion = np.array([[1, 0, -cx], [0, 1, -cy], [0, 0, 1]], dtype=np.float64)
    traslacion_inv = np.array([[1, 0, cx], [0, 1, cy], [0, 0, 1]], dtype=np.float64)
    a = np.deg2rad(grados)
    rotacion = np.array(
        [[np.cos(a), np.sin(a), 0], [-np.sin(a), np.cos(a), 0], [0, 0, 1]],
        dtype=np.float64,
    )
    return traslacion_inv @ rotacion @ traslacion


def homografia_escala(lado: int, escala: float) -> np.ndarray:
    cx = (lado - 1) / 2.0
    cy = (lado - 1) / 2.0
    traslacion = np.array([[1, 0, -cx], [0, 1, -cy], [0, 0, 1]], dtype=np.float64)
    traslacion_inv = np.array([[1, 0, cx], [0, 1, cy], [0, 0, 1]], dtype=np.float64)
    zoom = np.array([[escala, 0, 0], [0, escala, 0], [0, 0, 1]], dtype=np.float64)
    return traslacion_inv @ zoom @ traslacion


def lut_gamma(gamma: float) -> np.ndarray:
    x = np.arange(256, dtype=np.float64)
    return np.clip(((x / 255.0) ** gamma) * 255.0, 0, 255).round().astype(np.uint8)


def crear_detector(nombre: str):
    if nombre == "FAST":
        return cv2.FastFeatureDetector_create(threshold=25, nonmaxSuppression=True)
    if nombre == "ORB":
        return cv2.ORB_create(
            nfeatures=5000,
            scaleFactor=1.2,
            nlevels=8,
            edgeThreshold=31,
            firstLevel=0,
            WTA_K=2,
            scoreType=cv2.ORB_HARRIS_SCORE,
            patchSize=31,
            fastThreshold=20,
        )
    if nombre == "SIFT":
        return cv2.SIFT_create()
    raise ValueError(f"Detector desconocido: {nombre}")


def repetibilidad(
    img: np.ndarray,
    H: np.ndarray,
    detector,
    tol: float = TOL_REPETIBILIDAD,
    lut: np.ndarray | None = None,
) -> tuple[float, int, int, int]:
    alto, ancho = img.shape[:2]
    img_t = cv2.warpPerspective(
        img, H, (ancho, alto), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0
    )
    if lut is not None:
        img_t = cv2.LUT(img_t, lut)
    kp_orig = detector.detect(img, None)
    kp_trans = detector.detect(img_t, None)
    if not kp_orig or not kp_trans:
        return 0.0, len(kp_orig), len(kp_trans), 0
    pts = np.array([k.pt for k in kp_orig], dtype=np.float32).reshape(-1, 1, 2)
    proyectados = cv2.perspectiveTransform(pts, H).reshape(-1, 2)
    destino = np.array([k.pt for k in kp_trans], dtype=np.float32)
    dentro = (
        (proyectados[:, 0] >= 0)
        & (proyectados[:, 0] < ancho)
        & (proyectados[:, 1] >= 0)
        & (proyectados[:, 1] < alto)
    )
    proyectados = proyectados[dentro]
    if len(proyectados) == 0:
        return 0.0, len(kp_orig), len(kp_trans), 0
    d = np.linalg.norm(proyectados[:, None, :] - destino[None, :, :], axis=2)
    aciertos = int((d.min(axis=1) <= tol).sum())
    return aciertos / len(proyectados), len(kp_orig), len(kp_trans), len(proyectados)


def azar(n_trans: int, lado: int, tol: float = TOL_REPETIBILIDAD) -> float:
    if n_trans == 0:
        return 0.0
    p = 1.0 - (1.0 - np.pi * tol * tol / (lado * lado)) ** n_trans
    return float(np.clip(p, 0.0, 1.0))


# %% [markdown]
# ## 1. Núcleo y Ejercicio 1: rejilla de denoising
#
# Cargo las imágenes, genero el ruido con semilla por celda, aplico los diez filtros y calculo PSNR,
# SSIM y tiempo. En `IMG_03` no tengo referencia limpia: dejo vacías las métricas de fidelidad y la
# analizo con el Laplaciano.

# %% -------------------------------------------------------------------------
# Fase 4: monto la rejilla de denoising
# ---------------------------------------------------------------------------
FILTROS_E1 = [
    ("media", {"k": 3}),
    ("media", {"k": 5}),
    ("gaussiano", {"sigma": 1.0, "k": 7}),
    ("gaussiano", {"sigma": 2.0, "k": 13}),
    ("mediana", {"k": 3}),
    ("mediana", {"k": 5}),
    ("mediana_hibrida", {"k": 3}),
    ("mediana_truncada", {"k": 7, "alpha": 0.2}),
    ("bilateral_A", {"d": 9, "sigma_color": 75, "sigma_space": 5}),
    ("bilateral_B", {"d": 7, "sigma_color": 75, "sigma_space": 5}),
]

CONDICIONES_E1 = [
    ("sal_pimienta", 0.05, "0.05"),
    ("sal_pimienta", 0.10, "0.10"),
    ("sal_pimienta", 0.30, "0.30"),
    ("gaussiano", 10.0, "10"),
    ("gaussiano", 20.0, "20"),
    ("gaussiano", 40.0, "40"),
]


# Aquí genero una sola imagen ruidosa por celda y la comparto entre los diez filtros.
def ejecutar_e1(imagenes: dict[str, np.ndarray], out_dir: Path = OUT):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    filas = []
    aux = []
    reales = []
    for idx_imagen, nombre in enumerate(IMAGENES, start=1):
        limpia = imagenes[nombre]
        for idx_condicion, (tipo, nivel, nivel_texto) in enumerate(CONDICIONES_E1):
            rng = rng_celda(SEMILLA, idx_imagen, idx_condicion)
            if tipo == "sal_pimienta":
                ruidosa = ruido_sal_pimienta(limpia, nivel, rng)
                n_impactos = int(round(nivel * limpia.size))
                impactos_unicos = int((ruidosa != limpia).sum())
                fraccion = impactos_unicos / limpia.size
                sigma_empirico = np.nan
                fraccion_recortada = np.nan
            else:
                ruidosa, sigma_empirico, fraccion_recortada = ruido_gaussiano_con_detalle(
                    limpia, nivel, rng
                )
                n_impactos = np.nan
                impactos_unicos = int((ruidosa != limpia).sum())
                fraccion = impactos_unicos / limpia.size
            aux.append(
                {
                    "imagen": nombre,
                    "tipo_ruido": tipo,
                    "nivel": nivel_texto,
                    "fraccion_alterada": float(fraccion),
                    "sigma_empirico": sigma_empirico,
                    "fraccion_recortada": fraccion_recortada,
                    "n_impactos": n_impactos,
                    "impactos_unicos": impactos_unicos,
                }
            )
            for filtro, parametros in FILTROS_E1:
                tiempo_ms, salida = medir_tiempo(
                    lambda: aplicar_filtro(filtro, ruidosa, parametros)
                )
                if nombre == "IMG_03.jpg":
                    valor_psnr = np.nan
                    valor_ssim = np.nan
                    sigma_in = sigma_laplaciano(ruidosa)
                    sigma_out = sigma_laplaciano(salida)
                    reduccion = (sigma_in - sigma_out) / sigma_in if sigma_in > 0 else 0.0
                    reales.append(
                        {
                            "imagen": nombre,
                            "tipo_ruido": tipo,
                            "nivel": nivel_texto,
                            "filtro": filtro,
                            "parametros": texto_parametros(filtro, parametros),
                            "sigma_laplaciano_entrada": sigma_in,
                            "sigma_laplaciano_salida": sigma_out,
                            "reduccion_sigma": float(reduccion),
                            "mad_cambio": float(
                                np.mean(np.abs(salida.astype(np.float64) - ruidosa.astype(np.float64)))
                            ),
                            "brillo_medio": float(salida.mean()),
                        }
                    )
                else:
                    valor_psnr = float(psnr(limpia, salida))
                    valor_ssim = float(ssim(limpia, salida))
                filas.append(
                    {
                        "imagen": nombre,
                        "tipo_ruido": tipo,
                        "nivel": nivel_texto,
                        "filtro": filtro,
                        "parametros": texto_parametros(filtro, parametros),
                        "psnr": valor_psnr,
                        "ssim": valor_ssim,
                        "tiempo_ms": float(tiempo_ms),
                    }
                )
    df = pd.DataFrame(filas)
    columnas = ["imagen", "tipo_ruido", "nivel", "filtro", "parametros", "psnr", "ssim", "tiempo_ms"]
    df = df[columnas]
    assert len(df) == 3 * 6 * 10, f"E1 debe tener 180 filas, tiene {len(df)}"
    for nombre in IMAGENES:
        sub = df[df["imagen"] == nombre]
        assert len(sub) == 60, f"{nombre}: {len(sub)} filas, se esperaban 60"
        for tipo, _, nivel_texto in CONDICIONES_E1:
            celda = sub[(sub["tipo_ruido"] == tipo) & (sub["nivel"] == nivel_texto)]
            assert len(celda) == 10, f"{nombre}/{tipo}/{nivel_texto}: {len(celda)} filas"
    df.to_csv(out_dir / "resultados_denoising.csv", index=False)
    df_aux = pd.DataFrame(aux)
    df_aux.to_csv(out_dir / "ruido_fraccion_real.csv", index=False)
    df_real = pd.DataFrame(reales)
    columnas_real = [
        "imagen",
        "tipo_ruido",
        "nivel",
        "filtro",
        "parametros",
        "sigma_laplaciano_entrada",
        "sigma_laplaciano_salida",
        "reduccion_sigma",
        "mad_cambio",
        "brillo_medio",
    ]
    df_real = df_real[columnas_real]
    assert len(df_real) == 60, f"IMG_03 debe tener 60 filas, tiene {len(df_real)}"
    df_real.to_csv(out_dir / "analisis_ruido_real.csv", index=False)
    return df, df_aux, df_real


# %% [markdown]
# ## 2. Tablas y figuras del Ejercicio 1
#
# Construyo las tablas de apoyo y las figuras desde `resultados_denoising.csv` y
# `analisis_ruido_real.csv`; aquí no elijo ningún parámetro, solo leo lo que ya está medido.

# %% -------------------------------------------------------------------------
# Fase 4: construyo las tablas y figuras del ejercicio 1
# ---------------------------------------------------------------------------
ETIQUETAS_FILTROS_E1 = [
    "media 3",
    "media 5",
    "gauss σ=1",
    "gauss σ=2",
    "mediana 3",
    "mediana 5",
    "híbrida 3",
    "truncada 7",
    "bilateral A",
    "bilateral B",
]
ETIQUETAS_CONDICIONES_E1 = ["sal 5 %", "sal 10 %", "sal 30 %", "gauss σ=10", "gauss σ=20", "gauss σ=40"]


def _nivel_texto(valor) -> str:
    numero = float(valor)
    if numero < 1.0:
        return f"{numero:.2f}"
    return f"{int(round(numero))}"


def _normalizar_nivel(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["nivel"] = df["nivel"].map(_nivel_texto)
    return df


def tabla_ganadores_e1(df: pd.DataFrame) -> pd.DataFrame:
    df = _normalizar_nivel(df)
    ref = df[df["psnr"].notna()].copy()
    filas = []
    for (imagen, tipo, nivel), sub in ref.groupby(["imagen", "tipo_ruido", "nivel"], sort=False):
        for metrica in ("psnr", "ssim"):
            orden = sub.sort_values([metrica, "tiempo_ms"], ascending=[False, True])
            mejor = orden.iloc[0]
            filas.append(
                {
                    "imagen": imagen,
                    "tipo_ruido": tipo,
                    "nivel": nivel,
                    "metrica": metrica.upper(),
                    "filtro": mejor["filtro"],
                    "parametros": mejor["parametros"],
                    "valor": float(mejor[metrica]),
                    "tiempo_ms": float(mejor["tiempo_ms"]),
                }
            )
    return pd.DataFrame(filas)


def tabla_medianas_vs_medias_e1(df: pd.DataFrame) -> pd.DataFrame:
    df = _normalizar_nivel(df)
    ref = df[df["psnr"].notna()].copy()
    filas = []
    for (imagen, tipo, nivel), sub in ref.groupby(["imagen", "tipo_ruido", "nivel"], sort=False):
        for k in (3, 5):
            med = sub[(sub["filtro"] == "mediana") & (sub["parametros"] == f"k={k}")]
            prom = sub[(sub["filtro"] == "media") & (sub["parametros"] == f"k={k}")]
            if len(med) == 1 and len(prom) == 1:
                filas.append(
                    {
                        "imagen": imagen,
                        "tipo_ruido": tipo,
                        "nivel": nivel,
                        "k": k,
                        "psnr_mediana": float(med["psnr"].iloc[0]),
                        "psnr_media": float(prom["psnr"].iloc[0]),
                        "delta_psnr": float(med["psnr"].iloc[0] - prom["psnr"].iloc[0]),
                        "ssim_mediana": float(med["ssim"].iloc[0]),
                        "ssim_media": float(prom["ssim"].iloc[0]),
                        "delta_ssim": float(med["ssim"].iloc[0] - prom["ssim"].iloc[0]),
                    }
                )
    return pd.DataFrame(filas)


def tabla_bilateral_e1(df: pd.DataFrame) -> pd.DataFrame:
    df = _normalizar_nivel(df)
    ref = df[df["psnr"].notna()].copy()
    filas = []
    for (imagen, tipo, nivel), sub in ref.groupby(["imagen", "tipo_ruido", "nivel"], sort=False):
        gauss = sub[(sub["filtro"] == "gaussiano") & (sub["parametros"] == "sigma=2.0;k=13")]
        if len(gauss) != 1:
            continue
        g = gauss.iloc[0]
        for nombre in ("bilateral_A", "bilateral_B"):
            bil = sub[sub["filtro"] == nombre]
            if len(bil) != 1:
                continue
            b = bil.iloc[0]
            filas.append(
                {
                    "imagen": imagen,
                    "tipo_ruido": tipo,
                    "nivel": nivel,
                    "bilateral": nombre,
                    "delta_ssim": float(b["ssim"] - g["ssim"]),
                    "delta_psnr": float(b["psnr"] - g["psnr"]),
                    "razon_tiempo": float(b["tiempo_ms"] / g["tiempo_ms"]) if g["tiempo_ms"] > 0 else np.nan,
                }
            )
    return pd.DataFrame(filas)


def _matriz_e1(df: pd.DataFrame, imagen: str, metrica: str) -> np.ndarray:
    df = _normalizar_nivel(df)
    sub = df[df["imagen"] == imagen]
    valores = sub[metrica].to_numpy(dtype=float)
    if len(valores) != 60:
        raise ValueError(f"{imagen}: se esperaban 60 filas, hay {len(valores)}")
    return valores.reshape(6, 10)


def _guardar(fig, ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ruta, dpi=200, bbox_inches="tight")
    plt.close(fig)


def figuras_heatmaps_e1(df: pd.DataFrame, df_real: pd.DataFrame, out_dir: Path = OUT) -> None:
    df = _normalizar_nivel(df)
    df_real = _normalizar_nivel(df_real)
    rango = {
        "psnr": (float(np.nanmin(df["psnr"])), float(np.nanmax(df["psnr"]))),
        "ssim": (float(np.nanmin(df["ssim"])), float(np.nanmax(df["ssim"]))),
    }
    for metrica in ("psnr", "ssim"):
        fig, axes = plt.subplots(1, 2, figsize=(13, 5.2), sharey=True)
        for ax, imagen in zip(axes, ["IMG_01.jpg", "IMG_02.jpg"]):
            matriz = _matriz_e1(df, imagen, metrica)
            im = ax.imshow(
                matriz,
                aspect="auto",
                cmap="viridis",
                vmin=rango[metrica][0],
                vmax=rango[metrica][1],
            )
            for i in range(6):
                for j in range(10):
                    valor = matriz[i, j]
                    if np.isfinite(valor):
                        ax.text(j, i, f"{valor:.2f}", ha="center", va="center", fontsize=6.5, color="white")
            ax.set_xticks(range(10), ETIQUETAS_FILTROS_E1, rotation=45, ha="right", fontsize=8)
            ax.set_yticks(range(6), ETIQUETAS_CONDICIONES_E1, fontsize=8)
            ax.set_title(imagen.replace(".jpg", ""), fontsize=10)
        fig.colorbar(im, ax=axes, shrink=0.8, label=metrica.upper())
        fig.suptitle(f"E1 · {metrica.upper()} medio por imagen, ruido y filtro", fontsize=12)
        _guardar(fig, out_dir / "figuras" / f"e1_heatmap_{metrica}.png")

    matriz_rug = _matriz_e1(df_real, "IMG_03.jpg", "sigma_laplaciano_salida")
    fig, ax = plt.subplots(figsize=(7.5, 5.2))
    im = ax.imshow(matriz_rug, aspect="auto", cmap="magma_r")
    for i in range(6):
        for j in range(10):
            ax.text(j, i, f"{matriz_rug[i, j]:.2f}", ha="center", va="center", fontsize=6.5, color="white")
    ax.set_xticks(range(10), ETIQUETAS_FILTROS_E1, rotation=45, ha="right", fontsize=8)
    ax.set_yticks(range(6), ETIQUETAS_CONDICIONES_E1, fontsize=8)
    ax.set_title("IMG_03 · σ del Laplaciano a la salida (sin referencia limpia)", fontsize=10)
    fig.colorbar(im, ax=ax, shrink=0.8, label="σ Laplaciano")
    _guardar(fig, out_dir / "figuras" / "e1_heatmap_rugosidad_IMG_03.png")


def figuras_curvas_e1(df: pd.DataFrame, df_real: pd.DataFrame, out_dir: Path = OUT) -> None:
    df = _normalizar_nivel(df)
    df_real = _normalizar_nivel(df_real)
    colores = plt.cm.tab10(np.linspace(0, 1, 10))
    for metrica in ("psnr", "ssim"):
        fig, axes = plt.subplots(2, 2, figsize=(13, 8), sharey=True)
        for fila, imagen in enumerate(["IMG_01.jpg", "IMG_02.jpg"]):
            for col, tipo in enumerate(["sal_pimienta", "gaussiano"]):
                ax = axes[fila, col]
                sub = df[(df["imagen"] == imagen) & (df["tipo_ruido"] == tipo)]
                for idx, (filtro, parametros) in enumerate(FILTROS_E1):
                    linea = sub[sub["filtro"] == filtro]
                    if filtro in ("media", "gaussiano", "mediana"):
                        linea = linea[linea["parametros"] == texto_parametros(filtro, parametros)]
                    if len(linea) == 0:
                        continue
                    x = linea["nivel"].astype(float).to_numpy()
                    y = linea[metrica].to_numpy(dtype=float)
                    ax.plot(x, y, marker="o", ms=4, lw=1.4, color=colores[idx], label=ETIQUETAS_FILTROS_E1[idx])
                ax.set_xscale("log" if tipo == "sal_pimienta" else "linear")
                ax.set_title(f"{imagen.replace('.jpg','')} · {tipo.replace('_',' ')}", fontsize=10)
                ax.grid(alpha=0.25)
                ax.set_xlabel("nivel")
                ax.set_ylabel(metrica.upper())
        asas, etiquetas = axes[0, 0].get_legend_handles_labels()
        fig.legend(asas, etiquetas, loc="lower center", ncol=5, fontsize=8, frameon=False)
        fig.suptitle(f"E1 · {metrica.upper()} frente al nivel de ruido", fontsize=12)
        fig.tight_layout(rect=[0, 0.08, 1, 0.96])
        _guardar(fig, out_dir / "figuras" / f"e1_curvas_{metrica}.png")

    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5), sharey=True)
    for ax, tipo in zip(axes, ["sal_pimienta", "gaussiano"]):
        sub = df_real[df_real["tipo_ruido"] == tipo]
        for idx, (filtro, parametros) in enumerate(FILTROS_E1):
            linea = sub[sub["filtro"] == filtro]
            if filtro in ("media", "gaussiano", "mediana"):
                linea = linea[linea["parametros"] == texto_parametros(filtro, parametros)]
            if len(linea) == 0:
                continue
            x = linea["nivel"].astype(float).to_numpy()
            y = linea["reduccion_sigma"].to_numpy(dtype=float)
            ax.plot(x, y, marker="o", ms=4, lw=1.4, color=colores[idx], label=ETIQUETAS_FILTROS_E1[idx])
        ax.set_xscale("log" if tipo == "sal_pimienta" else "linear")
        ax.set_title(f"IMG_03 · {tipo.replace('_',' ')}", fontsize=10)
        ax.set_xlabel("nivel")
        ax.set_ylabel("reducción relativa de σ")
        ax.grid(alpha=0.25)
    asas, etiquetas = axes[0].get_legend_handles_labels()
    fig.legend(asas, etiquetas, loc="lower center", ncol=5, fontsize=8, frameon=False)
    fig.suptitle("E1 · IMG_03 · reducción de rugosidad (sin referencia limpia)", fontsize=12)
    fig.tight_layout(rect=[0, 0.12, 1, 0.94])
    _guardar(fig, out_dir / "figuras" / "e1_curvas_rugosidad_IMG_03.png")


def _recorte(img: np.ndarray, r0: int, c0: int, lado: int = 128) -> np.ndarray:
    return img[r0 : r0 + lado, c0 : c0 + lado]


def _panel_recorte(ax, img: np.ndarray, titulo: str) -> None:
    ax.imshow(img, cmap="gray", vmin=0, vmax=255, interpolation="nearest")
    ax.set_title(titulo, fontsize=9)
    ax.axis("off")


def figuras_recortes_e1(imagenes: dict[str, np.ndarray], df: pd.DataFrame, out_dir: Path = OUT) -> None:
    df = _normalizar_nivel(df)
    # En IMG_01 con sal al 10 % el ganador de PSNR es la mediana 3; para la comparación visual elijo el gaussiano σ=2.
    limpia = imagenes["IMG_01.jpg"]
    rng = rng_celda(SEMILLA, 1, 1)
    ruidosa = ruido_sal_pimienta(limpia, 0.10, rng)
    filtros = [
        ("mediana", {"k": 3}),
        ("gaussiano", {"sigma": 2.0, "k": 13}),
        ("mediana_truncada", {"k": 7, "alpha": 0.2}),
    ]
    r0, c0 = 80, 200
    fig, axes = plt.subplots(1, 5, figsize=(18, 4))
    _panel_recorte(axes[0], _recorte(limpia, r0, c0), "limpia")
    _panel_recorte(axes[1], _recorte(ruidosa, r0, c0), "sal 10 %")
    for ax, (filtro, params) in zip(axes[2:], filtros):
        salida = aplicar_filtro(filtro, ruidosa, params)
        fila = df[
            (df["imagen"] == "IMG_01.jpg")
            & (df["tipo_ruido"] == "sal_pimienta")
            & (df["nivel"] == "0.10")
            & (df["filtro"] == filtro)
            & (df["parametros"] == texto_parametros(filtro, params))
        ].iloc[0]
        _panel_recorte(
            axes[2 + filtros.index((filtro, params))],
            _recorte(salida, r0, c0),
            f"{filtro} {fila['parametros']}\nPSNR {fila['psnr']:.2f} · SSIM {fila['ssim']:.4f}",
        )
    fig.suptitle("E1 · IMG_01 · sal y pimienta 10 % · recorte 128×128", fontsize=12, y=1.02)
    fig.tight_layout()
    _guardar(fig, out_dir / "figuras" / "e1_recortes_IMG_01.png")

    # En IMG_03 con gaussiano σ=20 no tengo PSNR/SSIM; comparo a ojo y con la rugosidad.
    ruidosa3 = imagenes["IMG_03.jpg"]
    rng3 = rng_celda(SEMILLA, 3, 4)
    ruidosa3 = ruido_gaussiano_con_detalle(ruidosa3, 20.0, rng3)[0]
    filtros3 = [
        ("mediana", {"k": 3}),
        ("bilateral_A", {"d": 9, "sigma_color": 75, "sigma_space": 5}),
        ("gaussiano", {"sigma": 2.0, "k": 13}),
        ("mediana_truncada", {"k": 7, "alpha": 0.2}),
    ]
    r0, c0 = 250, 340
    fig, axes = plt.subplots(1, 6, figsize=(22, 4))
    _panel_recorte(axes[0], _recorte(imagenes["IMG_03.jpg"], r0, c0), "real")
    _panel_recorte(axes[1], _recorte(ruidosa3, r0, c0), "real + gauss σ=20")
    for idx, (filtro, params) in enumerate(filtros3, start=2):
        salida = aplicar_filtro(filtro, ruidosa3, params)
        _panel_recorte(
            axes[idx],
            _recorte(salida, r0, c0),
            f"{filtro} {texto_parametros(filtro, params)}\nσ salida {sigma_laplaciano(salida):.2f}",
        )
    fig.suptitle("E1 · IMG_03 · ruido real + gaussiano σ=20 · recorte 128×128", fontsize=12, y=1.02)
    fig.tight_layout()
    _guardar(fig, out_dir / "figuras" / "e1_recortes_IMG_03.png")


# %% [markdown]
# ## 3. Ejercicio 2: lectura cuantitativa del espectro
#
# Comparo el perfil de la imagen filtrada con el de la respuesta del filtro. Emparejo caja y
# gaussiano por el corte de la respuesta; el criterio literal lo dejo como control para que se vea
# su degeneración.

# %% -------------------------------------------------------------------------
# Fase 5: comparo los perfiles radiales del ejercicio 2
# ---------------------------------------------------------------------------
CASOS_E2 = [
    ("original", "ninguno"),
    ("caja_3", "k=3"),
    ("caja_5", "k=5"),
    ("caja_9", "k=9"),
    ("gaussiano_0.8", "sigma=0.8;k=7"),
    ("gaussiano_1.6", "sigma=1.6;k=11"),
    ("gaussiano_3.0", "sigma=3.0;k=19"),
]
CAJAS_E2 = ["caja_3", "caja_5", "caja_9"]
GAUSSIANOS_E2 = ["gaussiano_0.8", "gaussiano_1.6", "gaussiano_3.0"]


def _parametros_caso_e2(caso: str) -> tuple[str, dict]:
    if caso == "original":
        return "original", {}
    if caso.startswith("caja_"):
        k = int(caso.split("_")[1])
        return "media", {"k": k}
    if caso.startswith("gaussiano_"):
        sigma = float(caso.split("_")[1])
        k = 2 * int(np.ceil(3 * sigma)) + 1
        return "gaussiano", {"sigma": sigma, "k": k}
    raise ValueError(caso)


def _aplicar_caso_e2(caso: str, img: np.ndarray) -> np.ndarray:
    if caso == "original":
        return img.copy()
    nombre, parametros = _parametros_caso_e2(caso)
    return aplicar_filtro(nombre, img, parametros)


def leer_parametro(nombre: str, out_dir: Path = OUT) -> float:
    df = pd.read_csv(out_dir / "registro_parametros.csv")
    return float(df.loc[df["parametro"] == nombre, "valor"].iloc[0])


# Aquí comparo el corte de la imagen con el de la respuesta; el primero no separa filtros.
def ejecutar_e2(imagenes: dict[str, np.ndarray], out_dir: Path = OUT):
    out_dir = Path(out_dir)
    epsilon = leer_parametro("epsilon_rebotes", out_dir)
    filas = []
    for nombre_imagen, img in imagenes.items():
        cuadrado = recorte_cuadrado(img)
        lado = cuadrado.shape[0]
        for caso, texto in CASOS_E2:
            filtrada = _aplicar_caso_e2(caso, cuadrado)
            perfil_img = perfil_radial(espectro_imagen(filtrada))
            filas.append(
                {
                    "imagen": nombre_imagen,
                    "caso": caso,
                    "parametros": texto,
                    "fuente": "imagen_filtrada",
                    "f_corte": frecuencia_corte(perfil_img, lado),
                    "rebotes": contar_rebotes(perfil_img, epsilon),
                    "ssim_vs_original": float(ssim(cuadrado, filtrada)),
                }
            )
            if caso == "original":
                perfil_resp = np.ones_like(perfil_img)
                corte_resp = np.nan
                rebotes_resp = 0
            else:
                nombre_filtro, parametros = _parametros_caso_e2(caso)
                perfil_resp = perfil_radial(espectro_respuesta(nombre_filtro, parametros, lado))
                corte_resp = frecuencia_corte(perfil_resp, lado)
                rebotes_resp = contar_rebotes(perfil_resp, epsilon)
            filas.append(
                {
                    "imagen": nombre_imagen,
                    "caso": caso,
                    "parametros": texto,
                    "fuente": "respuesta_filtro",
                    "f_corte": corte_resp,
                    "rebotes": rebotes_resp,
                    "ssim_vs_original": np.nan,
                }
            )
    df = pd.DataFrame(filas)
    columnas = ["imagen", "caso", "parametros", "fuente", "f_corte", "rebotes", "ssim_vs_original"]
    df = df[columnas]
    assert len(df) == 3 * 7 * 2, f"E2 debe tener 42 filas, tiene {len(df)}"
    for nombre in imagenes:
        sub = df[df["imagen"] == nombre]
        assert len(sub) == 14, f"{nombre}: {len(sub)} filas, se esperaban 14"
        assert set(sub["caso"]) == {c for c, _ in CASOS_E2}
        assert set(sub["fuente"]) == {"imagen_filtrada", "respuesta_filtro"}
    df.to_csv(out_dir / "perfiles_frecuencia.csv", index=False)

    def _parejas_desde_fuente(fuente: str) -> pd.DataFrame:
        filas = []
        ssim_sub = df[df["fuente"] == "imagen_filtrada"].set_index(["imagen", "caso"])
        for nombre in imagenes:
            sub = df[(df["imagen"] == nombre) & (df["fuente"] == fuente)].set_index("caso")
            for caja in CAJAS_E2:
                corte_caja = float(sub.loc[caja, "f_corte"])
                cortes = {g: float(sub.loc[g, "f_corte"]) for g in GAUSSIANOS_E2}
                deltas = {g: abs(corte_caja - c) for g, c in cortes.items()}
                if max(cortes.values()) - min(cortes.values()) <= 1e-6:
                    gauss = min(GAUSSIANOS_E2, key=lambda g: float(g.split("_")[1]))
                else:
                    minimo = min(deltas.values())
                    empatados = [g for g in GAUSSIANOS_E2 if deltas[g] - minimo <= 1e-9]
                    gauss = min(empatados, key=lambda g: float(g.split("_")[1]))
                corte_gauss = cortes[gauss]
                ssim_caja = float(ssim_sub.loc[(nombre, caja), "ssim_vs_original"])
                ssim_gauss = float(ssim_sub.loc[(nombre, gauss), "ssim_vs_original"])
                filas.append(
                    {
                        "imagen": nombre,
                        "caja": caja,
                        "parametros_caja": sub.loc[caja, "parametros"],
                        "gaussiano": gauss,
                        "parametros_gaussiano": sub.loc[gauss, "parametros"],
                        "f_corte_caja": corte_caja,
                        "f_corte_gaussiano": corte_gauss,
                        "delta_f": abs(corte_caja - corte_gauss),
                        "ssim_caja": ssim_caja,
                        "ssim_gaussiano": ssim_gauss,
                        "delta_ssim": ssim_caja - ssim_gauss,
                    }
                )
        return pd.DataFrame(filas)

    df_parejas = _parejas_desde_fuente("imagen_filtrada")
    df_parejas.to_csv(out_dir / "parejas_caja_gaussiano.csv", index=False)
    df_parejas_resp = _parejas_desde_fuente("respuesta_filtro")
    df_parejas_resp.to_csv(out_dir / "parejas_caja_gaussiano_respuesta.csv", index=False)
    return df, df_parejas, df_parejas_resp


def _perfiles_e2(imagenes: dict[str, np.ndarray], epsilon: float):
    perfiles_img = {}
    perfiles_resp = {}
    for nombre, img in imagenes.items():
        cuadrado = recorte_cuadrado(img)
        lado = cuadrado.shape[0]
        perfiles_img[nombre] = {}
        for caso, _ in CASOS_E2:
            filtrada = _aplicar_caso_e2(caso, cuadrado)
            perfil = perfil_radial(espectro_imagen(filtrada))
            perfiles_img[nombre][caso] = (perfil / perfil[0], lado)
        perfiles_resp[nombre] = {}
        for caso, _ in CASOS_E2:
            if caso == "original":
                perfiles_resp[nombre][caso] = (np.ones_like(perfiles_img[nombre]["original"][0]), lado)
            else:
                nombre_filtro, parametros = _parametros_caso_e2(caso)
                perfil = perfil_radial(espectro_respuesta(nombre_filtro, parametros, lado))
                perfiles_resp[nombre][caso] = (perfil / perfil[0], lado)
    return perfiles_img, perfiles_resp


def figuras_perfiles_e2(df: pd.DataFrame, imagenes: dict[str, np.ndarray], out_dir: Path = OUT) -> None:
    epsilon = leer_parametro("epsilon_rebotes", out_dir)
    perfiles_img, perfiles_resp = _perfiles_e2(imagenes, epsilon)
    colores = {
        "original": "black",
        "caja_3": "#1f77b4",
        "caja_5": "#ff7f0e",
        "caja_9": "#2ca02c",
        "gaussiano_0.8": "#d62728",
        "gaussiano_1.6": "#9467bd",
        "gaussiano_3.0": "#8c564b",
    }
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.8), sharey=True)
    for ax, nombre in zip(axes, imagenes):
        for caso, _ in CASOS_E2:
            perfil, lado = perfiles_img[nombre][caso]
            x = np.arange(len(perfil)) / lado
            ax.plot(x, perfil, lw=1.3, color=colores[caso], label=caso)
            fila = df[(df["imagen"] == nombre) & (df["caso"] == caso) & (df["fuente"] == "imagen_filtrada")]
            corte = float(fila["f_corte"].iloc[0])
            if np.isfinite(corte):
                ax.plot(corte, 0.5, "o", ms=4, color=colores[caso])
        ax.axhline(0.5, color="gray", ls="--", lw=0.8)
        ax.set_xlim(0, 0.5)
        ax.set_yscale("log")
        ax.set_ylim(1e-4, 1.2)
        ax.set_title(nombre.replace(".jpg", ""), fontsize=10)
        ax.set_xlabel("frecuencia (ciclos/píxel)")
        ax.grid(alpha=0.25, which="both")
    axes[0].set_ylabel("magnitud normalizada")
    asas, etiquetas = axes[0].get_legend_handles_labels()
    fig.legend(asas, etiquetas, loc="lower center", ncol=7, fontsize=8, frameon=False)
    fig.suptitle("E2 · perfiles radiales de la imagen filtrada (escala logarítmica)", fontsize=12)
    fig.tight_layout(rect=[0, 0.1, 1, 0.95])
    _guardar(fig, out_dir / "figuras" / "e2_perfiles_imagen.png")

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    colores_resp = {
        "caja_3": "#1f77b4",
        "caja_5": "#ff7f0e",
        "caja_9": "#2ca02c",
        "gaussiano_0.8": "#d62728",
        "gaussiano_1.6": "#9467bd",
        "gaussiano_3.0": "#8c564b",
    }
    nombre_principal = "IMG_01.jpg"
    for ax, (xlim, ylim, titulo) in zip(
        axes,
        [((0, 0.5), (0, 1.05), "completo"), ((0.08, 0.5), (0, 0.05), "zoom de lóbulos")],
    ):
        for caso in CAJAS_E2 + GAUSSIANOS_E2:
            perfil, lado = perfiles_resp[nombre_principal][caso]
            x = np.arange(len(perfil)) / lado
            ax.plot(x, perfil, lw=1.3, color=colores_resp[caso], label=caso)
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_title(titulo, fontsize=10)
        ax.set_xlabel("frecuencia (ciclos/píxel)")
        ax.grid(alpha=0.25)
    axes[0].set_ylabel("magnitud normalizada")
    asas, etiquetas = axes[0].get_legend_handles_labels()
    fig.legend(asas, etiquetas, loc="lower center", ncol=6, fontsize=8, frameon=False)
    fig.suptitle("E2 · respuesta de los seis filtros (IMG_01, lado 341)", fontsize=12)
    fig.tight_layout(rect=[0, 0.1, 1, 0.95])
    _guardar(fig, out_dir / "figuras" / "e2_respuesta_filtros.png")

    df_parejas = pd.read_csv(out_dir / "parejas_caja_gaussiano_respuesta.csv")
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.8), sharey=True)
    nombre = "IMG_01.jpg"
    for ax, caja in zip(axes, CAJAS_E2):
        fila = df_parejas[(df_parejas["imagen"] == nombre) & (df_parejas["caja"] == caja)].iloc[0]
        gauss = fila["gaussiano"]
        for caso, color in ((caja, colores_resp[caja]), (gauss, colores_resp[gauss])):
            perfil, lado = perfiles_resp[nombre][caso]
            x = np.arange(len(perfil)) / lado
            ax.plot(x, perfil, lw=1.5, color=color, label=caso)
            ax.plot(float(fila["f_corte_caja"] if caso == caja else fila["f_corte_gaussiano"]), 0.5, "o", ms=5, color=color)
        ax.axhline(0.5, color="gray", ls="--", lw=0.8)
        ax.set_xlim(0, 0.5)
        ax.set_ylim(0, 1.05)
        ax.set_title(f"{caja} vs {gauss} (respuesta)\nΔSSIM = {fila['delta_ssim']:+.4f}", fontsize=9)
        ax.set_xlabel("frecuencia (ciclos/píxel)")
        ax.grid(alpha=0.25)
    axes[0].set_ylabel("magnitud normalizada")
    asas, etiquetas = axes[0].get_legend_handles_labels()
    fig.legend(asas, etiquetas, loc="lower center", ncol=6, fontsize=8, frameon=False)
    fig.suptitle("E2 · parejas caja/gaussiano por corte de respuesta (IMG_01)", fontsize=12)
    fig.tight_layout(rect=[0, 0.1, 1, 0.95])
    _guardar(fig, out_dir / "figuras" / "e2_parejas_caja_gaussiano.png")


# %% [markdown]
# ## 4. Ejercicio 3: Canny con umbrales por evidencia
#
# Genero la escena sintética y su referencia por código. El barrido mide precisión, exhaustividad
# y F1 con tolerancia de 2 px; después compruebo la estabilidad y describo la transferencia a las
# tres imágenes reales.

# %% -------------------------------------------------------------------------
# Fase 6: monto Canny sobre la escena sintética y la transferencia
# ---------------------------------------------------------------------------
PERCENTILES_CANNY = (70, 75, 80, 85, 90, 95)
FRACCIONES_CANNY = (0.3, 0.4, 0.5, 0.6)


def actualizar_registro(nuevas: list[dict], out_dir: Path = OUT) -> pd.DataFrame:
    ruta = Path(out_dir) / "registro_parametros.csv"
    if ruta.exists():
        df = pd.read_csv(ruta)
    else:
        df = pd.DataFrame(columns=["parametro", "valor", "criterio", "barrido"])
    for fila in nuevas:
        df = df[df["parametro"] != fila["parametro"]]
        df = pd.concat([df, pd.DataFrame([fila])], ignore_index=True)
    df.to_csv(ruta, index=False)
    return df


def magnitud_sobel(img: np.ndarray) -> np.ndarray:
    gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    return np.hypot(gx, gy)


def canny_regla(suave: np.ndarray, percentil: float, fraccion: float) -> tuple[int, int, np.ndarray]:
    magnitud = magnitud_sobel(suave)
    no_nulos = magnitud[magnitud > 0]
    if len(no_nulos) == 0:
        return 1, 1, np.zeros_like(suave, dtype=np.uint8)
    alto = max(1, int(round(float(np.percentile(no_nulos, percentil)))))
    bajo = max(1, int(alto * fraccion))
    det = cv2.Canny(suave, bajo, alto, apertureSize=3, L2gradient=True)
    return alto, bajo, det


# La referencia sale de las primitivas; no uso Canny para fabricarla.
def ejecutar_e3(imagenes: dict[str, np.ndarray], out_dir: Path = OUT):
    out_dir = Path(out_dir)
    sigma = leer_parametro("sigma_suavizado_canny", out_dir)
    escena, referencia = crear_escena_sintetica()
    rng = np.random.default_rng(np.random.SeedSequence([SEMILLA, 3, 0]))
    ruidosa = ruido_gaussiano(escena, 15.0, rng)
    if sigma > 0:
        k = 2 * int(np.ceil(3 * sigma)) + 1
        suave = filtro_gaussiano(ruidosa, sigma, k)
    else:
        suave = ruidosa

    filas = []
    for percentil in PERCENTILES_CANNY:
        for fraccion in FRACCIONES_CANNY:
            alto, bajo, det = canny_regla(suave, percentil, fraccion)
            precision, recall, f1, px = puntuar_bordes(det, referencia, TOL_CANNY)
            filas.append(
                {
                    "percentil_alto": percentil,
                    "fraccion_baja": fraccion,
                    "umbral_alto": alto,
                    "umbral_bajo": bajo,
                    "precision": precision,
                    "recall": recall,
                    "f1": f1,
                    "px_borde": px,
                }
            )
    df = pd.DataFrame(filas)
    df = df.sort_values(["percentil_alto", "fraccion_baja"]).reset_index(drop=True)
    columnas = ["percentil_alto", "fraccion_baja", "umbral_alto", "umbral_bajo", "precision", "recall", "f1", "px_borde"]
    df = df[columnas]
    assert len(df) == 24, f"E3 debe tener 24 filas, tiene {len(df)}"
    assert set(zip(df["percentil_alto"], df["fraccion_baja"])) == {
        (p, f) for p in PERCENTILES_CANNY for f in FRACCIONES_CANNY
    }
    df.to_csv(out_dir / "barrido_canny.csv", index=False)

    optimo = df.sort_values(
        ["f1", "precision", "percentil_alto", "fraccion_baja"],
        ascending=[False, False, False, True],
    ).iloc[0]
    unidad = df[(df["percentil_alto"] == 85) & (df["fraccion_baja"] == 0.5)].iloc[0]
    perdida_abs = float(optimo["f1"] - unidad["f1"])
    perdida_rel = float(perdida_abs / optimo["f1"]) if optimo["f1"] > 0 else float("nan")

    filas_est = []
    for rep in range(10):
        rng_rep = np.random.default_rng(np.random.SeedSequence([SEMILLA, 3, 200 + rep]))
        ruidosa_rep = ruido_gaussiano(escena, 15.0, rng_rep)
        if sigma > 0:
            k = 2 * int(np.ceil(3 * sigma)) + 1
            suave_rep = filtro_gaussiano(ruidosa_rep, sigma, k)
        else:
            suave_rep = ruidosa_rep
        for regla, p, f in (
            ("optimo", int(optimo["percentil_alto"]), float(optimo["fraccion_baja"])),
            ("unidad", 85, 0.5),
        ):
            alto, bajo, det = canny_regla(suave_rep, p, f)
            precision, recall, f1, px = puntuar_bordes(det, referencia, TOL_CANNY)
            filas_est.append(
                {
                    "realizacion": rep,
                    "regla": regla,
                    "precision": precision,
                    "recall": recall,
                    "f1": f1,
                    "umbral_alto": alto,
                    "umbral_bajo": bajo,
                    "px_borde": px,
                }
            )
    df_est = pd.DataFrame(filas_est)
    columnas_est = ["realizacion", "regla", "precision", "recall", "f1", "umbral_alto", "umbral_bajo", "px_borde"]
    df_est = df_est[columnas_est]
    assert len(df_est) == 20, f"Estabilidad debe tener 20 filas, tiene {len(df_est)}"
    df_est.to_csv(out_dir / "estabilidad_canny.csv", index=False)

    filas_trans = []
    for nombre, img in imagenes.items():
        if sigma > 0:
            k = 2 * int(np.ceil(3 * sigma)) + 1
            suave_img = filtro_gaussiano(img, sigma, k)
        else:
            suave_img = img
        reglas = [
            ("optimo_sintetico", int(optimo["umbral_alto"]), int(optimo["umbral_bajo"])),
            ("unidad_sintetica", int(unidad["umbral_alto"]), int(unidad["umbral_bajo"])),
        ]
        alto_opt, bajo_opt, _ = canny_regla(
            suave_img, int(optimo["percentil_alto"]), float(optimo["fraccion_baja"])
        )
        alto_uni, bajo_uni, _ = canny_regla(suave_img, 85, 0.5)
        reglas.append(("percentil_optimo_local", alto_opt, bajo_opt))
        reglas.append(("percentil_unidad_local", alto_uni, bajo_uni))
        for regla, alto, bajo in reglas:
            det = cv2.Canny(suave_img, bajo, alto, apertureSize=3, L2gradient=True)
            px = int(np.count_nonzero(det))
            filas_trans.append(
                {
                    "imagen": nombre,
                    "regla": regla,
                    "umbral_alto": int(alto),
                    "umbral_bajo": int(bajo),
                    "px_borde": px,
                    "frac_borde": float(px / (img.shape[0] * img.shape[1])),
                }
            )
    df_trans = pd.DataFrame(filas_trans)
    columnas_trans = ["imagen", "regla", "umbral_alto", "umbral_bajo", "px_borde", "frac_borde"]
    df_trans = df_trans[columnas_trans]
    assert len(df_trans) == 12, f"Transferencia debe tener 12 filas, tiene {len(df_trans)}"
    df_trans.to_csv(out_dir / "transferencia_canny.csv", index=False)

    actualizar_registro(
        [
            {
                "parametro": "sigma_suavizado_canny",
                "valor": float(sigma),
                "criterio": "maximo mejor F1 en la escena sintetica con semilla auxiliar; desempate menor sigma",
                "barrido": "outputs/barrido_aux_sigma_canny.csv",
            },
            {
                "parametro": "canny_p_optimo",
                "valor": int(optimo["percentil_alto"]),
                "criterio": "maximo F1; desempate precision, percentil alto y fraccion baja",
                "barrido": "outputs/barrido_canny.csv",
            },
            {
                "parametro": "canny_f_optimo",
                "valor": float(optimo["fraccion_baja"]),
                "criterio": "maximo F1; desempate precision, percentil alto y fraccion baja",
                "barrido": "outputs/barrido_canny.csv",
            },
            {
                "parametro": "canny_umbral_alto_optimo",
                "valor": int(optimo["umbral_alto"]),
                "criterio": "umbrales absolutos de la fila optima sintetica",
                "barrido": "outputs/barrido_canny.csv",
            },
            {
                "parametro": "canny_umbral_bajo_optimo",
                "valor": int(optimo["umbral_bajo"]),
                "criterio": "umbrales absolutos de la fila optima sintetica",
                "barrido": "outputs/barrido_canny.csv",
            },
            {
                "parametro": "canny_umbral_alto_unidad",
                "valor": int(unidad["umbral_alto"]),
                "criterio": "regla de la unidad: percentil 85 y fraccion 0.5",
                "barrido": "outputs/barrido_canny.csv",
            },
            {
                "parametro": "canny_umbral_bajo_unidad",
                "valor": int(unidad["umbral_bajo"]),
                "criterio": "regla de la unidad: percentil 85 y fraccion 0.5",
                "barrido": "outputs/barrido_canny.csv",
            },
            {
                "parametro": "canny_perdida_absoluta_f1",
                "valor": perdida_abs,
                "criterio": "F1 optimo - F1 unidad",
                "barrido": "outputs/barrido_canny.csv",
            },
            {
                "parametro": "canny_perdida_relativa_f1",
                "valor": perdida_rel,
                "criterio": "(F1 optimo - F1 unidad) / F1 optimo",
                "barrido": "outputs/barrido_canny.csv",
            },
        ],
        out_dir,
    )
    return df, optimo, unidad, df_est, df_trans


# %% [markdown]
# ## 5. Figuras del Ejercicio 3
#
# Dibujo el barrido, las curvas precisión-exhaustividad, la estabilidad y la transferencia.

# %% -------------------------------------------------------------------------
# Fase 6: dibujo las figuras del ejercicio 3
# ---------------------------------------------------------------------------
def figuras_e3(imagenes: dict[str, np.ndarray], out_dir: Path = OUT) -> None:
    out_dir = Path(out_dir)
    sigma = leer_parametro("sigma_suavizado_canny", out_dir)
    escena, referencia = crear_escena_sintetica()
    rng = np.random.default_rng(np.random.SeedSequence([SEMILLA, 3, 0]))
    ruidosa = ruido_gaussiano(escena, 15.0, rng)
    if sigma > 0:
        k = 2 * int(np.ceil(3 * sigma)) + 1
        suave = filtro_gaussiano(ruidosa, sigma, k)
    else:
        suave = ruidosa

    fig, axes = plt.subplots(1, 4, figsize=(18, 4.6))
    axes[0].imshow(escena, cmap="gray", vmin=0, vmax=255)
    axes[0].set_title("escena limpia")
    axes[1].imshow(escena, cmap="gray", vmin=0, vmax=255)
    overlay = np.zeros((*escena.shape, 3), dtype=np.float32)
    overlay[referencia > 0] = [1.0, 0.0, 0.0]
    axes[1].imshow(overlay, alpha=0.8)
    axes[1].set_title("referencia (rojo)")
    axes[2].imshow(ruidosa, cmap="gray", vmin=0, vmax=255)
    axes[2].set_title("ruidosa σ=15")
    axes[3].imshow(suave, cmap="gray", vmin=0, vmax=255)
    axes[3].set_title(f"suavizada σ={sigma:.1f}")
    for ax in axes:
        ax.axis("off")
    fig.suptitle("E3 · escena sintética y referencia de bordes", fontsize=12)
    fig.tight_layout()
    _guardar(fig, out_dir / "figuras" / "e3_escena.png")

    df = pd.read_csv(out_dir / "barrido_canny.csv")
    df_piv = df.pivot(index="percentil_alto", columns="fraccion_baja", values="f1")
    matriz = df_piv.to_numpy()
    fig, ax = plt.subplots(figsize=(7.5, 5.6))
    im = ax.imshow(matriz, aspect="auto", cmap="viridis", vmin=0, vmax=1)
    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            ax.text(j, i, f"{matriz[i, j]:.3f}", ha="center", va="center", fontsize=8, color="white")
    ax.set_xticks(range(len(df_piv.columns)), [f"{c:.1f}" for c in df_piv.columns])
    ax.set_yticks(range(len(df_piv.index)), [f"{p:.0f}" for p in df_piv.index])
    ax.set_xlabel("fracción baja")
    ax.set_ylabel("percentil alto")
    from matplotlib.patches import Rectangle
    ax.add_patch(Rectangle((2.5, 4.5), 1, 1, fill=False, edgecolor="red", lw=2))
    ax.add_patch(Rectangle((1.5, 2.5), 1, 1, fill=False, edgecolor="white", lw=2))
    ax.text(3.0, 4.82, "óptimo", color="red", ha="center", fontsize=8, fontweight="bold")
    ax.text(2.0, 2.82, "unidad", color="white", ha="center", fontsize=8, fontweight="bold")
    ax.set_title("E3 · F1 de las 24 combinaciones", fontsize=11)
    fig.colorbar(im, ax=ax, shrink=0.8, label="F1")
    _guardar(fig, out_dir / "figuras" / "e3_barrido_f1.png")

    fig, ax = plt.subplots(figsize=(7.8, 5.4))
    for fraccion, etiqueta, color in ((0.5, "principal: f=0,5", "#1f77b4"), (0.6, "secundaria: f=0,6", "#d62728")):
        sub = df[df["fraccion_baja"] == fraccion].sort_values("percentil_alto")
        ax.plot(sub["recall"], sub["precision"], marker="o", ms=5, lw=1.5, color=color, label=etiqueta)
        for _, fila in sub.iterrows():
            ax.annotate(f"{int(fila['percentil_alto'])}", (fila["recall"], fila["precision"]), textcoords="offset points", xytext=(4, 4), fontsize=7)
    opt = df.sort_values(["f1", "precision", "percentil_alto", "fraccion_baja"], ascending=[False, False, False, True]).iloc[0]
    uni = df[(df["percentil_alto"] == 85) & (df["fraccion_baja"] == 0.5)].iloc[0]
    ax.scatter([opt["recall"]], [opt["precision"]], s=180, facecolors="none", edgecolors="red", lw=2, label="óptimo")
    ax.scatter([uni["recall"]], [uni["precision"]], s=180, facecolors="none", edgecolors="black", lw=2, label="unidad")
    ax.set_xlim(0.99, 1.002)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("exhaustividad")
    ax.set_ylabel("precisión")
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8, loc="center left")
    ax.set_title("E3 · precisión–exhaustividad", fontsize=11)
    _guardar(fig, out_dir / "figuras" / "e3_curvas_pr.png")

    est = pd.read_csv(out_dir / "estabilidad_canny.csv")
    medias = est.groupby("regla")[["precision", "recall", "f1"]].mean()
    desv = est.groupby("regla")[["precision", "recall", "f1"]].std()
    fig, ax = plt.subplots(figsize=(7.8, 4.8))
    x = np.arange(3)
    ancho = 0.36
    for k, (regla, color) in enumerate((("optimo", "#2ca02c"), ("unidad", "#d62728"))):
        ax.bar(x + (k - 0.5) * ancho, medias.loc[regla].to_numpy(), ancho, yerr=desv.loc[regla].to_numpy(), capsize=3, color=color, label=regla)
    ax.set_xticks(x, ["precisión", "exhaustividad", "F1"])
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("media ± desviación típica")
    ax.grid(alpha=0.25, axis="y")
    ax.legend(fontsize=8)
    ax.set_title("E3 · estabilidad en 10 realizaciones", fontsize=11)
    _guardar(fig, out_dir / "figuras" / "e3_estabilidad.png")

    trans = pd.read_csv(out_dir / "transferencia_canny.csv")
    for nombre, img in imagenes.items():
        if sigma > 0:
            k = 2 * int(np.ceil(3 * sigma)) + 1
            suave_img = filtro_gaussiano(img, sigma, k)
        else:
            suave_img = img
        fig, axes = plt.subplots(1, 5, figsize=(20, 4.4))
        axes[0].imshow(suave_img, cmap="gray", vmin=0, vmax=255)
        axes[0].set_title(nombre.replace(".jpg", ""), fontsize=10)
        axes[0].axis("off")
        for ax, regla in zip(axes[1:], ["optimo_sintetico", "unidad_sintetica", "percentil_optimo_local", "percentil_unidad_local"]):
            fila = trans[(trans["imagen"] == nombre) & (trans["regla"] == regla)].iloc[0]
            det = cv2.Canny(
                suave_img,
                int(fila["umbral_bajo"]),
                int(fila["umbral_alto"]),
                apertureSize=3,
                L2gradient=True,
            )
            ax.imshow(det, cmap="gray", vmin=0, vmax=255)
            ax.set_title(
                f"{regla}\nalto {int(fila['umbral_alto'])} · bajo {int(fila['umbral_bajo'])} · {100*fila['frac_borde']:.2f} %",
                fontsize=8,
            )
            ax.axis("off")
        fig.suptitle(f"E3 · transferencia · {nombre}", fontsize=12, y=1.02)
        fig.tight_layout()
        _guardar(fig, out_dir / "figuras" / f"e3_transferencia_{nombre.replace('.jpg','')}.png")


# %% [markdown]
# ## 6. Ejercicio 4: repetibilidad de keypoints
#
# Evalúo FAST, ORB y SIFT con rotación, escala e iluminación. Defino la repetibilidad proyectando
# keypoints, con tolerancia de 3 px y recorte de los que se salen del encuadre; calculo el azar por
# densidad. También barro el umbral de FAST, la pirámide de ORB y `tol`.

# %% -------------------------------------------------------------------------
# Fase 7: mido la repetibilidad del ejercicio 4
# ---------------------------------------------------------------------------
TRANSFORMACIONES_E4 = {
    "rotacion": (0.0, 10.0, 20.0, 30.0, 45.0, 60.0, 90.0),
    "escala": (0.5, 0.7, 0.85, 1.0, 1.25, 1.5, 2.0),
    "iluminacion": (0.6, 0.8, 1.0, 1.3, 1.7),
}
DETECTORES_E4 = ("FAST", "ORB", "SIFT")


def _homografia_y_lut(transformacion: str, valor: float, lado: int):
    if transformacion == "rotacion":
        return homografia_rotacion(lado, valor), None
    if transformacion == "escala":
        return homografia_escala(lado, valor), None
    if transformacion == "iluminacion":
        return np.eye(3, dtype=np.float64), lut_gamma(valor)
    raise ValueError(transformacion)


def crear_orb(nlevels: int = 8):
    return cv2.ORB_create(
        nfeatures=5000,
        scaleFactor=1.2,
        nlevels=nlevels,
        edgeThreshold=31,
        firstLevel=0,
        WTA_K=2,
        scoreType=cv2.ORB_HARRIS_SCORE,
        patchSize=31,
        fastThreshold=20,
    )


# Proyecto con la homografía y recorto lo que se sale del encuadre; el azar va aparte.
def ejecutar_e4(imagenes: dict[str, np.ndarray], out_dir: Path = OUT):
    out_dir = Path(out_dir)
    filas = []
    for nombre, img in imagenes.items():
        cuadrado = recorte_cuadrado(img)
        lado = cuadrado.shape[0]
        for nombre_det in DETECTORES_E4:
            detector = crear_detector(nombre_det)
            for transformacion, valores in TRANSFORMACIONES_E4.items():
                for valor in valores:
                    H, lut = _homografia_y_lut(transformacion, valor, lado)
                    rate, n_orig, n_trans, n_valid = repetibilidad(
                        cuadrado, H, detector, TOL_REPETIBILIDAD, lut
                    )
                    filas.append(
                        {
                            "imagen": nombre,
                            "detector": nombre_det,
                            "transformacion": transformacion,
                            "valor": float(valor),
                            "repetibilidad": rate,
                            "n_orig": n_orig,
                            "n_trans": n_trans,
                            "n_validos": n_valid,
                            "tol": TOL_REPETIBILIDAD,
                            "azar": azar(n_trans, lado, TOL_REPETIBILIDAD),
                        }
                    )
    df = pd.DataFrame(filas)
    columnas = [
        "imagen",
        "detector",
        "transformacion",
        "valor",
        "repetibilidad",
        "n_orig",
        "n_trans",
        "n_validos",
        "tol",
        "azar",
    ]
    df = df[columnas]
    assert len(df) == 3 * 3 * 19, f"E4 debe tener 171 filas, tiene {len(df)}"
    for nombre in imagenes:
        sub = df[df["imagen"] == nombre]
        assert len(sub) == 57, f"{nombre}: {len(sub)} filas"
        for det in DETECTORES_E4:
            assert len(sub[sub["detector"] == det]) == 19
        for transformacion, valores in TRANSFORMACIONES_E4.items():
            assert set(sub[sub["transformacion"] == transformacion]["valor"]) == set(valores)
    df.to_csv(out_dir / "repetibilidad.csv", index=False)

    filas_sens = []
    for nombre, img in imagenes.items():
        cuadrado = recorte_cuadrado(img)
        lado = cuadrado.shape[0]
        for umbral in (10, 25, 50):
            detector = cv2.FastFeatureDetector_create(threshold=umbral, nonmaxSuppression=True)
            for escala in TRANSFORMACIONES_E4["escala"]:
                H = homografia_escala(lado, escala)
                rate, n_orig, n_trans, n_valid = repetibilidad(
                    cuadrado, H, detector, TOL_REPETIBILIDAD
                )
                filas_sens.append(
                    {
                        "imagen": nombre,
                        "detector": "FAST",
                        "barrido": "escala",
                        "parametro": "fastThreshold",
                        "valor": umbral,
                        "valor_transformacion": float(escala),
                        "repetibilidad": rate,
                        "n_orig": n_orig,
                        "n_trans": n_trans,
                        "n_validos": n_valid,
                        "tol": TOL_REPETIBILIDAD,
                        "azar": azar(n_trans, lado, TOL_REPETIBILIDAD),
                    }
                )
        for nlevels in (1, 4, 8):
            detector = crear_orb(nlevels)
            for escala in TRANSFORMACIONES_E4["escala"]:
                H = homografia_escala(lado, escala)
                rate, n_orig, n_trans, n_valid = repetibilidad(
                    cuadrado, H, detector, TOL_REPETIBILIDAD
                )
                filas_sens.append(
                    {
                        "imagen": nombre,
                        "detector": "ORB",
                        "barrido": "escala",
                        "parametro": "nlevels",
                        "valor": nlevels,
                        "valor_transformacion": float(escala),
                        "repetibilidad": rate,
                        "n_orig": n_orig,
                        "n_trans": n_trans,
                        "n_validos": n_valid,
                        "tol": TOL_REPETIBILIDAD,
                        "azar": azar(n_trans, lado, TOL_REPETIBILIDAD),
                    }
                )
        detector = crear_detector("FAST")
        for tolerancia in (1.0, 2.0, 3.0, 5.0):
            for transformacion, valores in (("rotacion", TRANSFORMACIONES_E4["rotacion"]), ("escala", TRANSFORMACIONES_E4["escala"])):
                for valor in valores:
                    H, lut = _homografia_y_lut(transformacion, valor, lado)
                    rate, n_orig, n_trans, n_valid = repetibilidad(
                        cuadrado, H, detector, tolerancia, lut
                    )
                    filas_sens.append(
                        {
                            "imagen": nombre,
                            "detector": "FAST",
                            "barrido": transformacion,
                            "parametro": "tol",
                            "valor": tolerancia,
                            "valor_transformacion": float(valor),
                            "repetibilidad": rate,
                            "n_orig": n_orig,
                            "n_trans": n_trans,
                            "n_validos": n_valid,
                            "tol": tolerancia,
                            "azar": azar(n_trans, lado, tolerancia),
                        }
                    )
    df_sens = pd.DataFrame(filas_sens)
    columnas_sens = [
        "imagen",
        "detector",
        "barrido",
        "parametro",
        "valor",
        "repetibilidad",
        "n_orig",
        "n_trans",
        "n_validos",
        "tol",
        "azar",
        "valor_transformacion",
    ]
    df_sens = df_sens[columnas_sens]
    assert len(df_sens) == 294, f"Sensibilidad debe tener 294 filas, tiene {len(df_sens)}"
    df_sens.to_csv(out_dir / "repetibilidad_sensibilidad.csv", index=False)

    filas_medio = []
    for nombre, img in imagenes.items():
        cuadrado = recorte_cuadrado(img)
        lado = cuadrado.shape[0]
        for nombre_det in DETECTORES_E4:
            detector = crear_detector(nombre_det)
            for centro, etiqueta in ((True, "pixel"), (False, "medio")):
                H = homografia_rotacion(lado, 90, centro_pixel=centro)
                rate, n_orig, n_trans, n_valid = repetibilidad(
                    cuadrado, H, detector, TOL_REPETIBILIDAD
                )
                filas_medio.append(
                    {
                        "imagen": nombre,
                        "detector": nombre_det,
                        "transformacion": "rotacion",
                        "valor": 90.0,
                        "centro": etiqueta,
                        "repetibilidad": rate,
                        "n_orig": n_orig,
                        "n_trans": n_trans,
                        "n_validos": n_valid,
                        "tol": TOL_REPETIBILIDAD,
                    }
                )
    df_medio = pd.DataFrame(filas_medio)
    columnas_medio = [
        "imagen",
        "detector",
        "transformacion",
        "valor",
        "centro",
        "repetibilidad",
        "n_orig",
        "n_trans",
        "n_validos",
        "tol",
    ]
    df_medio = df_medio[columnas_medio]
    assert len(df_medio) == 18, f"Medio píxel debe tener 18 filas, tiene {len(df_medio)}"
    df_medio.to_csv(out_dir / "repetibilidad_control_medio_pixel.csv", index=False)

    actualizar_registro(
        [
            {
                "parametro": "fast_threshold",
                "valor": 25,
                "criterio": "valor principal declarado; sensibilidad 10/25/50 en escala",
                "barrido": "outputs/repetibilidad_sensibilidad.csv",
            },
            {
                "parametro": "orb_nfeatures",
                "valor": 5000,
                "criterio": "alto para que el limite no domine; valor declarado",
                "barrido": "outputs/repetibilidad.csv",
            },
            {
                "parametro": "orb_nlevels",
                "valor": 8,
                "criterio": "valor principal declarado; sensibilidad 1/4/8 en escala",
                "barrido": "outputs/repetibilidad_sensibilidad.csv",
            },
            {
                "parametro": "sift_configuracion",
                "valor": "default",
                "criterio": "cv2.SIFT_create() sin argumentos",
                "barrido": "outputs/repetibilidad.csv",
            },
            {
                "parametro": "tol_repetibilidad",
                "valor": 3.0,
                "criterio": "tolerancia principal; sensibilidad 1/2/3/5",
                "barrido": "outputs/repetibilidad_sensibilidad.csv",
            },
            {
                "parametro": "azar_formula",
                "valor": "1-(1-pi*tol^2/lado^2)^n_trans",
                "criterio": "linea base por densidad; aproximacion uniforme declarada",
                "barrido": "outputs/repetibilidad.csv",
            },
        ],
        out_dir,
    )
    return df, df_sens, df_medio


def figuras_e4(imagenes: dict[str, np.ndarray], out_dir: Path = OUT) -> None:
    out_dir = Path(out_dir)
    fig_dir = out_dir / "figuras"
    df = pd.read_csv(out_dir / "repetibilidad.csv")
    colores = {"FAST": "#1f77b4", "ORB": "#d62728", "SIFT": "#2ca02c"}
    especificaciones = (
        ("rotacion", "Rotación (grados)", "Repetibilidad frente a rotación", "e4_rotacion.png"),
        ("escala", "Escala (factor)", "Repetibilidad frente a escala", "e4_escala.png"),
        ("iluminacion", "Gamma (γ)", "Repetibilidad frente a iluminación", "e4_iluminacion.png"),
    )
    for transformacion, xlabel, titulo, nombre_fichero in especificaciones:
        fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.8), sharey=True)
        for ax, nombre in zip(axes, imagenes):
            sub_img = df[(df["imagen"] == nombre) & (df["transformacion"] == transformacion)]
            for detector in DETECTORES_E4:
                sub = sub_img[sub_img["detector"] == detector].sort_values("valor")
                ax.plot(
                    sub["valor"],
                    sub["repetibilidad"],
                    marker="o",
                    linewidth=1.6,
                    color=colores[detector],
                    label=detector,
                )
                ax.plot(
                    sub["valor"],
                    sub["azar"],
                    linestyle="--",
                    linewidth=1.0,
                    color=colores[detector],
                    alpha=0.45,
                )
            ax.set_title(nombre)
            ax.set_xlabel(xlabel)
            ax.set_ylim(-0.02, 1.02)
            ax.grid(alpha=0.25)
            ax.legend(fontsize=8, loc="best")
        axes[0].set_ylabel("Repetibilidad")
        fig.suptitle(titulo + "; línea discontinua: azar por densidad", fontsize=12)
        fig.tight_layout()
        _guardar(fig, fig_dir / nombre_fichero)

    sens = pd.read_csv(out_dir / "repetibilidad_sensibilidad.csv")

    for parametro, valores, titulo, nombre_fichero in (
        ("fastThreshold", (10.0, 25.0, 50.0), "Sensibilidad al umbral de FAST", "e4_sens_fast.png"),
        ("nlevels", (1.0, 4.0, 8.0), "Sensibilidad a la pirámide de ORB", "e4_sens_orb.png"),
    ):
        fig, axes = plt.subplots(1, 3, figsize=(15.5, 4.6), sharey=True)
        for ax, nombre in zip(axes, imagenes):
            sub_img = sens[(sens["imagen"] == nombre) & (sens["parametro"] == parametro)]
            for valor in valores:
                sub = sub_img[sub_img["valor"] == valor].sort_values("valor_transformacion")
                ax.plot(
                    sub["valor_transformacion"],
                    sub["repetibilidad"],
                    marker="o",
                    linewidth=1.5,
                    label=f"{parametro}={valor:g}",
                )
            ax.set_title(nombre)
            ax.set_xlabel("Escala (factor)")
            ax.set_ylim(-0.02, 1.02)
            ax.grid(alpha=0.25)
            ax.legend(fontsize=8)
        axes[0].set_ylabel("Repetibilidad")
        fig.suptitle(titulo, fontsize=12)
        fig.tight_layout()
        _guardar(fig, fig_dir / nombre_fichero)

    tolerancias = (1.0, 2.0, 3.0, 5.0)
    fig, axes = plt.subplots(2, 3, figsize=(15.5, 8.2), sharey=True)
    for fila, (barrido, xlabel, titulo_fila) in enumerate(
        (("rotacion", "Rotación (grados)", "Rotación"), ("escala", "Escala (factor)", "Escala"))
    ):
        for col, nombre in enumerate(imagenes):
            ax = axes[fila, col]
            sub_img = sens[
                (sens["imagen"] == nombre)
                & (sens["parametro"] == "tol")
                & (sens["barrido"] == barrido)
            ]
            for tolerancia in tolerancias:
                sub = sub_img[sub_img["valor"] == tolerancia].sort_values("valor_transformacion")
                ax.plot(
                    sub["valor_transformacion"],
                    sub["repetibilidad"],
                    marker="o",
                    linewidth=2.2 if tolerancia == 3.0 else 1.2,
                    alpha=1.0 if tolerancia == 3.0 else 0.75,
                    label=f"tol={tolerancia:g}",
                )
            ax.set_title(f"{nombre} · {titulo_fila}")
            ax.set_xlabel(xlabel)
            ax.set_ylim(-0.02, 1.02)
            ax.grid(alpha=0.25)
            ax.legend(fontsize=8)
    for ax in axes[:, 0]:
        ax.set_ylabel("Repetibilidad")
    fig.suptitle("Sensibilidad a la tolerancia de FAST; trazo grueso: tol=3 (principal)", fontsize=12)
    fig.tight_layout()
    _guardar(fig, fig_dir / "e4_sens_tol.png")

    medio = pd.read_csv(out_dir / "repetibilidad_control_medio_pixel.csv")
    fig, axes = plt.subplots(1, 3, figsize=(15.0, 4.4), sharey=True)
    ancho = 0.36
    for ax, nombre in zip(axes, imagenes):
        sub = medio[medio["imagen"] == nombre]
        x = np.arange(len(DETECTORES_E4))
        for i, centro in enumerate(("pixel", "medio")):
            vals = [
                float(sub[(sub["detector"] == det) & (sub["centro"] == centro)]["repetibilidad"].iloc[0])
                for det in DETECTORES_E4
            ]
            ax.bar(x + (i - 0.5) * ancho, vals, ancho, label=centro)
        ax.set_xticks(x)
        ax.set_xticklabels(DETECTORES_E4)
        ax.set_ylim(0.0, 1.02)
        ax.set_title(nombre)
        ax.grid(axis="y", alpha=0.25)
        ax.legend(fontsize=8)
    axes[0].set_ylabel("Repetibilidad a 90°")
    fig.suptitle("Control de centro de píxeles frente a medio píxel", fontsize=12)
    fig.tight_layout()
    _guardar(fig, fig_dir / "e4_medio_pixel.png")


# %% [markdown]
# ## 7. Ejecución completa
#
# Esta celda lanza todo el banco en orden y escribe los CSV y las figuras en `outputs/`. Si ejecuto
# el script como `python codigo/banco_pruebas.py`, entro por el mismo punto.

# %% -------------------------------------------------------------------------
# Ejecución completa: lanzo todo el banco
# ---------------------------------------------------------------------------
# Lanzo todo en el orden con el que generé los CSV.
def ejecutar_todo(out_dir: Path = OUT) -> dict[str, pd.DataFrame]:
    verificar_hashes(DATA)
    imagenes = {nombre: cargar_gris(DATA / nombre) for nombre in IMAGENES}
    df_e1, _, df_real = ejecutar_e1(imagenes, out_dir)
    figuras_heatmaps_e1(df_e1, df_real, out_dir)
    figuras_curvas_e1(df_e1, df_real, out_dir)
    figuras_recortes_e1(imagenes, df_e1, out_dir)
    tabla_ganadores_e1(df_e1).to_csv(out_dir / "tabla_e1_ganadores.csv", index=False)
    tabla_medianas_vs_medias_e1(df_e1).to_csv(
        out_dir / "tabla_e1_medianas_vs_medias.csv", index=False
    )
    tabla_bilateral_e1(df_e1).to_csv(out_dir / "tabla_e1_bilateral.csv", index=False)
    df_e2, _, _ = ejecutar_e2(imagenes, out_dir)
    figuras_perfiles_e2(df_e2, imagenes, out_dir)
    df_e3, optimo, unidad, df_est, df_trans = ejecutar_e3(imagenes, out_dir)
    figuras_e3(imagenes, out_dir)
    df_e4, df_e4_sens, df_e4_medio = ejecutar_e4(imagenes, out_dir)
    figuras_e4(imagenes, out_dir)
    return {
        "e1": df_e1,
        "e2": df_e2,
        "e3": df_e3,
        "e3_estabilidad": df_est,
        "e3_transferencia": df_trans,
        "e4": df_e4,
        "e4_sensibilidad": df_e4_sens,
        "e4_medio_pixel": df_e4_medio,
        "optimo_canny": optimo,
        "unidad_canny": unidad,
    }


if __name__ == "__main__":
    resultados = ejecutar_todo()
    print("E1:", resultados["e1"].shape)
    print("E2:", resultados["e2"].shape)
    print("E3:", resultados["e3"].shape)
    print("E3 estabilidad:", resultados["e3_estabilidad"].shape)
    print("E3 transferencia:", resultados["e3_transferencia"].shape)
    print("E4:", resultados["e4"].shape)
