# U1 · Introducción al Aprendizaje Automático — Resumen de estudio

> Repaso rápido. Detalle, ejemplos y código → [`U1_temario_denso.md`](U1_temario_denso.md).

---

## 1. Key concepts

### Qué es el ML
- **ML** = sistemas que **aprenden patrones de los datos** sin ser programados para cada caso.
- **Programación clásica:** datos + reglas → respuestas. **ML:** datos + respuestas → **reglas (modelo)**.
- **Mitchell (1997):** un programa aprende de la experiencia **E** respecto a la tarea **T** y la medida **P** si su rendimiento en T, medido por P, **mejora con E**.
- **IA ⊃ ML ⊃ Deep Learning.** Deep Blue (1997) = búsqueda + reglas, **no** ML.
- ML aprende $f(x;\theta)$ **minimizando una pérdida** sobre ejemplos. No «piensa»: **ajusta**.
- **Algoritmo** = receta; **modelo** = resultado de aplicar el algoritmo a unos datos.
- **Parámetros** los aprende el modelo; **hiperparámetros** los elige la persona.

### Hitos
Turing 1950 · Perceptrón 1957 · Samuel/«machine learning» 1959 · inviernos de la IA 70-80 · backprop 1986 · ImageNet 2009 · AlexNet 2012 · AlphaGo 2016 · Transformer 2017 · ChatGPT 2022 · Nobel 2024 (Hopfield/Hinton; Hassabis/Jumper).

### Tipos de aprendizaje

| Tipo | Datos | Objetivo | Ejemplo |
|---|---|---|---|
| **Supervisado** | $(X,y)$ | Predecir $y$ | Clasificación (spam), regresión (precio) |
| **No supervisado** | Solo $X$ | Descubrir estructura | Clustering, PCA, reglas de asociación |
| **Semi-supervisado** | Pocos $(X,y)$ + muchos $X$ | Combinar | Imágenes médicas con pocas anotaciones |
| **Por refuerzo** | Agente + entorno | Maximizar recompensa | Juegos, robótica |

- **Clasificación:** salida discreta. **Regresión:** salida continua.
- **Basado en modelos** (guarda parámetros) vs **basado en instancias** (guarda ejemplos, p. ej. k-NN).
- Algoritmos: **K-Means** (clustering), **PCA** (reducción), **Apriori/FP-Growth** (asociación).
- Refuerzo: **estado, acción, recompensa** → aprende una **política**.
- Truco: *¿tengo la respuesta correcta para los ejemplos?* Todos → supervisado · ninguno → no supervisado · pocos → semi · solo recompensas → refuerzo.

### Componentes y datos
- **3 pilares:** datos · ingeniería de atributos · modelo.
- Dataset: **instancias** (filas), **atributos** $X$ (columnas), **etiqueta** $y$.
- Etiquetas: binaria · multiclase (una clase) · multietiqueta (varias a la vez) · continua · sin etiqueta.
- Datos: numéricos, categóricos, texto, imágenes, series temporales, combinados.
- Problemas de datos: **calidad, representatividad, sesgos, formato, volumen**.

### Etapas
Problema → Datos → **EDA** → Limpieza → **Split** → Entrenar → Evaluar → Desplegar (+ monitorizar drift). Es un **ciclo iterativo**.
- Preparar datos consume la mayor parte del tiempo (~45 % según Anaconda 2020; «hasta 80 %» según la plataforma).
- Preprocesar: **faltantes** (eliminar/imputar), **outliers** (IQR, z-score), **escalar** (min-max, estandarizar), **codificar** (one-hot / label / target), **seleccionar atributos**, **transformar**.
- **Split:** train (ajusta $\theta$) · validación (hiperparámetros) · **test (una sola vez)**. Típico 70/15/15.
- **Separar antes de transformar** y usar `Pipeline` → evita **data leakage**.

### Generalización
- **Underfitting:** error alto en train y test (sesgo alto). **Overfitting:** train muy bajo, test alto (varianza alta).
- Más complejidad → sesgo ↓, varianza ↑ → error de test en **U**.
- Remedios overfitting: más datos, modelo más simple, regularización, *early stopping*, selección de atributos.
- Validación: **hold-out**, **k-fold CV** (media ± desviación; $k$ veces más caro), **bootstrapping** (~63,2 % únicos).
- **Curvas de aprendizaje:** brecha grande → overfitting; ambas altas y juntas → underfitting.

---

## 2. Fórmulas esenciales

| Concepto | Fórmula |
|---|---|
| Descenso de gradiente | $\theta\leftarrow\theta-\eta\,\nabla_\theta L$ |
| MSE (regresión lineal $\hat y=wx+b$) | $\frac1n\sum(\hat y_i-y_i)^2$; $\ \partial_w=\frac2n\sum(\hat y_i-y_i)x_i$; $\ \partial_b=\frac2n\sum(\hat y_i-y_i)$ |
| Min-max | $x'=\dfrac{x-x_{\min}}{x_{\max}-x_{\min}}$ |
| Estandarización | $x'=\dfrac{x-\mu}{\sigma}$ |
| Regla IQR | atípico si fuera de $[Q_1-1{,}5\,\text{IQR},\ Q_3+1{,}5\,\text{IQR}]$ |
| **Accuracy** | $\dfrac{TP+TN}{TP+TN+FP+FN}$ |
| **Precision** | $\dfrac{TP}{TP+FP}$ |
| **Recall** (sensibilidad) | $\dfrac{TP}{TP+FN}$ |
| **Especificidad** | $\dfrac{TN}{TN+FP}$ |
| **F1** | $2\dfrac{P\cdot R}{P+R}=\dfrac{2TP}{2TP+FP+FN}$ |
| **MAE** | $\frac1n\sum\lvert y_i-\hat y_i\rvert$ |
| **MSE / RMSE** | $\frac1n\sum(y_i-\hat y_i)^2\ /\ \sqrt{\text{MSE}}$ |
| **R²** | $1-\dfrac{\sum(y_i-\hat y_i)^2}{\sum(y_i-\bar y)^2}$ |

**Matriz de confusión:** filas = real, columnas = predicho. **FP** = falsa alarma · **FN** = se escapa.

**Ejemplo ancla:** $TP=40,FP=10,FN=20,TN=130$ → accuracy 0,85 · precision 0,80 · recall 0,667 · F1 0,727.
**Regresión ancla:** $y=(3,5,2{,}5,7)$, $\hat y=(2{,}5,5,4,8)$ → MAE 0,75 · MSE 0,875 · RMSE 0,935 · R² 0,724.

---

## 3. ¿Cuándo usar qué?

| Situación | Métrica / acción |
|---|---|
| Clases balanceadas | Accuracy |
| **Falso negativo caro** (cáncer, fraude) | **Recall** ↑ (bajar umbral) |
| **Falso positivo caro** (borrar correo legítimo) | **Precision** ↑ (subir umbral) |
| Desbalance + ambos errores importan | **F1**, PR-AUC |
| Comparar modelos sin fijar umbral | **ROC-AUC** |
| Evento muy raro | **PR-AUC**, recall/precision (no accuracy) |
| Regresión, errores grandes muy costosos | **RMSE** |
| Regresión con outliers | **MAE** |
| Proporción de varianza explicada | **R²** (puede ser negativo) |
| Pocos datos | Modelo simple + regularización |
| Muchas variables, pocos ejemplos | Reducir dimensionalidad / seleccionar atributos |
| k-NN, SVM, redes | **Escalar** variables |
| Árboles / Random Forest | No necesitan escalado |
| Categoría **nominal** | One-hot (no label encoding) |
| Categoría **ordinal** | Label encoding |
| Clases desbalanceadas | SMOTE/oversampling/undersampling **dentro** del pipeline, o métricas adecuadas |
| Series temporales | Split **cronológico**, no aleatorio |

---

## 4. Errores típicos de examen

1. **Accuracy 99 % = buen modelo** ✗ → con 1 % de positivos, «siempre NO» da 99 % y recall 0.
2. **Confundir precision con especificidad** (la especificidad es $TN/(TN+FP)$).
3. **Mirar el test para decidir** (modelo, umbral, hiperparámetros) → deja de ser test.
4. **Escalar/imputar con todo el dataset antes de dividir** → data leakage.
5. **Más iteraciones = mejor modelo** ✗: mejoran el train, no garantizan generalizar.
6. **Label encoding en variable nominal** → introduce un orden falso.
7. **Confundir aprendizaje no supervisado con semi-supervisado** (semi = *algunas* etiquetas).
8. **Pensar que Deep Blue es ML** (era búsqueda + reglas).
9. **Interpretar correlación como causalidad.**
10. **Saltarse la EDA** y entrenar directamente.
11. **Learning rate demasiado grande** → el descenso **diverge**.
12. **R² siempre entre 0 y 1** ✗ (puede ser negativo).
13. **Multiclase ≠ multietiqueta.**
14. Ignorar que el ML **hereda sesgos** de los datos.

---

## 5. Checklist: debo saber…

- [ ] Definir ML y la definición de Mitchell (T, E, P) con un ejemplo propio.
- [ ] Explicar la diferencia clásica vs ML con el esquema datos/reglas/respuestas.
- [ ] Distinguir IA, ML y Deep Learning.
- [ ] Clasificar un caso en supervisado / no supervisado / semi / refuerzo.
- [ ] Diferenciar clasificación y regresión; binaria / multiclase / multietiqueta.
- [ ] Identificar instancias, atributos y etiqueta en una tabla.
- [ ] Diferenciar algoritmo y modelo; parámetros e hiperparámetros.
- [ ] Describir las etapas de un proyecto y por qué es iterativo.
- [ ] Aplicar imputación, escalado y codificación y decir cuándo usar cada una.
- [ ] Explicar train / validación / test y por qué el test se usa una vez.
- [ ] Explicar data leakage y cómo evitarlo (`Pipeline`).
- [ ] Reconocer under/overfitting en un gráfico o en números train/test.
- [ ] Explicar sesgo vs varianza y la «U» del error de test.
- [ ] Calcular una matriz de confusión y sus 4 métricas a mano.
- [ ] Explicar la paradoja de la accuracy con datos desbalanceados.
- [ ] Explicar el efecto de subir/bajar el umbral (precision vs recall).
- [ ] Calcular MAE, MSE, RMSE y R² a mano.
- [ ] Elegir métrica según el coste de los errores.
- [ ] Describir un paso de descenso de gradiente y el efecto de la tasa de aprendizaje.

---

## 6. Autoevaluación

1. Un modelo saca 99 % en train y 70 % en test. ¿Qué le pasa y qué harías?
2. Agrupar clientes sin saber de antemano qué grupos existen: ¿qué tipo de aprendizaje y qué algoritmo?
3. En un detector de cáncer, ¿qué error es más caro y qué métrica priorizas?
4. Un banco tiene 1 % de fraudes. Un modelo acierta el 99 %. ¿Es bueno? ¿Qué más mirarías?
5. ¿Por qué no se debe escalar con todo el dataset antes de dividir?
6. Diferencia entre parámetro e hiperparámetro. Pon un ejemplo de cada uno.
7. ¿Qué ocurre con el error de train y de test al aumentar la complejidad del modelo?
8. Con $TP=30,FP=10,FN=10,TN=50$, calcula accuracy, precision, recall y F1.
9. Subes el umbral de decisión de 0,5 a 0,8. ¿Qué pasa con precision y recall?
10. ¿Cuándo preferirías MAE y cuándo RMSE?
11. Un $R^2$ negativo en test, ¿qué significa?
12. ¿Cuál es la diferencia entre aprendizaje semi-supervisado y no supervisado?
13. ¿Por qué el conjunto de test solo debe usarse una vez, al final?
14. En una cuadrícula de $k=5$ pliegues, ¿cuántas veces se usa cada dato para entrenar y para validar?
15. ¿Por qué Deep Blue no es un ejemplo de aprendizaje automático?

<details>
<summary><strong>Respuestas</strong></summary>

1. **Overfitting** (brecha train–test enorme). Más datos, modelo más simple o regularización, *early stopping*, selección de atributos, validación cruzada.
2. **No supervisado — clustering** (p. ej. K-Means).
3. El **falso negativo** (enfermo no detectado) → priorizar **recall** (bajar el umbral).
4. **No necesariamente**: «siempre NO» también saca 99 %. Mirar **recall, precision, F1, matriz de confusión, PR-AUC**.
5. Porque el escalador aprende media/desviación; si usa datos de test, hay **data leakage** y la métrica sale optimista. Ajustarlo solo con train (en un `Pipeline`).
6. Parámetro: lo **aprende** el modelo (peso $w$ de una recta). Hiperparámetro: lo **elige la persona** (profundidad de un árbol, $k$ de k-NN, tasa de aprendizaje).
7. **Train** baja siempre; **test** baja y luego **sube** (U).
8. $n=100$: accuracy $=(30+50)/100=0{,}80$; precision $=30/40=0{,}75$; recall $=30/40=0{,}75$; F1 $=0{,}75$.
9. **Precision sube** (menos falsas alarmas), **recall baja** (se escapan más positivos).
10. **MAE** si hay outliers/robustez; **RMSE** si los errores grandes son especialmente graves.
11. Que el modelo es **peor que predecir siempre la media** de $y$.
12. Semi: tiene **algunas etiquetas** y las usa; no supervisado: **ninguna**.
13. Si lo usas para decidir, el test deja de ser independiente y la métrica final **ya no estima la generalización real**.
14. **4 veces** para entrenar y **1** para validar.
15. Era **búsqueda + reglas expertas** programadas, no aprendía de datos.
</details>
