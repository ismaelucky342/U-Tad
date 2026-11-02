"""
EJ01 ⭐ · Anatomía de un dataset y tipos de aprendizaje
Objetivo: identificar instancias, atributos y etiqueta; distinguir supervisado y no supervisado
usando el MISMO dataset (Iris). Dependencias: scikit-learn, pandas, numpy.
Ejecutar: python ej01_tipos_y_dataset.py

ENUNCIADO
1. Carga Iris como DataFrame. Indica cuántas instancias, atributos y clases hay.
2. Supervisado: entrena una regresión logística (con escalado) y mide la accuracy en test.
3. No supervisado: ejecuta K-Means (k=3) IGNORANDO la etiqueta y compara los clústeres
   con las especies reales (tabla cruzada).
4. Reflexiona: ¿por qué K-Means no puede «acertar» el nombre de la especie aunque agrupe bien?
"""
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# 1 ── anatomía
iris = load_iris(as_frame=True)
df = iris.frame                                  # 4 atributos + columna 'target'
X, y = iris.data, iris.target
print(f"Instancias: {len(df)} | atributos: {X.shape[1]} {list(X.columns)} | clases: {[str(c) for c in iris.target_names]}")
print(df.head(3), "\n")

# 2 ── supervisado
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=200)).fit(Xtr, ytr)
print(f"[Supervisado] accuracy en test: {clf.score(Xte, yte):.3f}\n")

# 3 ── no supervisado (sin usar y)
km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
tabla = pd.crosstab(pd.Series(y.map(dict(enumerate(iris.target_names))), name="especie real"),
                    pd.Series(km.labels_, name="clúster"))
print("[No supervisado] clústeres vs especie real:\n", tabla, "\n")

# 4 ── SOLUCIÓN / qué observar
print("Observación: setosa cae entera en un clúster (muy separable); versicolor y virginica se")
print("mezclan un poco. Los clústeres se numeran 0,1,2 de forma ARBITRARIA: K-Means no conoce los")
print("nombres de las especies, solo agrupa por similitud. Sin etiquetas no hay 'respuesta correcta'.")
