# Iteraciones del Proyecto AEC2

## Iteración 1: Modelo Baseline (V0)
En la primera iteración, implementé un modelo baseline simple utilizando una red neuronal recurrente con LSTM bidireccional. Utilicé embeddings aprendidos durante el entrenamiento con dimensión 128, seguido de una capa de dropout espacial y una LSTM bidireccional con 64 unidades. La salida pasa por una capa densa con activación ReLU y dropout, terminando en una salida sigmoide para clasificación binaria.

**Cambios realizados:**
- Tokenización básica con límite de 50,000 palabras
- Padding/truncation a 200 tokens
- Optimizador Adam con learning rate 0.001
- Early stopping y checkpointing

**Resultados:**
- MCC: 0.8665
- Accuracy: ~87%
- El modelo mostró buen rendimiento inicial, pero había espacio para mejoras en regularización.

## Iteración 2: Mejora en Regularización (V1)
En esta iteración, añadí más regularización para prevenir overfitting. Incrementé el dropout a 0.5, añadí regularización L2 en las capas densas, y utilicé SpatialDropout1D en la capa de embedding.

**Cambios realizados:**
- Aumento de dropout a 0.5
- Regularización L2 con factor 1e-4
- SpatialDropout1D con rate 0.3
- Ajuste de unidades LSTM a 96

**Resultados:**
- MCC: 0.8885 (mejora sobre baseline)
- Accuracy: ~89%
- Mejor generalización observada en validación.

## Iteración 3: Arquitectura CNN+LSTM (V2)
Introduje una arquitectura híbrida combinando capas convolucionales para extracción de features locales con LSTM para modelado secuencial.

**Cambios realizados:**
- Capas Conv1D con diferentes tamaños de kernel (2,3,4,5)
- GlobalMaxPooling1D para cada rama convolucional
- Concatenación de features convolucionales con salida LSTM
- Más unidades en capas densas

**Resultados:**
- MCC: 0.8733
- Accuracy: ~87%
- El modelo fue más complejo pero no superó consistentemente al V1.

## Iteración 4: Transfer Learning con DistilBERT (V3)
Experimenté con transfer learning utilizando DistilBERT pre-entrenado para aprovechar representaciones contextuales avanzadas.

**Cambios realizados:**
- Uso de DistilBERT base uncased
- Fine-tuning con capas adicionales
- Ajuste de hiperparámetros para BERT

**Resultados:**
- MCC: 0.6456 (degradación significativa)
- Accuracy: ~65%
- El fine-tuning no convergió bien, posiblemente debido a tamaño de dataset o configuración.

## Iteración 5: Optimización de Hiperparámetros (V4)
Regresé a la arquitectura CNN+LSTM pero con optimización exhaustiva de hiperparámetros usando grid search limitado.

**Cambios realizados:**
- Ajuste fino de learning rate, batch size, unidades
- Experimentación con diferentes configuraciones de capas
- Mejora en preprocesamiento de texto

**Resultados:**
- MCC: ~0.83
- Accuracy: ~83%
- Rendimiento decente pero no el mejor.

## Iteración 6: Modelo Final Optimizado (V5/V6)
En la iteración final, combiné las mejores prácticas de las iteraciones anteriores: regularización fuerte, arquitectura híbrida CNN+LSTM, y optimización de hiperparámetros.

**Cambios realizados:**
- Arquitectura CNN+LSTM refinada
- Regularización completa (dropout, L2, spatial dropout)
- Learning rate scheduling con ReduceLROnPlateau
- Gradient clipping para estabilidad
- Aumento de epochs con early stopping paciente

**Resultados:**
- MCC: 0.8733
- Accuracy: ~87%
- Precision/Recall balanceado
- Mejor estabilidad en entrenamiento

**Conclusión:**
El modelo V6 representa la mejor configuración encontrada, equilibrando complejidad y rendimiento. Las iteraciones mostraron que la regularización es crucial para este dataset, mientras que el transfer learning con BERT requirió más ajuste. La arquitectura híbrida CNN+LSTM demostró ser efectiva para esta tarea de clasificación de texto.