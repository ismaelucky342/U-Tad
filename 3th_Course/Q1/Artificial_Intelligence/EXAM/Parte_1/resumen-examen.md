# Análisis Comparativo: Baseline vs Final - Fashion-MNIST

**Autor:** Ismael Hernandez Clemente  
**Fecha:** 2 de febrero de 2026  
**Examen IA - U-Tad**

---

## 1. Modelo Baseline (Original)

### Arquitectura
```python
model = keras.Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])
```

### Características
- **Capas:** 7 capas totales
- **Parámetros:** ~1.2M parámetros
- **Optimizador:** Adam (default LR=0.001)
- **Épocas:** 15 fijas
- **Batch size:** 128
- **Regularización:** ❌ Ninguna
- **Callbacks:** ❌ Ninguno

### Preprocesado
- Normalización [0-1]
- Split: 85% train, 15% val (stratified)
- One-hot encoding

### Resultados Esperados
- **Train Accuracy:** ~92%
- **Val Accuracy:** ~88%
- **Test Accuracy:** ~87%
- **Overfitting:** Moderado-Alto (gap ~4-5%)

---

## 2. Cambios en el Modelo Final

### 2.1 Arquitectura Mejorada

```python
model = keras.Sequential([
    # BLOQUE 1
    Conv2D(32, (3,3), activation='relu', padding='same'),  # ← padding='same'
    BatchNormalization(),                                   # ← NUEVO
    Conv2D(32, (3,3), activation='relu', padding='same'),  # ← doble conv
    BatchNormalization(),                                   # ← NUEVO
    MaxPooling2D((2,2)),
    Dropout(0.25),                                         # ← NUEVO
    
    # BLOQUE 2
    Conv2D(64, (3,3), activation='relu', padding='same'),
    BatchNormalization(),                                   # ← NUEVO
    Conv2D(64, (3,3), activation='relu', padding='same'),  # ← doble conv
    BatchNormalization(),                                   # ← NUEVO
    MaxPooling2D((2,2)),
    Dropout(0.25),                                         # ← NUEVO
    
    # DENSE
    Flatten(),
    Dense(256, activation='relu'),                         # ← 256 vs 128
    BatchNormalization(),                                   # ← NUEVO
    Dropout(0.5),                                          # ← NUEVO
    Dense(10, activation='softmax')
])
```

### 2.2 Entrenamiento Mejorado

```python
callbacks = [
    EarlyStopping(monitor='val_loss', patience=8, restore_best_weights=True),
    ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=4, min_lr=1e-7)
]

history = model.fit(
    x_train, y_train_cat,
    batch_size=128,
    epochs=40,  # ← más épocas disponibles
    validation_data=(x_val, y_val_cat),
    callbacks=callbacks  # ← NUEVO
)
```

### 2.3 Evaluación Extendida

```python
# Test evaluation
test_loss, test_acc = model.evaluate(x_test, y_test_cat)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred_classes)
sns.heatmap(cm, annot=True, cmap='Blues')

# Classification report
print(classification_report(y_test, y_pred_classes, target_names=class_names))

# Error analysis
incorrect = np.where(y_pred_classes != y_test)[0]
# Visualización de predicciones incorrectas
```

---

## 3. Tabla Comparativa de Cambios

| Componente | Baseline | Final | Mejora |
|------------|----------|-------|--------|
| **Conv por bloque** | 1 | 2 | Mayor capacidad de aprendizaje |
| **Padding** | valid (default) | same | Preserva información de bordes |
| **Batch Normalization** | ❌ | ✅ (6 capas) | Estabiliza entrenamiento |
| **Dropout** | ❌ | ✅ (0.25, 0.5) | Previene overfitting |
| **Dense neurons** | 128 | 256 | Mayor capacidad |
| **EarlyStopping** | ❌ | ✅ (patience=8) | Evita overfitting automático |
| **ReduceLROnPlateau** | ❌ | ✅ (factor=0.5) | Optimiza convergencia |
| **Épocas** | 15 fijas | 40 adaptativas | Tiempo para converger |
| **Evaluación** | Solo val | Val + Test + CM + Report | Análisis completo |

---

## 4. Explicación de Mejoras Clave

### 4.1 Batch Normalization
**¿Qué hace?**
- Normaliza activaciones entre capas (media=0, std=1)
- Reduce Internal Covariate Shift

**¿Por qué mejora?**
- ✅ Entrenamiento más estable y rápido
- ✅ Permite usar learning rates más altos
- ✅ Regularización leve adicional
- ✅ Reduce dependencia de inicialización

**Impacto:** +2-3% accuracy, convergencia 2x más rápida

---

### 4.2 Dropout
**¿Qué hace?**
- "Apaga" neuronas aleatoriamente durante entrenamiento
- 0.25 en conv layers (25% apagadas)
- 0.5 en dense layers (50% apagadas)

**¿Por qué mejora?**
- ✅ Previene co-adaptación de neuronas
- ✅ Fuerza redundancia en características
- ✅ Actúa como ensemble implícito

**Impacto:** Reduce overfitting ~50%, +2-4% test accuracy

---

### 4.3 EarlyStopping
**¿Qué hace?**
- Monitoriza `val_loss` cada época
- Si no mejora en 8 épocas → para entrenamiento
- Restaura pesos del mejor modelo

**¿Por qué mejora?**
- ✅ Evita overfitting automáticamente
- ✅ No necesita adivinar número óptimo de épocas
- ✅ Ahorra tiempo de entrenamiento

**Impacto:** Garantiza mejor modelo, ahorra 20-40% tiempo

---

### 4.4 ReduceLROnPlateau
**¿Qué hace?**
- Si `val_loss` no mejora en 4 épocas → LR = LR * 0.5
- Continúa reduciendo hasta min_lr=1e-7

**¿Por qué mejora?**
- ✅ LR alto al inicio → exploración rápida
- ✅ LR bajo al final → refinamiento fino
- ✅ Escapa de mesetas (plateaus)

**Impacto:** +1-2% accuracy final

---

### 4.5 Padding='same'
**Comparación:**
```
Baseline (valid):
28x28 → Conv(3x3) → 26x26  ❌ Pierde 2 píxeles por lado

Final (same):
28x28 → Conv(3x3) → 28x28  ✅ Preserva dimensiones
```

**¿Por qué mejora?**
- ✅ Preserva información de bordes (crítico en 28x28)
- ✅ Permite apilar más capas sin perder resolución
- ✅ En Fashion-MNIST los bordes son importantes (zapatos, ropa)

**Impacto:** +1-2% accuracy

---

### 4.6 Doble Convolución (VGG-style)
**Baseline:** Conv → Pool  
**Final:** Conv → Conv → Pool

**¿Por qué mejora?**
- ✅ Primera conv: detecta bordes y texturas básicas
- ✅ Segunda conv: combina en patrones complejos
- ✅ Campo receptivo más grande (5x5 efectivo vs 3x3)
- ✅ Más parámetros = mayor capacidad

**Impacto:** +2-3% accuracy

---

## 5. Resultados Esperados

| Métrica | Baseline | Final | Mejora |
|---------|----------|-------|--------|
| **Train Accuracy** | ~92% | ~95% | +3% |
| **Val Accuracy** | ~88% | ~92% | +4% |
| **Test Accuracy** | ~87% | ~91% | +4% |
| **Overfitting (gap)** | ~4-5% | ~1-2% | ✅ Reducido |
| **Épocas necesarias** | 15 | ~20-25 | EarlyStopping |
| **Tiempo por época** | 10s | 15s | +50% (más capas) |

---

## 6. Posibles Mejoras Adicionales para el Modelo Final

### 6.1 Data Augmentation ⭐⭐⭐⭐⭐
```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=10,        # Rotar ±10°
    width_shift_range=0.1,    # Desplazar 10%
    height_shift_range=0.1,
    zoom_range=0.1,           # Zoom ±10%
    fill_mode='nearest'
)

history = model.fit(
    datagen.flow(x_train, y_train_cat, batch_size=128),
    epochs=40,
    validation_data=(x_val, y_val_cat),
    callbacks=callbacks
)
```

**Impacto:** +2-4% test accuracy  
**Dificultad:** Baja  
**Tiempo:** 20 minutos  
**¿Por qué?** Aumenta datos artificialmente, mejora generalización

---

### 6.2 Optimizador AdamW ⭐⭐⭐⭐
```python
from tensorflow.keras.optimizers import AdamW

model.compile(
    optimizer=AdamW(learning_rate=0.001, weight_decay=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
```

**Impacto:** +1-2% accuracy  
**Dificultad:** Muy baja  
**Tiempo:** 5 minutos  
**¿Por qué?** Adam mejorado con weight decay correcto

---

### 6.3 Residual Connections (ResNet) ⭐⭐⭐⭐
```python
def residual_block(x, filters):
    shortcut = x
    
    x = layers.Conv2D(filters, (3,3), padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    
    x = layers.Conv2D(filters, (3,3), padding='same')(x)
    x = layers.BatchNormalization()(x)
    
    # Ajustar dimensiones si es necesario
    if shortcut.shape[-1] != filters:
        shortcut = layers.Conv2D(filters, (1,1))(shortcut)
    
    x = layers.Add()([x, shortcut])
    x = layers.Activation('relu')(x)
    return x

# Usar en el modelo
x = residual_block(x, 32)
x = layers.MaxPooling2D((2,2))(x)
```

**Impacto:** +2-3% accuracy  
**Dificultad:** Media  
**Tiempo:** 1-2 horas  
**¿Por qué?** Permite redes más profundas, mejor flujo de gradientes

---

### 6.4 Learning Rate Schedule (Cosine) ⭐⭐⭐
```python
from tensorflow.keras.optimizers.schedules import CosineDecay

lr_schedule = CosineDecay(
    initial_learning_rate=0.001,
    decay_steps=1000
)

optimizer = keras.optimizers.Adam(learning_rate=lr_schedule)
```

**Impacto:** +1-2% accuracy  
**Dificultad:** Baja  
**Tiempo:** 15 minutos  
**¿Por qué?** Reduce LR suavemente, mejor convergencia

---

### 6.5 Mixup Data Augmentation ⭐⭐⭐
```python
def mixup(x, y, alpha=0.2):
    batch_size = x.shape[0]
    lam = np.random.beta(alpha, alpha, batch_size)
    lam = lam.reshape(batch_size, 1, 1, 1)
    
    idx = np.random.permutation(batch_size)
    
    x_mixed = lam * x + (1 - lam) * x[idx]
    y_mixed = lam.reshape(batch_size, 1) * y + (1 - lam).reshape(batch_size, 1) * y[idx]
    
    return x_mixed, y_mixed

# Aplicar durante entrenamiento
```

**Impacto:** +2-3% accuracy  
**Dificultad:** Media  
**Tiempo:** 1-2 horas  
**¿Por qué?** Regularización muy fuerte, modelo más robusto

---

### 6.6 Ensemble de Modelos ⭐⭐⭐⭐
```python
# Entrenar 5 modelos con diferentes seeds
models = []
for i in range(5):
    np.random.seed(i)
    tf.random.set_seed(i)
    
    model = create_model()
    model.fit(x_train, y_train_cat, ...)
    models.append(model)

# Predicción por promedio
predictions = np.mean([model.predict(x_test) for model in models], axis=0)
y_pred = np.argmax(predictions, axis=1)
```

**Impacto:** +2-4% accuracy  
**Dificultad:** Baja  
**Tiempo:** 3-5 horas (entrenamiento)  
**¿Por qué?** Reduce varianza, combina fortalezas de múltiples modelos

---

### 6.7 Attention Mechanism (SE Block) ⭐⭐⭐
```python
def se_block(x, ratio=8):
    channels = x.shape[-1]
    
    # Squeeze
    gap = layers.GlobalAveragePooling2D()(x)
    
    # Excitation
    fc1 = layers.Dense(channels // ratio, activation='relu')(gap)
    fc2 = layers.Dense(channels, activation='sigmoid')(fc1)
    
    # Scale
    fc2 = layers.Reshape((1, 1, channels))(fc2)
    return layers.Multiply()([x, fc2])

# Añadir después de cada bloque conv
x = layers.Conv2D(64, (3,3), padding='same', activation='relu')(x)
x = se_block(x)
```

**Impacto:** +1-2% accuracy  
**Dificultad:** Media  
**Tiempo:** 1-2 horas  
**¿Por qué?** Modelo aprende qué canales son importantes

---

## 7. Priorización de Mejoras

### Top 3 (Máximo ROI)
1. **Data Augmentation** → +3% en 20 min
2. **AdamW** → +1% en 5 min
3. **Ensemble** → +3% (pero 5h entrenamiento)

### Si tienes tiempo
4. **ResNet Blocks** → +2% en 2h
5. **Mixup** → +2% en 2h
6. **Attention** → +1% en 2h

### Resultado final esperado
- **Con Top 3:** ~94-95% test accuracy
- **Con todas:** ~96-97% test accuracy

---

## 8. Resumen Ejecutivo

### Baseline → Final
**Cambios principales:**
1. BatchNormalization (6 lugares)
2. Dropout (3 lugares: 0.25, 0.25, 0.5)
3. EarlyStopping + ReduceLROnPlateau
4. Doble convolución por bloque
5. Padding='same'
6. 256 neuronas en Dense (vs 128)

**Resultado:** +4% accuracy, menos overfitting

### Final → Mejor versión
**Mejoras recomendadas:**
1. Data Augmentation (OBLIGATORIO)
2. AdamW optimizer (FÁCIL)
3. Ensemble o ResNet (ALTO IMPACTO)

