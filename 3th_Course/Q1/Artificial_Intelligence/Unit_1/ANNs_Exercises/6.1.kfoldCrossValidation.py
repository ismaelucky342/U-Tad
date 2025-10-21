import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import KFold

# --------------------------------
# Datos
# --------------------------------
# Ejemplo: Definir x_train y y_train como arrays de ejemplo
# Reemplaza esto con tus propios datos
x_train = np.random.rand(100, 10)  # 100 muestras, 10 características
y_train = np.random.rand(100, 1)   # 100 targets

X = x_train  # Features de entrenamiento
y = y_train  # Targets de entrenamiento

# --------------------------------
# Configurar k-fold cross-validation
# --------------------------------
kf = KFold(n_splits=5, shuffle=True, random_state=42)  # 5 folds, mezclamos datos antes de dividir
mse_scores = []  # Lista para guardar el MSE de cada fold
mae_scores = []  # Lista para guardar el MAE de cada fold

# --------------------------------
# Iterar sobre cada fold
# --------------------------------
for train_index, val_index in kf.split(X):
    # Dividir los datos en entrenamiento y validación según los índices del fold actual
    X_train_fold, X_val_fold = X[train_index], X[val_index]
    y_train_fold, y_val_fold = y[train_index], y[val_index]
    
    # --------------------------------
    # Definir el modelo Keras
    # --------------------------------
    model = Sequential([Dense(1, activation="linear", input_shape=(X.shape[1],))])  # Una capa lineal
    model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mae"])  # Compilar con MSE y MAE
    
    # --------------------------------
    # Entrenamiento del modelo en este fold
    # --------------------------------
    model.fit(X_train_fold, y_train_fold, epochs=50, batch_size=32, verbose=0)  # verbose=0 para no imprimir todo
    
    # --------------------------------
    # Evaluar el modelo en el fold de validación
    # --------------------------------
    mse, mae = model.evaluate(X_val_fold, y_val_fold, verbose=0)  # Obtener métricas
    mse_scores.append(mse)  # Guardar MSE de este fold
    mae_scores.append(mae)  # Guardar MAE de este fold

# --------------------------------
# Resultados finales
# --------------------------------
print("MSE promedio:", np.mean(mse_scores))  # Promedio de MSE en los 5 folds
print("MAE promedio:", np.mean(mae_scores))  # Promedio de MAE en los 5 folds

import matplotlib.pyplot as plt

folds = range(1, len(mse_scores) + 1)
plt.figure(figsize=(8, 5))
plt.plot(folds, mse_scores, marker='o', label='MSE por fold')
plt.plot(folds, mae_scores, marker='s', label='MAE por fold')
plt.xlabel('Fold')
plt.ylabel('Score')
plt.title('MSE y MAE en cada fold de K-Fold Cross Validation')
plt.legend()
plt.grid(True)
plt.show()