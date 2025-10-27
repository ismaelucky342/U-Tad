# =============================================================================
# CONFIGURACIÓN INICIAL - Backend de Keras
# =============================================================================
# Configuramos Keras para usar JAX como backend en lugar de TensorFlow
import os 
os.environ["KERAS_BACKEND"] = "jax"

# =============================================================================
# IMPORTACIÓN DE LIBRERÍAS
# =============================================================================
# Importamos las librerías necesarias para construir y entrenar la red neuronal
import keras
from keras import layers
from keras import Sequential
from keras.datasets import california_housing
from sklearn.preprocessing import StandardScaler

# =============================================================================
# CARGA DE DATOS
# =============================================================================
# Cargamos el dataset de precios de viviendas en California
# El dataset se divide en conjunto de entrenamiento y prueba
# tupla, con paréntesis que sino es una guarrada
(train_data, train_targets), (test_data, test_targets) = california_housing.load_data(version="small")

# Verificamos las dimensiones de los datos de entrenamiento
print("Shape de datos de entrenamiento:", train_data.shape)

# Verificamos las dimensiones de los datos de prueba
print("Shape de datos de prueba:", test_data.shape)

# Verificamos el valor mínimo de los targets de entrenamiento
print("Valor mínimo de targets:", train_targets.min())

# =============================================================================
# NORMALIZACIÓN DE DATOS
# =============================================================================
# Normalizamos los datos de entrada usando la media y desviación estándar
# del conjunto de entrenamiento (importante: NO usar estadísticas del test)
mu = train_data.mean(axis=0)
s = train_data.std(axis=0)
x_train = (train_data - mu) / s
x_test = (test_data - mu) / s

# Escalamos los targets dividiéndolos por 100,000 para facilitar el entrenamiento
y_train = train_targets / 1e5
y_test = test_targets / 1e5

# =============================================================================
# CONSTRUCCIÓN DEL MODELO
# =============================================================================
# Creamos una red neuronal secuencial con:
# - 2 capas ocultas de 64 neuronas cada una con activación ReLU
# - 1 capa de salida con 1 neurona y activación lineal (regresión)
model = keras.Sequential([
    layers.Dense(64, activation="relu"), 
    layers.Dense(64, activation="relu"), 
    layers.Dense(1, activation="linear")
])
model.summary()

# =============================================================================
# COMPILACIÓN DEL MODELO
# =============================================================================
# Configuramos el optimizador, función de pérdida y métricas
# - Optimizador: Adam (adaptativo, buen rendimiento general)
# - Loss: MSE (Error Cuadrático Medio, común en regresión)
# - Métrica: MAE (Error Absoluto Medio, interpretable)
model.compile(
    optimizer="adam",
    loss="mean_squared_error",
    metrics=["mean_absolute_error"]
)

# =============================================================================
# ENTRENAMIENTO DEL MODELO
# =============================================================================
# Definimos hiperparámetros del entrenamiento
num_epochs = 100  # Número de épocas (pasadas completas por los datos)
batch_size = 16   # Tamaño del lote para el descenso del gradiente

# Entrenamos el modelo con validación del 20% de los datos de entrenamiento
history = model.fit(
    x_train, y_train,
    validation_split=0.2,
    epochs=num_epochs,
    batch_size=batch_size,
)

# =============================================================================
# RESUMEN FINAL DEL MODELO
# =============================================================================
# Mostramos el resumen del modelo entrenado
model.summary()

print("\n¡Entrenamiento completado!")
