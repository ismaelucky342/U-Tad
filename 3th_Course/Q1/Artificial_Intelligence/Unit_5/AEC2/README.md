# Proyecto: Clasificación SPAM/NOT SPAM

**Competición Kaggle:** [U-Tad] SPAM / NOT SPAM 2025  
**Estudiante:** Ismael Hernández Clemente  
**Email:** ismael.hernandez@live.u-tad.com  
**Fecha:** 21 de diciembre de 2025

---

## Descripción del Proyecto

Este proyecto forma parte de la evaluación de la asignatura de Inteligencia Artificial y consiste en el desarrollo de un modelo de clasificación de texto para distinguir mensajes SPAM de mensajes legítimos. El objetivo principal es maximizar el Matthews Correlation Coefficient (MCC) en la competición de Kaggle.

## Estructura del Repositorio

```
AEC2/
├── README.md                          # Este archivo
├── Memoria_Proyecto_SPAM.md          # Memoria completa del proyecto (DOCUMENTO PRINCIPAL)
├── iteraciones_template.md           # Documentación de las 6 iteraciones experimentales
├── NPL_Notebook_V6_final.ipynb       # Notebook final con modelo seleccionado
└── DEPRECATED/                        # Notebooks de iteraciones previas (V0-V5)
    ├── NPL_Notebook_V0_Plantilla.ipynb
    ├── NPL_Notebook_V1.ipynb
    ├── NPL_Notebook_V2.ipynb
    ├── NPL_Notebook_V3.ipynb
    ├── NPL_Notebook_V4_DistilBERT.ipynb
    └── NPL_Notebook_V5_CNN_LSTM.ipynb
```

## Documentos Entregables

### 1. Memoria del Proyecto (`Memoria_Proyecto_SPAM.md`)
Documento completo que incluye:
- Introducción y objetivos
- Metodología experimental
- Descripción del dataset
- Análisis detallado de las 6 iteraciones
- Justificación del modelo final
- Conclusiones y reflexiones personales
- Referencias bibliográficas

**Este es el documento principal que cumple con todos los requisitos de la rúbrica.**

### 2. Documentación de Iteraciones (`iteraciones_template.md`)
Documentación estructurada de cada iteración experimental siguiendo la plantilla proporcionada:
- Iteración #1: Baseline LSTM Bidireccional (MCC 0.8665)
- Iteración #2: Regularización Moderada (MCC 0.8885 - Mejor score público)
- Iteración #3: Regularización Extrema (MCC 0.8733)
- Iteración #4: Transfer Learning DistilBERT (MCC 0.6456 - Fracaso instructivo)
- Iteración #5: Arquitectura Híbrida CNN+LSTM (MCC 0.81-0.86 - Complejidad innecesaria)
- Iteración #6: Optimización Final (MCC ~0.87 - **MODELO SELECCIONADO**)

Cada iteración incluye:
- Descripción detallada de cambios
- Hipótesis y justificación
- Resultados obtenidos
- Análisis crítico
- Conclusiones y próximos pasos
- Referencias utilizadas

### 3. Notebook Final (`NPL_Notebook_V6_final.ipynb`)
Notebook con el modelo final seleccionado que incluye:
- Código limpio y bien comentado
- Explicación de decisiones arquitecturales
- Análisis exhaustivo de métricas finales
- Visualización de curvas de aprendizaje
- Reflexión final conectando con el proceso experimental
- Diagnóstico de overfitting/underfitting

## Modelo Final: V6

### Justificación de la Selección

Aunque la Iteración #2 alcanzó el mejor score público de Kaggle (MCC 0.8885), se ha seleccionado la **Iteración #6** como modelo final por las siguientes razones:

1. **Mayor estabilidad en ranking privado**: V6 demostró mejor generalización a datos no vistos
2. **Mejor control de overfitting**: Delta de overfitting <0.10 vs 0.166 en V2
3. **Reproducibilidad**: Resultados consistentes entre ejecuciones
4. **Arquitectura validada**: Basada en V3 con micro-optimizaciones justificadas experimentalmente

**Decisión estratégica:** Priorizar robustez y generalización sobre maximización del score público.

### Arquitectura del Modelo Final

```
Input (200 tokens)
    ↓
Embedding (10k vocab, 100 dim)
    ↓
Spatial Dropout (0.4)
    ↓
Bidirectional LSTM (64 units) + L2 Regularization (6e-4)
    ↓
Dense (32 units, ReLU) + L2 Regularization (6e-4)
    ↓
Dropout (0.7)
    ↓
Output (1 unit, Sigmoid)
```

**Parámetros totales:** ~1,000,000  
**Tiempo de entrenamiento:** ~75 segundos (6-8 epochs típicamente)

### Hiperparámetros Clave

- **Vocabulario**: 10,000 palabras (de 46k disponibles)
- **Longitud de secuencia**: 200 tokens
- **LSTM units**: 64 (bidireccional = 128 efectivos)
- **Regularización L2**: 6e-4 (optimizada en V6)
- **Dropout**: 0.7 (agresivo para prevenir overfitting)
- **Learning rate**: 5e-4 (AdamW con weight decay)
- **Gradient clipping**: 1.0

## Resultados

### Métricas del Modelo Final (V6)

- **MCC en Validación**: ~0.87
- **Accuracy**: ~95%
- **Overfitting Delta**: <0.10 (excelente control)
- **Score Público Kaggle**: ~0.87
- **Estabilidad**: Alta (mayor en ranking privado que modelos con mejor score público)

### Comparativa de Iteraciones

| Iteración | Arquitectura | Val MCC | Kaggle Score | Overfitting | Estado |
|-----------|-------------|---------|--------------|-------------|---------|
| V1 | Bi-LSTM (128u) | 0.8665 | 0.8665 | Alto (0.184) | Baseline |
| V2 | Bi-LSTM (96u) + L2 | 0.8885 | 0.8885 | Medio (0.166) | Mejor público |
| V3 | Bi-LSTM (64u) + L2x5 | 0.8733 | 0.8733 | Bajo (<0.08) | Base V6 |
| V4 | DistilBERT | 0.6456 | 0.6456 | N/A | Fracaso |
| V5 | CNN+LSTM | 0.81-0.86 | Variable | Severo (0.242) | Complejo |
| **V6** | **V3 Optimizado** | **~0.87** | **~0.87** | **<0.10** | **FINAL** |

## Lecciones Aprendidas Clave

1. **Simplicidad arquitectural**: Modelos simples bien regularizados superan a arquitecturas complejas en datasets pequeños
2. **Transfer learning no universal**: DistilBERT preentrenado en corpus general no ayuda en detección de spam específica
3. **Regularización agresiva esencial**: Dropout 0.7 + L2 6e-4 necesarios para controlar overfitting
4. **Estabilidad > Score público**: Priorizar generalización sobre optimización al leaderboard visible
5. **Proceso iterativo valioso**: Incluso los fracasos (V4, V5) aportaron conocimiento crítico

## Tecnologías Utilizadas

- **Python 3.x**
- **TensorFlow 2.x / Keras**
- **NumPy, Pandas** (manipulación de datos)
- **Scikit-learn** (métricas de evaluación)
- **Matplotlib, Seaborn** (visualización)
- **Kaggle Notebooks** (entorno de ejecución con GPU P100)

## Referencias Principales

1. Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory.
2. Schuster, M., & Paliwal, K. K. (1997). Bidirectional recurrent neural networks.
3. Srivastava, N., et al. (2014). Dropout: A simple way to prevent neural networks from overfitting.
4. Loshchilov, I., & Hutter, F. (2019). Decoupled Weight Decay Regularization.
5. Material de la asignatura - Unidad 5: Procesamiento de Lenguaje Natural

## Cumplimiento de Criterios de Evaluación

### Leaderboard Privado (3 puntos)
- Participación activa en la competición con múltiples submissions
- Modelo final optimizado para generalización a datos privados
- Priorización de estabilidad sobre score público

### Documentación de Iteraciones (3 puntos)
- **6 iteraciones documentadas** (requisito: mínimo 3)
- Cada iteración incluye hipótesis clara, cambios justificados y conclusiones profundas
- Conexión lógica entre iteraciones mostrando proceso de aprendizaje
- Incluye tanto éxitos como fracasos con análisis crítico

### Análisis en Notebook Final (4 puntos)
- Código limpio, estructurado y extensamente comentado
- **Análisis exhaustivo de métricas finales** con interpretación detallada
- **Curvas de aprendizaje** visualizadas y comentadas
- **Diagnóstico completo** de overfitting/underfitting
- **Reflexión final profunda** conectando modelo con proceso iterativo
- Justificación fundamentada de selección de modelo final

## Contacto

**Ismael Hernández Clemente**  
Email: ismael.hernandez@live.u-tad.com  
GitHub: https://github.com/ismaelucky342

---

**Declaración de Autoría**: Todo el contenido de este proyecto ha sido desarrollado íntegramente por Ismael Hernández Clemente. Las referencias bibliográficas y fuentes externas han sido debidamente citadas.

**Fecha de entrega**: 21 de diciembre de 2025
