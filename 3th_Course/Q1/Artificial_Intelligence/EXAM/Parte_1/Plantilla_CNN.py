# Red Neuronal Convolucional Básica usando Keras  # Título/descrición del script

# =============================================================================  # Separador visual (comentario)
# Configuramos Keras para usar JAX como backend en lugar de TensorFlow  # Explica propósito del bloque
import os  # Importa el módulo os para manejar variables de entorno y rutas
os.environ["KERAS_BACKEND"] = "jax"  # Establece la variable de entorno KERAS_BACKEND para usar JAX

# =============================================================================  # Separador visual (comentario)
# IMPORTACIÓN DE LIBRERÍAS  # Encabezado del bloque de importación
# =============================================================================  # Separador visual (comentario)
import keras  # Importa la biblioteca Keras (interfaz de alto nivel para redes neuronales)
from keras import layers  # Importa el submódulo 'layers' para definir capas de la red
from keras import Sequential  # Importa la clase Sequential para construir el modelo en secuencia
from keras.datasets import mnist  # Importa el dataset MNIST incluido en Keras
from sklearn.model_selection import train_test_split  # Importa utilidad para dividir conjuntos (no usada en el código actual)
from sklearn.preprocessing import OneHotEncoder  # Importa OneHotEncoder para convertir etiquetas a one-hot
import numpy as np  # Importa NumPy con el alias np para operaciones numéricas

# =============================================================================  # Separador visual (comentario)
# CARGA DE DATOS  # Encabezado del bloque de carga de datos
# =============================================================================  # Separador visual (comentario)
# Cargamos el dataset MNIST de dígitos escritos a mano  # Explica lo que hace la siguiente línea
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()  # Descarga y carga las imágenes y etiquetas de entrenamiento y prueba

# =============================================================================  # Separador visual (comentario)
# PREPROCESAMIENTO DE DATOS  # Encabezado del bloque de preprocesamiento
# =============================================================================  # Separador visual (comentario)
# Normalizamos las imágenes dividiendo por 255 para tener valores entre 0 y 1  # Explica normalización
train_images = train_images.astype('float32') / 255.0  # Convierte a float32 y normaliza píxeles de entrenamiento
test_images = test_images.astype('float32') / 255.0  # Convierte a float32 y normaliza píxeles de prueba

# Aplanamos las imágenes para que sean vectores de 784 elementos (28*28)  # Explica reshaping
train_images = train_images.reshape((60000, 28 * 28))  # Remodela las imágenes de entrenamiento a vectores de 784 elementos
test_images = test_images.reshape((10000, 28 * 28))  # Remodela las imágenes de prueba a vectores de 784 elementos

# Aplicamos One-Hot Encoding a las etiquetas  # Explica propósito del codificador
encoder = OneHotEncoder(sparse=False)  # Crea el codificador one-hot (sparse=False devuelve array denso)
train_labels = encoder.fit_transform(train_labels.reshape(-1, 1))  # Ajusta el codificador en las etiquetas de entrenamiento y transforma
test_labels = encoder.transform(test_labels.reshape(-1, 1))  # Transforma las etiquetas de prueba según el codificador ya ajustado

# =============================================================================  # Separador visual (comentario)
# CONSTRUCCIÓN DEL MODELO  # Encabezado del bloque de construcción del modelo
# =============================================================================  # Separador visual (comentario)
model = Sequential([  # Crea un modelo secuencial y define sus capas en una lista
    layers.Dense(128, input_shape=(784,), activation='relu'),  # Capa densa oculta con 128 neuronas y activación ReLU, entrada de 784
    layers.Dense(64, activation='relu'),                       # Segunda capa densa oculta con 64 neuronas y activación ReLU
    layers.Dense(10, activation='softmax')                     # Capa de salida con 10 neuronas y activación softmax para clasificación multiclase
])

# =============================================================================  # Separador visual (comentario)
# COMPILACIÓN DEL MODELO  # Encabezado del bloque de compilación
# =============================================================================  # Separador visual (comentario)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])  # Compila el modelo indicando optimizador, función de pérdida y métricas
model.summary()  # Muestra un resumen del modelo (capas, parámetros, forma de salida)

# =============================================================================  # Separador visual (comentario)
# ENTRENAMIENTO DEL MODELO  # Encabezado del bloque de entrenamiento
# =============================================================================  # Separador visual (comentario)
model.fit(train_images, train_labels, epochs=10, batch_size=32, verbose=1)  # Entrena el modelo con los datos de entrenamiento durante 10 épocas

# =============================================================================  # Separador visual (comentario)
# EVALUACIÓN DEL MODELO  # Encabezado del bloque de evaluación
# =============================================================================  # Separador visual (comentario)
loss, accuracy = model.evaluate(test_images, test_labels)  # Evalúa el modelo en el conjunto de prueba y devuelve pérdida y precisión
print(f"Precisión en el conjunto de prueba: {accuracy*100:.2f}%")  # Imprime la precisión en porcentaje con dos decimales

# =============================================================================  # Separador visual (comentario)
# PREDICCIÓN CON EL MODELO  # Encabezado del bloque de predicción
# =============================================================================  # Separador visual (comentario)
predictions = model.predict(test_images)  # Genera probabilidades de clase para las imágenes de prueba
predicted_classes = np.argmax(predictions, axis=1)  # Convierte las probabilidades a etiquetas predichas (índice de la máxima probabilidad)
print("Predicciones de las primeras 10 imágenes de prueba:", predicted_classes[:10])  # Imprime las primeras 10 etiquetas predichas
