"""
EJ05 ⭐⭐⭐ · Proyecto completo: preprocesamiento + split + CV + modelos + test único + data leakage
Objetivo: aplicar el flujo entero de la unidad sin fugas de información.
Dependencias: numpy, pandas, scikit-learn. Ejecutar: python ej05_pipeline_validacion_cruzada.py

ENUNCIADO
1. Construye un dataset tipo Titanic (con faltantes y categóricas) de 600 filas, semilla fija.
2. Separa un test (20 %) y NO lo toques hasta el final.
3. Construye un Pipeline (imputación + escalado + one-hot + modelo) y compara con validación
   cruzada estratificada (k=5): baseline, regresión logística, k-NN y árbol (profundidad 3 y sin límite).
4. Elige el mejor por CV, reentrénalo con todo el train y evalúalo UNA VEZ en test (accuracy, F1,
   matriz de confusión).
5. Demuestra el data leakage: selecciona atributos con todo el dataset y compara con hacerlo
   dentro del pipeline sobre datos aleatorios.
"""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

# 1 ── datos sintéticos tipo Titanic
rng = np.random.default_rng(7)
n = 600
sexo = rng.choice(["hombre", "mujer"], n)
pclass = rng.choice([1, 2, 3], n, p=[.25, .25, .5])
edad = np.clip(rng.normal(30, 13, n), 1, 80)
tarifa = np.clip(rng.lognormal(3, 0.8, n) * (4 - pclass) / 2, 3, 300)
embarque = rng.choice(["S", "C", "Q"], n, p=[.7, .2, .1])
logit = -0.5 + 2.2 * (sexo == "mujer") + 0.7 * (3 - pclass) - 0.02 * (edad - 30)
sobrevive = (rng.uniform(size=n) < 1 / (1 + np.exp(-logit))).astype(int)
df = pd.DataFrame(dict(pclass=pclass, sexo=sexo, edad=edad, tarifa=tarifa, embarque=embarque, sobrevive=sobrevive))
df.loc[rng.choice(n, 90, replace=False), "edad"] = np.nan             # 15 % de edades faltantes
df.loc[rng.choice(n, 10, replace=False), "embarque"] = None
print("Faltantes:\n", df.isna().sum()[lambda s: s > 0].to_string(), f"\nBalance de clases: {df.sobrevive.mean():.1%} sobreviven\n")

X, y = df.drop(columns="sobrevive"), df["sobrevive"]

# 2 ── test aparte
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)

# 3 ── pipelines
num = ["edad", "tarifa"]; cat = ["pclass", "sexo", "embarque"]
def prep():
    return ColumnTransformer([
        ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("esc", StandardScaler())]), num),
        ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                          ("ohe", OneHotEncoder(handle_unknown="ignore"))]), cat)])
modelos = {
    "baseline (mayoritaria)": DummyClassifier(strategy="most_frequent"),
    "regresión logística":    LogisticRegression(max_iter=500),
    "k-NN (k=5)":             KNeighborsClassifier(5),
    "árbol prof. 3":          DecisionTreeClassifier(max_depth=3, random_state=0),
    "árbol sin límite":       DecisionTreeClassifier(random_state=0),
}
cv = StratifiedKFold(5, shuffle=True, random_state=0)
resultados = {}
for nombre, m in modelos.items():
    s = cross_val_score(Pipeline([("prep", prep()), ("m", m)]), Xtr, ytr, cv=cv, scoring="accuracy")
    resultados[nombre] = s.mean()
    print(f"{nombre:24s} accuracy CV = {s.mean():.3f} ± {s.std():.3f}")

# 4 ── ganador → test una sola vez
mejor = max(resultados, key=resultados.get)
final = Pipeline([("prep", prep()), ("m", modelos[mejor])]).fit(Xtr, ytr)
p = final.predict(Xte)
print(f"\nMejor por CV: {mejor}")
print(f"TEST (una vez): accuracy={accuracy_score(yte, p):.3f}  F1={f1_score(yte, p):.3f}")
print(confusion_matrix(yte, p))

# 5 ── data leakage con datos aleatorios
rng = np.random.default_rng(0)
Xr = rng.normal(size=(100, 5000)); yr = rng.integers(0, 2, 100)
Xsel = SelectKBest(f_classif, k=20).fit_transform(Xr, yr)
con = cross_val_score(LogisticRegression(), Xsel, yr, cv=5).mean()
sin = cross_val_score(make_pipeline(SelectKBest(f_classif, k=20), LogisticRegression()), Xr, yr, cv=5).mean()
print(f"\nDatos SIN señal → accuracy CV con fuga: {con:.2f} | sin fuga (Pipeline): {sin:.2f}")

# SOLUCIÓN / qué observar:
#  - El baseline marca el suelo (acertar siempre la clase mayoritaria ≈ 72 %); un modelo útil debe superarlo claramente.
#  - Ojo: con la clase positiva MAYORITARIA, el F1 del baseline sale engañosamente alto (≈ 0.84); por eso aquí se usa accuracy y se compara siempre contra el baseline.
#  - El árbol sin límite memoriza (sobreajuste) y suele rendir peor en CV que el de profundidad 3.
#  - El test se evalúa UNA vez, con el modelo elegido solo por CV.
#  - Con fuga, datos aleatorios «parecen» predecibles (~0.85); sin fuga, ~0.5 (el azar).
