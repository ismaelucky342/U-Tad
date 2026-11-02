"""
EJ04 ⭐⭐ · Métricas de clasificación, desbalance y umbral
Objetivo: ver por qué la accuracy engaña y cómo el umbral desplaza precision/recall.
Dependencias: numpy, scikit-learn. Ejecutar: python ej04_metricas_clasificacion.py

ENUNCIADO
1. Calcula a mano (con las fórmulas) accuracy, precision, recall, F1 y especificidad de
   TP=40, FP=10, FN=20, TN=130 y verifícalo con scikit-learn.
2. Dataset de fraude con 1 % de positivos: compara un DummyClassifier («siempre NO») con una
   regresión logística (class_weight='balanced'). Muestra accuracy, recall, precision, F1 y ROC-AUC.
3. Barre el umbral de decisión de la regresión logística (0.1 … 0.9) y observa precision vs recall.
4. Calcula el umbral que minimiza el coste total (ratio*FN + FP) cuando un fraude perdido cuesta
   1, 10, 50 y 200 veces más que una falsa alarma. ¿Cómo evoluciona el umbral óptimo?
"""
import numpy as np
from sklearn.datasets import make_classification
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, confusion_matrix, f1_score, precision_score,
                             recall_score, roc_auc_score)
from sklearn.model_selection import train_test_split

# 1 ── a mano
TP, FP, FN, TN = 40, 10, 20, 130
acc = (TP + TN) / (TP + TN + FP + FN); prec = TP / (TP + FP); rec = TP / (TP + FN)
f1 = 2 * prec * rec / (prec + rec); esp = TN / (TN + FP)
print(f"A mano → accuracy={acc:.3f} precision={prec:.3f} recall={rec:.3f} F1={f1:.3f} especificidad={esp:.3f}")
y_real = np.array([1] * (TP + FN) + [0] * (TN + FP))
y_pred = np.array([1] * TP + [0] * FN + [0] * TN + [1] * FP)
print(f"sklearn → accuracy={accuracy_score(y_real, y_pred):.3f} precision={precision_score(y_real, y_pred):.3f} "
      f"recall={recall_score(y_real, y_pred):.3f} F1={f1_score(y_real, y_pred):.3f}\n")

# 2 ── desbalance
X, y = make_classification(n_samples=5000, n_features=10, n_informative=5, weights=[0.99],
                           class_sep=1.0, flip_y=0, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.4, stratify=y, random_state=0)
print(f"Positivos en test: {yte.sum()} de {len(yte)} ({yte.mean():.1%})")

dummy = DummyClassifier(strategy="most_frequent").fit(Xtr, ytr)
logit = LogisticRegression(class_weight="balanced", max_iter=1000).fit(Xtr, ytr)
for nombre, m in (("siempre NO", dummy), ("logística", logit)):
    p = m.predict(Xte)
    auc = roc_auc_score(yte, m.predict_proba(Xte)[:, 1])
    print(f"{nombre:11s} acc={accuracy_score(yte, p):.3f} recall={recall_score(yte, p):.3f} "
          f"prec={precision_score(yte, p, zero_division=0):.3f} F1={f1_score(yte, p):.3f} AUC={auc:.3f}")

# 3 ── umbral
print("\numbral  precision  recall    F1   FP   FN")
proba = logit.predict_proba(Xte)[:, 1]
for t in np.arange(0.1, 1.0, 0.2):
    p = (proba >= t).astype(int)
    tn, fp, fn, tp = confusion_matrix(yte, p).ravel()
    print(f"{t:6.1f}  {precision_score(yte, p, zero_division=0):9.3f} {recall_score(yte, p):7.3f} "
          f"{f1_score(yte, p):6.3f} {fp:4d} {fn:4d}")

# 4 ── elegir el umbral según el coste de los errores: minimizar  ratio*FN + 1*FP
print("\nUmbral que minimiza el coste total según cuánto más caro sea un FN que un FP:")
umbrales = np.round(np.arange(0.05, 1.0, 0.05), 2)
cm = {t: confusion_matrix(yte, (proba >= t).astype(int)).ravel() for t in umbrales}   # (tn, fp, fn, tp)
for ratio in (1, 10, 50, 200):
    coste = {t: ratio * cm[t][2] + cm[t][1] for t in umbrales}
    t_opt = min(coste, key=coste.get)
    print(f"  FN cuesta {ratio:>3}× un FP → umbral óptimo = {t_opt:.2f}  (FP={cm[t_opt][1]}, FN={cm[t_opt][2]})")

# SOLUCIÓN / qué observar:
#  - «Siempre NO» tiene 99 % de accuracy y 0 % de recall: la accuracy engaña con datos desbalanceados.
#  - La logística (con class_weight='balanced') detecta ~85 % de los fraudes, pero a cambio de muchas
#    falsas alarmas (precision baja ≈ 0.11 al umbral 0.5). Subir el umbral mejora la precision y baja el recall.
#  - El umbral óptimo NO es el 0.5 por defecto: depende del coste de cada error. Cuanto más caro es perder
#    un positivo (FN), más BAJO es el umbral óptimo (se prioriza el recall).
#  - ROC-AUC (≈ 0.95) mide la calidad del ranking sin fijar umbral; F1, precision y recall sí dependen de él.
