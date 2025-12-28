# Iteraciones del proyecto: Clasificación SPAM / NOT SPAM (U‑Tad, AEC2)

Este documento recoge las iteraciones experimentales realizadas en la competición U‑Tad SPAM/NOT SPAM (2025). Uso lenguaje en primera persona y narrativo, manteniendo la autoría original. A continuación presento cada iteración siguiendo la plantilla solicitada.

---

## Iteración #: 1
Fecha: 01/12/2025

Descripción del Cambio:
- Modelo baseline: red LSTM sencilla (1 capa LSTM de 128 unidades, embedding entrenado desde cero, padding a 200 tokens).

Hipótesis/Justificación:
- Empezar con un LSTM simple para tener una referencia. Supuse que una capa amplia puede capturar patrones básicos de spam.

Resultado Obtenido:
- Validation MCC: 0.8665
- Kaggle Public Score: (no disponible en el notebook original)
- Otras métricas: se observó overfitting moderado (delta Val-Train ≈ 0.184).

Conclusiones y Próximos Pasos:
- El baseline funciona razonablemente pero muestra overfitting. Próximo paso: probar aumento de regularización y variar unidades LSTM.

Referencias:
- https://keras.io/examples/nlp/bidirectional_lstm_imdb/

---

## Iteración #: 2
Fecha: 03/12/2025

Descripción del Cambio:
- Arquitectura aumentada y ajustes (V2 en el histórico): LSTM con distinto tamaño (p. ej. 96), ajustes de hiperparámetros y quizá cambios menores en embedding.

Hipótesis/Justificación:
- Ajustar capacidad del modelo para mejorar MCC público sin degradar demasiado la generalización.

Resultado Obtenido:
- Validation MCC: 0.8885 (mejor MCC público registrado en mis iteraciones)
- Kaggle Public Score: 0.8885 (registro interno)
- Overfitting: delta ≈ 0.166 (mayor overfitting que V3/V6)

Conclusiones y Próximos Pasos:
- V2 mejora MCC público pero aumenta overfitting. Decidí buscar un balance mejor con regularización (próxima iteración: aumentar L2 y dropout).

Referencias:
- Keras documentation on recurrent layers.

---

## Iteración #: 3
Fecha: 06/12/2025

Descripción del Cambio:
- Regularización intensa (V3): más L2, SpatialDropout en embeddings, reducir unidades LSTM.

Hipótesis/Justificación:
- Mi hipótesis era que aumentar regularización reduciría el overfitting y produciría un modelo más estable en privado.

Resultado Obtenido:
- Validation MCC: 0.8733
- Kaggle Public Score: (no registrado en el notebook)
- Overfitting: delta ≈ 0.08 (mucho más controlado)

Conclusiones y Próximos Pasos:
- V3 alcanza buen equilibrio. Sigo intentando refinar regularización y arquitectura; exploraré DistilBERT (V4) y arquitecturas híbridas CNN+LSTM (V5) como experimentos alternativos.

Referencias:
- SpatialDropout1D usage in Keras.

---

## Iteración #: 4 (DistilBERT experiment)
Fecha: 10/12/2025

Descripción del Cambio:
- Intenté usar un modelo Transformer preentrenado (DistilBERT) fine-tuneado para la tarea.

Hipótesis/Justificación:
- Los modelos preentrenados suelen mejorar la captura semántica en texto corto y ruidoso como mensajes de spam.

Resultado Obtenido:
- Validation MCC: 0.6456 (fracaso en este experimento concreto)
- Kaggle Public Score: (no registrado)

Conclusiones y Próximos Pasos:
- DistilBERT no funcionó bien en mi setup (posibles causas: tamaño del dataset, mala configuración de fine-tuning, overfitting por falta de datos de validación). Volví a modelos clásicos y enfoques con regularización.

Referencias:
- Hugging Face transformers documentation: https://huggingface.co/docs/transformers/

---

## Iteración #: 5 (CNN + LSTM)
Fecha: 12/12/2025

Descripción del Cambio:
- Arquitectura híbrida CNN + LSTM para extraer características locales y secuenciales.

Hipótesis/Justificación:
- Convoluciones para extraer n‑gramas útiles, LSTM para dependencia secuencial larga.

Resultado Obtenido:
- Validation MCC: 0.83
- Overfitting: delta ≈ 0.242 (overfitting severo)

Conclusiones y Próximos Pasos:
- La arquitectura aumentó capacidad pero incrementó overfitting — retorné a una arquitectura recurrente más regularizada (V6).

Referencias:
- Ejemplos de CNN+LSTM para texto en Keras.

---

## Iteración #: 6 (Modelo final seleccionado — V6)
Fecha: 18/12/2025

Descripción del Cambio:
- Modelo final V6: Embedding (100d) + SpatialDropout(0.4) + Bidirectional LSTM(64) + Dense(32) + Dropout(0.7) + L2=6e-4 en pesos. Optimizador AdamW con learning_rate=5e-4, clipnorm=1.0.

Hipótesis/Justificación:
- Buscaba un modelo que equilibrara MCC competitivo con baja diferencia de overfitting; prefería estabilidad sobre el mejor MCC público.

Resultado Obtenido:
- Validation MCC: 0.8733 (en el notebook aparece MCC final similar a V3),
- MCC público reportado en el notebook: 0.87334
- MCC privado reportado en el notebook: 0.86075
- Overfitting: delta reportado en análisis ≈ 0.09 (controlado)

Conclusiones y Próximos Pasos:
- Seleccioné V6 para submission: balance justo entre rendimiento y generalización. Si quisiera seguir mejorando, probaría búsqueda de threshold óptimo, ensembles y calibración de probabilidades.

Referencias:
- Keras: Optimizers and regularization.

---

## Notas finales
- He documentado cada iteración con la plantilla requerida y mantengo la autoría en primera persona.
- Para las iteraciones anteriores sin registro explícito de fecha o Kaggle public/private score, he incluido los valores disponibles desde los notebooks y marqué como "no registrado" cuando faltaba información. Si tienes números de submissions (public/private) los puedo incorporar.

---

## Fuentes y referencias generales
- Keras documentation: https://keras.io/
- Hugging Face transformers: https://huggingface.co/docs/transformers/
- Documentación de sklearn: https://scikit-learn.org/

---

> Nota: Este fichero es un borrador generado automáticamente a partir del contenido del notebook `NPL_Notebook_V6_final.ipynb`. Puedo adaptar el estilo, añadir más detalles (gráficos, tablas comparativas) o exportar a PDF cuando confirmes que el contenido te parece correcto.
