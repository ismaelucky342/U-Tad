# Red Neuronal Convolucional Básica usando Keras

# =============================================================================
# Configuramos Keras para usar JAX como backend en lugar de TensorFlow
import os
os.environ["KERAS_BACKEND"] = "jax"

# =============================================================================
# IMPORTACIÓN DE LIBRERÍAS
# =============================================================================
import keras
from keras import layers
from keras import Sequential
from keras.datasets import mnist
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# =============================================================================
# CARGA DE DATOS
# =============================================================================
# Cargamos el dataset MNIST de dígitos escritos a mano
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# =============================================================================
# PREPROCESAMIENTO DE DATOS
# =============================================================================
# Normalizamos las imágenes dividiendo por 255 para tener valores entre 0 y 1
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# Aplanamos las imágenes para que sean vectores de 784 elementos (28*28)
train_images = train_images.reshape((60000, 28 * 28))
test_images = test_images.reshape((10000, 28 * 28))

# Aplicamos One-Hot Encoding a las etiquetas
encoder = OneHotEncoder(sparse=False)
train_labels = encoder.fit_transform(train_labels.reshape(-1, 1))
test_labels = encoder.transform(test_labels.reshape(-1, 1))

# =============================================================================
# CONSTRUCCIÓN DEL MODELO
# =============================================================================
model = Sequential([
    layers.Dense(128, input_shape=(784,), activation='relu'),  # Capa oculta con 128 neuronas
    layers.Dense(64, activation='relu'),                       # Segunda capa oculta con 64 neuronas
    layers.Dense(10, activation='softmax')                     # Capa de salida para 10 clases
])

# =============================================================================
# COMPILACIÓN DEL MODELO
# =============================================================================
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# =============================================================================
# ENTRENAMIENTO DEL MODELO
# =============================================================================
model.fit(train_images, train_labels, epochs=10, batch_size=32, verbose=1)

# =============================================================================
# EVALUACIÓN DEL MODELO
# =============================================================================
loss, accuracy = model.evaluate(test_images, test_labels)
print(f"Precisión en el conjunto de prueba: {accuracy*100:.2f}%")

# =============================================================================
# PREDICCIÓN CON EL MODELO
# =============================================================================
predictions = model.predict(test_images)
predicted_classes = np.argmax(predictions, axis=1)
print("Predicciones de las primeras 10 imágenes de prueba:", predicted_classes[:10])

