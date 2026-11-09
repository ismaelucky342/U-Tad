# 2609_INSD4_VICO_A

**SCORM:** _739878_1
**URL del contenido:** https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormdriver/indexAPI.html

## Contenido

### Lesson 1 - Introducción y objetivos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/c7Gk8Jmf92vk-MVtXiiUxZ5SlfH7Dllv</sub>

PASE A LA LECCIÓN
Unidad 2. Filtrado de imágenes y detección de características básicas.
Introducción y objetivos

Introducción

En esta unidad didáctica nos adentraremos en las técnicas fundamentales de procesamiento de imágenes digitales orientadas a mejorar la calidad de los datos visuales y a extraer información relevante de las imágenes. Tras haber estudiado los fundamentos sobre formación de la imagen, modelos de color, histograma, etc., ahora pasamos a abordar operaciones de filtrado y detección de características que son esenciales para aplicaciones más avanzadas. En particular, aprenderemos cómo modificar imágenes mediante filtros para suavizar ruido o resaltar detalles, así como métodos para detectar estructuras significativas como bordes y puntos clave.

Comenzaremos presentando la operación de convolución sobre imágenes, que constituye la base de muchos filtros. Veremos cómo la convolución permite combinar la intensidad de un píxel con la de sus vecinos mediante una pequeña matriz de coeficientes, a la que llamaremos kernel, logrando efectos diversos dependiendo de dichos coeficientes. A continuación, introduciremos el concepto de dominio frecuencial usando la Transformada de Fourier, el cual nos proporciona una “lectura” de la imagen en términos de frecuencias. Esto nos ayudará a entender qué significa un filtro de paso bajo o de paso alto y cómo actúan sobre las componentes de baja o alta frecuencia de la imagen.

Seguidamente, estudiaremos los filtros de paso bajo (suavizado), que permiten reducir el ruido y suavizar detalles pequeños en la imagen. Veremos cómo estos filtros atenúan las variaciones bruscas, produciendo imágenes más suaves, pero a costa de perder nitidez en bordes y detalles. Para complementar estos filtros, analizaremos los filtros de paso alto, diseñados para resaltar cambios abruptos de intensidad, es decir, detectar bordes o realzar detalles finos, donde analizaremos cómo estos filtros realzan bordes (donde la intensidad cambia rápidamente) ya que precisamente los bordes representan cambios bruscos de intensidad en la imagen.

Más adelante, nos adentraremos en técnicas de filtrado no lineal que, a diferencia de los filtros lineales, aplican reglas diferentes para combinar los píxeles de una vecindad. Veremos filtros para eliminar ruido impulsivo preservando mejor los contornos que un promedio, y filtros más avanzados diseñados para preservar características importantes evitando los artefactos de métodos más simples.

A continuación, estudiaremos en detalle el detector de bordes de Canny, un algoritmo clásico en visión por computador que combina varios de los conceptos que ya hemos estudiado, como son: suavizado, gradiente o umbralización, en una secuencia de pasos optimizados para obtener un mapa de bordes claro y consistente. Analizaremos cada etapa de este algoritmo, desde la reducción de ruido inicial hasta aplicar diferentes técnicas para decidir qué bordes son realmente válidos, entendiendo por qué este método produce típicamente mejores resultados que aplicar un simple filtro de gradiente con un umbral.

Finalmente, abordaremos la detección de puntos clave o punto de interés en imágenes. Estos puntos clave pueden ser esquinas, esquinas u otras estructuras locales distinguibles. Son elementos muy útiles porque capturan información única de la imagen que puede emplearse para tareas como alineamiento de imágenes, reconstrucción 3D o reconocimiento de objetos. Veremos en qué consisten las esquinas desde el punto de vista de la imagen (lugares donde la intensidad varía en múltiples direcciones) y presentaremos métodos de detección que permiten encontrar rápidamente esas esquinas u otros puntos prominentes.

Haz clic para voltear

Convolución en imágenes: filtros aplicados en el dominio espacial

Haz clic para voltear

Imagina que queremos analizar cada píxel de una imagen, pero no de forma aislada, sino teniendo en cuenta los píxeles que lo rodean. La convolución es precisamente la herramienta que nos permite mezclar el valor de un píxel con sus vecinos usando una pequeña tabla de pesos llamada kernel o filtro (3×3, 4×4, 5×5…) para obtener una nueva versión según el filtrado que deseamos. 

Haz clic para voltear

Transformada de Fourier: análisis de imágenes en frecuencia

Haz clic para voltear

La idea clave es que cada imagen digital contiene componentes de baja y alta frecuencia. Las frecuencias bajas corresponden a variaciones suaves en la intensidad (regiones de brillo casi constante o gradientes suaves), mientras que las frecuencias altas corresponden a variaciones bruscas, como las que ocurren en los bordes, texturas finas o ruido. La Transformada de Fourier nos proporciona un espectro donde podemos ver qué tanto de cada frecuencia hay en la imagen.

Haz clic para voltear

Detección de estructuras de interés

Haz clic para voltear

Hasta ahora hemos aprendido a “escuchar” la imagen con filtros: suavizar lo que estorba y realzar lo que importa. El siguiente paso es poner chinchetas donde la imagen nos ofrece anclajes fiables: lugares que resisten pequeños cambios de encuadre, escala o iluminación y a los que podamos regresar más tarde para emparejar, alinear o seguir.

Objetivos

1

Entender la operación de convolución y su papel en el procesamiento de imágenes.

2

Interpretar imágenes en el dominio de la frecuencia mediante la Transformada de Fourier.

3

Diferenciar filtros de paso bajo y paso alto y conocer ejemplos de cada tipo: comprender cómo los filtros de suavizado (paso bajo) reducen ruido y detalles pequeños, y cómo los filtros de realce de bordes (paso alto) destacan las transiciones abruptas para detectar contornos o afinar la imagen.

4

Aplicar filtros lineales clásicos para suavizar imágenes y detección de bordes, entendiendo las ventajas e inconvenientes de cada uno.

5

Conocer técnicas de filtrado no lineal orientadas a preservar detalles importantes.

6

Explicar el algoritmo de detección de bordes de Canny, describiendo cada una de sus etapas.

7

Entender la detección de puntos clave en imágenes, diferenciando qué son esquinas y qué son otros puntos de interés.

¡Comenzamos!

### CONTINUAR CURSO

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/</sub>

CONTINUAR CURSO
INTRODUCCIÓN Y OBJETIVOS
Introducción y objetivos
CONVOLUCIÓN EN IMÁGENES: FILTROS APLICADOS EN EL DOMINIO ESPACIAL
Introducción
Convolución discreta
Parámetros de la convolución
TRANSFORMADA DE FOURIER: ANÁLISIS DE IMÁGENES EN FRECUENCIA
Introducción
Transformada de Fourier. Definición formal
Teorema de la convolución
FILTROS LINEALES
Introducción
Filtros de paso bajo (LPF)
Filtros de paso alto (HP)
FILTRADO NO LINEAL Y PRESERVACIÓN DE BORDES
Introducción
Filtro de la mediana
Filtro de la mediana híbrida
Filtro de la mediana truncada
Filtro bilateral
Filtro de Kuwahara
Filtro Rolling-Guidance
Detector de Bordes de Canny
DETECCIÓN DE ESTRUCTURAS DE INTERÉS
Introducción
Detección de puntos clave o keypoints
Detección de manchas o blobs
Invarianzas
Algoritmos de descripción de imágenes
Descripción de imágenes
CONCLUSIONES
Conclusiones de la unidad
Completado
Completado
Completado
Completado
Completado
Completado

### Lesson 2 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/bXu5SRoVXOovPGRDjCzcLTAD38MltBFK</sub>

Introducción

Imagina que queremos analizar cada píxel de una imagen, pero no de forma aislada, sino teniendo en cuenta los píxeles que lo rodean. La convolución es precisamente la herramienta que nos permite mezclar el valor de un píxel con sus vecinos usando una pequeña tabla de pesos llamada kernel o filtro (3×3, 4×4, 5×5…) para obtener una nueva versión según el filtrado que deseamos. 

¿Cómo aplicaremos la convolución en el ámbito de las imágenes? Vamos a deslizar el filtro por toda la imagen, haciendo que en cada posición multipliquemos “valor del píxel vecino × peso del kernel” y sumemos todo. Ese número, resultado de la suma, sustituirá al valor del píxel central en la imagen filtrada.

Si los pesos son todos positivos y suman 1, obtenemos promedios (suavizado).

Si hay pesos positivos y negativos que se cancelan, realzamos cambios bruscos (bordes, detalles).

Si el patrón del kernel parece una “plantilla”, la salida responde fuerte cuando la imagen tiene ese patrón local.

Aplicar una convolución es, en esencia, combinar información local de forma controlada. Por eso es la base de casi todo el filtrado clásico y de las CNN que estudiaremos más adelante.

¿Todo listo? ¡Empezamos!

### Lesson 3 - Convolución discreta

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/tVv0o47nlQKlpqlXa4-i9vwBM8zYRUp3</sub>

Convolución discreta

En el caso de las imágenes, como hemos visto anteriormente, trabajaremos con una matriz de elementos numéricos, y por lo tanto nos vamos a centrar en convoluciones discretas, ya que son valores puntuales y no valores continuos.

Veámoslo desde un punto de vista matemático. Sean
 e
 dos funciones discretas. Entonces la convolución 1D de ambas funciones se define como,Veámoslo desde un punto de vista matemático. Sean  e  dos funciones discretas. Entonces la convolución 1D de ambas funciones se define como,

¿Cómo podemos interpretar esta fórmula? Tomamos
, lo invertimos, que por eso aparece
,  y lo desplazamos a la posición
, lo multiplicamos término a término con
, y sumamos.

Veamos un pequeño ejemplo. Tomemos
 y
, entonces para la posición

Y de igual manera se puede operar el resto de los elementos de

Como las imágenes con las que nosotros trabajamos son matrices que se componen de dos dimensiones, nos vamos a centrar en la convolución 2D. La convolución 2D es la operación lineal que usamos para “mezclar” una imagen
 con un núcleo o filtro
 y así obtener otra imagen
donde los valores quedan atenuados o realzados. Este el corazón de algunas de las transformaciones que veremos a lo largo de esta unidad.

De nuevo, veámoslo desde un punto de vista matemático. Si llamamos
 a la imagen y
 al kernel, entonces podemos definir una convolución 2D como,

donde
 es cada posición de la imagen de salida, y  es el índice central del kernel (por ejemplo
 para un kernel 3x3). En otras palabras, desplazamos el kernel sobre cada píxel de entrada, multiplicamos cada valor de los píxeles vecinos por el peso correspondiente del kernel, y sumamos todos esos productos para obtener el nuevo valor.

La convolución clásica en 2D “voltea” el kernel antes de barrerlo por la imagen. Muchas librerías implementan correlación (misma idea pero sin volteo) y, salvo por el signo/orientación en filtros derivativos, el uso es análogo.

Veamos algunas de las propiedades que usaremos con las convoluciones,

Linealidad:

Conmutatividad:

Asociatividad:
 se pueden encadenar filtros

Separabilidad: si
 se filtran primero filas y luego columnas.

La versatilidad de la convolución es enorme: con los coeficientes adecuados, un kernel puede producir efectos de suavizado, detección de bordes, realce de contraste, desenfoque de movimiento, eliminación de ruido, etc. Por eso se dice que la convolución permite extraer diferentes características de la imagen según el kernel que usemos. De hecho, en ámbitos más avanzados (como las redes neuronales convolucionales que veremos más adelante) los kernels son aprendidos automáticamente para detectar rasgos específicos. Pero en esta unidad nos centraremos en kernels determinísticos predefinidos y su efecto.

A continuación, se muestra cómo podríamos implementar manualmente una convolución simple en Python para un pixel dado, así como usar las funciones de OpenCV para aplicar un filtro a toda la imagen.

import cv2
import numpy as np

# Cargar una imagen en escala de grises
imagen = cv2.imread('ruta/imagen_entrada.jpg', cv2.IMREAD_GRAYSCALE)

# Definir un kernel de ejemplo
kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]], dtype=np.float32)

# Aplicar convolución 2D usando OpenCV
imagen_filtrada = cv2.filter2D(imagen, ddepth=cv2.CV_32F, kernel=kernel)

# También es posible realizar la convolución "a mano" para un píxel específico:
x, y = 100, 150  # coordenadas ejemplo
region = imagen[y-1:y+2, x-1:x+2]        # extraer región 3x3 alrededor de (x,y)
valor_nuevo = np.sum(region * kernel)   # multiplicar elemento a elemento y sumar
print("Valor original:", imagen[y, x], "Valor filtrado:", valor_nuevo)

En este código, cv2.filter2D se encarga de aplicar el kernel a toda la imagen. Hemos definido un kernel 3x3, con coeficiente central 4 y -1 alrededor, que definiremos más adelante en la unidad, para resaltar cambios bruscos. Luego mostramos cómo podríamos calcular el valor filtrado de un solo píxel  obteniendo su vecindario 3x3 y realizando la operación manualmente (multiplicación elemento a elemento y suma).

### Lesson 4 - Parámetros de la convolución

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/A1DqMKuRfROw3kiTQP8dCfb7Q3yIZb89</sub>

Parámetros de la convolución
Filtro o kernel: la “huella” del operador en el plano imagen

Imaginemos una plantilla pequeña de pesos (una matriz
​, típicamente con tamaños impares como 3×3, 5×5, 7×7). Esa plantilla se superpone sobre cada vecindario de la imagen y dicta cómo combinar los píxeles locales para producir la salida. Esa plantilla es el kernel (o filtro).

Centro: en un kernel impar, el centro es
⌋). Este es el punto dónde cae la salida con al realizar la convolución. Con tamaños pares (4×4, 6×6…) la noción de centro no es clara y suele provocar desplazamientos de media muestra; por eso preferimos tamaños impares para evitar sesgos geométricos.

Separabilidad: algunos kernels 2D se descomponen como producto de dos 1D (horizontal×vertical). Eso reduce coste y suele mejorar estabilidad numérica.

Multi-canal: en procesado clásico aplicamos el kernel canal a canal (p. ej., en RGB lineal o luminancia) para evitar “mezclas raras” de color.

Este gráfico ilustra cómo un kernel se "desliza" sobre una imagen durante la operación de convolución y cómo se calcula cada píxel de la imagen de salida.

Matriz de Entrada: La primera imagen muestra la matriz de píxeles de entrada. El recuadro rojo indica la posición de la "ventana" del kernel en un momento dado. En la convolución, esta ventana se mueve por cada píxel de la imagen de entrada, de izquierda a derecha y de arriba a abajo.

Kernel: La segunda imagen muestra el kernel utilizado. En este ejemplo, es un kernel de promediado 3x3.

Matriz de Salida: La tercera imagen es el resultado de la convolución. Cada píxel en esta matriz de salida se calcula de la siguiente manera:

La ventana del kernel se posiciona sobre el píxel correspondiente en la matriz de entrada.

Se multiplican los valores de los píxeles dentro de la ventana de la matriz de entrada por los valores correspondientes del kernel (multiplicación elemento a elemento).

Se suman todos estos productos.

El resultado de esta suma se convierte en el valor del píxel en la matriz de salida en la posición actual.

Por ejemplo, para calcular el píxel en la posición  de la matriz de salida, el kernel se centra (o se alinea) sobre la región de la matriz de entrada que rodea , se realiza la multiplicación elemento a elemento entre la ventana de la entrada y el kernel, y se suman los resultados para obtener el valor en  de la salida. Este proceso se repite para cada píxel de la matriz de salida.

Este proceso de "deslizamiento" del kernel y el cálculo ponderado en cada posición es fundamental para muchas operaciones de procesamiento de imágenes, desde el suavizado y la detección de bordes hasta el filtrado y el reconocimiento de patrones.

Relleno de bordes o padding: qué hay fuera de la imagen

Cuando el kernel se está aplicando a píxeles que están cerca de la “frontera” de la imagen, se puede salir del borde e intentar coger valores que están “fuera” de rango, necesitamos en este caso  decidir qué valores usa fuera del campo visual.

Imaginemos una matriz de una imagen en la que queremos analizar los píxeles de la “frontera”, que están en la fila 0. Al intentar aplicar un kernel 3×3 ahí, va a intentar acceder a los valores de las filas -1 y -2 para poder sacar los valores de los píxeles vecinos y hacer un promedio. Como bien sabemos, intentar acceder a las filas -1, -2 de un array, nos devolverá un error.

La solución para no cometer este error es el padding, técnica que afecta mucho al resultado de los límites y consiste en añadir, alrededor de la imagen, valores “dummy” (siguiendo diferentes técnicas) evitando así que nos salgamos de fuera de la imagen al aplicar al kernel.

reflect/symmetric (espejo): copia la imagen como si hubiera un espejo en el borde. Suele minimizar halos y discontinuidades, muy buena opción por defecto en suavizados y derivadas.

edge/replicate (replicar): repite el valor del borde. Útil en algunos pipelines, pero crea mesetas que afectan a derivadas.

constant (cero u otro valor): rellena con un valor fijo. Es el más simple y rápido, pero puede introducir bordes artificiales (halos oscuros) con filtros de promedio.

Si la imagen original es de tamaño  y el kernel es de tamaño , la imagen filtrada tiende a ser ligeramente más pequeña (de tamaño
) si no se aplica relleno en los bordes. Esto ocurre porque el kernel no puede sobrepasar los límites de la imagen. El padding también puede usarse para hacer que la imagen de salida tenga el mismo tamaño que la imagen de entrada.

Paso o stride: cada cuánto saltamos al escribir la salida

En implementaciones (como en bibliotecas tipo OpenCV) es posible elegir como manejar el borde de la imagen (rellenando con ceros, replicando el último píxel, usando una reflexión, etc.) así como configurar el stride o paso, que determina la distancia con la que se desplaza el kernel cada vez que se aplica.

El stride (paso) determina la resolución de muestreo de la salida: en lugar de calcular una salida para cada píxel de entrada (usando un stride = 1), podemos saltar de s en s (stride = 2, 3, …). Es, en esencia, una convolución seguida de un submuestreo.

Cabe destacar que para strides mayores a (1, 1) se produce una reducción de dimensiones respecto a la original.

En el siguiente vídeo vamos a ver un par de ejemplos de cómo funciona la convolución y cómo el filtro o kernel, va recorriendo la imagen y cómo la imagen final va apareciendo con los valores calculados mediante la convolución.

Reproducir Vídeo
¡Fantástico! Has completado este apartado.

### Lesson 5 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/c0C_1viyfevMGCtoaVtxUa_pxp-ahVcx</sub>

Introducción

Hasta ahora hemos descrito los filtros en el dominio espacial (es decir, definimos cómo se calcula cada píxel de salida a partir de los píxeles del vecindario en la imagen). Existe otra forma muy poderosa de entender el efecto de un filtro: analizando su acción en el dominio de la frecuencia. Para ello necesitamos introducir la Transformada de Fourier (TF) en 2D aplicada a imágenes. Si en el dominio espacial una imagen es una función
 de intensidades respecto a las coordenadas, su transformada de Fourier
 es otra representación, con otro enfoque sobre la intensidad, donde expresa la imagen como una suma de ondas sinusoidales de diferentes frecuencias y amplitudes. En otras palabras, la transformada de Fourier nos permite descomponer la imagen en oscilaciones de distinto ritmo a lo largo de
 e

La idea clave es que cada imagen digital contiene componentes de baja y alta frecuencia. Las frecuencias bajas corresponden a variaciones suaves en la intensidad (regiones de brillo casi constante o gradientes suaves), mientras que las frecuencias altas corresponden a variaciones bruscas, como las que ocurren en los bordes, texturas finas o ruido. La Transformada de Fourier nos proporciona un espectro donde podemos ver qué tanto de cada frecuencia hay en la imagen.

### Lesson 6 - Transformada de Fourier. Definición formal

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/xZLU6d4KVkdX9EVpcX6naJrqgJJwcUN7</sub>

Transformada de Fourier. Definición formal

Formalmente, la transformada de Fourier continua de una imagen
 se define como:

y su versión discreta (DFT) para imágenes digitalizadas de tamaño
 toma la forma de una doble suma,

Sin embargo, en lugar de centrarnos en la fórmula, vamos a destacar lo que significa
 es una función en el dominio de frecuencia donde cada punto
 representa una frecuencia espacial específica en la dirección horizontal (frecuencia
) y vertical (frecuencia
). El valor
(que será número complejo) nos da la amplitud y la fase con que esa frecuencia está presente en la imagen.

Cuando visualizamos el espectro de Fourier de una imagen, comúnmente representamos la magnitud
. Suele mostrarse en escala logarítmica (porque el rango de valores puede ser muy amplio) y con las frecuencias cero centradas para mayor claridad. En ese tipo de visualización:

El centro de la imagen del espectro corresponde a las frecuencias bajas (u=0, v=0 en el centro, que representan intensidad constante o variaciones muy lentas).

A medida que nos alejamos hacia los bordes de la imagen espectral, aumentan las frecuencias altas (variaciones más rápidas en la imagen original).

Los valores brillantes en el espectro indican qué frecuencias tienen mayor presencia en la imagen original.

### Lesson 7 - Teorema de la convolución

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/2EA4axVu02nlIkfNs1vlMjGa9wMEyJFn</sub>

Teorema de la convolución

Una vez que tenemos el concepto de transformada de Fourier, es importante mencionar el Teorema de Convolución: la convolución en el dominio espacial equivale a la multiplicación en el dominio frecuencial, y viceversa. Es decir, si aplicamos un filtro a una imagen aplicando la convolución con un kernel, eso equivale a tomar la transformada de Fourier de la imagen y multiplicarla por la transformada de Fourier del kernel (adecuadamente ubicada), y luego transformar de vuelta al espacio.

Este principio explica por qué muchos filtros se entienden mejor en frecuencia: por ejemplo, un filtro de paso bajo es aquel cuya representación en frecuencia es una función que deja pasar (multiplica por 1) las frecuencias bajas y atenúa (o multiplica por 0) las altas. En cambio, un filtro de paso alto hará lo opuesto: bloquear las frecuencias bajas (las componentes suaves) y dejar pasar las altas (las variaciones bruscas asociadas a bordes).

Como podemos observar en el gráfico:

La Imagen Original muestra la imagen sin modificar.

La imagen de Convolución Espacial muestra el resultado de aplicar un filtro de detección de bordes directamente mediante la convolución, donde los bordes de la imagen original se vuelven prominentes.

La imagen de Filtrado en Dominio de Frecuencia, en cambio, muestra el resultado de multiplicar las Transformadas de Fourier de la imagen y un kernel, y luego aplicar la Transformada de Fourier Inversa, para poder obtener el resultado de la operación.

Visualmente, la imagen de Convolución Espacial y la imagen de Filtrado en Dominio de Frecuencia son prácticamente idénticas, validándonos el Teorema de la Convolución, demostrando que realizar la operación en el dominio de la frecuencia puede ser computacionalmente más eficiente para ciertos tipos de filtros, especialmente en imágenes grandes.

¡Fantástico! Has completado este apartado.

### Lesson 8 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/N-Te3JUP4om2rELNWo8DGMOyoWztdZab</sub>

Introducción

Al inicio de la unidad hemos definido la convolución como la técnica básica para transformar una imagen teniendo en cuenta su vecindad: deslizamos un pequeño kernel y, en cada posición, combinamos ponderadamente los píxeles de alrededor. Ahora vamos a dar un paso más y a ponerle intención a esa operación. ¿Para qué queremos mezclar vecinos? ¿Qué esperamos conservar y qué estamos dispuestos a sacrificar? De estas preguntas nacen dos familias de filtros lineales que veremos constantemente en visión por computador: los de paso bajo y los de paso alto.

Lo importante aquí no es memorizar kernels, sino entender el efecto: los filtros lineales responden de la misma forma en cualquier lugar de la imagen y combinan píxeles mediante una suma ponderada. Esa regularidad los hace predecibles y eficientes, pero también explica sus límites: un suavizado lineal no “sabe” distinguir entre ruido y el borde de un ojo.

### Lesson 9 - Filtros de paso bajo (LPF)

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/Ps1q4d6OdgrnOAUTpjfL3VvxmDw7GO1P</sub>

Filtros de paso bajo (LPF)

Los filtros de paso bajo son aquellos que dejan pasar las componentes de baja frecuencia de la imagen y atenúan o eliminan las altas frecuencias. En el dominio espacial, su efecto es suavizar la imagen: reducen el ruido de alta frecuencia y promedian variaciones, produciendo una versión más borrosa (menos detallada) de la imagen original. Estos filtros son muy útiles para eliminar ruido aleatorio o detalles irrelevantes antes de analizar una imagen, o para crear efectos de desenfoque.

Filtrado de caja o media

El filtro de media (también llamado filtro de caja o box en inglés) es quizá el más simple de los filtros de suavizado. Su kernel consiste en asignar el mismo peso a todos los píxeles en una vecindad y hacer el promedio. Por ejemplo, un kernel 3x3 de media sería:

Es decir, toma 9 píxeles (el central y sus 8 vecinos inmediatos) y calcula la media aritmética de sus valores. Al reemplazar cada píxel por la media de sus vecinos, la imagen resultante aparece más suave: se han “difuminado” las variaciones locales. Cuanto mayor sea el tamaño del kernel (por ejemplo 5x5, 7x7, etc.), más marcado será el desenfoque ya que se promedian más píxeles.

El principal beneficio del filtro de media es su sencillez y su capacidad de reducir el ruido aleatorio (especialmente si es de tipo granular, alto-frecuencia). Sin embargo, tiene un inconveniente notable: tiende a borrar también los detalles y bordes importantes, porque esos bordes justamente son transiciones de alta frecuencia que el filtro promedio aplana. Por eso decimos que el filtro de caja es "demasiado agresivo": elimina el ruido, pero también difumina todo lo demás. Más adelante veremos filtros más “inteligentes” que suavizan sin difuminar tanto los contornos.

Un punto para tener en cuenta, es que el filtrado de media no preserva bordes: si tenemos un borde nítido (por ejemplo, mitad de la imagen negra y mitad blanca), el promedio generará una transición intermedia gris en la zona del borde, ensanchándolo y haciéndolo menos definido. Por ello, para aplicaciones donde la localización exacta de bordes es importante, el filtro de caja podría no ser la mejor opción.

Implementación del filtro de caja
import numpy as np
import matplotlib.pyplot as plt # Import matplotlib

def box_kernel(k):
    assert k % 2 == 1, "Usa k impar"
    K = np.ones((k, k), np.float32)
    return K / K.size

def _pad2d(img, r, mode='reflect'):
    return np.pad(img, ((r, r), (r, r)), mode=mode)

def box_filter_naive(gray, k=5, padding='reflect'):
    gray = gray.astype(np.float32)
    r = k // 2
    I = _pad2d(gray, r, mode=padding)
    K = box_kernel(k)
    H, W = gray.shape
    out = np.empty_like(gray)
    for y in range(H):
        for x in range(W):
            out[y, x] = np.sum(I[y:y+k, x:x+k] * K)
    return out

gray_image = np.array([[10, 20, 30],
                       [40, 50, 60],
                       [70, 80, 90]], dtype=np.uint8)

filtered_image = box_filter_naive(gray_image, k=7)

plt.figure(figsize=(6, 3))

plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray', vmin=0, vmax=255)
plt.title("Imagen original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray', vmin=0, vmax=255)
plt.title("Imagen filtrada (k=7)")
plt.axis('off')

plt.show()
Filtro Gaussiano

El filtro gaussiano es otro filtro de paso bajo muy utilizado, que realiza también un promedio de los píxeles vecinos, pero con ponderaciones que siguen una distribución Gaussiana. Esto significa que se le da más peso al píxel central y a los vecinos más cercanos, y menos peso a los más lejanos dentro de la ventana. El kernel gaussiano en 2D tiene la forma:

El filtro gaussiano tiene varias ventajas sobre el de caja:

Produce un suavizado más suave y natural, sin introducir discontinuidades abruptas, porque la contribución de los píxeles decae gradualmente con la distancia.

Preserva algo mejor los bordes, en el sentido de que no extiende tanto la influencia de valores de un lado del borde hacia el otro (aunque ojo, cualquier filtro lineal de suavizado difumina bordes hasta cierto punto).

Tiene propiedades matemáticas convenientes: por ejemplo, es separable (podemos aplicar primero un filtro 1D gaussiano horizontal y luego uno vertical para lograr el mismo efecto que un 2D completo, ahorrando cálculo). Además, la convolución de dos gaussianas es otra gaussiana: aplicar dos veces un filtro gaussiano de desviación  equivale a uno solo de desviación . Esto permite escalonar suavizados en etapas sin efectos secundarios raros (solo se "ensancha" la gaussiana efectiva).

La gaussiana teórica es infinita, pero en la práctica dibujamos esta campana en una ventana finita. Si la ventana es demasiado pequeña, se cortan las colas y aparecen sutiles halos en perfiles de borde (como si hubiéramos recortado la campana con tijeras). La regla que nunca falla: haz la ventana lo bastante grande para cubrir
 por cada lado.

Implementación del filtro gaussiano
import numpy as np

def gaussian1d(sigma, radius=None):
    if radius is None:
        radius = int(np.ceil(3*sigma))
    x = np.arange(-radius, radius+1, dtype=np.float32)
    g = np.exp(-0.5*(x/sigma)**2)
    g /= g.sum()             # normaliza (DC = 1)
    return g

def sep_convolve2d(img, krow, kcol=None, padding='reflect'):
    # Reutiliza tu separable: primero horizontal, luego vertical
    krow = np.asarray(krow, np.float32).ravel()
    kcol = krow if kcol is None else np.asarray(kcol, np.float32).ravel()
    cr, rr = len(krow)//2, len(kcol)//2

    def _pad(im, py, px):
        return np.pad(im, ((py, py), (px, px)), mode=padding)

    def _h(im):
        H, W = im.shape
        I = _pad(im, 0, cr)
        out = np.empty_like(im, np.float32)
        for y in range(H):
            for x in range(W):
                out[y, x] = (I[y, x:x+2*cr+1] * krow).sum()
        return out

    def _v(im):
        H, W = im.shape
        I = _pad(im, rr, 0)
        out = np.empty_like(im, np.float32)
        for y in range(H):
            for x in range(W):
                out[y, x] = (I[y:y+2*rr+1, x] * kcol).sum()
        return out

    if img.ndim == 2:
        return _v(_h(img.astype(np.float32)))
    else:
        # procesar por canal
        return np.stack([sep_convolve2d(img[...,c], krow, kcol, padding)
                         for c in range(img.shape[2])], axis=-1)

En términos de atenuación de frecuencias, el filtro gaussiano es prácticamente óptimo: genera la menor distorsión de fase y un decaimiento suave de las altas frecuencias en el espectro, lo que evita la aparición de artefactos visibles en el dominio espacial (por ejemplo, minimiza el ringing o sombras oscilantes alrededor de bordes que producen otros métodos más bruscos).

En el siguiente video vamos a ver mediante un ejemplo interactivo cómo van afectando el tamaño del kernel para el filtro de la caja, y el valor de
 para el filtro Gaussiano, y las diferencias directas que se pueden ver entre ambos filtros.

Reproducir Vídeo

A pesar de sus ventajas, ni el promedio uniforme ni el gaussiano distinguen entre ruido y detalles: ambos tratan toda variación de intensidad por igual (siguiendo sus pesos). Más adelante veremos filtros no lineales que sí distinguen entre un cambio debido a ruido y un cambio debido a un borde real.

Otros filtros de paso bajo

Además de los mencionados, existen otros filtros lineales de paso bajo menos comunes:

Filtro de promedio ponderado arbitrario: en lugar de una gaussiana, podríamos definir pesos específicos. Por ejemplo, un kernel 5x5 que dé más peso a los 4 vecinos inmediatos ortogonales que a los diagonales, etc. Mientras los pesos sumen 1, será un filtro de suavizado (básicamente una variación del promedio).

Filtro de suavizado exponencial: se puede implementar recursivamente, dando más peso a píxeles cercanos al centro con una ley exponencial. Es similar a aplicar un efecto de desenfoque dando pesos decrecientes radialmente de forma exponencial.

Filtro de Butterworth: es un tipo de filtro diseñado originalmente en electrónica, con una respuesta en frecuencia más plana en la banda pasante y una transición suave. Tiene una formulación en frecuencia y se puede aplicar a imágenes calculando su máscara frecuencial o aproximando un kernel espacial.

En general, cuando aplicamos suavizado debemos considerar la relación entre reducción de ruido y pérdida de detalle. Un suavizado muy fuerte elimina más ruido, pero también puede borrar información útil (textura, bordes finos), mientras que uno muy leve quizás no elimine suficiente ruido. La elección del tipo de filtro y su intensidad (tamaño de kernel, sigma, etc.) dependerá de la naturaleza de la imagen y los objetivos que tengamos. Por ejemplo, en preprocesamiento para visión por computador, a menudo se aplica un leve suavizado gaussiano (p.ej. 3x3, sigma ~1) para quitar ruido de sensor antes de detectar bordes, pero no tan fuerte como para desplazar o difuminar esos bordes notoriamente.

### Lesson 10 - Filtros de paso alto (HP)

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/K8ogKdHeglW6hNzTUIJI_x1nfNS8iPPx</sub>

Filtros de paso alto (HP)

Los filtros de paso alto son complementarios a los de paso bajo: están diseñados para resaltar las componentes de alta frecuencia de la imagen, es decir, las variaciones bruscas de intensidad. En una imagen típica, ¿dónde encontramos altas frecuencias? Principalmente en los bordes de los objetos (transiciones fuertes de oscuro a claro o viceversa) y en detalles muy finos o ruido. Por lo tanto, un filtro de paso alto tiende a producir como resultado una imagen donde se destacan los contornos y detalles finos, mientras que las áreas de intensidad relativamente constante quedan oscuras (cerca de cero).

Los filtros de paso alto aproximan operaciones de la derivada sobre la imagen:

Una derivada primera (gradiente) acentúa donde la imagen cambia (bordes).

Una derivada segunda resalta cambios en el gradiente (también útil para bordes, detectando máximos de pendiente).

Mediante la convolución podemos aproximar derivadas discretas mediante kernels.

Filtros basados en el gradiente (primera derivada)

Cuando miramos una fotografía, nuestros ojos no leen números: siguen líneas, perciben cambios, se detienen en bordes. En el lenguaje de la imagen digital, esos bordes son lugares donde la intensidad “sube” o “baja” con decisión. Los filtros de paso alto basados en gradiente se usan precisamente para captar pendientes: detectar dónde la imagen cambia con rapidez y en qué dirección sucede ese cambio.

Imaginemos la ladera de una montaña. Si nos movemos por ella, podemos notar lo inclinado del terreno y hacia dónde apunta la pendiente. La imagen digital es un mapa de alturas (intensidades) y el gradiente será lo que nos dice cuánto cambia la intensidad y hacia dónde cambia.

Esta simple idea tiene consecuencias muy prácticas: si sabemos medir esa pendiente local, podemos dibujar un mapa de contornos (magnitud del gradiente) y además orientar esos contornos (ángulo del gradiente). Con esas dos piezas es posible afinar líneas, decidir qué es borde y qué no.

Un píxel solo no nos cuenta si estamos en una rampa; necesitamos mirar su vecindad. La operación que lo consigue es la que hemos visto, la convolución, junto con un kernel, que actúa como “regla de cálculo” de la pendiente.

El resultado no es una imagen final sino dos mapas:

Un mapa con el cambio en X (izquierda–derecha).

Un mapa con el cambio en Y (arriba–abajo).

A partir de ahí construimos:

Magnitud (qué fuerte es la pendiente) — nuestro “marcador de bordes”.

Orientación (hacia dónde apunta) — el “compás” que nos permitirá afinar.

Pensemos en la imagen
 como una superficie. El gradiente
 es un vector que, en cada píxel, nos dice dos cosas:

Señala hacia dónde crece más rápido la intensidad si se da un paso diminuto.

Su módulo ​​
 nos dice “cuánto” cambia la intensidad al movernos un píxel en la dirección óptima. Cuanto mayor es
, más abrupto es el salto: bordes más fuertes.

La “gran trampa” de los gradientes es el ruido. Derivar en continuo equivale a multiplicar el espectro por una constante. Cuanto más “rápido” oscila algo, más lo amplifica el gradiente. El ruido fino oscila mucho ⇒ sube. Pero ¿cómo lo mitigamos?

Podemos suavizar previamente con un Gaussiano o con cualquier otro filtro de paso bajo, donde podemos reducir el ruido.

Una vez que tenemos el filtro de paso bajo aplicado, aplicamos entonces un filtro de paso alto.

En el siguiente video vamos a ver con un ejemplo visual, por qué debemos aplicar un filtro Gaussiano previo a aplicar cualquier filtro de los que vamos a ver en esta sección.

Reproducir Vídeo

A continuación, vamos a analizar diferentes tipos de filtros de paso alto basados en el gradiente, viendo sus pros y contras.

Prewitt (el minimalista que envejeció regular)

El filtro Prewitt es uno de los primeros filtros de detección de bordes. Se define por dos kernels  separables que aproximan la derivada primera en direcciones horizontal y vertical.

Básicamente,
 toma la diferencia entre la suma de intensidades en la fila de arriba y la fila de abajo de cada vecindad, y
 la diferencia entre la suma de la columna derecha y la izquierda. Cuando se aplica la convolución a la imagen con
, produce valores altos en lugares donde hay un borde horizontal (por ejemplo, una transición de negro a blanco hará
 arriba vs
 abajo, sumando a un valor alto positivo). Inversamente, una transición contraria dará un valor negativo alto (que interpretado en magnitud indica borde también). Similarmente
  reacciona a bordes verticales.

Esta imagen muestra la aplicación de los kernels de Prewitt a una imagen real:

La imagen de Filtro Prewitt_x resalta principalmente los bordes horizontales en la imagen original.

La imagen de Filtro Prewitt_y resalta principalmente los bordes verticales.

La imagen de Magnitud del Gradiente combina los resultados de ambos kernels para mostrar la fuerza total de los bordes, independientemente de su orientación.

Este ejemplo ilustra cómo los kernels de Prewitt actúan como detectores de bordes direccionales y cómo la magnitud del gradiente puede combinarlos para obtener un mapa de bordes general.

El filtro Prewitt es fácil de entender, pero tiene un inconveniente: como usa un promedio simple (1,1,1) arriba y abajo, es susceptible al ruido y no da un peso mayor al píxel central que al extremo de la vecindad. En la siguiente imagen, podemos ver cómo el ruido afecta a la misma imagen anterior, y cómo varía la detección de bordes.

Sobel (el pragmático de 3×3)

El filtro de Sobel es una variante mejorada del Prewitt. En vez de promediar uniformemente, incorpora un ligero suavizado gaussiano en una dirección para reducir el efecto del ruido. Los kernels Sobel horizontales y verticales 3x3 típicos son:

Como se puede observar, el Sobel horizontal
 es similar al Prewitt (
 arriba,
 abajo) pero con los valores de la columna central duplicados en magnitud (
 y
 en el medio). Esto equivale a aplicar la convolución a la imagen primero con un filtro de promedio [1 2 1] verticalmente y luego con [-1 0 1] horizontalmente (o viceversa, dado que es separable).

Esencialmente, Sobel aproxima la derivada del gaussiano: suaviza un poco en la dirección perpendicular al borde antes de calcular la diferencia, reduciendo la sensibilidad al ruido. El Sobel vertical
 hace lo propio en la otra dirección.

Como podemos ver en esta imagen, Sobel tiende a ser ligeramente menos sensible al ruido que Prewitt debido a los pesos en sus kernels. Sin embargo, ambos detectores de bordes simples son significativamente afectados por el ruido de alta frecuencia. Las áreas ruidosas resultan en una alta respuesta del filtro, creando falsos positivos en la detección de bordes. Esto subraya la importancia de aplicar técnicas de suavizado (como filtros Gaussianos) antes de la detección de bordes cuando se trabaja con imágenes ruidosas.

Es interesante notar que los filtros de Sobel detectan bordes, pero no los afinan ni deciden umbrales; solo calculan un mapa de gradiente. Más adelante, el algoritmo Canny tomará estos resultados como punto de partida y los procesará para obtener bordes binarios bien definidos.

Filtro derivada del Gaussiano

Hasta ahora hemos usado máscaras pequeñas (Prewitt, Sobel) para escuchar dónde cambia la imagen. Funcionan bien, pero cuando el ruido se mezcla con texturas finas —granito, pelo, ladrillo— esas máscaras pueden “encender” demasiadas cosas. La Derivada del Gaussiano (∂G) propone otra táctica: primero calmar el paisaje y luego medir la pendiente. En la práctica es como pasar una esponja suave antes de apoyar el nivel: la lectura es más estable.

¿Qué problema resuelve?

Ruido que se hace pasar por borde: al suavizar antes de derivar, los granos aislados dejan de disparar el detector.

Texturas que distraen: al elegir la escala (el tamaño de la esponja, σ), decides qué detalles ignorar y qué contornos mantener.

Consistencia: la misma idea funciona en imágenes a distintas resoluciones; tú solo ajustas σ.

Imaginemos que deslizamos una campana de goma (una Gaussiana) por la imagen. Esa campana da más peso a los vecinos cercanos y menos a los lejanos, “alisando” el terreno. Ahora bien, si miras la pendiente de esa campana mientras la deslizas (su derivada), obtienes un sensor que siente los cambios, pero ya ha hecho oídos sordos a lo pequeñito que no te interesa. Eso es ∂G.

Cómo funciona:

Construimos una campana Gaussiana 1D (en X e Y).

Calculamos su derivada 1D (la pendiente de esa campana).

Filtramos separadamente: para Gx aplicamos ∂G en X y G en Y; para Gy, al revés.

El resultado son gradientes suaves y estables.

Ventajas frente a Sobel:

Sobel incluye un suavizado fijo (1–2–1). ∂G te deja elegir la cantidad exacta (σ) según la escena.

Con ∂G, el suavizado y la derivada forman una pareja coherente: mejor estabilidad y menos artefactos en diagonales finas.

Filtros basados en la segunda derivada o laplaciano

Si los filtros por gradiente controlaban la pendiente de la imagen, los filtros por segunda derivada controlan la curvatura: dónde cambia la pendiente de signo. Esta mirada nos regala bordes centrados, independencia de orientación y, sobre todo, un control de escala muy natural: podemos decidir si queremos ver las arrugas de una hoja o sólo su contorno.

Imaginemos que recorremos una rampa: con el gradiente podemos notar si la intensidad sube o baja y cuánto. Con la segunda derivada notamos dónde la rampa cambia su inclinación. A lo largo de un borde ideal (oscuro → claro), la intensidad primero crece, luego se estabiliza; la segunda derivada pasa de positiva a negativa (o al revés) y cruza por cero en el centro del borde. Ese cruce por cero es la pista que vamos a explotar para localizar contornos de forma muy precisa, incluso cuando no nos preocupa su orientación.

Volvamos a imaginar la imagen
como una superficie. El Laplaciano es la suma de segundas derivadas ortogonales,

En un borde ideal (paso), la segunda derivada cambia de signo al cruzarlo: por eso los cero-cruces del Laplaciano alinean bien contornos; en manchas redondas, el Laplaciano extrema en el centro a la escala “correcta”.

Un kernel Laplaciano típico 3x3 es:

Hay variantes con 4 en el centro y -1 alrededor, etc., pero todas comparten la idea de tener un coeficiente central positivo grande y vecinos negativos sumando su magnitud (de modo que la suma de todos coeficientes es 0). Aplicar este kernel realza los píxeles que son muy diferentes a su entorno promedio.

El Laplaciano destaca bordes sin dirección preferente (detecta cualquier cambio abrupto sin distinguir orientación). Suele producir una imagen donde los contornos aparecen resaltados como líneas brillantes sobre fondo oscuro (o viceversa, dependiendo del signo usado). Sin embargo, es muy sensible al ruido (porque la segunda derivada amplifica fluctuaciones pequeñas), por lo que a menudo se aplica después de un suavizado leve.

¡Fantástico! Has completado este apartado.

### Lesson 11 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/cQfPc_bsuTeAv8lgYaSbc3aPVPJu-8EX</sub>

Introducción

En el apartado anterior aprendimos a modificar bajas y altas frecuencias con filtros lineales. Funcionan bien cuando el objetivo es global —promediar, derivar, realzar—, pero tienen una limitación estructural: tratan por igual cualquier cambio local. Para un filtro lineal, un grano de ruido y el borde del pico del tucán son ambos “alta frecuencia”. Si promediamos, se difumina todo; si derivamos, se exalta todo. ¿Y si quisiéramos suavizar el ruido sin tocar los bordes que nos interesan? Ahí entran los filtros no lineales.

Un filtro es no lineal cuando el nuevo valor de un píxel no es una simple suma ponderada de sus vecinos. En su lugar, utiliza decisiones (comparaciones, medianas, mínimos/máximos, pesos que dependen de la propia imagen, etc.). Esta “inteligencia local” le permite adaptarse al contenido: reacciona de manera distinta si la vecindad parece ruido, borde o textura.

¿Por qué los necesitamos? Porque en visión por computador no siempre queremos “alisar todo” o “resaltar todo”. A menudo necesitamos limpiar la señal y, al mismo tiempo, preservar estructuras (bordes, líneas finas, esquinas) que son las que alimentarán otros métodos más avanzados.

A continuación, veremos varios filtros no lineales comunes en visión por computador: los filtros de la mediana, el filtro bilateral, el filtro de Kuwahara y el Rolling Guidance. Cada uno introduce una estrategia distinta para preservar características de la imagen mientras reduce el ruido.

### Lesson 12 - Filtro de la mediana

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/e7DyggEi5K1OvomP4ocWpaFDU3fvBtAQ</sub>

Filtro de la mediana

El filtro de mediana es probablemente el filtro no lineal más conocido. Su funcionamiento es sencillo: en lugar de promediar los valores del vecindario (como hace el filtro de media), toma el valor mediano. Es decir, ordena todos los valores de intensidad en la ventana alrededor del píxel y selecciona el que queda en la mitad de la lista (la mediana estadística).

Imaginemos una ventana
 que se posa sobre la imagen. La mediana no promedia: ordena los
 valores y se queda con el central. Eso tiene dos efectos inmediatos:

Si hay valores extremos, la mediana los ignora mientras no sean mayoría.

En un borde nítido (dos regiones planas separadas), la mediana elige la mayoría local: no inventa tonos intermedios —preserva el salto—, a diferencia de un promedio que fusila el borde con grises “fantasma”.

Otra propiedad interesante es que la mediana tiende a preservar mejor los bordes que un filtro lineal. Imaginemos un borde nítido: mitad de los píxeles negros, mitad blancos. Un promedio produce una franja gris en medio (borde difuminado). En cambio, la mediana, si la ventana abarca ambos lados, elige uno u otro lado según la mayoría de los píxeles en la ventana. En un borde ideal (paso abrupto), la mediana mantendrá el borde casi en su lugar original en vez de promediarlo. Visualmente, la mediana suele conservar mejor la nitidez de un escalón que el promedio.

Pero tiene una desventaja, al no ser lineal, es menos eficiente computacionalmente (ordenar píxeles en cada ventana tiene un costo mayor). Además, si el ruido no es impulsivo sino, digamos, ruido Gaussiano suave, la mediana no siempre es óptima; podría distorsionar más la imagen en lugar de mejorarla.

### Lesson 13 - Filtro de la mediana híbrida

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/wFbh4wCztqFrQGMxdNu63xCwfPi-Kp1j</sub>

Filtro de la mediana híbrida

La mediana “normal” es fantástica para quitar, pero tiene un problema al que tiende: redondea. Redondea esquinas, adelgaza cruces en T y a veces suaviza más de la cuenta las líneas oblicuas. La mediana híbrida nace para eso: limpiar sin traicionar la geometría. ¿Cómo lo logra? Pidiéndole opinión a dos “jurados” del vecindario —la cruz y las diagonales— y luego tomando una decisión equilibrada con el propio píxel central.

Jurado 1 (la cruz): mira arriba, abajo, izquierda y derecha (más el centro). Es sensible a líneas rectas y bordes alineados con la cuadrícula.

Jurado 2 (las diagonales): mira noreste, noroeste, sureste y suroeste (más el centro). Es sensible a esquinas y a líneas oblicuas.

Cada jurado propone su mediana (su “dictamen”). Y el veredicto del filtro es la mediana de [mediana_cruz, mediana_diagonal, centro]. Esta última “votación” es la clave: si el centro no es un outlier (valor que se sale del patrón esperado), suele sobrevivir; si lo es, lo reemplaza un valor coherente con la estructura local (cruz o diagonal), preservando esquinas y trazos finos.

¿Cuándo usar mediana híbrida?

Ruido impulsivo en escenas con geometría: fachadas, planos, documentos con tipografías y cruces de trazos.

Detalles oblicuos y esquinas que la mediana clásica tiende a “redondear”.

Preproceso antes de detectar bordes cuando hay ruido y no queremos adelgazar contornos reales.

En esta imagen podemos ver cómo estos filtros no lineales son efectivos para eliminar el ruido impulsivo, y cómo el tamaño del kernel y el tipo de filtro de mediana (estándar vs. híbrido) influyen en el resultado final de filtrado, especialmente en la preservación de detalles y bordes.

Cómo se usa

Elige un tamaño de ventana impar (3×3, 5×5 recomendado, 7×7 si el ruido es muy denso).

Para cada píxel:

Calcula la mediana de la cruz (centro + N, S, E, O).

Calcula la mediana de las diagonales (centro + NE, NO, SE, SO).

Calcula la mediana de esos dos resultados y del centro.

Usa ese valor como nuevo píxel.

Esta segunda imagen, podemos ver un zoom en un área de la imagen que contiene una esquina de la rama donde están sujetos los tucanes. Al comparar las imágenes con zoom:

El Original Ruidoso muestra el ruido claramente la esquina.

El resultado aplicando el Filtro de la Mediana 5x5 redondea ligeramente la esquina debido a la operación de la mediana.

El resultado aplicando el Filtro de la Mediana Híbrida 5x5 tiende a preservar mejor la forma original de la esquina, mostrando menos redondeo en la esquina, mientras sigue reduciendo el ruido.

Ejemplo de uso
import numpy as np, cv2

def hybrid_median_filter(gray: np.ndarray, k: int = 5) -> np.ndarray:
    assert k % 2 == 1 and k >= 3, "k debe ser impar y >=3"
    gray = gray.astype(np.float32, copy=False)
    r = k // 2
    pad = cv2.copyMakeBorder(gray, r, r, r, r, cv2.BORDER_REFLECT)

    H, W = gray.shape
    out = np.empty_like(gray)

    for y in range(H):
        for x in range(W):
            yy, xx = y + r, x + r
            patch = pad[yy - r:yy + r + 1, xx - r:xx + r + 1]

            cross = np.concatenate([patch[r, :], patch[:, r]])
            diag1 = patch.diagonal()
            diag2 = np.fliplr(patch).diagonal()

            m_cross = np.median(cross)
            m_diag  = np.median(np.concatenate([diag1, diag2]))
            center  = patch[r, r]

            out[y, x] = np.median([m_cross, m_diag, center])

    return np.clip(out, 0, 255).astype(np.uint8)

# Ejemplo
img = cv2.imread("entrada.png", cv2.IMREAD_GRAYSCALE)
hmf = hybrid_median_filter(img, k=5)
cv2.imwrite("salida_hmf_5x5.png", hmf)

### Lesson 14 - Filtro de la mediana truncada

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/KIv0FfPc6ov0BKtmyLF-VzEY0gSJqr5F</sub>

Filtro de la mediana truncada

Hay veces en los que la mediana clásica hace “lo correcto” y con una ventana pequeña la imagen queda limpia. Pero hay otras —escáner con polvo, compresión con bloques, cámaras baratas en interiores— en los que no hay un solo intruso: hay muchos valores extremos en la misma vecindad. Si subes el tamaño de la mediana para vencerlos, la foto empieza a verse plana, como encerada. La mediana truncada entra justo ahí: recorta lo más extremo antes de decidir, para limpiar con firmeza, pero sin alisar de más.

Pensemos en una reunión ruidosa. Antes de tomar una decisión, podemos pedir a los más estridentes que hagan silencio un momento. Entonces, con el resto, decides. Eso hace la mediana truncada:

Recorta (temporalmente) los valores más bajos y altos del vecindario.

Con lo que queda —el cuerpo de la distribución— calcula una mediana representativa.

El resultado no se deja arrastrar por los extremos, pero tampoco aplasta las texturas como lo haría subir “a lo bruto” el tamaño de ventana.

La forma que vamos a ver cómo se aplica este filtro es,

Ordenamos los valores de la ventana

Corta un porcentaje α de los más bajos y otro α de los más altos (por ejemplo, 10% y 10%).

Toma la mediana de lo que queda.

¿Cuándo debemos usarla?: cuando encontremos ruido denso o varios outliers en la misma ventana. Ocurre en escenas donde la mediana clásica oscila porque en cada parche “mandan” 2–3 valores extremos.

Este ejemplo vamos a ver la diferencia del efecto de los tres filtros de mediana diferentes (Estándar, Híbrida y Truncada) aplicados una imagen con un nivel de ruido bastante grande.

Imagen Original con Ruido: Vemos la imagen con un ruido añadido. Con este nivel de ruido, podemos observar, una degradación significativa de la imagen original.

Mediana Estándar: Con un ruido tan alto, el filtro de mediana estándar sigue siendo efectivo para eliminar la mayoría de los puntos de ruido, pero debido a la alta densidad de ruido, puede empezar a afectar más a los bordes y detalles finos, causando un mayor suavizado.

Mediana Híbrida: Con el ruido más alto, la mediana híbrida tiende a mantener una mejor preservación de las estructuras lineales y esquinas en comparación con la mediana estándar del mismo tamaño, aunque la alta densidad de ruido puede seguir afectando su rendimiento.

Mediana Truncada:

Con
 se descarta un 10% de los valores extremos. Con un ruido muy alto, este nivel de truncamiento puede no ser suficiente para eliminar todos los puntos de ruido, y algunos artefactos pueden persistir.

Con
 se descarta un 30% de los valores extremos. Un valor de  más alto descarta más valores atípicos, lo que puede resultar en una mejor supresión de ruido con densidades de ruido muy altas. Sin embargo, un  muy alto también puede empezar a eliminar píxeles que son parte de detalles finos pero que tienen valores inusuales, llevando a una pérdida de detalle. Comparando estos resultados, se puede ver el compromiso entre la eliminación de ruido y la preservación de detalles en presencia de ruido muy alto.

Utilizando este zoom, nos permite realizar una comparación más cercana de cómo cada filtro afecta a los bordes, texturas y pequeños detalles bajo una condición de ruido muy adversa. Así podemos comparar la nitidez de los bordes y la presencia de artefactos de ruido residual en cada resultado. La elección del filtro y del valor de  en la mediana truncada se vuelve crucial para equilibrar la eliminación de ruido con la preservación de la información de la imagen.

### Lesson 15 - Filtro bilateral

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/crfTnYgFBpuP2p3HpmS2GfUkXS_5JRsv</sub>

Filtro bilateral

Imaginemos que queremos “pasar una mopa” a la imagen para quitar el grano… pero no queremos que esa mopa se meta a través de los bordes. Con un Gaussiano clásico, todo lo que esté cerca promedia, aunque pertenezca a otro objeto con tono distinto: los contornos se lavan. El bilateral cambia las reglas: promedia solo con los vecinos que están cerca y son parecidos en intensidad. Resultado: las regiones planas quedan limpias, los bordes siguen vivos.

El bilateral es un filtro con dos candados:

Candado espacial (sigma espacial,
): “¿estás cerca de mí?” Vecinos lejanos pesan poco, igual que en un Gaussiano. Controla el radio de influencia.

Candado de intensidad (sigma de rango,
): “¿te pareces a mí?” Si el vecino tiene intensidad muy distinta, su peso cae casi a cero. No cruza bordes.

Solo cuando un vecino está cerca y se parece, entra al promedio. Esa doble condición es la que preserva fronteras.

Aquí podemos ver claramente cómo funciona el proceso del filtrado bilateral, 

Parche Original: Se muestra un fragmento de imagen. El recuadro rojo indica el vecindario del píxel central que se va a filtrar. Vamos a definir el vecindario de “radio “
 del píxel  como los píxeles que están a una distancia menor o igual que
 ,

Pesos Espaciales: Se calcula un peso basado en la distancia euclidiana de cada píxel vecino al píxel central. Los píxeles más cercanos tienen pesos más altos.

Para un mejor acabado, podemos utilizar una función Gaussiana con desviación estándar  , para ajustar los pesos espaciales.

Pesos de Intensidad: Se calcula un peso basado en la diferencia de intensidad entre cada píxel vecino y el píxel central Los píxeles con valores de intensidad similares al píxel central tienen pesos más altos.

Al igual que con los pesos espaciales, podemos utilizar otra función Gaussiana con desviación estándar  , para ajustar los pesos y obtener un mejor.

Pesos Combinados: Los pesos espaciales y de intensidad se multiplican para obtener un peso combinado para cada píxel en el vecindario. Este peso combinado es alto solo para los píxeles que están cerca y tienen una intensidad similar.

Normalización: Los pesos combinados se normalizan para que sumen 1. Primero calculamos la suma de todos los pesos combinados, y esa suma se la dividimos a cada uno de los pesos.

Cálculo del Valor Filtrado: El nuevo valor del píxel central se calcula como la suma ponderada de los valores de los píxeles en el vecindario, utilizando los pesos combinados normalizados.

Pixel de Salida: El valor del píxel central en la imagen de salida se reemplaza por el valor filtrado calculado.

Qué vemos en el esquema:

El Parche Original muestra el fragmento de imagen con el vecindario seleccionado.

El Parche con Píxel Central Filtrado por Bilateral muestra el resultado después de aplicar el filtro al píxel central.

Los gráficos de pesos muestran visualmente cómo se distribuyen los pesos espaciales, de intensidad y combinados dentro del vecindario. Podemos observar, cómo los pesos de intensidad son bajos para los píxeles con valores muy diferentes al píxel central (como el 5 y 15 en este ejemplo, en comparación con el 150 central), lo que ayuda a preservar los bordes.

El filtro bilateral es efectivo para la reducción de ruido mientras preserva los bordes, lo que lo hace popular en fotografía y procesamiento de imágenes para suavizar texturas sin perder detalles importantes. Los parámetros
 y
 controlan cuánto suavizado se aplica y cuánta diferencia de intensidad se considera un borde.

Al comparar los resultados visualmente:

El Filtro Bilateral tiende a suavizar más las texturas dentro de las regiones, pero mantiene los bordes relativamente nítidos. Podemos notar que las áreas planas se vuelven más uniformes, mientras que los contornos de los objetos permanecen definidos.

El Filtro de Mediana Híbrida, al igual que el filtro de mediana estándar, es muy bueno para eliminar ruido impulsivo (si lo hubiera), pero también puede suavizar ligeramente los bordes y detalles, aunque generalmente menos que un filtro de promedio lineal del mismo tamaño. Su fortaleza radica en preservar esquinas y estructuras lineales mejor que el filtro de mediana estándar.

La elección entre estos filtros depende del tipo de ruido presente y de los objetivos del procesamiento. El filtro bilateral es excelente para preservar bordes con ruido Gaussiano, mientras que los filtros de mediana (incluido el híbrido) son más robustos contra el ruido impulsivo.

La imagen original con ruido Gaussiano añadido. Este ruido se caracteriza por variaciones aleatorias en los valores de intensidad distribuidas normalmente.

El resultado de aplicar el Filtro Bilateral a la imagen con ruido Gaussiano. Observa cómo el filtro bilateral reduce eficazmente el ruido Gaussiano mientras preserva los bordes. Esto se debe a su capacidad para suavizar píxeles con intensidades similares, evitando promediar a través de los bordes.

El resultado de aplicar el Filtro de Mediana Híbrida a la imagen con ruido Gaussiano. Aunque el filtro de mediana puede reducir algo el ruido Gaussiano, no es tan efectivo como el filtro bilateral para este tipo de ruido. Tiende a dejar una apariencia más "bloqueada" o con menos suavizado en las áreas planas en comparación con el filtro bilateral.

La imagen original con ruido de Sal y Pimienta añadido. Este ruido se presenta como píxeles aleatorios muy brillantes (sal) o muy oscuros (pimienta).

El resultado de aplicar el Filtro Bilateral a la imagen con ruido de sal y pimienta. El filtro bilateral es menos efectivo para eliminar el ruido de sal y pimienta. Los valores extremos de los píxeles de ruido pueden influir significativamente en el cálculo ponderado, dejando puntos de ruido residual.

El resultado de aplicar el Filtro de Mediana Híbrida a la imagen con ruido de sal y pimienta. El filtro de mediana (y sus variantes como la híbrida) es altamente efectivo para eliminar el ruido de sal y pimienta, como ya hemos visto en secciones anteriores.

Estos dos ejemplos resaltan una diferencia clave en la sensibilidad y efectividad de estos filtros para diferentes tipos de ruido:

El Filtro Bilateral es ideal para reducir ruido Gaussiano mientras preserva los bordes.

El Filtro de Mediana Híbrida (y los filtros de mediana en general) es superior para eliminar ruido impulsivo como el ruido de sal y pimienta.

Por lo que, en función del tipo de ruido que tengamos en la imagen, la elección del filtro para reducir el ruido debe basarse en el tipo de ruido dominante presente en la imagen. En la práctica, se puede utilizar una combinación de filtros para abordar diferentes tipos de ruido o para lograr un resultado de suavizado y preservación de bordes específico.

Este ejemplo demuestra el efecto escalera y la inversión del gradiente al aplicar el filtro bilateral a una imagen con parámetros que exageran estos artefactos (valores altos para
 y
).

Efecto Escalera: En la imagen filtrada, podemos observar cómo las áreas con transiciones de color o intensidad suaves (como el cielo, piel, o fondos con gradientes) se convierten en bandas de color o intensidad discretas, creando una apariencia de "escalones".
La primera fila muestra la imagen completa, original y filtrada. Aquí es donde este efecto es más visible en las áreas con gradientes suaves.

Inversión del Gradiente: Este artefacto puede ser más sutil. Tenemos que buscar en la imagen filtrada (especialmente en el área con zoom) transiciones de color o intensidad que parezcan ir en la dirección opuesta a la de la imagen original.
Por ejemplo, una zona que se aclara gradualmente en el original podría oscurecerse en el filtrado, o un color podría cambiar hacia una tonalidad inesperada en el borde. Esto sucede cuando los pesos de intensidad en el filtro, influenciados por los valores de color, causan que píxeles lejanos con valores de color similares al píxel central tengan una ponderación alta, llevando a un promedio que invierte el gradiente local.
La segunda fila muestra un zoom en un área específica. Esta vista ampliada puede ayudar a identificar este problema si está presente en esa región, al permitir una comparación más detallada de las transiciones de color/intensidad entre la imagen original y la filtrada.

Este ejemplo subraya la importancia de sintonizar cuidadosamente los parámetros del filtro bilateral. Si  y  son demasiado altos, se pueden introducir estos artefactos que degradan la calidad perceptual de la imagen, a pesar de la reducción de ruido.

### Lesson 16 - Filtro de Kuwahara

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/rdM_5mU_OfavXkgBRcgknLcYuSioSnYp</sub>

Filtro de Kuwahara

A veces queremos limpiar textura fina y grano sin tocar la forma. El Gaussiano lo alisa todo (cruzando bordes), el bilateral necesita afinar sus dos “candados” (espacio e intensidad) y, aun así, puede producir “escalones”. El Kuwahara propone otra mirada: antes de promediar, mira qué parte del vecindario es más homogénea. Promedia solo dentro de la subzona más estable. Así, el filtro se frena en los bordes y suaviza el interior de las regiones. El resultado típico tiene un punto “pictórico”: zonas uniformes separadas por contornos nítidos.

Para cada píxel, consideramos una ventana cuadrada alrededor y la dividimos en cuatro regiones solapadas (cuadrantes) que todas contienen el píxel central:

Arriba-Izquierda (AI)

Arriba-Derecha (AD)

Abajo-Izquierda (BI)

Abajo-Derecha (BD)

Este ejemplo paso a paso ilustra el funcionamiento del filtro de Kuwahara en un píxel central:

1.  Parche Original: Cada recuadro de color (cian, verde, amarillo y magenta) representa una de las regiones que usa el filtro Kuwahara (tamaño 2x2 para un kernel de 3x3). En la imagen también podemos observar las medias y varianzas calculadas para cada subregión.

2.  Subregiones: El kernel principal se divide en cuatro subregiones superpuestas. Para cada píxel, el filtro considera el vecindario definido por el tamaño del kernel. Dentro de este vecindario, se calculan las subregiones.

Independientemente del tamaño del kernel, siempre vamos a tener 4 regiones definidas para el filtro de Kuwahara, tal y como lo hemos definido al inicio de la sección,

Cálculo de Media (
 ) y Varianza (
): Para cada una de las cuatro subregiones, se calcula la media y la varianza de los píxeles que contiene. La varianza es una medida que nos ayuda a entender la dispersión de los valores (es decir, cuánto cambian los valores dentro de esa región).

Donde
 representa el número de elementos de la subregión.

4.  Selección de la Subregión: El filtro compara las varianzas de las cuatro subregiones. Selecciona la subregión que tiene la mínima varianza. Una baja varianza indica que los píxeles en esa subregión tienen valores muy similares, lo que sugiere que es una región relativamente plana o suave, o que se encuentra completamente en un lado de un borde.

5.  Pixel de Salida: El valor del píxel central en la imagen de salida se reemplaza por la media de la subregión seleccionada (la de mínima varianza).

Este proceso permite al filtro de Kuwahara suavizar el ruido (reduciendo la varianza en áreas planas) mientras intenta preservar los bordes (seleccionando la subregión que evita cruzar el borde si es posible).

Problemas Comunes del Filtro de Kuwahara en Imágenes a Color 

Aunque el filtro de Kuwahara es bueno para preservar bordes mientras suaviza el ruido en áreas planas, puede introducir ciertos artefactos:

Aspecto de Bloque o Cuadriculado: Debido a que el filtro reemplaza el píxel central con la media de una de las cuatro subregiones cuadradas, las áreas planas pueden tener una apariencia ligeramente segmentada o "cuadriculada", especialmente con tamaños de kernel más grandes. Esto se ve en las áreas que deberían ser suaves pero que muestran transiciones abruptas entre las regiones donde se seleccionaron diferentes subregiones.

Pérdida de Microdetalle: El filtro de Kuwahara tiende a suavizar las texturas finas y los detalles de bajo contraste dentro de las áreas planas. Aunque esto es parte de su función de reducción de ruido, puede resultar en una pérdida de información visual sutil.

Bordes Algo “Angularizados”: Si bien el filtro Kuwahara preserva los bordes mejor que un filtro de promedio lineal, los bordes diagonales o curvos pueden aparecer ligeramente angularizados o escalonados debido a la naturaleza cuadrada de las subregiones.

Este ejemplo aplica el filtro de Kuwahara a una imagen a color (aplicando el filtro a cada canal de color por separado) y muestra algunos de sus problemas típicos.

Demostrar y corregir estos problemas de manera efectiva a menudo requiere técnicas más avanzadas, como filtros híbridos o post-procesamiento, que van más allá de la aplicación básica del filtro de Kuwahara.

### Lesson 17 - Filtro Rolling-Guidance

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/OsKHmvfpon-cu5IG1R8Kks8KOczsGfCG</sub>

Filtro Rolling-Guidance

A veces el bilateral se te queda corto: limpia, sí, pero en escenas con mucha textura (ladrillo fino, hierba, piel con grano fuerte) o cuando buscamos un aspecto más estructural (cartooning elegante, bases para segmentación), que queramos ir quitando detalle por “capas” sin tocar las fronteras que dibujan la forma. Ahí entra el Rolling Guidance Filter (RGF): un proceso iterativo que en cada vuelta genera una imagen-guía más “tranquila” y usa esa guía para filtrar, salvaguardando los bordes, la imagen original. Al “rodar” (rolling) varias veces, la textura se apaga progresivamente y los bordes relevantes se mantienen.

Primero: hacemos una pasada de suavizado leve para calmar la guía.

Después: usamos esta versión calmada como guía para un filtrado de recuperación de bordes.

Repetimos: la nueva salida se convierte en la guía de la siguiente iteración, y así sucesivamente.

Con cada iteración, la guía “se centra” en estructuras grandes; el filtro, obedeciendo a esa guía, no mezcla a través de sus bordes. El resultado es una imagen por capas: fuera el detalle fino; dentro, regiones limpias separadas por contornos reales.

IMAGEN ORIGINAL
IMAGEN GUÍA
PASO DE SUAVIZADO INICIAL
RESULTADOS DESPUÉS DE ITERACIONES DE ROLLING GUIDANCE

La imagen de entrada sin modificar.

Podemos ver cómo el suavizado inicial difumina los detalles, los bordes y puede causar una ligera mezcla de colores. A medida que aumentan las iteraciones, las áreas planas y las texturas se vuelven más suaves y uniformes en color (reducción de ruido y abstracción de texturas), mientras que los bordes principales se mantienen relativamente definidos y las transiciones de color en los bordes se preservan mejor que con un suavizado Gaussiano simple y repetido.

Aunque el Rolling Guidance es eficaz para la reducción de ruido y la abstracción de texturas con preservación de bordes, tiene algunas limitaciones, que pueden volverse más evidentes con un mayor número de iteraciones:

1.  Pérdida de Detalles Finos y Texturas: Aunque preserva los bordes principales, el filtro puede suavizar agresivamente las texturas finas y los detalles de bajo contraste dentro de las regiones. Con muchas iteraciones, estas áreas pueden volverse excesivamente planas.

2.  Efecto "Pintura al Óleo" o "Cartoonizado": El fuerte suavizado dentro de las regiones y la preservación de bordes pueden dar a la imagen un aspecto similar al de una pintura al óleo o un dibujo animado, donde las transiciones son muy nítidas y las áreas planas son uniformes. Esto puede ser deseable en algunos casos (por ejemplo, para efectos artísticos), pero puede no ser apropiado si se busca un resultado más natural.

3.  Dependencia de la Imagen Guía: La calidad del resultado final depende significativamente de la imagen guía. Si la imagen guía no captura correctamente los bordes importantes o introduce artefactos, estos problemas pueden propagarse al resultado filtrado.

4.  Costo Computacional: Es un filtro iterativo y, dependiendo del tamaño de la imagen y el número de iteraciones, puede ser computacionalmente costoso.

Podemos observar el resultado con un mayor número de iteraciones en esta segunda segundo gráfico. Si comparamos las áreas planas y las texturas con la imagen original, veremos un suavizado más pronunciado y el posible surgimiento de un aspecto más "pintoresco". Esto ilustra que, si bien más iteraciones aumentan el suavizado, también pueden llevar a una pérdida de realismo y a los límites mencionados del filtro.

### Lesson 18 - Detector de Bordes de Canny

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/gdEPOg9yayZDwlW5IKd6J5NMqS1rKc6S</sub>

Detector de Bordes de Canny

Ya sabemos suavizar para domar ruido, y medir la pendiente usando el gradiente para ver dónde cambia la imagen. Pero ese mapa de magnitudes suele salir grueso y, si umbralizamos sin más, o nos pasamos, donde perdemos los bordes de la imagen o nos quedamos corto, donde puede aparecer ruido granular o sal y pimienta. Canny empaqueta una receta muy sensata para convertir ese borrador en un boceto limpio: líneas finas, continuas y lo más libres posible de ruido.

1
2
3
4
5
1 de 6

¿Cómo funciona?

COMENZAR
2 de 6
Paso 1
Reducción de ruido (suavizado previo)

“Apaga” el grano que, para pasos posteriores, se podría comportar como bordes falsos y marcar bordes inexistentes. Podemos aplicar:

Gaussiano
 (con un kernel
) para grano fotográfico normal.

Mediana 3×3 si hay sal-y-pimienta.

Para más control de escala, usa derivada del Gaussiano más adelante.

Tengamos en cuenta, que si una vez aplicada la reducción de ruido, sigue quedando algo de ruido, suele ser que faltó suavizado (o sobran umbrales bajos).

3 de 6
Paso 2
Medición del gradiente (magnitud y orientación)

Estima cuánto cambia la intensidad (magnitud) y hacia dónde (orientación). Ya que el borde real es una transición de intensidades, gracias al gradiente vamos a poder detectar estas transiciones. Podemos aplicar, el filtro Sobel (3×3) por defecto ya que se aplica sobre ambos ejes X e Y.

4 de 6
Paso 3
Supresión de No-Máximos (NMS)

El problema principal que tenemos en el paso anterior, es que los bordes no son uniformes entre sí, y tienen magnitudes diferentes. Por ello convertimos la banda gruesa de magnitudes en una línea de 1 píxel, para poder crear líneas uniformes, y además poder eliminar aquellos píxeles que no pertenecen a ningún borde. Para cada píxel, mira la dirección del gradiente (perpendicular al borde) y comprara su magnitud con dos vecinos a lo largo de esa dirección. Sólo sobrevive si es el máximo local.

5 de 6
Paso 4
Doble umbralización

Clasificamos cada píxel adelgazado que hemos obtenido en el apartado anterior en los siguientes tipos.

i. Fuertes: Pertenecen a un borde a tener una intensidad elevada

ii. Débiles: Su intensidad no es suficientemente elevada para pertenecer a un borde, pero tampoco lo suficientemente débil para no pertenecer.

iii. No relevantes: No tienen intensidad suficiente para pertenecer al borde, y por lo tanto pueden ser descartados.

Con esta clasificación evitamos cortar bordes reales (al rescatar débiles conectados) y suprime “pelos” de ruido. Debemos elegir de una manera práctica los umbrales que decidimos qué serán píxeles fuertes, píxeles débiles y partir de qué umbral descartamos píxeles. Por ejemplo, para el umbral “alto”, podemos tomar el percentil 85 de los valores que tenemos en la imagen mayores que 0; y como umbral “bajo” la mitad de este percentil. Eso quiere decir, que aquellos valores que se encuentren por encima del percentil 85, van a ser marcados como píxeles fuertes; los que estén entre el percentil 85 y su mitad, serán categorizados como píxeles débiles, y todo lo que esté por debajo será descartado.

6 de 6
Paso 5
Resaltar bordes con Histéresis

Una vez tenemos los píxeles débiles detectados, “recorremos” aquellos bordes con píxeles fuertes, y si encontramos en el camino píxeles débiles, estos los convertimos a píxeles fuertes. Para el resto de los píxeles débiles que no están cerca de ningún píxel fuerte, pasan a ser no relevantes y se descartan. Esto lo realizamos para no cortar bordes que pueden contener “baches” a lo largo de su longitud.

En el siguiente video vamos a ver cómo se deben elegir correctamente los parámetros de la detección de bordes de Canny teniendo en cuenta los elementos de la imagen que queremos resaltar.

Reproducir Vídeo
¡Fantástico! Has completado este apartado.

### Lesson 19 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/MhS6LHJ_j8zUXaTgH3vRqS8pm4rk2Tzk</sub>

Introducción

Hasta ahora hemos aprendido a “escuchar” la imagen con filtros: suavizar lo que estorba y realzar lo que importa. El siguiente paso es poner chinchetas donde la imagen nos ofrece anclajes fiables: lugares que resisten pequeños cambios de encuadre, escala o iluminación y a los que podamos regresar más tarde para emparejar, alinear o seguir. A estos anclajes los llamaremos estructuras de interés, y en este apartado vamos a abrir dos familias fundamentales:

Puntos clave (esquinas/intersecciones): zonas donde el contenido cambia en dos direcciones a la vez. Su vecindario “no encaja” por mucho que te muevas ligeramente en X o en Y.

Manchas o blobs: regiones compactas (máximos o mínimos locales) que destacan en una escala concreta; aparecen y desaparecen cuando “enfocamos” la imagen con lupas de distinto tamaño.

Piensa en los puntos clave como chinchetas que se clavan en las esquinas y en los blobs como gotas o islotes que emergen cuando miras la imagen a una escala adecuada.

¿Por qué nos interesan?

Porque casi cualquier tarea clásica de visión necesita referencias repetibles:

Registro y mosaicos: unir dos fotos del mismo lugar tomadas desde posiciones distintas.

Seguimiento (tracking): encontrar de nuevo “los mismos” puntos en vídeo.

Calibración/pose: estimar cómo está orientada una cámara respecto a una escena.

Reconstrucción: emparejar vistas para recuperar geometría.

Sin buenas estructuras de interés, todo esto se vuelve frágil: o no encuentras suficientes correspondencias o las que encuentras no son fiables.

### Lesson 20 - Detección de puntos clave o keypoints

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/3oLxlJ1w-KFeIn2e6JNoi4Y2FJ5fQyIV</sub>

Detección de puntos clave o keypoints

Queremos “agarrarnos” a la imagen en lugares que no se confundan si cambiamos un poco el encuadre, la escala o la iluminación. Esos lugares son los puntos clave (keypoints): esquinas bien formadas, intersecciones de trazos, pequeñas estructuras locales que “no se parecen a nada” alrededor. Funcionan como chinchetas: si las colocamos en la imagen A y las volvemos a ver en la imagen B (desde otro ángulo o distancia), podemos emparejar, alinar y medir con confianza.

Algoritmo FAST

Cuando necesitamos muchos puntos clave y los necesitamos tenerlos casi en tiempo real, en aplicaciones como robótica o realidad virtual, otros algoritmos pueden quedarse cortos en número de frames por segundo. FAST nació para eso: detectar esquinas con una prueba lógica muy barato sobre un anillo de 16 píxeles alrededor del centro. No pide derivadas ni convoluciones grandes; decide con comparaciones de intensidad y un umbral. El resultado: pocos cálculos, mucha señal.

¿En qué consiste este algoritmo?

Seleccionamos un píxel
 de la imagen, que se define con su intensidad
.

Se define un umbral
.

Se dibuja un círculo de 16 píxeles alrededor del píxel.

Evaluamos si el píxel 
 es un punto de interés. Para ello se evalúa si al menos
 pixeles de los 16, (normalmente se escogen 12) son más brillantes que
 o menos que
 Si supera el umbral, se considera un punto clave.

El píxel central se clasifica como un punto clave FAST si existe un segmento contiguo de
 píxeles (por ejemplo, 9 o 12) en el círculo que son todos significativamente más brillantes o todos significativamente más oscuros que el píxel central (considerando el umbral).

Si se encuentra dicho segmento contiguo de
  píxeles brillantes o oscuros, el píxel central se declara un punto clave.

En el diagrama de la izquierda, podemos ver una situación donde se detecta un punto clave porque hay un segmento contiguo de píxeles significativamente más brillantes.

En cambio, en el de la derecha, muestra una matriz donde, a pesar de que hay píxeles más brillantes y oscuros alrededor del centro, no hay un segmento contiguo de la longitud requerida (
) que cumpla la condición de brillo/oscuridad con respecto al umbral. Por lo tanto, el píxel central no se clasifica como punto clave.

Hay una variante opcional, para aumentar la velocidad del algoritmo la cual sólo comprueba los 4 píxeles que están en los ángulos rectos, es decir, las posiciones 1, 5, 9 y 13 del círculo. Esta variante provoca muchos falsos positivos, ya que descarta muchos candidatos, aunque aumente mucho a velocidad del algoritmo.

### Lesson 21 - Detección de manchas o blobs

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/ozi7wkMCGsk0XdDbl7kRMhydk6xFs2Zz</sub>

Detección de manchas o blobs

Hasta aquí hemos buscado esquinas (cambios en dos direcciones), pero hay otra familia de estructuras igual de útil: las manchas o blobs. Pensemos en islotes compactos —puntas de luz, lunares oscuros, letras, tornillos— que destacan frente a su alrededor. Un mismo blob puede aparecer o desaparecer según el tamaño de la lupa con la que miremos: a escala fina vemos grano; a escala gruesa, vemos siluetas; en una escala intermedia esa mancha concreta “grita” más que nada. Detectar blobs consiste, precisamente, en buscar máximos/mínimos de una respuesta en el espacio y en la escala.

Para detectar estas manchas, vamos a volver a usar unas viejas conocidas, las derivadas. Como hemos visto en los filtros, las primeras derivadas (gradiente) nos dicen “aquí crece o disminuye rápido”; en el término de detectar elementos, son ideales para bordes.

Por otro lado, las segundas derivadas nos dicen cómo cambia el propio cambio, en lugar de decirnos dónde están. En un bulto brillante sobre fondo oscuro:

En el centro del blob, la intensidad cae en todas direcciones: ahí la curvatura es máxima negativa (si tomas brillo alto positivo).

En el borde del blob, el Laplaciano suele cruzar por cero (pasa de “convexo” a “cóncavo”).

Esa pareja (extremo en el centro, cruce por cero en el borde) es lo que convierte a las segundas derivadas en un detector natural de las manchas que estamos buscando.

Volvamos a recordar, que podemos ver una imagen como una escala de grises como un mapa de alturas, donde a cada punto se le corresponde un nivel, es decir su intensidad. La isocurva es la línea que une todos los puntos que tienen el mismo valor, es decir, la isocurva es lo que representa el contorno de un objeto o el borde, y lo que nos va a ayudar a detectar los bordes.

Cuando filtramos la imagen con un operador de segunda derivada (por ejemplo, un Laplaciano), la isocurva de valor cero (los cruces por cero) dibuja fronteras de objetos o blobs.

Si pintamos los cruces por cero de un LoG (Laplaciano del Gaussiano), obtenemos contornos cerrados alrededor de la mancha.

Si además miramos dentro de ese contorno, suele haber un pico (máximo o mínimo) de la respuesta: ese es el centro del blob.

En práctica moderna, solemos preferir buscar los picos (máximos/mínimos) directamente en espacio-escala; pero entender los ceros ayuda a visualizar dónde termina la mancha.

Laplaciano del Gaussiano (LoG)

El Laplaciano del Gaussiano (LoG) es un detector de “manchas” (blobs) que funciona así: primero miramos la imagen con una lupa del tamaño que elijamos (un Gaussiano que suaviza a esa escala), y justo después aplicamos un medidor de curvatura (el Laplaciano, una segunda derivada). Donde la imagen forma un “montículo” o “hueco” compacto a esa escala, el LoG se dispara en el centro; alrededor, cruza por cero y te dibuja el borde del blob.

¿Por qué Gaussiano + Laplaciano?

Gaussiano = lupa/escala. Suavizar con un Gaussiano de desviación  es como desenfocar un poco la imagen para ignorar detalles más finos que esa escala. Con  pequeño vemos micro-textura; con σ grande vemos formas más gordas.

Laplaciano = curvatura. La segunda derivada nos dice si estamos en la cima de un “montículo” (curvatura negativa para blobs claros) o en el fondo de un “hueco” (curvatura positiva para blobs oscuros). También nos marca el contorno con los cruces por cero (donde la curvatura cambia de signo).

Imaginemos una moneda brillante sobre un fondo más oscuro:

En el centro de la moneda, la intensidad baja en todas las direcciones → la curvatura (Laplaciano) es negativa y grande (en valor absoluto).

A lo largo del borde de la moneda, la curvatura pasa de negativa a positiva → el LoG cruza por cero (nos dibuja el contorno).

En el fondo llano, la curvatura es casi cero → el LoG se anula.

Una mancha o blob no tiene un “tamaño universal”. Para poder detectarlo correctamente, vamos a probar con varias lupas (varios ) y buscamos picos en 3D: posición (x, y) y escala (σ).

Elegimos una lista de escalas:
₁
₂
ₙ
 (por ejemplo, usando una progresión geométrica:

Para cada σ:

Suavizamos con Gauss (σ).

Aplicamos Laplaciano → obtenemos el LoG a esa escala.

Normalizamos por escala (≈ multiplicar por σ²) para poder comparar respuestas entre escalas.

Apila todos los mapas (uno por σ) y busca máximos/mínimos locales en vecindarios 3D (x, y, σ).

La escala del pico, σ*, te da el tamaño del blob; el radio aproximado es √2·σ*; la posición del pico es el centro del blob.

Si aplicamos un Laplaciano directo (sin Gauss), podemos detectar cambios de curvatura, pero:

es muy sensible al ruido (segundas derivadas amplifican lo fino),

no podemos controlar la escala del detalle que queremos.

Por eso, en la práctica, siempre hacemos “Gauss → Laplaciano”: así controlamos qué detalle ignoramos (σ) y nos quedamos con manchas o blobs estables.

Diferencias de Gaussianas (DoG)

Otro filtro que nos va a ayudar a detectar de manchas (blobs), es la Diferencia de Gaussianas (DoG), que consiste en mirar la imagen con dos desenfoques (dos “lupas”) de tamaños cercanos y restarlos. Todo lo que “vive” entre esas dos escalas se realza; lo que es más fino o grueso se atenúa. Si repetimos el proceso en varias escalas y buscamos picos 3D (posición + escala), obtenemos centros y tamaños de blobs de forma rápida y muy efectiva.

¿Por qué restar dos Gaussianas?

El Gaussiano con  es una lupa: alisa detalles más finos que .

Restar dos Gaussianas cercanas (
 y
) resalta estructuras cuyo tamaño está entre
 y
.

Matemáticamente, este método es una excelente aproximación al método del Laplaciano del Gaussiano (LoG) pero con mucho menos coste: dos desenfoques separables y una resta.

Imagina que queremos encontrar islitas en el mar de la imagen. Con DoG hacemos dos fotos con lupas de tamaños cercanos y las restas: lo que vive entre esos tamaños aparece. Funciona y es rápido, pero a veces, si la isla es justo un poco más pequeña o un poco más grande que nuestra banda, se nos escapa: cae “entre dos emisoras” y su señal baja.

Observaciones:

En general, ambos algoritmos detectan manchas (blobs) que corresponden a áreas de cambio de intensidad en la imagen, como esquinas y puntos brillantes u oscuros.

Puede haber diferencias en el número de blobs detectados por cada algoritmo, así como en sus tamaños y ubicaciones exactas. Esto se debe a las diferencias en cómo cada algoritmo aproxima el Laplaciano y cómo manejan las diferentes escalas.

LoG se considera teóricamente más preciso para detectar blobs circulares en diferentes escalas, ya que detecta los máximos de la respuesta del Laplaciano en el espacio de escala.

DoG es una aproximación computacionalmente más eficiente de LoG y a menudo se utiliza en aplicaciones prácticas como la detección de características en SIFT, que veremos más adelante. Aunque es una aproximación, DoG a menudo produce resultados muy similares a LoG y es más rápido de calcular.

La elección entre LoG y DoG puede depender de la aplicación específica, los requisitos de precisión y las limitaciones computacionales. ¿Quiere decir esto que DoG sea “malo”? Para nada: es rapidísimo y, bien configurado (
 y multiescala densa), se acerca mucho a LoG. Pero si nuestra prioridad es recuperar el mayor número de manchas reales (incluidas las difíciles: pequeñas, con contraste justo o pegadas a bordes), el LoG nos da más señales fuertes por escala y, por tanto, más detecciones útiles.

Determinante del Hessiano (DoH)

Ya tenemos dos detectores de manchas en nuestra caja de herramientas: LoG (curvatura “circular” a una escala) y DoG (resalta lo que vive entre dos escalas). El Determinante del Hessiano (DoH) se suma con una idea muy directa: si en el centro de una región hay curvatura en las dos direcciones (horizontal y vertical) y esa curvatura “empuja” en el mismo sentido, lo más probable es que estemos sobre una mancha compacta y no sobre un borde alargado. DoH es, por tanto, un “comprobador de curvatura 2D”: valora la curvatura a lo largo de dos ejes y las mezclas entre ellos, y dispara justo donde hay bulto/sumidero bien formado.

¿Qué es el Hessiano?

El Hessiano es una “matriz de segundas derivadas” de la imagen suavizada a cierta escala. Si nuestra imagen la denotamos por
, la matriz Hessiana viene determinada por,

Donde,

 es la segunda derivada de la imagen dos veces sobre la componente
.

 es la segunda derivada de la imagen, primero sobre
, y después sobre
.

 es la segunda derivada de la imagen, primero sobre
, y después sobre
.

 es la segunda derivada de la imagen dos veces sobre la componente
.

El determinante de esta matriz Hessiana (DoH) funciona como un “test de manchas”:

En el centro de una mancha (clara u oscura) la curvatura en X y en Y suele tener el mismo signo y ser grande en magnitud → el determinante sale alto.

En un borde alargado, una dirección curva fuerte y la otra apenas lo hace → el determinante tiende a cero (“no hay blob, sólo borde”).

En una silla (una curvatura positiva y otra negativa), el determinante sale negativo → tampoco es un blob.

¿En qué se diferencia de LoG/DoG en la práctica?

Selectividad a “formas redondas”: DoH tiende a ser muy selectivo con blobs bien formados y poco tolerante con bordes; si buscamos “puntos de anclaje” limpios, será nuestro método ideal.

Contorno: LoG nos da un cero que perfila el borde del blob, mientras que DoH no. DoH es para centros/tamaños robustos, no para dibujar contornos.

Coste: calcular segundas derivadas en dos ejes + mixta es algo más caro que un DoG, pero sigue siendo práctico (las Gaussianas son separables y Sobel es eficiente).

Aproximaciones rápidas: SURF (que veremos más adelante) popularizó DoH con filtros caja sobre imágenes integrales, acelerando muchísimo el proceso con una ligera pérdida de precisión.

### Lesson 22 - Invarianzas

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/8ZARdtc3MsvFEOLl6BehKDmw9VOVSlAF</sub>

Invarianzas

Una vez visto cómo encontrar puntos clave, esquinas, intersecciones con FAST, y manchas o blobs con LoG/DoG/DoH, ahora necesitamos que esas “chinchetas” sigan siendo reconocibles cuando la cámara se desplaza, gira, hace zoom o cambia la luz. Ahí entran las invariancias: trucos (de detector y de descriptor) para que lo que era el mismo punto siga pareciéndolo bajo transformaciones habituales del mundo real.

Antes de entrar en las diferentes invarianzas que podemos encontrar, centrémonos en entender qué es una invarianza, una equivarianza y el papel crucial que juegan en los algoritmos de procesamiento de imágenes.

¿Qué es una invariancia? Es cuando un proceso da el mismo resultado, aunque se transforme la entrada de una cierta manera. Por definición, un sistema
 es invariante a una transformación
 si

Es decir, estamos aplicando una transformación
 a una imagen, y el resultado queda igual que si la transformación no hubiera ocurrido. Algunos ejemplos de invarianzas son,

Para un histograma de intensidades global no depende de dónde están los píxeles, solo de cuántos hay de cada tono → invariancia a traslación (aunque no sea muy discriminativo espacialmente).

Un descriptor basado en direcciones de gradiente normalizadas cambia poco si subes o bajas la exposición → invariancia (robustez) a iluminación.

Por otro lado, debemos tener en cuenta otro concepto, la equivarianza: cuando el resultado cambia de forma predecible al transformar la entrada aplicando una transformación. Por definición, se dice que un sistema
  es equivariante a
 si

es decir, transformar la entrada equivale a transformar de forma conocida la salida. Por ejemplo, algunos casos de equivarianzas son,

La convolución que aplicamos en Gauss, Sobel, LoG o DoH, es equivariante a traslación: si desplazamos la imagen, el mapa filtrado se desplaza igual.

El mapa de bordes de Canny se desplaza si desplazamos la imagen (equivarianza), pero no es invariante (no se queda idéntico, ya que se mueve con la imagen se mueve).

La equivarianza nos da previsibilidad. Podemos predecir cómo viaja la señal (picos, bordes, blobs) cuando la imagen cambia, y con esa previsibilidad podemos construir invariancia (por ejemplo, usando la orientación/escalas detectadas para normalizar el parche).

Un buen algoritmo de procesamiento de imágenes debe ser capaz de extraer toda la información posible de la imagen, sin verse afectado por cómo se haya capturado la imagen: que esté alineada correctamente y esté algo girada, que la iluminación no sea la correcta, o que no se haya podido capturar el objeto a un tamaño correcto. Todos estos factores, deben hacer que algoritmo de procesamiento de imágenes se comporte de la misma manera ante cualquier situación.

### Lesson 23 - Algoritmos de descripción de imágenes

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/O6M1Jx0P1IjjfhTvnHuSVXJg-KhTwWkm</sub>

Algoritmos de descripción de imágenes

Ya sabemos dónde agarrarnos a la imagen: esquinas y manchas (puntos clave y manchas, keypoints y blobs) que sobreviven a traslaciones, giros y cambios de escala. El siguiente paso es poder reconocer esos mismos puntos en otra foto. Para eso necesitamos descriptores: funciones que toman un parche alrededor de cada punto y lo convierten en un vector que (1) cambia poco si mueves/giras/reescalas o varía la luz, y (2) es distinto para puntos que no son el mismo. En otras palabras: invariantes y discriminativos.

Algoritmo SIFT

Queremos reconocer “el mismo” punto en fotos distintas: un tornillo visto más cerca, un logo girado, una esquina con luz diferente. SIFT (Scale-Invariant Feature Transform) resuelve esto con un guion muy claro:

encuentra puntos que existen a una escala natural (no por magia, sino mirando la imagen con lupas de muchos tamaños),

ajusta su posición/escala con precisión y descarta falsas respuestas (píxeles con poco contraste o que en realidad son borde alargado),

mide la orientación dominante del vecindario para compensar rotaciones,

describe el parche con un histograma de gradientes que normaliza para ser robusto a la iluminación.

El resultado: un vector de 128 componentes por punto que se compara muy bien entre imágenes. Vamos a entrar en detalle de cada uno de los pasos,

1
2
3
4
5
1 de 6
Paso 1
Detección de puntos de interés

Primero buscamos la lista de candidatos para describir a la imagen original. Para ello vamos a usar un algoritmo como Laplaciano del Gaussiano (LoG) o Diferencia de Gaussianos (DoG).

2 de 6
Paso 2
Localización de los puntos de interés

Una vez que tenemos los puntos detectados en el paso anterior, hacemos un refinado de estos puntos. Para ello aplicamos el Determinante del Hessiano (DoH), donde por las propiedades del Hessiano de una imagen serán eliminados aquellos puntos que sean inestables.

3 de 6
Paso 3
Orientación a los puntos de interés

Se crea un histograma de orientación con 36 barras, debido a los  de giro. Se define un vecindario de puntos para cada punto de interés detectado, y para cada vecino se calcula su orientación. Finalmente, se crea una única orientación juntando todas las direcciones de los vecinos. Gracias a esto, se consigue crear una invarianza a la rotación.

4 de 6
Paso 4
Generación del descriptor

Para generar el descriptor final de la imagen, se define un vecindario de 16x16 píxeles alrededor de cada punto de interés. Esta región se divide en 16 bloques de 4x4, para cada bloque se genera un histograma de orientación de 8 barras. Estas 128 barras generan un vector que describe cada punto de interés.

5 de 6
Paso 5
Correspondencia de puntos de interés

Se utilizan técnicas como la distancia euclidiana para encontrar correspondencias de puntos clave entre dos imágenes.

6 de 6

Finalmente, junto con los descriptores, y su orientación tenemos los puntos de interés detectados por SIFT.

SIFT une cuatro ideas sencillas y poderosas:

-          DoG o LoG, para encontrar puntos con escala natural

-          Localizarlos y filtrar lo dudoso

-          Alinear por orientación

-          Describir con gradientes normalizados.

Por eso “aguanta” traslaciones, giros, zoom e iluminación, y por eso sigue siendo el referente cuando necesitas correspondencias fiables sin aprender un modelo complejo.

COMENZAR DE NUEVO

En el siguiente video, vamos a poder ver un pequeño ejemplo para poder “detectar” un logo dentro de una imagen. No lo vamos a detectar como tal, sino que vamos a comparar los detectores de ambas imágenes para ver si son los mismos y esto nos va a ayudar a entender si es la misma imagen o si por el contrario no “está” ese logo dentro de la imagen, es decir, no encontramos una relación directa entre los descriptores de las imágenes.

Reproducir Vídeo
Algoritmo SURF

Si SIFT es el “referente” en robustez, SURF nació para conseguir algo muy parecido, pero mucho más rápido en tiempo de cómputo. ¿Cómo lo hace? Cambia cálculo costoso por aproximaciones muy eficientes:

Detecta puntos tipo mancha o blob midiendo curvatura en 2D (como DoH), pero aproxima las segundas derivadas con filtros caja que se evalúan en O(1) usando imágenes integrales.

Describe el vecindario con un vector corto (64D por defecto; 128D opcional) construido a partir de esas mismas respuestas Haar.

El resultado: un pipeline que mantiene las invariancias clave (traslación, rotación —opcional—, escala, iluminación moderada) y ofrece un buen equilibrio entre velocidad y calidad.

Qué mide. Como en DoH, SURF decide “aquí hay mancha” cuando la curvatura en X y en Y es grande y “del mismo signo” (montículo/hoyo), y la curvatura cruzada no domina. Eso se resume en que SURF hace uso del determinante del Hessiano (DoH), para determinar estos valores iniciales de puntos de interés.

Cómo lo acelera. En vez de derivadas Gaussianas “finas”, SURF usa filtros caja que aproximan
 el determinante del Hessiano.

Donde se recomienda que

(Technische Universität München. Gaussian derivative images. [Online; accessed August, 2022].)

Con una imagen integral puedes sumar intensidades en rectángulos en tiempo constante, así que evaluar cada filtro es muy barato. Además, en SURF no se reescala la imagen para cada
: escala el filtro de 9x9 a 15x15, 21x21, etc., y lo aplica sobre la imagen integral. Así además conseguimos la invarianza con respecto a la escala de la imagen.

(Deepanshu Tyagi (Medimum). Surf pyramid image. [Online; accessed August, 2022].)

Este algoritmo tiene 4 pasos claramente diferenciados,

Detección de puntos de interés, mediante el “DoH acelerado” que hemos nombrado antes.

Determinación de la orientación, donde se asigna una orientación a cada punto identificado para que el descriptor sea invariante a la rotación.

Generación de descriptor. Se generan filtros basándose en filtros Haar. Los filtros Haar son los más simples que miden cambios bruscos: son como una regla con dos mitades, una suma positiva y otra negativa. Restar ambas nos da un “mini-gradiente” barato.

En 1D: un bloque
 pegado a otro
.

En 2D: rectángulos adyacentes (horizontal para
, vertical para
).

Con imagen integral, la suma en cada rectángulo es
, así que calcular
 y
 (direcciones en
 y en
) en muchos puntos es rapidísimo.

En SURF se usan para:

Orientación: midiendo
 y
 en un anillo de puntos, el vector resultante marca “hacia dónde tira” el patrón local.

Descriptor: en cada subregión se acumulan
 como resumen robusto del “cómo y cuánto” varía la intensidad.

Coincidencia de puntos clave. Al igual que en SIFT, se utilizan técnicas como la distancia euclidiana para encontrar correspondencias de puntos clave entre dos imágenes.

### Lesson 24 - Descripción de imágenes

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/AzWHY3eV4N20LwwWdYxNUHXZztYdv6GZ</sub>

Descripción de imágenes

Hasta aquí ya sabemos limpiar la imagen (suavizados lineales y no lineales), realzar estructura (paso alto, gradiente, segunda derivada), detectar anclajes robustos (esquinas con FAST y manchas con LoG/DoG/DoH) y hacerlos sobrevivir a cambios normales del mundo (traslación, rotación, escala e iluminación).

Durante toda esta sección, hemos estado hablando de establecer puntos de interés para poder comparar imágenes entre sí y hacer coincidencia de puntos clave. Para ello vamos a convertir los puntos clave que hemos calculado en vectores que se puedan reusar entre imágenes. Eso es describir: tomar el parche local (centrado en el punto clave (keypoint) y adaptado a su escala/orientación si hace falta) y sacar de ahí una firma:

Compacta (pocos números o, mejor aún, bits).

Robusta (cambia poco si giras, haces zoom o varía la luz de forma razonable).

Discriminativa (distingue puntos distintos).

Escalable (se empareja rápido con miles/millones de descriptores).

Tengamos en cuenta que ya hemos clavados las chinchetas (puntos clave y machas) en la imagen. Están ahí, firmes, pero no hablan. El descriptor es la huella digital de cada chincheta: un pequeño “carnet” que dice “soy este rincón de la realidad” aunque la cámara se haya movido, girado, hecho zoom o cambie la luz. Con esas huellas, de pronto, podemos reconocer y reconectarlo todo.

Un descriptor no es un adorno: es lo que convierte un píxel anclado en un punto reconocible a través del tiempo, de otras cámaras y de otras condiciones. Con esa “huella digital” podemos emparejar, medir, mapear, buscar, coser y seguir. Es la pieza del pipeline que transforma detecciones en conocimiento reutilizable.

Algoritmo BRIEF

El algoritmo BRIEF (Binary Robust Independent Elementary Features) es un algoritmo para la generación de descriptores de imágenes. BRIEF convierte los puntos de interés detectados en la imagen previamente, en una cadena de bits respondiendo a muchas preguntas muy baratas del estilo: “¿es este píxel más oscuro que este otro?” → 1 si sí, 0 si no. Repite la pregunta n veces con pares de puntos diferentes dentro del parche y así obtendremos un descriptor binario (128, 256 o 512 bits).

BRIEF no “entiende” rotación ni escala por sí mismo: esa invariancia se la damos nosotros alineando, reescalando el parche o usando la orientación/escala del punto de interés.

¿Cómo es el algoritmo de BRIEF?

Primero llega una lista de puntos
, junto con la orientación y la escala.

Extrae un recorte centrado en un punto, de un tamaño aproximado de 31 o 41 píxeles, al que llamamos “parche”.

BRIEF es sensible al ruido, por lo que, para estabilizar este ruido, aplicamos un filtro Gaussian     (
 ).

Se establece un patrón de pares
. Es el corazón del algoritmo. Para ello definimos pares de coordenadas relativas dentro del parche, y podemos aplicar diferentes aproximaciones. Si tenemos que el parche tiene un tamaño
, vamos a ver algunas formas populares de elegir estos patrones de pares,

Uniforme. Los píxeles
 e
 se escogen a través de una distribución uniforme de extensión
Es muy fácil de implementar, y cubre todo el parche con gran variedad de distancias y direcciones; en contrapartida, es vulnerable a recortes, ya que muchos pares caen cerca del borde.

Gaussiana. Los píxeles
 e
 se escogen a través de una distribución gaussiana de extensión
 Da un mejor rendimiento que el uniforme, ya que evita bordes y el patrón se concentra donde la geometría es más fiable, normalmente la zona central. Por otro lado, ofrece una menor cobertura de estructuras grandes del parche.

Coarse Polar Grid. El primer píxel
 siempre está centrado en
, y el segundo píxel  se escoge a través de coordenadas polares.

Para cada vector definimos,

Donde
 es la intensidad del punto de referencia
,
 es el punto con el que se realiza la comparación.

Empaquetamos cada array de bits que sale de
 a los vectores iniciales, y se guarda junto al punto de interés.

Tenemos al final como resultado un descriptor binario por cada uno de los puntos de interés de la imagen. Para poder comparar los puntos de interés entre diferentes imágenes, podemos usar la distancia Hamming, que mide cuántos bits difieren entre dos cadenas binarias de igual longitud.

Formalmente, para dos descriptores

donde
 es XOR.

Por lo tanto, la distancia de Hamming entre dos descriptores calculados por BRIEF es, por tanto, el número de pruebas que no coinciden entre ambos puntos. Se usa para emparejar: cuanto menor
, más parecidos son los parches. Es extremadamente rápida (XOR + popcount sobre palabras de 64 bits) y encaja naturalmente con descriptores binarios, a diferencia de distancias Euclídeas pensadas para vectores reales.

¡Fantástico! Has completado este apartado.

### Lesson 25 - Conclusiones de la unidad

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/XpAAEqQBmYT1cCtBxCC2Yeu38T4WXOLc</sub>

Conclusiones de la unidad

En esta unidad hemos pasado de “mirar” la imagen como un conjunto de datos a trabajar con su vecindario con criterio y con un objetivo, es decir, hemos aprendido a combinar píxeles cercanos mediante convolución para suavizar, realzar y, sobre todo, descubrir estructura.

Hemos aprendido qué es convolucionar en 2D, qué papel juega el kernel, y cómo esta operación nos permite construir efectos distintos según los pesos que apliquemos. Después, hemos analizado la imagen en frecuencia para entender la diferencia entre bajas y altas frecuencias y por qué un filtro de paso bajo “deja pasar lo grueso” y atenúa lo fino; ahí encaja el teorema de la convolución (convolucionar en espacio ≡ multiplicar en frecuencia). Con ese mapa conceptual, el resto de la unidad ha sido una secuencia de decisiones informadas: suavizar o realzar, lineal o no lineal, bordes o puntos clave, y finalmente describir lo encontrado para poder compararlo entre imágenes.

Por tanto, a estas alturas ya no “miramos” imágenes: sabemos intervenirlas con intención. Si queremos limpiarlas sin perder lo importante, pensamos en frecuencias: lo grueso vive en bajas, los bordes en altas. Con esa brújula elegimos convolución y kernel: caja o Gauss para calmar ruido (sabiendo que cada clic hacia la suavidad apaga un poco la nitidez), y Sobel/Prewitt/derivada del Gaussiano cuando necesitamos que las transiciones salten a primera vista. Si el borde es sagrado, rompo la linealidad: mediana, bilateral, Kuwahara o Rolling-Guidance para limpiar sin borrar contornos. Y cuando el objetivo es un mapa de bordes fiable, aplicamos el algoritmo Canny completo —suavizado, gradiente, NMS, doble umbral y histéresis— porque los bordes no solo hay que detectarlos: hay que hacerlos coherentes.

Después de realzar lo que importa, anclamos la escena con puntos que se repiten: esquinas (FAST, Harris) y manchas (LoG, DoG, DoH). Los tratamos con cariño de ingeniero: multiescala para que sobrevivan al zoom, orientación para que aguanten la rotación, y un recordatorio constante de que la convolución es equivariante (si la imagen se mueve, la respuesta se mueve con ella), y esa previsibilidad la convertimos en invariancia normalizando parches (centro, escala, ángulo, fotometría). Luego viene el apretón de manos: descriptores. Si prima la robustez, SIFT; si manda el tiempo real, BRIEF.

Si hasta ahora nos habíamos quedado con la idea de “imagen = datos” y un mini-pipeline para prepararla, ahora nos quedamos con “vecindario = significado” y teniendo que decidir cómo mezclamos vecinos (lineal o no lineal), qué frecuencias dejamos pasar, qué bordes aceptamos y dónde anclamos puntos que podamos reconocer después. Ese es el kit de herramientas que convierte píxeles en estructura usable.

¡Felicidades! Has finalizado la unidad. Y ahora, ¡a por las prácticas!


## Recursos y enlaces

- [Unidad 2. Filtrado de imágenes y detección de características básicas.](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/c7Gk8Jmf92vk-MVtXiiUxZ5SlfH7Dllv)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/bXu5SRoVXOovPGRDjCzcLTAD38MltBFK)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/tVv0o47nlQKlpqlXa4-i9vwBM8zYRUp3)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/A1DqMKuRfROw3kiTQP8dCfb7Q3yIZb89)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/c0C_1viyfevMGCtoaVtxUa_pxp-ahVcx)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/xZLU6d4KVkdX9EVpcX6naJrqgJJwcUN7)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/2EA4axVu02nlIkfNs1vlMjGa9wMEyJFn)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/N-Te3JUP4om2rELNWo8DGMOyoWztdZab)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/Ps1q4d6OdgrnOAUTpjfL3VvxmDw7GO1P)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/K8ogKdHeglW6hNzTUIJI_x1nfNS8iPPx)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/cQfPc_bsuTeAv8lgYaSbc3aPVPJu-8EX)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/e7DyggEi5K1OvomP4ocWpaFDU3fvBtAQ)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/wFbh4wCztqFrQGMxdNu63xCwfPi-Kp1j)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/KIv0FfPc6ov0BKtmyLF-VzEY0gSJqr5F)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/crfTnYgFBpuP2p3HpmS2GfUkXS_5JRsv)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/rdM_5mU_OfavXkgBRcgknLcYuSioSnYp)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/OsKHmvfpon-cu5IG1R8Kks8KOczsGfCG)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/gdEPOg9yayZDwlW5IKd6J5NMqS1rKc6S)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/MhS6LHJ_j8zUXaTgH3vRqS8pm4rk2Tzk)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/3oLxlJ1w-KFeIn2e6JNoi4Y2FJ5fQyIV)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/ozi7wkMCGsk0XdDbl7kRMhydk6xFs2Zz)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/8ZARdtc3MsvFEOLl6BehKDmw9VOVSlAF)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/O6M1Jx0P1IjjfhTvnHuSVXJg-KhTwWkm)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/AzWHY3eV4N20LwwWdYxNUHXZztYdv6GZ)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739878_1/scormcontent/index.html#/lessons/XpAAEqQBmYT1cCtBxCC2Yeu38T4WXOLc)