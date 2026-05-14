# Unidad 6. Aplicaciones de Deep Learning en NLP: LLMS con Python



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Modelos Transformers Con Hugging Face Transformers](#2-modelos-transformers-con-hugging-face-transformers)
  - [2.1 Introducción](#21-introducción)
  - [2.2 Fundamentos de la arquitectura Transformer](#22-fundamentos-de-la-arquitectura-transformer)
  - [2.3 Representaciones distribuidas y mecanismo de autoatención](#23-representaciones-distribuidas-y-mecanismo-de-autoatención)
  - [2.4 Uso de Hugging Face Transformers: pipelines y modelos preentrenados](#24-uso-de-hugging-face-transformers-pipelines-y-modelos-preentrenados)
  - [2.5 Enlaces de interés](#25-enlaces-de-interés)
- [3. Nlp Con Keras, Tensorflow Y Pytorch](#3-nlp-con-keras-tensorflow-y-pytorch)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Preprocesamiento y tokenización](#32-preprocesamiento-y-tokenización)
  - [3.3 Caso de uso con Keras/TensorFlow](#33-caso-de-uso-con-kerastensorflow)
  - [3.4 Caso de uso con PyTorch](#34-caso-de-uso-con-pytorch)
  - [3.5 ¿Cuál elegir?](#35-cuál-elegir)
- [4. Consideraciones De Rendimiento En Llms: Cpu Vs Gpu Y Aceleradores](#4-consideraciones-de-rendimiento-en-llms-cpu-vs-gpu-y-aceleradores)
  - [4.1 Introducción](#41-introducción)
  - [4.2 CPU vs. GPU: ¿por qué preferir la GPU en LLMs?](#42-cpu-vs-gpu-por-qué-preferir-la-gpu-en-llms)
  - [4.3 TPUs y otros aceleradores](#43-tpus-y-otros-aceleradores)
  - [4.4 Paralelismo y optimización](#44-paralelismo-y-optimización)
- [5. Implementación De Llms Con Tensorflow Y Pytorch](#5-implementación-de-llms-con-tensorflow-y-pytorch)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Pipeline de entrenamiento](#52-pipeline-de-entrenamiento)
  - [5.3 Implementación de un LLM con TensorFlow](#53-implementación-de-un-llm-con-tensorflow)
  - [5.4 Implementación de un LLM con PyTorch](#54-implementación-de-un-llm-con-pytorch)
- [6. Uso De Hugging Face Para Implementación Y Despliegue De Modelos](#6-uso-de-hugging-face-para-implementación-y-despliegue-de-modelos)
  - [6.1 Introducción](#61-introducción)
  - [6.2 ¿Por qué usar la Hugging Face Model Hub?](#62-por-qué-usar-la-hugging-face-model-hub)
  - [6.3 ¿Cómo subir un modelo a Hugging Face?](#63-cómo-subir-un-modelo-a-hugging-face)
  - [6.4 Chat local con modelos del Hub](#64-chat-local-con-modelos-del-hub)
- [7. Conclusiones](#7-conclusiones)
  - [7.1 Conclusiones de la unidad](#71-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad, nos adentraremos en el campo de los modelos de lenguaje de gran tamaño (LLMs) y sus aplicaciones en el Procesamiento de Lenguaje Natural (NLP) utilizando Python. El auge de los Transformers ha supuesto un salto cualitativo en la capacidad de los modelos para generar, resumir y comprender texto. Este avance ha abierto oportunidades para crear aplicaciones que abarcan desde asistentes virtuales capaces de realizar búsquedas contextuales, hasta sistemas de recomendación que analizan grandes volúmenes de documentación técnica o corporativa.

Como ingenieros de software, comprender los fundamentos de estos modelos no solo implica manejar la teoría de arquitecturas de atención y representaciones distribuidas, sino también dominar el entorno práctico necesario para su entrenamiento, ajuste fino y despliegue. Herramientas como Hugging Face Transformers facilitan la adopción de LLMs populares (BERT, GPT, T5, entre otros) y proporcionan un ecosistema rico en modelos preentrenados, contribuyendo significativamente a la productividad en prototipos y soluciones de producción.

A lo largo de esta unidad, expondremos ejemplos de código y describiremos en profundidad las estrategias para integrar LLMs con librerías como TensorFlow, PyTorch y Hugging Face. Además, analizaremos las consideraciones de rendimiento que surgen al trabajar con modelos de gran tamaño, explicando cuándo y cómo podemos escalar un prototipo en entornos GPU o en aceleradores especializados. Por último, veremos el pipeline completo de implementación y despliegue, desde la importación de un modelo base hasta la creación de un servicio de inferencia, prestando atención a la optimización y a las buenas prácticas de la industria.

Este contenido, junto con las unidades precedentes, nos permitirá incorporar de forma sólida las metodologías de Deep Learning aplicado al NLP en nuestros proyectos, abriendo camino a la creación de sistemas más inteligentes y eficaces que exploten el potencial del lenguaje natural en múltiples contextos.



- **Modelos transformadores con Hugging Face Transformers**  
  En este apartado, explicaremos los fundamentos técnicos de la arquitectura Transformer y mostraremos cómo integrarla en un pipeline de Hugging Face, completando ejemplos de código que servirán como base para proyectos más avanzados.
- **NLP con Keras, Tensorflow y Pytorch**  
  Este apartado pretende aunar ambos paradigmas (Keras/TensorFlow y PyTorch) para mostrar ejemplos de entrenamiento y predicción con modelos de lenguaje. Antes de sumergirnos en los ejemplos, revisaremos algunos conceptos de preprocesamiento que resultan críticos en NLP y que, aunque vistos en la teoría, merecen atención práctica.
- **Consideraciones de rendimiento en LLMS: CPU vs GPU y Aceleradores**  
  El objetivo es brindar una guía técnica que nos oriente en la decisión de compra o alquiler de recursos de cómputo, así como en la configuración de su pipeline de entrenamiento y despliegue.
- **Implementación de LLMS con Tensorflow y Pytorch**  
  En los apartados anteriores, hemos analizado la arquitectura Transformer, el uso de Hugging Face para el fine-tuning de modelos, las librerías Keras/TensorFlow y PyTorch para casos de NLP, así como las consideraciones de rendimiento que surgen al entrenar modelos de lenguaje de gran tamaño (LLMs). Ahora, en este cuarto apartado, consolidamos todo ese conocimiento y presentamos ejemplos más avanzados de implementación de LLMs tanto en TensorFlow como en PyTorch,
- **Uso de Hugging Face para implementación y despliegue de modelos**  
  La plataforma de Hugging Face se ha convertido en un referente para estos fines, ofreciendo un Model Hub con miles de repositorios, así como herramientas para la orquestación y el serving. A lo largo de este apartado, describiremos cómo subir modelos a la Hub, cómo descargarlos y validarlos en producción, y cómo se integran en flujos de despliegue continuo. Además, mostraremos cómo levantar localmente un LLM para un uso tipo “chat” sin necesidad de reentrenarlo.



#### Objetivos



Al concluir esta unidad, el estudiante será capaz de:



1. Conocer la arquitectura y el funcionamiento de los modelos Transformers: entender cómo los mecanismos de self-attention y feed-forward posibilitan el modelado del contexto en secuencias de texto. Familiarizarse con la evolución de las arquitecturas pre-Transformer hacia los LLMs actuales.
2. Dominar el uso de las librerías de Python más relevantes para NLP: aprender a cargar y adaptar modelos preentrenados mediante Hugging Face Transformers. Manejar conceptos de tokenización, pipelines y fine-tuning.
3. Implementar modelos de NLP con Keras, TensorFlow y PyTorch: realizar ejemplos prácticos de construcción y entrenamiento de modelos de lenguaje. Aplicar técnicas de regularización, learning rate schedules y métricas de evaluación.
4. Explorar las consideraciones de rendimiento en LLMs: distinguir la conveniencia de CPU, GPU o TPU según el tamaño del modelo y el volumen de datos. Conocer estrategias de paralelismo y escalado (Data Parallel, Model Parallel).
5. Desplegar modelos de gran tamaño en entornos productivos: entender la integración de modelos con pipelines CI/CD. Trabajar con Hugging Face Model Hub, creando y publicando repositorios de modelos.
6. Capacitar para la toma de decisiones técnicas y éticas: evaluar el coste computacional de un LLM y sus implicaciones de consumo energético. Reflexionar sobre los riesgos potenciales del uso de LLMs (sesgos, generación de contenido inadecuado, etc.) y mitigarlos en la medida de lo posible.



## 2. Modelos Transformers Con Hugging Face Transformers



### 2.1 Introducción



![image](assets/cm9bnwxiz0058356x92ablurj-stock-image.jpg)



Los Transformers han supuesto una revolución en el campo del Procesamiento de Lenguaje Natural (NLP) en los últimos años, llegando incluso a sustituir a modelos previos basados en redes recurrentes (RNN, LSTM) o convoluciones (CNN). Gracias a su enfoque de self-attention, los Transformers pueden manejar secuencias de texto (o cualquier tipo de datos secuenciales) sin necesidad de procesarlas estrictamente de forma secuencial. Esto permite que entrenemos en paralelo más eficientemente, y la construcción de modelos de gran tamaño, usualmente denominados LLMs (Large Language Models), como GPT, T5, BERT, etc.

La librería Hugging Face Transformers, escrita en Python, constituye hoy en día la referencia para el uso práctico de estos modelos. Proporciona:

- Modelos preentrenados de la mayoría de las arquitecturas conocidas (GPT-2, GPT-Neo, BERT, DistilBERT, T5, RoBERTa, etc.).
- Interfaces sencillas para el ajuste fino (fine-tuning) en tareas concretas (clasificación de texto, QA, summarization...).
- Un ecosistema de “pipelines” que permiten realizar inferencias (traducción, generación de texto, etc.) con unas pocas líneas de código.

En este apartado, explicaremos los fundamentos técnicos de la arquitectura Transformer y mostraremos cómo integrarla en un pipeline de Hugging Face, completando ejemplos de código que servirán como base para proyectos más avanzados.



![image](assets/cm9bny8qr005t356xc1xly8cs-INSD_BAIN_U6_Imagen1.jpg)



### 2.2 Fundamentos de la arquitectura Transformer



Antes de la aparición de los Transformers, las redes recurrentes (LSTM, GRU) dominaban el campo del NLP, procesando tokens uno a uno en secuencia. Esto conllevaba dificultades para modelar secuencias muy largas, pues la memoria del estado oculto se diluía con el paso de las iteraciones y el entrenamiento no era fácilmente paralelizable. Más tarde, se propusieron técnicas basadas en attention, como las celdas de atención en LSTM.

Un Transformer consta esencialmente de dos grandes partes en su versión original:



- **Codificador (Encoder)**  
  Recibe la secuencia de entrada (por ejemplo, tokens de una frase). Aplica multi-head self-attention, seguido de capas feed-forward y normalizaciones.
- **Decodificador (Decoder)**  
  Permite la generación de la secuencia de salida, también con multi-head self-attention, pero agregando un mecanismo de encoder-decoder attention que se nutre de las representaciones del encoder.



En las implementaciones especializadas en tareas de comprensión (por ejemplo, BERT), se omite la parte del decodificador y se usa únicamente un stack de codificadores. Por contra, en generadores de texto (GPT-2, GPT-3, GPT-Neo) se apuesta por un stack de decodificadores.

El núcleo del Transformer es el self-attention, que permite a cada posición de la secuencia “atender” (ponderar) otras posiciones relevantes. Cada token se enriquece con información contextual de toda la oración, en una única pasada, sin procesar secuencialmente los tokens. Esto se implementa mediante las llamadas matrices Q, K, V (consulta, clave, valor), calculadas linealmente a partir de las representaciones de cada token:



1.
2.
3.



donde 𝑋 es la matriz de embeddings de la secuencia, y 𝑊𝑄, 𝑊𝐾, 𝑊𝑉 son parámetros de la red. Luego, la atención se computa como:

En el caso de Multi-head attention replica este procedimiento varias veces en paralelo, mezclando los resultados.

Al prescindir de convoluciones o recurrencias, el Transformer no tiene de forma inherente la noción de posición de cada token en la secuencia. Para solventar esto, se introduce un positional encoding (PE) que se suma a los embeddings de los tokens. Existen variantes (seno-coseno fijos, learnable embeddings, etc.), pero la idea es inyectar información posicional para distinguir, p. ej., el primer token del quinto.

Esta codificación posicional permite, junto con la self-attention, que el modelo “sepa” la ubicación relativa de cada palabra en la secuencia.



### 2.3 Representaciones distribuidas y mecanismo de autoatención



Una de las ventajas competitivas de los Transformers es la forma en que combinan las representaciones distribuidas (vectorizaciones de tokens) con el mecanismo de autoatención (self-attention). A continuación, ahondamos en estos aspectos.



- **Embeddings**  
  La mayoría de las implementaciones de Transformers inician con una capa de embeddings que proyecta cada token (identificado por su ID en el vocabulario) a un vector de dimensión 𝑑. Estos embeddings se entrenan junto con el modelo o bien se inicializan con vectores preentrenados. El tamaño de vocabulario puede ser muy grande (algunas implementaciones superan los 50.000 tokens entre subpalabras y caracteres raros).

  Por ejemplo, si utilizamos sub-tokenización (Byte-Pair Encoding, WordPiece, etc.), la palabra “ingeniería” se podría representar con varios sub-tokens, cada uno con su embedding respectivo. La concatenación (más la posición) forma la entrada real al bloque Transformer.
- **Autoatención en detalle**  
  El self-attention no solo refuerza la correlación entre posiciones cercanas, sino que puede, en una sola capa, vincular tokens distantes si la similitud en Q y K es alta. Por ejemplo, en la frase: “El ingeniero revisó el código que había producido anteriormente.”

  El token “ingeniero” podría atender al token “produjo” (o “anteriormente”) si la semántica indica que la acción de producir código se relaciona con el ingeniero. Esto se hace de manera directa, sin tener que recorrer una secuencia en pasos.

  Para aumentar la capacidad representacional, se usan varios “cabezas” (heads) de atención paralelas (multi-head self-attention). Cada cabeza enfoca aspectos diferentes de la relación entre tokens (por ejemplo, concordancia gramatical, referencia anafórica, dependencias sintácticas, etc.). Los resultados de las cabezas se concatenan y proyectan, alimentando luego una red feed-forward (generalmente una MLP con activación ReLU o GELU) y, tras cada bloque, se aplica normalización y residual.



### 2.4 Uso de Hugging Face Transformers: pipelines y modelos preentrenados



Hugging Face nos proporciona su librería Hugging Face Transformers, que se ha convertido en un estándar para utilizar, adaptar y desplegar modelos de lenguaje de la familia Transformer. Nos ofrece un ecosistema completo con modelos preentrenados (BERT, GPT, T5, etc.), utilidades para el ajuste (fine-tuning) y “pipelines” predefinidos que facilitan las tareas como clasificación de texto, generación de contenido o detección de entidades. En este apartado, profundizaremos en cómo instalar y configurar la librería, explicaremos la lógica que subyace a los principales pipelines y mostraremos, de forma entrelazada, ejemplos de código para ilustrar cada paso.



#### Instalación y uso



Para comenzar a trabajar con Hugging Face Transformers, resulta habitual instalar la librería junto a un framework de Deep Learning como PyTorch o TensorFlow. La combinación con PyTorch es especialmente popular entre la comunidad, aunque cualquiera de los dos backends es válido. Un flujo típico de instalación podría ser:

- Instalación con PyTorch
  - **pip install transformers[torch] torch**
- Instalación con TensorFlow/Keras (visto en la asignatura de Inteligencia Artificial)
  - **pip install transformers tensorflow**

Es importante verificar que poseemos la versión adecuada para utilizar la GPU, de lo contrario, el entrenamiento y la inferencia de modelos de cierto tamaño serán lentos o incluso inviables.

Una vez finalizada la instalación, podemos realizar un test rápido importando la librería en un entorno Python. En apenas unas líneas, se pueden cargar modelos preentrenados de la plataforma Hugging Face y efectuar inferencias:



```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
prompt = "Software engineering is"
output = generator(prompt, max_length=40, num_return_sequences=1)
print(output)
# Output
[{'generated_text': 'Software engineering is an art for achieving goals and getting there," said Jeff Brown, president and CEO of The Future Analytics Group. "In terms of metrics, data visualization is not a new way of trying'}]
```



Hugging Face descarga automáticamente el modelo (en este caso gpt2) y permite generar texto completando el prompt. Aunque sea un ejemplo muy elemental, demuestra la practicidad de iniciar un prototipo sin entrenar desde cero.



#### Modelos preentrenados



La librería Transformers centraliza un gran número de modelos preentrenados en el Hugging Face Hub. Podemos encontrar arquitecturas clásicas como BERT o GPT-2, pero también versiones más recientes y potentes, como T5, DistilBERT, RoBERTa, GPT-Neo, Bloom o modelos como Phi de Microsoft, Gemma de Google o LLaMa de Meta, cada cual con características y tamaños diferentes. Es fundamental elegir un modelo preentrenado apropiado para la tarea:

- Si nuestro objetivo es clasificar sentimientos en un texto corto, podríamos utilizar un BERT pequeño, como bert-base-uncased, para agilizar los tiempos de entrenamiento y predecir con un rendimiento adecuado.
- Si necesitamos una tarea generativa (por ejemplo, redactar resúmenes o crear contenido), GPT-2 o GPT-Neo ofrecen funcionalidades de “text-generation” muy útiles.
- Para cuestiones de masked language modeling o relleno de huecos, las variantes del estilo BERT y roBERTa resultan idóneas gracias a su entrenamiento con este objetivo.

El mayor beneficio de trabajar con un modelo preentrenado reside en el ahorro de recursos y tiempo. Muchos de estos modelos se entrenaron en grandes corporaciones o comunidades de investigación, empleando clústeres de GPUs durante días o semanas. Como ingenieros de software, podemos reutilizar dicho conocimiento entrenado y refinarlo (fine-tuning) con un volumen de datos muy inferior.



#### Pipelines



Hugging Face propone el concepto de pipeline como interfaz de alto nivel para realizar tareas de NLP sin tener que manipular manualmente la tokenización o las salidas del modelo. Entre las más comunes, se incluyen text-classification, text-generation, question-answering, ner (Named Entity Recognition), translation y summarization. Cada pipeline gestiona los pasos de preprocesado e inferencia de manera transparente.

En resumen, encontramos los siguientes pipelines:

- Text Generation (pipeline("text-generation")): para generar texto a partir de un prompt.
- Masked Language Modeling (pipeline("fill-mask")): rellena huecos en oraciones (usado con BERT o roBERTa).
- Text Classification (pipeline("text-classification")): incluye análisis de sentimientos u otras clasificaciones.
- Named Entity Recognition (pipeline("ner")): identificar entidades en el texto.
- Question Answering (pipeline("question-answering")): dada una pregunta y un contexto, extrae la respuesta más probable.
- Summarization, Translation y otros.

Con pipelines, evitamos manipular directamente tensores, ya que se encargan de tokenizar y ejecutar el modelo. Para un control más fino y avanzado, se puede instanciar manualmente las clases AutoTokenizer y AutoModel, dándonos una capacidad más potente de ejecutar los modelos cómo queramos.



![image](assets/cm9boi5k700kd356x7reevcp9-INSD_BAIN_U6_Imagen2.jpg)



En la práctica, esta abstracción nos permite centrarnos en la lógica de la aplicación, en lugar de en los detalles de la arquitectura del modelo. Por ejemplo, si se desea traducir de inglés a francés, bastaría con:



```python
from transformers import pipeline
translation = pipeline("translation_en_to_fr")
result = translation("Hello, world!")
print(result)
# Output
[{'translation_text': 'Bonjour, monde!'}]
```



El pipeline translation_en_to_fr descarga un modelo preentrenado en la traducción inglés-francés e internamente tokeniza el texto, ejecuta el decodificador y entrega la frase traducida. Esta versatilidad es uno de los factores clave que ha hecho tan popular a Hugging Face Transformers.



#### Casos de uso



#### Clasificación de texto



```python
from transformers import pipeline

classifier = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

input_text = "Este curso de Ingeniería de Software es fantástico."
prediction = classifier(input_text)
print(prediction)
# Output
[{'label': 'neutral', 'score': 0.7426337003707886}]
```



Como podemos ver, este modelo nos proporciona una clasificación y la confianza de la misma. Existen numerosos modelos, cada uno con propiedades, entrenamientos y objetivos diferentes. Según nuestro caso de uso deberemos acudir a: [https://huggingface.co/models](https://huggingface.co/models) para identificar el ideal.

Para comprender lo que ocurre, ten en cuenta que la pipeline de “text-classification” busca, por defecto, un modelo con cabeza de clasificación ya entrenado en un conjunto de datos de sentimientos. El ejemplo cardiffnlp/twitter-roberta-base-sentiment-latest puede manejar varios idiomas. Al ejecutar este código, la librería:

- Descarga el modelo y el tokenizador si no los tuviéramos en caché.
- Aplica la tokenización a la frase de entrada.
- Pasa la secuencia al modelo, que produce logits para las categorías (positivo, negativo, neutro, etc.).
- Devuelve la etiqueta más probable.

Este proceso integral resulta bastante similar para cualquier pipeline, variando tan solo el tipo de transformaciones en la entrada y la forma de decodificar la salida.



#### Question-answering



```python
from transformers import pipeline

qa_pipe = pipeline("question-answering", model="deepset/roberta-base-squad2")

contexto = """
La arquitectura Transformer se basa en mecanismos de self-attention para modelar la dependencia 
entre tokens de la secuencia. Fue introducida en 2017 por Vaswani et al. en el artículo 
'Attention Is All You Need'.
"""

pregunta = "¿Qué mecanismo emplea la arquitectura Transformer para modelar la dependencia entre tokens?"
resultado = qa_pipe(question=pregunta, context=contexto)

print("Pregunta:", pregunta)
print("Respuesta:", resultado['answer'])
print("Probabilidad:", resultado['score'])
# Output
Pregunta: ¿Qué mecanismo emplea la arquitectura Transformer para modelar la dependencia entre tokens?
Respuesta: self-attention
Probabilidad: 0.7234193682670593
```



El modelo deepset/roberta-base-squad2 está entrenado en la tarea de SQuAD (Stanford Question Answering Dataset). Observamos que la pipeline recibe tanto la pregunta como el contexto y, tras procesar la secuencia concatenada, localiza el fragmento más relevante y lo devuelve. Este esquema es muy práctico en entornos de documentación técnica o repositorios de conocimiento, donde se desea encontrar respuestas a partir de artículos extensos.



#### Fine-tuning



```python
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import Trainer, TrainingArguments

# Supongamos que tenemos un dataset de oraciones y etiquetas
train_texts = ["Me encanta programar", "Odio los bugs", "La documentación es útil"]
train_labels = [1, 0, 1]

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

encodings = tokenizer(train_texts, truncation=True, padding=True)
class SimpleDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    def __len__(self):
        return len(self.labels)
    def __getitem__(self, i):
        item = {k: torch.tensor(v[i]) for k, v in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[i])
        return item

train_dataset = SimpleDataset(encodings, train_labels)
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    logging_steps=1
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset
)

trainer.train()
# Output
TrainOutput(global_step=6, training_loss=0.6376356979211172, metrics={'train_runtime': 9.3475, 'train_samples_per_second': 0.963, 'train_steps_per_second': 0.642, 'total_flos': 36999992160.0, 'train_loss': 0.6376356979211172, 'epoch': 3.0})
```



Durante el entrenamiento con Trainer, habitualmente se imprime información en el log acerca de los steps y el training loss. Cada uno de estos elementos tiene un significado particular:

- **Steps:** representan los pasos de entrenamiento, a menudo medidos como “iteraciones de batch”. Si tenemos un conjunto de datos (dataset) con, por ejemplo, 100 muestras y un batch size de 10, entonces cada epoch constará de 10 “steps”. En entornos con más datos, estos steps pueden contarse por miles o decenas de miles, reflejando cuántas veces se ha realizado un paso de forward pass + backpropagation sobre un batch de ejemplos.
- **Training loss:** es la función de coste que el modelo está tratando de minimizar durante el aprendizaje. Un training loss decreciente indica que el modelo está ajustándose mejor a los datos de entrenamiento (aprendiendo a predecir con mayor exactitud).

Una vez que ha finalizado el entrenamiento, el modelo, junto con sus pesos ajustados, se encuentra en la variable model o bien guardado en la carpeta de output_dir (por defecto, ./results).

Para realizar inferencia sobre un nuevo texto, repetimos la tokenización y hacemos el forward pass con nuestro modelo ya entrenado:

from transformers import BertTokenizer



```python
import torch

class_names={1:"positivo", 0:"negativo"}
# Suponiendo que hemos mantenido la misma tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Texto de prueba
test_text = "La experiencia de usuario fue excelente y muy intuitiva."

# Preprocesado
inputs = tokenizer(test_text, return_tensors="pt", truncation=True, padding=True)

# Pasamos al modelo en modo eval
model.eval()
with torch.no_grad():
    outputs = model(inputs)
    logits = outputs.logits  # Salida antes del softmax

# logits es un tensor con la puntuación para cada clase
predicted_class = torch.argmax(logits, dim=1).item()
print("Predicción:", class_names[predicted_class])
# Output
Predicción: positivo
```



En definitiva, Hugging Face Transformers nos facilita la aplicación de las arquitecturas Transformer sin necesidad de codear manualmente cada detalle de tokenización, forward pass y optimización.

Veamos a continuación todo el potencial que nos puede ofrecer Hugging Face y su comunidad:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651992_1/scormcontent/assets/INSD_BAIN_U6_Video1.mp4?v=1)



### 2.5 Enlaces de interés



> Curso de NLP en Hugging Face
>
> [Link](https://huggingface.co/learn/nlp-course/chapter1/1)

> PyTorch get started
>
> [Link](https://pytorch.org/get-started/locally/)



## 3. Nlp Con Keras, Tensorflow Y Pytorch



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



En este segundo apartado, nos enfocaremos en cómo implementar modelos de Procesamiento de Lenguaje Natural (NLP) utilizando Keras, TensorFlow y PyTorch, centrándonos especialmente en las tareas de búsqueda y análisis de la información que resultan fundamentales para la asignatura. Aunque en la asignatura de Inteligencia Artificial ya se han presentado Keras y TensorFlow, ahora retomaremos esos conocimientos para ajustarlos a un escenario específico: el tratamiento y modelado de textos con redes neuronales de última generación. Asimismo, analizaremos cómo PyTorch ofrece una alternativa sumamente flexible y popular en la comunidad, para quienes prefieren su dinámica de ejecución y la integración nativa con Hugging Face Transformers.

Dentro del ecosistema de Deep Learning en Python, Keras y TensorFlow han sido por mucho tiempo la puerta de entrada de numerosos desarrolladores, especialmente para tareas de clasificación de imágenes y secuencias. Keras facilita la definición de redes de forma modular y declarativa, mientras que TensorFlow provee un backend potente para desplegar el modelo en GPU, TPU o CPU.

Por otro lado, PyTorch ha ganado enorme popularidad gracias a su enfoque imperativo, su facilidad de depuración y la forma en que integra la librería torch.nn. Además, la comunidad open source a menudo prefiere PyTorch al entrenar modelos Transformers, ya que muchas implementaciones y repositorios (incluyendo la librería de Hugging Face) se centran en PyTorch como primera opción.

Este apartado pretende aunar ambos paradigmas (Keras/TensorFlow y PyTorch) para mostrar ejemplos de entrenamiento y predicción con modelos de lenguaje. Antes de sumergirnos en los ejemplos, revisaremos algunos conceptos de preprocesamiento que resultan críticos en NLP y que, aunque vistos en la teoría, merecen atención práctica.



### 3.2 Preprocesamiento y tokenización



A la hora de procesar texto, con frecuencia se necesita:

- **Limpieza de texto:** eliminación de HTML, normalización de tildes, caracteres extraños, etc.
- **División en tokens:** en NLP moderno, se utilizan técnicas como sub-tokenización (Byte-Pair Encoding, WordPiece) o bien tokenizadores especializados (p. ej. BertTokenizer, GPT2Tokenizer) capaces de manejar vocabularios de decenas de miles de subpalabras.
- **Creación de embeddings:** el texto se convierte en vectores que representan su significado. Pueden ser embeddings entrenados desde cero o reutilizados (Word2Vec, GloVe, e incluso embeddings contextuales estilo BERT).

En el caso de un sistema de búsqueda (por ejemplo, un motor semántico interno para grandes documentos de especificación de software), la idea es convertir cada documento en un vector que capture sus rasgos semánticos y, a su vez, indexar dichos vectores. Luego, cuando un usuario introduce una consulta, se la tokeniza del mismo modo y se genera un vector de consulta. Finalmente, se calculan las similitudes (p. ej., coseno) para determinar qué documentos son más afines. Tanto Keras como PyTorch nos permiten entrenar redes que aprendan representaciones optimizadas para esta tarea.

A modo de breve recordatorio, Keras introduce la clase Tokenizer para tokenizar texto, aunque en la práctica, cuando se trabaja con Transformers, es preferible usar la familia de tokenizadores de Hugging Face (AutoTokenizer), pues se integran con los embeddings y la estructura de la arquitectura.



### 3.3 Caso de uso con Keras/TensorFlow



Aunque ya se ha visto el uso de Keras/TensorFlow en la asignatura de Inteligencia Artificial, en este trataremos de ver una aplicación al mundo del NLP.

Vamos a definir un escenario para el que podremos utilizar NLP con Keras/TensorFlow. Supongamos que hemos recopilado un corpus de descripciones de tickets (tareas, incidencias de software) en una organización y deseamos clasificar si se trata de un bug, una feature request o un issue de seguridad. Se tiene un dataset de, por ejemplo, 5000 tickets anotados con estas tres clases. Se quiere entrenar un modelo rápido en Keras para discriminar la clase. A continuación, se explica la razón de cada paso y se ilustra el código.

Keras ofrece la clase TextVectorization para convertir texto bruto en secuencias de tokens (o n-grams). Después, se define una capa Embedding si se parte de embeddings aleatorios, o se cargan embeddings preentrenados (GloVe, Word2Vec...). Por último, se modela la secuencia de embeddings con una arquitectura simple (p. ej., CNN o LSTM) o una capa Dense, en función del caso de uso. Como lo fundamental en este ejemplo es la clasificación básica, definiremos una pequeña red con LSTM para capturar el contexto de la secuencia.



![image](assets/cm9bouudf00y9356xczr5dtlx-INSD_BAIN_U6_Imagen3.jpg)



```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
```



**Ejemplo:** clasificación de tickets (3 clases)



```python
train_texts = [
    "El botón guardar no funciona cuando hay muchos caracteres",
    "Solicito nueva funcionalidad de exportar logs",
    "Hay una brecha de seguridad al exponer el puerto 8080",
    "No se pueden subir archivos adjuntos grandes",
    # ...
]
train_labels = [0, 1, 2, 0]  # 0=BUG, 1=FEATURE, 2=SECURITY, etc.

# 1) Definición de la capa de vectorización
max_tokens = 10000
output_sequence_len = 40  # longitud máxima

vectorizer = layers.TextVectorization(
    max_tokens=max_tokens,
    output_mode='int',
    output_sequence_length=output_sequence_len
)

# Ajustamos la capa con nuestros textos (para obtener vocabulario)
text_dataset = tf.data.Dataset.from_tensor_slices(train_texts).batch(2)
vectorizer.adapt(text_dataset)

# 2) Construimos el modelo con Embedding + LSTM + Dense
embed_dim = 64
model = keras.Sequential([
    vectorizer,  # capa de preprocesado
    layers.Embedding(input_dim=max_tokens, output_dim=embed_dim, mask_zero=True),
    layers.LSTM(64),
    layers.Dense(3, activation='softmax')  # 3 clases
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 3) Ajustamos con datos
train_labels_tensor = tf.constant(train_labels, dtype=tf.int32)

model.fit(
    x=tf.constant(train_texts),
    y=train_labels_tensor,
    batch_size=2,
    epochs=15
)
```



Después de entrenar, podemos evaluar un ticket nuevo. Keras hace el vectorizado automático, gracias a que la capa vectorizer se encuentra en el pipeline:



```ini
test_text = "Se detecta un fallo al subir logs, posible bug en la librería"
test_tensor = tf.constant([test_text])
prediction = model.predict(test_tensor)
class_idx = prediction.argmax(axis=1)[0]
print("Clase predicha:", class_idx)
# Output
Clase predicha: 0
```



Siendo la clase 0 un bug, podemos observar como el modelo predice correctamente. Pero ¿qué pasaría si modificamos el número de epochs para entrenar? Veamos en el siguiente video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651992_1/scormcontent/assets/INSD_BAIN_U6_Video2.mp4?v=1)



### 3.4 Caso de uso con PyTorch



PyTorch se suele preferir cuando se requiere mayor flexibilidad imperativa, y es la base de muchas implementaciones de Transformers (como Hugging Face). Siguiendo un caso de uso análogo, supongamos que tenemos un corpus de comentarios en repositorios de Git de la empresa y queremos clasificarlos en “relacionado con la seguridad” (1) vs. “no relacionado con la seguridad” (0). Al final, se integrará a un motor de análisis que prioriza los issues de seguridad.

A diferencia de Keras, PyTorch no trae un “TextVectorization” integrado, por lo que solemos o bien usar la tokenización de Hugging Face o definimos un tokenizador básico manual. Aquí, por brevedad, usaremos un tokenizador “dummy” que separa por espacios. En la práctica, es recomendable utilizar un tokenizador robusto (p. ej., Byte-Pair Encoding).



```python
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader

# 1) Supongamos un dataset
train_texts = [
    "Este repositorio sufre vulnerabilidad al exponer credenciales",
    "El nuevo pipeline automatiza la creación de tags",
    "Podríamos añadir logging con más detalle",
    "Existen buffer overflows si no validamos entradas"
]
train_labels = [1, 0, 0, 1]  # 1=SEC, 0=NOSEC

# 2) Tokenizador sencillo
def simple_tokenizer(sentence):
    tokens = sentence.lower().split()
    return tokens

# Vocab
all_tokens = set()
for txt in train_texts:
    all_tokens.update(simple_tokenizer(txt))
vocab = list(all_tokens)
word2idx = {w: i+1 for i, w in enumerate(vocab)}  # id=0 -> pad

max_len = 8

def encode(sentence):
    tokens = simple_tokenizer(sentence)
    idxs = [word2idx.get(t, 0) for t in tokens[:max_len]]
    # pad
    while len(idxs) < max_len:
        idxs.append(0)
    return idxs

# 3) Dataset
class CommentDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels
    def __len__(self):
        return len(self.labels)
    def __getitem__(self, idx):
        X = encode(self.texts[idx])
        y = self.labels[idx]
        return torch.tensor(X), torch.tensor(y)

train_ds = CommentDataset(train_texts, train_labels)
train_dl = DataLoader(train_ds, batch_size=2, shuffle=True)

# 4) Definimos un modelo (Embedding + LSTM + Dense)
class SimpleNet(nn.Module):
    def __init__(self, vocab_size, embed_dim=64, hidden_dim=32):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size+1, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 1)
    
    def forward(self, x):
        # x: (batch, seq_len)
        emb = self.embedding(x)  # (batch, seq_len, embed_dim)
        out, (h, c) = self.lstm(emb)  # out: (batch, seq_len, hidden_dim), h: (1, batch, hidden_dim)
        # Tomamos h[-1]
        last_hidden = h[-1]  # (batch, hidden_dim)
        logits = self.fc(last_hidden)  # (batch, 1)
        return logits

model = SimpleNet(len(vocab))
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# 5) Entrenamiento
model.train()
for epoch in range(3):
    for X_batch, y_batch in train_dl:
        optimizer.zero_grad()
        logits = model(X_batch)
        y_batch = y_batch.float().unsqueeze(1)  # (batch,1)
        loss = criterion(logits, y_batch)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, loss={loss.item():.4f}")
```



Después de entrenar, podemos evaluar si se trata de algo relacionado con seguridad o no de la siguiente manera:



```python
model.eval()
new_comment = "El endpoint no encripta la información en tránsito"
with torch.no_grad():
    X_test = torch.tensor(encode(new_comment)).unsqueeze(0)  # shape (1, seq_len)
    logits_test = model(X_test)
    prob = torch.sigmoid(logits_test)
    label_pred = (prob >= 0.5).int().item()
    print("Predicción (0=NOSEC,1=SEC):", label_pred)
# Output
Predicción (0=NOSEC,1=SEC): 1
```



El pipeline es más manual que con Keras, pues definimos la tokenización y el DataLoader. A cambio, obtenemos flexibilidad para modificar cómo se computan secuencias, ajustamos la red con LSTM, introducimos atajos, etc. Además, resulta compatible con otras librerías (por ej., huggingface/transformers), en caso de que quisiéramos utilizar un tokenizador BERT con PyTorch en lugar de uno básico.



### 3.5 ¿Cuál elegir?



Tanto Keras/TensorFlow como PyTorch ofrecen bases sólidas para entrenar y desplegar modelos NLP en escenarios de búsqueda y análisis de la información

Tanto Keras/TensorFlow como PyTorch ofrecen bases sólidas para entrenar y desplegar modelos NLP en escenarios de búsqueda y análisis de la información. A lo largo de los ejemplos, hemos resaltado algunas particularidades:

• Preprocesamiento: la tokenización y normalización del texto es esencial, más aún si se trabaja con datos corporativos donde la calidad del texto no siempre es alta.

- **Elección del framework:** Keras/TensorFlow sigue un paradigma más declarativo, mientras que PyTorch brinda un enfoque más imperativo y flexible. Ambos son válidos; la elección depende de la preferencia del equipo y la compatibilidad con librerías de Transformers.
- **Uso de embeddings:** Para la búsqueda semántica, puede ser muy provechoso entrenar o reutilizar embeddings que reflejen la similitud semántica de documentos (ej.: BERT embeddings) y luego indexarlos con un motor vectorial.
- **Recursos de hardware:** Para proyectos pequeños (pocos datos, un LSTM ligero), el entrenamiento en CPU puede ser aceptable. Sin embargo, en tareas con grandes corpora o modelos voluminosos, la GPU se vuelve prácticamente indispensable.

Como ingenieros, comprender las bondades y limitaciones de cada librería, así como la arquitectura subyacente a las redes secuenciales o Transformers, nos proporciona una ventaja competitiva a la hora de diseñar servicios de clasificación, extracción de información y recuperación semántica de documentos. En conjunción con la librería Hugging Face Transformers (expuesta en el apartado anterior), tenemos a nuestro alcance un ecosistema que abarca desde la producción de embeddings y clasificaciones hasta la generación de texto y la extracción de respuestas en documentos.



## 4. Consideraciones De Rendimiento En Llms: Cpu Vs Gpu Y Aceleradores



### 4.1 Introducción



![image](assets/cm9bq2uua0011356xicxgokiq-stock-image.jpg)



En este tercer apartado, abordamos un aspecto decisivo cuando se trabaja con Large Language Models (LLMs): el rendimiento. Con la creciente magnitud de los modelos (que pueden llegar a requerir decenas o incluso centenares de gigabytes de parámetros), la elección del hardware y el esquema de ejecución se vuelve fundamental para garantizar tiempos de entrenamiento e inferencia razonables. Además, en contextos de búsqueda y análisis de la información, donde se pueden procesar miles de consultas simultáneas sobre grandes corpus, es imprescindible optimizar la infraestructura para sostener la carga.

A lo largo de este apartado, analizaremos:

- Diferencias entre CPU, GPU y aceleradores (TPUs, etc.) para el entrenamiento y la inferencia.
- Estrategias de paralelismo en LLMs (Data Parallel, Model Parallel, Pipeline Parallel).
- Herramientas y recomendaciones prácticas para optimizar el uso de redes, memoria y energía.

El objetivo es brindar una guía técnica que nos oriente en la decisión de compra o alquiler de recursos de cómputo, así como en la configuración de su pipeline de entrenamiento y despliegue.



### 4.2 CPU vs. GPU: ¿por qué preferir la GPU en LLMs?



Tradicionalmente, las CPUs se caracterizan por un bajo grado de paralelismo (pocos cores, cada uno muy potente), mientras que las GPUs exhiben un altísimo paralelismo (cientos o miles de núcleos más simples) con acceso a memorias de alta velocidad. Un LLM típico (por ejemplo, un GPT con cientos de millones de parámetros) requiere multiplicar grandes matrices y tensores en cada paso de entrenamiento e inferencia. Esto es altamente paralelizable, pues cada dimensión de la matriz se puede repartir entre núcleos. En CPU, estos cálculos se vuelven secuenciales en comparación, frenando drásticamente la velocidad.

- Entrenamiento en CPU puede ser hasta decenas de veces más lento que en GPU cuando hablamos de redes profundas con millones de parámetros.
- Inferencia en CPU puede volverse viable solo para pequeños lotes o modelos ligeros, pero para servir peticiones en tiempo real (por ejemplo, en un asistente conversacional), se beneficia enormemente de la GPU, especialmente si se maneja batching de múltiples consultas.

Es importante recalcar que en tareas mínimas (muy pocos datos, redes muy pequeñas) o procesos intensivos en lógica no vectorizable (por ejemplo, parsing complejo), la CPU puede resultar suficiente. Sin embargo, para LLMs (BERT, GPT, T5...), la GPU se convierte en la opción dominante.



![image](assets/cm9bq4wby0035356xjhklf8zz-INSD_BAIN_U6_Imagen4.jpg)



En el siguiente video veremos una explicación más detallada de por qué las GPUs son mejores:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651992_1/scormcontent/assets/video3.mp4?v=1)



### 4.3 TPUs y otros aceleradores



Además de la GPU, existen otros aceleradores especializados:



- **TPUs (Tensor Processing Units)**  
  Desarrollados por Google y accesibles en Google Cloud, están optimizados para multiplicaciones de matrices a gran escala, siguiendo una filosofía similar a la de las GPU, pero con características específicas de TensorFlow.
- **Habana Gaudi**  
  Aceleradores de Intel/Habana Labs, integrados en algunos proveedores en la nube.
- **Cerebras**  
  Sistemas con chips de tamaño wafer para entrenamiento de grandes modelos en una única pieza de silicio.



Para un proyecto estándar de ingeniería de software, las GPU son normalmente la elección universal, pues la oferta es amplia (NVIDIA, AMD), la compatibilidad con librerías como PyTorch y TensorFlow es excelente y la capacidad de alquilar máquinas GPU en la nube es mucho mayor. Las TPUs pueden resultar competitivas en cargas masivas de TensorFlow (por ejemplo, entrenar un T5 gigantesco), aunque requieren una adaptación del código a la API de XLA y, con frecuencia, un entorno de Google Cloud.

En un caso de uso de búsqueda semántica, por ejemplo, puede ser necesario:

- Indexar millones de documentos extrayendo embeddings.
- Requerir batch inference con un gran modelo.
- Buscar la mayor eficiencia de cómputo y menor coste.

Los aceleradores como GPU o TPU pueden recortar el tiempo de indexación de semanas a días (o de días a horas). No obstante, si el volumen de indexación es moderado o se actualiza infrecuentemente, una GPU puntual podría ser suficiente y más rentable que entornos complejos con TPUs.



![image](assets/cm9bqa5zx007j356xxv4by1m0-INSD_BAIN_U6_Imagen5.jpg)



### 4.4 Paralelismo y optimización



Para LLMs de gran tamaño (pensemos en 1B parámetros o más), a menudo no basta una sola GPU de 16-24 GB de VRAM. Existen diversas estrategias para distribuir la carga entre varias GPUs:

| Data Parallel | Model Parallel | Pipeline Parallel |
| --- | --- | --- |
| Se replican los parámetros del modelo en cada GPU, dividiendo el batch entre las GPUs. Cada GPU procesa una parte de los datos y envía gradientes a un nodo que agrega y actualiza los parámetros. Es sencillo de implementar (p. ej., torch.nn.DataParallel o DistributedDataParallel), pero no resuelve problemas de falta de memoria si el modelo es muy grande, pues cada GPU guarda todos los parámetros. | Se “parte” el modelo en varios fragmentos (distintas capas o distintos ejes de tensores) y cada GPU aloja un subconjunto de los parámetros. Esto permite que cada GPU maneje un trozo del modelo si este es tan grande que no cabe en una sola. Exige más cuidado en la orquestación de las capas y la comunicación entre GPUs. | Se dividen las capas del modelo en etapas (pipeline), y cada GPU maneja un “bloque” de capas, pasando la salida de su bloque a la siguiente GPU. Se puede combinar con Data Parallel en una configuración híbrida (llamada 2D o 3D parallelism) para escalar tanto en datos como en parámetros. |



![image](assets/cm9bqcw01008x356xd17ynmz6-INSD_BAIN_U6_Imagen6.png)



En muchos proyectos, Data Parallel es la primera opción para escalar el entrenamiento, siempre que el modelo quepa en la VRAM de una única GPU. Con LLMs extremadamente grandes, se requieren estrategias mixtas (Pipeline + Model parallel). Librerías como DeepSpeed de Microsoft, Megatron-LM de NVIDIA o la API de torch.distributed facilitan estas configuraciones.

El entrenamiento de LLMs puede requerir grandes inversiones de tiempo y dinero. Algunas técnicas de optimización importantes incluyen:

- **Mixed Precision Training (fp16 o bf16):** al trabajar en media precisión (16 bits), se reduce a la mitad (o más) la memoria y el ancho de banda necesario, acelerando la computación. PyTorch (torch.cuda.amp) y TensorFlow (tf.keras.mixed_precision) ofrecen métodos para habilitarlo.
- **Gradient Checkpointing:** en vez de almacenar todas las activaciones en cada forward pass, se vuelven a computar algunas para reducir el uso de memoria. A costa de un overhead computacional, se ahorra VRAM.
- **Cuantización post-entrenamiento:** para la inferencia, se puede cuantizar el modelo (por ejemplo, int8) para reducir el tamaño de los pesos y la latencia, a costa de un deterioro leve en precisión.
- **ZeRO (Zero Redundancy Optimizer):** de la librería DeepSpeed de Microsoft. Permite dividir parámetros, gradientes y estados de optimizador entre las GPUs para reducir la memoria duplicada.

En proyectos de ingeniería de software orientados a la búsqueda de información, puede que no sea necesario re-entrenar por completo un LLM gigante. Con un simple fine-tuning, o usando modelos distilados (DistilBERT, DistilGPT2), se pueden reducir significativamente los requerimientos de cómputo.

La elección entre CPU, GPU o aceleradores especializados para LLMs no solo depende de la dimensión del modelo y el volumen de datos, sino también de los requerimientos de latencia (en inferencia) y presupuesto. Para la mayoría de las tareas reales (en particular, en Búsqueda y Análisis de la Información con grandes corpora y LLMs potentes), la GPU prevalece como la solución principal, con la posibilidad de escalar a múltiples GPU cuando se necesitan mayores prestaciones. En casos más extremos, entran en juego las TPUs u otras plataformas.



## 5. Implementación De Llms Con Tensorflow Y Pytorch



### 5.1 Introducción



En los apartados anteriores, hemos analizado la arquitectura Transformer, el uso de Hugging Face para el fine-tuning de modelos, las librerías Keras/TensorFlow y PyTorch para casos de NLP, así como las consideraciones de rendimiento que surgen al entrenar modelos de lenguaje de gran tamaño (LLMs). Ahora, en este cuarto apartado, consolidamos todo ese conocimiento y presentamos ejemplos más avanzados de implementación de LLMs tanto en TensorFlow como en PyTorch, haciendo énfasis en:

- Configuraciones de entrenamiento (monolítica o distribuida) de un LLM (p. ej. BERT o GPT-2).
- Técnicas de ajuste fino (fine-tuning) y validación.
- Aspectos de producción, como serialización del modelo y punto de partida para la integración en pipelines de CI/CD.



### 5.2 Pipeline de entrenamiento



Cuando se implementa un LLM (p. ej. GPT, T5, BERT) en un escenario real, el pipeline de entrenamiento/prototipo suele constar de los siguientes pasos:

- Descarga o definición del modelo base (por ejemplo, bert-base-uncased, gpt2, t5-small).
- Tokenización y configuración de hiperparámetros (longitud máxima, batch size, etc.).
- Creación del Dataset (local, un DataLoader si es PyTorch, o un [tf.data](http://tf.data).Dataset si es TensorFlow).
- Elección de la estrategia de entrenamiento: monogPU, multiGPU, CPU, etc.
- Bucle de entrenamiento: Fine-tuning en la tarea concreta (clasificación, QA, etc.) con backprop y logging de métricas.
- Evaluación: Métricas de validación, test.
- Exportación del modelo y/o publicación en un repositorio (Hugging Face Model Hub, etc.).

En la práctica, para proyectos con Hugging Face Transformers, se suele usar la API del Trainer (PyTorch) o TFTrainer (TensorFlow). Sin embargo, en algunos entornos se requiere mayor control, generando un bucle de entrenamiento custom. A continuación, demostraremos ambas aproximaciones.



![image](assets/cm9bqij6m00cs356xvol4eggl-INSD_BAIN_U6_Imagen7.jpg)



### 5.3 Implementación de un LLM con TensorFlow



TensorFlow es común en entornos corporativos que utilicen Google Cloud y TPUs. Además, su ecosistema de despliegue (TF Serving, TF Lite) ofrece ventajas en aplicaciones móviles o web. Aunque Hugging Face se centra un poco más en PyTorch, existe soporte para TF que resulta adecuado para muchos casos.

Veamos a continuación un ejemplo de cómo entrenar un modelo dado un dataset.

Supongamos que tenemos una serie de documentos (páginas de manuales, informes técnicos, tickets detallados con información amplia, etc.) y deseamos clasificarlos en tres categorías: (0) BUG, (1) FEATURE, (2) SECURITY. De esta forma, cada vez que llega un nuevo documento (p. ej., texto extenso describiendo un problema o una petición), el sistema lo categoriza para la asignación al equipo correspondiente.

Generamos un archivo CSV que contenga dos columnas: text (cuerpo del documento) y label (0/1/2). Por ejemplo, train.csv:



```csv
text,label
"Este documento describe errores de acceso a la base de datos y salta un bug al hacer JOINs en tablas grandes",0
"Propuesta para implementar cifrado SSL en todos los endpoints",2
"El manual sugiere añadir una nueva plantilla de informes semanales",1
"Se reporta un bug al no poder registrar usuarios en horario nocturno",0
"El archivo describe la falta de cifrado en la transferencia de credenciales",2
"Informe de mejora en la interfaz para seleccionar múltiples proyectos",1
"Explica un fallo crítico al sobrescribir ficheros, bug que corrompe datos",0
"Se recomienda un módulo de seguridad anti inyección SQL",2
"Documento con una guía para expandir la funcionalidad de backups",1
"Error de desbordamiento de buffer al procesar archivos XML grandes",0
"Falla la generación de PDF cuando contiene caracteres especiales",0
"Propuesta de integración con servicios en la nube para almacenamiento",1
"Reporte de contraseñas almacenadas en texto plano en la base de datos",2
"La API devuelve error 401 incluso con credenciales válidas",0
"Sugerencia para añadir registro de actividad del usuario en tiempo real",1
"Vulnerabilidad en la validación de certificados SSL expira",2
"Bug en la conversión de zonas horarias afecta reportes diarios",0
```



Similarmente, definimos un eval.csv con unas pocas entradas para validación:



```csv
text,label
"La ejecución se interrumpe al guardar el log en un path largo, un bug en la API",0
"Se aconseja un parche que resuelva la falta de firewall interno",2
"El documento propone una función para listar dependencias del software",1
"Se reporta un bug al no poder registrar usuarios en horario nocturno",0
"El archivo describe la falta de cifrado en la transferencia de credenciales",2
"Se sugiere una mejora en la interfaz para seleccionar múltiples proyectos",1
"Explica un fallo crítico al sobrescribir ficheros, bug que corrompe datos",0
"La validación de campos numéricos falla con decimales, error en el formulario",0
"Propuesta para agregar soporte de autenticación biométrica en móviles",1
"Reporte de vulnerabilidad en la exposición de metadatos de documentos",2
"El sistema arroja error 500 al subir imágenes en formato WebP",0
"Recomendación de implementar verificación en dos pasos para todos los usuarios",2
"Solicitud de función para exportar estadísticas en formato CSV",1
```



A continuación, utilizaremos Transformers y el modelo bert-base-uncased como base, pero antes de ello nos debemos asegurar de tener instaladas todas las dependencias: pip install tensorflow keras transformers datasets

Simplemente tendremos que ejecutar este fragmento de código para tener nuestro modelo de clasificación entrenado.



```python
import tensorflow as tf
from transformers import (
    TFBertForSequenceClassification,
    BertTokenizerFast,
    DataCollatorWithPadding
)
import pandas as pd
from datasets import Dataset

# 1) Cargamos el modelo y el tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizerFast.from_pretrained(model_name)
model = TFBertForSequenceClassification.from_pretrained(model_name, num_labels=3)

# 2) Cargamos los archivos para entrenar
train_df = pd.read_csv("train.csv")
eval_df = pd.read_csv("eval.csv")

# 3) Creamos una función de ayuda para tokenizar
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding=False)

# Convertimos a un dataset de Hugging Face
train_dataset = Dataset.from_pandas(train_df)
eval_dataset = Dataset.from_pandas(eval_df)

# Tokenizamos los datasets
train_dataset = train_dataset.map(tokenize_function, batched=True)
eval_dataset = eval_dataset.map(tokenize_function, batched=True)

# Eliminamos las columnas con el texto
train_dataset = train_dataset.remove_columns(["text"])
eval_dataset = eval_dataset.remove_columns(["text"])

# 4) Data Collator (para padding dinámico en batch)
data_collator = DataCollatorWithPadding(tokenizer=tokenizer, return_tensors="tf")

# Creamos datasets de TensorFlow
tf_train_dataset = train_dataset.to_tf_dataset(
    columns=["input_ids", "attention_mask", "label"],
    shuffle=True,
    batch_size=2,
    collate_fn=data_collator
)

tf_eval_dataset = eval_dataset.to_tf_dataset(
    columns=["input_ids", "attention_mask", "label"],
    shuffle=False,
    batch_size=2,
    collate_fn=data_collator
)

# 5) Compilamos y entrenamos con keras
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=3e-5),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"]
)

model.fit(
    tf_train_dataset,
    validation_data=tf_eval_dataset,
    epochs=10
)

# Guardamos el modelo
model.save_pretrained("bert_doc_classifier")
```



Terminada la fase de entrenamiento, se puede recargar el modelo y usarlo para evaluar nuestro texto. Ejecutando el siguiente código podremos conocer la clasificación para un listado de documentos:



```ini
class_names={0: "bug", 1: "feature", 2: "security"}

model_saved = TFBertForSequenceClassification.from_pretrained("bert_ticket_classifier")
test_doc = "La aplicación falla si el archivo no es el formato correcto"
encoded_test = tokenizer(test_doc, return_tensors="tf", truncation=True)
result = model_saved(encoded_test)
logits = result.logits
pred_label = tf.argmax(logits, axis=1).numpy()[0]
print("Predicción de clase:", class_names[pred_label])
```



De esta manera, podemos utilizar un LLM previamente entrenado y hacer un fine tuning para nuestro caso de uso, por ejemplo, analizar sentimiento de textos de redes sociales. Así, obtendríamos una solución más robusta y completa que el simple uso de NLTK y spaCy.



### 5.4 Implementación de un LLM con PyTorch



Mientras la sección anterior vimos un fine-tuning con TensorFlow, PyTorch es a menudo la vía elegida en muchos proyectos open source por su enfoque imperativo y la disponibilidad de ejemplos en la comunidad. En este ejemplo, mostramos un escenario donde se desea entrenar un modelo generador para autocompletar descripciones de problemas de software, algo muy útil para la búsqueda o la asistente que sugiere contextos.

Para este caso utilizaremos un modelo GPT-2 para generar posibles descripciones de incidencias de software.

Del mismo modo que antes, generamos un dataset que contenga ejemplos de frases como las que queremos generar:



```xml
text
“The system stops when processing 5000 records in batch.”
“Export functionality becomes unresponsive after 5 minutes of inactivity.”
“Password is transmitted in clear, breaching confidentiality”
“Security patch does not fix SQL injection”
“Resources are not released and causes memory leak”
“We could add weekly performance reports with details”
“Interface lacks dark mode and affects UX”
“API does not validate maximum load size and causes buffer overflow”
“SSL configuration is not present, exposing data”
“Authentication fails when changing time zone”
“Log service does not catch exceptions of type NullPointer”
“Database connection timeout is set to 10 seconds”
“Cache is not updated after backend modifications”
“Input sanitization is missing in the contact form”
“The webhook returns code 500 with payloads larger than 1MB”
“Schema migrations are not atomic in distributed environments”
“Dashboard does not show real-time metrics after horizontal scaling”
“TLS certificate expires in 3 days with no automatic renewal system”
“Search function does not handle special characters correctly”
“Load balancer ignores instances with latency greater than 2s”
“Error messages are not internationalized for multilingual support”
“Queuing system allows duplicates due to lack of idempotency”
“Mobile version does not persist sessions when switching applications”
“The /api/v1/users endpoint leaks sensitive fields in debug mode.”
“Deployment script does not handle rollback on configuration failures”
```



A continuación, nos debemos asegurar de tener instaladas todas las dependencias: **pip install torch transformers datasets**

Simplemente tendremos que ejecutar este fragmento de código para tener nuestro modelo de clasificación entrenado.



```python
import pandas as pd
from datasets import Dataset
from transformers import GPT2LMHeadModel, GPT2TokenizerFast, Trainer, TrainingArguments, DataCollatorForLanguageModeling

# 1) Cargamos el csv
df = pd.read_csv("software_issues.csv") 

# Creamos un dataset de HuggingFace
raw_ds = Dataset.from_pandas(df)

# 2) Cargamos modelo base y tokenizer
model_name = "gpt2"
tokenizer = GPT2TokenizerFast.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Añadimos un token de padding (GPT2 no tiene por defecto)
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = model.config.eos_token_id

model.resize_token_embeddings(len(tokenizer))

# 3) Tokenización
def tokenize_gpt2(examples):
    return tokenizer(
        examples["text"], 
        max_length=64, 
        truncation=True,
        padding="max_length"
    )

tokenized_ds = raw_ds.map(tokenize_gpt2, batched=True)
tokenized_ds = tokenized_ds.remove_columns(["text"])

# GPT-2 requiere que 'input_ids' = 'labels' para modelado de lenguaje
def group_texts_for_lm(examples):
    examples["labels"] = examples["input_ids"].copy()
    return examples

lm_ds = tokenized_ds.map(group_texts_for_lm, batched=True)
lm_ds.set_format("torch")

# 4) Creamos un split de training y evaluación
train_size = int(0.8 * len(lm_ds))
eval_size = len(lm_ds) - train_size
train_ds = lm_ds.select(range(train_size))
eval_ds = lm_ds.select(range(train_size, train_size + eval_size))

# 5) Creamos el data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False 
)

# 6) Definimos argumentos de training
training_args = TrainingArguments(
    output_dir="./gpt2-finetuned-swissues",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    logging_steps=100,
    save_steps=500,
    save_total_limit=2,
    prediction_loss_only=True,
    report_to="tensorboard",
    evaluation_strategy="steps",
    eval_steps=500,
    load_best_model_at_end=True,
    metric_for_best_model="loss",
    greater_is_better=False,
    fp16=True,
    warmup_steps=500,
    gradient_accumulation_steps=4,
)

# 7) Inicializamos el trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=eval_ds,
    data_collator=data_collator
)

# 8) Entrenamos el modelo
trainer.train()

# 9) Guardamos el modelo
model.save_pretrained("./gpt2-finetuned-swissues-final")
tokenizer.save_pretrained("./gpt2-finetuned-swissues-final")

# 10) Función para generar texto con el modelo que hemos creado
def generate_text(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs.input_ids
    
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

# Inferencia
example_prompt = "It is failing when I try to upload the file"
print(f"Prompt: {example_prompt}")
print(f"Generado: {generate_text(example_prompt)}")
```



De esta manera al ejecutar el código podemos ver cómo nos generará una frase completa a raíz de la que le hemos proporcionado:



```markdown
Prompt: It is failing when I try to upload the file
Generado: It is failing when I try to upload the file and I get the error message. This is not a problem but I have to try. I have to use the same method. The problem is not for the best.
- The first time I try to upload the file, I get the same error message as the first time.
- The first time I try to upload the file and I get the error message.
- The second time I try to upload the file
```



El modelo GPT-2 está entrenado principalmente con datos en inglés, es por ello por lo que las generaciones en idiomas como el español pueden generar textos sin sentido. Para ello deberemos hacer un fine-tuning mucho mayor o recurrir a un modelo ya entrenado en español.

Veamos en el próximo video, cómo sería un caso similar, pero para un modelo que responda a preguntas:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651992_1/scormcontent/assets/video4.mp4?v=1)



La implementación de LLMs con TensorFlow o PyTorch es muy similar: se definen los datasets y su tokenización, se configuran los argumentos de entrenamiento y se aprovechan las clases Trainer / TFTrainer para automatizar el proceso. La decisión depende de la preferencia de la empresa, la disponibilidad de hardware y la familiaridad con uno u otro framework.

Lo importante es:

- Encapsular la lógica de preprocesamiento y tokenización de modo que sea reproducible.
- Monitorear la loss y las métricas, así como la memoria y tiempo de cómputo, sobre todo en LLMs grandes.
- Elegir cuidadosamente la tarea (clasificación, QA, traducción, etc.) y el modelo base (BERT, GPT, T5) en función de nuestras necesidades en Búsqueda y Análisis de la Información.



## 6. Uso De Hugging Face Para Implementación Y Despliegue De Modelos



### 6.1 Introducción



![image](assets/cm9bqvwix00pr356x7tumsxo4-stock-image.jpg)



En todo proyecto que involucre Búsqueda y Análisis de la Información con LLMs, no basta con entrenar o ajustar (fine-tuning) un modelo. Es igualmente importante contar con una estrategia de implementación y despliegue que permita:

1. Versionar y compartir fácilmente los pesos y la configuración del modelo.
2. Integrar con flujos de CI/CD para probar, aprobar y publicar modelos.
3. Servir inferencias de forma estable, escalable y segura, ya sea en local, contenedores o servicios gestionados.

La plataforma de Hugging Face se ha convertido en un referente para estos fines, ofreciendo un Model Hub con miles de repositorios, así como herramientas para la orquestación y el serving. A lo largo de este apartado, describiremos cómo subir modelos a la Hub, cómo descargarlos y validarlos en producción, y cómo se integran en flujos de despliegue continuo. Además, mostraremos cómo levantar localmente un LLM para un uso tipo “chat” sin necesidad de reentrenarlo.



### 6.2 ¿Por qué usar la Hugging Face Model Hub?



La Hugging Face Model Hub aporta ventajas significativas frente a un almacenamiento manual de modelos:

- **Versionado automático de archivos con Git + Git LFS (Large File Storage),** de modo que cualquier cambio en los pesos o en la configuración queda registrado en el historial.
- **Distribución facilitada:** un equipo puede subir el modelo; otros equipos pueden descargarlo con una simple línea de código (from_pretrained), sin enviar manualmente ficheros pesados.
- **Interfaz web:** cada repositorio cuenta con su portada, documentación y ejemplos, lo que agiliza la documentación interna.
- **Visibilidad (si se desea):** permitir que la comunidad (o la organización) reutilice el trabajo. O bien mantenerlo privado para proyectos confidenciales.
- **Integración con la librería transformers:** la API AutoModel.from_pretrained("user/model") automáticamente descarga y cachea el modelo.

Con ello, la Model Hub se convierte en una especie de “GitHub” específico para modelos de IA, agregando valor a la gestión de LLMs en entornos de Búsqueda y Análisis de la Información.



![image](assets/cm9bqyzik00rv356x91qjr78g-INSD_BAIN_U6_Imagen8.jpg)



### 6.3 ¿Cómo subir un modelo a Hugging Face?



Existen dos formas principales de subir un modelo a la Hugging Face Hub:

- **huggingface-cli:** una interfaz de línea de comandos (CLI) que facilita login, creación de repos y pushes.
- **API Python:** funciones como trainer.push_to_hub(), model.push_to_hub(), o huggingface_hub en scripts personalizados.



#### Hugging Face CLI



El proceso que tendremos que seguir para gestionar un modelo utilizando el CLI de Hugging Face será:

1. Crear una cuenta en: [https://huggingface.co/join](https://huggingface.co/join)
2. Obtener y almacenar un token personal: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
3. Para este ejercicio utilizaremos uno de tipo “Write”. No es lo recomendable en producción debido al exceso de permisos.



![image](assets/cm9br2e9g00uh356xianr2icn-INSD_BAIN_U6_Imagen9.jpg)



1. Instalar la librería huggingface_hub: **pip install huggingface_hub**
2. Iniciar sesión ejecutando el siguiente comando en la terminal y proporcionando el token obtenido anteriormente: **huggingface-cli login**

En este punto ya tenemos todo lo necesario para poder crear repositorios y publicar nuestros modelos.

Por ejemplo, para crear un repositorio simplemente debemos ejecutar el siguiente comando en la terminal: huggingface-cli repo create doc-classifier-lstm --type=model



#### API Python



De igual manera que antes, necesitamos tener instalado huggingface-cli y haber iniciado sesión proporcionando un token.

Tras esto, supongamos que hemos entrenado un BERT con la clase Trainer, simplemente tendremos que añadir a nuestro proceso:



```ini
trainer.train()
# Guardamos local
trainer.save_model("my_bert_ticket_classifier")

trainer.push_to_hub("Primera versión de BERT ticket classifier")
```



Veamos un caso de uso real de crear un repositorio y utilizarlo en el siguiente video:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_BAIN_A/content/_651992_1/scormcontent/assets/INSD_BAIN_U6_Video5.mp4?v=1)



### 6.4 Chat local con modelos del Hub



A menudo, se desea probar un modelo de lenguaje grande (LLM) de forma interactiva: escribir una pregunta, una instrucción o un contexto, y recibir una respuesta que actúe como un “chatbot” local. Esto es muy útil para la depuración o experimentación rápida sin necesidad de un entorno remoto.

Para este caso se recomienda tener un equipo con suficiente VRAM de GPU (24GB) y RAM. Como alternativa, podemos usar Google Colab con un entorno de GPU como se muestra en las siguientes imágenes:



![image](assets/cm9br7oko00zk356x3z1ikm5l-carousel1-INSD_BAIN_U6_Imagen10.jpg)

![image](assets/cm9br7oko00zk356x3z1ikm5l-carousel2-INSD_BAIN_U6_Imagen11.jpg)



Tras esto debemos instalar todas las dependencias mediante:

**pip install torch transformers huggingface_hub**

A continuación, iniciamos session usando el token generado anteriormente en Hugging Face mediante:

**huggingface-cli login**

Finalmente, si ejecutamos el siguiente código generaremos un chat utilizando el modelo previamente entrernado:



```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    model_name = "google/gemma-2-2b-it"  # Alternativa: "google/gemma-7b"
    print(f"Descargando tokenizer y modelo preentrenado {model_name}...")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()

    # Si la GPU está disponible, se envía el modelo a CUDA
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    print("Modelo cargado. ¡Listo para chatear!\n")
    print("Escribe 'exit' o 'quit' para salir.\n")

    # Bucle de chat
    while True:
        prompt = input("Tú: ")
        if prompt.strip().lower() in ["exit", "quit"]:
            print("Saliendo del chat...")
            break

        # Se prepara la entrada del usuario
        input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

        # Generamos la respuesta
        with torch.no_grad():
            output_ids = model.generate(
                input_ids,
                max_length=128,
                do_sample=True,
                top_p=0.9,
                temperature=0.7,
                pad_token_id=tokenizer.eos_token_id
            )
        
        # Decodificamos la respuesta
        generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        # A menudo, la salida incluye el prompt original + la respuesta, podemos recortar:
        response = generated_text[len(prompt) : ].strip()
        
        print(f"LLM: {response}\n")

if __name__ == "__main__":
    main()
```



![image](assets/cm9br93s9011j356x6544x99i-INSD_BAIN_U6_Imagen12.jpg)



Esto nos permite combinar el uso de modelos pre entrenados y entrenados por nosotros para hacer análisis de texto o incluso enriquecer la analítica.



## 7. Conclusiones



### 7.1 Conclusiones de la unidad



Al concluir esta unidad, enfocada en las Aplicaciones de Deep Learning en NLP: LLMs con Python, hemos comprobado cómo la arquitectura Transformer y sus sucesores han transformado por completo la forma de abordar el Procesamiento de Lenguaje Natural (NLP). A lo largo de la unidad, se ha repasado la base teórica necesaria (el mecanismo de autoatención, la organización de codificador-decodificador y las propiedades fundamentales de los embeddings) para después pasar a la práctica con Keras, TensorFlow, PyTorch y la librería Hugging Face Transformers. Este recorrido ha permitido observar la eficiencia de los modelos de gran tamaño (LLMs) a la hora de procesar y analizar texto, así como la posibilidad de ajustarlos (fine-tuning) en tareas específicas de alto valor, por ejemplo, la clasificación de documentos extensos, la autocompletación en aplicaciones de búsqueda o la generación de respuestas contextuales.

En paralelo, se han estudiado los retos de rendimiento que plantean los LLMs y cómo la elección de hardware (CPU, GPU, TPU u otros aceleradores) y esquemas de paralelismo (Data Parallel, Model Parallel o Pipeline Parallel) puede marcar la diferencia en la velocidad y la viabilidad del proyecto. A su vez, se ha destacado la importancia de técnicas de optimización como el entrenamiento en media precisión (fp16, bf16), la cuantización y el gradient checkpointing, que permiten aprovechar de forma más efectiva los recursos de cómputo.

Un aspecto fundamental tratado en este bloque ha sido la integración y el despliegue. Gracias a la Hugging Face Model Hub, se facilita la colaboración y el versionado de modelos, evitando el tedio de manejar manualmente archivos voluminosos y aumentando la trazabilidad de las modificaciones. Además, se han explicado métodos para levantar un LLM en local (a modo de “chat” interactivo)

En definitiva, esta unidad nos deja con la certeza de que los modelos de lenguaje de gran tamaño van a seguir avanzando, requiriendo tanto un sólido conocimiento de sus bases y arquitecturas como la capacidad de desplegarlos y mantenerlos de forma escalable y responsable. Quien profundice en estos conceptos, dominando tanto el entrenamiento como la puesta en producción de LLMs, estará preparado para enfrentar retos reales y crear soluciones más inteligentes y eficientes en el amplio universo de la ingeniería de software.



Nota Final: se anima a los estudiantes a mantenerse actualizados en un ámbito tan dinámico como la IA, participando en foros, probando nuevas versiones de librerías y asumiendo prácticas éticas en el uso y desarrollo de LLMs. Solo así podrán consolidar una ventaja competitiva y aprovechar todas las innovaciones que el Deep Learning en NLP ofrece.
