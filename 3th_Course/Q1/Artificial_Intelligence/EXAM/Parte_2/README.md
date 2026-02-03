# 📚 GUÍA DE MODELOS NLP - Clasificación Spam/Not Spam

## 🎯 Modelos Creados

Esta carpeta contiene **6 notebooks independientes**, cada uno enfocado en una técnica o mejora específica de NLP para exámenes universitarios.

---

## 📋 Lista de Modelos

### 🟢 **Modelo 1: Baseline - Red Neuronal Simple**
**Archivo:** `modelo_1_baseline.ipynb`

- **Arquitectura:** Embedding → GlobalAveragePooling → Dense
- **Problema:** NO captura orden de palabras (Bag of Words)
- **Ideal para:** Entender las limitaciones de modelos simples

**Conceptos clave:**
- Tokenización y padding
- Embedding layer
- GlobalAveragePooling
- Clasificación binaria

---

### 🔵 **Modelo 2: LSTM - Captura de Secuencias**
**Archivo:** `modelo_2_lstm.ipynb`

- **Mejora:** Añade LSTM para capturar orden temporal
- **Ventaja:** Procesa secuencias con memoria
- **Ideal para:** Entender RNN/LSTM en NLP

**Conceptos clave:**
- LSTM (4 gates: input, forget, output, cell)
- Dependencias temporales
- Memoria a largo plazo
- Cuándo usar RNN vs Dense

---

### 🟠 **Modelo 3: LSTM + Dropout (Regularización)**
**Archivo:** `modelo_3_lstm_dropout.ipynb`

- **Problema:** LSTM puede sufrir overfitting
- **Solución:** Dropout para regularización
- **Ideal para:** Entender overfitting y regularización

**Conceptos clave:**
- Dropout (tasas típicas: 0.2-0.5)
- Dónde colocar Dropout
- Overfitting vs Underfitting
- Visualización train vs validation

---

### 🟣 **Modelo 4: Bidirectional LSTM + Layer Normalization**
**Archivo:** `modelo_4_bidirectional_lstm.ipynb`

- **Problema:** LSTM solo lee en una dirección
- **Solución:** Bidirectional (lee forward + backward)
- **Bonus:** Layer Normalization para estabilidad
- **Ideal para:** Modelos avanzados de NLP

**Conceptos clave:**
- Bidirectional wrapping
- return_sequences (True vs False)
- Layer Normalization
- Arquitecturas profundas (2+ capas LSTM)

---

### 🟡 **Modelo 5: Bidirectional GRU (Alternativa eficiente)**
**Archivo:** `modelo_5_bidirectional_gru.ipynb`

- **Problema:** LSTM tiene muchos parámetros (lento)
- **Solución:** GRU (2 gates en vez de 4)
- **Ventaja:** 25% menos parámetros, más rápido
- **Ideal para:** Entender trade-off capacidad vs velocidad

**Conceptos clave:**
- GRU vs LSTM (diferencias arquitecturales)
- Cuándo elegir GRU
- Comparación de parámetros
- Trade-off: velocidad vs capacidad

---

### 🔴 **Modelo 6: LSTM + Early Stopping**
**Archivo:** `modelo_6_early_stopping.ipynb`

- **Problema:** No sabemos cuántas épocas entrenar
- **Solución:** Early Stopping (para automáticamente)
- **Ventaja:** Ahorra tiempo y previene overfitting
- **Ideal para:** Callbacks y automatización

**Conceptos clave:**
- Callbacks en Keras
- EarlyStopping (monitor, patience, restore_best_weights)
- Cuándo parar el entrenamiento
- Ahorro de tiempo y recursos

---

## 🎓 Progresión de Aprendizaje Recomendada

```
1. Modelo 1 (Baseline)
   ↓
   Aprende: Limitación del Bag of Words
   
2. Modelo 2 (LSTM)
   ↓
   Aprende: Capturar orden temporal
   
3. Modelo 3 (+ Dropout)
   ↓
   Aprende: Prevenir overfitting
   
4. Modelo 4 (Bidirectional)
   ↓
   Aprende: Contexto completo
   
5. Modelo 5 (GRU)
   ↓
   Aprende: Eficiencia y trade-offs
   
6. Modelo 6 (Early Stopping)
   ↓
   Aprende: Automatización
```

---

## 📊 Comparación Rápida

| Modelo | Arquitectura | Parámetros | Velocidad | Accuracy Esperada |
|--------|-------------|-----------|-----------|-------------------|
| 1. Baseline | Dense | Bajo | Rápida | Baseline |
| 2. LSTM | LSTM(64) | Medio | Media | +5-10% |
| 3. LSTM+Dropout | LSTM+Drop | Medio | Media | +2-5% (mejor generalización) |
| 4. BiLSTM+LN | 2xBiLSTM | Alto | Lenta | +3-7% |
| 5. BiGRU+LN | 2xBiGRU | Medio-Alto | Media | Similar a 4, más rápido |
| 6. LSTM+ES | LSTM+Drop | Medio | Óptima | Similar a 3, ahorra tiempo |

---

## 🔑 Conceptos Clave por Modelo

### Modelo 1
- ✅ Tokenización
- ✅ Padding
- ✅ Embedding
- ⚠️ Limitación: No orden

### Modelo 2
- ✅ LSTM gates
- ✅ Memoria temporal
- ✅ Procesamiento secuencial

### Modelo 3
- ✅ Dropout
- ✅ Regularización
- ✅ Overfitting detection

### Modelo 4
- ✅ Bidirectional
- ✅ Layer Normalization
- ✅ return_sequences
- ✅ Arquitecturas profundas

### Modelo 5
- ✅ GRU architecture
- ✅ LSTM vs GRU
- ✅ Trade-offs

### Modelo 6
- ✅ Callbacks
- ✅ EarlyStopping
- ✅ restore_best_weights

---

## 🎯 Para Preparar Exámenes

### Ejercicios típicos:

1. **Completar arquitectura:** Usar Modelos 1, 2, 4
2. **Justificar decisión:** Usar Modelo 5 (GRU vs LSTM)
3. **Prevenir overfitting:** Usar Modelos 3, 6
4. **Optimizar velocidad:** Usar Modelo 5 (GRU)
5. **Mejorar modelo existente:** Progresión 1→2→3→4

### Preguntas frecuentes:

**Q: ¿Por qué LSTM sobre Dense?**
→ Ver Modelo 2

**Q: ¿Cómo prevenir overfitting?**
→ Ver Modelos 3 y 6

**Q: ¿LSTM o GRU?**
→ Ver Modelo 5

**Q: ¿Qué es Bidirectional?**
→ Ver Modelo 4

**Q: ¿Cómo usar callbacks?**
→ Ver Modelo 6

---

## 💡 Consejos Finales

1. **Ejecuta todos los modelos** secuencialmente
2. **Compara resultados** entre ellos
3. **Entiende las mejoras** de cada paso
4. **Practica justificaciones** teóricas
5. **Memoriza arquitecturas** comunes

---

## 📚 Recursos Adicionales

- Keras Documentation: https://keras.io/
- LSTM Paper: Hochreiter & Schmidhuber (1997)
- GRU Paper: Cho et al. (2014)
- Dropout Paper: Srivastava et al. (2014)

---

## ✅ Checklist para el Examen

- [ ] Entiendo tokenización y padding
- [ ] Sé explicar Embedding layer
- [ ] Entiendo diferencia LSTM vs Dense
- [ ] Sé cuándo usar Dropout
- [ ] Entiendo return_sequences
- [ ] Sé diferencia LSTM vs GRU
- [ ] Entiendo Bidirectional
- [ ] Sé usar Early Stopping
- [ ] Puedo justificar cada decisión de diseño

---

**¡Buena suerte en el examen!** 🎊
