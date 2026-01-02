# Memoria - Competición Kaggle SPAM / NOT SPAM 2025

## Introducción y Contexto
Esta memoria se enmarca dentro de la AEC2 (Actividad de Evaluación Continua 2) de la asignatura de Inteligencia Artificial. El objetivo principal es desarrollar un modelo de Procesamiento de Lenguaje Natural (NLP) capaz de clasificar mensajes de texto como SPAM o NOT SPAM con la mayor precisión posible.

La competición como en la actividad anterior se desarrolla en la plataforma Kaggle, donde el rendimiento de los modelos se evalúa mediante el Matthews Correlation Coefficient (MCC). Esta métrica es fundamental en este proyecto, ya que proporciona una medida equilibrada de la calidad de la clasificación incluso cuando las clases están desbalanceadas, algo común en la detección de correo no deseado.

A lo largo de este documento, se detallan todas las fases por las que ha pasado el proyecto.

---

### Iteración 0: Starter Notebook (V0)
Fecha: 28/11/2025

Descripción del Cambio:
Punto de partida utilizando el notebook proporcionado por la asignatura. Implementación básica de una red neuronal para clasificación de texto.

Hipótesis/Justificación:
Establecer un entorno de trabajo funcional y entender el flujo de datos (carga, preprocesamiento, entrenamiento y generación de submission).

Resultado Obtenido:
*   Validation MCC: ~0.80
*   Observación: El modelo es funcional pero muy simple, sirviendo únicamente como base para futuras mejoras.

---

### Iteración 1: Modelo Baseline (Bi-LSTM) (V1)
Fecha: 04/12/2025

Descripción del Cambio:
He usado el notebook que nos proporcionaban de plantilla con una arquitectura de Red Neuronal Recurrente (RNN) con una capa de Embedding seguida de una LSTM Bidireccional de 128 unidades y GlobalMaxPooling1D. He pasado de una estructura secuencial simple a una que procesa la información en ambos sentidos.

Hipótesis/Justificación:
Mi hipótesis es que una LSTM bidireccional capturará mejor el contexto semántico de los mensajes al leer en ambas direcciones. En la clasificación de SPAM, el orden de las palabras y la relación entre ellas (como "ganar" seguido de "premio" en diferentes partes de la frase) es crucial. Al usar `GlobalMaxPooling1D`, busco extraer las características más relevantes de toda la secuencia procesada por la LSTM.

Resultado Obtenido:
*   Validation MCC: 0.8585
*   Observación: Buen rendimiento inicial, pero con un sobreajuste (overfitting) evidente.
*   Consulta/Referencia: [Stack Overflow: Difference between LSTM and Bidirectional LSTM](https://stackoverflow.com/questions/43035827/whats-the-difference-between-lstm-and-bidirectional-lstm) - Validé que para secuencias cortas de texto, la bidireccionalidad suele aportar un 2-3% extra de precisión.

---

### Iteración 2: Mejora en Regularización (V2)
Fecha: 04/12/2025

Descripción del Cambio:
He introducido regularización L2 (1e-4) en las capas densas y recurrentes, aumentado el Dropout al 0.5 y añadido SpatialDropout1D (0.3) justo después del Embedding.

Hipótesis/Justificación:
Al observar el fuerte overfitting de la V1, mi hipótesis es que el modelo está "memorizando" palabras específicas del set de entrenamiento. El `SpatialDropout1D` es clave aquí: a diferencia del Dropout normal, este elimina canales completos del embedding, forzando al modelo a no depender de dimensiones específicas del vector de palabras. La regularización L2 penaliza los pesos excesivamente grandes, buscando una superficie de error más suave.

Resultado Obtenido:
*   Validation MCC: 0.8585
*   Observación: El overfitting se ha reducido y el MCC se ha mantenido, lo que indica una mejor capacidad de generalización.
*   Consulta/Referencia: [Reddit r/MachineLearning: SpatialDropout1D vs Dropout](https://www.reddit.com/r/MachineLearning/comments/5fiv98/d_spatial_dropout_vs_normal_dropout/) - Discusión sobre por qué SpatialDropout es superior en capas de embedding para evitar la co-adaptación de características.

---

### Iteración 3: (V3)
Fecha: 05/12/2025

Descripción del Cambio:
He aplicado una regularización alta, elevando el Dropout al 0.7 y aumentando los coeficientes de L2. También he reducido el número de unidades en la LSTM para simplificar el modelo.

Hipótesis/Justificación:
Quería comprobar si una regularización mas "agresiva" permitiría una mejor generalización en el conjunto de test de Kaggle, incluso si el rendimiento en validación bajaba ligeramente. La idea era eliminar cualquier ruido residual que el modelo pudiera estar capturando.

Resultado Obtenido:
*   Validation MCC: 0.8633
*   Observación: El modelo se volvió demasiado rígido (*underfitting* parcial). Aunque el gap entre train y val desapareció, el rendimiento absoluto no superó a la V2 de forma significativa.
*   Consulta/Referencia: [Comunidad 42: Overfitting in small NLP datasets](https://42born2code.slack.com) (Canal AI) - Consulté con compañeros sobre el límite de la regularización; llegamos a la conclusión de que un Dropout > 0.6 suele ser contraproducente si no se aumenta la capacidad del modelo.

---

### Iteración 4: Transfer Learning con DistilBERT (V4)
Fecha: 06/12/2025

Descripción del Cambio:
He experimentado con DistilBERT pre-entrenado de la librería HuggingFace, realizando fine-tuning de las últimas capas y usando un optimizador AdamW con weight decay.

Hipótesis/Justificación:
Los modelos basados en Transformers suelen superar a las RNNs gracias a su mecanismo de atención. Mi hipótesis era que el conocimiento pre-entrenado de DistilBERT compensaría el tamaño limitado de nuestro dataset.

Resultado Obtenido:
*   Validation MCC: 0.6456
*   Observación: Resultados muy inferiores e inestables. El modelo es demasiado complejo para este dataset específico o requiere un ajuste de hiperparámetros (como el learning rate) mucho más fino y costoso computacionalmente.
*   Consulta/Referencia: [HuggingFace Forums: Fine-tuning BERT on small imbalanced datasets](https://discuss.huggingface.co/t/fine-tuning-bert-on-very-small-dataset/3468) - Confirmé que con menos de 5000 muestras, los Transformers pueden colapsar si no se usa un learning rate extremadamente bajo (ej. 2e-5).

---

### Iteración 5: Arquitectura Híbrida CNN + LSTM (Modelo Final) (V5)
Fecha: 10/12/2025

Descripción del Cambio:
He diseñado una arquitectura híbrida con ramas paralelas de Conv1D (kernels de tamaños 2, 3, 4 y 5) y una Bi-LSTM, concatenando sus salidas antes de la capa densa final.

Hipótesis/Justificación:
Esta es mi apuesta más fuerte. Las CNNs son excelentes extrayendo n-gramas locales (detectan patrones como "free money" o "click here" sin importar dónde estén), mientras que la LSTM captura la estructura global y el tono del mensaje. Al usar múltiples tamaños de kernel, capturo frases de diferentes longitudes. La combinación de ambas visiones (local y global) debería proporcionar la representación más rica del texto.

Resultado Obtenido:
*   Validation MCC: 0.8693
*   Validation Accuracy: 0.9521
*   Kaggle Public Score: 0.9012
*   Observación: Es el modelo más equilibrado y con mejor rendimiento en el leaderboard público y privado.
*   Consulta/Referencia: [Stack Overflow: Combining CNN and RNN for text classification](https://stackoverflow.com/questions/44230635/how-to-combine-cnn-and-rnn-for-text-classification) - Inspiración para la arquitectura de ramas paralelas para mejorar la detección de keywords en SPAM.

---