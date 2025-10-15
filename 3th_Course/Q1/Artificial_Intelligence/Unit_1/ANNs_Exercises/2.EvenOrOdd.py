import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Números del 0 al 99
X = np.array(range(100)).reshape(-1, 1)  # entrada
y = np.array([0 if i % 2 == 0 else 1 for i in range(100)])  # 0=par, 1=impar

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear modelo
model = Sequential([
    Dense(10, input_shape=(1,), activation='relu'),  # capa oculta con 10 neuronas
    Dense(10, activation='relu'),                    # segunda capa oculta
    Dense(1, activation='sigmoid')                   # capa de salida (1 clase)
])

# Compilar modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar modelo
model.fit(X_train, y_train, epochs=100, batch_size=5, verbose=1)

# Evaluar modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Precisión: {accuracy*100:.2f}%")
