from keras.datasets import california_housing
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np

# Cargar dataset
(train_data, train_targets), (test_data, test_targets) = california_housing.load_data(version="small")

# Normalizar
mu = train_data.mean(axis=0)
s = train_data.std(axis=0)
x_train = (train_data - mu) / s
x_test = (test_data - mu) / s
y_train = train_targets / 1e5
y_test = test_targets / 1e5

# Modelo lineal
model = Sequential([Dense(1, activation="linear", input_shape=(x_train.shape[1],))])
model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mae"])

# Entrenamiento
history = model.fit(x_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Predicciones sobre test set
y_pred = model.predict(x_test)

# Opcional: Gráfico de predicción vs real
plt.scatter(y_test, y_pred)
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Predicciones vs Valores Reales")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # línea ideal
plt.show()