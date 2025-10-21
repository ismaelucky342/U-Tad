import os
os.environ["KERAS_BACKEND"] = "jax"

import keras
from keras import layers
from keras import Sequential
from keras.datasets import california_housing
from sklearn.preprocessing import StandardScaler

# tupla, con parentesis que sino es una guarrada
(train_data, train_targets), (test_data, test_targets) = california_housing.load_data(version="small")

# formas de los arrays
print("train_data.shape:", train_data.shape)
print("test_data.shape:", test_data.shape)

# scaler = StandardScaler()
mu = train_data.mean(axis=0)
s = train_data.std(axis=0)
x_train = (train_data - mu) / s
x_test = (test_data - mu) / s

y_train = train_targets / 1e5
y_test = test_targets / 1e5

model = keras.Sequential([
    layers.Dense(64, activation="relu"), 
    layers.Dense(64, activation="relu"), 
    layers.Dense(1, activation="linear")
])
model.summary()

model.compile(
    optimizer="adam",
    loss="mean_squared_error",
    metrics=["mean_absolute_error"],
)

num_epochs = 100
batch_size = 16

history = model.fit(
    x_train, y_train,
    validation_split=0.2,
    epochs=num_epochs,
    batch_size=batch_size,
)

model.summary()
