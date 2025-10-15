import numpy as np
import matplotlib.pyplot as plt
import os

# Crear carpeta para guardar imágenes
os.makedirs('4.2.LinearRegression', exist_ok=True)

#  Datos con ruido
np.random.seed(42)
X = np.linspace(0, 10, 15).reshape(-1,1)
y = 3 * X.flatten() + 4 + np.random.randn(15) * 5

# Inicializar parámetros de la recta
w = np.random.randn()
b = np.random.randn()
lr = 0.01  # tasa de aprendizaje
epochs = 50

# Función de predicción
def predict(X, w, b):
    return w*X.flatten() + b

# Gradiente descendente paso a paso
for epoch in range(epochs):
    y_pred = predict(X, w, b)
    error = y_pred - y

    # Gradientes
    dw = (2/len(X)) * np.sum(error * X.flatten())
    db = (2/len(X)) * np.sum(error)

    # Actualizar parámetros
    w -= lr * dw
    b -= lr * db

    # Graficar en cada paso
    plt.figure(figsize=(8,6))
    plt.scatter(X, y, color='blue', label='Puntos reales')
    plt.plot(X, y_pred, color='red', label='Recta ajustada')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Regresión paso {epoch+1}')
    plt.legend()
    plt.savefig(f'4.2.LinearRegression/paso_{epoch+1:03d}.png')
    plt.close()

print("📂 Todas las imágenes guardadas en la carpeta '4.2.LinearRegression'.")
