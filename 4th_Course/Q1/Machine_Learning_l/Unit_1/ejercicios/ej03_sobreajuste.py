"""
EJ03 ⭐⭐ · Underfitting vs overfitting y la «U» del error de test
Objetivo: diagnosticar sub/sobreajuste comparando error de train y de test, y ver el efecto de tener más datos.
Dependencias: numpy, scikit-learn. Ejecutar: python ej03_sobreajuste.py

ENUNCIADO
1. Genera 14 puntos de entrenamiento (repartidos de forma uniforme en [0,1]) y 200 de test
   con y = sin(2πx) + ruido gaussiano (σ = 0.25).
2. Ajusta polinomios de grado 1..12 y calcula el RMSE en train y en test.
3. Toma como referencia el grado con menor error de test y clasifica cada grado como
   underfitting / buen ajuste / overfitting (criterio: test > 1.15 × el mejor).
4. Repite con 140 puntos de entrenamiento: ¿qué le pasa al sobreajuste de los grados altos?
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

f = lambda x: np.sin(2 * np.pi * x)


def experimento(n_train, semilla=42):
    rng = np.random.default_rng(semilla)
    xt = (np.arange(n_train) + 0.5) / n_train                     # train repartido por todo el rango
    yt = f(xt) + rng.normal(0, 0.25, n_train)
    xs = rng.uniform(0.02, 0.98, 200); ys = f(xs) + rng.normal(0, 0.25, 200)
    filas = []
    for d in range(1, 13):
        m = make_pipeline(PolynomialFeatures(d), StandardScaler(), LinearRegression()).fit(xt[:, None], yt)
        rmse = lambda a, b: float(np.sqrt(mean_squared_error(b, m.predict(a[:, None]))))
        filas.append((d, rmse(xt, yt), rmse(xs, ys)))
    return filas


def diagnostico(filas):
    mejor = min(filas, key=lambda r: r[2])
    print(f"{'grado':>5} {'train':>8} {'test':>8}  diagnóstico")
    for d, tr, te in filas:
        if te > 1.15 * mejor[2]:
            diag = "underfitting" if d < mejor[0] else "overfitting"
        else:
            diag = "buen ajuste"
        print(f"{d:5d} {tr:8.3f} {te:8.3f}  {diag}{'  ← mejor' if d == mejor[0] else ''}")
    return mejor


print("=== 14 puntos de entrenamiento ===")
diagnostico(experimento(14))
print("\n=== 140 puntos de entrenamiento ===")
diagnostico(experimento(140))

# SOLUCIÓN / qué observar:
#  - El error de train baja siempre al subir el grado; el de test baja hasta el grado ~3 y luego sube (la «U»).
#  - Grados 1-2: underfitting (error alto en train y test, el modelo no capta la forma del seno).
#  - Con 14 puntos, los grados 8-12 sobreajustan: train ≈ 0.09-0.11 pero test ≈ 0.32 (brecha grande).
#  - Con 140 puntos el mismo modelo complejo ya no sobreajusta: train y test casi coinciden (≈ 0.19-0.26).
#    MÁS DATOS reducen la varianza → permiten usar modelos más complejos sin sobreajustar.
