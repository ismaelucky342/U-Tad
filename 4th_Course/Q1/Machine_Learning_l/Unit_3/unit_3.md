# 2609_INSD4_AAUI_A

**SCORM:** _739330_1
**URL del contenido:** https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormdriver/indexAPI.html

## Contenido

### INTRODUCCIÓN Y OBJETIVOS

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/preview</sub>

Unidad 3. Modelos de regresión (Aprendizaje supervisado I).
COMENZAR CURSO
INTRODUCCIÓN Y OBJETIVOS
Introducción y objetivos
INTRODUCCIÓN AL APRENDIZAJE SUPERVISADO
Introducción
Conceptos y fundamentos
Tipos de tareas
REGRESIÓN LINEAL SIMPLE
Introducción
Concepto y fundamentos matemáticos
Ajuste del modelo
Limitaciones y supuestos
REGRESIÓN LINEAL MÚLTIPLE
Introducción
Concepto y fundamentos matemáticos
Selección de variables
Multicolinealidad
Comparación con regresión simple
Supuestos y diagnóstico
EVALUACIÓN DE MODELOS DE REGRESIÓN
Introducción
Métricas comunes
CONCLUSIONES
Conclusiones de la unidad
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar
Sin comenzar

### Lesson 1 - Introducción y objetivos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/KWHD4sXEzpFyNzxa9IsUJ9Jpz0xQWKjn</sub>

PASE A LA LECCIÓN
Unidad 3. Modelos de regresión (Aprendizaje supervisado I).
Introducción y objetivos

Introducción

El aprendizaje supervisado es una rama del aprendizaje automático cuyo objetivo es construir modelos capaces de predecir una salida a partir de un conjunto de entradas, empleando para ello datos etiquetados. Estos datos incluyen casos en los que tanto las características (variables independientes) como el valor esperado (variable dependiente) son conocidos. A partir de este conocimiento previo, el modelo aprende la relación subyacente para aplicarla a nuevos casos.

Dentro del aprendizaje supervisado, las tareas se dividen en dos grandes categorías: clasificación, cuando la variable de salida es discreta, y regresión, cuando la salida es continua. Esta unidad se centra en esta última, la regresión, profundizando en sus fundamentos teóricos y en su aplicación práctica. La regresión permite estimar el valor de una variable continua en función de una o varias variables predictoras, con aplicaciones en ámbitos tan diversos como la economía, la ingeniería, la meteorología o las ciencias sociales.

Se comienza con la regresión lineal simple, que modela la relación entre una única variable predictora y la variable objetivo mediante una recta, abordando su formulación matemática, la interpretación de sus coeficientes y el ajuste del modelo por el método de mínimos cuadrados. Posteriormente, se analizan los supuestos y limitaciones de este tipo de regresión, así como las técnicas para diagnosticarlos.

El siguiente bloque se dedica a la regresión lineal múltiple, una extensión del modelo simple que incorpora varias variables predictoras de forma simultánea. Este apartado cubre su formulación, la interpretación de los coeficientes, la selección de variables relevantes, el tratamiento de la multicolinealidad y la aplicación práctica. Se comparan además sus ventajas y limitaciones respecto a la regresión simple, destacando los riesgos de sobreajuste y la importancia de validar los supuestos estadísticos.

Finalmente, la unidad concluye con la evaluación de modelos de regresión, donde se estudian las métricas más empleadas para medir el rendimiento y la capacidad explicativa del modelo, tales como el Error Cuadrático Medio (MSE), la Raíz del Error Cuadrático Medio (RMSE), el Error Absoluto Medio (MAE), el Coeficiente de Determinación (R²) y su versión ajustada.

El enfoque seguido combina explicaciones conceptuales con ejemplos prácticos en Python, de modo que se facilite la comprensión de los fundamentos matemáticos y estadísticos al tiempo que se desarrollan las habilidades necesarias para implementar y evaluar modelos de regresión en contextos reales.

Haz clic para voltear

Introducción al aprendizaje supervisado

Haz clic para voltear

El aprendizaje supervisado constituye uno de los enfoques más extendidos y estudiados dentro del aprendizaje automático. En este paradigma, el modelo se entrena utilizando un conjunto de datos que contiene pares de entrada y salida conocidos. La entrada, también denominada vector de características o atributos, describe las propiedades relevantes de cada instancia; la salida, también llamada etiqueta o valor objetivo, representa la respuesta que se desea predecir. El objetivo del aprendizaje supervisado es aproximar una función f(X) ≈ Y que permita predecir con precisión la salida correspondiente para nuevas entradas no vistas durante el entrenamiento.

Haz clic para voltear

Regresión lineal simple

Haz clic para voltear

En el contexto del aprendizaje automático, la regresión lineal simple utiliza un conjunto de datos etiquetados, pares de ejemplos de entrada y su valor objetivo, para ajustar una línea que minimice la diferencia entre las predicciones y los valores reales. Este ajuste se realiza mediante un proceso de optimización que, tradicionalmente, se basa en el método de mínimos cuadrados.

Haz clic para voltear

Regresión lineal múltiple

Haz clic para voltear

La Regresión Lineal Múltiple (RLM) es una extensión natural de la regresión lineal simple que permite analizar la relación entre una variable dependiente continua y dos o más variables independientes. Este modelo es especialmente útil cuando el fenómeno a estudiar no puede ser explicado satisfactoriamente con un solo predictor, sino que depende de múltiples factores que interactúan entre sí.

Haz clic para voltear

Evolución de modelos de regresión

Haz clic para voltear

La evaluación de modelos de regresión es una etapa fundamental en el proceso de modelado, ya que permite cuantificar la capacidad predictiva y la calidad del ajuste alcanzado. El objetivo principal es disponer de herramientas objetivas para comparar diferentes modelos y seleccionar aquel que ofrezca un equilibrio óptimo entre precisión, simplicidad y capacidad de generalización.

Objetivos

Al finalizar esta unidad, el estudiante será capaz de:

1

Comprender el concepto de regresión dentro del aprendizaje supervisado, diferenciándolo de la clasificación y contextualizando su uso en la predicción de variables continuas.

2

Explicar la formulación matemática de la regresión lineal simple y múltiple, identificando las variables dependientes e independientes, los coeficientes y el término de error.

3

Comprender el método de mínimos cuadrados para estimar los parámetros de un modelo de regresión lineal.

4

Interpretar correctamente los coeficientes del modelo, reconociendo su significado en términos de pendiente, intercepto y efecto marginal de cada predictor.

5

Identificar y evaluar los supuestos estadísticos de la regresión lineal (linealidad, homocedasticidad, independencia de errores, normalidad residual y ausencia de multicolinealidad).

6

Diagnosticar problemas comunes en regresión mediante herramientas gráficas y métricas estadísticas.

7

Seleccionar adecuadamente las variables predictoras en un modelo múltiple, empleando criterios de significancia y análisis de correlación.

8

Implementar en Python modelos de regresión lineal simple y múltiple, utilizando librerías como scikit-learn.

9

Evaluar el rendimiento de un modelo de regresión mediante métricas como MSE, RMSE, MAE, R² y R² ajustado, interpretando sus resultados en el contexto del problema.

10

Comparar modelos de regresión a partir de sus métricas de desempeño, identificando ventajas y limitaciones de cada uno.

¡Comenzamos!

### Lesson 2 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/mZzoI043M_WKyqgQlevSAmTLjMA2ggKe</sub>

Introducción

El aprendizaje supervisado constituye uno de los enfoques más extendidos y estudiados dentro del aprendizaje automático. En este paradigma, el modelo se entrena utilizando un conjunto de datos que contiene pares de entrada y salida conocidos. La entrada, también denominada vector de características o atributos, describe las propiedades relevantes de cada instancia; la salida, también llamada etiqueta o valor objetivo, representa la respuesta que se desea predecir. El objetivo del aprendizaje supervisado es aproximar una función f(X) ≈ Y que permita predecir con precisión la salida correspondiente para nuevas entradas no vistas durante el entrenamiento.

Este enfoque se diferencia del aprendizaje no supervisado, donde no se dispone de etiquetas y el objetivo es descubrir patrones ocultos en los datos, y del aprendizaje por refuerzo, en el que el agente aprende a tomar decisiones a partir de recompensas acumuladas. Una de las ventajas clave del aprendizaje supervisado es que, al conocer de antemano la respuesta correcta para los ejemplos de entrenamiento, es posible evaluar de manera directa y cuantitativa el rendimiento del modelo.

El flujo básico de trabajo en aprendizaje supervisado comienza con un conjunto de entrenamiento etiquetado, que se utiliza para ajustar los parámetros del modelo, y continúa con la predicción sobre nuevos datos. Este proceso se apoya en la premisa de que las relaciones encontradas en los datos de entrenamiento se mantienen en los datos futuros. Si las características extraídas y las etiquetas están bien definidas y representadas, el modelo tendrá mayor capacidad de generalización.

Esquema de funcionamiento de un modelo de aprendizaje supervisado

¿Todo listo? ¡Empezamos!

### Lesson 3 - Conceptos y fundamentos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/H9K_4soYIMREtTh_yFZHs58D8TcfKKBG</sub>

Conceptos y fundamentos

En el aprendizaje supervisado, el objetivo central es encontrar una función de mapeo f:X→Y que asocie cada entrada x ∈ X con su salida correspondiente y ∈ Y.

X (dominio de entrada): conjunto de posibles combinaciones de variables predictoras o atributos.

Y (dominio de salida): variable objetivo, que puede ser un conjunto de valores reales (en regresión) o un conjunto finito de clases (en clasificación).

θ (parámetros del modelo): conjunto de valores ajustables durante el proceso de entrenamiento y que determinan el comportamiento de la función f.

Esquema del aprendizaje supervisado, se conoce la entrada y la salida. Se busca la función que a partir de una entrada daría la salida esperada.

El modelo resultante se representa como y′=f(x;θ) donde y′​ es la predicción generada para la entrada x. El entrenamiento busca los valores óptimos θ* que minimicen el error de predicción entre y′ e y según un criterio cuantitativo definido por una función de coste.

Componentes de un problema supervisado

El aprendizaje supervisado parte de un conjunto de datos formado por pares (entrada, salida).

La entrada representa la información disponible para realizar la predicción y puede consistir en texto, imágenes, series temporales o mediciones de sensores, entre otros formatos.

La salida o etiqueta corresponde al valor que el modelo debe predecir, y puede ser un número real o una categoría (por ejemplo, spam, no spam, perro, gato, pájaro, etc.), un vector (por ejemplo, cuatro coordenadas del rectángulo que rodea a una persona en la imagen) o incluso una estructura más compleja como secuencias (por ejemplo, [adjetivo, adjetivo, sustantivo] para la entrada coche grande y bonito) o coordenadas.

Además, un problema de aprendizaje supervisado involucra los siguientes elementos:

Instancias: cada observación o fila del conjunto de datos.

Atributos (features): variables explicativas que describen cada instancia.

Etiqueta (target): valor de salida que se desea predecir.

Modelo: función matemática entrenada para predecir la etiqueta a partir de los atributos.

Algoritmo: procedimiento que ajusta los parámetros del modelo usando los datos de entrenamiento.

El proceso se desarrolla sobre un conjunto de datos etiquetado, es decir, donde para cada entrada se conoce la salida correcta.

Representación, modelado y límites de decisión

En aprendizaje supervisado, el primer paso para que un algoritmo pueda procesar la información es representar adecuadamente las entradas y salidas en un formato comprensible para el modelo. Los algoritmos matemáticos no operan directamente con texto, imágenes, audio o vídeo; necesitan que la información esté codificada como vectores de características numéricos.

Transformación de las entradas en vectores de características

Un vector de características o vector de atributos es una representación numérica que resume las propiedades relevantes de cada instancia. Cada posición del vector corresponde a una característica cuantificable y el valor asignado refleja su presencia, frecuencia o intensidad.

Representación de un vector de características

En un problema de clasificación de correo electrónico para detección de spam, se recopilan los datos, por ejemplo 10000 mensajes de correo electrónico y se etiquetan como spam o no spam. Cada mensaje se convierte en un vector de características. El analista de datos decide, basándose en su experiencia, cómo convertir una entidad del mundo real, como un mensaje de correo electrónico, en un vector de características. Una forma habitual de convertir un texto en un vector de características, denominada bolsa de palabras consiste en utilizar un diccionario predefinido y asignar un valor binario o de frecuencia a cada palabra en función de si aparece o no en el documento. Por ejemplo, si el diccionario contiene 20 000 palabras, cada documento se representa como un vector de 20000 posiciones, y la asignación binaria se puede estipular como que en nuestro vector de características la primera característica es igual a 1 si el mensaje de correo electrónico contiene la palabra “a”, de lo contrario, esta característica es 0, la segunda característica es igual a 1 si el mensaje de correo electrónico contiene la palabra “aaron”, de lo contrario, esta característica es igual a 0, …, la característica en la posición 20000 es igual a 1 si el mensaje de correo electrónico contiene la palabra “zulu”, de lo contrario, esta característica es igual a 0. Repitiendo el procedimiento anterior para cada mensaje de correo electrónico de la colección, lo que da 10000 vectores de características (cada vector tiene una dimensionalidad de 20000) y una etiqueta (“spam”/”no spam”).

Este proceso convierte datos no estructurados (texto) en datos estructurados y numéricos, aptos para el aprendizaje automático.

Codificación de la salida o etiqueta

Las etiquetas, si son categóricas, deben transformarse en valores numéricos para que el algoritmo pueda utilizarlas.

Por ejemplo, algunos algoritmos requieren números como 0 (para representar la etiqueta “no spam”) y 1 (para representar la etiqueta “spam”). En otros casos, como la máquina de vectores de soporte (SVM), este algoritmo requiere que la etiqueta positiva (en nuestro caso, “spam”) tenga el valor numérico +1 y que la etiqueta negativa (“no spam”) tenga el valor -1.

Esta codificación es fundamental, ya que muchas funciones matemáticas que definen el modelo requieren que la variable objetivo sea numérica.

Modelado y espacio de características

Una vez representados, los vectores de características pueden interpretarse como puntos en un espacio de alta dimensión.

En el ejemplo anterior, cada correo se ubica en un punto de un espacio de 20000 dimensiones. El objetivo del algoritmo es aprovechar el conjunto de datos y encontrar una frontera de decisión que separe correctamente los puntos de clases diferentes. En modelos lineales, esta frontera es un hiperplano que separe ambas clases con el mayor margen posible, definido por:

w⋅x − b = 0

donde:

●        w es un vector de pesos, de la misma dimensión que el vector de entrada x.

●        b es un término de sesgo (bias) que ajusta la posición del hiperplano.

Predicción y límite de decisión

En una SVM lineal, la predicción para un nuevo ejemplo se calcula como y=sign(w⋅x−b). Por lo tanto, para predecir si un mensaje de correo electrónico es spam o no utilizando un modelo SVM, hay que tomar el texto del mensaje, convertirlo en un vector de características, multiplicar este vector por w, restar b y tomar el signo del resultado. Si el valor es positivo, el ejemplo se asigna a la clase +1. Si es negativo, se asigna a la clase –1.

La frontera que separa las clases se denomina límite de decisión. Este límite puede ser lineal (hiperplano recto) en modelos lineales o no lineal cuando se aplican funciones de transformación (kernels).

Una vez entrenado y validado el modelo, este puede utilizarse para inferir la variable objetivo en datos nuevos, es decir, en ejemplos que no se utilizaron durante el entrenamiento. Este proceso, denominado inferencia, constituye el objetivo fundamental del aprendizaje automático: aprender modelos a partir de ejemplos para luego aplicarlos automáticamente sobre nuevos datos.

Optimización del margen

Un principio clave de las SVM y otros clasificadores es un problema de optimización, maximizar el margen, definido como la distancia entre el límite de decisión y los ejemplos más cercanos de cada clase. Cuanto mayor sea el margen, mayor es la separación entre clases y mejor es la capacidad de generalización del modelo (predecir correctamente en datos nuevos).

Matemáticamente, maximizar el margen equivale a minimizar la norma euclídea de w:

min∥w∥                sujeto a                               yi(w⋅xi−b)≥1,    i=1,...,N

El proceso de construcción del modelo se denomina entrenamiento. Para vectores de características bidimensionales, el problema y la solución se pueden visualizar como se muestra en la siguiente figura. Los círculos azules y naranjas representan, respectivamente, ejemplos positivos y negativos, y la línea dada por wx-b =0 es el límite de decisión.

Ejemplo de un modelo SVM para un vector de características bidimensional.

Geométricamente, las ecuaciones w⋅x-b = 1 y w⋅x- b = -1 definen dos hiperplanos paralelos, como se ve en la figura. La distancia entre estos hiperplanos viene dada por 2∥w∥, por lo que cuanto menor sea la norma ∥w∥, mayor será la distancia entre estos dos hiperplanos. Así es como funcionan las máquinas de vectores de soporte. Esta versión concreta del algoritmo construye el denominado modelo lineal. Se denomina lineal porque el límite de decisión es una línea recta (o un plano, o un hiperplano).

Este objetivo de maximizar el margen puede formularse de forma equivalente mediante una función de coste L(θ), que mide la discrepancia entre las predicciones del modelo y las salidas reales del conjunto de entrenamiento:

donde

N es el número de ejemplos de entrenamiento.

l es una función de error puntual (por ejemplo, error cuadrático para regresión o entropía cruzada para clasificación).

El entrenamiento consiste en encontrar los parámetros óptimos θ* que minimicen la función de coste:

θ*=argminθL(θ)

En la práctica, este problema se resuelve mediante métodos analíticos (en casos simples) o, más comúnmente, usando técnicas numéricas iterativas como el descenso por gradiente, que actualiza los parámetros en la dirección que reduce el error:

θ←θ−η ∇θL(θ)

η es la tasa de aprendizaje (learning rate), que controla el tamaño de cada paso de ajuste.

∇θ​L(θ) es el gradiente de la función de coste respecto a los parámetros.

La forma del límite de decisión, la forma en que se calcula algorítmica o matemáticamente a partir de los datos de entrenamiento, diferencia un algoritmo de aprendizaje de otro.

Generalización y robustez

Un modelo bien ajustado con un margen amplio es menos sensible a pequeñas variaciones en los datos de entrada. Esto significa que nuevos ejemplos similares a los de entrenamiento estarán, con alta probabilidad, en el mismo lado del límite de decisión y el modelo cometerá menos errores en datos no vistos.

En otras situaciones menos probables, nuestro modelo cometerá errores, pero como estas situaciones son menos probables, el número de errores será probablemente menor que el número de predicciones correctas. Intuitivamente, cuanto mayor sea el conjunto de ejemplos de entrenamiento, menos probable será que los nuevos ejemplos sean diferentes (y se encuentren en el gráfico lejos) de los ejemplos utilizados para el entrenamiento. Para minimizar la probabilidad de cometer errores en los nuevos ejemplos, el algoritmo SVM, al buscar el margen más grande, intenta explícitamente trazar el límite de decisión de tal manera que se encuentre lo más lejos posible de los ejemplos de ambas clases.

La generalización es la capacidad de un modelo para realizar buenas predicciones en datos que no fueron utilizados durante su entrenamiento. Para medirla, es común reservar una parte de los datos de entrenamiento y “ocultarla” durante el ajuste, usándola después para evaluar el rendimiento.

Un factor esencial para lograr buena generalización es la representatividad de los datos de entrenamiento. Si estos no reflejan adecuadamente la realidad del problema, o si la distribución de los datos futuros difiere significativamente de la de entrenamiento, el rendimiento disminuirá. En tal caso, puede ser necesario reentrenar el modelo con datos más actualizados o equilibrados.

También deben evitarse los sesgos en los datos, ya que se trasladan al modelo. Un sesgo común es el causado por clases desbalanceadas o por la exclusión de ciertos grupos o categorías. Estos sesgos pueden generar predicciones injustas o poco precisas, y conviene identificarlos y corregirlos antes del entrenamiento.

### Lesson 4 - Tipos de tareas

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/ZSWyE5DDY4V0IVvV_1z66eEdByMKcagx</sub>

Tipos de tareas

En el aprendizaje supervisado, el objetivo principal es aprender una función que relacione un conjunto de variables de entrada con una variable de salida u objetivo. Según la naturaleza de esta variable de salida, las tareas supervisadas se clasifican en dos grandes grupos: clasificación y regresión.

Clasificación

En una tarea de clasificación, la variable objetivo adopta valores de un conjunto finito de categorías o clases. El modelo debe asignar a cada instancia de entrada la clase más probable, basándose en los atributos que la describen.  Se busca un modelo que retorne una entre K categorías para una entidad que se representa por variables de m entrada o atributos.

fθ : ℝm → {1,2, …, K}

Si el conjunto de clases tiene únicamente dos categorías posibles, se trata de clasificación binaria (por ejemplo, spam frente a no spam).

Si el número de categorías es mayor que dos, se denomina clasificación multiclase (por ejemplo, reconocimiento de dígitos del 0 al 9).

Ejemplos de problemas de clasificación:

Identificar si un correo electrónico es spam o no spam a partir de descriptores de su contenido y metadatos.

Diagnosticar si una muestra de tejido es benigna o maligna en función de descriptores celulares.

Reconocer la letra del alfabeto que representa una imagen de un gesto de lengua de señas.

En este tipo de tareas, el rendimiento del modelo se evalúa comparando las clases predichas con las reales, calculando métricas como accuracy, precision o recall.

Modelos basados en modelo y modelos basados en instancias

La mayoría de los algoritmos supervisados son model-based (modelo basado en modelo), es decir, generan un modelo a partir de los datos de entrenamiento (por ejemplo, SVM aprende los parámetros w y b). Una vez construido el modelo, los datos originales pueden descartarse. Otros métodos, como k-Nearest Neighbors (kNN), son instance-based (modelo basado en instancias): almacenan el conjunto de entrenamiento y, para clasificar un nuevo ejemplo, buscan las instancias más cercanas en el espacio de características y asignan la clase más frecuente.

Aprendizaje superficial y aprendizaje profundo

La mayoría de algoritmos supervisados son de shallow learning (aprendizaje superficial), es decir, aprenden los parámetros del modelo directamente a partir de las características de entrada. En cambio, el deep learning (aprendizaje profundo) utiliza redes neuronales profundas, donde la mayor parte de los parámetros se aprende a partir de representaciones intermedias (salidas de capas previas), lo que permite modelar relaciones más complejas.

Regresión

En una tarea de regresión, la variable objetivo es numérica y continua. El objetivo del modelo es predecir un valor real a partir de un conjunto de variables predictoras o independientes. Típicamente se llaman variables independientes a las entradas y variables dependientes a la salida.

fθ : ℝm → ℝ

Ejemplos de problemas de regresión:

Predecir el flujo de tráfico de una calle a partir de la información de un vídeo en tiempo real.

Estimar la concentración de un contaminante en el aire basándose en mediciones anteriores.

Pronosticar la intensidad de una llamarada solar en función del brillo y la cantidad de manchas en la corona del Sol.

En estas tareas, el rendimiento se evalúa midiendo la discrepancia entre los valores reales y los predichos, mediante métricas como el error cuadrático medio (MSE) o el error absoluto medio (MAE).

Regresión lineal simple

Se utiliza cuando existe una sola variable independiente (x) para predecir la variable dependiente (y). El modelo se representa como:

y = ax + b

●        a: coeficiente (pendiente)

●        b: intercepto

El objetivo es encontrar los valores de a y b que minimicen el error entre las predicciones y los valores reales, comúnmente usando el criterio de mínimos cuadrados.

Regresión lineal múltiple

Cuando se utilizan dos o más variables independientes para predecir y. El modelo se generaliza como:

y = a1x1 + a2x2 + ⋯ + anxn + b

Este caso es más común en la práctica, ya que la mayoría de problemas reales dependen de múltiples factores. Sin embargo, el uso de más variables requiere cuidado para evitar problemas como la multicolinealidad o el sobreajuste.

En esta unidad se abordarán los modelos de regresión tanto de regresión lineal como de regresión múltiple. En la siguiente unidad, se estudiarán modelos de clasificación.

Clasificación

Regresión

Tipo de salida

Etiqueta discreta (categoría)

Valor numérico continuo

Número de clases

Finitas: binaria (2 clases) o multiclase (≥3 clases)

Infinito (valores reales)

Objetivo

Asignar una clase a una instancia

Estimar un valor numérico para una instancia

Algoritmos típicos

SVM

Árboles de decisión

kNN

Redes neuronales

Regresión lineal

Regresión polinómica

SVR

Métricas de evaluación

Accuracy, precision, recall, F1-score, AUC

Error cuadrático medio (MSE), error absoluto medio (MAE), R²

Naturaleza del problema

Problema de decisión (escoger una categoría)

Problema de estimación (predecir un valor)

¡Fantástico! Has completado este apartado.

### Lesson 5 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/sZt8voNgC7X1AcuKqAULV4D___6Bvabx</sub>

Introducción

La regresión lineal simple es uno de los modelos más antiguos, utilizados y comprendidos dentro del aprendizaje supervisado. Su objetivo es predecir valores numéricos continuos a partir de la relación observada entre una única variable independiente o explicativa y una variable dependiente u objetivo. Esta relación se representa mediante una línea recta, lo que permite modelar de forma sencilla cómo los cambios en la variable independiente afectan a la variable dependiente.

A diferencia de los problemas de clasificación, donde el resultado esperado es una etiqueta discreta, en la regresión el modelo estima un valor real. Por ejemplo, podríamos predecir el precio de una vivienda en función de su superficie, la temperatura de mañana a partir de datos históricos o el peso de una persona según su altura.

En el contexto del aprendizaje automático, la regresión lineal simple utiliza un conjunto de datos etiquetados, pares de ejemplos de entrada y su valor objetivo, para ajustar una línea que minimice la diferencia entre las predicciones y los valores reales. Este ajuste se realiza mediante un proceso de optimización que, tradicionalmente, se basa en el método de mínimos cuadrados.

Además de su simplicidad y facilidad de interpretación, la regresión lineal simple presenta otra ventaja, suele ser menos propensa al sobreajuste (overfitting) que otros modelos más complejos, especialmente cuando se cumplen sus supuestos estadísticos. No obstante, es importante comprender sus limitaciones, ya que solo captura relaciones lineales y su rendimiento depende en gran medida de la calidad y representatividad de los datos.

### Lesson 6 - Concepto y fundamentos matemáticos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/M6Bjquya0SzWzEBtJZe9A08wbDOPsXDH</sub>

Concepto y fundamentos matemáticos

En un modelo de regresión lineal simple, la relación entre la variable independiente x y la variable dependiente y se expresa como:

y = ax + b + ε

donde:

y: variable dependiente (variable a predecir).

x: variable independiente (el predictor).

a: pendiente de la recta (slope), que indica el cambio esperado en y por cada unidad de cambio en x. Es el peso (weight) de la función.

b: intercepto o término constante, que representa el valor esperado de y cuando x=0. Es el sesgo (bias) de la función.

ε: término de error o perturbación, que recoge todos los factores no explicados por el modelo.

En aprendizaje automático se suele escribir con la siguiente nomenclatura, donde w son los pesos y b el sesgo:

y = wixi + b

A continuación, se presenta un ejemplo sobre la relación entre el peso de un automóvil (en miles de kilogramos) y su eficiencia de combustible (en km por litro). Se tiene el siguiente conjunto de datos:

Kilogramos en miles (función)

km por litro (etiqueta)

3.5

18

3.69

15

3.44

18

3.43

16

4.34

15

4.42

14

2.37

24

Si se trazan estos puntos como vector de característica representado en un espacio, se obtiene el siguiente gráfico. En el gráfico, se aprecia que a medida que aumenta el peso del vehículo, la eficiencia en km por litro tiende a disminuir, lo que sugiere una relación lineal negativa entre ambas variables:

Peso del automóvil (en kg) en comparación con la clasificación de km por litro.

El objetivo es encontrar los valores óptimos de a y b que hagan que la recta se ajuste lo mejor posible a la nube de puntos formada por los datos.

Sobre los datos anteriores, se podría crear un modelo propio dibujando una línea de mejor ajuste a través de los puntos:

Una línea de mejor ajuste trazada a través de los datos de la figura anterior.

En términos algebraicos, el modelo se definiría como

●       y: km por litro, el valor que se quiere predecir.

●       a: pendiente de la línea.

●       x:  kg, valor de entrada.

●       b:  intersección en y.

Esta posible línea de ajuste para estos datos tiene la forma: y′=(−4.6)(x1)+34. El sesgo es 34 (intercepto) y el peso es -4.6 (pendiente). Esto significa que, por cada incremento de una unidad en el peso (en miles de kg), la eficiencia disminuye en aproximadamente 4.6 km por litro. El modelo se podría usar para hacer predicciones. Por ejemplo, con este modelo, para un automóvil que pese 3.2 miles de kg (x=3.2x): y′ = (−4.6)(3.2) + 34 = 19.28. El modelo estima una eficiencia de 19.28 km por litro.

Con el modelo, un automóvil de 3200 kg tiene una eficiencia de combustible prevista de 19.28 km por litro.

Una vez que se ha planteado la ecuación general de la recta y se ha interpretado la pendiente y el intercepto en el contexto del problema, el siguiente paso es determinar qué valores de estos parámetros producen la línea que mejor se ajusta a los datos reales. Dado que no basta con dibujar una recta de forma intuitiva y arbitraria, es necesario un criterio matemático que cuantifique el ajuste del modelo y que permita optimizar los parámetros para minimizar las diferencias entre los valores observados y los valores predichos.

### Lesson 7 - Ajuste del modelo

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/EoDcJtSEo-Brd_0KAC-FoCWtuFWAk9zB</sub>

Ajuste del modelo

En estadística, las diferencias entre los valores reales (yi) y los valores predichos (y′i) para cada valor observado ( xi) se denominan residuos y se calculan como:

ei=yi−y′i

En el contexto del aprendizaje automático, a estos residuos se les denomina errores, y se evalúan mediante una función de pérdida (loss function), que es una medida numérica de qué tan incorrectas son las predicciones del modelo. La función de pérdida mide la distancia entre las predicciones del modelo y las etiquetas reales, y el objetivo del entrenamiento es minimizar esta pérdida para mejorar el rendimiento del modelo.

Existen varias formas de definir esta distancia. En regresión lineal, las más comunes son:

Pérdida L1 (MAE, Mean Absolute Error): utiliza el valor absoluto de los errores, penalizando todos por igual, lo que la hace más robusta frente a valores atípicos.

Error absoluto medio (MAE): Es el promedio de las pérdidas de L1 en un conjunto de N ejemplos.

Pérdida L2 (MSE, Mean Squared Error): eleva al cuadrado los errores, lo que penaliza más severamente los errores grandes y hace que el modelo tienda a acercarse más a los valores atípicos.

Error cuadrático medio (ECM): Es el promedio de las pérdidas de L2 en un conjunto de N ejemplos.

La diferencia funcional entre la pérdida L1 y la pérdida L2 (o entre el MAE y el MSE) es la elevación al cuadrado. Cuando la diferencia entre la predicción y la etiqueta es grande, elevar al cuadrado hace que la pérdida sea aún mayor. Cuando la diferencia es pequeña (menor que 1), elevar al cuadrado hace que la pérdida sea aún menor.

Método de mínimos cuadrados

En la práctica, el método de mínimos cuadrados ordinarios (Ordinary Least Squares, OLS), utiliza precisamente la pérdida L2 como criterio de ajuste. Este método parte de la idea de que la mejor recta es aquella que minimiza la suma de los cuadrados de los errores entre las predicciones y los valores reales.

donde:

y′i=a+bxi

Elevar al cuadrado los residuos tiene varias ventajas:

Elimina los signos negativos (para que errores positivos y negativos no se cancelen).

Penaliza más los errores grandes que los pequeños, lo que tiende a producir un ajuste más equilibrado

Regresión lineal con los valores reales y residuos o errores indicados, tanto positivo como negativo. La pérdida son las flechas dibujadas desde los puntos de datos hacia el modelo. Las flechas muestran qué tan lejos están las predicciones del modelo de los valores reales.

Con la línea de mejor ajuste anterior, se calcula la pérdida L2 para un solo ejemplo. A partir de la línea de mejor ajuste, se obtuvieron los siguientes valores para el peso=-4.6 y el sesgo=34. Si el modelo predice que un automóvil de 2370 kg rinde 23.1 km por litro, pero en realidad rinde 26 km por litro, se calcula la pérdida de L2 de la siguiente manera: L2 = (yi−y′i)2 = (26−23.1)2 = 8.41. En este ejemplo, la pérdida L2 para ese único dato es de 8.41.

Cuando se hace para varios valores, el método de mínimos cuadrados busca que la suma de los cuadrados de estos residuos sea lo más pequeña posible:

Fórmula del método de mínimos cuadrados

Este método, además, es matemáticamente conveniente, ya que su derivada es continua y permite obtener soluciones en forma cerrada. Así, el valor óptimo de a y b se obtiene derivando la función objetivo respecto a ambos parámetros y resolviendo el sistema resultante.

Desde la perspectiva del aprendizaje automático, esta suma de cuadrados puede dividirse entre el número de observaciones para obtener el Error Cuadrático Medio (MSE), que es la función de pérdida más habitual en regresión lineal. El objetivo del entrenamiento es encontrar los valores de pendiente a e intercepto b que minimicen este MSE. El MSE se explicará en mayor profundidad en el apartado de métricas de evaluación.

Partimos de la función objetivo:

Fórmula de la función objetivo

Se derivan las expresiones parciales respecto a a y b, y se igualan a cero:

Fórmulas de las derivadasde las expresiones partciales

Resolviendo este sistema de ecuaciones, se obtienen:

Fórmula del sistema de ecuaciones resuelto

donde xˉ y yˉ son las medias de las variables.

La interpretación de los valores obtenidos es la siguiente:

Pendiente a: mide el cambio promedio en y por cada unidad de incremento en x.

Si a>0, existe una relación positiva: al aumentar x, y tiende a aumentar.

Si a<0, existe una relación negativa: al aumentar x, y tiende a disminuir.

Si a=0, no existe relación lineal entre las variables.

Intercepto b: es el valor esperado de y cuando x=0. Su interpretación depende del contexto y, en algunos casos, puede no tener sentido práctico (por ejemplo, si x=0 es un valor imposible en el dominio del problema).

Regresiones lineales con, a la izquierda, pendiente positiva indicando que hay una correlación positiva y, a la derecha, pendiente negativa, indicando una correlación negativa.

En resumen, el método de mínimos cuadrados puede entenderse como, en estadística, minimizar la suma de los cuadrados de los residuos y, en aprendizaje automático, minimizar la función de pérdida L2 o MSE para obtener los parámetros óptimos.

Decidir la función de pérdida a usar puede depender del conjunto de datos y de la forma en que se desee controlar ciertas predicciones. La mayoría de los valores de atributos de un conjunto de datos suelen encontrarse dentro de un rango distinto. Por ejemplo, los automóviles suelen pesar entre 900 y 2500 kg, y rinden entre 3 y 30 km por litro. Un automóvil de 3600 kg o uno que rinde 160 km / l se consideran valores atípicos, ya que están fuera del rango típico.

Un valor atípico (outlier) también puede referirse a qué tan alejadas están las predicciones de un modelo de los valores reales. Por ejemplo, 1360 kg se encuentra dentro del rango de peso típico de un automóvil, y 17 km/l se encuentra dentro del rango de eficiencia de combustible típico. Sin embargo, un automóvil de 1360 kg que rinde 64 km/l sería un valor atípico en términos de la predicción del modelo, ya que este predeciría que un automóvil de 1360 kg rendiría alrededor de 32 km/l.

Cuando se elija la mejor función de pérdida, hay que tener en cuenta cómo se quiere que el modelo trate los valores atípicos. Por ejemplo, el MSE desplaza el modelo más hacia los valores atípicos, mientras que el MAE no lo hace. La pérdida L2 genera una penalización mucho mayor para un valor atípico que la pérdida L1. Por ejemplo, las siguientes imágenes muestran un modelo entrenado con MAE y un modelo entrenado con MSE. La línea roja representa un modelo completamente entrenado que se usará para hacer predicciones. Los valores atípicos están más cerca del modelo entrenado con MSE que del modelo entrenado con MAE:

1 de 2

Ajuste mediante descenso de gradiente

Aunque el método de mínimos cuadrados proporciona una solución exacta para los parámetros a y b en regresión lineal simple, en la práctica no siempre es la opción más eficiente o viable. Cuando el número de variables es muy grande, los datos no caben en memoria, o el modelo es más complejo y no tiene solución analítica, se recurre a métodos iterativos de optimización. Uno de los más utilizados en aprendizaje automático es el descenso de gradiente (Gradient Descent).

El descenso de gradiente es una técnica matemática que busca, de forma iterativa, los pesos y el sesgo que producen el modelo con la pérdida más baja. El procedimiento sigue estos pasos:

Inicializar el peso y el sesgo con valores aleatorios cercanos a cero.

Calcular la pérdida con los valores actuales de peso y sesgo.

Calcular la dirección en la que se deben mover estos valores para reducir la pérdida (esto se hace a través del cálculo del gradiente de la función de pérdida).

Actualizar el peso y el sesgo moviéndolos una pequeña cantidad en la dirección de descenso.

Repetir este proceso hasta que la pérdida no pueda reducirse más de forma significativa.

El descenso de gradientes es un proceso iterativo que encuentra los pesos y sesgos que producen el modelo con la pérdida más baja.

Este proceso se conoce como iterativo porque, en lugar de calcular directamente los parámetros óptimos, se aproxima a ellos poco a poco. La magnitud de los ajustes en cada iteración está controlada por la tasa de aprendizaje (learning rate), un hiperparámetro que debe elegirse con cuidado, demasiado alta puede impedir la convergencia, y demasiado baja puede hacer que el entrenamiento sea muy lento.

Durante el entrenamiento, es habitual observar una curva de pérdida, que muestra cómo cambia el valor de la función de pérdida a lo largo de las iteraciones. En una convergencia típica, la pérdida disminuye rápidamente en las primeras iteraciones y luego se reduce más lentamente hasta estabilizarse. Este punto de estabilización indica que el modelo ha encontrado un mínimo de la función de pérdida.

Curva de pérdida que muestra el modelo que converge alrededor de la marca de la iteración 1000.

En el caso de la regresión lineal, la función de pérdida es convexa, lo que significa que tiene un único mínimo global. Esto garantiza que, siempre que el aprendizaje esté bien configurado, el descenso de gradiente encontrará los valores óptimos de peso y sesgo.

Si se representa la función de pérdida en tres dimensiones, peso en el eje X, sesgo en el eje Y y pérdida en el eje Z, la superficie resultante tendrá forma de cuenco. Durante el descenso de gradiente, los parámetros se mueven desde un punto inicial (generalmente alto en la superficie) hacia el fondo del cuenco, que corresponde al menor valor de pérdida posible.

Superficie de pérdida que muestra su forma convexa.

Un modelo lineal converge cuando alcanza este mínimo. En ese punto, iteraciones adicionales apenas cambian los parámetros, ya que el gradiente es prácticamente cero. Es importante destacar que mínima pérdida no significa pérdida cero, sino el valor más bajo posible dado el conjunto de datos y el modelo.

Por ejemplo, para un conjunto de datos de eficiencia de combustible en función del peso del vehículo, el descenso de gradiente podría encontrar que el peso óptimo es −5.44 y el sesgo óptimo es 35.94, con una pérdida mínima de 5.54. Estos parámetros definen la línea que mejor se ajusta a los datos y que, según la función de pérdida elegida, proporciona el mejor equilibrio entre todas las observaciones.

Modelo graficado con los valores de peso y sesgo que producen la pérdida más baja.

En resumen, mientras que OLS resuelve el problema en un solo paso mediante fórmulas, el descenso de gradiente lo resuelve de forma progresiva, lo que lo convierte en una técnica fundamental para entrenar modelos de aprendizaje automático a gran escala y en contextos donde la optimización analítica no es factible.

Hiperparámetros

En el contexto del aprendizaje automático, los hiperparámetros son valores que el usuario establece antes del entrenamiento y que controlan diferentes aspectos del proceso de optimización. A diferencian de los parámetros del modelo, como los pesos y el sesgo, que el algoritmo calcula automáticamente durante el entrenamiento.

En regresión lineal entrenada mediante descenso de gradiente, los hiperparámetros más relevantes son:

●        Tasa de aprendizaje (learning rate)

●        Tamaño del lote (batch size)

●        Número de épocas (epochs)

Tasa de aprendizaje

La tasa de aprendizaje es un número real positivo que determina la magnitud de los pasos que da el algoritmo en cada actualización de parámetros. Es el factor que multiplica al gradiente durante el descenso, controlando cuánto se ajustan los pesos y el sesgo en cada iteración.

Si es demasiado baja, el modelo converge muy lentamente, requiriendo muchas iteraciones. Si es demasiado alta, el modelo puede no converger, ya que los parámetros “rebotan” alrededor del mínimo o incluso divergen. El valor adecuado permite una convergencia rápida y estable.

Tamaño del lote

El tamaño del lote indica cuántos ejemplos se utilizan para calcular el gradiente antes de actualizar los parámetros.

Lote completo (batch gradient descent): usa todos los datos de entrenamiento para una sola actualización por época. Es más estable, pero lento con conjuntos de datos grandes.

Descenso de gradiente estocástico (SGD): usa un solo ejemplo por actualización. Es rápido por iteración, pero introduce mucho ruido en la función de pérdida.

SGD con minilotes (mini-batch gradient descent): usa un subconjunto de ejemplos (mayor que 1 y menor que el tamaño del conjunto completo). Equilibra estabilidad y velocidad, y es el método más utilizado en la práctica.

 Lote completo en comparación con minilote

Un tamaño de lote pequeño se comporta de forma similar a SGD, mientras que uno grande se aproxima al descenso de gradiente por lote completo.

Épocas

Una época (epoch) equivale a un pase completo por todo el conjunto de entrenamiento. Generalmente se requieren varias épocas para que el modelo converja.

Ejemplo: si un conjunto tiene 1000 ejemplos y el tamaño del lote es 100, se necesitan 10 iteraciones para completar una época.

La elección del número de épocas es empírica, demasiadas pueden llevar a sobreajuste (overfitting), y muy pocas pueden dejar el modelo subentrenado (underfitting).

Tipo de lote

Cuándo se actualizan los parámetros

Ejemplo con 1,000 datos y 20 épocas

Lote completo

Una vez por cada época

20 actualizaciones

SGD

Una vez por cada ejemplo

20,000 actualizaciones

Mini-batch (100 ejemplos)

Una vez por lote

200 actualizaciones

La configuración adecuada de la tasa de aprendizaje, el tamaño de lote y el número de épocas es clave para obtener un entrenamiento eficiente y un modelo con buen rendimiento. Estos hiperparámetros se determinan habitualmente mediante experimentación y validación sobre datos no usados en el entrenamiento.

A continuación, un ejemplo sencillo de cómo estimar los coeficientes de una regresión lineal simple utilizando scikit-learn en python:

import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de ejemplo
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Variable independiente
y = np.array([2, 3, 4, 6, 8])  # Variable dependiente

# Crear y ajustar el modelo
modelo = LinearRegression()
modelo.fit(x, y)

# Coeficientes
pendiente = modelo.coef_[0]
intercepto = modelo.intercept_

print(f"Pendiente (a): {pendiente}")
print(f"Intercepto (b): {intercepto}")

# Predicción
x_nuevo = np.array([[6]])
y_pred = modelo.predict(x_nuevo)
print(f"Predicción para x=6: {y_pred[0]}")

En este vídeo se explica, con un ejemplo, cómo se crea en python un modelo de regresión lineal simple, comenzando con la carga los datos y su transformación para el formato requerido por la librería usada:

Reproducir Vídeo

En el siguiente vídeo se usa el modelo creado para mostrar la regresión lineal calculada con los datos de entrenamiento gráficamente y realizar predicciones con este modelo:

Reproducir Vídeo

### Lesson 8 - Limitaciones y supuestos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/4DoYrw6fDL0eu2wWLw3wuPEMPNt6v6hc</sub>

Limitaciones y supuestos

La regresión lineal simple se basa en un conjunto de supuestos que, si no se cumplen, pueden afectar seriamente la validez de las estimaciones y predicciones. Estos supuestos forman parte del marco teórico del modelo y permiten que las inferencias y conclusiones sean fiables.

Supuesto de linealidad

Se asume que la relación entre la variable independiente x y la variable dependiente y es lineal, matemáticamente: y=ax+b. Si la relación real es no lineal, el modelo lineal no capturará adecuadamente la tendencia, generando errores sistemáticos.

Se puede diagnosticar con visualizaciones como gráficos de dispersión de x e y para la inspección visual o con gráficos de residuos enfrentados a los valores ajustados, si se observa un patrón curvo, la relación podría no ser lineal.

Supuesto de independencia

Se asume que las observaciones son independientes entre sí, es decir, que el valor de la variable dependiente para una observación no está influenciado por el valor que adopta en otra observación distinta. Este supuesto garantiza que cada dato aporte información nueva y no redundante al ajuste del modelo.

Cuando no se cumple el supuesto de independencia, las estimaciones de los coeficientes pueden seguir siendo no sesgadas, pero las inferencias estadísticas (como los intervalos de confianza o las pruebas de hipótesis) dejan de ser válidas, ya que se subestima la verdadera variabilidad de los errores.

Supuesto de homocedasticidad

Se asume que la varianza de los errores es constante para todos los valores de x (homocedasticidad). Si la varianza cambia (por ejemplo, los residuos son más dispersos para valores grandes de x), existe heterocedasticidad, lo que afecta la validez de las pruebas de hipótesis y los intervalos de confianza.

Se puede diagnosticar con visualizaciones como gráfico enfrentando residuos y valores ajustados, si la dispersión de los residuos aumenta o disminuye con el valor ajustado, hay heterocedasticidad.

Supuesto de independencia de errores

Se asume que los errores son independientes entre sí. Este supuesto es especialmente crítico en series temporales, donde puede existir correlación entre errores consecutivos (autocorrelación).

Se puede diagnosticar con análisis visuales de los residuos a lo largo del tiempo.

Supuesto de normalidad de los residuos

Se asume que los errores siguen una distribución normal con media cero. Este supuesto es importante para que las pruebas de significancia de los coeficientes sean válidas.

Se puede diagnosticar visualmente con histogramas de residuos. O con la prueba de Shapiro–Wilk o Kolmogorov–Smirnov para evaluar la normalidad.

Limitaciones del modelo

Aunque la regresión lineal simple es intuitiva y computacionalmente eficiente, presenta limitaciones:

Solo modela relaciones lineales; no captura patrones complejos sin transformaciones o variables adicionales.

Sensible a valores atípicos (outliers), que pueden distorsionar la estimación de a y b.

Requiere que los supuestos anteriores se cumplan para obtener estimaciones confiables.

Antes de confiar en los resultados de una regresión lineal simple, es fundamental diagnosticar los supuestos mediante análisis gráficos y pruebas estadísticas. En la práctica profesional, este paso suele ser tan importante como el cálculo de los coeficientes del modelo.

¡Fantástico! Has completado este apartado.

### Lesson 9 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/GyfIVHAivi6QP2cwd3-Nl1HbCahHbH7E</sub>

Introducción

La Regresión Lineal Múltiple (RLM) es una extensión natural de la regresión lineal simple que permite analizar la relación entre una variable dependiente continua y dos o más variables independientes. Este modelo es especialmente útil cuando el fenómeno a estudiar no puede ser explicado satisfactoriamente con un solo predictor, sino que depende de múltiples factores que interactúan entre sí.

En la práctica, gran parte de los problemas de predicción y análisis en ciencia de datos involucran múltiples variables predictoras: el precio de una vivienda depende de su superficie, número de habitaciones, ubicación, antigüedad, etc.; el rendimiento académico de un estudiante puede estar influido por las horas de estudio, el nivel socioeconómico, la calidad docente y la motivación personal.

La RLM permite cuantificar el efecto de cada predictor manteniendo constantes los demás, de forma que se pueda aislar la influencia específica de cada uno. Sin embargo, con esta mayor capacidad de modelado también aparecen nuevos retos, como la selección de variables relevantes y la detección de relaciones redundantes o colineales entre predictores.

### Lesson 10 - Concepto y fundamentos matemáticos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/89D_L4AeNbIgVgRlx__t6NOo-5p4qolb</sub>

Concepto y fundamentos matemáticos

En su formulación general, un modelo de regresión lineal múltiple extiende el modelo lineal simple para incluir varios predictores y se expresa como:

y = a1x1 + a2x2 + ⋯ + anxn + b + ε

donde:

y: variable dependiente o respuesta que queremos predecir.

x1,x2,…,xn: variables independientes o predictores.

a1,a2,…,an​: coeficientes de regresión, que indican cuánto cambia y por un incremento unitario en el predictor correspondiente, manteniendo los demás predictores constantes.

b: intercepto, valor de y cuando todas las variables independientes son cero.

ε: término de error o perturbación aleatoria, que recoge la influencia de factores no incluidos en el modelo.

En notación matricial, el modelo puede escribirse como:

y = Xa + ε

donde:

 y: vector n×1 con los valores observados de la variable dependiente.

X: matriz n×(p+1) que contiene las observaciones de los predictores, incluyendo una columna inicial de unos para el intercepto.

a: vector (p+1)×1 con los coeficientes del modelo.

ε: vector n×1 con los términos de error.

Estimación de los coeficientes

El objetivo sigue siendo encontrar los parámetros que minimicen una función de pérdida, normalmente el Error Cuadrático Medio (MSE), equivalente a minimizar la suma de los cuadrados de los residuos. Esto es exactamente el mismo criterio visto en regresión lineal simple, pero aplicado a un vector de parámetros en lugar de a un único valor de pendiente.

En forma matricial, el método de mínimos cuadrados proporciona la solución:

a′ = (XTX)−1XTy

La interpretación de los coeficientes aj es:

Si aj>0,  incremento en y cuando xj​ aumenta una unidad, manteniendo el resto de variables constantes.

Si aj<0, disminución en y cuando xj​ aumenta una unidad, manteniendo el resto de variables constantes.

Si aj≈0, el predictor xj​ no tiene un efecto lineal significativo sobre y en presencia de los demás predictores.

En cuanto al entrenamiento, si se utiliza un procedimiento iterativo como el descenso de gradiente, el cálculo del gradiente y la actualización de parámetros se realizan de forma análoga a la regresión simple, pero considerando simultáneamente todos los coeficientes.

Una diferencia clave respecto a la regresión simple es que, con varios predictores, puede aparecer multicolinealidad, que afecta a la estabilidad y a la interpretación de los coeficientes. Este aspecto se desarrolla más adelante.

En este ejemplo se carga el dataset Boston Housing que contiene información sobre viviendas en Boston y sus características (número de habitaciones, índice de criminalidad, distancia a centros de trabajo, etc.). Se ajusta un modelo de regresión lineal múltiple usando LinearRegression() de scikit-learn para estimar los coeficientes aj y el intercepto b. Y se evalúa la presencia de multicolinealidad mediante el cálculo del Factor de Inflación de la Varianza (VIF). Si VIF > 5, posible problema de colinealidad moderada, si VIF > 10, colinealidad severa.

# 1. Importar librerías
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm

# 2. Cargar dataset Boston Housing
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target  # Variable dependiente (precio medio de la vivienda)

# 3. Variables predictoras (X) y variable objetivo (y)
X = df.drop('MEDV', axis=1)
y = df['MEDV']

# 4. Ajustar el modelo de Regresión Lineal Múltiple
model = LinearRegression()
model.fit(X, y)

print("Intercepto (b):", model.intercept_)
print("Coeficientes (a_j):")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.4f}")

# 5. Calcular el Factor de Inflación de la Varianza (VIF)
X_with_const = sm.add_constant(X)  # Añadir término independiente para statsmodels
vif_data = pd.DataFrame()
vif_data["Variable"] = X_with_const.columns
vif_data["VIF"] = [variance_inflation_factor(X_with_const.values, i)
                   for i in range(X_with_const.shape[1])]

print("\nFactor de Inflación de la Varianza (VIF):")
print(vif_data)

Si observamos un VIF muy alto en la variable TAX, podría indicar que está fuertemente correlacionada con otra como RAD (índice de accesibilidad radial), lo que reduciría la interpretabilidad de sus coeficientes. Ante este escenario, podríamos eliminar una de las variables.

### Lesson 11 - Selección de variables

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/eVQyO0KlWazgPMJRlQPI7-FOAQ_KhiGz</sub>

Selección de variables

En un modelo de regresión lineal múltiple, el objetivo no es únicamente ajustar la ecuación, sino también determinar qué predictores realmente aportan información relevante para explicar la variable respuesta.  Incluir variables irrelevantes o redundantes no solo aumenta la complejidad del modelo, sino que también puede degradar su capacidad de generalización.

Seleccionar las variables adecuadas tiene varios beneficios:

Mejora la interpretabilidad: un modelo con pocos predictores es más fácil de explicar y comunicar.

Reduce el riesgo de sobreajuste: al disminuir el número de parámetros, se minimiza la probabilidad de que el modelo capture ruido en lugar de patrones reales.

Optimiza el rendimiento computacional: modelos más simples requieren menos tiempo de entrenamiento y menos memoria.

Existen varias estrategias para identificar qué predictores incluir:

Correlación simple

Calcular el coeficiente de correlación de Pearson entre cada predictor xj y la variable dependiente y.

Predictores con una correlación muy baja (cercana a cero) pueden no aportar valor, aunque hay que tener cuidado: una baja correlación marginal no implica necesariamente irrelevancia si existen interacciones con otros predictores.

Análisis de significancia estadística

Una vez ajustado un modelo preliminar, se pueden analizar los valores p de los coeficientes aj​.

Valores p menores que un umbral común (0.05) suelen indicar que el predictor contribuye significativamente a explicar la variabilidad de y.

Selección paso a paso (stepwise)

Procedimientos como forward selection (agregar variables una por una) o backward elimination (eliminar variables menos significativas) permiten construir modelos parsimoniosos basados en criterios estadísticos como el AIC o BIC.

Regularización

Métodos como Lasso y Ridge introducen penalizaciones que pueden reducir el impacto de predictores irrelevantes e incluso eliminar algunos de ellos (en el caso de Lasso).

En la práctica, la selección de variables es un equilibrio entre criterios estadísticos, conocimiento del dominio y viabilidad de obtención de los datos.

### Lesson 12 - Multicolinealidad

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/lwhAuFqW8SXMo2la97yTBmnYx9QJVSlh</sub>

Multicolinealidad

En un modelo de Regresión Lineal Múltiple, se asume que los predictores x1,x2,…,xn​ son independientes entre sí. Cuando dos o más predictores están fuertemente correlacionados, se produce multicolinealidad, un problema que puede afectar seriamente la interpretación y estabilidad del modelo.

La multicolinealidad ocurre cuando un predictor xj puede expresarse (casi) como una combinación lineal de otros predictores. Esto implica que parte de la información que aporta un predictor ya está contenida en otro(s), lo que provoca redundancia. Las consecuencias de la multicolinealidad pueden ser:

Coeficientes inestables: pequeños cambios en los datos pueden generar grandes variaciones en los estimadores aj.

Pérdida de interpretabilidad: se dificulta determinar la influencia individual de cada predictor.

Inflación de errores estándar: los intervalos de confianza para los coeficientes se vuelven más amplios, dificultando la detección de significancia estadística.

Existen varias técnicas para diagnosticar este problema:

Matriz de correlaciones

○        Calcular la correlación entre cada par de predictores.

○        Valores absolutos cercanos a 1 indican una alta correlación lineal.

Factor de Inflación de la Varianza (VIF)

○        Para cada predictor xj​, se ajusta un modelo de regresión donde xj​ es la variable dependiente y el resto de predictores son las variables independientes.

○        Se calcula:

Fórmula del factor de inflación de la varianza (VIF)
 donde Rj2 es el coeficiente de determinación de ese modelo auxiliar.

○        Valores típicos de referencia:

■        VIF = 1 → no hay colinealidad.

■        1 < VIF < 5 → colinealidad moderada.

■        VIF > 5 → preocupación.

■        VIF > 10 → colinealidad severa.

Posibles soluciones:

Eliminar variables redundantes: si dos predictores están muy correlacionados, considerar eliminar uno de ellos.

Combinar variables: crear un nuevo predictor que resuma la información de varios (por ejemplo, un índice o promedio).

Regularización: aplicar métodos como Ridge o Lasso, que penalizan la magnitud de los coeficientes y ayudan a mitigar el problema.

### Lesson 13 - Comparación con regresión simple

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/Mo6ObkGQbx--0CADnqdd1RnOkD2T-B-s</sub>

Comparación con regresión simple

La regresión lineal simple y la regresión lineal múltiple comparten la misma base matemática y los mismos supuestos estadísticos, pero se diferencian en el número de variables explicativas incluidas en el modelo y en la complejidad de interpretación y ajuste.

Característica

Regresión Lineal Simple

Regresión Lineal Múltiple

Número de predictores

1 variable independiente

2 o más variables independientes

Forma de la ecuación

y = ax + b + ε

y = a1x1 + a2x2 + ⋯ + anxn + b + ε

Interpretación de coeficientes

Única pendiente: cambio en y por unidad de x

Cada pendiente: cambio en y por unidad de xj manteniendo las demás variables constantes

Riesgo de multicolinealidad

No existe

Puede aparecer si los predictores están correlacionados

Capacidad predictiva

Limitada si la variable seleccionada no captura toda la variabilidad de y

Mayor capacidad predictiva al incorporar más información relevante

Complejidad

Baja

Alta (más supuestos que verificar y riesgo de sobreajuste)

A continuación, se presenta un ejemplo comparativo empleando el conjunto de datos Boston Housing, evaluando el coeficiente de determinación (R2) obtenido en cada caso.

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import pandas as pd

# Cargar el dataset
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target

# División en train y test
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    df[['RM']],  # Variable simple: número medio de habitaciones
    df['MEDV'],
    test_size=0.2,
    random_state=42
)

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    df.drop('MEDV', axis=1),
    df['MEDV'],
    test_size=0.2,
    random_state=42
)

# Modelo simple
model_s = LinearRegression()
model_s.fit(X_train_s, y_train_s)
r2_simple = model_s.score(X_test_s, y_test_s)

# Modelo múltiple
model_m = LinearRegression()
model_m.fit(X_train_m, y_train_m)
r2_multiple = model_m.score(X_test_m, y_test_m)

print(f"R² modelo simple: {r2_simple:.4f}")
print(f"R² modelo múltiple: {r2_multiple:.4f}")

El modelo de regresión múltiple suele ofrecer un R2 más alto que el modelo simple, ya que incorpora más predictores y, por tanto, explica una mayor proporción de la varianza de la variable dependiente. Sin embargo, un R2 alto no garantiza una mejor generalización; un exceso de predictores puede llevar a sobreajuste. La evaluación final debe considerar métricas adicionales y validación cruzada para comprobar la robustez del modelo.

### Lesson 14 - Supuestos y diagnóstico

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/8AZqAUAQB9HHwT3PaeSGL1-RViXzTAwe</sub>

Supuestos y diagnóstico

Al igual que en la regresión lineal simple, la regresión lineal múltiple requiere que se cumplan ciertos supuestos estadísticos para que los estimadores obtenidos mediante mínimos cuadrados sean no sesgados, eficientes y consistentes. Sin embargo, debido a la presencia de múltiples predictores, el diagnóstico y verificación de estos supuestos adquiere una importancia aún mayor.

Linealidad

Se asume que la relación entre la variable dependiente y cada variable independiente es lineal, manteniendo las demás constantes.

Se recomienda representar los residuos frente a cada predictor, la ausencia de patrones sistemáticos indica cumplimiento del supuesto.

Independencia de errores

Los términos de error (ε) deben ser independientes entre sí.

En datos temporales, se pueden emplear gráficos de residuos en función del tiempo o aplicar pruebas como Durbin-Watson.

Homocedasticidad

La varianza de los residuos debe ser constante en todo el rango de predicciones.

Se puede diagnosticar con la representación gráfica de los residuos frente a los valores ajustados permite detectar heteroscedasticidad (patrones en forma de cono o abanico). También puede utilizarse el test de Breusch-Pagan.

Normalidad de los residuos

Los errores deben seguir una distribución normal con media cero.

Se puede diagnosticar visualmente con la representación de histogramas o pruebas como Shapiro-Wilk o Kolmogorov-Smirnov.

Ausencia de multicolinealidad

Los predictores no deben estar fuertemente correlacionados entre sí, ya que esto puede distorsionar las estimaciones de los coeficientes y su significancia estadística.

Se puede diagnosticar con el cálculo del Factor de Inflación de la Varianza (VIF).

VIF=1: ausencia de colinealidad.

 1<VIF<5: colinealidad moderada.

VIF>5: posible problema.

VIF>10 problema grave que requiere intervención.

import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Cargar datos de ejemplo
boston = load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
y = boston.target

# Calcular VIF
X_with_const = sm.add_constant(X)
vif_data = pd.DataFrame()
vif_data["Variable"] = X_with_const.columns
vif_data["VIF"] = [variance_inflation_factor(X_with_const.values, i)
                   for i in range(X_with_const.shape[1])]

print(vif_data)

Un VIF alto sugiere que la variable correspondiente está altamente correlacionada con otras variables del modelo.

En caso de multicolinealidad grave, se recomienda eliminar variables redundantes o combinar predictores correlacionados.

El incumplimiento de uno o varios supuestos puede provocar:

Estimaciones sesgadas de los coeficientes.

Incremento de la varianza de los estimadores.

Pérdida de capacidad predictiva.

Por ello, antes de interpretar los resultados o utilizar el modelo para predicciones, es fundamental realizar un análisis de diagnóstico completo y, si es necesario, aplicar transformaciones o ajustar el conjunto de predictores para garantizar la validez del modelo.

En este vídeo se explica, con un ejemplo, cómo se crea en python un modelo de regresión lineal multivariable, comenzando con la carga los datos y su transformación para el formato requerido por la librería usada:

Reproducir Vídeo

En el siguiente vídeo se usa el modelo creado para mostrar la regresión lineal calculada con los datos de entrenamiento gráficamente y realizar predicciones con este modelo:

Reproducir Vídeo
¡Fantástico! Has completado este apartado.

### Lesson 15 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/l9B1SjXsVSv9vOnywMtyGV_j18m_5yoe</sub>

Introducción

La evaluación de modelos de regresión es una etapa fundamental en el proceso de modelado, ya que permite cuantificar la capacidad predictiva y la calidad del ajuste alcanzado. El objetivo principal es disponer de herramientas objetivas para comparar diferentes modelos y seleccionar aquel que ofrezca un equilibrio óptimo entre precisión, simplicidad y capacidad de generalización.

Un modelo que predice con exactitud sobre los datos de entrenamiento, pero presenta un rendimiento deficiente sobre datos nuevos, es un modelo sobreajustado. Por este motivo, la evaluación debe considerar tanto la calidad del ajuste como la capacidad de extrapolar resultados a observaciones no utilizadas en el entrenamiento.

Para este fin, se utilizan métricas cuantitativas que miden el error de predicción y el grado en que las variables explicativas logran explicar la variabilidad de la variable objetivo. Algunas métricas evalúan la magnitud media del error, otras penalizan errores grandes de forma más severa, y otras estiman la proporción de varianza explicada por el modelo. La elección de la métrica adecuada depende del contexto, de la escala de la variable objetivo y del objetivo analítico planteado.

### Lesson 16 - Métricas comunes

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/7NNyxgR2bbU3yvS6ZG4X-pmTiv9v126t</sub>

Métricas comunes

Error cuadrático medio (MSE, Mean Squared Error).

Una de las métricas más utilizadas es el Error Cuadrático Medio (MSE, Mean Squared Error), que calcula el promedio de los cuadrados de las diferencias entre los valores reales y las predicciones del modelo. La fórmula es:

Fórmula del error cuadrático medio (MSE)

En esta expresión, yi​ representa el valor real para la observación i y y′i su valor predicho. Al elevar al cuadrado las diferencias, los errores positivos y negativos no se cancelan entre sí, y además se penalizan más los errores grandes. Esto hace que el MSE sea muy útil cuando se quiere dar mayor importancia a las predicciones con grandes desviaciones respecto a la realidad.

Un valor de MSE igual a cero indicaría un ajuste perfecto, algo poco común en la práctica. Un MSE bajo indica que, en promedio, las predicciones están próximas a los valores reales, mientras que un valor alto sugiere un ajuste deficiente. No obstante, su principal limitación es que el resultado se expresa en unidades cuadradas, lo que dificulta la interpretación directa en la escala original de la variable dependiente.

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_real, y_pred)
print("MSE:", mse)

Por ejemplo, si se predicen precios de viviendas y el MSE = 25, esto significa que, en promedio, la diferencia entre el valor real y el valor predicho, elevada al cuadrado, es de 25 euros². El hecho de que esté en unidades cuadradas (euros²) dificulta su interpretación directa, porque no expresa un error en euros, sino en euros al cuadrado.

Para solventar este problema, se utiliza con frecuencia la Raíz del Error Cuadrático Medio (RMSE, Root Mean Squared Error)

Raíz del Error Cuadrático Medio (RMSE, Root Mean Squared Error)

La Raíz del Error Cuadrático Medio (RMSE, Root Mean Squared Error) es la raíz cuadrada del MSE:

Fórmula de la raíz del error cuadrático medio (RMSE)

El RMSE conserva la sensibilidad a los errores grandes propia del MSE, pero sus valores están en la misma unidad y escala que la variable objetivo, lo que facilita su interpretación. Esto significa que los errores grandes tienen un peso mayor en el cálculo, ya que antes de promediar se elevan al cuadrado.

Siguiendo el ejemplo anterior, si el MSE = 25 euros², su raíz cuadrada sería RMSE = 5 €. Esto indica que, en promedio, la desviación típica de las predicciones respecto a los valores reales es de unos 5 euros por vivienda, es decir, que en promedio, el modelo se equivoca en unos 5 euros por vivienda respecto a su valor real. Sin embargo, es importante notar que este promedio está sesgado hacia arriba por errores grandes, ya que estos influyen más en la métrica.

import numpy as np
rmse = np.sqrt(mean_squared_error(y_real, y_pred))
print("RMSE:", rmse)

Error Absoluto Medio (MAE, Mean Absolute Error)

Otra métrica muy empleada es el Error Absoluto Medio (MAE, Mean Absolute Error), definido como el promedio del valor absoluto de las diferencias entre predicciones y valores reales:

Fórmula del error absoluto medio (MAE)

En este caso, al no elevar al cuadrado los errores, todos se ponderan de forma proporcional a su magnitud. Esto hace que el MAE sea más robusto frente a valores atípicos que el MSE o el RMSE, ya que no se amplifica la influencia de errores muy grandes. Además, sus valores se expresan en la misma unidad que la variable dependiente, lo que facilita su interpretación.

Un MAE bajo indica que, en promedio, las predicciones están cerca de los valores reales en la misma unidad de medida de la variable objetivo.

Por ejemplo, si en un conjunto de predicciones la mayoría de los errores están en torno a 5 €, pero hay un error puntual de 30 €, el RMSE aumentará de forma notable debido a ese valor atípico, mientras que el MAE apenas se verá afectado. Si el MAE = 5 €, esto significa que, en promedio, el modelo se equivoca en 5 euros por vivienda, independientemente de si hay algún error muy grande o muy pequeño.

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_real, y_pred)
print("MAE:", mae)

Coeficiente de Determinación (R2)

Además de medir el error, es habitual cuantificar cuánto de la variabilidad de la variable dependiente es explicada por el modelo. Para ello se emplea el Coeficiente de Determinación (R2), definido como:

Fórmula del coeficiente de determinación

El R2 toma valores entre 0 y 1, donde 0 indica que el modelo no explica ninguna variabilidad y 1 representa un ajuste perfecto. Un R2 de 0,85, por ejemplo, significa que el 85% de la variación observada en la variable dependiente es explicada por las variables independientes incluidas en el modelo. Sin embargo, el R2 tiende a aumentar con la inclusión de más predictores, incluso aunque estos no aporten información relevante, lo que puede inducir a error en la evaluación del modelo.

from sklearn.metrics import r2_score
r2 = r2_score(y_real, y_pred)
print("R^2:", r2)

Para corregir este problema, se utiliza el Coeficiente de Determinación Ajustado (Rˉ2).

Coeficiente de Determinación Ajustado (Rˉ2)

El Coeficiente de Determinación Ajustado (Rˉ2) introduce una penalización en función del número de predictores y el tamaño de la muestra:

Fórmula del coeficiente de determinación ajustado

Aquí, k es el número de variables explicativas y n el número de observaciones. El Rˉ2 solo aumentará si la nueva variable mejora el ajuste más de lo que se esperaría por azar, lo que lo convierte en una herramienta útil para comparar modelos con diferente número de predictores y evitar la sobreparametrización.

n = len(y_real)
k = 2  # número de predictores del modelo
r2_adj = 1 - (1 - r2) * (n - 1) / (n - k - 1)
print("R^2 ajustado:", r2_adj)

Interpretación de métricas

El MSE y el RMSE son métricas sensibles a errores grandes, el MAE es más robusto frente a valores atípicos, el R2 mide la capacidad explicativa global del modelo y el Rˉ2 añade una corrección que ayuda a prevenir interpretaciones erróneas cuando se incluyen variables innecesarias. La elección de la métrica adecuada dependerá de las características del problema, la escala de la variable objetivo y el tipo de error que se desee minimizar.

El MSE y el RMSE son especialmente útiles cuando se quiere penalizar de forma severa los errores grandes, pero son más sensibles a valores atípicos. El MAE, en cambio, proporciona una visión más estable del error medio cuando se sospecha la presencia de outliers. El R2 permite entender la capacidad explicativa del modelo, pero debe complementarse con el Rˉ2 para evitar interpretaciones erróneas al incluir predictores irrelevantes.

En la práctica, es recomendable utilizar varias métricas de forma conjunta. Por ejemplo, un modelo puede tener un R2 alto pero un RMSE elevado, lo que indicaría que, aunque explica bien la variabilidad, comete errores grandes en casos concretos. Por otro lado, un MAE bajo con un R2 moderado puede señalar que el modelo predice de forma consistente pero no captura toda la variabilidad posible.

¡Fantástico! Has completado este apartado.

### Lesson 17 - Conclusiones de la unidad

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/UvseO-BVUzuy5PqT739LMfr9mlQydxwU</sub>

Conclusiones de la unidad

A lo largo de esta unidad se han desarrollado los fundamentos conceptuales y prácticos de los modelos de regresión dentro del aprendizaje supervisado. Se ha comenzado con una introducción general a los modelos de regresión, enmarcándolo en el contexto más amplio de la predicción de valores numéricos a partir de datos etiquetados, y diferenciándolo de otras tareas como la clasificación.

La primera parte de la unidad se ha centrado en la regresión lineal simple, abordando su formulación matemática, la interpretación de sus parámetros y el procedimiento para estimarlos mediante el método de mínimos cuadrados. El contenido teórico se ha complementado con un ejemplo práctico que ha permitido visualizar cómo, a partir de datos, es posible ajustar una recta de predicción y utilizarla para estimar nuevos valores.

A continuación, se ha presentado la regresión lineal múltiple como extensión del modelo simple. Se han detallado su formulación, la interpretación de los coeficientes y los criterios para la selección de variables, además de profundizar en el problema de la multicolinealidad y en cómo detectarla y corregirla. Este apartado también ha incorporado un ejemplo práctico en Python para mostrar la implementación y análisis del modelo en un caso con múltiples predictores, destacando las diferencias clave frente a la regresión simple.

La parte final de la unidad se ha dedicado a la evaluación de modelos de regresión. Se han revisado las métricas más utilizadas, explicando no sólo cómo se calculan, sino también cómo interpretarlas y en qué casos cada una resulta más adecuada. El análisis comparativo ha permitido entender que no existe una métrica única para todos los contextos, y que la evaluación debe adaptarse a las características del problema y a los objetivos del modelo.

Nota final:

Una de las principales tareas dentro del aprendizaje supervisado es la regresión, cuando los datos de salida están etiquetados y son valores continuos. La selección adecuada de predictores, la detección de multicolinealidad y la interpretación de las métricas de error son pasos esenciales para garantizar modelos robustos y útiles. Con los conocimientos adquiridos en esta unidad, se cuenta con una base sólida para crear modelos de regresión y adaptarlos a problemas más complejos.

●        Diferenciar la regresión y la clasificación.

●        Comprender la regresión lineal simple.

●        Comprender la regresión lineal multivariable.

●        Conocer las diferentes métricas de evaluación.

¡Felicidades! Has finalizado la unidad. Y ahora, ¡a por las prácticas!


## Recursos y enlaces

- [Unidad 3. Modelos de regresión (Aprendizaje supervisado I).](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/KWHD4sXEzpFyNzxa9IsUJ9Jpz0xQWKjn)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/mZzoI043M_WKyqgQlevSAmTLjMA2ggKe)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/H9K_4soYIMREtTh_yFZHs58D8TcfKKBG)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/ZSWyE5DDY4V0IVvV_1z66eEdByMKcagx)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/sZt8voNgC7X1AcuKqAULV4D___6Bvabx)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/M6Bjquya0SzWzEBtJZe9A08wbDOPsXDH)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/EoDcJtSEo-Brd_0KAC-FoCWtuFWAk9zB)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/4DoYrw6fDL0eu2wWLw3wuPEMPNt6v6hc)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/GyfIVHAivi6QP2cwd3-Nl1HbCahHbH7E)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/89D_L4AeNbIgVgRlx__t6NOo-5p4qolb)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/eVQyO0KlWazgPMJRlQPI7-FOAQ_KhiGz)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/lwhAuFqW8SXMo2la97yTBmnYx9QJVSlh)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/Mo6ObkGQbx--0CADnqdd1RnOkD2T-B-s)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/8AZqAUAQB9HHwT3PaeSGL1-RViXzTAwe)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/l9B1SjXsVSv9vOnywMtyGV_j18m_5yoe)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/7NNyxgR2bbU3yvS6ZG4X-pmTiv9v126t)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_AAUI_A/content/_739330_1/scormcontent/index.html#/lessons/UvseO-BVUzuy5PqT739LMfr9mlQydxwU)