import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Cargar datos
iris = load_iris()
X = iris.data  # características
y = iris.target.reshape(-1, 1)  # etiquetas

# One-hot encoding
encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y)

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear modelo
model = Sequential([
    Dense(10, input_shape=(4,), activation='relu'),  # capa oculta con 10 neuronas
    Dense(10, activation='relu'),                    # segunda capa oculta
    Dense(3, activation='softmax')                  # capa de salida (3 clases)
])

# Compilar modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar modelo
model.fit(X_train, y_train, epochs=100, batch_size=5, verbose=1)

# Evaluar modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Precisión: {accuracy*100:.2f}%")
