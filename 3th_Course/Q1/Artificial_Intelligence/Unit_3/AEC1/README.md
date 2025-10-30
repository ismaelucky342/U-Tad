# 🐕🐱 Dogs vs. Cats 2025 - Notebook Optimizado

## 📋 Descripción del Proyecto

Este notebook implementa una solución completa y optimizada para la competición **[U-Tad] Dogs vs. Cats 2025** de Kaggle, utilizando técnicas modernas de Deep Learning y Transfer Learning con PyTorch.

## 🔄 Cambios Respecto a la Versión Anterior

### 1. **Migración Completa de Framework**
- ❌ **Antes**: Keras/TensorFlow
- ✅ **Ahora**: PyTorch con timm y Albumentations
  - Mayor flexibilidad y control sobre el entrenamiento
  - Soporte nativo para mixed precision training
  - Mejor integración con modelos preentrenados modernos

### 2. **Modelo y Arquitectura**
- ❌ **Antes**: Modelo básico sin especificar
- ✅ **Ahora**: **EfficientNet-B3** preentrenado en ImageNet
  - Transfer learning desde ImageNet
  - Funciones para congelar/descongelar el backbone
  - Arquitectura eficiente y moderna

### 3. **Estrategia de Validación**
- ❌ **Antes**: Train/validation split simple
- ✅ **Ahora**: **K-Fold Cross-Validation con 5 folds**
  - Mejor estimación del rendimiento real
  - Reduce el riesgo de overfitting
  - Ensemble de 5 modelos para predicciones más robustas

### 4. **Entrenamiento por Etapas**
- ❌ **Antes**: Entrenamiento en una sola etapa
- ✅ **Ahora**: **Dos etapas de entrenamiento**
  - **Etapa 1**: 5 epochs con backbone congelado (solo cabeza)
  - **Etapa 2**: 15 epochs de fine-tuning completo
  - Learning rates adaptativos (1e-3 → 1e-4)

### 5. **Data Augmentation Mejorado**
- ❌ **Antes**: Augmentation básico o inexistente
- ✅ **Ahora**: **Albumentations con transformaciones modernas**
  - RandomResizedCrop (scale 0.8-1.0)
  - HorizontalFlip (p=0.5)
  - RandomBrightnessContrast (±0.2)
  - ShiftScaleRotate (shift=0.1, scale=0.1, rotate=15°)
  - Normalización ImageNet

### 6. **Optimizaciones de Entrenamiento**
- ❌ **Antes**: Entrenamiento estándar
- ✅ **Ahora**: Múltiples optimizaciones
  - **Mixed Precision Training** (torch.cuda.amp) → ~2x más rápido
  - **AdamW optimizer** con weight_decay=1e-2
  - **Label Smoothing** (0.1) para mejor generalización
  - **Early Stopping** (patience=5) para evitar overfitting
  - Guardado del mejor modelo por validation accuracy

### 7. **Inference y Ensemble**
- ❌ **Antes**: Predicciones de un solo modelo
- ✅ **Ahora**: **Ensemble de 5 modelos (K-Fold)**
  - Promedio de predicciones de los 5 folds
  - Mayor estabilidad y precisión
  - Reducción de la varianza

### 8. **Estructura y Organización**
- ❌ **Antes**: Código básico sin estructura clara
- ✅ **Ahora**: **Notebook modular y bien organizado**
  - Secciones claramente definidas
  - Funciones reutilizables
  - Comentarios detallados en español
  - Dataset y DataLoader personalizados

### 9. **Reproducibilidad**
- ❌ **Antes**: Sin control de semillas
- ✅ **Ahora**: **100% reproducible**
  - Todas las semillas fijadas (torch, numpy, cuda)
  - Configuración determinística
  - Pin memory y workers configurados

### 10. **Visualización y Análisis**
- ❌ **Antes**: Sin visualización
- ✅ **Ahora**: **Visualizaciones incluidas**
  - Función para visualizar predicciones
  - Estadísticas detalladas del entrenamiento
  - Resumen de métricas por fold

## 🏗️ Estructura del Notebook

1. **Configuración**
   - Imports de PyTorch, timm, Albumentations
   - Configuración de seeds y device
   - Hiperparámetros globales

2. **Preparación del Dataset**
   - CustomDataset de PyTorch
   - Función para cargar datos de entrenamiento
   - Separación de imágenes y etiquetas

3. **Transformaciones y Data Augmentation**
   - Train transforms (con augmentation)
   - Validation/Test transforms (sin augmentation)

4. **Modelo con Transfer Learning**
   - Creación de EfficientNet-B3
   - Funciones freeze/unfreeze
   - Configuración para clasificación binaria

5. **Funciones de Entrenamiento y Validación**
   - train_epoch con mixed precision
   - validate_epoch sin actualización de pesos
   - Métricas (loss, accuracy)

6. **Entrenamiento con K-Fold**
   - StratifiedKFold (5 folds)
   - Loop por cada fold
   - Etapa 1: backbone congelado
   - Etapa 2: fine-tuning completo
   - Early stopping y guardado del mejor modelo

7. **Inferencia en Test Set**
   - TestDataset personalizado
   - Predicciones de los 5 folds
   - Promedio de predicciones

8. **Generación de Submission**
   - Creación de submission.csv
   - Formato correcto para Kaggle
   - Estadísticas de las predicciones

9. **Visualización (Opcional)**
   - Función para mostrar predicciones
   - Visualización de confianza del modelo

10. **Conclusiones**
    - Resumen de técnicas implementadas
    - Mejoras posibles
    - Checklist de features

## 🚀 Tecnologías Utilizadas

- **PyTorch** - Framework principal
- **timm** - Transfer learning con modelos preentrenados
- **Albumentations** - Data augmentation avanzado
- **scikit-learn** - K-Fold cross-validation
- **pandas** - Manipulación de datos
- **matplotlib** - Visualización

## 📊 Hiperparámetros Principales

```python
CONFIG = {
    'model_name': 'efficientnet_b3',
    'img_size': 300,
    'num_classes': 2,
    'batch_size': 32,
    'num_folds': 5,
    'epochs_stage1': 5,      # Backbone congelado
    'epochs_stage2': 15,     # Fine-tuning completo
    'lr_stage1': 1e-3,
    'lr_stage2': 1e-4,
    'weight_decay': 1e-2,
    'label_smoothing': 0.1,
    'num_workers': 2
}
```

## 🎯 Características Clave

✅ Transfer Learning con EfficientNet-B3  
✅ K-Fold Cross-Validation (5 folds)  
✅ Entrenamiento por etapas (congelado + fine-tuning)  
✅ Data Augmentation moderado con Albumentations  
✅ Mixed Precision Training (AMP)  
✅ Label Smoothing (0.1)  
✅ AdamW optimizer con weight decay  
✅ Early Stopping (patience=5)  
✅ Ensemble de predicciones (promedio de 5 folds)  
✅ 100% reproducible (seeds fijadas)  
✅ Código limpio y comentado  

## 🔧 Requisitos

```bash
torch>=2.0.0
torchvision>=0.15.0
timm>=0.9.0
albumentations>=1.3.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
Pillow>=10.0.0
```

## 💻 Uso

1. **En Kaggle**:
   - Crear un nuevo notebook
   - Copiar todo el código
   - Asegurarse de tener GPU activada
   - Ejecutar todas las celdas
   - Descargar `submission.csv`

2. **Localmente**:
   - Instalar dependencias
   - Ajustar rutas de datos en CONFIG
   - Ejecutar el notebook
   - Generar submission.csv

## 📈 Mejoras Futuras Posibles

- [ ] Usar EfficientNet-B4 o B5 (más precisión)
- [ ] Aumentar epochs en etapa 2
- [ ] Probar SGD con momentum
- [ ] Añadir CutOut, MixUp, CutMix
- [ ] Test Time Augmentation (TTA)
- [ ] Probar otros modelos (ResNet, ConvNeXt)
- [ ] Ajuste fino de learning rate con scheduler

## 👤 Autor

**Ismael Hormigo Castro** - U-Tad 2025

## 📅 Fecha

30 de octubre de 2025

## 📝 Notas

Este notebook está diseñado para ser ejecutado en el entorno de Kaggle GPU sin necesidad de dependencias manuales. Todo el código es reproducible y está optimizado para maximizar la precisión en la competición Dogs vs. Cats.

---

**¡Listo para subir a Kaggle y conseguir un buen score! 🎯**