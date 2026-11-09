# 2609_INSD4_VICO_A

**SCORM:** _739879_1
**URL del contenido:** https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormdriver/indexAPI.html

## Contenido

### START COURSE

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/preview</sub>

Unidad 3. Redes neuronales y Deep learning.
START COURSE
INTRODUCCIÓN Y OBJETIVOS
Introducción y objetivos
INTELIGENCIA ARTIFICIAL EN VISIÓN POR COMPUTADOR
Introducción
Deep Learning en visión por computador
Hitos del Deep Learning
REPASO DE REDES NEURONALES
Introducción
Neurona biológica
Neurona artificial
Redes Neuronales Artificiales (ANN)
APRENDIZAJE DE LAS REDES NEURONALES
Introducción
Forward: Algoritmo de Propagación
Loss: Funciones de pérdida
Descenso del gradiente y Backpropagation: Algoritmo de retropropagación
Update: Actualización de pesos
Problemas más característicos de las redes neuronales
ENTRENAMIENTO DE LAS REDES NEURONALES
Introducción
División y validación
Sesgo y varianza
PERCEPTRÓN MULTICAPA PARA IMÁGENES
Introducción
¿Cómo vemos las redes neuronales en imágenes?
CONCLUSIONES
Conclusiones de la unidad
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted
Unstarted

### Lesson 1 - Introducción y objetivos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/ALHzL0IhSPSyGjAnd8i4t4LzKC8SojJa</sub>

Introducción y objetivos

Introducción

Imaginemos que pudiéramos enseñar a las máquinas a ver de la misma forma que nosotros entrenamos nuestro cerebro. En las unidades anteriores hemos afinado nuestra mirada de ingeniero: aprendimos a procesar imágenes, mejorar su calidad y extraer características fundamentales. Ahora, en esta unidad, daremos un salto apasionante: veremos cómo las propias máquinas pueden aprender a reconocer patrones visuales por sí solas. Bienvenidos al mundo de las redes neuronales y el deep learning, donde las cámaras dejan de ser simples capturadoras de píxeles para convertirse en aprendices visuales.

Esto marca un cambio de paradigma. Si antes aplicábamos filtros y detectores diseñados manualmente, ahora conoceremos modelos inspirados en el cerebro humano que ajustan sus parámetros automáticamente a partir de datos. ¿Cómo un sistema puede distinguir un perro de un gato tras ver miles de fotos? ¿O cómo un coche autónomo “ve” una señal de stop? Detrás de esos logros están las redes neuronales profundas. En esta unidad exploraremos esas “cajas negras” que han revolucionado la visión por computador, haciendo posible que un algoritmo aprenda por experiencia.

Recordaremos que una red neuronal es como un equipo de neuronas artificiales trabajando en capas: cada “neurona” realiza un cálculo sencillo, pero conectadas en masa logran resolver tareas complejas. Hablaremos del proceso de entrenamiento: cómo la red ajusta sus “sinapsis” (pesos) mediante prueba y error para minimizar sus fallos. Conversaremos sobre nociones intuitivas de aprendizaje automático, como el equilibrio entre aprenderlo todo (a riesgo de recordar hasta el ruido, overfitting) o quedarse corto (underfitting). Hablaremos del término deep learning —aprendizaje profundo— que no es más que usar redes neuronales más grandes y con más capas, capaces de abstraer información en distintos niveles (desde bordes y colores hasta formas y objetos, en el caso de imágenes).

Partiremos de preguntas sencillas, “¿cómo aprende una máquina?”, y emplearemos analogías cotidianas para entender ideas complejas. Antes de sumergirnos en detalles técnicos, pensemos en lo fascinante del desafío: estamos intentando que un programa de computador vea y aprenda del mundo visual como lo haría un ser vivo, aunque con algoritmos y números en lugar de neuronas biológicas. Este viaje promete cambiar tu forma de concebir el software: después de todo, ¿qué puede haber más avanzado que un código que mejora cuantas más experiencias “vive”? Empecemos esta nueva aventura con curiosidad, sabiendo que al final de la unidad habremos dado a nuestras máquinas un toque de inteligencia visual, preparándonos para profundizar aún más en las unidades siguientes.

Click to flip

Inteligencia artificial en visión por computador

Click to flip

Imaginemos que nos dan un montón de fotos sin instrucciones. Antes, resolver algo como “¿aparece un gato?” significaba escribir reglas a mano: si ves orejas puntiagudas, si el contorno se parece a, etc… un rompecabezas infinito. El Deep Learning cambió el juego y en lugar de programar reglas, entrenamos un modelo para que las descubra. Le enseñamos pares imagen → etiqueta, y el modelo ajusta millones de pequeñas perillas ajustes internas (pesos y sesgos) hasta que aprende a distinguir patrones útiles.

Click to flip

Repaso de redes neuronales

Click to flip

En este apartado nos vamos a centrar en hacer un cambio de mirada. Dejaremos de pensar en “escribir condiciones” y pasaremos a pensar en “dejar que la red aprenda conexiones”. Para eso, nos quedaremos con tres ideas clave: (1) cada neurona pondera lo que recibe y decide si “aporta” algo a la siguiente capa; (2) la no linealidad (la activación) es lo que hace que muchas neuronas sencillas juntas construyan patrones complejos; y (3) en visión, una imagen no es más que un conjunto de números que viaja por la red hasta convertirse en una decisión (por ejemplo, “esto es un 3”). Con estas ideas fijadas, el resto de la unidad —entrenamiento, pérdidas, optimizadores— encaja como un mecanismo natural.

Click to flip

Aprendizaje de las redes neuronales

Click to flip

Definida la arquitectura de una red neuronal, es decir, cuántas capas tendrá, cuántas neuronas por capa y qué funciones de activación usarán, el siguiente paso es entrenarla para que realice la tarea deseada. El entrenamiento típicamente se hace de forma supervisada: disponemos de un conjunto de datos de entrada y las salidas esperadas (etiquetas o valores objetivo) para esos datos.

Click to flip

Entrenamiento de las redes neuronales

Click to flip

Entrenar una red neuronal no es un acto puntual, es un proceso iterativo de ensayo, medición, corrección y ajuste. En la sección anterior ya vimos el latido interno de cada iteración (forward → loss → backpropagation → update). Ahora vamos a elevar la vista y ver cómo ese latido se organiza a escala de proyecto: cómo preparamos y dividimos los datos para que el aprendizaje sea honesto, cómo medimos los avances sin engañarnos (validación), cómo decidimos cuándo parar y, sobre todo, cómo navegamos la tensión permanente entre sesgo y varianza para lograr modelos que generalicen bien.

Click to flip

Perceptrón multicapa para imágenes

Click to flip

Hasta ahora, hemos descrito las redes neuronales de forma general, aplicables a datos tabulares o de cualquier tipo. Cuando se trata de imágenes, hay consideraciones especiales debido a su naturaleza espacial. Una imagen típica puede representarse como una matriz 2D (para escala de grises) o 3D (si incluimos canales de color). Por ejemplo, una imagen de 64x64 píxeles en color es esencialmente una matriz .Hasta ahora, hemos descrito las redes neuronales de forma general, aplicables a datos tabulares o de cualquier tipo. Cuando se trata de imágenes, hay consideraciones especiales debido a su naturaleza espacial. Una imagen típica puede representarse como una matriz 2D (para escala de grises) o 3D (si incluimos canales de color). Por ejemplo, una imagen de 64x64 píxeles en color es esencialmente una matriz .

Objetivos

1

Comprender qué es una red neuronal artificial y explicar por qué el deep learning resulta especialmente útil en visión por computador.

2

Interiorizar el flujo completo de aprendizaje de una red: forward → pérdida → backpropagation → update, conectándolo con buenas prácticas de entrenamiento.

3

Adoptar hábitos de experimentación reproducible: división correcta de datos, métricas adecuadas y señales de parada coherentes con los objetivos del problema.

4

Reconocer limitaciones y riesgos comunes (neurona muerta, vanishing/exploding gradients, overfitting/underfitting) y aplicar estrategias de mitigación básicas.

5

Construir una línea base honesta en imágenes pequeñas con un perceptrón multicapa (MLP), entendiendo su valor pedagógico y sus límites.

¡Comenzamos!

### Lesson 2 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/MFQjTOQz-KHVKdCJipItyh1Wm8b1rA72</sub>

Introducción

Imaginemos que nos dan un montón de fotos sin instrucciones. Antes, resolver algo como “¿aparece un gato?” significaba escribir reglas a mano: si ves orejas puntiagudas, si el contorno se parece a, etc… un rompecabezas infinito. El Deep Learning cambió el juego y en lugar de programar reglas, entrenamos un modelo para que las descubra. Le enseñamos pares imagen → etiqueta, y el modelo ajusta millones de pequeñas perillas ajustes internas (pesos y sesgos) hasta que aprende a distinguir patrones útiles.

En este apartado pondremos ese cambio de paradigma en contexto, repasaremos qué es el Deep Learning, para qué se usa hoy en visión y cómo encaja con las redes neuronales que veremos en esta unidad.

¿Todo listo? ¡Empezamos!

### Lesson 3 - Deep Learning en visión por computador

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/QRwICul__cNvRdKiZ-EZxA96Zq-HX71t</sub>

Deep Learning en visión por computador

El Deep Learning (DL) es la forma de aprendizaje automático que usa redes neuronales profundas (muchas capas encadenadas) para aprender representaciones de los datos. Si una red superficial aprende “pocas” transformaciones, una red profunda compone múltiples niveles, es decir, patrones muy simples (contrastes, pequeñas transiciones de intensidad) se combinan en motivos más ricos (trazos, texturas), y estos, en conceptos más nucleares (por ejemplo, el aspecto global de un dígito o un pictograma). Esa composición jerárquica es la clave, cada capa “limpia y reordena” la información para que la siguiente tenga un problema un poco más fácil.

Tres ingredientes hicieron posible su auge:

Datos: pasamos de cientos a millones de ejemplos visuales.

Cómputo: GPUs/TPUs para entrenar en horas lo que antes requería semanas.

Algoritmos y trucos de entrenamiento: activaciones eficaces (ReLU), mejores inicializaciones, optimizadores adaptativos (Adam), normalización, regularización práctica (dropout, early stopping), etc.

Aunque en siguientes unidades entraremos en profundidad en arquitecturas especializadas, aquí nos quedamos con la idea operativa: una red neuronal que toma píxeles y entrega una decisión. El esquema —datos normalizados → red con capas → salida (probabilidades o valores) → función de pérdida → ajuste por retropropagación (backpropagation)— es el que veremos en todas las aplicaciones de visión, cambien o no los “bloques” internos.

Aplicaciones clave (panorama actual):

Clasificación de imágenes: decide la clase principal (“semáforo”, “silla”, “letra A”). Perfecta para empezar a entrenar y diagnosticar modelos (precisión global, clases confusas).

Localización y conteo sencillo: detectar si hay al menos un objeto o cuántos hay, en escenarios controlados (control de calidad visual básico, inventarios).

Segmentación y máscaras simples: cuando no basta con la clase y queremos saber dónde está el objeto (las Próximas unidades profundizarán; aquí lo nombramos para situarte).

OCR básico / lectura de caracteres: desde dígitos hasta letras impresas en tipografías controladas, donde un MLP bien entrenado ya muestra el ciclo de aprendizaje completo.

Restauración elemental (concepto): modelos que aprenden a mejorar imágenes (p. ej., denoising sencillo) a partir de pares “degradada → limpia”.

Clasificación médica de entrada (siempre con cautela): como apoyo inicial a especialistas (ej.: distinguir imágenes normales vs sospechosas en cribados de baja complejidad).

Fijémonos en el patrón común: datos → red → salida, y alrededor, buenas prácticas de entrenamiento. Eso es justo lo que vamos a perfeccionar aquí con redes densas sobre imágenes pequeñas: un taller de mecánica del aprendizaje; así en el futuro, cuando cambie la arquitectura, la mecánica seguirá siendo la misma.

¿Por qué funciona tan bien en visión por computador?

Porque las imágenes tienen redundancia y estructura: hay patrones locales que se repiten (bordes, texturas, letras) y combinaciones de esos patrones que ocurren en objetos del mundo real. Una red neuronal profunda aprende a explotar esas regularidades sin que se las enumeremos. Dado un objetivo claro (la función de pérdida) y suficientes ejemplos, la red ajusta sus parámetros para concentrarse en lo relevante y olvidar el ruido. Y, muy importante, mejora con los datos: cada nuevo lote bien etiquetado es “más experiencia” para el modelo.

### Lesson 4 - Hitos del Deep Learning

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/jrEeeG-TX7KVYfQk8Xp-RgnzNkiFX2IK</sub>

Hitos del Deep Learning

Una mirada rápida, en orden temporal, para situar el progreso que nos ha traído hasta aquí. Nos va a ayudar a entender el recorrido para “colocar las piezas”:

1958 — Perceptrón: la primera neurona artificial con aprendizaje. Inspiró décadas de investigación, aunque pronto se vio su límite en problemas no lineales.

Años 80 — Backpropagation “popularizado”: se (re)descubre y difunde la retropropagación como método eficaz para entrenar múltiples capas. El “latido” que usamos hoy.

Finales 90 — Primeros éxitos en visión controlada: redes que reconocen dígitos o caracteres impresos con gran fiabilidad en datasets acotados.

2006–2011 — “Renacimiento” profundo: técnicas de pre-entrenamiento, activaciones y mejores inicializaciones vuelven entrenable a modelos con varias capas.

2012 — Salto a gran escala: un modelo profundo domina un gran reto de reconocimiento de imágenes a escala masiva; el campo adopta DL como estrategia estándar. (AlexNet)

2014–2015 — Entrenamiento estable y profundo: normalización de activaciones, optimizadores adaptativos (Adam) y arquitecturas más profundas entrenan mejor y más rápido.

2014 — Modelos generativos modernos: redes que crean imágenes sintéticas (adversarios que compiten para mejorar) abren otra vía: no solo reconocer, también sintetizar.

2017 — Atención y nuevas familias de modelos: el mecanismo de “mirar donde importa” permite escalar modelos y entrenar con flujos de datos masivos.

2019–2021 — Pre-entrenamiento y auto-supervisión: aprender sin etiquetas (o con muy pocas) a partir de grandes colecciones se vuelve práctica común; transferir lo aprendido a tareas específicas acelera proyectos.

2021–2024 — Modelos fundacionales y multimodales: sistemas que leen y ven a la vez; el conocimiento visual se integra en asistentes y plataformas capaces de razonar sobre imágenes, texto y más.

Hoy — Producción y responsabilidad: pipelines de MLOps, monitorización, trazabilidad, ética y sesgos; la pregunta ya no es “¿funciona?”, sino “¿funciona siempre, para todos, y cómo lo garantizamos?”.

¡Fantástico! Has completado este apartado.

### Lesson 5 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/WRNhdxECNlfqNDVOCLRezK-9cwxqo1iC</sub>

Introducción

Imaginemos que entramos en un laboratorio donde todo son señales: destellos, impulsos, pequeñas decisiones que se encadenan unas con otras. Ese laboratorio es nuestra metáfora de una red neuronal. En este apartado vamos a preparar la “mochila mental” para entender y entrenar redes con imágenes. No vamos a explorar todavía arquitecturas complejas; vamos a afinar la intuición correcta:

qué es una neurona (primero en el cerebro, luego en el software),

cómo esas neuronas se organizan en capas para transformar información,

y por qué ese mecanismo, tan simple pieza a pieza, logra resolver tareas visuales que, hasta hace poco, exigían diseñar reglas a mano.

En este apartado nos vamos a centrar en hacer un cambio de mirada. Dejaremos de pensar en “escribir condiciones” y pasaremos a pensar en “dejar que la red aprenda conexiones”. Para eso, nos quedaremos con tres ideas clave: (1) cada neurona pondera lo que recibe y decide si “aporta” algo a la siguiente capa; (2) la no linealidad (la activación) es lo que hace que muchas neuronas sencillas juntas construyan patrones complejos; y (3) en visión, una imagen no es más que un conjunto de números que viaja por la red hasta convertirse en una decisión (por ejemplo, “esto es un 3”). Con estas ideas fijadas, el resto de la unidad —entrenamiento, pérdidas, optimizadores— encaja como un mecanismo natural.

### Lesson 6 - Neurona biológica

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/SrFYYEn_gIEMdpuIpkdwpPC3tyOQ-zDl</sub>

Neurona biológica

Pensemos en una neurona como una estación de cruce: llegan señales por múltiples “carreteras” (las dendritas), se acumulan en una rotonda central (el soma) y, si el tráfico supera cierto nivel, la estación abre el paso y lanza un impulso por una gran vía de salida (el axón) hacia otras estaciones (otras neuronas). Cada carretera no pesa lo mismo: hay vías rápidas y otras con peaje; en términos biológicos, eso se denomina sinapsis con diferente fuerza sináptica (algunas excitan, otras frenan). La neurona está continuamente integrando lo que le llega y si el balance final es suficientemente alto, dispara (emite un pulso) y ese pulso influye en sus vecinas.

Dos ideas prácticas para llevarnos al software:

Ponderación + decisión. No todas las entradas valen igual: la neurona da más peso a lo relevante e ignora lo que no suma. Ese es el germen del concepto de peso en la neurona artificial.

Plasticidad. Las conexiones no son fijas: con la experiencia cambian de fuerza. Esa adaptabilidad inspira el aprendizaje en redes: ajustamos los “pesos” para que, con el tiempo, el sistema responda mejor a lo que queremos que detecte.

Con esta imagen en mente, el salto a la neurona artificial resulta natural: sustituimos dendritas por entradas numéricas, fuerza sináptica por pesos ajustables, integración en el soma por suma ponderada + sesgo, y la decisión de disparar o emitir un impulso por una función de activación (que dice cuánto “aporta” la neurona a la siguiente capa). Muchas de estas “estaciones” alineadas forman capas; y varias capas encadenadas construyen significado paso a paso: de señales simples a patrones más complejos.

¿Por qué nos sirve esta historia para visión por computador?

Porque una red no “ve” como nosotros; aprende a responder a patrones en los números. En imágenes, esos números son los píxeles. Si organizamos neuronas en capas, la red puede pasar de pistas muy locales (pequeñas variaciones de intensidad) a configuraciones más ricas (trazos de un dígito, contornos de un icono), y terminar en una decisión (“clase 7, 93%”). En este apartado nos vamos a quedar con la mecánica mental que lo hace posible: ponderar, activar, encadenar. Con eso bien asentado, el entrenamiento que viene después deja de ser una caja negra y se convierte en un proceso que sabemos leer y corregir.

### Lesson 7 - Neurona artificial

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/BtLgnucIzD3WZwiiHsloHLO9CyT5_TWA</sub>

Neurona artificial

Como hemos visto, la neurona biológica, en esencia, es como un interruptor biológico que se enciende solo cuando recibe estímulos suficientes. Este comportamiento inspiró a los investigadores a crear un modelo matemático simplificado de neurona, dando origen a la neurona artificial. Aunque más simple que su símil biológico, la neurona artificial imita su lógica básica de funcionamiento: combinar entradas, ponderarlas según su importancia y producir una salida señalando si la combinación “activó” la neurona.

Una neurona artificial típica (también llamada perceptrón en su forma más simple) consta de: entradas, pesos, un sesgo
 (bias) y una función de activación, que juntas generan una salida. Las entradas son valores numéricos que representan, por ejemplo, características o señales de un problema. Cada entrada lleva asociado un peso, que indica la importancia o influencia de esa entrada en la neurona. La neurona realiza primero una suma ponderada de todas sus entradas: calcula una combinación lineal multiplicando cada entrada por su peso y sumándolos, además de un término extra llamado sesgo (bias). El sesgo es un número que modela el umbral interno de la neurona: actúa como una entrada adicional constante (de valor 1) con un peso propio . En términos matemáticos, la operación interna de la neurona puede expresarse así:

A esta suma ponderada  se le aplica luego una función de activación , produciendo la salida de la neurona:

La función de activación cumple el papel del “umbral” biológico: decide el nivel de activación de la neurona en base a
. Si
es, por ejemplo, una función que devuelve 1 cuando supera cierto valor y 0 en caso contrario, la neurona artificial se comportaría como un detector binario (enciende/apaga). De hecho, el perceptrón original propuesto por Frank Rosenblatt en 1958 usaba una función escalón de este tipo (activación binaria) para imitar el “disparo” todo-o-nada de una neurona real.

Una forma intuitiva de entender la neurona artificial es pensar que “decide” algo a partir de sus entradas. Por ejemplo, imaginemos un pequeño sistema que determine si un email es spam: cada entrada
 podría ser un indicador (¿aparece cierta palabra clave?), y su peso
 representaría qué tan relevante es esa palabra para indicar spam. La neurona suma las evidencias; el sesgo
 ajusta la propensión a declarar “spam” independientemente de las entradas. Si el total
 supera cierto nivel, la neurona (tras la activación) dará una salida alta cercana a 1, señalando “sí, es spam”. Si no, la salida será baja (cerca de 0) indicando “no es spam”. Así, con pesos y sesgo adecuados, una sola neurona puede actuar como un clasificador simple.

Lo poderoso es que la función de activación
 suele ser no lineal, lo que permite que la neurona tome decisiones no triviales. En lugar de una salida meramente proporcional a
, la activación introduce un comportamiento saturado o umbralizado. Un ejemplo clásico es la función sigmoide, definida como
. Esta función tiene forma de “S” suave (de ahí su nombre) y convierte cualquier valor de entrada en un número entre 0 y 1. Valores muy negativos de  darán una salida cercana a 0, valores muy positivos darán salida cercana a 1, y alrededor de
 la transición es gradual. En nuestro ejemplo del email,
 sigmoide podría interpretarse como la “probabilidad” de ser spam según la evidencia acumulada.

Otro ejemplo muy utilizado es la función ReLU (Rectified Linear Unit), definida como
. La ReLU corta los valores negativos (si
, la salida es 0) y deja pasar linealmente los positivos (si
,
). Es decir, actúa como un filtro que bloquea señales por debajo de 0 y transmite sin saturación las superiores a 0. La simplicidad de ReLU la ha hecho muy popular en redes neuronales modernas, porque tiende a facilitar el aprendizaje: al no saturarse para grandes (a diferencia de la sigmoide, que se aplana acercándose a 1), reduce problemas de gradientes pequeños en el entrenamiento de redes profundas.

En imágenes, si  es un pequeño vecindario de píxeles, un conjunto de pesos  puede comportarse como un detector suave de un patrón local (por ejemplo, “más claro a la izquierda que a la derecha”). Varias neuronas con preferencias distintas se combinan para captar trazos y formas cada vez más ricas.

### Lesson 8 - Redes Neuronales Artificiales (ANN)

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/20S9o1neISY8CjtqFNo4sIP-lgXVunNC</sub>

Redes Neuronales Artificiales (ANN)

Hasta aquí hemos visto una neurona artificial aislada. Por sí sola, puede realizar tareas sencillas –como decidir si activar o no un resultado– siguiendo una frontera de decisión relativamente simple (por ejemplo, separar “sí” y “no” linealmente según ). Sin embargo, el verdadero poder surge al interconectar muchas neuronas artificiales en una red. Al igual que las neuronas biológicas se combinan en circuitos cerebrales, las neuronas artificiales se organizan en capas y redes, cooperando para resolver problemas más complejos.

En una red neuronal artificial (ANN) típica, las neuronas se disponen en capas: una capa de entrada que recibe los datos originales, una o varias capas ocultas intermedias que transforman progresivamente la información, y una capa de salida que entrega el resultado final. Cada neurona de una capa (excepto la de entrada) toma como entradas las salidas de la capa anterior.

Por ejemplo, en visión por computador, podríamos tener neuronas de la primera capa detectando patrones básicos en píxeles (bordes, colores); sus salidas alimentan neuronas en la siguiente capa que detectan combinaciones más complejas (formas, texturas), y así sucesivamente, hasta que las últimas neuronas deciden qué clase de objeto aparece en una imagen. En otras palabras, cada neurona artificial aporta una pequeña “decisión” y, combinadas en una red, logran tomar decisiones muy sofisticadas.

Es importante destacar que los pesos  de cada conexión y los sesgos  de cada neurona son los parámetros que definen el comportamiento de la red. Son análogos a lo que en el cerebro serían las fortalezas de las sinapsis o la facilidad con que una neurona se activa. Estos parámetros no se fijan manualmente en tareas complejas, sino que se aprenden a partir de datos: la red neuronal ajusta sus pesos y sesgos automáticamente durante un proceso de entrenamiento, típicamente usando algoritmos como la retropropagación del error con descenso de gradiente, que veremos a lo largo de la unidad.

El objetivo del entrenamiento es encontrar los valores de todos esos pesos  y sesgos  que hagan que la red produzca las salidas correctas para las entradas de ejemplo, minimizando el error. En el caso de una sola neurona, aprender equivale a ajustar su vector de pesos y su bias para que la neurona responda adecuadamente (por ejemplo, que detecte spam con buena precisión). En redes con muchas neuronas, el número de parámetros se dispara (pueden ser miles o millones de pesos), pero gracias a métodos computacionales eficientes es posible ajustarlos automáticamente.

De hecho, durante décadas el entrenamiento de redes neuronales profundas fue inviable por falta de potencia de cómputo, y esa es una de las razones por las que la investigación en redes neuronales “durmió” hasta los avances de los 1990s y, sobre todo, del siglo XXI.

Estructura de las redes neuronales

Podemos distinguir tres tipos de capas en una red simple:

Características básicas de una Red Neuronal

La profundidad de la red viene dada por el número de capas ocultas. Si hay 0 capas ocultas (es decir, las entradas conectan directamente a las salidas), la red se reduce a un modelo lineal simple. Con 1 capa oculta, tenemos lo que se denomina un perceptrón multicapa de una capa oculta, capaz ya de aproximar funciones no lineales básicas. Con múltiples capas ocultas, la red se considera profunda (Deep Neural Network), de ahí el término Deep Learning. Cada capa adicional permite que la red aprenda representaciones más abstractas o de más alto nivel de los datos.

Un concepto importante es que las capas ocultas sucesivas pueden considerarse como extractoras de características jerárquicas. Por ejemplo, en visión por computador (especialmente con redes convolucionales, pero el concepto aplica en general), las primeras capas pueden aprender a detectar patrones muy simples en los datos (por ejemplo, en imágenes: bordes horizontales, verticales, colores básicos), las siguientes capas combinan esos patrones para detectar formas o partes más complejas (esquinas, texturas), y las capas más profundas integran todo para reconocer estructuras de alto nivel (objetos, rostros, etc.). Esta jerarquía automática de características es una de las potencias del Deep Learning frente a los métodos tradicionales donde las características debían definirse manualmente.

En la práctica, una sola capa oculta puede necesitar un número prohibitivo de neuronas para aproximar funciones complejas. Por eso se emplean múltiples capas ocultas: distribuir la complejidad entre varias capas suele ser más eficiente y requerir menos neuronas totales, además de que ciertas funciones son mucho más fáciles de aprender con profundidad (por ejemplo, funciones que compongan patrones a distintos niveles, como reconocimiento visual, lenguaje, etc.).

La capacidad de una red neuronal se incrementa con el número de neuronas y capas, pero ello también aumenta su complejidad y la cantidad de parámetros (pesos y biases) a entrenar.

Por ejemplo, supongamos una red densa sencilla para clasificación de imágenes MNIST (dígitos escritos a mano 28x28):

capa de entrada 784 nodos

una capa oculta de 128 neuronas

y capa de salida de 10 neuronas (para 10 dígitos).

El número de pesos en esa red sería:

En total
 parámetros. A medida que añadimos más capas o neuronas, estos números crecen rápidamente, lo que implica más datos necesarios para entrenar (para evitar sobreajuste) y más coste computacional.

Dado que una red neuronal es básicamente una función paramétrica muy flexible, el objetivo al entrenarla será encontrar los valores adecuados de todos esos parámetros (pesos y sesgos) para que la función implementada se ajuste a la tarea deseada (por ejemplo, predecir correctamente las etiquetas en un problema de clasificación).

import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Datos de entrenamiento para XOR (entrada de 2 bits y salida XOR)
X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
y = np.array([0, 1, 1, 0], dtype=float)

# Definición de una red neuronal con una capa oculta
model = keras.Sequential([
    layers.Dense(2, activation='relu', input_shape=(2,)),  # capa oculta con 2 neuronas ReLU
    layers.Dense(1, activation='sigmoid')                  # capa de salida con 1 neurona sigmoide
])

# Compilar el modelo con un optimizador y una función de pérdida
model.compile(optimizer='adam', loss='binary_crossentropy')

# Entrenar el modelo (ajustar pesos) con los datos XOR
model.fit(X, y, epochs=100, verbose=0)  # 100 épocas, sin mostrar cada paso

# Evaluar las predicciones del modelo ya entrenado
predicciones = model.predict(X)
print("Salidas predichas:", np.round(predicciones.squeeze(), 3))

En este código definimos una red feed-forward muy pequeña: 2 neuronas ocultas (con activación ReLU) y 1 neurona de salida sigmoide. A pesar de su tamaño mínimo, esta red tiene suficiente complejidad para aprender la tabla XOR. Tras entrenar 100 épocas con el algoritmo Adam (un método de descenso de gradiente estocástico avanzado), la red converge a predicciones cercanas a [0, 1, 1, 0] para las cuatro combinaciones de entrada, resolviendo correctamente la tarea XOR que ningún modelo lineal podía.

Este ejemplo muestra cómo podemos implementar fácilmente redes neuronales en código usando Keras, pero es importante entender lo que ocurre bajo la abstracción: internamente Keras inicializa pesos aleatoriamente y usa backpropagation para ajustarlos iterativamente en cada época. En la siguiente sección profundizaremos precisamente en los algoritmos de entrenamiento de redes neuronales.

En el siguiente video vamos a ver un ejemplo de cómo una red neuronal se puede usar para imágenes. No entraremos en detalle de cómo se entrena, define o como se construye esta red neuronal, solo la tomaremos como ejemplo para ver cómo de potentes son las redes neuronales, y su gran utilidad en imágenes.

Play Video
¡Fantástico! Has completado este apartado.

### Lesson 9 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/Hc28CcUOsab0JcBhq_n0p-GEWK7WNV_9</sub>

Introducción

Definida la arquitectura de una red neuronal, es decir, cuántas capas tendrá, cuántas neuronas por capa y qué funciones de activación usarán, el siguiente paso es entrenarla para que realice la tarea deseada. El entrenamiento típicamente se hace de forma supervisada: disponemos de un conjunto de datos de entrada y las salidas esperadas (etiquetas o valores objetivo) para esos datos. El proceso de entrenamiento ajustará los pesos  y bias  de todas las neuronas para minimizar la discrepancia entre las salidas actuales de la red y las salidas esperadas.

Imaginemos que una red neuronal funciona como una red hidráulica de una ciudad, en la que hay: depósitos, válvulas, estrechamientos, bifurcaciones y medidores de presión. En esta analogía, los datos son el agua que entra por la toma principal; las capas son tramos de tubería con válvulas que dejan pasar más o menos caudal; la salida es un manómetro al final de la línea; y el aprendizaje sería el ciclo de explotación (operación y ajuste del sistema):

Dejamos correr el agua (forward),

Leemos los manómetros para saber si llegamos a la presión/caudal objetivo (loss),

Realizamos una inspección río arriba para localizar dónde se generó el exceso o la falta de presión (backpropagation),

Por último, giramos un poco las tuercas de las válvulas (update).

Repetimos este ciclo con distintos caudales y condiciones, hasta que, incluso con demandas nuevas, la red sea capaz de entregar el caudal correcto sin romper tuberías ni desperdiciar agua.

### Lesson 10 - Forward: Algoritmo de Propagación

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/ThcNA1BssmRuToZ35HGFc0Gte9b-WWYi</sub>

Unidad 3. Redes neuronales y Deep learning.
Lesson 9 - Introducción
Forward: Algoritmo de Propagación

Este algoritmo es el que se encarga de procesar la entrada y generar la salida correspondiente.

Entrada: un lote de imágenes ya normalizadas (por ejemplo, en
 o estandarizadas).

Proceso: la información avanza capa a capa. Cada capa: mezcla lineal (pesos y sesgo) + activación (la decisión no lineal).

Salida: un número, una probabilidad binaria o un vector de probabilidades que suma 1.

Objetivo del forward: producir una predicción
. Aún no actualizamos pesos ni miramos errores: sólo pensamos y medimos.

Siguiendo, con el ejemplo del sistema hidráulico de nuestra ciudad, cuando abrimos la compuerta de entrada y el agua fluye hacia delante, estamos en el forward. Cada tramo
, toma el caudal que le llega
, lo mezcla linealmente con sus características hidráulicas
 y su presión base
.

En otras palabras, para cada capa
, cogemos lo procesado en la capa anterior
 donde en el caso de la entrada, es la imagen preprocesada, y hacemos una combinación lineal con los pesos asignados en esta capa
 y sus sesgos
:

Ese
 sería la presión previa a la válvula, es decir lo que vamos a decidir si va a continuar este flujo, hacia los siguientes “tramos” o capas. La válvula en sí es la activación
, donde podemos encontrar diferentes tipos de “válvulas”, a lo que llamamos funciones de activación:

ReLU: se comporta como una llave que sólo abre cuando la presión empuja a favor (si
, pasa; si
, se cierra).

Sigmoide: es como una compuerta que nunca cierra del todo ni abre al 100%,

Softmax es un colector al final que reparte un caudal total entre varias salidas que compiten hasta sumar uno.

En imágenes, si nuestro batch tiene
 ejemplos y la entrada a la capa tiene dimensión
, entonces:

 (m neuronas en la capa)

El funcionamiento de estos algoritmos lo podemos ver desde dos puntos de vista diferentes. Primero, utilizando las librerías básicas de Python de numpy, para poder entenderlo desde un punto de vista más directo.

import numpy as np

def relu(z): return np.maximum(0.0, z)

def softmax(z):
    z = z - np.max(z, axis=1, keepdims=True)  # estabilidad
    exp = np.exp(z)
    return exp / np.sum(exp, axis=1, keepdims=True)

# X: (B, n_in)
# W1: (n_in, h), b1: (h,)
# W2: (h, n_out), b2: (n_out,)
def forward(X, W1, b1, W2, b2):
    Z1 = X @ W1 + b1
    A1 = relu(Z1)
    Z2 = A1 @ W2 + b2
    A2 = softmax(Z2)
    cache = {"X": X, "Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}
    return A2, cache  # cache servirá en backprop

Y, por otro lado, que es el que vamos a usar en los entornos reales, usando las librerías de Keras.

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy

model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation="relu"),
    Dense(10, activation=None)  # logits
])
model.compile(optimizer="adam",
              loss=SparseCategoricalCrossentropy(from_logits=True),
              metrics=["accuracy"])

# Forward "visible" = .predict(...)
# (en entrenamiento, Keras hace forward + loss por ti)
probas = model.predict(x_batch)  # si from_logits=True, esto son logits; aplica softmax si quieres visualizarlas

En el siguiente video vamos a ver algunos ejercicios, para entender cómo funciona el algoritmo de propagación desde un punto de vista teórico, sin implementar ningún código.

Play Video
Lesson 11 - Loss: Funciones de pérdida

### Lesson 11 - Loss: Funciones de pérdida

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/u0imrRgbXI8J7G419O--v7D8kAajGium</sub>

Loss: Funciones de pérdida

Para medir como de bien o mal está realizando la tarea la red, con un cierto conjunto de parámetros, definimos una función de pérdida (también llamada función de coste o error)
. Esta función asigna un número (el error) a las predicciones de la red comparándolas con los valores verdaderos. El vector
 representa todos los parámetros del modelo (todos los pesos y sesgos de todas las neuronas).

Al elegir la función de pérdida, debemos tener en cuenta el tipo de problema.

Problemas de clasificación

En clasificación, la red no solo debe acertar la clase; también debe aprender cómo y con qué confianza llegar a esa decisión. Las funciones de pérdida son el idioma con el que le decimos a la red qué significa “mejorar” cuando el objetivo es asignar probabilidades a clases. Principalmente tenemos tres tipos de funciones de pérdida en clasificación,

Binary Cross-Entropy (BCE): Le aplicamos una penalización a la salida , dependiendo de una probabilidad
. Este tipo de función la podemos aplicar cuando queremos hacer una clasificación binaria o multi-etiqueta (K salidas con sigmoide independiente por etiqueta).

Su valor es pequeño cuando la probabilidad asignada al resultado correcto es alta, y por el contrario crece muchísimo si asignamos una probabilidad alta a un resultado erróneo.

Categorical Cross-Entropy (CCE) (con one-hot): Por el contrario, si tenemos que varias salidas son excluyentes, entonces softmax nos ofrecerá un vector de probabilidades
que suman 1, y entonces tenedremos una pérdida de
.

En esta imagen podemos ver una gráfica de cómo se comporta la función
 para que podamos entender cómo estos valores se van a repartir, en función de la probabilidad elegida,

Como antes, si las hemos asignado las probabilidades altas a una respuesta correcta, entonces el valor devuelto será bajo, mientras que, si nos hemos equivocado confiando en una respuesta, entonces su valor comencerá a crecer.

Por ejemplo, si tenemos una imagen en la cual la red neuronal etiqueta la imagen con la palabra “gato”,

Predicción 1: gato: 0.51, perro: 0.49 → CCE moderada (acierto tímido).

Predicción 2: gato: 0.90, perro: 0.10 → CCE baja (acierto sólido).

Predicción 3: gato: 0.01, perro: 0.99 → CCE muy alta (error sobreconfiado).

Problemas de regresión

En regresión la red no elige una clase: predice un valor continuo (temperatura, precio, ángulo, tiempo). Necesitamos una regla que convierta “cuán lejos” está la predicción del valor real en una señal diferenciable que guíe backpropagation. Esa regla es la función de pérdida en regresión. Tenemos dos tipos principales de funciones de pérdida en regresión,

MSE (Error Cuadrático Medio)

Sensibilidad a outliers (cuadrática).

Máxima verosimilitud si el ruido es gaussiano.

MAE (Error Absoluto Medio)

Robusto a outliers (lineal).

Más “plano” cerca del mínimo → a veces converge más lento.

1
2
3
4
5
1 of 6

El propósito de ambas funciones puede resumirse así:

START
2 of 6
Traducir error numérico en señal de aprendizaje útil

La pérdida devuelve un número continuo que disminuye cuanto más precisa es la predicción.

Sus derivadas (gradientes) indican cómo y cuánto mover los pesos para acercar la salida al valor real.

3 of 6
Alinear el entrenamiento con el coste del problema.

No todos los errores cuestan igual

MSE (cuadrática) penaliza mucho los errores grandes → útil si los “grandes fallos” son muy caros.

MAE (absoluta) penaliza de forma lineal → más robusta a outliers; todos los errores pesan “por igual”.

4 of 6
Dar un marco probabilístico (NLL) a la predicción.

Las pérdidas clásicas son negative log-likelihoods de modelos simples de ruido:

MSE ↔ asume ruido gaussiano con varianza constante.

MAE ↔ asume ruido Laplace (colas más pesadas).

5 of 6
Controlar robustez y estabilidad del entrenamiento

MSE tiene gradiente creciente con el error → converge rápido si no hay outliers, pero puede volverse inestable con valores extremos.

MAE tiene gradiente constante → más robusto, a veces más lento cerca del mínimo.

6 of 6
Respetar rango/escala y transformaciones del objetivo

Si el objetivo está muy escalado, normalízalo (z-score) o usa pérdidas relativas.

Si la salida debe ser positiva o acotada, usamos una activación final adecuada y una pérdida coherente.

### Lesson 12 - Descenso del gradiente y Backpropagation: Algoritmo de retropropagación

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/BlSgPmALXg8dBRP1uq8o_VZ1vXrwNTZ4</sub>

Descenso del gradiente y Backpropagation: Algoritmo de retropropagación

El descenso de gradiente (Gradient Descent) es el algoritmo básico para minimizar funciones de pérdida. Es un método de optimización iterativo que, partiendo de alguna estimación inicial de los parámetros
, realiza actualizaciones graduales en la dirección del negativo del gradiente de la pérdida. Intuitivamente, imaginemos la superficie de la función de pérdida en el espacio de parámetros como un paisaje con colinas y valles.

El gradiente
 en un punto indica la dirección de subida más pronunciada; por tanto, el negativo del gradiente apunta hacia abajo, hacia donde la función decrece más rápidamente. Si damos un pequeño paso en esa dirección, estaremos reduciendo la pérdida.

Matemáticamente, la actualización básica de un parámetro  siguiendo descenso de gradiente es:

donde
 es la tasa de aprendizaje (learning rate), un factor de escala pequeño (como 0.1, 0.01, etc.) que determina el tamaño del paso a dar. Este proceso se repite iterativamente recalculando el gradiente en la nueva posición y actualizando de nuevo, hasta que (idealmente) se alcanza al menos un mínimo local de la función de pérdida.

En el contexto de redes neuronales,
 incluye todos los pesos y biases. Calcular el gradiente completo
 significa encontrar la derivada parcial de
 respecto a cada peso
 en cada capa
 y neurona
. Afortunadamente, existe un algoritmo eficiente para este cálculo: la retropropagación del error (backpropagation).

Backpropagation es un procedimiento que utiliza la regla de la cadena de cálculo diferencial para distribuir el error hacia atrás a través de la red y obtener gradientes para cada parámetro. En pocas palabras, funciona así:

Se realiza una pasada hacia adelante (forward pass) con una entrada, calculando las salidas de cada neurona capa por capa hasta obtener la salida final de la red.

Se evalúa la función de pérdida comparando la salida de la red con la salida deseada (etiqueta).

Luego, en la pasada hacia atrás (backward pass), se calcula cómo varía la pérdida con respecto a la salida de la última capa (gradiente inicial), y se propaga ese gradiente hacia atrás usando las derivadas locales de cada neurona. La derivada local de una neurona es simple: dado
,

es decir, la derivada de la pérdida respecto a la entrada de la neurona es la derivada de la pérdida respecto a su salida multiplicada por la derivada de la activación (regla de la cadena). 

De esta forma, backprop va capa por capa calculando
 y  
 para todos los pesos y biases. Una vez obtenidos los gradientes, se aplican las actualizaciones de los parámetros en sentido contrario (desde la última capa hacia la primera, de ahí "retropropagación").

Con backpropagation, cada ejemplo de entrenamiento nos proporciona gradientes que indican cómo modificar ligeramente cada peso para reducir el error en ese ejemplo. En descenso de gradiente batch (lote completo), se promediarían los gradientes sobre todos los ejemplos antes de actualizar los parámetros una vez por época. Sin embargo, en la práctica es más común el descenso de gradiente estocástico (SGD) o por minibatches: se actualizan los pesos tras calcular los gradientes en un subconjunto pequeño de datos (un batch con, digamos, 32 o 64 ejemplos aleatorios) en lugar de esperar a procesar todo el conjunto.

Este algoritmo revolucionó el campo de las redes neuronales en los 80s al hacer viable el entrenamiento de redes con múltiples capas. Antes, solo se sabían entrenar pesos de una sola capa (perceptrón simple) mediante reglas como la delta rule, pero no había un método general para ajustar pesos de capas ocultas. Backprop, formalizado por Rumelhart, Hinton y Williams en 1986, demostró que la regla de la cadena podía aplicarse eficientemente aprovechando la propia estructura de la red (básicamente es un algoritmo de programación dinámica).

En el siguiente video vamos a ver paso a paso cómo se calcula el gradiente en una red sencilla usando la regla de la cadena, y cómo se actualizan los pesos.

Play Video

### Lesson 13 - Update: Actualización de pesos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/NNz_zJU7YBqSuphGX9IOoPTGGmib0Fwl</sub>

Update: Actualización de pesos

Una vez calculados los gradientes mediante backpropagation, se procede a actualizar los pesos. ¿Cuándo se actualizan exactamente? Depende de la variante de descenso de gradiente elegida:

Descenso de gradiente batch: Se calcula el gradiente sobre todo el conjunto de entrenamiento (sumando las derivadas de cada ejemplo) y se hace una actualización por epoch. Esto garantiza moverse exactamente en la dirección del gradiente total verdadero, pero es ineficiente para grandes datasets y puede quedarse atrapado en mínimos locales poco profundos.

Descenso de gradiente estocástico (SGD): Se calcula el gradiente usando solo un ejemplo (o unos pocos) y se actualiza inmediatamente. Es mucho más ruidoso (el gradiente de un ejemplo no representa exactamente la dirección de mayor descenso global), pero en promedio converge. Tiende a oscilar alrededor del mínimo, pero a explorar mejor la topología de la pérdida, pudiendo escapar de mínimos locales estrechos.

Minibatch gradient descent: Es un punto medio. Se usa un grupo pequeño de ejemplos (por ejemplo 32, 64) para estimar el gradiente y actualizar. Esto vectoriza cálculo (aprovecha GPUs) y suaviza algo la varianza del gradiente sin requerir todo el dataset.

En la práctica, el entrenamiento de redes siempre se hace por minibatches. SGD por minibatches (que a veces se sigue llamando simplemente SGD) es el estándar porque es mucho más rápido (se actualiza varias veces por dataset) y suele ofrecer mejor generalización.

Otro aspecto crucial es elegir la tasa de aprendizaje  adecuada. Si  es muy pequeña, las actualizaciones de los pesos serán diminutas y el entrenamiento convergerá muy lento (podría requerir muchísimas épocas). Si  es muy grande, los pasos podrían pasarse de largo el mínimo y la pérdida incluso puede divergir (los pesos explotan a valores enormes y el error crece). A menudo se comienza con un 
 moderado (ej. 0.01) y se ajusta empíricamente o mediante técnicas de optimización de hiperparámetros. También es común reducir el learning rate progresivamente durante el entrenamiento (estrategias de learning rate decay o schedulers) para afinar la convergencia una vez estamos cerca del mínimo.

Debido a las limitaciones del descenso de gradiente básico, se han desarrollado varios algoritmos de optimización avanzados para acelerar y mejorar la convergencia en redes neuronales:

Momentum: acumula un promedio exponencial de gradientes pasados para suavizar la trayectoria (como dar inercia a las actualizaciones, evitando zigzags). Equivale a agregar un término de velocidad que conserva parte de la actualización anterior.

RMSProp: ajusta el paso dividiendo por la raíz cuadrada de la media móvil de cuadrados de gradientes (Root Mean Square Propagation). Así, si un parámetro experimenta gradientes consistentemente grandes, se le reduce el paso, y viceversa, normalizando en cierto modo la magnitud de actualizaciones por parámetro.

Adam (Adaptive Moment Estimation): combina Momentum + RMSProp. Mantiene promedios móviles tanto de gradientes como de sus cuadrados, adaptando las tasas de aprendizaje para cada parámetro individualmente. Es muy popular por su robustez; suele converger rápido con poca calibración manual de .

Otros: Adagrad (histórico, precursor de RMSProp), Adadelta, Nadam (Adam + Nesterov momentum), etc.

En la práctica, Adam es a menudo la elección por defecto para muchos problemas, aunque no siempre garantiza la mejor generalización. SGD con momentum todavía se usa, especialmente cuando se busca exprimir el mejor rendimiento generalizando (a veces un final de entrenamiento con SGD puro a tasa baja puede mejorar un modelo entrenado con Adam). En esta unidad no profundizaremos en todos estos algoritmos, pero es importante saber que existen y que aprovechan gradientes y tendencias pasadas para ajustar dinámicamente los pasos.

Resumiendo, el entrenamiento típico de una red neuronal consiste en:

Inicializar los pesos  y biases  (p. ej. con pequeños valores aleatorios).

Para cada epoch (iteración sobre el dataset completo):

Dividir datos en minibatches y, para cada minibatch:

Realizar forward pass para obtener predicciones.

Calcular la pérdida media en ese batch.

Realizar backward pass (backpropagation) para obtener gradientes de  respecto a cada parámetro.

Actualizar los parámetros con el algoritmo de optimización elegido (p. ej. SGD, Adam).

Opcionalmente, evaluar la pérdida o exactitud en conjunto de validación para monitorear el progreso (como veremos, esto es útil para detectar sobreajuste).

Repetir hasta que la pérdida converja (o mejore marginalmente) o hasta agotar un número predefinido de épocas.

Este proceso de optimización es la esencia del aprendizaje de la red: los pesos se van "amoldando" a los datos. Al finalizar, esperamos que la red haya capturado las relaciones input-output subyacentes.

### Lesson 14 - Problemas más característicos de las redes neuronales

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/UG2CUSbirlQJZMISqXWlZxFbFCKQ8HET</sub>

Problemas más característicos de las redes neuronales

A medida que las redes ganan profundidad (muchas capas), los algoritmos de optimización enfrentan un problema: los gradientes calculados por backpropagation pueden volverse extremadamente pequeños o grandes conforme se propagan hacia las capas iniciales. Esto se conoce como el problema del vanishing gradient (gradiente que se desvanece) y el exploding gradient (gradiente que explota), respectivamente.

Vanishing gradient (gradiente menguante): Ocurre cuando las derivadas acumuladas a través de múltiples capas tienden a ser muy pequeñas, haciendo que los pesos de capas iniciales prácticamente no se actualicen. Esto suele pasar cuando las funciones de activación saturan sus derivadas a 0 (como la sigmoide o tanh en sus colas). Por ejemplo, si varias capas usan sigmoide, la derivada
 en cada neurona puede ser <0.25 en magnitud (máximo de sigmoide es 0.25 en z=0, pero lejos de 0 es casi 0). Multiplicar muchas de estas derivadas (una por capa) hace que el gradiente total se atenúe exponencialmente. Como resultado, las capas cercanas a la entrada aprenden muy lentamente o nada; la red “olvida” ajustar las primeras capas y se enfoca solo en las últimas.

Exploding gradient (gradiente explosivo): Es lo contrario, los gradientes pueden multiplicarse capa tras capa dando valores astronómicamente grandes. Por ejemplo, si los pesos son inicializados muy grandes o en ciertas arquitecturas recurrentes, la norma del gradiente puede crecer exponencialmente al retropropagar. Esto lleva a actualizaciones enormes de los pesos que pueden desestabilizar completamente el entrenamiento (pérdida da NaN o infinita).

Matemáticamente, ambos fenómenos están relacionados con los autovalores de la matriz de Jacobiano de las transformaciones en cada capa. Si el producto de derivadas (o autovalores) es <1, gradiente decae; si es >1, crece. En redes feed-forward clásicas, el vanishing era más común (especialmente con activaciones sigmoide/tanh). Con ReLU, el problema de vanishing se mitigó en la zona positiva (derivada = 1), pero aún puede haberlo en regiones donde muchas neuronas se saturen a 0 (o en recurrentes con multiplicación recurrente).

Para enfrentar estos problemas:

Se introdujeron técnicas de inicialización de pesos inteligentes (por ejemplo, inicialización Xavier o He), que escogen distribuciones para los pesos de forma que las activaciones y gradientes tengan varianzas controladas a través de las capas.

Surgieron nuevas funciones de activación que mantuvieran gradientes más saludables: ReLU fue una, luego Leaky ReLU, ELU, etc., para evitar regiones grandes de derivada cero.

En redes recurrentes (vistas en unidades avanzadas), se desarrollaron arquitecturas especiales como LSTM o GRU precisamente para impedir la desaparición del gradiente a través del tiempo.

Para exploding gradients, se aplican técnicas como gradient clipping (recorte de gradientes: limitar el valor máximo de un gradiente para evitar saltos gigantes) cuando se detectan gradientes anómalamente grandes.

Pequeño esqueleto Keras “antivanish”

import tensorflow as tf
from tensorflow.keras import layers as L, Sequential, regularizers

def block(units):
    return [
        L.Dense(units, kernel_initializer="he_normal",
                kernel_regularizer=regularizers.l2(1e-4),
                bias_initializer=tf.keras.initializers.Constant(0.0)),
        L.BatchNormalization(),          # mantiene Z en rango útil
        L.LeakyReLU(alpha=0.01),         # no satura y deja pasar gradiente
    ]

model = Sequential([
    L.Flatten(input_shape=(28,28)),
    *block(256),
    *block(256),
    *block(128),
    L.Dense(10, activation=None)         # logits; loss with from_logits=True
])

opt = tf.keras.optimizers.Adam(1e-3)     # paso moderado
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer=opt, loss=loss, metrics=["accuracy"])

Ejemplo “a prueba de explosiones” 

Aquí tienes un trozo de código Keras “a prueba de explosiones” que aplica, de forma directa, las medidas clave para evitar gradient explosion: inicialización correcta (He), normalización por capa, activaciones no saturantes, pérdida estable desde logits, weight decay (L2 / AdamW) y, sobre todo, gradient clipping (tope global a la norma del gradiente) + LR scheduling.

import tensorflow as tf
from tensorflow.keras import Sequential, regularizers
from tensorflow.keras import layers as L

# --- Bloque denso "seguro" contra explosión ---
def safe_block(units, l2=1e-4, alpha=0.01):
    return [
        L.Dense(
            units,
            kernel_initializer="he_normal",              # varianza adecuada (He) p/ReLU
            kernel_regularizer=regularizers.l2(l2),      # weight decay (si no usamos AdamW)
            bias_initializer=tf.keras.initializers.Zeros()
        ),
        L.BatchNormalization(),                          # regula magnitudes intermedias
        L.LeakyReLU(alpha=alpha)                         # no satura + deja pasar gradiente
    ]

# --- Modelo MLP didáctico (imágenes 28x28) ---
model = Sequential([
    L.Flatten(input_shape=(28, 28)),                    # Flatten por claridad didáctica
    *safe_block(256),
    *safe_block(256),
    *safe_block(128),
    L.Dense(10, activation=None)                        # logits → pérdida estable con from_logits=True
])

# --- Optimizador con clipping global (tope de la norma del gradiente) ---
# Opción A: AdamW si tu TF lo soporta (desacopla weight decay)
try:
    opt = tf.keras.optimizers.AdamW(
        learning_rate=1e-3,
        weight_decay=1e-4,                              # weight decay desacoplado (mejor que L2 clásico)
        clipnorm=1.0                                    # CLIPPING: tope global a la norma del gradiente
    )
except Exception:
    # Opción B: Adam + L2 en capas (arriba) y clipping por norma global
    opt = tf.keras.optimizers.Adam(
        learning_rate=1e-3,
        clipnorm=1.0                                    # CLIPPING: evita bandazos destructivos
    )

# --- Pérdida estable: desde logits (softmax estable interno) ---
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# --- Callbacks para estabilidad adicional: bajar LR al estancarse y parar a tiempo ---
cbs = [
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss", factor=0.5, patience=2, verbose=1
    ),
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss", patience=6, restore_best_weights=True
    ),
]

model.compile(optimizer=opt, loss=loss, metrics=["accuracy"])

# Entrenamiento (x_train, y_train, x_val, y_val ya preparados y normalizados)
history = model.fit(
    x_train, y_train,
    validation_data=(x_val, y_val),
    epochs=40,
    batch_size=128,
    callbacks=cbs,
    verbose=2
)

¡Fantástico! Has completado este apartado.

### Lesson 15 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/SCYs10kKcyiWtyFz7GcJyUa2U9MIypPe</sub>

Introducción

Entrenar una red neuronal no es un acto puntual, es un proceso iterativo de ensayo, medición, corrección y ajuste. En la sección anterior ya vimos el latido interno de cada iteración (forward → loss → backpropagation → update). Ahora vamos a elevar la vista y ver cómo ese latido se organiza a escala de proyecto: cómo preparamos y dividimos los datos para que el aprendizaje sea honesto, cómo medimos los avances sin engañarnos (validación), cómo decidimos cuándo parar y, sobre todo, cómo navegamos la tensión permanente entre sesgo y varianza para lograr modelos que generalicen bien.

### Lesson 16 - División y validación

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/qzLuNXuq6CHqvb4eBgNT8QHvpnVBrmcS</sub>

División y validación

Al entrenar cualquier modelo de aprendizaje automático, debemos asegurarnos de evaluar su desempeño de forma honesta, es decir, en datos no vistos durante el entrenamiento. Esto es fundamental para detectar si el modelo está generalizando bien o si simplemente memoriza los datos de entrenamiento (lo que llamamos sobreajuste).

Por ello, usualmente dividimos el conjunto de datos en al menos dos partes: un conjunto de entrenamiento (train set) y un conjunto de prueba (test set). El entrenamiento de la red (ajuste de pesos) se realiza exclusivamente con los datos de entrenamiento. Una vez finalizado, se evalúa el modelo resultante en el conjunto de prueba para estimar su rendimiento en datos nuevos.

Además, es práctica común extraer del conjunto de entrenamiento una porción para usarla como conjunto de validación (validation set). El conjunto de validación sirve para monitorear el desempeño del modelo durante el entrenamiento y para tomar decisiones de hiperparámetros. Por ejemplo, podemos entrenar la red por varias épocas e ir calculando la pérdida (y exactitud, si es clasificación) tanto en train como en validation al final de cada época. Si vemos que la pérdida de entrenamiento sigue bajando, pero la de validación empieza a subir, indicaría sobreajuste a partir de cierta época, y podríamos detener el entrenamiento (early stopping) en ese punto óptimo de validación. También usamos la validación para probar diferentes configuraciones (número de neuronas, tasa de aprendizaje, etc.) y elegir la que mejor valía en validación. Una vez fijado el modelo final, se evalúa en test solo una vez.

Típicamente, la partición es algo así como 70%-80% de datos para entrenamiento, 20%-15% para validación, y 10%-15% para prueba, aunque varía. Cuando el dataset es pequeño, a veces no se desea desperdiciar muchos datos en validación; en tales casos se puede usar validación cruzada (k-fold).

Bajemos a tierra los protagonistas del entrenamiento: quién cocina (train), quién prueba (validación) y quién paga la cuenta (test).

Train. Aquí el equipo aprende: el modelo ve ejemplos, calcula gradientes y ajusta pesos. Todo lo que “se entrena” ocurre aquí. También es donde se ajustan (fit) las “salsas base” de datos: escalados, normalizaciones, PCA, codificadores… Se aprenden con train y luego se aplican a val y test sin volver a mirar sus etiquetas ni recalcular parámetros.

Validación (val). No cocina, opina. Sirve para tomar decisiones durante el desarrollo: seleccionar arquitectura, learning rate, regularización, activar early stopping o ReduceLROnPlateau, elegir el umbral de clasificación que optimiza tu F1 o PR-AUC, etc. Es un espejo honesto siempre que no filtre nada hacia train. En visión, no se aplican augmentations aleatorios en val: queremos ver el plato como saldrá a sala.

Test. Es el examen final. Lo tocamos sólo una vez al terminar. Nada de “lo miro y retoco”. Su trabajo es estimar cómo se rendirá fuera del cuaderno. Si lo consultamos y después ajustamos hiperparámetros, deja de ser examen y pasa a ser otra validación más (sesgo optimista garantizado).

Cuando una foto no basta: K-fold y por qué (y cómo) usarlo

Una sola partición train/val puede darnos una “foto” afortunada o desafortunada del rendimiento. K-fold es una técnica donde no fijamos un único conjunto de validación, sino que realizamos k iteraciones de entrenamiento, cada vez usando un fragmento distinto de los datos como validación y el resto como entrenamiento, y promediamos resultados.

Por ejemplo, en 5-fold cross-validation, dividimos los datos en 5 bloques de igual tamaño; entrenamos 5 modelos diferentes, cada uno usando 4 bloques de train y 1 bloque distinto de validación. Al final promediamos las métricas de validación de las 5 corridas. Esto da una estimación más robusta del rendimiento y aprovecha mejor los datos (cada ejemplo fue usado como validación exactamente una vez).

Sin embargo, entrenar k veces es costoso, por lo que en redes neuronales grandes (donde cada entrenamiento ya es largo) no suele hacerse 5-fold CV completo, sino que se conforma con un hold-out (una sola separación train-val). La validación cruzada es más común en modelos simples o datasets pequeños, para comparar modelos.

Aquí podemos ver un ejemplo de cómo usar K-fold,

import numpy as np
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = []

for fold, (tr_idx, va_idx) in enumerate(skf.split(X, y), 1):
    X_tr, y_tr = X[tr_idx], y[tr_idx]
    X_va, y_va = X[va_idx], y[va_idx]

    # Ajustes SOLO en train del fold
    scaler = StandardScaler().fit(X_tr)
    X_tr = scaler.transform(X_tr)
    X_va = scaler.transform(X_va)

    # Define y entrena tu modelo Keras aquí...
    # model.fit(X_tr, y_tr, validation_data=(X_va, y_va), ...)

    # Evalúa y guarda la métrica de interés (p. ej., PR-AUC o F1)
    scores.append(val_metric)

print(f"Métrica media K-fold: {np.mean(scores):.4f} ± {np.std(scores):.4f}")

¿Por qué es tan importante separar los datos? Porque si ajustáramos y evaluáramos el modelo en los mismos datos, incurriríamos en sobreajuste por evaluación. Un modelo suficientemente complejo (como una red neuronal con muchos parámetros) puede lograr errores de entrenamiento arbitrariamente bajos, incluso cero errores en entrenamiento, si tiene capacidad de memorizar cada ejemplo. Pero ese rendimiento perfecto no se traducirá en igual rendimiento en datos nuevos, si lo que ha hecho es simplemente recordar respuestas en lugar de captar patrones generales.

### Lesson 17 - Sesgo y varianza

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/Yoq30hHP0F6yw6lNxvaLCrWAJNVXu2nn</sub>

Sesgo y varianza

Imaginemos que tenemos una manta y queremos entrenar un modelo como dormir y no tener frio. Si nos tapamos demasiado la cabeza (es decir, un modelo muy simple), se nos enfrían los pies: el sistema no alcanza a capturar la estructura del problema y comete errores sistemáticos. Es el sesgo o bias. Por el contrario, si tiramos demasiado de la manta hacia los pies (usamos un modelo muy flexible), podemos cubrir todos los detalles del juego de entrenamiento… pero nos quedamos destapado de nuevo: con datos nuevos el rendimiento fluctúa y el modelo no generaliza. Es la varianza.

Entrenar bien consiste en tensar la manta lo justo, ni más ni menos, y eso exige saber leer las curvas, interpretar las señales y mover los mandos adecuados en cada situación.

Decimos que un modelo sobreajusta cuando aprende demasiado los detalles y ruido del conjunto de entrenamiento, perdiendo capacidad de generalización. Un signo claro de sobreajuste es cuando el error en entrenamiento sigue disminuyendo (el modelo cada vez se ajusta más a esos datos), pero el error en validación empieza a empeorar. En ese punto, el modelo está sobre-entrenándose en patrones específicos del train que no se repiten en val.

Por el contrario, un modelo subajusta cuando ni siquiera logra buen desempeño en los datos de entrenamiento; es decir, la capacidad del modelo es insuficiente para capturar la estructura subyacente aún en train. Se manifiesta con errores de entrenamiento altos.

Esto conecta con la noción de bias (sesgo) y variance (varianza) del modelo:

Un modelo con alto bias es demasiado rígido o simple, incapaz de aprender las relaciones verdaderas, por lo que tiene error alto en entrenamiento (subajuste). En otras palabras, tiene un sesgo fuerte que le impide ajustarse a la complejidad de los datos.

Un modelo con alta varianza es demasiado flexible, ajusta las peculiaridades de cada conjunto de datos de entrenamiento, por lo que, aunque el error en entrenamiento pueda ser bajo, la variabilidad entre distintos conjuntos es grande y típicamente error alto en validación (sobreajuste).

El compromiso bias-variance implica que debemos encontrar el balance adecuado: un modelo con suficiente complejidad para tener bias bajo (capturar bien la estructura) pero suficiente regularización o limitación para mantener baja la varianza (no volverse loco ajustando ruido).

Caso 1: Bajo bias, baja varianza (esquina superior izquierda): dardos agrupados en el centro - el ideal, modelo preciso y consistente.

Caso 2: Alto bias, baja varianza (esquina superior derecha): los dardos (predicciones) caen todos juntos, pero lejos del centro. El modelo es consistente pero inexacto (subajuste: error sistemático).

Caso 3: Bajo bias, alta varianza (esquina inferior izquierda): los dardos en promedio apuntan al centro (el modelo tiene capacidad de acertar), pero están muy dispersos. A veces da en el blanco y a veces se equivoca mucho dependiendo del caso (sobreajuste: sensitive al conjunto).

Caso 4: Alto bias, alta varianza (esquina inferior derecha: dispersos y lejos del centro - modelo malo en general.

Nuestra meta es movernos de los extremos (sobreajuste o subajuste) hacia un modelo equilibrado con buen desempeño en cualquier conjunto.

En las redes neuronales, al ser modelos muy expresivos (muchos parámetros), el peligro suele inclinarse hacia el sobreajuste si no se toman medidas. Por eso, además de separar datos de validación, se emplean técnicas de regularización para controlar la complejidad efectiva del modelo, que se verán con más detalle en unidades posteriores.

Volviendo a la detección práctica: típicamente graficamos la pérdida de entrenamiento y validación a lo largo de las épocas.

Si ambas curvas bajan y luego se estabilizan convergiendo a valores similares, el modelo está en buen punto (no parece sobreajuste grave).

Si la pérdida de validación empieza a subir mientras la de entrenamiento sigue bajando, se está produciendo sobreajuste a partir de cierta época. La diferencia entre ambas curvas es la brecha de generalización. En ese caso, una estrategia es detener el entrenamiento en la época de mínima pérdida de validación (punto de early stopping).

Si ambas curvas se estabilizan, pero en un valor de error todavía alto, y encima cercanos el uno al otro, indicaría subajuste: el modelo no fue capaz de ni siquiera ajustarse al train (posiblemente demasiado simple, o entrenado insuficientes épocas, o con optimizador mal configurado). Allí la solución puede ser incrementar capacidad (más neuronas/capas) o mejorar la optimización (más épocas, lr mayor, etc.).

¿Qué podemos ver en estas gráficas?

PANEL A (UNDERFITTING)
PANEL B (OVERFITTING)

En este panel, observamos que tanto la curva de pérdida de entrenamiento (Train Loss) como la curva de pérdida de validación (Val Loss) son relativamente altas al final del entrenamiento.

Además, ambas curvas tienden a seguir disminuyendo, o al menos no se han estabilizado completamente.

Esto indica que el modelo es demasiado simple (pocas neuronas) o no se ha entrenado durante suficientes épocas para aprender patrones complejos en los datos.

El modelo no tiene la capacidad suficiente para ajustarse bien ni a los datos de entrenamiento ni a los datos nuevos de validación.

La línea roja punteada sugiere que deberíamos 'Entrenar más' o considerar usar un modelo 'más complejo' para reducir ambas pérdidas.

En resumen:

Underfitting: El modelo es demasiado simple o no ha sido entrenado lo suficiente. No se ajusta bien a los datos de entrenamiento ni de validación.

Overfitting: El modelo es demasiado complejo o ha sido entrenado durante demasiado tiempo. Se ajusta muy bien a los datos de entrenamiento, pero pierde capacidad de generalización a datos nuevos.

Aquí tenemos un ejemplo de cómo se aplica en código cuando tenemos alto sesgo o alta varianza,

from tensorflow.keras import layers as L, regularizers as R, Sequential

# Partimos de un modelo base
def make_base():
    return Sequential([
        L.Input(shape=(28, 28, 1)),
        L.Flatten(),
        L.Dense(256, kernel_initializer="he_normal"),
        L.BatchNormalization(), L.ReLU(),
        L.Dense(128, kernel_initializer="he_normal"),
        L.BatchNormalization(), L.ReLU(),
        L.Dense(10, activation=None)  # logits
    ])

# Si huele a ALTO SESGO (underfitting): sube capacidad con moderación
def make_more_capacity():
    return Sequential([
        L.Input(shape=(28, 28, 1)),
        L.Flatten(),
        L.Dense(384, kernel_initializer="he_normal"),
        L.BatchNormalization(), L.ReLU(),
        L.Dense(192, kernel_initializer="he_normal"),
        L.BatchNormalization(), L.ReLU(),
        L.Dense(10, activation=None)
    ])

# Si huele a ALTA VARIANZA (overfitting): refuerza regularización
def make_more_regularized():
    return Sequential([
        L.Input(shape=(28, 28, 1)),
        L.Flatten(),
        L.Dense(256, kernel_initializer="he_normal",
                kernel_regularizer=R.l2(1e-4)),      # L2 suave
        L.BatchNormalization(), L.ReLU(),
        L.Dropout(0.3),                             # Dropout moderado
        L.Dense(128, kernel_initializer="he_normal",
                kernel_regularizer=R.l2(1e-4)),
        L.BatchNormalization(), L.ReLU(),
        L.Dropout(0.3),
        L.Dense(10, activation=None)
    ])

Sesgo y varianza no son dos monstruos abstractos: son dos maneras en las que el entrenamiento se aleja de su destino. La buena noticia es que se reconocen y se corrigen con hábitos simples: observar train/val con atención, mover un dial cada vez, y alinear siempre la evaluación con el objetivo real del proyecto. Cuando lo hacemos, esa manta corta deja de ser un problema y se convierte en una ventaja: sabemos exactamente cuánto tensarla, dónde sujetarla y cuándo detenernos. El resultado es un modelo que aprende lo importante, olvida lo superfluo y llega a producción con un comportamiento predecible. Y eso —más que cualquier arquitectura rimbombante— es lo que separa a un sistema fiable de uno que solo luce bien en la demo.

En el siguiente video, vamos a ver de manera visual de sobreajuste vs subajuste: primero un modelo de grado 1 (lineal) que subajusta (la línea no captura la curva real de datos), luego un modelo de grado altísimo que sobreajusta (la curva pasa por todos los puntos, pero oscila extrañamente entre ellos), y finalmente un modelo de complejidad intermedia que generaliza mejor. Esto ayuda a visualizar cómo se ven en la práctica un modelo con bias alto, con varianza alta, y con buen equilibrio.

Play Video

En el contexto de esta unidad, al entrenar nuestras redes neuronales básicas, aplicaremos estas ideas: siempre separaremos datos de entrenamiento y validación para monitorizar el rendimiento. Por ejemplo, cuando entrenemos una red en Keras (como se verá en la Unidad 4 con CNNs), usaremos parámetros como validation_split=0.1 en model.fit
(opens in a new tab)
() o proveeremos un conjunto de validación para que el framework nos reporte la métrica de validación cada época. Esto nos permitirá, incluso automáticamente, usar callbacks como EarlyStopping para frenar cuando la métrica no mejora en validación.

Finalmente, una vez entrenado y ajustado el modelo, se evalúa en el conjunto de prueba para obtener su rendimiento final estimado. Esa métrica se reporta como la capacidad del modelo (p.ej., “la red neuronal alcanza un 95% de exactitud en clasificación de dígitos en la prueba, superando el 90% de la técnica tradicional XYZ”).

¡Fantástico! Has completado este apartado.

### Lesson 18 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/ZWb8TM0Z6IhCQMHHdlbPsM7ULf_Ad9pw</sub>

Introducción

Hasta ahora, hemos descrito las redes neuronales de forma general, aplicables a datos tabulares o de cualquier tipo. Cuando se trata de imágenes, hay consideraciones especiales debido a su naturaleza espacial. Una imagen típica puede representarse como una matriz 2D (para escala de grises) o 3D (si incluimos canales de color). Por ejemplo, una imagen de 64x64 píxeles en color es esencialmente una matriz .

### Lesson 19 - ¿Cómo vemos las redes neuronales en imágenes?

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/7OGsZjMu3skY3eVssfHkbKG64j9CEWMR</sub>

¿Cómo vemos las redes neuronales en imágenes?

Las redes neuronales que hemos visto no pueden operar directamente con matrices; sus neuronas esperan vectores de entrada. Por tanto, para alimentar una imagen a una red neuronal densamente conectada, se debe aplanar (flatten) la imagen a un vector unidimensional concatenando filas o columnas. Es decir, convertimos la matriz  en un vector de tamaño .

Por ejemplo, una imagen 28x28 (como las de MNIST) se convierte en un vector de 784 valores antes de entrar a la red. Esta operación la realiza una capa de tipo Flatten en muchos frameworks (en Keras, layers.Flatten() se coloca al inicio del modelo para transformar automáticamente la imagen en un vector).

El aplanamiento permite alimentar imágenes a una red neuronal, pero introduce problemas: al tirar la imagen como un vector, la red pierde toda la noción de estructura espacial de los píxeles. Las neuronas en la primera capa tratarán cada píxel de forma independiente sin saber cuáles están cerca unos de otros en la imagen original. En consecuencia:

Patrones locales que en la imagen son significativos (por ejemplo, un borde vertical que abarca píxeles adyacentes en una columna) no son fáciles de capturar por una neurona densa sin entrenar, porque esa proximidad no está explícita – tiene que aprenderla de cero a partir de los datos.

El número de pesos se vuelve enorme muy rápido para imágenes medianas o grandes. Una imagen de  (que es bastante pequeña comparada con fotos reales) tiene 65,536 píxeles por canal; si es en color,  entradas. Una sola neurona oculta conectada a todos esos píxeles tendría 196k pesos. Si tenemos 100 neuronas ocultas, son ~19.6 millones de pesos solo en la primera capa. Esto es manejable con hardware actual, pero para imágenes más grandes (e.g. $1024 \times 1024$) la cantidad de parámetros se vuelve insostenible y la red sería muy lenta de entrenar y propensa a sobreajuste por tantos grados de libertad.

Además, las redes neuronales no son invariantes a traslaciones u otras transformaciones locales de la imagen. Un patrón (digamos una arista diagonal) aprendido en una posición específica de la imagen no será reconocido si aparece en otra posición, a menos que la red haya aprendido redundante ese patrón en múltiples neuronas para cubrir distintas áreas. Esto difiere de, por ejemplo, el ojo humano o los enfoques de visión clásicos donde uno desea detectar un patrón independientemente de dónde esté.

Todos estos motivos llevaron a desarrollar arquitecturas especiales para visionado de imágenes: las redes neuronales convolucionales (CNNs), que veremos en la siguiente unidad. Las CNN introducen la noción de filtros “aprendibles” que se desplazan sobre la imagen (convoluciones), conservando relaciones espaciales locales y usando muchos menos pesos al explotar la idea de campo receptivo limitado y pesos compartidos. En esencia, una CNN aprende detectores de características que son invariantes a la posición, resolviendo gran parte de las limitaciones mencionadas.

Pero antes de adelantar acontecimientos, es importante recalcar que sí es posible usar redes neuronales con imágenes a pequeña escala o para ciertos fines, solo que no es lo más eficiente. De hecho, el ejemplo histórico de redes neuronales en visión (previo a las CNN) era usar redes pequeñas para imágenes muy reducidas (como dígitos 8x8). A medida que se intentó escalar a imágenes más grandes, se vieron obligados a inventar las CNN (LeCun et al., 1989, para reconocer dígitos de 28x28 ya introdujeron CNNs, precisamente por estas ventajas).

A pesar de estas limitaciones, ejercitar la comprensión entrenando un perceptrón multicapa simple en un conjunto de imágenes pequeño es instructivo. Por ejemplo, si entrenamos una red densamente conectada en el dataset MNIST de dígitos (28x28 en escala de grises), podríamos lograr una precisión decente (~92-95%) con una capa oculta de tamaño moderado, aunque una CNN alcanzaría >98% fácilmente. El MLP puede confundir dígitos que una CNN distinguiría mejor debido a que la CNN aprovecha estructuras locales (como la presencia de un bucle arriba indicando un "9" vs un "4", etc.).

En el siguiente vamos a ver un ejemplo con TensorFlow Playground aplicando una red neuronal a datos visuales. Vamos a ver las funciones de activación, cómo los pesos evolucionan, etc.

Play Video

El siguiente código arma el esqueleto del perceptrón multicapa para imágenes. Debemos observar que parametrizamos el tipo de cabeza (“sigmoid”, “softmax” o “linear”) y dejamos el criterio de pérdida como algo que podremos elegir según la tarea en la próxima unidad. Aquí nos interesa ver shapes, flujo y estabilidad del entrenamiento.

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras import layers as L
from tensorflow.keras import callbacks as C

def make_mlp_baseline(input_shape=(28, 28, 1), head="sigmoid", out_dim=1,
                      width=(256, 128), dropout=0.3):
    layers = [L.Input(shape=input_shape), L.Flatten()]
    for units in width:
        layers += [
            L.Dense(units, kernel_initializer="he_normal"),
            L.BatchNormalization(),
            L.ReLU()
        ]
    if head == "sigmoid":
        layers += [L.Dense(out_dim, activation="sigmoid")]
    elif head == "softmax":
        layers += [L.Dense(out_dim, activation="softmax")]
    else:  # "linear"
        layers += [L.Dense(out_dim, activation=None)]
    return Sequential(layers)

model = make_mlp_baseline(input_shape=(28, 28, 1), head="sigmoid", out_dim=1)

# Optimizador y callbacks para un entrenamiento estable (la pérdida dependerá de tu objetivo en la siguiente unidad)
opt = tf.keras.optimizers.AdamW(1e-3, weight_decay=1e-4, clipnorm=1.0)
model.compile(optimizer=opt, loss="mse", metrics=["mae"])  # placeholder genérico

cbs = [
    C.ModelCheckpoint("mlp_baseline.keras", save_best_only=True, monitor="val_loss"),
    C.ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=2),
    C.EarlyStopping(monitor="val_loss", patience=6, restore_best_weights=True)
]

# Ejemplo de fit (X_img: [N,H,W,1] normalizado; y_target: vector/escalares compatibles con tu cabeza de salida)
# history = model.fit(X_img_train, y_train, validation_data=(X_img_val, y_val),
#                     epochs=40, batch_size=128, shuffle=True, callbacks=cbs)

¡Fantástico! Has completado este apartado.

### Lesson 20 - Conclusiones de la unidad

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/6E521jOzeOe3T9-z5tz_MqvrIbSgm5SM</sub>

Conclusiones de la unidad

A lo largo de esta unidad hemos desentrañado el corazón del aprendizaje automático en visión por computador. Comenzamos imaginando neuronas artificiales sencillas y terminamos construyendo arquitecturas profundas capaces de aprender de los datos. Ahora comprendemos que una red neuronal no es magia ni adivinación: es el fruto de muchos pequeños ajustes hechos con método y paciencia, mediante algoritmos de entrenamiento que refinan sus conexiones paso a paso.

Hemos visto cómo una red aprende por experiencia: recibe una imagen, comete un error en su predicción y luego se corrige a sí misma. Ese mecanismo iterativo de retropropagación de error (backpropagation) ha dejado de ser un concepto abstracto para convertirse en algo tangible: imaginamos los pesos de la red ajustándose como si fueran ajustes de una radio buscando la señal óptima. También reflexionamos sobre las buenas prácticas al entrenar: dividir los datos en entrenamiento, validación y prueba nos enseñó la importancia de evaluar un modelo con ojos críticos, para evitar tanto el exceso de confianza (sobreajuste) como la ignorancia por falta de aprendizaje (subajuste). Aprender a manejar el equilibrio bias-variance ya nos prepara para construir modelos más robustos en el futuro.

Anteriormente, habíamos afinado imágenes y extraído características manualmente, y en esta unidad hemos dado vida a un modelo capaz de aprender esas características por su cuenta. Es un cambio de enfoque sutil pero poderoso: pasamos de programar soluciones paso a paso a programar la capacidad de aprender. Este cambio nos obliga a pensar de forma diferente, a confiar en los datos y en algoritmos estadísticos para resolver problemas visuales.

Ahora ya no vemos a una red neuronal como un cúmulo incomprensible de matemáticas, sino como un aliado en la resolución de problemas complejos, al que debemos guiar con buenos datos y parámetros adecuados. Hemos ganado intuición para diagnosticar si nuestro modelo “está estudiando de memoria” o “entiende de verdad” (y sabes qué hacer en cada caso).

En resumen, terminamos la unidad con una base sólida en redes neuronales y deep learning. Esta base será esencial en las próximas unidades, donde profundizaremos en redes especializadas como las convolucionales. El camino del aprendizaje profundo apenas comienza, pero ya hemos dado un paso fundamental para recorrerlo con confianza y curiosidad.

¡Felicidades! Has finalizado la unidad. Y ahora, ¡a por las prácticas!


## Recursos y enlaces

- [Unidad 3. Redes neuronales y Deep learning.](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/ALHzL0IhSPSyGjAnd8i4t4LzKC8SojJa)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/MFQjTOQz-KHVKdCJipItyh1Wm8b1rA72)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/QRwICul__cNvRdKiZ-EZxA96Zq-HX71t)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/jrEeeG-TX7KVYfQk8Xp-RgnzNkiFX2IK)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/WRNhdxECNlfqNDVOCLRezK-9cwxqo1iC)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/SrFYYEn_gIEMdpuIpkdwpPC3tyOQ-zDl)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/BtLgnucIzD3WZwiiHsloHLO9CyT5_TWA)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/20S9o1neISY8CjtqFNo4sIP-lgXVunNC)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/Hc28CcUOsab0JcBhq_n0p-GEWK7WNV_9)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/ThcNA1BssmRuToZ35HGFc0Gte9b-WWYi)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/u0imrRgbXI8J7G419O--v7D8kAajGium)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/BlSgPmALXg8dBRP1uq8o_VZ1vXrwNTZ4)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/NNz_zJU7YBqSuphGX9IOoPTGGmib0Fwl)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/UG2CUSbirlQJZMISqXWlZxFbFCKQ8HET)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/SCYs10kKcyiWtyFz7GcJyUa2U9MIypPe)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/qzLuNXuq6CHqvb4eBgNT8QHvpnVBrmcS)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/Yoq30hHP0F6yw6lNxvaLCrWAJNVXu2nn)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/ZWb8TM0Z6IhCQMHHdlbPsM7ULf_Ad9pw)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/7OGsZjMu3skY3eVssfHkbKG64j9CEWMR)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/index.html#/lessons/6E521jOzeOe3T9-z5tz_MqvrIbSgm5SM)
- [IMG](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/assets/UTAD_ISD_VC_imagen14.jpg)
- [IMG](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/assets/UTAD_ISD_VC_imagen12.jpg)
- [SOURCE](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/assets/UTAD_ISD_VC_video2.mp4?v=1)
- [IMG](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_739879_1/scormcontent/assets/UTAD_ISD_VC_video2.jpg)