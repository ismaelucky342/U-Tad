# Unidad 1

Definimos las redes neuronales como el componente esencial de la inteligencia artificial moderna, catalogaremos las IAs según su desarrollo actual destacando aplicaciones prácticas del machine learning centrándonos en las aplicaciones como el perceptrón y el perceptrón multicapa. 

- Redes neuronales Artificiales
- Redes neuronales Artificiales Básicas
- Ejemplos prácticos para crear entrenar y ejecutar ANNS.

## Redes Neuronales Artificiales

Para contextualizar, la IA es el conjunto de software creado para imitar la función cognitiva humana, un concepto surgido en los años 40 con un enorme desarrollo actual gracias en parte al surgimiento de conceptos como el big data, que permiten entrenar las redes neuronales a base de gran cantidad de datos y a la velocidad de procesamiento de las máquinas actuales. 

Estos sistemas han evolucionado hasta llegar al machine learning, que es un subconjunto de la IA y al deep learning que a su vez es un subconjunto del machine learning. La evolución de estos sistemas representa un cambio paradigmático en la forma en que las máquinas procesan información y toman decisiones. El machine learning permite a los sistemas aprender de los datos sin ser explícitamente programados para cada tarea específica, mientras que el deep learning utiliza arquitecturas de redes neuronales profundas para extraer características y representaciones de alto nivel de los datos de entrada.

### Clasificación de la Inteligencia Artificial

Todas las **aplicaciones actuales de ML** se encuentran dentro de lo que conocemos como **inteligencia Artificial Estrecha (Narrow AI)**. Las inteligencias artificiales actuales comienzan a imitar las capacidades de razonamiento y pensamiento de los seres humanos. No sólo siguen reglas y mantienen el contexto, sino que también simulan los procesos de pensamiento humano. Esta categoría incluye sistemas especializados que sobresalen en tareas específicas como reconocimiento de imágenes, procesamiento de lenguaje natural, sistemas de recomendación, diagnóstico médico asistido, conducción autónoma y traducción automática.

Actualmente estamos a mitad de camino de lo que sería la **Inteligencia General Artificial (Artificial General Intelligence-AGI)** que de momento es en gran medida teórica. Estos sistemas podrán comprender, aprender, adaptar y aplicar conocimientos a tareas diversas, de forma similar a la de los seres humanos. La AGI representaría un salto cualitativo donde una máquina podría transferir conocimiento entre dominios diferentes, razonar de manera abstracta, comprender contextos complejos y adaptar su aprendizaje a situaciones completamente nuevas sin necesidad de reentrenamiento específico.

Hipotéticamente, la inteligencia artificial general podría convertirse en **Superinteligencia Artificial (Artificial Superintelligence-ASI)**. Este nivel teórico de inteligencia superaría ampliamente las capacidades cognitivas humanas en todos los aspectos, incluyendo creatividad, resolución de problemas, inteligencia social y sabiduría general. La llegada de la inteligencia artificial también trae consigo una serie de **problemas éticos y de seguridad** que incluyen consideraciones sobre privacidad de datos, sesgo algorítmico, desplazamiento laboral, autonomía de armas, y la necesidad de establecer marcos regulatorios robustos que garanticen el desarrollo responsable de estas tecnologías.

### Medición y Evaluación de la Inteligencia Artificial

Para la medición del progreso y destreza de una IA debemos poder definir y evaluar la inteligencia para hacer comparaciones entre sistemas, las propias IA y la inteligencia humana, no siendo realmente suficiente medir únicamente una habilidad completa (debemos medir la inteligencia general). Las **redes neuronales artificiales (ANNs)** imitan el comportamiento del cerebro humano, conocido por su eficiencia en tareas cognitivas complejas y de procesamiento de información. 

Los criterios de evaluación incluyen benchmarks estandarizados, pruebas de generalización, eficiencia computacional, robustez ante datos adversarios y capacidad de aprendizaje continuo. Además, se consideran aspectos como la interpretabilidad de las decisiones, la capacidad de razonamiento causal y la habilidad para trabajar con información incompleta o ambigua.

### Aplicaciones de las redes neuronales artificiales

Las ANN básicas tienen las siguientes aplicaciones principales: 

- Reconocimiento de patrones simples para clasificar datos sencillos como formas básicas o categorías de texto, incluyendo clasificación de dígitos manuscritos, detección de spam en correos electrónicos y categorización de documentos.
- Tareas de predicción básicas, como la predicción de tendencias en datos simples y lineales, aplicables a pronósticos de ventas, estimación de valores inmobiliarios y predicción de consumo energético.
- Sistemas de control automatizados que responden a entradas específicas siguiendo reglas aprendidas.
- Filtrado y procesamiento de señales para eliminar ruido o extraer características relevantes.
- Compresión de datos mediante la identificación de representaciones más compactas de la información.

## Redes Neuronales Artificiales Básicas (ANNs)

Con este punto se potencian los conceptos de perceptrón simple y el multicapa, ampliando su posible integración con el aprendizaje automático y aprendizaje profundo. Se explicará en detalle el algoritmo de retropropagación (backpropagation), siendo esta la técnica de propagación por excelencia, así como la optimización por descenso de gradiente para minimización de la función de pérdida que ajusta los pesos de la red neuronal y mejora su desempeño en clasificación y regresión. 

Comenzando con esta introducción, las redes neuronales artificiales básicas son por definición las arquitecturas más simples y fundamentales de las redes neuronales, siendo su principal característica su relativa simplicidad respecto a sus hermanas mayores y su adecuación para resolver problemas menos complejos. Estas arquitecturas fundamentales sirven como bloques constructivos para entender sistemas más sofisticados y proporcionan una base sólida para el aprendizaje de conceptos avanzados en inteligencia artificial.

### Tipos de Redes neuronales artificiales básicas (ANN)

Existen varios tipos de redes neuronales artificiales. El perceptrón simple es la forma más básica de red neuronal con una sola capa de salida utilizada mayoritariamente para clasificación lineal donde la función de activación decide si activar o no la neurona basándose en una combinación lineal de entradas y pesos. Este modelo, propuesto por Frank Rosenblatt en 1958, fue uno de los primeros intentos de crear máquinas capaces de aprender. El perceptrón simple calcula una suma ponderada de las entradas, añade un sesgo, y aplica una función escalón para producir una salida binaria. Aunque limitado a problemas linealmente separables, el perceptrón simple estableció los fundamentos para desarrollos posteriores en el campo.

El perceptrón multicapa (MLP) es una red con una o más capas ocultas lo que permite modelar relaciones no lineales mucho más complejas, con múltiples capas de neuronas algunas ocultas entre la entrada y la salida. Pueden aprender y modelar relaciones no lineales en los datos mediante la composición de múltiples transformaciones no lineales. Esta arquitectura supera las limitaciones del perceptrón simple al introducir capas intermedias que extraen características progresivamente más abstractas de los datos. Los MLP son redes completamente conectadas donde cada neurona de una capa está conectada con todas las neuronas de la capa siguiente, permitiendo la captura de interacciones complejas entre características.

Además de los perceptrones y de las redes neuronales multicapa, existen otros tipos de redes neuronales artificiales básicas, representando fundamentos y conceptos clave en las redes neuronales artificiales. Son las siguientes:

- **Redes de Kohonen (Mapas Auto-Organizados - SOM)**: Se trata de un tipo de red utilizada para la reducción de dimensionalidad y visualización de datos, su misión es mapear datos de alta dimensión a un espacio de menor dimensión (típicamente bidimensional) preservando la topología original. Estas redes no supervisadas son especialmente útiles para descubrir estructuras en datos complejos, realizar agrupamiento y visualizar relaciones entre variables en espacios de alta dimensión. El algoritmo de aprendizaje competitivo permite que las neuronas se organicen de manera que reflejen la distribución estadística de los datos de entrada.

- **Redes de Hopfield**: Son un tipo de red neuronal recurrente utilizadas para el almacenamiento y recuperación de patrones. Las redes de Hopfield son binarias y se usan principalmente en problemas de optimización y de memoria asociativa. Funcionan como memorias auto-asociativas que pueden recuperar patrones completos a partir de entradas parciales o ruidosas. El modelo energético subyacente permite que la red converja hacia estados estables que representan patrones almacenados, siendo útiles en aplicaciones como reconocimiento de patrones degradados, resolución de problemas combinatorios y modelado de procesos cognitivos.

- **Máquinas de Boltzmann**: Son redes neuronales estocásticas que pueden aprender distribuciones de probabilidad sobre sus conjuntos de entrada. Las Máquinas de Boltzmann Restringidas (RBM) son una versión simplificada y comúnmente utilizada para tareas de reducción de dimensionalidad, filtrado colaborativo y preentrenamiento de redes neuronales profundas. Utilizan un enfoque probabilístico basado en la distribución de Boltzmann de la mecánica estadística, permitiendo modelar dependencias complejas entre variables. Las RBM han sido fundamentales en el desarrollo del deep learning, especialmente en el preentrenamiento no supervisado de redes profundas.

Además de estas redes neuronales artificiales básicas, se pueden considerar otras arquitecturas fundamentales que, aunque no son tan comúnmente clasificadas como 'básicas', han jugado un papel importante en el desarrollo de la teoría y las aplicaciones de las redes neuronales. Se trata de las **Redes de Base Radial (RBF)** y de las **Máquinas de Vector de Soporte con Kernel (SVM con Kernel)**.

Las **Redes de Base Radial (RBF)** son redes neuronales feedforward con una capa oculta que utiliza funciones de base radial como funciones de activación. Son útiles para problemas de clasificación y regresión, especialmente cuando los datos presentan agrupamientos naturales. La arquitectura típica consiste en tres capas: entrada, una capa oculta con neuronas de base radial (usualmente gaussianas), y una capa de salida lineal. Las RBF son particularmente efectivas en aproximación de funciones, interpolación de datos dispersos y control de sistemas dinámicos.

Las **Máquinas de Vector de Soporte con Kernel (SVM con Kernel)** no son redes neuronales en el sentido tradicional, pero pueden ser vistas como una forma de red neuronal que proyecta datos a un espacio de mayor dimensión para encontrar un hiperplano de separación óptimo. Utilizan el "truco del kernel" para trabajar implícitamente en espacios de alta dimensión sin calcular explícitamente las coordenadas en ese espacio, logrando eficiencia computacional. Las SVM son especialmente robustas frente al sobreajuste y efectivas en espacios de alta dimensión, siendo ampliamente utilizadas en clasificación de texto, reconocimiento de imágenes y bioinformática.

## Integración en ML y DL de las ANNs

Las redes neuronales básicas pueden ser utilizadas tanto en machine learning como en deep learning. La principal diferencia radica en la profundidad de la red y la complejidad de los patrones que pueden capturar. Su uso dependerá del contexto, de la complejidad de la tarea y de los recursos computacionales disponibles.

- En **machine learning** se pueden utilizar para tareas relativamente simples o con conjuntos de datos pequeños y menos complejos. Estas redes neuronales pueden tener una o pocas capas ocultas y se utilizan para problemas donde la complejidad de los datos no requiere una arquitectura profunda. El ML abarca técnicas y algoritmos, incluyendo redes neuronales, aunque no se limita a ellas. Otros ejemplos de algoritmos de ML son los árboles de decisión, máquinas de vectores de soporte (SVM), regresión logística, K-means, K-NN (K-vecinos más cercanos), y métodos de ensamble como Random Forest y Gradient Boosting. Estas técnicas suelen requerir ingeniería de características manual, donde expertos del dominio identifican y crean las características relevantes para el modelo.

- El **deep learning** se asocia con redes profundas, siendo su principal característica el uso de redes con muchas capas (a menudo decenas o cientos) para capturar complejidades elevadas y representaciones más abstractas de los datos. Sin embargo, también puede incluir redes neuronales con una o pocas capas en contextos específicos. Se consideran parte del DL en el sentido de que siguen utilizando los principios de aprendizaje profundo, como la retropropagación y el descenso de gradiente, pero con una arquitectura más sencilla. El deep learning destaca por su capacidad de aprendizaje de representaciones, donde las características se extraen automáticamente de los datos sin necesidad de ingeniería manual, permitiendo modelar jerarquías complejas de conceptos.

## **Componentes y funciones de las redes neuronales artificiales (ANNs) básicas**

Las redes neuronales artificiales básicas (ANNs) aprenden y procesan datos a través de una arquitectura en capas que transforma progresivamente la información desde la entrada hasta la salida. Utilizan pesos, sesgos y funciones de activación para modelar y resolver problemas, aprendiendo a capturar relaciones complejas entre entradas y salidas, así como a identificar patrones significativos en los datos. A continuación, se detallan estos componentes y las funciones necesarias para cumplir con su objetivo.

- Las **Neuronas Artificiales** son los elementos básicos de una red neuronal, inspirados en el funcionamiento de las neuronas biológicas. Están organizadas en distintas capas dentro de la red, cada una con un rol específico en el procesamiento de información. Cada neurona artificial recibe múltiples entradas, las procesa mediante una combinación lineal ponderada, añade un sesgo, y aplica una función de activación para producir una salida.

- En la **capa de entrada**, los datos iniciales son recibidos del entorno externo y son pasados a la siguiente capa para su procesamiento sin transformación. El número de neuronas en esta capa corresponde al número de características o variables de entrada del problema. Esta capa no realiza cálculos, sino que simplemente distribuye los valores de entrada a las capas posteriores.

- Cada neurona en las capas siguientes aplica una **función de activación** a las **entradas recibidas** (que pueden ser múltiples) ponderadas por sus respectivos pesos, y produce una **salida** que puede servir como entrada para las capas siguientes. La función de activación introduce no linealidad en el modelo, permitiendo que la red aprenda relaciones complejas más allá de simples transformaciones lineales.

- En las **capas ocultas** es donde ocurre la mayor parte del procesamiento y de transformación de las entradas en representaciones internas más abstractas. Pueden ser una o varias capas intermedias entre la capa de entrada y la capa de salida. Una red se denomina **profunda** si tiene al menos dos capas ocultas, aunque definiciones más modernas consideran profundas a redes con muchas más capas. Estas capas ocultas aprenden a extraer características jerárquicas de los datos, donde las primeras capas detectan patrones simples y las capas más profundas combinan estos patrones en representaciones más complejas y abstractas.

- La **capa de salida** es la última capa de la red que produce el resultado final del modelo, cuya forma depende del tipo de problema. Aquí se obtiene la salida final de la red neuronal después de todas las transformaciones realizadas por las capas anteriores. Cada nodo en esta capa representa una posible **clase** en problemas de clasificación o un **valor continuo** en problemas de regresión. La función de activación en esta capa se elige según el tipo de tarea: softmax para clasificación multiclase, sigmoide para clasificación binaria, o lineal para regresión.

- Los **pesos** en las conexiones entre neuronas determinan la importancia relativa de las entradas y son los parámetros principales que la red ajusta durante el entrenamiento. Cada entrada se multiplica por un peso ajustable, que es crucial para el funcionamiento y la precisión del modelo. El peso ajusta la influencia de la entrada en la neurona, y su valor óptimo es aprendido durante el entrenamiento mediante algoritmos de optimización. Los pesos pueden interpretarse como la "fuerza" de las conexiones sinápticas en analogía con el cerebro biológico.

- Los **sesgos** (bias) son parámetros adicionales que ajustan la función de activación de cada neurona, permitiendo que el modelo aprenda de manera más efectiva al proporcionar flexibilidad adicional. Además de las entradas ponderadas, cada neurona suma un sesgo a la combinación lineal de entradas ponderadas antes de aplicar la función de activación. El sesgo permite que la neurona se active incluso cuando todas sus entradas son cero, ajustando el umbral de activación y mejorando la capacidad del modelo para ajustarse a los datos.

- La **función de activación** introduce no linealidades en el modelo, lo que permite a la red aprender y representar relaciones complejas entre los datos que no podrían capturarse con solo transformaciones lineales. Ejemplos de funciones de activación incluyen:
    - **Sigmoide**: comprime valores al rango (0,1), útil para probabilidades pero sufre de gradientes desvanecientes.
    - **Tanh**: similar a sigmoide pero con rango (-1,1), centrada en cero.
    - **ReLU (Rectified Linear Unit)**: la más común en redes profundas, definida como max(0,x), computacionalmente eficiente y mitiga gradientes desvanecientes.
    - **Leaky ReLU**: variante de ReLU que permite pequeños valores negativos, evitando neuronas "muertas".
    - **Softmax**: utilizada en la capa de salida para clasificación multiclase, produce distribución de probabilidad.
    
Cada una tiene características específicas que las hacen adecuadas para diferentes tipos de problemas y posiciones en la red. En teoría, según el teorema de aproximación universal, una red neuronal con al menos una capa oculta y suficientes neuronas puede aprender cualquier función continua con precisión arbitraria.

## **Algoritmos principales para entrenar las redes neuronales**

El **algoritmo de retropropagación (Backpropagation)** es el método más usado para entrenar redes neuronales y representa uno de los avances más importantes en el campo del aprendizaje automático. Se basa en el **descenso por gradiente**, ajustando los pesos de manera iterativa para minimizar la función de pérdida y mejorar la precisión en tareas como clasificación o regresión. Este algoritmo aplica eficientemente la regla de la cadena del cálculo para calcular gradientes de la función de pérdida respecto a cada parámetro de la red.

El proceso detallado consiste en:

1. **Inicializar pesos y sesgos**: Los parámetros de la red se inicializan aleatoriamente, típicamente con valores pequeños cercanos a cero, usando técnicas como la inicialización de Xavier o He para evitar problemas de convergencia.

2. **Propagación hacia adelante (Forward Propagation)**: Se calculan las salidas de cada capa aplicando secuencialmente las transformaciones lineales (multiplicación por pesos y suma de sesgos) seguidas de funciones de activación. Este proceso continúa hasta la capa de salida, donde se obtiene la predicción final del modelo.

3. **Cálculo de la pérdida**: Se compara la salida predicha con los valores esperados (etiquetas verdaderas) usando una función de pérdida apropiada, como el error cuadrático medio para regresión o la entropía cruzada para clasificación.

4. **Propagación hacia atrás (Backpropagation)**: Se calculan los gradientes del error respecto a cada peso y sesgo utilizando la regla de la cadena, propagando el error desde la capa de salida hacia las capas anteriores. Este proceso determina cuánto contribuye cada parámetro al error total.

5. **Actualización de parámetros**: Se modifican pesos y sesgos siguiendo la dirección que reduce la pérdida, típicamente usando optimizadores como SGD (Stochastic Gradient Descent), Adam, RMSprop o AdaGrad. La tasa de aprendizaje controla el tamaño de los pasos en esta actualización.

6. **Iteración**: Este ciclo se repite durante múltiples épocas (pasadas completas por el conjunto de entrenamiento) hasta que el error sea suficientemente bajo o se alcance otro criterio de parada, permitiendo que la red aprenda progresivamente a realizar mejor su tarea.

Variantes modernas incluyen técnicas como batch normalization para estabilizar el entrenamiento, dropout para prevenir sobreajuste, y learning rate scheduling para ajustar dinámicamente la tasa de aprendizaje.

## **Conceptos matemáticos clave de las ANNs**

En **álgebra lineal**, las entradas, pesos y salidas se representan como vectores y matrices, y las transformaciones lineales se aplican mediante multiplicación de matrices en cada capa. La operación fundamental en una capa de red neuronal puede expresarse como **y = f(Wx + b)**, donde **W** es la matriz de pesos, **x** es el vector de entrada, **b** es el vector de sesgos, y **f** es la función de activación. El álgebra lineal permite operaciones vectorizadas eficientes que son cruciales para el procesamiento en paralelo y la implementación en GPUs.

En **cálculo**, es crucial calcular derivadas parciales y gradientes para entender cómo los cambios infinitesimales en los pesos afectan la salida y el error del modelo. Se utiliza el gradiente descendente y sus variantes para ajustar los pesos de manera que minimicen la función de pérdida. La regla de la cadena del cálculo es fundamental en backpropagation, permitiendo calcular eficientemente derivadas de funciones compuestas que representan el flujo de información a través de múltiples capas. El concepto de derivada direccional indica la dirección de máximo crecimiento de una función, y su negativo apunta hacia la dirección de máximo decrecimiento, que es la base del descenso de gradiente.

Las **funciones de activación** como Sigmoid, Tanh y ReLU introducen no linealidades esenciales que permiten a las ANN aprender representaciones complejas y aproximar funciones no lineales. Sin estas funciones, una red neuronal profunda sería equivalente a una transformación lineal simple, limitando severamente su capacidad expresiva. La elección de la función de activación afecta la velocidad de convergencia, la capacidad de aprendizaje y la robustez del modelo frente a problemas como gradientes desvanecientes o explosivos.

La **optimización** en ANN se basa en la definición de una función de pérdida (o función objetivo) para medir cuantitativamente el rendimiento del modelo, comparando predicciones con valores reales. Se utilizan algoritmos de optimización sofisticados como:
- **SGD (Stochastic Gradient Descent)**: actualiza parámetros usando gradientes de mini-batches.
- **Adam (Adaptive Moment Estimation)**: combina momentum y tasas de aprendizaje adaptativas.
- **RMSprop**: ajusta tasas de aprendizaje por parámetro basándose en magnitudes recientes de gradientes.
- **AdaGrad**: adapta tasas de aprendizaje basándose en la frecuencia de actualizaciones de parámetros.

Estos optimizadores mejoran la convergencia, manejan mejor superficies de pérdida complejas y requieren menos ajuste manual de hiperparámetros.

En **probabilidad y estadística**, las ANN se aplican a tareas de regresión (predicción de valores continuos) y clasificación (predicción de categorías discretas), a menudo modelando distribuciones de probabilidad condicionales. Se utilizan técnicas de regularización como:
- **L1 (Lasso)**: penaliza la suma de valores absolutos de pesos, promoviendo dispersión.
- **L2 (Ridge)**: penaliza la suma de cuadrados de pesos, favoreciendo valores pequeños distribuidos.
- **Dropout**: desactiva aleatoriamente neuronas durante el entrenamiento para prevenir co-adaptación.
- **Early stopping**: detiene el entrenamiento cuando el rendimiento en validación deja de mejorar.

Estas técnicas previenen el sobreajuste, mejorando la generalización del modelo a datos no vistos.

La **teoría de la información** aporta conceptos fundamentales como:
- **Entropía**: mide la incertidumbre o aleatoriedad en una distribución de probabilidad.
- **Entropía cruzada**: cuantifica la diferencia entre dos distribuciones de probabilidad, ampliamente utilizada como función de pérdida en clasificación.
- **Divergencia KL (Kullback-Leibler)**: mide cuán diferente es una distribución de probabilidad de otra de referencia.
- **Información mutua**: cuantifica la dependencia estadística entre variables.

Estos conceptos son esenciales para entender cómo las redes neuronales aprenden representaciones óptimas de los datos y cómo se diseñan funciones de pérdida apropiadas.

## **Niveles de medición de los datos**

Las bases metodológicas de Machine Learning se fundamentan en los **niveles de medición de los datos**, que determinan cómo deben ser procesados, transformados y analizados. Los niveles de medición obligan a elegir ciertos **modelos** y **técnicas** debido a las propiedades matemáticas y estadísticas inherentes de los datos. La escala de medición de Stevens identifica cuatro niveles principales:

- **Datos nominales**: Categorías sin orden intrínseco (ej: colores, géneros, tipos de producto). Solo permiten operaciones de igualdad/desigualdad. Requieren codificación como one-hot encoding para uso en redes neuronales.

- **Datos ordinales**: Categorías con orden pero sin distancia medible (ej: satisfacción baja/media/alta, niveles educativos). Permiten operaciones de orden pero no aritméticas significativas. Pueden codificarse ordinalmente o como one-hot según el contexto.

- **Datos de intervalo**: Valores numéricos con distancias medibles pero sin cero absoluto (ej: temperatura en Celsius, años calendario). Permiten suma y resta, pero no ratios significativos.

- **Datos de razón**: Valores numéricos con cero absoluto significativo (ej: altura, peso, ingresos). Permiten todas las operaciones aritméticas incluyendo multiplicación y división.

Los **datos nominales y ordinales**, que no requieren operaciones aritméticas tradicionales, son adecuados para técnicas como la regresión logística, árboles de decisión y redes neuronales con codificación adecuada (one-hot, ordinal o embedding), y generalmente se utilizan para modelos de clasificación. Estos datos necesitan transformaciones especiales para ser procesados numéricamente.

Los **datos de intervalo y razón** permiten una mayor flexibilidad matemática y son compatibles con una amplia gama de modelos, incluidos la regresión lineal, análisis de componentes principales (PCA), redes neuronales con capas densas, y algoritmos de clustering como K-means. Se utilizan principalmente para modelos de regresión pero también en clasificación cuando se combinan con umbralización o funciones apropiadas.

La **relación entre los niveles de medición y los modelos cuantitativos/cualitativos** es importante para elegir las técnicas de análisis adecuadas y las transformaciones de datos necesarias:

- Los **datos nominales** son ideales para **modelos cualitativos**, como técnicas de clasificación y categorización, y suelen ser representados mediante codificación one-hot en redes neuronales para tareas de clasificación. Ejemplo práctico: clasificación de especies de plantas basada en características categóricas como tipo de hoja, color de flor, o hábitat.

- Los **datos ordinales**, aunque categóricos, tienen un orden intrínseco que puede ser utilizado tanto en **modelos cualitativos como cuantitativos**. Pueden codificarse numéricamente respetando el orden o tratarse como categorías. Ejemplo: niveles de satisfacción de clientes (muy insatisfecho, insatisfecho, neutral, satisfecho, muy satisfecho) o grados de severidad de una enfermedad.

- Los **datos de intervalo** permiten operaciones aritméticas (suma, resta) y son adecuados para **análisis estadísticos cuantitativos** avanzados, aunque carecen de cero absoluto. Ejemplo: temperaturas diarias en grados Celsius o fechas en calendario, donde las diferencias son significativas pero los ratios no.

- Los **datos de razón**, con un verdadero cero absoluto, permiten **análisis más completos y precisos**, incluyendo todas las operaciones aritméticas y proporcionales. Ejemplo: ingresos mensuales, peso de individuos, distancias recorridas, o tiempo de respuesta, donde tanto diferencias como ratios tienen significado.

El nivel de medición de los datos influye directamente en:
- **Preprocesamiento requerido**: normalización, estandarización, codificación.
- **Tipo de modelo aplicable**: algunos modelos asumen propiedades numéricas específicas.
- **Funciones de pérdida apropiadas**: entropía cruzada para categorías, MSE para continuos.
- **Métricas de evaluación**: exactitud para clasificación, RMSE para regresión.
- **Interpretabilidad de resultados**: cómo se pueden interpretar coeficientes o importancia de características.

### **Metodología para entrenamiento y evaluación**

Una **metodología genérica** es un enfoque estándar y sistemático utilizado para entrenar y evaluar modelos de machine learning de manera rigurosa. Esta metodología incluye pasos secuenciales comunes como la **preparación de datos** (limpieza, transformación, división), la **definición del modelo** (arquitectura, hiperparámetros), el **entrenamiento** (optimización de parámetros), la **evaluación** (medición de rendimiento) y la **optimización** (ajuste fino de hiperparámetros y mejoras iterativas). 

El proceso completo típicamente incluye:

1. **Recolección y exploración de datos**: Obtener datos relevantes, analizar distribuciones, identificar valores atípicos y comprender relaciones entre variables.

2. **Preprocesamiento**: Limpieza de datos (manejo de valores faltantes, outliers), transformación (normalización, estandarización, codificación de variables categóricas), y ingeniería de características (creación de nuevas features relevantes).

3. **División de datos**: Separar en conjuntos de entrenamiento, validación y prueba, típicamente en proporciones 70-15-15 o 60-20-20, asegurando representatividad y aleatoriedad.

4. **Selección y configuración del modelo**: Elegir arquitectura apropiada, definir hiperparámetros iniciales y configurar el proceso de entrenamiento.

5. **Entrenamiento**: Ajustar parámetros del modelo usando datos de entrenamiento, monitoreando métricas y aplicando técnicas de regularización.

6. **Validación**: Evaluar rendimiento en datos de validación, ajustar hiperparámetros y detectar problemas como sobreajuste.

7. **Evaluación final**: Medir rendimiento en datos de prueba completamente independientes para estimar capacidad de generalización.

8. **Iteración y mejora**: Refinar modelo basándose en resultados, experimentar con diferentes arquitecturas o técnicas, y documentar hallazgos.

Esta metodología es adaptable a una amplia gama de problemas, permitiendo ajustes según las características específicas de los datos, las restricciones computacionales y las necesidades del problema.

### **Validación cruzada de datos**

La **validación cruzada** (cross-validation) es una técnica robusta para evaluar modelos de *machine learning* que maximiza el uso de datos disponibles y proporciona estimaciones más confiables del rendimiento. El método más común es **k-fold cross-validation**, que divide los datos en k subconjuntos (*folds*) de tamaño aproximadamente igual. 

El proceso funciona así:

1. Los datos se dividen aleatoriamente en k particiones.
2. Se realizan k iteraciones de entrenamiento y evaluación.
3. En cada iteración, k-1 folds se usan para entrenar y 1 fold para validar.
4. Se rota el fold de validación hasta que cada uno haya sido usado una vez.
5. Se promedian las métricas de rendimiento de las k iteraciones.

Variantes de validación cruzada incluyen:

- **Leave-One-Out (LOO)**: Caso extremo donde k = número de muestras. Útil con datasets pequeños pero computacionalmente costoso.
- **Stratified K-Fold**: Mantiene proporciones de clases en cada fold, crucial para datos desbalanceados.
- **Time Series Split**: Respeta orden temporal, importante para datos secuenciales.
- **Repeated K-Fold**: Repite k-fold con diferentes particiones aleatorias para mayor robustez.

Beneficios de la validación cruzada:

- Previene *overfitting* al probar el modelo en múltiples subconjuntos independientes.
- Ofrece una estimación más robusta y generalizable del rendimiento real del modelo.
- Reduce varianza en la estimación de rendimiento comparado con una sola división train-test.
- Aprovecha mejor datos limitados al usar todas las muestras para entrenamiento y validación.

Consideraciones:

- Mayor costo computacional (k veces el entrenamiento normal).
- No reemplaza la evaluación final en conjunto de prueba completamente separado.
- La elección de k (típicamente 5 o 10) balancea sesgo, varianza y costo computacional.

## Aprendizaje supervisado y no supervisado

La **clasificación de datos en aprendizaje automático** se divide en dos paradigmas fundamentales que difieren en la naturaleza de los datos de entrada y los objetivos de aprendizaje:

### Aprendizaje Supervisado

El **aprendizaje supervisado** utiliza datos con etiquetas conocidas (pares entrada-salida) para entrenar un modelo que aprenda la relación entre características de entrada y resultados esperados, permitiendo predecir salidas para nuevas entradas. 

**Características principales:**
- Requiere datos etiquetados (anotados manualmente o automáticamente).
- El modelo aprende una función de mapeo: f(X) → Y.
- Objetivo: minimizar error entre predicciones y valores verdaderos.
- Retroalimentación directa disponible durante el entrenamiento.

**Aplicaciones principales:**

**Clasificación**: Asignar muestras a categorías discretas.
- Binaria: spam/no spam, fraude/legítimo, enfermo/sano.
- Multiclase: reconocimiento de dígitos (0-9), clasificación de especies, categorización de documentos.
- Multilabel: etiquetado de imágenes con múltiples objetos, clasificación de géneros musicales.

**Regresión**: Predecir valores continuos.
- Predicción de precios (viviendas, acciones).
- Estimación de demanda energética.
- Pronóstico de ventas.
- Predicción de temperatura o variables climáticas.

**Algoritmos representativos:**
- **Regresión Lineal/Logística**: Modelos simples pero interpretables.
- **SVM (Support Vector Machines)**: Efectivos en espacios de alta dimensión.
- **K-NN (K-Nearest Neighbors)**: Basado en similitud con vecinos cercanos.
- **Árboles de Decisión**: Intuitivos, base de métodos de ensamble.
- **Random Forest**: Ensamble de árboles, robusto al overfitting.
- **Gradient Boosting (XGBoost, LightGBM)**: Estado del arte en muchos problemas tabulares.
- **Redes Neuronales**: Desde perceptrones simples hasta arquitecturas profundas.

### Aprendizaje No Supervisado

El **aprendizaje no supervisado** trabaja con datos sin etiquetas, buscando descubrir **patrones ocultos, estructuras intrínsecas, agrupaciones naturales o representaciones compactas** de los datos sin guía externa.

**Características principales:**
- No requiere etiquetas ni supervisión humana.
- El modelo busca estructura subyacente en los datos.
- Objetivo: descubrir patrones, reducir dimensionalidad o detectar anomalías.
- Evaluación más subjetiva y dependiente del dominio.

**Aplicaciones principales:**

**Clustering (Agrupamiento)**: Agrupar datos similares sin conocer categorías previamente.
- Segmentación de clientes por comportamiento de compra.
- Agrupación de documentos por temas.
- Identificación de comunidades en redes sociales.
- Compresión de imágenes mediante cuantización de colores.

**Reducción de dimensionalidad**: Proyectar datos de alta dimensión a espacios más manejables.
- Visualización de datos complejos.
- Compresión de datos preservando información relevante.
- Eliminación de ruido y características redundantes.
- Preprocesamiento para otros algoritmos.

**Detección de anomalías**: Identificar patrones inusuales o atípicos.
- Detección de fraudes financieros.
- Identificación de fallos en sistemas.
- Monitoreo de seguridad en redes.
- Control de calidad en manufactura.

**Algoritmos representativos:**
- **K-Means**: Clustering por centroides, eficiente pero sensible a inicialización.
- **Clustering Jerárquico**: Construye dendrogramas, útil para estructuras anidadas.
- **DBSCAN**: Identifica clusters de forma arbitraria y detecta outliers.
- **Gaussian Mixture Models (GMM)**: Clustering probabilístico flexible.
- **PCA (Principal Component Analysis)**: Reducción lineal de dimensionalidad.
- **t-SNE**: Visualización no lineal preservando vecindarios locales.
- **UMAP**: Alternativa moderna a t-SNE, más rápida y escalable.
- **Autoencoders**: Redes neuronales para aprendizaje de representaciones compactas.
- **Isolation Forest**: Detección de anomalías basada en aislamiento de puntos.

### Comparación entre Aprendizaje Supervisado y No Supervisado

| **Aspecto** | **Aprendizaje Supervisado** | **Aprendizaje No Supervisado** |
| --- | --- | --- |
| **Etiquetas** | Sí, requiere datos anotados | No, trabaja con datos sin etiquetar |
| **Objetivo** | Predecir resultados basados en ejemplos etiquetados | Descubrir patrones ocultos en los datos |
| **Modelos** | Clasificación, regresión | Clustering, reducción de dimensionalidad, detección de anomalías |
| **Evaluación** | Comparación directa con etiquetas verdaderas (métricas objetivas) | Más complejo, suele basarse en métricas internas o validación de dominio |
| **Ejemplos** | Clasificación de imágenes, predicción de precios, diagnóstico médico | Segmentación de clientes, compresión de datos, detección de fraudes |
| **Costo de datos** | Alto (requiere etiquetado manual o automático) | Bajo (datos sin etiquetar abundantes) |
| **Interpretabilidad** | Resultados directamente interpretables | Requiere análisis adicional para interpretación |
| **Aplicaciones típicas** | Sistemas de recomendación, reconocimiento de voz, traducción automática | Análisis exploratorio, preprocesamiento, minería de datos |

### Aprendizaje Semisupervisado y por Refuerzo

Además de los paradigmas principales, existen otros enfoques:

**Aprendizaje Semisupervisado**: Combina pequeñas cantidades de datos etiquetados con grandes volúmenes de datos sin etiquetar. Útil cuando el etiquetado es costoso pero se dispone de muchos datos sin anotar. Ejemplos: self-training, co-training, métodos basados en grafos.

**Aprendizaje por Refuerzo**: El agente aprende mediante interacción con un entorno, recibiendo recompensas o penalizaciones por sus acciones. Aplicaciones: juegos (AlphaGo), robótica, sistemas de control, conducción autónoma.

### Búsqueda de Patrones en Aprendizaje Automático

La **búsqueda de patrones en aprendizaje automático** se aborda de manera fundamentalmente distinta según el enfoque:

**En Aprendizaje Supervisado**: 
Busca **relaciones sistemáticas entre características de entrada y etiquetas conocidas**. El modelo aprende una función de mapeo que minimiza el error de predicción entre sus salidas y los resultados reales. Este proceso es dirigido por la retroalimentación proporcionada por las etiquetas.

**Ejemplos detallados:**
- **Clasificación de correos como spam**: El modelo aprende patrones en características como frecuencia de palabras específicas, uso de mayúsculas, presencia de enlaces, estructura del remitente, que distinguen correos legítimos de spam.
- **Clasificación de imágenes (gatos vs. perros)**: Aprende jerarquías de características desde bordes y texturas hasta formas complejas y partes de animales que permiten discriminar entre especies.
- **Predicción de precios de viviendas**: Modela relaciones entre características (tamaño, ubicación, número de habitaciones, antigüedad, amenidades) y precios históricos para estimar valores de propiedades nuevas.
- **Diagnóstico médico asistido**: Identifica patrones en síntomas, resultados de pruebas y datos demográficos que se correlacionan con diagnósticos confirmados.

**En Aprendizaje No Supervisado**:
Busca **estructuras ocultas, agrupaciones naturales o representaciones compactas** sin usar etiquetas como guía. Se centra en detectar similitudes inherentes, reducir complejidad dimensional o identificar comportamientos anómalos.

**Ejemplos detallados:**
- **Segmentación de clientes**: Agrupa usuarios con patrones de compra, navegación o interacción similares para estrategias de marketing personalizadas, sin conocer a priori las categorías de clientes.
- **Agrupamiento de documentos**: Organiza textos por temas o contenido similar usando técnicas como TF-IDF y clustering, descubriendo categorías temáticas emergentes.
- **Detección de fraudes**: Identifica transacciones que se desvían significativamente del comportamiento normal aprendido de datos históricos, sin ejemplos etiquetados de fraude.
- **Análisis de redes sociales**: Descubre comunidades o grupos de usuarios con intereses o conexiones similares mediante análisis de grafos.
- **Compresión y visualización de datos**: Reduce datos de alta dimensión (ej: imágenes, expresión genética) a representaciones 2D o 3D que preservan estructura importante para exploración visual.

**Diferencias clave en la búsqueda de patrones:**

- **Supervisado**: Patrones se definen en relación a un objetivo específico (etiqueta).
- **No supervisado**: Patrones emergen de la estructura intrínseca de los datos.
- **Supervisado**: Validación mediante comparación con ground truth.
- **No supervisado**: Validación mediante coherencia interna o interpretación de dominio.
- **Supervisado**: Orientado a predicción y generalización a nuevos casos.
- **No supervisado**: Orientado a comprensión, exploración y descubrimiento.

### **Modelo, conjunto de datos de validación, evaluación del rendimiento y overfitting**

### Modelo

Un **modelo de aprendizaje automático** es una **representación matemática parametrizada** que aprende patrones, relaciones y estructuras a partir de datos de entrenamiento para realizar tareas específicas como clasificación, regresión, clustering o predicción. La calidad y utilidad del modelo dependen críticamente de:

- **Representatividad de los datos**: Los datos de entrenamiento deben capturar adecuadamente la variabilidad y características del problema real.
- **Arquitectura apropiada**: El modelo debe tener capacidad suficiente (pero no excesiva) para capturar la complejidad del problema.
- **Proceso de entrenamiento**: Algoritmos de optimización, hiperparámetros y técnicas de regularización apropiados.
- **Capacidad de generalización**: Habilidad para desempeñarse bien en datos no vistos durante el entrenamiento.

### Conjuntos de datos

La división estratégica de datos es fundamental para un desarrollo de modelo robusto:

- **Conjunto de Entrenamiento (Training Set)**: 
    - Típicamente 60-80% de los datos totales.
    - Usado para ajustar los parámetros del modelo (pesos y sesgos en redes neuronales).
    - El modelo "ve" estos datos durante el aprendizaje.
    - Debe ser suficientemente grande y representativo.

- **Conjunto de Validación (Validation Set)**:
    - Típicamente 10-20% de los datos.
    - Permite ajustar hiperparámetros (tasa de aprendizaje, número de capas, etc.) y arquitectura del modelo.
    - Usado para monitorear overfitting durante el entrenamiento.
    - Ayuda en decisiones como early stopping.
    - No contamina la evaluación final.

- **Conjunto de Prueba (Test Set)**:
    - Típicamente 10-20% de los datos.
    - Reservado estrictamente para evaluación final.
    - Nunca usado durante entrenamiento o ajuste de hiperparámetros.
    - Proporciona estimación imparcial de capacidad de generalización.
    - Simula datos del mundo real que el modelo encontrará en producción.

**Consideraciones importantes:**
- Mantener distribuciones similares en los tres conjuntos.
- Asegurar aleatoriedad en la división (excepto en datos temporales).
- Para datos desbalanceados, usar división estratificada.
- En datasets pequeños, usar validación cruzada en lugar de división simple.

### Evaluación del rendimiento

La **evaluación cuantitativa del rendimiento** se realiza mediante **métricas específicas** según el tipo de problema:

**Para Clasificación:**
- **Exactitud (Accuracy)**: Proporción de predicciones correctas. Simple pero puede engañar con datos desbalanceados.
- **Precisión (Precision)**: De las predicciones positivas, cuántas son correctas. Importante cuando falsos positivos son costosos.
- **Sensibilidad/Recall**: De los casos positivos reales, cuántos se detectan. Crítico cuando falsos negativos son peligrosos.
- **F1-Score**: Media armónica de precisión y recall. Balancea ambas métricas.
- **Matriz de Confusión**: Visualiza todas las combinaciones de predicciones y valores reales.
- **AUC-ROC**: Mide capacidad de discriminación en diferentes umbrales.
- **Especificidad**: Tasa de verdaderos negativos.

**Para Regresión:**
- **MSE (Mean Squared Error)**: Penaliza fuertemente errores grandes.
- **RMSE (Root MSE)**: En las mismas unidades que la variable objetivo.
- **MAE (Mean Absolute Error)**: Menos sensible a outliers que MSE.
- **R² (Coeficiente de Determinación)**: Proporción de varianza explicada.
- **MAPE (Mean Absolute Percentage Error)**: Error relativo, útil para comparar diferentes escalas.

**Para Clustering:**
- **Silhouette Score**: Mide cohesión interna y separación entre clusters.
- **Davies-Bouldin Index**: Ratio de dispersión intra-cluster vs inter-cluster.
- **Inercia**: Suma de distancias cuadradas a centroides (en K-means).
- **Adjusted Rand Index**: Compara clustering con ground truth si está disponible.

### Overfitting (sobreajuste)

El **overfitting** es uno de los problemas más importantes en aprendizaje automático, ocurriendo cuando el modelo aprende en exceso los detalles específicos, el ruido y las peculiaridades de los datos de entrenamiento, perdiendo capacidad de generalización a nuevos datos.

**Síntomas característicos:**
- Rendimiento excelente en entrenamiento pero pobre en validación/prueba.
- Alta varianza en predicciones.
- Modelo excesivamente complejo para el problema.
- Sensibilidad extrema a pequeños cambios en datos de entrada.

**Causas comunes:**
- Modelo con capacidad excesiva (demasiados parámetros).
- Datos de entrenamiento insuficientes.
- Entrenamiento prolongado sin control.
- Falta de regularización.
- Características irrelevantes o ruidosas.
- Datos no representativos del problema general.

**Soluciones y técnicas de mitigación:**

1. **Regularización**:
     - L1 (Lasso): Promueve dispersión, selección automática de features.
     - L2 (Ridge): Penaliza pesos grandes, distribución más uniforme.
     - Elastic Net: Combina L1 y L2.

2. **Más datos de entrenamiento**: Aumenta representatividad y reduce memorización.

3. **Validación cruzada**: Evaluación robusta en múltiples particiones.

4. **Early Stopping**: Detiene entrenamiento cuando rendimiento en validación se degrada.

5. **Dropout**: Desactiva aleatoriamente neuronas durante entrenamiento, forzando redundancia.

6. **Data Augmentation**: Genera variaciones de datos existentes (rotaciones, ruido, traslaciones).

7. **Simplificación del modelo**:
     - Reducir número de parámetros.
     - Eliminar capas o neuronas.
     - Usar arquitecturas más simples.

8. **Selección de características**: Eliminar features irrelevantes o redundantes.

9. **Ensemble Methods**: Combinar múltiples modelos reduce varianza.

10. **Batch Normalization**: Estabiliza distribuciones de activaciones.

**Contraparte - Underfitting:**
Cuando el modelo es demasiado simple para capturar la complejidad del problema:
- Rendimiento pobre tanto en entrenamiento como en prueba.
- Alto sesgo, baja varianza.
- Solución: aumentar complejidad del modelo, más features, entrenamiento más prolongado.

**Balance óptimo:**
El objetivo es encontrar el punto óptimo donde el modelo generaliza bien sin sobreajustarse ni subajustarse, logrando buen rendimiento tanto en datos de entrenamiento como en datos nuevos.

## Modelo de Regresión Lineal

La **regresión lineal** es uno de los modelos estadísticos y de machine learning más fundamentales, históricos y ampliamente utilizados, sirviendo como punto de partida esencial para comprender técnicas más avanzadas y complejas. Su objetivo principal es modelar la relación matemática entre una variable dependiente (objetivo, respuesta) y una o varias variables independientes (predictoras, features), mediante una función lineal —una línea recta en 2D o un hiperplano en dimensiones superiores— que minimiza el error entre los valores reales observados y los valores predichos por el modelo.

### Fundamentos Matemáticos

**Regresión Lineal Simple** (una variable independiente):
```
y = β₀ + β₁x + ε
```
Donde:
- y: variable dependiente
- x: variable independiente
- β₀: intercepto (valor de y cuando x=0)
- β₁: pendiente (cambio en y por unidad de cambio en x)
- ε: término de error (ruido)

**Regresión Lineal Múltiple** (múltiples variables independientes):
```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
```

En forma matricial:
```
Y = Xβ + ε
```

### Método de Mínimos Cuadrados Ordinarios (OLS)

El método más común para ajustar los coeficientes es **mínimos cuadrados ordinarios**, que minimiza la suma de los errores cuadráticos:

```
min Σ(yᵢ - ŷᵢ)²
```

La solución analítica para los coeficientes es:
```
β = (XᵀX)⁻¹XᵀY
```

### Características y Ventajas

Este modelo destaca por múltiples razones:

**Simplicidad:**
- Fácil de implementar y computacionalmente eficiente.
- Requiere menos recursos que modelos complejos.
- Adecuado para datasets pequeños y medianos.

**Interpretabilidad:**
- Los coeficientes tienen significado directo: representan el cambio esperado en Y por unidad de cambio en X.
- Permite identificar qué variables son más influyentes.
- Facilita comunicación de resultados a stakeholders no técnicos.

**Utilidad dual:**
- **Predicción**: Estimar valores futuros basándose en nuevas observaciones.
- **Análisis descriptivo**: Entender relaciones entre variables y su fuerza.

### Supuestos del Modelo

La regresión lineal asume:

1. **Linealidad**: Relación lineal entre variables independientes y dependiente.
2. **Independencia**: Observaciones independientes entre sí.
3. **Homoscedasticidad**: Varianza constante de los errores.
4. **Normalidad de errores**: Residuos siguen distribución normal.
5. **No multicolinealidad**: Variables independientes no altamente correlacionadas.

Violaciones de estos supuestos pueden llevar a predicciones sesgadas o ineficientes.

### Métricas de Evaluación

**Coeficiente de Determinación (R²)**:
```
R² = 1 - (SS_res / SS_tot)
```
- Indica proporción de varianza explicada (0 a 1).
- R² = 1: ajuste perfecto.
- R² = 0: modelo no mejor que predecir la media.
- R² ajustado penaliza complejidad del modelo.

**Error Cuadrático Medio (MSE)**:
```
MSE = (1/n) Σ(yᵢ - ŷᵢ)²
```

**Raíz del Error Cuadrático Medio (RMSE)**:
```
RMSE = √MSE
```
En las mismas unidades que Y, más interpretable.

**Error Absoluto Medio (MAE)**:
```
MAE = (1/n) Σ|yᵢ - ŷᵢ|
```
Menos sensible a outliers que MSE.

### Medidas de Incertidumbre

Además de predicciones puntuales, la regresión lineal proporciona:

**Intervalos de Confianza para Coeficientes**:
- Rango de valores plausibles para β con nivel de confianza especificado (típicamente 95%).
- Indica significancia estadística: si el intervalo no incluye 0, la variable es significativa.

**Intervalos de Predicción**:
- Rango donde se espera que caiga una nueva observación.
- Más amplios que intervalos de confianza, incorporan incertidumbre del modelo y variabilidad inherente.

**Estadísticos de Prueba**:
- **Prueba t**: Significancia individual de coeficientes.
- **Prueba F**: Significancia global del modelo.
- **p-valores**: Probabilidad de observar los datos si la hipótesis nula (coeficiente=0) fuera cierta.

### Conexión con Redes Neuronales

La regresión lineal guarda una relación íntima y reveladora con las redes neuronales:

**Equivalencia con Perceptrón Simple**:
Un perceptrón básico **sin función de activación no lineal** (o con activación lineal) es matemáticamente equivalente a un modelo de regresión lineal:
```
ŷ = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
```
Donde w son los pesos (equivalentes a β) y b es el sesgo (equivalente a β₀).

**Superación de Limitaciones**:
- La introducción de **funciones de activación no lineales** (sigmoid, tanh, ReLU) permite a las redes neuronales superar las limitaciones de la regresión lineal.
- Múltiples capas permiten modelar relaciones jerárquicas y complejas.
- Las redes neuronales pueden verse como generalizaciones no lineales de la regresión lineal.

**Caso Especial**:
- Una red neuronal de una sola capa con activación lineal **es exactamente** regresión lineal.
- Añadir capas ocultas con activaciones lineales sigue siendo equivalente a regresión lineal (composición de funciones lineales es lineal).
- La no linealidad es esencial para el poder de las redes neuronales.

### Extensiones y Variantes

**Regresión Polinomial**:
- Añade términos de orden superior: x², x³, etc.
- Sigue siendo lineal en los parámetros.
- Puede capturar relaciones curvas.

**Regresión Ridge (L2)**:
- Añade penalización: λΣβᵢ²
- Previene overfitting reduciendo magnitud de coeficientes.
- Útil con multicolinealidad.

**Regresión Lasso (L1)**:
- Añade penalización: λΣ|βᵢ|
- Puede forzar coeficientes exactamente a cero.
- Realiza selección automática de features.

**Elastic Net**:
- Combina L1 y L2.
- Balancea ventajas de ambas técnicas.

### Aplicaciones Prácticas

- Predicción de precios (inmobiliario, acciones, commodities).
- Análisis de tendencias temporales.
- Modelado de relaciones causa-efecto en ciencias sociales.
- Forecasting en negocios (ventas, demanda).
- Análisis de sensibilidad de variables.
- Benchmarking: línea base para comparar modelos más complejos.

### Limitaciones

- Solo captura relaciones lineales.
- Sensible a outliers.
- Asume homocedasticidad y normalidad de errores.
- No maneja bien multicolinealidad alta.
- Puede underfit problemas complejos.

A pesar de sus limitaciones, la regresión lineal permanece como herramienta fundamental por su simplicidad, interpretabilidad y eficacia en muchos problemas reales, además de servir como base conceptual para entender modelos más sofisticados.