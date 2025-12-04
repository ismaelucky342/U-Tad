# 🎯 Guía Rápida de Uso - Competición SPAM/NOT SPAM

## ✅ Estado Actual del Proyecto

Has completado la **Iteración 1 - Baseline** con las siguientes características:

### Archivos Creados

1. **`u-tad-spam-not-spam-starter-notebook.ipynb`** ✅
   - Notebook principal con modelo baseline LSTM Bidireccional
   - Incluye análisis exploratorio completo
   - Visualizaciones profesionales
   - Sección de conclusiones y reflexión final
   - **LISTO PARA EJECUTAR EN KAGGLE**

2. **`iteraciones_template.md`** ✅
   - Plantilla para documentar cada iteración
   - Estructura completa para crear el PDF final
   - Secciones pre-rellenadas con ejemplos

3. **`README.md`** ✅
   - Documentación completa del proyecto
   - Estrategia de experimentación
   - Referencias y recursos útiles
   - Tips para mejorar el score

4. **`IDEAS_MEJORAS.md`** ✅
   - 10 iteraciones sugeridas con código completo
   - Desde embeddings pre-entrenados hasta BERT
   - Estimación de mejora esperada para cada iteración

5. **`utils.py`** ✅
   - Funciones auxiliares reutilizables
   - Visualizaciones de métricas
   - Utilidades de análisis

---

## 🚀 Próximos Pasos

### Paso 1: Ejecutar el Notebook en Kaggle

1. **Subir a Kaggle:**
   - Ve a https://www.kaggle.com/code
   - Click en "New Notebook"
   - Selecciona "Upload Notebook"
   - Sube `u-tad-spam-not-spam-starter-notebook.ipynb`

2. **Configurar el entorno:**
   - Asegúrate de que esté conectado al dataset: `u-tad-spam-not-spam-2025-edition`
   - Activa GPU (Settings → Accelerator → GPU T4 x2)
   - Internet: ON (si vas a usar embeddings pre-entrenados más adelante)

3. **Ejecutar todas las celdas:**
   - Click en "Run All"
   - Tiempo estimado: 5-10 minutos
   - Observa las métricas de validación

4. **Hacer submission:**
   - Una vez ejecutado, se generará `submission.csv`
   - Click en "Submit to Competition"
   - Anota el Public Score que obtengas

### Paso 2: Documentar Iteración 1

1. **Edita `iteraciones_template.md`:**
   ```markdown
   ## Iteración #1
   
   ### Resultado Obtenido
   - **Validation MCC:** [TU RESULTADO]
   - **Validation Accuracy:** [TU RESULTADO]
   - **Kaggle Public Score:** [TU SCORE EN KAGGLE]
   
   ### Conclusiones y Próximos Pasos
   [Analiza si el modelo tiene overfitting, underfitting, etc.]
   ```

2. **Captura de pantalla:**
   - Guarda las gráficas de curvas de aprendizaje
   - Guarda la matriz de confusión
   - Guarda el classification report

### Paso 3: Planear Iteración 2

Basándote en los resultados de Iteración 1, elige una mejora:

**Opciones recomendadas:**

#### Opción A: Embeddings Pre-entrenados (MÁS FÁCIL) 🟢
- **Dificultad:** Baja
- **Tiempo:** 30 minutos
- **Mejora esperada:** +0.03-0.05 MCC
- **Archivo:** Ver `IDEAS_MEJORAS.md` → Iteración 2

#### Opción B: CNN + LSTM Híbrido (MODERADA) 🟡
- **Dificultad:** Media
- **Tiempo:** 1 hora
- **Mejora esperada:** +0.02-0.04 MCC
- **Archivo:** Ver `IDEAS_MEJORAS.md` → Iteración 3

#### Opción C: TextCNN con múltiples kernels (AVANZADA) 🔴
- **Dificultad:** Alta
- **Tiempo:** 2-3 horas
- **Mejora esperada:** +0.03-0.06 MCC
- **Archivo:** Ver `IDEAS_MEJORAS.md` → Iteración 4

---

## 📋 Checklist para la Entrega Final

### Documentación PDF (iteraciones.pdf)
- [ ] Mínimo 3 iteraciones documentadas
- [ ] Cada iteración incluye:
  - [ ] Descripción del cambio
  - [ ] Hipótesis/Justificación
  - [ ] Resultados obtenidos (MCC, accuracy, etc.)
  - [ ] Conclusiones y próximos pasos
  - [ ] Referencias bibliográficas
- [ ] Tabla comparativa de todas las iteraciones
- [ ] Justificación del mejor modelo

### Notebook Final
- [ ] Código del mejor modelo
- [ ] Bien comentado y estructurado
- [ ] Sección de análisis final con:
  - [ ] Métricas finales (MCC, accuracy, precision, recall)
  - [ ] Curvas de aprendizaje
  - [ ] Análisis de overfitting/underfitting
  - [ ] Reflexión final
- [ ] Ejecutable sin errores

### Submissions en Kaggle
- [ ] Al menos 3 submissions realizadas
- [ ] Mejor score documentado
- [ ] Capturas de pantalla del leaderboard

---

## 🔧 Solución de Problemas Comunes

### Error: "AttributeError: 'MessageFactory' object has no attribute 'GetPrototype'"

**Solución:** Ya está arreglado en el notebook. La primera celda incluye:
```python
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
```

### Error: "ResourceExhaustedError: OOM when allocating tensor"

**Solución:** Reduce el batch size:
```python
BATCH_SIZE = 16  # En lugar de 32
```

### Warning: "CUDA errors"

**Solución:** Es normal en Kaggle, no afecta la ejecución.

### Validation MCC muy bajo (< 0.5)

**Causas posibles:**
1. Dataset desbalanceado → Usar class_weight
2. Overfitting → Aumentar dropout
3. Underfitting → Aumentar capacidad del modelo

---

## 📊 Scores de Referencia

### Benchmarks esperados:

| Iteración | Arquitectura | MCC Esperado | Nivel |
|-----------|--------------|--------------|-------|
| 1 | Bi-LSTM Baseline | 0.75-0.82 | 🟢 Bueno |
| 2 | Bi-LSTM + GloVe | 0.80-0.87 | 🟢 Muy Bueno |
| 3 | CNN + LSTM | 0.82-0.89 | 🟡 Excelente |
| 4 | TextCNN | 0.84-0.90 | 🟡 Excelente |
| 5+ | BERT/Ensemble | 0.88-0.95 | 🔴 Sobresaliente |

**Objetivo mínimo:** MCC > 0.80  
**Objetivo competitivo:** MCC > 0.85  
**Objetivo top 10%:** MCC > 0.90

---

## 🎓 Tips de Última Hora

1. **No te olvides de las referencias:**
   - Si usas código de internet, cítalo
   - Si usas embeddings pre-entrenados, cita el paper
   - Si usas arquitecturas conocidas, cita el paper original

2. **Documentación > Score:**
   - Mejor 3 iteraciones bien documentadas que 10 sin documentar
   - Explica tus decisiones y aprende de los errores

3. **Gestión del tiempo:**
   - No dejes todo para el último día
   - Haz al menos 1 iteración por día
   - Reserva tiempo para escribir el PDF

4. **Experimentación inteligente:**
   - Empieza con cambios pequeños
   - Si algo funciona, explora por qué
   - Si algo no funciona, también documéntalo (es aprendizaje)

---

## 📞 Recursos de Ayuda

### Si tienes dudas sobre:

**Keras/TensorFlow:**
- https://keras.io/examples/nlp/

**NLP Concepts:**
- https://web.stanford.edu/class/cs224n/

**Kaggle Competitions:**
- https://www.kaggle.com/docs/competitions

**Material de clase:**
- Revisa las unidades 4 y 5 de la asignatura

---

## 🎯 Resumen Ejecutivo

**YA TIENES:**
- ✅ Notebook baseline completo y funcional
- ✅ Plantillas de documentación
- ✅ 10 ideas de mejora con código
- ✅ Utilidades para análisis

**DEBES HACER:**
1. Ejecutar notebook en Kaggle (5-10 min)
2. Documentar Iteración 1 (10 min)
3. Hacer Iteración 2 (1-2 horas)
4. Hacer Iteración 3 (1-2 horas)
5. Compilar PDF final (1 hora)

**TIEMPO TOTAL ESTIMADO:** 5-8 horas

**FECHA LÍMITE COMPETICIÓN:** 12 diciembre 2025 - 12:45  
**FECHA LÍMITE ENTREGA:** 21 diciembre 2025 - 23:59

---

## 🚀 ¡Adelante!

Tienes todo lo necesario para destacar en esta competición. La base está sólida, ahora es momento de experimentar y aprender. **¡Mucha suerte! 🎉**

---

**Creado por:** Ismael Hernandez Clemente  
**Fecha:** 04 de diciembre de 2025  
**Versión:** 1.0
