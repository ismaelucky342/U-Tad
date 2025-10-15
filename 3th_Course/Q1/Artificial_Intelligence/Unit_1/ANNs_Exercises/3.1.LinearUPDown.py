import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# Generamos 100 puntos aleatorios (x, y)
np.random.seed(42)
X = np.random.rand(100, 2) * 10  # 2 características: x e y
y = (X[:,1] > 5).astype(int)      # 1 si y > 5, 0 si y <= 5

plt.scatter(X[:,0], X[:,1], c=y, cmap='bwr')
plt.axhline(5, color='black', linestyle='--')  # línea y=5
plt.show()

model = Sequential([
    Dense(5, input_shape=(2,), activation='relu'),
    Dense(5, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=100, batch_size=5, verbose=1)

preds = (model.predict(X) > 0.5).astype(int)

plt.scatter(X[:,0], X[:,1], c=preds.flatten(), cmap='bwr')
plt.axhline(5, color='black', linestyle='--')
plt.savefig("resultado.png")
