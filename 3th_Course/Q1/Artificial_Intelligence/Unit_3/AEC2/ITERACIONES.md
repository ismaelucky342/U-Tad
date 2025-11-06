# Iteraciones - Dogs vs Cats Competition# Documentación de Iteraciones - Perros vs Gatos



**Autor**: Ismael Hernández Clemente  

**Asignatura**: Inteligencia Artificial - U-Tad  ### Hipótesis/Justificación

**Competición**: Kaggle Dogs vs Cats 2025  

**Objetivo**: Score >0.80 en el leaderboard público## ITERACIÓN 1 - CNN Baseline (DEPRECATED)Mi hipótesis es que una arquitectura CNN básica con BatchNormalization y Dropout debería superar 



---ampliamente el baseline (0.569) al ser capaz de extraer características relevantes de las imágenes.



## Estrategia General**Fecha**: 29/10/2025  El uso de BatchNormalization debería acelerar la convergencia y el Dropout prevenir el overfitting.



Mi plan para esta competición es ir paso a paso, sin quemar etapas. Primero quiero entender el problema con algo simple, una CNN básica para ver cómo se comporta el modelo, identificar problemas y luego ir añadiendo mejoras incrementales. Si al final veo que la CNN no da para más, pues tiro de Transfer Learning.**Estado**: ❌ Movido a MODELOS_DEPRECATED



**Las fases que tenía en mente:**### Resultados Obtenidos

1. **Baseline simple** - Ver qué pasa sin complicarme la vida

2. **Data augmentation** - Intentar controlar el overfitting que seguro va a aparecer### Cambios Realizados

3. **Ajustes finos** - Probar hiperparámetros y callbacks

4. **Transfer Learning** - Si todo lo anterior no funciona bien**Métricas de Entrenamiento:**



Voy a documentar especialmente los errores, porque al final es donde más aprendes. Cada iteración tiene el mismo formato: qué cambié, por qué lo hice, qué pasó y qué aprendí de verdad.Construí una CNN desde cero con arquitectura clásica:- Training Accuracy final: 0.901



---- 3 bloques convolucionales (32→64→128 filtros)- Validation Accuracy (mejor - época 5): 0.811



## ITERACIÓN 1 - CNN Plantilla modificada - BatchNormalization después de cada convolución- Validation Accuracy final (época 12): 0.715



**Fecha**: 29/10/2025  - MaxPooling para reducir dimensionalidad- Validation Loss final: 0.602

**Estado**: DEPRECATED - Movido a la carpeta MODELOS_DEPRECATED

- Capa densa 512 + Dropout 0.5

### Qué hice

- Salida softmax para 2 clases**Métricas de Evaluación:**

Construí la CNN desde cero reutilizando la plantilla y siguiendo el patrón clásico que siguen los materiales de clase del tema 2. Nada especial, solo la estructura típica:

- Supplementary Data Accuracy: 0.653

- 3 bloques convolucionales con filtros que van aumentando (32, 64, 128)

- BatchNormalization después de cada convolución (según leí acelera la convergencia)**Configuración:**- Supplementary Data Loss: 0.918

- MaxPooling para ir reduciendo el tamaño espacial

- Una capa densa de 512 neuronas con Dropout 0.5- Épocas: 12

- Salida con softmax para las 2 clases (perro/gato)

- Optimizer: RMSprop (lr=0.001)**Kaggle Score:**

**Configuración del entrenamiento:**

- 12 épocas- Sin data augmentation- Public Score: [Pendiente]

- Optimizer RMSprop con learning rate 0.001

- Sin data augmentation (quería ver primero qué pasaba sin nada)- Image size: 256x256

- Imágenes redimensionadas a 256x256



### Por qué esta configuración

### Justificación Técnica### Análisis de Curvas de Aprendizaje

La arquitectura la saqué del material de U-Tad  que habíamos visto en clase y 42AI computer vision. Vi que BatchNormalization ayuda bastante con la estabilidad del entrenamiento y el Dropout de 0.5 debería evitar algo de overfitting. Mi idea era empezar con algo simple y ver qué problemas aparecían, en lugar de meterme en algo muy complejo desde el principio.



**Referencias que consulté:**

- Material de 42AI sobre Deep Learning: https://github.com/42-AI/bootcamp_machine-learning La arquitectura se basa en el patrón clásico de CNNs que aprendí en los tutoriales de 42AI sobre computer vision. La idea de usar BatchNormalization viene de ver que acelera convergencia y estabiliza el entrenamiento.**Evolución por épocas clave:**

- Keras docs sobre BatchNormalization: https://keras.io/api/layers/normalization_layers/batch_normalization/



### Resultados**Referencias:**| Época | Train Acc | Val Acc | Train Loss | Val Loss | Estado |



| Métrica | Valor |- 42AI - Introduction to Deep Learning: https://github.com/42-AI/bootcamp_machine-learning|-------|-----------|---------|------------|----------|---------|

|---------|-------|

| Mejor Val Accuracy | 0.811 (época 5) |- Keras Documentation - BatchNormalization: https://keras.io/api/layers/normalization_layers/batch_normalization/| 1     | 0.573     | 0.621   | 26.67      | 0.678    | Aprendiendo |

| Val Accuracy final | 0.715 (época 12) |

| Supplementary Acc | 0.653 || 5     | 0.786     | **0.811** | 0.454    | **0.431** | MEJOR PUNTO |

| Gap Train/Val | 18.6% |

### Resultados| 6     | 0.817     | 0.667   | 0.391      | 0.863    | Colapso |

**Lo que pasó:**

| 12    | 0.901     | 0.715   | 0.216      | 0.602    | Overfitting severo |

El modelo empezó bastante bien, llegó a 0.81 en validación en la época 5 y luego todo se fue al garete. Desde la época 6 el validation loss empezó a subir como loco mientras el training loss seguía bajando tranquilamente. Overfitting clásico de manual.

| Métrica | Valor |

El gap de 18.6% entre training y validation es brutal. Y lo peor es que en supplementary data (datos que no había visto nunca) solo llegó a 0.65, lo que significa que no está generalizando nada bien.

|---------|-------|**Observaciones:**

### Conclusión del modelo?

| Best Val Accuracy | 0.811 (época 5) |- Desde la época 6 se detecta overfitting severo

El modelo tiene capacidad para aprender el problema (lo del 0.81 lo demuestra) pero se está memorizando las imágenes en lugar de aprender patrones generales. Me falta urgentemente data augmentation. Sin eso, el modelo ve las mismas imágenes exactas en cada época y obviamente las memoriza.

Esta primera iteración útil para entender el problema, pero claramente no sirve para producción ni para Kaggle. Siguiente paso: añadir data augmentation para forzarlo a aprender patrones en lugar de memorizar.

**Referencias sobre el problema:**

- Paper sobre overfitting: https://arxiv.org/abs/1409.1556 (sección 3.2)| Gap Train/Val | 18.6% |- Validation loss explota desde época 6 (0.431 → 0.863 → 1.101)



---



## ITERACIÓN 2 - Data Augmentation**Conclusión**: Overfitting brutal desde época 6. El modelo memoriza en lugar de generalizar. Necesita urgentemente data augmentation.### Conclusiones y Próximos Pasos



**Fecha**: 02/11/2025  

**Estado**: DEPRECATED - Movido a carpeta MODELOS_DEPRECATED

---**Lo que funcionó bien:**

### Qué hice

- ✅ La arquitectura base es sólida: supera el baseline en +10-24 puntos según época

Mantuve exactamente la misma arquitectura pero añadí data augmentation bastante agresivo:

## ITERACIÓN 2 - Data Augmentation (DEPRECATED)- ✅ BatchNormalization ayuda a la convergencia

- RandomFlip horizontal (los perros y gatos pueden mirar en cualquier dirección)

- RandomRotation hasta 36° (para simular diferentes ángulos de cámara)- ✅ El modelo aprende características relevantes (llega a 0.81 en validación)

- RandomZoom del 20% (simular diferentes distancias)

- RandomTranslation del 10% (los animales no siempre están centrados)**Fecha**: 02/11/2025  

- Subí el Dropout de 0.5 a 0.6 para forzar más regularización

- Añadí Early Stopping y ReduceLROnPlateau como red de seguridad**Estado**: ❌ Movido a MODELOS_DEPRECATED**Problemas detectados:**

- Dejé hasta 25 épocas pero con early stopping por si acaso

- ❌ **Overfitting severo** desde época 6

### Por qué esta configuración

### Cambios Realizados- ❌ Sin data augmentation, el modelo memoriza en lugar de generalizar

Después del desastre de overfitting de la Iter1, me puse a investigar sobre data augmentation. Vi varios videos de Yannic Kilcher donde explica que cuando tienes pocos datos (y 12,500 imágenes es relativamente poco para deep learning), el augmentation es absolutamente crítico para generalización.

- ❌ Dropout 0.5 no es suficiente para prevenir overfitting

La idea es que cada época el modelo vea versiones ligeramente diferentes de las mismas imágenes (rotadas, volteadas, con zoom), forzándolo a aprender características invariantes en lugar de memorizar pixeles exactos. Es como estudiar entendiendo los conceptos en lugar de memorizar las respuestas literales.

Mismo modelo pero con data augmentation agresivo:- ❌ Gap enorme entre validation (0.715) y supplementary data (0.653)

El Early Stopping lo añadí para que pare automáticamente si empieza a sobreajustar, y el ReduceLROnPlateau para hacer ajustes más finos cuando se acerque al óptimo (reduce el learning rate cuando el validation loss deja de mejorar).

- RandomFlip horizontal

**Referencias que me ayudaron:**

- Video de Yannic Kilcher sobre Data Augmentation: https://www.youtube.com/watch?v=Zrp2b8qXHYk- RandomRotation (±36°)**Diagnóstico:**

- Keras guide sobre preprocessing layers: https://keras.io/guides/preprocessing_layers/

- Paper "The Effectiveness of Data Augmentation": https://arxiv.org/abs/1712.04621- RandomZoom (±20%)El modelo tiene capacidad para aprender el problema (lo demuestra el 0.81 en época 5), pero 

- Recomendaciones de Fast.ai sobre augmentation: https://docs.fast.ai/vision.augment.html

- RandomTranslation (±10%)**necesita urgentemente regularización adicional mediante data augmentation** para mejorar 

### Resultados

- Dropout aumentado a 0.6la generalización.

| Métrica | Iter 1 | Iter 2 | Cambio |

|---------|--------|--------|--------|- Early Stopping + ReduceLROnPlateau

| Val Accuracy | 0.811 | 0.868 | +7.0% |

| Supplementary Acc | 0.653 | 0.753 | +15.3% |- Épocas: 25**Próximos pasos para Iteración 2:**

| Gap Train/Val | 18.6% | 5.3% | -13.3% |

| Épocas útiles | 5 | 25 | +20 |1. **CRÍTICO**: Implementar Data Augmentation (rotaciones, flips, zoom)



**Lo que pasó:**### Justificación Técnica2. Añadir Early Stopping para parar cuando val_loss empiece a subir



Cambio brutal. El modelo entrenó las 25 épocas completas sin colapsar. La validation accuracy llegó a 0.868, pero lo realmente importante es que en supplementary data (datos totalmente nuevos) subió de 0.65 a 0.75. Eso significa que está generalizando mucho mejor.3. Aumentar Dropout de 0.5 a 0.6



El gap train/val bajó de 18.6% a 5.3%, que es totalmente razonable y manejable. Sí hubo una pequeña caída en la época 22 pero se recuperó bien.Después de ver el desastre de la Iteración 1, investigué sobre data augmentation. Vi varios videos de Yannic Kilcher explicando que en problemas con pocos datos, el augmentation es crítico para generalización. La idea es que cada época vea versiones diferentes de las mismas imágenes, forzando al modelo a aprender patrones invariantes.4. Considerar aumentar épocas a 20 con early stopping



### Qué aprendí de verdad5. Probar con ReduceLROnPlateau para ajustar learning rate dinámicamente



**Lección clave que me llevo:** En clasificación de imágenes con datasets limitados, data augmentation no es algo opcional que añades si te sobra tiempo. Es absolutamente obligatorio desde el primer momento. La diferencia es brutal: +15.3% en supplementary data, que son los datos que realmente importan.**Referencias:**



A partir de ahora todas las iteraciones van a llevar data augmentation por defecto. No tiene sentido no usarlo, es regalar rendimiento gratis.- Yannic Kilcher - Data Augmentation in Deep Learning: https://www.youtube.com/watch?v=Zrp2b8qXHYk**Objetivo Iteración 2:** 



**Referencias sobre por qué funciona:**- Keras Guide - Image Data Augmentation: https://keras.io/guides/preprocessing_layers/- Validation Accuracy: 0.82-0.85

- Fast.ai lesson sobre augmentation: https://course.fast.ai/ (Lesson 5)

- CS231n sobre regularization: http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture7.pdf- Paper - "The Effectiveness of Data Augmentation in Image Classification": https://arxiv.org/abs/1712.04621- Eliminar overfitting y mantener consistencia entre train/val/test



---- Kaggle Score esperado: 0.78-0.82



## RESUMEN Iteraciones 1-2### Resultados



**Lo más importante que aprendí hasta aquí:**### Referencias



El data augmentation cambió completamente el juego. No es una mejora incremental, es un cambio fundamental en cómo el modelo aprende. La diferencia entre 0.65 y 0.75 en datos nuevos es enorme en términos prácticos.| Métrica | Iteración 1 | Iteración 2 | Mejora |- Documentación de Keras Data Augmentation: https://keras.io/api/layers/preprocessing_layers/



**Números clave:**|---------|-------------|-------------|--------|- BatchNormalization: https://keras.io/api/layers/normalization_layers/batch_normalization/

- +7% en validation (bien)

- +15.3% en generalización (excelente)| Val Accuracy | 0.811 | **0.868** | +7.0% |- Dropout: https://keras.io/api/layers/regularization_layers/dropout/

- -13.3 puntos de overfitting (crítico)

| Supplementary Acc | 0.653 | **0.753** | +15.3% |

En este punto pensé que esto estaba listo para Kaggle. Spoiler: no lo estaba ni de cerca.

| Gap Train/Val | 18.6% | **5.3%** | -13.3% |---

---



## ITERACIÓN 3 - Primer Submit Kaggle

**Conclusión**: Éxito rotundo. Data augmentation resolvió el overfitting completamente. El modelo entrenó 25 épocas estables vs 5 útiles en Iter1.## ITERACIÓN 2 - Data Augmentation + Early Stopping + ReduceLROnPlateau

**Fecha**: 04/11/2025  

**Estado**: DEPRECATED - Movido a carpeta MODELOS_DEPRECATED  

**Kaggle Score**: 0.58768 (DESASTRE TOTAL)

---**Fecha**: 05/11/2025

### Qué hice



Re-entrené el modelo de Iter2 con una semilla aleatoria diferente para ver si conseguía algún punto extra. Mismo setup exacto, solo cambió la inicialización aleatoria de los pesos.

## 📊 RESUMEN ITERACIONES 1-2: APRENDIZAJE CLAVE### Descripción del Cambio

### Por qué esta configuración



Quería probar si con diferente inicialización conseguía mejor performance. En deep learning la inicialización aleatoria puede cambiar bastante los resultados finales, así que no está de más probar.

**Lección principal**: En problemas de clasificación de imágenes con datasets limitados, **data augmentation no es opcional, es obligatorio**. La diferencia entre 0.65 y 0.75 en supplementary data es brutal.Basándome en los resultados de la Iteración 1 (overfitting severo), he implementado las siguientes mejoras:

**Referencias sobre inicialización:**

- Discusiones de Kaggle sobre variabilidad: https://www.kaggle.com/c/dogs-vs-cats/discussion

- Foros de 42 sobre reproducibilidad en ML

**Números clave:****1. Data Augmentation integrado en el modelo:**

### Resultados

- Mejora validation: +7.0%- RandomFlip horizontal

| Métrica | Valor |

|---------|-------|- Mejora generalización: +15.3%- RandomRotation (±36°, factor 0.1)

| Val Accuracy | 0.858 |

| Supplementary Acc | 0.653 |- Reducción overfitting: -13.3 puntos gap- RandomZoom (±20%, factor 0.2)

| Kaggle Score | 0.58768 |

| Diferencia esperado/real | -29% |- RandomTranslation (±10% en altura y anchura)



**Lo que pasó:****Decisión**: Todas las iteraciones futuras incluirán data augmentation por defecto.



DESASTRE ABSOLUTO. Yo esperaba un score de 0.83-0.85 basándome en la validation accuracy, pero me salió 0.587. Algo estaba muy mal y no tenía ni idea de qué.**2. Regularización mejorada:**



Después de analizar el submission.csv línea por línea, descubrí el problema: el modelo predijo 64% perros y solo 36% gatos. En un dataset balanceado 50/50 como este, esto explica perfectamente el score de ~58%. Si predices más perros de lo que deberías, pierdes muchos puntos.---- Dropout aumentado: 0.5 → 0.6



### Qué aprendí de verdad



**Lección brutal que me costó un submission:** La validation accuracy local puede mentir descaradamente. El modelo estaba sesgado hacia predecir más perros y las métricas locales no me avisaron de esto hasta que subí a Kaggle y vi el desastre.## ITERACIÓN 3 - Primer Submit Kaggle (DEPRECATED)**3. Control inteligente del entrenamiento:**



**Problemas identificados:**- Early Stopping (monitor='val_loss', patience=5, restore_best_weights=True)

1. Usar categorical crossentropy + softmax puede dar probabilidades sesgadas entre clases

2. Usar np.argmax() sin verificar la distribución de predicciones es peligroso**Fecha**: 04/11/2025  - ReduceLROnPlateau (factor=0.5, patience=3, min_lr=1e-7)

3. El early stopping paró muy pronto (época 15) y quizás no dejó aprender bien

**Estado**: ❌ Movido a MODELOS_DEPRECATED  

**Referencias que consulté para entender el problema:**

- Stack Overflow - Binary vs Categorical: https://stackoverflow.com/questions/47034888/**Kaggle Score**: 0.58768 💀**4. Más épocas permitidas:**

- Kaggle discussions sobre predicciones desbalanceadas: https://www.kaggle.com/discussions/getting-started/27270

- Épocas: 12 → 25 (con early stopping para no desperdiciar)

Necesito cambiar urgentemente a binary classification y verificar las predicciones antes de enviar a Kaggle.

### Cambios Realizados

---

**Configuración mantenida:**

## ITERACIÓN 4 - Bug Fixes

Re-entrenamiento del modelo Iter2 con diferente semilla aleatoria para probar variabilidad. Mismo setup exacto pero early stopping activado en época 15.- Arquitectura: 3 bloques Conv (32, 64, 128) + BatchNorm + MaxPooling

**Fecha**: 05/11/2025  

**Estado**: DEPRECATED - Movido a carpeta MODELOS_DEPRECATED  - Optimizador: RMSprop (lr=0.001 inicial)

**Kaggle Score**: 0.54664 (AÚN PEOR)

### Resultados- Batch size: 125

### Qué hice

- Image size: 256x256

Corregí todo lo que vi mal en Iter3:

| Métrica | Valor |

- Cambié de categorical a binary classification

- Cambié la capa de salida de softmax(2) a sigmoid(1)|---------|-------|### Hipótesis/Justificación

- Predicciones con umbral explícito 0.5 en lugar de usar np.argmax() ciegamente

- Quité el early stopping, dejé 20 épocas fijas para que aprenda bien| Val Accuracy | 0.858 |

- Cambié a optimizer Adam (más estable según leí)

| Supplementary Acc | 0.653 |**Problema identificado en Iteración 1:**

### Por qué esta configuración

| **Kaggle Score** | **0.58768** |El modelo sufría de overfitting severo porque memorizaba las imágenes exactas del conjunto de entrenamiento. Sin variaciones en los datos, después de 5-6 épocas comenzaba a sobreajustarse.

Investigué bastante en los foros de 42 y en discusiones de Kaggle. Básicamente vi que para problemas binarios, usar binary crossentropy con sigmoid es más estable matemáticamente que categorical con softmax. El umbral 0.5 explícito elimina cualquier ambigüedad en la conversión de probabilidades a clases.



**Referencias que me salvaron:**

- Material de 42AI sobre binary classification: https://github.com/42-AI/bootcamp_python**Diferencia esperado vs real**: -29% 💀**Hipótesis de mejora:**

- Curso de Andrew Ng sobre binary vs multiclass: https://www.coursera.org/learn/machine-learning (Week 6)

- Keras best practices: https://keras.io/examples/Con data augmentation, cada época verá versiones ligeramente diferentes de las mismas imágenes (rotadas, volteadas, con zoom, desplazadas). Esto debería:



### Resultados### Análisis del Desastre1. Forzar al modelo a aprender características generales en lugar de memorizar



| Métrica | Valor |2. Permitir entrenar más épocas sin overfitting

|---------|-------|

| Val Accuracy | 0.742 |Después de analizar el submission.csv, descubrí que el modelo predijo **64% perros y 36% gatos**. En un dataset balanceado 50/50, esto explica perfectamente el score ~58%.3. Mejorar la generalización en datos nuevos (supplementary y test)

| Supplementary Acc | 0.603 |

| Distribución predicciones | 40% gatos / 60% perros |

| Kaggle Score | 0.54664 |

**Causas identificadas:**El Early Stopping evitará desperdiciar tiempo si el modelo converge antes de 25 épocas, y ReduceLROnPlateau hará ajustes más finos cuando el modelo se acerque al óptimo.

**Lo que pasó:**

1. Categorical crossentropy + softmax puede dar probabilidades sesgadas

TODAVÍA PEOR que antes. El score bajó de 0.587 a 0.546. Me quedé en shock.

2. np.argmax() sin verificación de distribución**Objetivo cuantitativo:**

La distribución de predicciones ahora sí está más balanceada (40/60 es aceptable), así que el bug de predicción está efectivamente arreglado. Pero el score sigue siendo horrible.

3. Early stopping paró demasiado pronto (época 15)- Validation accuracy: 0.82-0.85 (vs 0.811 mejor de Iter1)

**Diagnóstico real:** El problema no era solo el bug de predicción. El problema fundamental es que la CNN desde cero simplemente NO GENERALIZA bien:

- Validation: 74% (más o menos aprende el validation set)- Supplementary accuracy: 0.78-0.82 (vs 0.653 de Iter1)

- Supplementary: 60% (empieza a fallar con datos nuevos)

- Kaggle: 54% (falla completamente con el test real)**Referencias:**- Gap train/val: <8 puntos (vs 18.6 de Iter1)



### Qué aprendí de verdad- Stack Overflow - Binary vs Categorical Crossentropy: https://stackoverflow.com/questions/47034888/- Eliminar el colapso de validation loss



**Reality check durísimo:** CNN desde cero tiene demasiada variabilidad entre entrenamientos. No es estable. Con solo 3 submissions restantes no puedo seguir apostando por esto, es tirar submissions a la basura.- Kaggle Discussion - Imbalanced Predictions: https://www.kaggle.com/discussions/getting-started/27270



La validation accuracy alta no te garantiza absolutamente nada en Kaggle. El modelo puede estar sobreajustando incluso al propio validation set.### Resultados Obtenidos



**Decisión crítica:** Es momento de dejar la CNN desde cero y pasar a Transfer Learning. Ya no es una opción para "si hace falta", es una necesidad urgente.**Conclusión**: El modelo local no es tan bueno como parecía. Necesito corregir bugs de predicción y cambiar a binary classification.



**Referencias que me convencieron:****Métricas de Entrenamiento:**

- CS231n sobre transfer learning: http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture11.pdf

- Fast.ai explicando cuándo usar TL: https://course.fast.ai/ (spoiler: casi siempre)---- Training Accuracy final: 0.8158



---- Validation Accuracy final (época 25): **0.8684** **RÉCORD ABSOLUTO**



## RESUMEN Iteraciones 3-4: Lección de humildad## ITERACIÓN 4 - Bug Fixes (DEPRECATED)- Validation Loss final: 0.3310



**Lo que aprendí de la forma más dura posible:**- Total épocas completadas: 25 (sin early stopping)



- Val accuracy 74% → Kaggle 54% (pérdida de 20 puntos)**Fecha**: 05/11/2025  - Mejores pesos: Restaurados desde época 25

- 2 submissions completamente desperdiciados

- Posición en el ranking: bottom**Estado**: ❌ Movido a MODELOS_DEPRECATED  



**La lección:** No puedes confiar ciegamente en las métricas locales. El modelo puede estar memorizando incluso el validation set. Y la CNN desde cero tiene demasiada variabilidad entre entrenamientos diferentes.**Kaggle Score**: 0.54664 💀💀**Evolución por épocas clave Iteración 2:**



**Decisión crítica:** Transfer Learning. Los modelos pre-entrenados como VGG16 o ResNet ya aprendieron features generales de millones de imágenes. Solo necesito ajustar las últimas capas para mi problema específico (perros vs gatos).



---### Cambios Realizados| Época | Train Acc | Val Acc | Train Loss | Val Loss | LR | Estado |



## ITERACIÓN 5 - Transfer Learning VGG16|-------|-----------|---------|------------|----------|-----|---------|



**Fecha**: 05/11/2025  **Correcciones críticas:**| 8     | 0.698     | 0.735   | 0.582      | 0.507    | 1e-3 | Mejora estable |

**Estado**: MODELO ACTIVO  

**Kaggle Score**: 0.86380  - Categorical → **Binary classification**| 11    | 0.727     | 0.733   | 0.549      | 0.517    | 5e-4 | LR reducido (época 11) |

**Ranking**: 7 de ~50 participantes (Top 15%)

- Softmax(2) → **Sigmoid(1)**| 18    | 0.781     | 0.841   | 0.463      | 0.397    | 5e-4 | Ascenso pronunciado |

### Qué hice

- np.argmax() → **Umbral explícito 0.5**| 20    | 0.787     | 0.846   | 0.447      | 0.379    | 5e-4 | Pico temporal |

Cambio radical de arquitectura, dejé la CNN desde cero y tiré de Transfer Learning:

- Épocas fijas: 20 (sin early stopping)| 21    | 0.790     | 0.848   | 0.445      | 0.359    | 5e-4 | Máximo previo |

- Base: VGG16 pre-entrenado en ImageNet (14 millones de imágenes)

- TODAS las capas convolucionales congeladas (no las entreno)- Optimizer: Adam (más estable que RMSprop)| 22    | 0.790     | 0.717   | 0.441      | 1.034    | 5e-4 | Caída dramática |

- Solo entreno una cabecera simple encima: Dense(256) + Dropout(0.5) + Dense(1)

- Binary classification con sigmoid| 23    | 0.794     | 0.820   | 0.432      | 0.400    | 5e-4 | Recuperación |

- Imágenes 224x224 (lo que VGG16 necesita)

### Justificación Técnica| 24    | 0.799     | 0.826   | 0.429      | 0.381    | 2.5e-4 | LR reducido (época 24) |

**Setup del entrenamiento:**

- 15 épocas (Transfer Learning converge mucho más rápido)| **25** | **0.816** | **0.868** | **0.397** | **0.331** | **2.5e-4** | **EXPLOSIÓN FINAL** |

- Learning rate 0.0001 (muy bajo para fine-tuning, no queremos romper los pesos pre-entrenados)

- Data augmentation más conservador (Transfer Learning no necesita tanto)Después de investigar en los foros de 42 y Kaggle, vi que para problemas binarios, usar binary crossentropy con sigmoid es más estable que categorical con softmax. La conversión directa con umbral 0.5 elimina ambigüedad.

- Tiempo de entrenamiento: 11 minutos vs 20 minutos de la CNN

**Métricas de Evaluación:**

### Por qué esta configuración

**Referencias:**- Supplementary Data Accuracy: **0.7533**

Transfer Learning es el estándar de la industria cuando no tienes millones de imágenes para entrenar desde cero. VGG16 ya aprendió a detectar bordes, texturas, formas, patrones complejos en 14 millones de imágenes de ImageNet. 

- 42AI - Binary Classification Best Practices: https://github.com/42-AI/bootcamp_python- Supplementary Data Loss: 0.6736

Al congelar sus capas convolucionales, lo que hago es aprovechar todo ese conocimiento pre-aprendido y solo entrenar la decisión final "esto es un perro o un gato" sobre esas features ya extraídas. Es mucho más eficiente y estable.

- Andrew Ng - Binary vs Multiclass: https://www.coursera.org/learn/machine-learning

Esto lo saqué directamente de los tutoriales de Stanford CS231n y las recomendaciones de fast.ai que básicamente dicen "usa transfer learning siempre que puedas, no seas héroe intentando entrenar desde cero".

**Kaggle Score:**

**Referencias clave que seguí:**

- Stanford CS231n sobre Transfer Learning: http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture11.pdf (slides 15-30)### Resultados- Public Score: [EXPERIMENTAL - No enviado]

- Fast.ai Practical Deep Learning: https://course.fast.ai/ (Lesson 1 ya usa TL)

- Keras Transfer Learning Guide: https://keras.io/guides/transfer_learning/- Private Score: [EXPERIMENTAL - No enviado]

- Paper original de VGG16: https://arxiv.org/abs/1409.1556

- Video de Aladdin Persson explicando VGG16: https://www.youtube.com/watch?v=ACmuBbuXn20| Métrica | Valor |



### Resultados|---------|-------|### Análisis de Resultados - Comparación Iteraciones



| Métrica | CNN Iter 4 | VGG16 | Mejora || Val Accuracy | 0.742 |

|---------|------------|-------|--------|

| Val Accuracy | 0.742 | 0.975 | +31.4% || Supplementary Acc | 0.603 |**COMPARATIVA ITERACIÓN 1 vs 2:**

| Val Precision | 0.842 | 0.966 | +14.8% |

| Val Recall | 0.605 | 0.985 | +62.8% || Distribución Submit | 40% gatos / 60% perros ✓ |

| Val Loss | 0.586 | 0.075 | -87.2% |

| Kaggle Score | 0.547 | 0.864 | +58.0% || **Kaggle Score** | **0.54664** 💀💀 || Métrica | Iteración 1 | Iteración 2 | Mejora | Estado |

| Tiempo entrenamiento | 20 min | 11 min | -45% |

|---------|-------------|-------------|--------|---------|

**Lo que pasó:**

**¡PEOR QUE ANTES!** Score bajó de 0.58768 a 0.54664.| **Mejor Val Acc** | 0.811 (época 5) | **0.868** (época 25) | +**7.04%** | ÉXITO EXTRAORDINARIO |

ÉXITO TOTAL. En 11 minutos de entrenamiento conseguí mejor resultado que 3 días iterando con CNN desde cero. Ni comparación.

| **Supplementary Acc** | 0.653 | **0.753** | +**15.3%** | ÉXITO NOTABLE |

El modelo alcanzó 0.975 de validation accuracy con precision y recall perfectamente balanceados (96.6% vs 98.5%). El loss bajísimo (0.075) muestra que el modelo está muy confiado en sus predicciones, no está dudando.

### Análisis del Segundo Desastre| **Estabilidad** | Colapso época 6 | Estable 25 épocas | +**19 épocas** | ÉXITO TOTAL |

**Score Kaggle 0.86380:**

- Posición 7 de aproximadamente 50 participantes| **Overfitting** | Severo desde época 6 | Completamente controlado | Resuelto | ÉXITO TOTAL |

- Top 15% del ranking

- Gap con el primer puesto (0.968): -10.4%La distribución está balanceada (40/60 es aceptable) pero el score es horrible. Esto significa que **el modelo CNN desde cero simplemente NO GENERALIZA**.| **Gap Train/Val** | 18.6 puntos | 5.26 puntos | **-13.34 puntos** | ÉXITO TOTAL |

- Gap con el tercero (0.957): -9.3%

| **Mejora vs Baseline** | +42.5% | **+52.6%** | +**10.1 puntos** | EXCEPCIONAL |

### Qué aprendí de verdad

**Diagnóstico:**

**Por qué funcionó tan bien:**

- Val: 74% (aprende validación)### Conclusiones y Próximos Pasos

VGG16 elimina completamente toda la variabilidad y los problemas de entrenar desde cero. Las features pre-aprendidas son muy robustas y generalizan increíblemente bien porque fueron entrenadas con millones de imágenes variadas.

- Supp: 60% (empieza a fallar)

Binary classification + umbral 0.5 explícito es mucho más estable que categorical para problemas de 2 clases. Y lo más importante: verifiqué la distribución de predicciones antes de enviar a Kaggle (está perfectamente balanceada).

- Kaggle: **54%** (falla completamente)**Lo que funcionó EXCELENTE:**

**Conclusión:** Transfer Learning fue absolutamente la decisión correcta. Debería haberlo usado desde el principio, me habría ahorrado 3 días de iteraciones fallidas y 2 submissions desperdiciados. La lección es clara: no intentes ser héroe entrenando CNNs complejas desde cero cuando tienes modelos pre-entrenados disponibles.

- **Data Augmentation es LA CLAVE**: Resolvió completamente el overfitting

**Referencias sobre por qué TL funciona:**

- Paper sobre feature transfer: https://papers.nips.cc/paper/5347-how-transferable-are-features-in-deep-neural-networks**Conclusión brutal**: CNN desde cero tiene demasiada variabilidad y no es estable para este problema. Con solo 3 submissions restantes, no puedo seguir apostando por esto.- **Mejor resultado histórico**: 0.848 val_accuracy (+3.7% vs Iter1)  

- Blog de Jeremy Howard (fast.ai) sobre TL: https://www.fast.ai/posts/2016-10-08-teaching-philosophy.html

- **Estabilidad dramáticamente mejorada**: 15 épocas adicionales sin colapso

---

---- **Gap train/val controlado**: De 18.6 a ~5.8 puntos

## RESUMEN FINAL: De 0.54 a 0.86

- **ReduceLROnPlateau efectivo**: Ajustes finos automáticos

**Timeline completo del proyecto:**

## 📊 RESUMEN ITERACIONES 3-4: LECCIÓN DE HUMILDAD- **Early Stopping como red de seguridad**: Protege contra inestabilidad tardía

| Iter | Modelo | Val Acc | Kaggle | Aprendizaje clave |

|------|--------|---------|--------|-------------------|

| 1 | CNN base | 0.811 | - | Overfitting brutal sin augmentation |

| 2 | + Augmentation | 0.868 | - | Augmentation es obligatorio |**Realidad check**: Validation accuracy alta NO GARANTIZA buen score en Kaggle. El modelo sobreajustó al validation set también.**Problema detectado (épocas 22-23):**

| 3 | Re-train | 0.858 | 0.588 | Val accuracy puede mentir |

| 4 | Bug fixes | 0.742 | 0.547 | CNN desde cero no generaliza bien |- **Inestabilidad tardía**: Caída súbita de 0.848 → 0.717 en época 22

| 5 | VGG16 TL | 0.975 | 0.864 | Transfer Learning funciona |

**Números brutales:**- **Posible causa**: Learning rate muy bajo (5e-4) creando fluctuaciones

**Mejora total:** 0.547 → 0.864 = +58% de score (de bottom a top 15%)

- Val accuracy: 74% → Kaggle: **54%** (-20%)- **Protección**: Early stopping recuperará mejores pesos (época 21)

**Las 5 lecciones clave que me llevo:**

- 2 submissions desperdiciados

1. **Data augmentation no es opcional** en computer vision con datos limitados (Iter 1→2)

2. **Validation accuracy local puede mentir brutalmente**, no confíes ciegamente (Iter 2→3)- Ranking: Bottom del leaderboard**Resultados finales y Predicción Ranking:**

3. **Binary classification es más estable que categorical** para problemas de 2 clases (Iter 3→4)

4. **CNN desde cero tiene demasiada variabilidad** para ser confiable en producción (Iter 1-4)- **Validation accuracy final**: **0.8684** (época 25)

5. **Transfer Learning es el camino correcto desde el principio**, no la última opción (Iter 5)

**Decisión crítica**: Abandonar CNN desde cero. Es el momento de **Transfer Learning**.- **Supplementary accuracy**: **0.7533** (excelente generalización)

**Posición actual:** 7 de 50 (Top 15%)  

**Submissions restantes:** 2 de 5  - **Public leaderboard estimado**: **0.83-0.87** (basado en val_acc)

**Margen de mejora:** ~10 puntos hasta top 3

**Justificación**: Los modelos pre-entrenados (VGG16, ResNet) ya aprendieron features generales de millones de imágenes. Solo necesito ajustar las últimas capas para perros vs gatos. Esto debería ser mucho más estable.- **Posición esperada**: **Top 15-20%** (muy competitivo)

---

- **Mejora vs baseline (0.569)**: +**52.6%** (extraordinario)

## Próximos Pasos

---- **Gap val/supplementary**: 11.5 puntos (razonable para generalización)

Con 2 submissions restantes y estando en posición 7, tengo básicamente tres opciones:



**Opción A - Fine-tuning VGG16:**

- Descongelar las últimas 2-3 capas convolucionales del VGG16## ITERACIÓN 5 - Transfer Learning VGG16 ✅**Estrategia Iteración 3 (si fuera necesaria):**

- Learning rate muy bajo (1e-5 o menos)

- **Riesgo:** Puede empeorar si sobreajusto los pesos pre-entrenados1. **Transfer Learning**: VGG16/ResNet50 pre-entrenado

- **Potencial:** +2-4% de score

**Fecha**: 05/11/2025  2. **Learning Rate Scheduling**: Cosine annealing 

**Opción B - Ensemble de modelos:**

- Entrenar VGG16 + ResNet50 por separado**Estado**: ✅ **MODELO ACTIVO**  3. **Ensemble**: Promedio de múltiples modelos

- Promediar las predicciones de ambos

- **Riesgo:** Puede que no mejore mucho para el esfuerzo**Kaggle Score**: 0.86380 🎯  4. **Image size**: 224x224 → 384x384 para más detalles

- **Potencial:** +1-3% de score

**Ranking**: #7 de ~50 participantes

**Opción C - Test Time Augmentation (TTA):**

- Predecir cada imagen 5 veces con transformaciones diferentes (rotaciones, flips)**VEREDICTO ITERACIÓN 2:**

- Promediar los resultados de las 5 predicciones

- **Riesgo:** Muy bajo, casi seguro que mejora algo### Cambios Realizados**ÉXITO EXCEPCIONAL** - Objetivos ampliamente superados:

- **Potencial:** +1-2% de score

- Objetivo: >0.82 → **Conseguido: 0.8684** (+5.8% extra)

**Mi decisión:** Voy a probar primero **Test Time Augmentation (Opción C)** porque es la opción de menor riesgo y casi seguro que da alguna mejora. Si funciona bien y mejoro posición, uso el último submission para probar ensemble o fine-tuning dependiendo de cómo esté el ranking.

**Arquitectura completamente nueva:**- Supplementary: esperado 0.78-0.82 → **Conseguido: 0.7533** 

**Referencias para próximos pasos:**

- TTA tutorial: https://machinelearningmastery.com/how-to-use-test-time-augmentation-to-improve-model-performance-for-image-classification/- Base: VGG16 pre-entrenado en ImageNet- Overfitting: **Completamente eliminado**

- Fine-tuning guide: https://keras.io/guides/transfer_learning/ (sección "Fine-tuning")

- Ensemble methods: https://www.kaggle.com/getting-started/18153- Todas las capas convolucionales **CONGELADAS**- Generalización: **Excelente** (gap razonable val/supp)



---- Cabecera personalizada: Dense(256) + Dropout(0.5) + Dense(1)- Ranking: **Top 15-20% probable**



## Referencias Generales- Binary classification con sigmoid



### Cursos y Material Educativo- Image size: 224x224 (requerido por VGG16)**Status: EXPERIMENTAL - No enviado a Kaggle**

- **42AI Bootcamp Machine Learning**: https://github.com/42-AI (material que usamos en clase)

- **Stanford CS231n** - CNNs for Visual Recognition: http://cs231n.stanford.edu/ (EL curso de referencia)

- **Fast.ai Practical Deep Learning**: https://course.fast.ai/ (muy práctico, menos teoría)

- **Andrew Ng Deep Learning Specialization**: https://www.coursera.org/specializations/deep-learning (más teórico)**Configuración:****Conclusión técnica:**



### Papers Importantes- Épocas: 15 (TL converge rápido)La combinación de Data Augmentation + ReduceLROnPlateau + Early Stopping ha demostrado ser **altamente efectiva** para esta arquitectura CNN desde cero. El modelo ha alcanzado un nivel de rendimiento **excepcional** que rivaliza con arquitecturas más complejas.

- **VGG16 Paper** (Simonyan & Zisserman, 2014): https://arxiv.org/abs/1409.1556

- **Data Augmentation Paper** (Perez & Wang, 2017): https://arxiv.org/abs/1712.04621- Learning rate: 0.0001 (muy bajo para fine-tuning)

- **Transfer Learning Survey** (Pan & Yang, 2010): https://ieeexplore.ieee.org/document/5288526

- **Feature Transferability**: https://papers.nips.cc/paper/5347-how-transferable-are-features-in-deep-neural-networks- Data augmentation: Conservador (TL no necesita tanto)---



### Documentación Técnica- Tiempo entrenamiento: 11 minutos vs 20 min CNN

- **Keras Documentation**: https://keras.io/ (mi referencia principal)

- **TensorFlow Transfer Learning Tutorial**: https://www.tensorflow.org/tutorials/images/transfer_learning## ITERACIÓN 3 - Re-entrenamiento con Diferente Inicialización

- **Kaggle Learn Computer Vision**: https://www.kaggle.com/learn/computer-vision

### Justificación Técnica

### Videos YouTube

- **Yannic Kilcher - Data Augmentation**: https://www.youtube.com/watch?v=Zrp2b8qXHYk (explica muy bien por qué funciona)**Fecha**: 05/11/2025

- **Aladdin Persson - VGG16 Explained**: https://www.youtube.com/watch?v=ACmuBbuXn20 (implementación desde cero)

- **StatQuest - Neural Networks**: https://www.youtube.com/watch?v=CqOfi41LfDw (para entender conceptos base)Transfer Learning es el estándar en computer vision cuando no tienes millones de imágenes. VGG16 ya aprendió features como bordes, texturas y formas en 14M de imágenes de ImageNet. Congelando sus capas, solo entreno la decisión final "¿esto es perro o gato?" sobre esas features pre-aprendidas.



### Comunidad y Foros### Descripción del Cambio

- **Kaggle Dogs vs Cats Discussions**: https://www.kaggle.com/c/dogs-vs-cats/discussion

- **Stack Overflow Deep Learning**: https://stackoverflow.com/questions/tagged/deep-learningLa idea viene de los tutoriales de Stanford CS231n y las recomendaciones de fast.ai sobre "cuando usar transfer learning" (respuesta: siempre que puedas).

- **Reddit r/MachineLearning**: https://www.reddit.com/r/MachineLearning/

Re-entrenar el **mismo modelo** de la Iteración 2 con **diferente semilla aleatoria** para explorar variabilidad en el entrenamiento y potencialmente conseguir mejor performance.

---

**Referencias:**

**Última actualización:** 06/11/2025  

**Estado:** ACTIVO - Top 15% del ranking  - Stanford CS231n - Transfer Learning: http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture11.pdf**Configuración idéntica a Iteración 2:**

**Próxima iteración:** Test Time Augmentation para intentar top 10

- Fast.ai - Practical Deep Learning: https://course.fast.ai/- Arquitectura: 3 bloques Conv (32, 64, 128) + BatchNorm + MaxPooling

- Keras Tutorial - Transfer Learning Guide: https://keras.io/guides/transfer_learning/- Data Augmentation: RandomFlip, RandomRotation, RandomZoom, RandomTranslation

- Paper VGG16 - "Very Deep Convolutional Networks": https://arxiv.org/abs/1409.1556- Dropout: 0.6

- YouTube - Aladdin Persson VGG16 Explained: https://www.youtube.com/watch?v=ACmuBbuXn20- Early Stopping + ReduceLROnPlateau

- Optimizador: RMSprop (lr=0.001 inicial)

### Resultados- Batch size: 125, Image size: 256x256



| Métrica | CNN Iter 4 | VGG16 Iter 5 | Mejora |### Hipótesis/Justificación

|---------|------------|--------------|--------|

| Val Accuracy | 0.742 | **0.975** | +31.4% |**Concepto de re-entrenamiento aleatorio:**

| Val Precision | 0.842 | **0.966** | +14.8% |En deep learning, diferentes inicializaciones de pesos pueden llevar a resultados significativamente diferentes. La Iteración 2 consiguió 0.8684, pero existe la posibilidad de que una nueva inicialización encuentre un mínimo local mejor o peor.

| Val Recall | 0.605 | **0.985** | +62.8% |

| Val Loss | 0.586 | **0.075** | -87.2% |**Ventajas esperadas:**

| **Kaggle Score** | 0.547 | **0.864** | **+58.0%** |- Posible mejora sobre 0.8684 con mejor inicialización

| Tiempo | 20 min | **11 min** | -45% |- Early stopping más efectivo (evitar inestabilidad épocas 22-23)

- Menor tiempo de entrenamiento si converge antes

### Análisis del Éxito

**Riesgos:**

**Precisión/Recall perfectamente balanceados** (96.6% vs 98.5%) indica que el modelo no tiene sesgo hacia ninguna clase. El loss bajísimo (0.075) muestra confianza extrema en las predicciones.- Posible rendimiento inferior por mala suerte

- Variabilidad inherente del entrenamiento

**Score Kaggle 0.86380:**

- Posición: **#7 de ~50**### Resultados Obtenidos

- Top: **15%** del ranking

- Gap con #1 (0.968): -10.4%**Métricas de Entrenamiento:**

- Gap con #3 (0.957): -9.3%- Training Accuracy final: 0.8434

- Validation Accuracy final (época 15): **0.8582**

**Por qué funcionó:**- Validation Loss final: 0.3616

- VGG16 elimina la variabilidad de entrenar desde cero- Total épocas completadas: 20 (early stopping activado)

- Features pre-aprendidas son robustas y generalizan bien- Mejores pesos: Restaurados desde época 15

- Binary classification + umbral 0.5 es más estable

- Distribución predicciones balanceada (verificado)**Evolución por épocas clave Iteración 3:**



**Conclusión**: Transfer Learning fue la decisión correcta. En 11 minutos conseguí mejor resultado que 3 días iterando con CNN desde cero.| Época | Train Acc | Val Acc | Train Loss | Val Loss | LR | Estado |

|-------|-----------|---------|------------|----------|-----|---------|

---| 15    | **0.843** | **0.858** | **0.379** | **0.362** | **2.5e-4** | **MEJOR ÉPOCA** |

| 19    | 0.843     | 0.858   | 0.381      | 0.378    | 2.5e-4 | Último antes ES |

## 📊 RESUMEN FINAL: DE 0.54 A 0.86| 20    | -         | -       | -          | -        | -   | **Early Stopping** |



**Timeline completo:****Métricas de Evaluación:**

- Supplementary Data Accuracy: **0.6533**

| Iter | Modelo | Val Acc | Kaggle | Estado | Aprendizaje |- Supplementary Data Loss: 0.8321

|------|--------|---------|--------|--------|-------------|

| 1 | CNN base | 0.811 | - | ❌ | Overfitting brutal |**Kaggle Score:**

| 2 | + Augmentation | 0.868 | - | ❌ | Mejoró local pero no testeado |- Public Score: **0.58768** 

| 3 | Re-train | 0.858 | 0.588 | ❌ | Predicciones sesgadas |- Private Score: [Pendiente hasta cierre competición]

| 4 | Bug fixes | 0.742 | **0.547** | ❌ | CNN no generaliza |

| **5** | **VGG16** | **0.975** | **0.864** | ✅ | **Transfer Learning funciona** |### Análisis de Resultados - Comparación Iteraciones



**Mejora total**: 0.547 → 0.864 = **+58% de score****COMPARATIVA ITERACIÓN 2 vs 3:**



**Lecciones clave:**| Métrica | Iteración 2 | Iteración 3 | Diferencia | Análisis |

1. Data augmentation es obligatorio (Iter 1→2)|---------|-------------|-------------|------------|----------|

2. Validation accuracy local puede mentir (Iter 2→3)| **Val Acc** | **0.8684** | 0.8582 | **-1.02%** | Iter2 mejor |

3. Binary classification más estable que categorical (Iter 3→4)| **Supp Acc** | **0.7533** | 0.6533 | **-13.27%** | Iter2 significativamente mejor |

4. **CNN desde cero tiene demasiada variabilidad** (Iter 1-4)| **Épocas** | 25 | **15** | **-10** | Iter3 más eficiente |

5. **Transfer Learning es el camino correcto** (Iter 5)| **Gap Train/Val** | 5.26% | **1.48%** | **-3.78%** | Iter3 más estable |

| **Kaggle Score** | [No enviado] | **0.5877** | - | **DESASTRE TOTAL** |

**Posición actual**: #7 de ~50 (Top 15%)  | **Early Stop** | No activado | **Activado** | - | Iter3 más conservador |

**Submissions restantes**: 2/5  

**Objetivo siguiente**: Top 5 con fine-tuning o ensemble### Análisis del Desastre Kaggle



---**Score obtenido: 0.58768**

**Esperado: ~0.83-0.85**

## Próximos Pasos**Gap: -29.4% de lo esperado**



Con 2 submissions restantes y posición #7, las opciones son:**Diagnóstico del problema:**



**Opción A - Fine-tuning VGG16:****1. 🚨 Predicción sesgada hacia una sola clase:**

- Descongelar últimas 2-3 capas conv- Sample submission: TODOS los labels = 0 (solo perros)

- Learning rate muy bajo (1e-5)- Score ~58% sugiere que el modelo predijo 100% perros

- Riesgo: Puede empeorar- En dataset balanceado (50/50), esto da accuracy ≈ 50-60%

- Potencial: +2-4% score

**2. 🐛 Bug crítico en generación de predicciones:**

**Opción B - Ensemble:**- Posible error en conversión probabilidades → labels

- VGG16 + ResNet50- Early stopping podría haber restaurado pesos de época muy temprana

- Promedio de predicciones- Threshold incorrecto (>0.5 vs >0.9, etc.)

- Riesgo: Puede no mejorar mucho

- Potencial: +1-3% score**3. 🔄 Diferencia entorno local vs Kaggle:**

- Librerías diferentes

**Opción C - Test Time Augmentation:**- Preprocessing distinto

- Predecir 5 veces con rotaciones- Orden de datos diferente

- Promediar resultados

- Riesgo: Muy bajo**4. 📊 Early stopping contraproducente:**

- Potencial: +1-2% score- Época 15 podría ser demasiado temprana

- Modelo no tuvo tiempo de aprender patrones complejos

**Decisión**: Voy a probar **Opción C (TTA)** primero porque es la de menor riesgo. Si funciona bien, el último submission lo uso para ensemble.

### Conclusiones y Lecciones Aprendidas

---

**❌ Lo que NO funcionó:**

## Referencias Generales- **Early stopping agresivo**: Paró demasiado pronto (época 15)

- **Re-entrenamiento**: Nueva semilla dio peor resultado

### Cursos y Tutoriales- **Generación predicciones**: Bug crítico que causó sesgo hacia una clase

- 42AI Bootcamp - Machine Learning & Deep Learning: https://github.com/42-AI- **Validación local**: No predijo el comportamiento en test real

- Stanford CS231n - Convolutional Neural Networks: http://cs231n.stanford.edu/

- Fast.ai - Practical Deep Learning for Coders: https://course.fast.ai/**✅ Lo que SÍ funcionó:**

- Andrew Ng - Deep Learning Specialization: https://www.coursera.org/specializations/deep-learning- **Eficiencia**: Entrenamiento más rápido (15 vs 25 épocas)

- **Estabilidad**: Gap train/val mínimo (1.48%)

### Papers Clave- **Convergencia**: Early stopping funcionó técnicamente

- VGG16: "Very Deep Convolutional Networks for Large-Scale Image Recognition" (Simonyan & Zisserman, 2014): https://arxiv.org/abs/1409.1556

- Data Augmentation: "The Effectiveness of Data Augmentation in Image Classification" (Perez & Wang, 2017): https://arxiv.org/abs/1712.04621**🎯 Próximos pasos críticos:**

- Transfer Learning: "A Survey on Transfer Learning" (Pan & Yang, 2010): https://ieeexplore.ieee.org/document/52885261. **ARREGLAR BUG**: Revisar código de generación de predicciones

2. **ELIMINAR Early Stopping**: Entrenar épocas fijas (20-25)

### Documentación Técnica3. **TRANSFER LEARNING**: CNN desde cero tiene demasiada variabilidad

- Keras Official Documentation: https://keras.io/4. **VALIDAR PREDICCIONES**: Verificar distribución antes de enviar

- TensorFlow Transfer Learning Guide: https://www.tensorflow.org/tutorials/images/transfer_learning

- Kaggle Learn - Computer Vision: https://www.kaggle.com/learn/computer-vision### Plan de Recuperación - Iteración 4



### Videos YouTube**Objetivo**: Conseguir score >0.75 (4 submissions restantes)

- Yannic Kilcher - Data Augmentation Explained: https://www.youtube.com/watch?v=Zrp2b8qXHYk

- Aladdin Persson - VGG16 from Scratch: https://www.youtube.com/watch?v=ACmuBbuXn20**Estrategia A - Arreglar CNN desde cero:**

- StatQuest - Neural Networks Explained: https://www.youtube.com/watch?v=CqOfi41LfDw- Misma arquitectura Iter2, SIN early stopping

- Épocas fijas: 25

### Foros y Comunidad- Revisar código predicciones línea por línea

- Kaggle Discussions - Dogs vs Cats: https://www.kaggle.com/c/dogs-vs-cats/discussion

- Stack Overflow - Deep Learning Tag: https://stackoverflow.com/questions/tagged/deep-learning**Estrategia B - Transfer Learning:**

- Reddit r/MachineLearning: https://www.reddit.com/r/MachineLearning/- VGG16 pre-entrenado + fine-tuning

- Más estable y predecible

---- Menor riesgo de bugs



**Última actualización**: 06/11/2025  **Estrategia C - Híbrida:**

**Estado del proyecto**: ACTIVO - Top 15% del ranking  - CNN corregida + verificación predicciones

**Próxima iteración**: Test Time Augmentation (TTA)- Backup con Transfer Learning


**Recomendación**: **Estrategia B (Transfer Learning)** - Minimizar riesgos con solo 4 submissions restantes.

### Referencias
- Kaggle Submission Debugging: https://www.kaggle.com/learn/intro-to-machine-learning
- Early Stopping Best Practices: https://keras.io/api/callbacks/early_stopping/
- Transfer Learning Guide: https://keras.io/guides/transfer_learning/

### Referencias
- Keras Data Augmentation: https://keras.io/api/layers/preprocessing_layers/image_augmentation/
- Early Stopping: https://keras.io/api/callbacks/early_stopping/
- ReduceLROnPlateau: https://keras.io/api/callbacks/reduce_lr_on_plateau/
- Understanding Data Augmentation: https://keras.io/guides/preprocessing_layers/
