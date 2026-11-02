"""
EJ02 ⭐⭐ · Descenso de gradiente a mano y efecto de la tasa de aprendizaje
Objetivo: implementar modelo + pérdida + optimizador y ver convergencia / divergencia.
Dependencias: numpy. Ejecutar: python ej02_descenso_gradiente.py

ENUNCIADO
1. Genera datos y = 2x + 1 + ruido (semilla fija).
2. Implementa descenso de gradiente para y_hat = w*x + b con pérdida MSE.
3. Entrena con lr = 0.001, 0.05 y 0.30. Muestra el MSE final de cada una.
4. Compara con la solución exacta de mínimos cuadrados (np.polyfit).
5. Añade un outlier y observa cómo cambia la recta aprendida.
"""
import numpy as np


def entrenar(x, y, lr, iters=500):
    w = b = 0.0
    hist = []
    for _ in range(iters):
        e = w * x + b - y                 # error de predicción
        hist.append(float((e ** 2).mean()))
        w -= lr * 2 * (e * x).mean()      # dL/dw
        b -= lr * 2 * e.mean()            # dL/db
        if not np.isfinite(hist[-1]) or hist[-1] > 1e12:
            break                         # divergencia
    return w, b, hist


rng = np.random.default_rng(0)
x = rng.uniform(0, 5, 40)
y = 2 * x + 1 + rng.normal(0, 0.5, 40)

# 3 ── tres tasas de aprendizaje
for lr in (0.001, 0.05, 0.30):
    w, b, h = entrenar(x, y, lr)
    estado = "DIVERGE 💥" if h[-1] > 1e6 else "ok"
    print(f"lr={lr:<6} w={w:9.3f} b={b:9.3f}  MSE final={h[-1]:.4g}  ({estado}, {len(h)} iters)")

# 4 ── solución exacta
pw, pb = np.polyfit(x, y, 1)
print(f"\nMínimos cuadrados exactos: w={pw:.3f} b={pb:.3f}")

# 5 ── outlier
x2 = np.append(x, 5.0); y2 = np.append(y, -10.0)           # un punto muy fuera de la tendencia
w2, b2, _ = entrenar(x2, y2, 0.05)
print(f"Con outlier (5, -10):       w={w2:.3f} b={b2:.3f}  ← la recta se desplaza hacia el punto")

# SOLUCIÓN / qué observar:
#  - lr muy pequeña: converge pero con 500 iteraciones aún no llega (w, b lejos de 2 y 1).
#  - lr adecuada: llega a ≈ la solución exacta.
#  - lr demasiado grande: el MSE crece en cada paso → diverge.
#  - El MSE eleva al cuadrado el error: un solo outlier arrastra la recta.
