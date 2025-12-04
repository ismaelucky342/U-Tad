# Documentación de Iteraciones - Competición SPAM/NOT SPAM

**Estudiante:** Ismael Hernandez Clemente  
**Email:** ismael.hernandez@live.u-tad.com  
**Competición:** [U-Tad] SPAM / NOT SPAM 2025  
**Objetivo:** Maximizar Matthews Correlation Coefficient (MCC)

---

## Iteración #1 ✅

**Fecha:** 04/12/2025

### Descripción del Cambio
Implementación del modelo baseline con arquitectura LSTM Bidireccional:
- Embedding layer (100 dimensiones)
- Spatial Dropout (0.2)
- Bidirectional LSTM (128 unidades, return_sequences=True)
- Global Max Pooling
- Dense layer (64 unidades) con Dropout (0.5)
- Output layer con sigmoid

Configuración:
- Vocabulario: 10,000 palabras (46,022 palabras únicas en dataset)
- Longitud de secuencia: 200 tokens
- Optimizer: AdamW (lr=1e-3, weight_decay=1e-4)
- Batch size: 32
- Epochs: 50 (detenido en época 8 por EarlyStopping)
- Callbacks: EarlyStopping (patience=5), ModelCheckpoint, ReduceLROnPlateau (patience=3)
- Total parámetros: 1,251,009

### Hipótesis/Justificación
Mi hipótesis es que una arquitectura LSTM Bidireccional capturará mejor el contexto secuencial de los mensajes SPAM, ya que palabras clave pueden aparecer en cualquier posición del texto. El Global Max Pooling extraerá las características más discriminativas, mientras que el Dropout alto (50%) ayudará a prevenir overfitting dado el tamaño del dataset.

### Resultado Obtenido
- **Validation MCC:** 0.8665 ⭐
- **Validation Accuracy:** 0.9577 (95.77%)
- **Validation Precision:** 0.9109 (91.09%)
- **Validation Recall:** 0.9211 (92.11%)
- **Training Loss:** 0.0055
- **Validation Loss:** 0.1895
- **Tiempo de entrenamiento:** ~86 segundos (8 epochs)
- **Kaggle Public Score:** 0.8665 ± 0.02 (Top 8 🏆)

**Análisis de Performance:**
- El modelo mostró **overfitting significativo** (diferencia de 0.1840 entre train loss y val loss)
- EarlyStopping detuvo el entrenamiento en época 8 tras no mejorar desde época 3
- Excelente balance entre Precision (91%) y Recall (92%) para clase SPAM
- Predicciones en test: 77.64% Not SPAM, 22.36% SPAM (similar a distribución de training: 75/25)

### Conclusiones y Próximos Pasos

**✅ Lo que funcionó bien:**
1. Arquitectura LSTM Bidireccional es sólida para capturar contexto secuencial
2. Global Max Pooling efectivo para extraer características discriminativas
3. EarlyStopping evitó sobreentrenamiento innecesario
4. Tiempo de entrenamiento excelente (<2 minutos con GPU P100)

**⚠️ Problemas identificados:**
1. **Overfitting severo** - El modelo memoriza demasiado el training set
2. Train loss extremadamente baja (0.0055) sugiere capacidad excesiva
3. Diferencia de 4.14% entre train accuracy y val accuracy

**🎯 Mejoras prioritarias para Iteración #2:**
1. **Reducir overfitting** (CRÍTICO):
   - Aumentar Spatial Dropout de 0.2 → 0.3
   - Añadir L2 regularization a capas Dense
   - Reducir unidades LSTM de 128 → 96
   - Data Augmentation con sinónimos o backtranslation

2. **Mejorar representación semántica**:
   - Incorporar embeddings pre-entrenados GloVe-100d
   - Freezar embeddings durante primeras epochs

3. **Experimentar con arquitecturas**:
   - Probar CNN + LSTM híbrido para capturar n-gramas locales
   - TextCNN con múltiples kernel sizes (3, 4, 5)

**📊 Objetivo Iteración #2:** MCC > 0.88 reduciendo overfitting

### Referencias
- Keras Bidirectional LSTM: https://keras.io/api/layers/recurrent_layers/bidirectional/
- Understanding LSTM: http://colah.github.io/posts/2015-08-Understanding-LSTMs/
- Matthews Correlation Coefficient: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.matthews_corrcoef.html

---

## Iteración #2 ✅

**Fecha:** 04/12/2025

### Descripción del Cambio
Regularización moderada para reducir overfitting:
- LSTM Units: 128 → 96 (-25%)
- Dense Units: 64 → 48 (-25%)
- Spatial Dropout: 0.2 → 0.3 (+50%)
- Dropout: 0.5 → 0.6 (+20%)
- L2 Regularization: None → 1e-4 (NUEVO)
- Early Stopping Patience: 5 → 3
- ReduceLROnPlateau Patience: 3 → 2
- Total parámetros: 1,160,609 (-7.2% vs V1)

### Hipótesis/Justificación
Hipótesis: Reducir capacidad del modelo + aumentar regularización (dropout + L2) forzará al modelo a generalizar mejor en lugar de memorizar el training set. El overfitting severo de V1 (Delta=0.184) debería reducirse significativamente.

### Resultado Obtenido
- **Validation MCC:** 0.8885 (+0.0220 vs V1)
- **Validation Accuracy:** 95.07% (-0.70% vs V1)
- **Train Loss:** 0.0411 (vs 0.0055 en V1)
- **Val Loss:** 0.2075 (vs 0.1895 en V1)
- **Overfitting Delta:** 0.1663 (vs 0.1840 en V1)
- **Tiempo de entrenamiento:** ~73 segundos (6 epochs)
- **Kaggle Public Score:** 0.8885 (mismo que validación)

**Análisis:**
- MCC mejoró (+2.2%) - Objetivo cumplido
- Overfitting reducido 9.6% pero sigue alto (Delta=0.166 > 0.10)
- Train loss aumentó correctamente (menos memorización)
- Val loss empeoró ligeramente
- Parámetros reducidos 7.2%

### Conclusiones y Próximos Pasos

**Lo que funcionó:**
- Aumento de MCC significativo
- Modelo menos propenso a memorizar
- Reducción de parámetros efectiva

**Lo que NO funcionó:**
- Overfitting sigue siendo alto (Delta > 0.10)
- Val loss no mejoró
- Mejora insuficiente (9.6%)

**Decisión:** Se requiere TERAPIA DE CHOQUE en Iteración 3
- Reducir capacidad 50% vs V1 (no solo 25%)
- Dropout extremo (0.7 en dense, 0.4 spatial)
- L2 regularization x5 más fuerte (5e-4)
- Learning rate reducido (5e-4)
- Gradient clipping (norm=1.0)
- Early stopping ultra agresivo (patience=2)

**Objetivo Iteración 3:** Overfitting Delta < 0.08 manteniendo MCC > 0.87

### Referencias
- L2 Regularization: https://keras.io/api/layers/regularizers/
- Dropout Paper: Srivastava et al. (2014)

---

## Iteración #3 ✅

**Fecha:** 04/12/2025

### Descripción del Cambio
TERAPIA DE CHOQUE - Regularización extrema:
- LSTM Units: 96 → 64 (-33% vs V2, -50% vs V1)
- Dense Units: 48 → 32 (-33% vs V2, -50% vs V1)
- Spatial Dropout: 0.3 → 0.4 (EXTREMO)
- Dropout: 0.6 → 0.7 (EXTREMO)
- L2 Regularization: 1e-4 → 5e-4 (x5 más fuerte)
- Learning Rate: 1e-3 → 5e-4 (-50%)
- Gradient Clipping: None → 1.0 (NUEVO)
- Early Stopping Patience: 3 → 2 (ultra agresivo)
- ReduceLROnPlateau Patience: 2 → 1 (inmediato)
- Bias regularization: Añadida L2 también en bias
- Total parámetros: ~1,000,000 estimado (-20% vs V2, -20% vs V1)

### Hipótesis/Justificación
Hipótesis: V2 mostró mejora insuficiente (9.6% reducción overfitting). Se necesitan cambios radicales. Reducir capacidad 50% total vs V1 + regularización extrema (dropout 0.7) + L2 x5 más fuerte + gradient clipping debería forzar generalización agresiva. Aunque pueda perder algo de capacidad predictiva, el objetivo es romper el ciclo de overfitting y establecer una base sólida para mejoras futuras (GloVe, CNN+LSTM).

### Resultado Obtenido
- **Validation MCC:** ~0.87-0.88 (estimado, pendiente ejecución completa)
- **Validation Accuracy:** TBD
- **Train Loss:** TBD (objetivo > 0.05)
- **Val Loss:** TBD (objetivo < 0.14)
- **Overfitting Delta:** TBD (objetivo < 0.08)
- **Kaggle Public Score:** 0.8733 (ligeramente peor que V2)

**Análisis Preliminar:**
- MCC en Kaggle: 0.8733 (-0.0152 vs V2)
- Posible pérdida de capacidad predictiva por regularización extrema
- Trade-off: menos overfitting pero posiblemente underfitting
- Necesidad de balance entre generalización y capacidad

### Conclusiones y Próximos Pasos

**Estado:** Pendiente análisis completo mañana 05/12/2025

**Observaciones iniciales:**
- La terapia de choque puede haber sido demasiado agresiva
- Kaggle score bajó ligeramente
- Posible underfitting por regularización extrema

**Estrategias para Iteración 4:**

**Opción A - Balance V2+V3:**
- LSTM: 80 units (entre 96 y 64)
- Dense: 40 units (entre 48 y 32)
- Dropout: 0.65 (entre 0.6 y 0.7)
- L2: 2e-4 (entre 1e-4 y 5e-4)
- Buscar sweet spot entre V2 y V3

**Opción B - GloVe Embeddings:**
- Mantener arquitectura V2 (mejor MCC)
- Incorporar embeddings pre-entrenados GloVe-100d
- Mejora semántica sin cambiar regularización

**Opción C - CNN + LSTM Híbrido:**
- Cambio arquitectural radical
- CNN para n-gramas locales + LSTM para secuencias
- Aprovechar fortalezas de ambos

**Decisión mañana:** Analizar métricas completas V3 y elegir estrategia

### Referencias
- Gradient Clipping: https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam
- Overfitting vs Underfitting Balance: https://developers.google.com/machine-learning/crash-course/generalization/peril-of-overfitting

---

## Iteración #4

**Fecha:** [DD/MM/2025]

### Descripción del Cambio
[Describir cambios]

### Hipótesis/Justificación
[Explicar hipótesis]

### Resultado Obtenido
- **Validation MCC:**
- **Validation Accuracy:**
- **Kaggle Public Score:**

### Conclusiones y Próximos Pasos
[Análisis y plan]

### Referencias
- [Referencias utilizadas]

---

## Iteración #5

**Fecha:** [DD/MM/2025]

### Descripción del Cambio
[Describir cambios]

### Hipótesis/Justificación
[Explicar hipótesis]

### Resultado Obtenido
- **Validation MCC:**
- **Validation Accuracy:**
- **Kaggle Public Score:**

### Conclusiones y Próximos Pasos
[Análisis y plan]

### Referencias
- [Referencias utilizadas]

---

## Resumen Comparativo de Todas las Iteraciones

| Iteración | Arquitectura Principal | Val MCC | Val Acc | Kaggle Score | Overfitting | Cambio Principal | Tiempo |
|-----------|------------------------|---------|---------|--------------|-------------|------------------|--------|
| 1 ✅ | Bi-LSTM (128) | 0.8665 | 95.77% | 0.8665 Top 8 | Alto (Δ=0.184) | Baseline | 86s (8 epochs) |
| 2 ✅ | Bi-LSTM (96) + L2 | 0.8885 | 95.07% | 0.8885 | Medio (Δ=0.166) | Regularización moderada | 73s (6 epochs) |
| 3 ⚠️ | Bi-LSTM (64) + L2x5 | ~0.87-0.88 | [TBD] | 0.8733 | [TBD] | Terapia de choque | [TBD] |
| 4 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [Decidir mañana] | - |
| 5 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | - | - |

**Análisis:**
- **Mejor MCC:** V2 (0.8885) - Regularización moderada
- **Más rápido:** V2 (73s, 6 epochs)
- **Menos overfitting:** V2 (Δ=0.166, mejora 9.6%)
- **Problema V3:** Posible underfitting por regularización extrema

**Estrategia recomendada:** Partir de V2 (mejor resultado) y añadir GloVe embeddings en V4

---

## Mejor Modelo Final

**Iteración seleccionada:** [Número]  
**MCC en Validación:** [Valor]  
**Score Público Kaggle:** [Valor]  
**Score Privado Kaggle:** [Valor - completar después del 12/12/2025]

### Justificación de la Selección
[Explicar por qué este modelo fue el mejor, haciendo referencia a los experimentos documentados]

---

## Lecciones Aprendidas

1. **Sobre Arquitecturas:**
   - [Qué arquitecturas funcionaron mejor y por qué]

2. **Sobre Hiperparámetros:**
   - [Qué configuraciones fueron más efectivas]

3. **Sobre Regularización:**
   - [Técnicas que ayudaron a prevenir overfitting]

4. **Sobre el Dataset:**
   - [Insights sobre características del dataset SPAM]

---

## Referencias Generales del Proyecto

1. **Keras Documentation:** https://keras.io/
2. **NLP with Deep Learning:** https://web.stanford.edu/class/cs224n/
3. **Kaggle Learn - NLP:** https://www.kaggle.com/learn/natural-language-processing
4. **Material de la asignatura:** [Especificar unidades relevantes]
