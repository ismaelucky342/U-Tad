"""Barridos auxiliares de la Fase 3.

Genera:
    outputs/barrido_aux_truncada.csv
    outputs/barrido_aux_bilateral.csv
    outputs/barrido_aux_epsilon.csv
    outputs/barrido_aux_sigma_canny.csv
    outputs/registro_parametros.csv (parcial; se completa en fases posteriores)

Uso:
    _trabajo/venv/bin/python _herramientas/barridos_auxiliares.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import cv2
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "U2_Practica_Hernandez_Ismael" / "codigo"))
import banco_pruebas as bp  # noqa: E402

OUT = bp.OUT
OUT.mkdir(parents=True, exist_ok=True)
bp.verificar_hashes()

NOMBRES = ["IMG_01.jpg", "IMG_02.jpg", "IMG_03.jpg"]
IMAGENES = {n: bp.cargar_gris(bp.DATA / n) for n in NOMBRES}

print("Imágenes cargadas:", {n: g.shape for n, g in IMAGENES.items()})

# ---------------------------------------------------------------------------
# 1. Mediana truncada: k x alpha con ruido gaussiano
# ---------------------------------------------------------------------------
ruidosas = {}
for idx, nombre in enumerate(NOMBRES, start=1):
    for idx_nivel, sigma in enumerate((10, 20, 40)):
        rng = bp.rng_celda(bp.SEMILLA_AUX, idx, 10 + idx_nivel)
        ruidosas[(nombre, sigma)] = bp.ruido_gaussiano(IMAGENES[nombre], sigma, rng)

filas_truncada = []
for k in (3, 5, 7):
    for alpha in (0.1, 0.2, 0.3, 0.4):
        m = int(np.floor(alpha * k * k))
        if k * k - 2 * m < 1:
            continue
        ssims, psnrs = [], []
        for nombre in NOMBRES:
            for sigma in (10, 20, 40):
                salida = bp.media_recortada(ruidosas[(nombre, sigma)], k, alpha)
                psnrs.append(bp.psnr(IMAGENES[nombre], salida))
                ssims.append(bp.ssim(IMAGENES[nombre], salida))
        filas_truncada.append(
            {
                "k": k,
                "alpha": alpha,
                "m": m,
                "ssim_medio": float(np.mean(ssims)),
                "psnr_medio": float(np.mean(psnrs)),
            }
        )

df_truncada = pd.DataFrame(filas_truncada)
df_truncada = df_truncada.sort_values(
    ["ssim_medio", "psnr_medio", "k", "alpha"], ascending=[False, False, True, True]
).reset_index(drop=True)
df_truncada.to_csv(OUT / "barrido_aux_truncada.csv", index=False)
mejor_truncada = df_truncada.iloc[0]
print("\nMejor mediana truncada:")
print(mejor_truncada.to_string())

# ---------------------------------------------------------------------------
# 2. Bilateral: d x sigmaColor x sigmaSpace con ruido gaussiano sigma=20
# ---------------------------------------------------------------------------
ruidosas20 = {}
for idx, nombre in enumerate(NOMBRES, start=1):
    rng = bp.rng_celda(bp.SEMILLA_AUX, idx, 20)
    ruidosas20[nombre] = bp.ruido_gaussiano(IMAGENES[nombre], 20, rng)

filas_bilateral = []
for d in (5, 7, 9, 11):
    for sigma_color in (25, 50, 75, 100):
        for sigma_space in (5, 10, 20):
            ssims, psnrs = [], []
            for nombre in NOMBRES:
                salida = bp.filtro_bilateral(ruidosas20[nombre], d, sigma_color, sigma_space)
                psnrs.append(bp.psnr(IMAGENES[nombre], salida))
                ssims.append(bp.ssim(IMAGENES[nombre], salida))
            filas_bilateral.append(
                {
                    "d": d,
                    "sigma_color": sigma_color,
                    "sigma_space": sigma_space,
                    "psnr_medio": float(np.mean(psnrs)),
                    "ssim_medio": float(np.mean(ssims)),
                    "configuracion": "",
                }
            )

df_bilateral = pd.DataFrame(filas_bilateral)
idx_a = int(df_bilateral["ssim_medio"].idxmax())
idx_b = int(df_bilateral["psnr_medio"].idxmax())
if idx_b == idx_a:
    orden_psnr = df_bilateral["psnr_medio"].sort_values(ascending=False).index
    idx_b = int(next(i for i in orden_psnr if i != idx_a))
df_bilateral.loc[idx_a, "configuracion"] = "A"
df_bilateral.loc[idx_b, "configuracion"] = "B"
fila_a = df_bilateral.loc[idx_a].copy()
fila_b = df_bilateral.loc[idx_b].copy()
df_bilateral = df_bilateral.sort_values(
    ["configuracion", "ssim_medio"], ascending=[True, False]
).reset_index(drop=True)
df_bilateral.to_csv(OUT / "barrido_aux_bilateral.csv", index=False)
print("\nBilateral A (mejor SSIM):")
print(fila_a.to_string())
print("\nBilateral B (mejor PSNR distinto):")
print(fila_b.to_string())

# ---------------------------------------------------------------------------
# 3. epsilon de rebotes sobre las respuestas gaussianas
# ---------------------------------------------------------------------------
lado = bp.recorte_cuadrado(IMAGENES["IMG_01.jpg"]).shape[0]
perfiles_gauss = {}
for sigma, k in ((0.8, 7), (1.6, 11), (3.0, 19)):
    respuesta = bp.espectro_respuesta("gaussiano", {"sigma": sigma, "k": k}, lado)
    perfiles_gauss[sigma] = bp.perfil_radial(respuesta)

filas_epsilon = []
epsilon_elegido = None
for epsilon in np.logspace(-6, -1, 60):
    rebotes = {s: bp.contar_rebotes(perfiles_gauss[s], float(epsilon)) for s in perfiles_gauss}
    fila = {"epsilon": float(epsilon)}
    fila.update({f"rebotes_gaussiano_{s}": rebotes[s] for s in perfiles_gauss})
    filas_epsilon.append(fila)
    if epsilon_elegido is None and all(v == 0 for v in rebotes.values()):
        epsilon_elegido = float(epsilon)

df_epsilon = pd.DataFrame(filas_epsilon)
df_epsilon.to_csv(OUT / "barrido_aux_epsilon.csv", index=False)
if epsilon_elegido is None:
    raise RuntimeError("Ningún epsilon del barrido da cero rebotes en los tres gaussianos")
print(f"\nepsilon elegido: {epsilon_elegido:.6g}")

# ---------------------------------------------------------------------------
# 4. sigma de suavizado previo de Canny sobre la escena sintética
# ---------------------------------------------------------------------------
escena, referencia = bp.crear_escena_sintetica()
rng_aux = bp.rng_celda(bp.SEMILLA_AUX, 3, 0)
escena_ruidosa = bp.ruido_gaussiano(escena, 15, rng_aux)

filas_sigma = []
for sigma in (0.0, 0.5, 1.0, 1.5, 2.0):
    if sigma == 0.0:
        suave = escena_ruidosa
    else:
        k = 2 * int(np.ceil(3 * sigma)) + 1
        suave = bp.filtro_gaussiano(escena_ruidosa, sigma, k)
    gx = cv2.Sobel(suave, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(suave, cv2.CV_64F, 0, 1, ksize=3)
    magnitud = np.hypot(gx, gy)
    no_nulos = magnitud[magnitud > 0]
    mejor = None
    for percentil in (70, 75, 80, 85, 90, 95):
        alto = max(1, int(round(float(np.percentile(no_nulos, percentil)))))
        for fraccion in (0.3, 0.4, 0.5, 0.6):
            bajo = max(1, int(alto * fraccion))
            deteccion = cv2.Canny(suave, bajo, alto, apertureSize=3, L2gradient=True)
            precision, recall, f1, px = bp.puntuar_bordes(deteccion, referencia, bp.TOL_CANNY)
            if mejor is None or f1 > mejor["mejor_f1"]:
                mejor = {
                    "sigma": sigma,
                    "mejor_f1": f1,
                    "percentil_alto": percentil,
                    "fraccion_baja": fraccion,
                    "umbral_alto": alto,
                    "umbral_bajo": bajo,
                    "precision": precision,
                    "recall": recall,
                    "px_borde": px,
                }
    filas_sigma.append(mejor)

df_sigma = pd.DataFrame(filas_sigma)
df_sigma = df_sigma.sort_values(
    ["mejor_f1", "sigma"], ascending=[False, True]
).reset_index(drop=True)
df_sigma.to_csv(OUT / "barrido_aux_sigma_canny.csv", index=False)
mejor_sigma = df_sigma.iloc[0]
print("\nMejor sigma de Canny:")
print(mejor_sigma.to_string())

# ---------------------------------------------------------------------------
# 5. Registro parcial de parámetros
# ---------------------------------------------------------------------------
registro = [
    {
        "parametro": "truncada_k",
        "valor": int(mejor_truncada["k"]),
        "criterio": "maximo SSIM medio en 3 imagenes y gaussianos 10/20/40; desempate PSNR, k, alpha",
        "barrido": "outputs/barrido_aux_truncada.csv",
    },
    {
        "parametro": "truncada_alpha",
        "valor": float(mejor_truncada["alpha"]),
        "criterio": "maximo SSIM medio en 3 imagenes y gaussianos 10/20/40; desempate PSNR, k, alpha",
        "barrido": "outputs/barrido_aux_truncada.csv",
    },
    {
        "parametro": "bilateral_A_d",
        "valor": int(fila_a["d"]),
        "criterio": "maximo SSIM medio con gaussiano sigma=20 en 3 imagenes",
        "barrido": "outputs/barrido_aux_bilateral.csv",
    },
    {
        "parametro": "bilateral_A_sigma_color",
        "valor": int(fila_a["sigma_color"]),
        "criterio": "maximo SSIM medio con gaussiano sigma=20 en 3 imagenes",
        "barrido": "outputs/barrido_aux_bilateral.csv",
    },
    {
        "parametro": "bilateral_A_sigma_space",
        "valor": int(fila_a["sigma_space"]),
        "criterio": "maximo SSIM medio con gaussiano sigma=20 en 3 imagenes",
        "barrido": "outputs/barrido_aux_bilateral.csv",
    },
    {
        "parametro": "bilateral_B_d",
        "valor": int(fila_b["d"]),
        "criterio": "maximo PSNR medio con gaussiano sigma=20, distinto de A",
        "barrido": "outputs/barrido_aux_bilateral.csv",
    },
    {
        "parametro": "bilateral_B_sigma_color",
        "valor": int(fila_b["sigma_color"]),
        "criterio": "maximo PSNR medio con gaussiano sigma=20, distinto de A",
        "barrido": "outputs/barrido_aux_bilateral.csv",
    },
    {
        "parametro": "bilateral_B_sigma_space",
        "valor": int(fila_b["sigma_space"]),
        "criterio": "maximo PSNR medio con gaussiano sigma=20, distinto de A",
        "barrido": "outputs/barrido_aux_bilateral.csv",
    },
    {
        "parametro": "epsilon_rebotes",
        "valor": epsilon_elegido,
        "criterio": "menor epsilon que da cero rebotes en los tres gaussianos",
        "barrido": "outputs/barrido_aux_epsilon.csv",
    },
    {
        "parametro": "sigma_suavizado_canny",
        "valor": float(mejor_sigma["sigma"]),
        "criterio": "maximo mejor F1 en la escena sintetica con semilla auxiliar; desempate menor sigma",
        "barrido": "outputs/barrido_aux_sigma_canny.csv",
    },
]
pd.DataFrame(registro).to_csv(OUT / "registro_parametros.csv", index=False)
print("\nRegistro parcial escrito en", OUT / "registro_parametros.csv")
