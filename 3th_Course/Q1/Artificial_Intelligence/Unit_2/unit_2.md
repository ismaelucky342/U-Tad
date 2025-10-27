# Unidad 2

Creado: 23 de octubre de 2025 11:37

![image.png](unit_2/image.png)

# Keras

Se trata de una biblioteca de alto nivel utilizada para construir y entrenar modelos de redes neuronales profundas (recuerda por la unidad 1 que una red se considera profunda cuando tiene más de una capa oculta). Facilita el desarrollo de modelos complejos con múltiples capas, diseñadas para aprender y representar datos en varios niveles de abstracción, a través de una interfaz fácil de usar.

### Origen de la herramienta

Para ubicar historicamente esta herramineta nos remontamos a 2015, gracias a un investigador de google que buscaba facilitar el desarrollo del deep learning. 
El objetivo inicial de Keras fue el de permitir la creación rápida de prototipos de modelos de redes neuronales, con énfasis en la facilidad de uso y en su modularidad.

Ha sido ampliamente adoptada por la comunidad de investigadores y desarrolladores debido a su enfoque intuitivo y a sus capacidades avanzadas, ya que su API está diseñada para ser fácil de entender y usar, permitiendo a los desarrolladores concentrarse en la construcción del modelo sin preocuparse por los detalles de implementación.

Está organizada en módulos independientes que se pueden combinar para construir modelos complejos. Esto incluye módulos para capas neuronales, funciones de activación, optimizadores, y funciones de pérdida.

### Estructura de keras

Esta herraminenta está diseñada para ser modular, flexible y facil de usar, permitiendo construir modelos de deep learning con diferentes tipos de modelos y capas. Ofrecido en dos modelos: 

- Secuencial: El modelo secuencial es una pila lineal de capas, donde cada capa tiene exactamente una entrada y una salida. Este tipo de modelo es adecuado para la mayoría de los casos de uso simples, donde las capas se apilan una tras otra.
- Funcional: El modelo funcional ofrece una mayor flexibilidad y es adecuado para casos de uso más complejos, como modelos con múltiples entradas y salidas, capas compartidas y conexiones residuales.

### Capas en Keras

Keras ofrece una amplia variedad de capas destinadas a la construcción de modelis de deep learning siendo las mas comúnes: 

- **Densas:** Conectan todas las neuronas entre capas.
- **Convolucionales:** Detectan patrones locales en datos (como imágenes).
- **Pooling:** Reducen tamaño y complejidad de los mapas de características.
- **Recurrentes:** Procesan secuencias recordando información previa.
- **Normalización:** Estabilizan y aceleran el entrenamiento.
- **Regularización:** Previenen el sobreajuste del modelo.
- **Activación:** Introducen no linealidad en la red.

# Redes Convolucionales

**Las redes convolucionales (CNN o ConvNet)** se consideran parte de las redes neuronales artificiales avanzadas. ****Son una clase especializada de redes neuronales artificiales, especialmente
adecuadas para analizar datos con una estructura en forma de cuadrícula, como imágenes y vídeos.

Utilizan capas convolucionales para detectar características locales y patrones en los datos, lo que las hace extremadamente efectivas en aplicaciones de visión por ordenador, como la clasificación de imágenes, la segmentación semántica y la detección de objetos. 

Las redes convolucionales (CNN) son esenciales en visión por ordenador, ya que reconocen patrones visuales directamente desde los píxeles con poco preprocesamiento. Sus **capas convolucionales** extraen automáticamente características locales (bordes, texturas, etc.) mediante filtros deslizantes. 

![image.png](unit_2/image%201.png)

Las **capas de pooling**, como *MaxPooling*, reducen la dimensionalidad manteniendo la información más relevante, y las **funciones de activación** (principalmente *ReLU*) introducen no linealidad para modelar relaciones complejas. Finalmente, las **capas completamente conectadas** realizan la **clasificación final**.

### Funcionamineto de una capa convolucional

Cada capa convolucional aplica pequeños **filtros,** que son matrices de pesos, sobre la entrada. Los pesos se aprenden durante el proceso de entrenamiento de la red. Los filtros (también llamados Kernel) se desplazan (o ‘convolucionan’) a lo largo de la imagen, multiplicando los valores del filtro por los valores de la imagen en cada posición y sumando los resultados. 

- El **mapa de características** es el resultado de la convolución de un filtro sobre la imagen. Cada filtro detecta diferentes aspectos de la imagen, por lo que múltiples filtros se aplican en una misma capa para extraer varias características.
- El mapa de características resultante de cada convolución se usa como entrada para las siguientes capas de la red, como otras capas convolucionales, capas de pooling (que reducen aún más la dimensionalidad) y finalmente capas completamente conectadas (fully connected) que son las que toman las decisiones finales (por ejemplo, clasificación, detección de objetos o segmentación).

**Convolucionar** se trata del proceso mediante el que se aplica un filtro (Kernel) a una entrada para generar un mapa de características. Al aplicar la convolución se reduce la dimensionalidad de la imagen original mientras se conserva la información más relevante.

<aside>
💡

*”Permite que las capas posteriores se enfoquen en características más abstractas y complejas, disminuyendo la cantidad de datos que la red necesita procesar”*

</aside>

El **stride** es el paso que da el filtro al moverse por la imagen, si el stride es 1, el filtro avanza un píxel cada vez, si es 2, salta de dos en dos, haciendo la salida más pequeña.

> En una CNN para reconocer dígitos (como MNIST) las primeras capas detectan **bordes**, las capas intermedias combinan esos bordes en**formas más complejas** (curvas, intersecciones) y las últimas capas juntan todo para**identificar el número completo**.
> 

![image.png](unit_2/image%202.png)

## Operaciones con matrices en las CNN

![image.png](unit_2/image%203.png)

### Conversión de la imagen a matriz

Toda imagen, ya sea en escala de grises o a color, se convierte en una **matriz de valores numéricos**. Cada píxel se representa según su intensidad, y en imágenes a color se considera un conjunto de valores para rojo, verde y azul. Esta representación permite que la red neuronal pueda “entender” la imagen y operar matemáticamente sobre ella. 

> Como curiosidad, esta conversión también facilita técnicas de normalización, lo que ayuda al entrenamiento al mantener los valores dentro de un rango manejable.
> 

### Convolución: detectar patrones locales

El **filtro o kernel** es una pequeña matriz que se aplica sobre la imagen para detectar patrones específicos, como bordes, texturas o formas. Al moverse sobre la imagen y combinar sus valores con los de la subregión que cubre, el filtro genera un **mapa de características**, que destaca las áreas donde el patrón buscado aparece con mayor intensidad.

- Por ejemplo, un filtro diseñado para bordes verticales resaltará los cambios bruscos de intensidad de izquierda a derecha.
- En redes reales, los filtros no siempre se diseñan manualmente; la mayoría se **aprenden automáticamente** durante el entrenamiento, ajustándose para reconocer las características más útiles para la tarea.

### Pooling: resumir información

Después de la convolución, el mapa de características puede ser muy grande. Para **reducir su tamaño y mantener lo más importante**, se aplica un proceso llamado **pooling**, siendo el Max Pooling el más común. Este proceso selecciona el valor más representativo dentro de cada subregión del mapa, conservando la información relevante y reduciendo la carga de procesamiento. 

> Este paso también ayuda a que la red sea más **robusta frente a pequeñas variaciones o desplazamientos en la imagen**.
> 

### Flattening: preparación para clasificación

Una vez reducido el mapa de características, se convierte en un **vector unidimensional**, un proceso conocido como flattening. Este vector es lo que se alimenta a las **capas completamente conectadas**, donde cada neurona combina los valores de entrada con **pesos y sesgos** aprendidos.

### Predicción final

La capa de salida de la red aplica una función de activación, como **softmax**, para producir la **predicción final**, por ejemplo, determinar qué dígito aparece en una imagen del conjunto MNIST. Gracias a la combinación de convolución, pooling y capas densas, la red es capaz de **reconocer patrones complejos** que podrían ser muy difíciles de identificar con métodos tradicionales.

### Puntos interesantes

- Las CNN imitan parcialmente la forma en que funciona la **corteza visual** en los humanos, detectando primero características simples y luego combinándolas para reconocer formas más complejas.
- Los filtros iniciales suelen detectar **bordes y texturas**, mientras que las capas más profundas capturan patrones abstractos y contextuales.
- Esta arquitectura ha permitido avances impresionantes en campos como **reconocimiento facial, vehículos autónomos, segmentación médica** y m

## Capas Max Pooling

Con las capas Max Pooling se consiguen extraer ventanas de los mapas de características de entrada y sacar el valor máximo de cada canal. Es conceptualmente similar a la convolución, salvo que en lugar de transformar los parches locales mediante una transformación lineal aprendida (el núcleo convolucional), se transforman mediante una operación de tensor máximo codificada. 

Una gran diferencia con la convolución es que Max Pooling se realiza normalmente con ventanas de 2x2 y stride 2, con el fin de reducir la muestra de los mapas de características en un factor de 2. Por otro lado, la convolución se realiza normalmente con ventanas de 3x3 y sin stride (stride 1).

![image.png](unit_2/image%204.png)

### Introducción

El **algoritmo de retropropagación** es esencial para entrenar redes neuronales, incluyendo las convolucionales (CNN). Su función principal es **ajustar los pesos y sesgos** de la red para que las predicciones sean lo más precisas posibles. En otras palabras, permite que la red “aprenda” de los errores que comete al procesar los datos.

---

### Cómo funciona la retropropagación

1. **Propagación hacia adelante (Forward Pass)**
    - Se introduce una entrada (por ejemplo, la imagen de un dígito manuscrito).
    - Las capas convolucionales aplican filtros para extraer características.
    - Las capas de pooling reducen la dimensionalidad, conservando lo más importante.
    - La información se aplana en un vector y pasa por capas completamente conectadas.
    - La capa de salida aplica una función de activación (por ejemplo, softmax) para generar las **probabilidades de cada clase**.
2. **Cálculo del error**
    - Se compara la salida de la red con la etiqueta verdadera del dato.
    - Se utiliza una **función de pérdida** (como entropía cruzada) para medir la diferencia entre la predicción y la realidad.
        
        > *“La entropía cruzada mide **qué tan diferente es la predicción de la red respecto a la realidad**.”*
        > 
3. **Retropropagación del error (Backward Pass)**
    - El error se propaga hacia atrás desde la capa de salida hacia las capas anteriores.
    - En cada capa se calculan los **gradientes**, que indican cómo debería cambiar cada peso y sesgo para reducir el error.
    - Se aplica la **regla de la cadena** del cálculo diferencial para relacionar el error con cada parámetro de la red.
4. **Actualización de pesos y sesgos**
    - Los gradientes se usan con un **algoritmo de optimización** (como descenso de gradiente estocástico o Adam) para ajustar los pesos y sesgos.
    - El ajuste se realiza en la dirección que **minimiza la función de pérdida**.
5. **Entrenamiento iterativo**
    - Este proceso se repite muchas veces (épocas) y con diferentes subconjuntos de datos (mini-batches).
    - Cada iteración mejora la capacidad de la red para reconocer patrones y realizar predicciones más precisas.

---

### Aplicación en CNN

En el caso de una CNN que reconoce dígitos manuscritos (MNIST):

- Las **capas convolucionales** extraen bordes y formas del dígito.
- El **pooling** reduce el tamaño de los mapas de características manteniendo lo más relevante.
- El **vector aplanado** se pasa a capas densas que combinan los valores para clasificar el dígito.
- La **retropropagación** ajusta los filtros y pesos de todas las capas para que la red aprenda a identificar correctamente cada número.

---

### Puntos interesantes

- La retropropagación permite que la red **aprenda de sus errores**, ajustando millones de parámetros de manera automática.
- Es aplicable a distintos tipos de redes, no solo CNN: recurrentes (RNN), autoencoders, generativas adversariales (GAN), entre otras.
- El proceso combina conceptos de **álgebra lineal, cálculo y optimización**, lo que lo hace extremadamente poderoso pero también elegante desde el punto de vista matemático.

![image.png](unit_2/image%205.png)

---

### Ventajas de las redes convolucionales (CNN)

**Extracción automática de características**

- Detectan patrones locales y globales de los datos sin necesidad de ingeniería manual.
- Esto mejora la eficiencia frente a métodos clásicos como SVM o árboles de decisión.

**Reducción de dimensionalidad y parámetros**

- Técnicas como **pooling** y **compartición de pesos** reducen la cantidad de datos que la red necesita procesar.
- Mantienen la información importante, haciendo la red más eficiente.

**Captura de relaciones espaciales**

- Conservan la estructura espacial de los datos, permitiendo reconocer patrones aunque cambien de posición, orientación o escala.

**Generalización y robustez**

- Aprenden a identificar patrones de forma flexible, lo que mejora su capacidad de funcionar con datos nuevos o ligeramente distintos.

**Aplicaciones versátiles**

- Son muy efectivas en **visión por ordenador** (reconocimiento de imágenes, objetos y escenas).
- También se aplican en **procesamiento de lenguaje natural**, análisis de **series temporales** o **reconocimiento del habla**.

**Flexibilidad y transferencia de aprendizaje**

- Arquitecturas preentrenadas como **VGG-16, ResNet50, Inceptionv3 o EfficientNet** permiten adaptarlas a nuevas tareas con pocos datos.

**Identificación de patrones invariantes**

- Las capas convolucionales detectan características independientemente de cambios en posición, orientación, escala o traslación.

---

## **Transfer Learning**

El **aprendizaje por transferencia** (*Transfer Learning*) es una técnica del **aprendizaje automático** y, especialmente, del **deep learning**, en la que un modelo previamente **preentrenado** en una tarea general se **reutiliza** (total o parcialmente) para una nueva tarea, normalmente con **menos datos** y **menor coste computacional**.

La idea central es **transferir el conocimiento** que el modelo ya ha adquirido (por ejemplo, las representaciones de características aprendidas) a otro problema relacionado.

**¿Porqué?**

Entrenar redes profundas desde cero requiere:

- Grandes volúmenes de datos.
- Mucho tiempo de cómputo.
- Riesgo de sobreajuste en conjuntos pequeños.

El *transfer learning* soluciona esto aprovechando redes entrenadas en grandes datasets como **ImageNet**, **COCO**, o **BERT** (en NLP).

## Regularización de una CNN

La regularización es una técnica utilizada para prevenir el sobreajuste (overfitting), asegurando que el modelo generalice bien en datos no vistos. Keras proporciona varias técnicas de regularización:

- DropOut: Es una técnica en la que se desactivan aleatoriamente un número de unidades de la red durante el entrenamiento. Desconecta un 50% de las neuronas de la capa a la que está conectada en cada paso de entrenamiento. Esto fuerza a la red a no depender demasiado de ciertas neuronas, promoviendo así la generalización.
- Regularización L1 y L2: La regularización L1 agrega una penalización igual al valor absoluto de los coeficientes de los parámetros, mientras que L2 agrega una penalización igual al cuadrado del valor de los coeficientes. Se realiza para prevenir el sobreajuste (overfitting) 
al penalizar grandes valores de los pesos en las capas de red.

## Ajuste de Hiperparámetros de la red

El ajuste de hiperparámetros implica encontrar la combinación óptima de hiperparámetros para mejorar el rendimiento del modelo. Algunos hiperparámetros comunes incluyen la tasa de aprendizaje, el tamaño del lote y el número de épocas.

- Tasa de Aprendizaje: Se puede ajustar la tasa de aprendizaje del optimizador. Keras también proporciona callbacks para ajustar dinámicamente la tasa de aprendizaje durante el entrenamiento.
    
    ```python
    from tensorflow.keras.callbacks import LearningRateScheduler
    
    def scheduler(epoch, lr):
       if epoch < 10:
           return lr
       else:
           return lr * tf.math.exp(-0.1)
    
    callback = LearningRateScheduler(scheduler)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                 loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=20, callbacks=[callback])
    ```
    
- Tamaño del lote y numero de épocas: Se experimentar con diferentes tamaños de lote y distintos números de épocas para encontrar la combinación que mejor funcione para tu modelo y datos.
    
    ```python
    model.fit(x_train, y_train, epochs=50, batch_size=64, validation_split=0.2)
    ```
    

### Aumento de Datos

El aumento de datos (Data Augmentation) es una técnica para generar nuevas muestras de datos de entrenamiento a partir de las existentes mediante transformaciones aleatorias. Esto ayuda a mejorar la generalización del modelo.

```python
rom tensorflow.keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(
 rotation_range=20,
 width_shift_range=0.2,
 height_shift_range=0.2,
 shear_range=0.2,
 zoom_range=0.2,
 horizontal_flip=True,
 fill_mode='nearest')
datagen.fit(x_train)
model.fit(datagen.flow(x_train, y_train, batch_size=32),
 steps_per_epoch=len(x_train) // 32, epochs=50)
```

### **Optimización de modelos de una CNN**

- Early Stopping: Es una técnica para detener el entrenamiento cuando el rendimiento en los datos de validación deja de mejorar.
    
    ```python
    from tensorflow.keras.callbacks import EarlyStopping
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    model.fit(x_train, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stopping])
    ```
    
- Batch Normalization: Normaliza las activaciones de una capa a lo largo del lote, mejorando la estabilidad y velocidad del entrenamiento.
    
    ```python
    from tensorflow.keras.layers import BatchNormalization
    
    model = Sequential([
       Flatten(input_shape=(28, 28)),
       Dense(128, activation='relu'),
       BatchNormalization(),
       Dense(10, activation='softmax')
    ])
    ```
    
- Model Checkpointing: Guardar el modelo en checkpoints durante el entrenamiento permite recuperar el mejor modelo basado en métricas de validación.
    
    ```python
    from tensorflow.keras.callbacks import ModelCheckpoint
    
    checkpoint = ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True)
    model.fit(x_train, y_train, epochs=50, batch_size=32, validation_split=0.2, callbacks=[checkpoint])
    ```