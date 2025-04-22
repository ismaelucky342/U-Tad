import json
import random
import numpy as np
import nltk
from nltk.stem import PorterStemmer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

# Inicializar
stemmer = PorterStemmer()
nltk.download('punkt')

# Cargar los datos
with open("intents.json") as file:
    data = json.load(file)

# Preprocesamiento
words = []
classes = []
documents = []
ignore_words = ["?", "!", ".", ","]

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent["tag"]))
    if intent["tag"] not in classes:
        classes.append(intent["tag"])

# Stem, lowercase y limpieza
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(set(words))
classes = sorted(set(classes))

# Datos de entrenamiento
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = [stemmer.stem(w.lower()) for w in doc[0]]
    for w in words:
        bag.append(1 if w in pattern_words else 0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

# Mezclar y convertir
random.shuffle(training)
training = np.array(training, dtype=object)

train_x = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

# Modelo
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))

# Compilar
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])
model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

# Funciones para el chat
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def classify(sentence):
    input_data = bow(sentence, words)
    res = model.predict(np.array([input_data]))[0]
    results = [(i, r) for i, r in enumerate(res) if r > 0.2]

    results.sort(key=lambda x: x[1], reverse=True)
    return classes[results[0][0]] if results else "no_match"

def get_response(tag):
    for intent in data["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    return "No entiendo lo que dices."

# Chat
print("Chatbot: ¡Hola! Escribe algo (o 'salir'):")
while True:
    message = input("Tú: ")
    if message.lower() == "salir":
        print("Chatbot: ¡Hasta luego!")
        break

    intent = classify(message)
    response = get_response(intent)
    print("Chatbot:", response)
