# 2609_INSD4_VICO_A

**SCORM:** _783731_1
**URL del contenido:** https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormdriver/indexAPI.html

## Contenido

### Lesson 25 - Conclusiones de la unidad

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/kIIH8ThNKIcgKkNhtbX6lrPNF4u4Xywp</sub>

Unidad 1. Fundamentos de Visión por computador e imagen digital.
Lesson 24 - Ecualización adaptativa de histograma por contraste (CLAHE)
Conclusiones de la unidad

Al llegar al final de esta unidad ya no miramos una imagen como un cuadro bonito, sino como un conjunto ordenado de datos. Ese cambio de mirada —de la escena al número— es lo que da sentido a todo lo que hemos ido construyendo: entender que cada píxel es una medida, que la imagen es una matriz y que lo que hacemos al procesarla es transformar colecciones de valores para volverlos más informativos. Con esa idea en mente, las piezas encajan solas. Saber cómo se adquiere la señal y cómo se lee —esa diferencia práctica entre la lectura secuencial de un CCD y la lectura paralela por columnas de un CMOS— nos da solución frente a muchos “misterios” del día a día: por qué unas cámaras son más rápidas, por qué aparece cierto artefacto al capturar movimiento, o por qué dos dispositivos ven ligeramente distinto lo mismo. Cuando entendemos el origen de los números, podemos empezar a reconocer sus huellas en los resultados.

Con la representación clara y el color bajo control, aparece el que quizá sea el instrumento más valioso para entender las imágenes desde sus entrañas: el histograma. Mirarlo es como tomarle el pulso a la imagen. Podemos entender de un vistazo si los tonos están apretujados en sombras, si las luces están lavadas, si hay dos montículos que delatan un fondo y un objeto bien diferenciados. Y, sobre todo, conociendo el histograma en profundidad, podemos proceder a actuar en consecuencia: invertir intensidades cuando nos conviene cambiar la “polaridad” del problema; ajustar la gamma para rescatar detalle sin desordenar el brillo; estirar el contraste para ocupar todo el rango disponible; ecualizar para redistribuir la información y hacer aflorar matices que estaban comprimidos; hacerlo de forma adaptativa —y con limitación— cuando la escena es desigual y el ruido acecha; o, directamente, convertir una imagen en una decisión nítida con una buena umbralización guiada por la forma del propio histograma. No hay fórmulas intimidantes detrás de estas ideas: hay intuición, lectura de distribuciones y mapeos sencillos que cambian la utilidad de la imagen de manera radical.

Este recorrido no es un catálogo de trucos sueltos, sino un flujo que prepara cualquier imagen para lo que venga después. Si nos toca segmentar, ya no “probaremos umbrales” a ciegas: sabremos leer la separación que nos propone el histograma y elegir con criterio o delegar en un método automático sensato. Si construimos descriptores o alimentamos un modelo que aprende, agradeceremos haber estabilizado la distribución de intensidades y haber normalizado el color: los algoritmos son menos caprichosos cuando les proporcionamos datos consistentes. Y si un día algo falla, tendremos bases para diagnosticar: ¿es la captura?, ¿es la iluminación?, ¿es el rango mal aprovechado?, ¿es un umbral mal colocado?

Con los conceptos que hemos ido describiendo a lo largo de la unidad, las técnicas posteriores —desde un simple realce hasta un sistema de reconocimiento— dejan de ser cajas negras: entenderemos qué necesitan ver y cómo dárselo. Esa es la verdadera ganancia de esta unidad: hemos aprendido a ver con ojos de ingeniero y a convertir imágenes en datos bien puestos sobre la mesa, listos para ser analizados, filtrados, descritos o aprendidos con mucha más eficacia en los siguientes pasos del camino.

¡Felicidades! Has finalizado la unidad. Y ahora, ¡a por las prácticas!

### Índice del contenido

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/</sub>

Completed
Unidad 1. Fundamentos de Visión por computador e imagen digital.
RESUME COURSE
INTRODUCCIÓN Y OBJETIVOS
Introducción y objetivos
VISIÓN FÍSICA Y BIOLÓGICA
Introducción
Visión como sistema físico
Visión biológica
MODELOS DE CÀMARA
Introducción
¿Cómo funciona una cámara?
Cámara oscura o pinhole
Lente delgada
SENSORES DE IMAGEN Y PIPELINE DE FORMACIÓN (CCD VS CMOS)
Introducción
¿Qué es un ADC?
Cómo funciona un sensor CCD
Cómo funciona un sensor CMOS
Pipeline de formación de imagen (ISP)
IMAGEN DIGITAL Y GESTION DEL COLOR
Introducción
Captura de color
Imagen digital
OPERACIONES PUNTUALES BASADAS EN HISTOGRAMA
Introducción
Operación de negativo (inversión de intensidades)
Corrección de gamma
Estiramiento de contraste o stretching
Segmentación de histograma o thresholding
Ecualización de histograma (HE)
Ecualización adaptativa de histograma (AHE)
Ecualización adaptativa de histograma por contraste (CLAHE)
CONCLUSIONES
Conclusiones de la unidad

### Lesson 1 - Introducción y objetivos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/sssOuc1hXgb2pkkXQdugf_EVelPQz9hs</sub>

Introducción y objetivos

Introducción

Esta unidad ofrece una mirada de extremo a extremo al proceso que transforma la luz del mundo real en datos fiables para algoritmos. El propósito es construir un mapa conceptual común —claro y operativo— que sirva de base al resto de la asignatura, especialmente en modalidad a distancia.

En primer lugar, se enmarca la visión desde el punto de vista físico y biológico: qué significa “ver” en términos de luz y percepción, y cómo ese recorrido inspira las decisiones de ingeniería. A partir de ahí se presenta el itinerario de formación de imagen: escena → óptica → sensor → representación digital → operaciones de realce y preparación de datos.

Sobre esta columna vertebral se introducen los modelos de cámara utilizados en visión por computador y su papel en la proyección de la escena al plano imagen. Se contextualiza después el sensor y su electrónica como puente entre fotones y números, para entender por qué la elección de captura condiciona todo el procesamiento posterior.

A continuación, se consolida la idea de la imagen como señal discreta: cómo la rejilla de píxeles, la profundidad de bits y la curva de visualización influyen en la estabilidad de cualquier algoritmo. Con ese suelo, se abordan las representaciones de color más usadas en práctica (manteniendo el foco en cuándo conviene cada una) y las transformaciones basadas en histograma como herramientas de normalización y realce.

Finalmente, se subraya la importancia de la evaluación y la reproducibilidad: establecer contratos claros de datos, medir efectos de preprocesado y dejar la imagen en condiciones para etapas posteriores (descriptores, invariancias y aprendizaje profundo).

El resultado buscado es doble: criterio para tomar decisiones informadas en captura y preprocesado, y confianza para implementar pipelines sencillos pero sólidos en Python/OpenCV que sirvan de cimiento a los temas avanzados de la asignatura.

Click to flip

Visión física y biológica

Click to flip

En este apartado, entenderemos la visión como una cadena de transformación de información. Primero, un sistema físico —la cámara— convierte luz que llega desde la escena en datos digitales. Después, un sistema biológico —el ojo y el cerebro— realiza una transformación diferente, pero con objetivos similares: hacer visibles estructuras útiles y comprimir la complejidad del mundo para tomar decisiones. Como ingenieros de software, nos interesan sus abstracciones y limitaciones, porque condicionan el diseño de pipelines, la elección de parámetros y la evaluación.

Click to flip

Modelos de cámara

Click to flip

En este apartado trabajaremos con dos modelos fundamentales que representan aproximaciones complementarias al problema de la formación de imágenes. El modelo de cámara oscura nos proporcionará la proyección geométrica más pura, ideal para entender los principios fundamentales y para diferentes aplicaciones posteriores; y por otro lado, el modelo de lente delgada introducirá los efectos físicos reales que dominan en sistemas prácticos: apertura, enfoque, profundidad de campo y exposición.

Click to flip

Sensores de imagen y pipeline de formación (CCD vs CMOS)

Click to flip

En esta sección vamos a ver dos familias de sensores que vamos a analizar, CCD y CMOS, y compararemos dos formas distintas de procesar la información que nos llega desde la lente, y cómo se convierte en información digital.

Click to flip

Imagen digital y gestión del color

Click to flip

En este apartado exploraremos cómo los sistemas digitales capturan, representan y manipulan información de color. Veremos que aparentemente simples decisiones sobre espacios de color pueden tener implicaciones profundas para el rendimiento de algoritmos de visión por computador. Entenderemos por qué el mismo objeto puede aparecer con colores completamente diferentes bajo diferentes condiciones de iluminación, y cómo los sistemas artificiales pueden ser más (o menos) robustos que la visión humana a estos cambios.

Click to flip

Operaciones puntuales basadas en histograma

Click to flip

Este apartado nos enseñará a operar sobre la imagen guiándonos por su histograma para mejorar la imagen o prepararla mejor para algoritmos posteriores. Ahora nos ocuparemos de que los detalles sean visibles y las diferencias relevantes queden realzadas.

Objetivos

1

Comprender la relevancia y motivaciones de la Visión por Computador, distinguiendo entre el proceso de visión biológica y la visión artificial en sistemas informáticos.

2

Describir la representación digital de una imagen.

3

Entender el modelo de formación de imágenes en una cámara.

4

Aplicar y entender transformaciones de color en una imagen..

5

Desarrollar pequeñas aplicaciones o scripts en Python utilizando bibliotecas especializadas para manipular imágenes.

6

Analizar los resultados obtenidos y resolver problemas básicos relacionados con la calidad de imagen.

¡Comenzamos!

### Lesson 2 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/RmdqNZMu52kIfQL3c_fvuwgpOS111C99</sub>

Introducción

Cuando pensamos en la visión, la mayoría de nosotros la damos por sentada. Abrimos los ojos y "vemos" el mundo que nos rodea, como si fuera la cosa más natural del mundo. Sin embargo, lo que realmente está ocurriendo es uno de los procesos de transformación de información más sofisticados que conocemos.

En este apartado, entenderemos la visión como una cadena de transformación de información. Primero, un sistema físico —la cámara— convierte luz que llega desde la escena en datos digitales. Después, un sistema biológico —el ojo y el cerebro— realiza una transformación diferente, pero con objetivos similares: hacer visibles estructuras útiles y comprimir la complejidad del mundo para tomar decisiones. Como ingenieros de software, nos interesan sus abstracciones y limitaciones, porque condicionan el diseño de pipelines, la elección de parámetros y la evaluación.

La visión, tanto artificial como biológica, comienza con un elemento fundamental: la luz. Pero antes de adentrarnos en los detalles técnicos, reflexionemos sobre lo que realmente significa "ver". Cuando miras esta página, no estás simplemente "tomando una fotografía" de ella. Tu sistema visual está constantemente tomando decisiones sobre qué información es relevante, está adaptándose a las condiciones de iluminación, está interpretando patrones y está construyendo un modelo mental coherente del mundo que te rodea.

Este proceso tiene dos componentes principales que estudiaremos en detalle: el sistema físico, entendiendo cómo la luz interactúa con la materia y se propaga hasta nuestros detectores; y el sistema biológico, viendo cómo los organismos vivos han evolucionado para captar, procesar e interpretar esta información luminosa. Comprender ambos aspectos nos dará las herramientas conceptuales necesarias para diseñar sistemas artificiales que puedan replicar, y en algunos casos superar, las capacidades de la visión natural.

¿Todo listo? ¡Empezamos!

### Lesson 3 - Visión como sistema físico

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/-NCIfYRKc2PIdvaz6wxtbYHqlc8KHjNU</sub>

Visión como sistema físico

Para entender realmente qué significa "ver", debemos empezar por el principio. Toda visión, ya sea natural o artificial, se basa en la detección e interpretación de radiación electromagnética.

Desde el plano físico, la visión implica dos etapas principales: primero, la interacción de la luz con la materia en la escena; segundo, la detección de esa luz por un sensor. Podemos pensar en cualquier escenario donde haya luz: una superficie u objeto en la escena emite luz (si es suficientemente caliente, como una bombilla o el sol, emite luz propia) o bien refleja la luz que recibe de otras fuentes (por ejemplo, una manzana refleja la luz del sol). Esa luz reflejada se dispersa en todas direcciones y parte de ella es capturada por un sistema óptico, ya sea el cristalino de nuestro ojo o la lente de una cámara. La óptica se encarga de concentrar los rayos de luz y formar una imagen enfocada en un plano receptor (la retina en el ojo, o el sensor electrónico en la cámara).

Es importante notar que la imagen formada no es una copia perfecta de la realidad, sino una medición condicionada por varios factores físicos. ¿De qué depende cómo resulta esa imagen? Principalmente de tres aspectos:

Iluminación de la escena, dependiendo de cuánta luz hay y de qué tipo.

Geometría de la óptica, por ejemplo, si usamos un orificio pequeño o una lente, si está bien enfocada, etc.

Sensibilidad del detector, influyendo qué tan bien el sensor o cómo la película fotográfica responde a esa luz).

Estos factores son los que determinarán la nitidez, el brillo, el contraste y la fidelidad de la imagen resultante. Imaginemos que estamos viendo un objeto en un cuarto poco iluminado versus al aire libre en un día soleado. Incluso con la misma cámara, la imagen será muy diferente: en la oscuridad quizás casi no se distinga nada (poca iluminación), mientras que a plena luz veremos muchos detalles.

1
2
3
4
5
1 of 6
Espectro electromagnético

Cuando la luz encuentra un objeto, pueden ocurrir tres cosas fundamentales: puede ser reflejada, absorbida o transmitida (atravesar el objeto). La proporción en que ocurre cada una de estas interacciones depende tanto de las propiedades del material como del tipo de luz que se está proyectando sobre el objeto.

Sabemos que la luz tiene una doble dualidad, la de partícula y la de onda. Para nuestro caso, nos vamos a centrar en el comportamiento de la luz como onda electromagnética que se transmite a través de un medio. Al comportarse como una onda, tiene asociado una longitud de onda a la que denominamos , que medimos en nanómetros (nm) y que representa la cantidad de espacio que recorre la onda en un periodo.

START
2 of 6
3 of 6

Al conjunto de todas las posibles longitudes de onda de las ondas electromagnéticas es a lo que llamamos el espectro electromagnético.

Nuestros ojos solo son sensibles a una pequeña porción de ese espectro (lo que llamamos luz visible, aproximadamente de 380 nm a 780 nm de longitud de onda). Fuera de ese rango tenemos, por debajo, la luz ultravioleta (UV) y más allá los rayos X y gamma; por encima, la luz infrarroja (IR), microondas y ondas de radio.

La luz visible es simplemente aquella pequeña franja del espectro a la que nuestros ojos responden. Dentro de esa franja, las diferentes longitudes de onda las percibimos como diferentes colores: aproximadamente las longitudes cortas (~400 nm) se ven azuladas y las largas (~700 nm) se ven rojizas. Es importante destacar que nuestros ojos no miden la longitud de onda exacta de la luz que llega; más bien, tenemos sensores con distintas sensibilidades espectrales que en conjunto producen la sensación de color en el cerebro.

4 of 6

La porción del espectro inmediatamente fuera de lo visible también tiene importancia práctica en visión por computador. Por ejemplo, la luz ultravioleta (UV) tiene longitudes de onda más cortas que el violeta (~<380 nm). El ojo humano no ve la luz ultravioleta directamente (aunque la puede sentir indirectamente, como cuando produce fluorescencia en materiales o causa quemaduras solares). Muchas cámaras estándar tampoco la registran porque sus lentes y filtros internos la bloquean. Sin embargo, existen aplicaciones donde el UV es útil: en criminalística e inspección, se usan lámparas UV para revelar sustancias que emiten luz visible (fluorescencia); en procesos industriales y médicos (fotolitografía, curado de resinas), se aprovecha su alta energía; incluso hay tintas de seguridad que solo se ven bajo luz ultravioleta.

5 of 6

Por otro lado, está la luz infrarroja (IR), con longitudes de onda más largas que el rojo (~>780 nm). Tampoco la vemos, pero la sentimos como calor. Muchos objetos comunes emiten infrarrojo de forma natural dependiendo de su temperatura (toda persona u objeto caliente emite radiación térmica). Las cámaras termográficas aprovechan esto para “ver” el calor, pudiendo detectar personas en la oscuridad total o medir temperaturas a distancia.

6 of 6

Esta interacción selectiva es lo que nos permite distinguir entre diferentes materiales y objetos. Una hoja verde refleja más luz en las longitudes de onda verdes y absorbe más en las rojas y azules. Un metal pulido refleja la mayoría de la luz visible, mientras que el carbón absorbe casi toda la luz visible. Un cristal transparente transmite la mayor parte de la luz visible, pero puede absorber fuertemente en el ultravioleta o infrarrojo.

Comprender estas interacciones es fundamental para diseñar sistemas de visión por computador robustos. Por ejemplo, si estamos diseñando un sistema para identificar diferentes tipos de plásticos en una planta de reciclaje, podrías aprovecharte del hecho de que diferentes plásticos tienen firmas espectrales distintivas en el infrarrojo cercano.

### Lesson 4 - Visión biológica

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/NBkfhG_e7DR_VNYb2sV5qrU7Zoa2hy6U</sub>

Visión biológica

Después de entender los principios físicos fundamentales de la luz y su interacción con la materia, es momento de explorar cómo la naturaleza ha desarrollado sistemas extraordinariamente sofisticados para capturar y procesar esta información luminosa.

El ojo humano es, en muchos sentidos, una cámara biológica. Tiene componentes análogos a los de una cámara fotográfica: la córnea y el cristalino del ojo actúan como lentes que enfocan la luz; el iris es como un diafragma que abre o cierra la pupila para regular cuánta luz entra (apertura); la retina en el fondo del ojo es el “sensor” donde se forma la imagen; y el nervio óptico transmite las señales visuales al cerebro, cumpliendo un papel parecido al cable que llevaría datos desde un sensor electrónico a un procesador.

En la retina encontramos dos tipos principales de “sensores” a lo que llamaremos fotorreceptores, cada uno optimizado para diferentes condiciones de iluminación y tipos de información visual.

Los bastones son detectores de alta sensibilidad especializados en condiciones de baja iluminación. Son increíblemente sensibles - pueden detectar incluso fotones individuales en condiciones ideales. Sin embargo, no proporcionan información de color y tienen menor resolución espacial.

Los conos requieren más luz para funcionar, pero proporcionan alta resolución espacial y son responsables de la visión en color. En los humanos existen tres tipos de conos, cada uno con sensibilidad máxima a diferentes partes del espectro visible (azules, rojos y verdes).

Por eso de noche vemos principalmente en blanco y negro y con menos nitidez, mientras que de día apreciamos colores vivos y detalles finos: de noche están trabajando sobre todo los bastones, de día dominan los conos.

La distribución de bastones y conos en la retina no es uniforme. En el centro de la retina, en una zona llamada mácula, se encuentra la fóvea, que es una pequeña depresión responsable de nuestra visión central aguda. La fóvea es especial porque allí hay una altísima densidad de conos (para máxima resolución y color), y prácticamente no hay bastones en el centro foveal. Esto significa que nuestra visión más nítida y con color más preciso ocurre en esa pequeña región central a donde dirigimos la mirada; en cambio, en la periferia de la retina (lo que vemos “de reojo”) la densidad de conos baja y predominan los bastones, lo que nos da más sensibilidad a movimiento y a luces débiles en los bordes de nuestra visión, pero menos detalle y color.

No todas las personas “capturan” el mismo rango efectivo dentro del espectro visible. Incluso entre las personas sin ningún problema aparente, existe una diferencia natural de cómo cada uno percibe los colores.

Además, una fracción significativa de la población presenta problemas en la percepción de colores, conocido comúnmente como daltonismo, que reducen o distorsionan la discriminación de ciertos ejes de color.

Protanomalía / Protanopia. Donde se produce una caída de sensibilidad hacia los rojos; y por lo tanto, los rojos y los verdes tienden a confundirse, incluso los rojos pueden percibirse más oscuros.

Deuteranomalía / Deuteranopia. Con este problema se producen confusiones de rojo–verde con una pérdida de matiz en verdes.

Tritanomalía / Tritanopia. Aquí se producen confusiones de azul–amarillo; donde los azules y verdes claros pueden volverse intercambiables.

Acromatopsia / Monocromacias. Es el problema visual menos frecuente, donde se produce una percepción prácticamente sin color, como si fuera prácticamente ver en una escala de grises.

Estas condiciones nos recuerdan que la “captura de color” biológica tiene sus limitaciones y variabilidades. En visión por computador, a veces hay que tener en cuenta que cierto procesamiento de color debiera ser robusto a estas diferencias

¡Fantástico! Has completado este apartado.

### Lesson 5 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/jQqNRBTfkH5DE4YcGwMy56qzUzKNxvbz</sub>

Introducción

Habiendo explorado cómo funciona la visión en el mundo físico y biológico, es momento de dar el siguiente paso fundamental: entender cómo podemos crear modelos matemáticos que describan la formación de imágenes. Un modelo de cámara es esencialmente una abstracción matemática que nos permite predecir cómo se proyectará un punto tridimensional del mundo real en una imagen bidimensional.

En este apartado trabajaremos con dos modelos fundamentales que representan aproximaciones complementarias al problema de la formación de imágenes. El modelo de cámara oscura nos proporcionará la proyección geométrica más pura, ideal para entender los principios fundamentales y para diferentes aplicaciones posteriores; y por otro lado, el modelo de lente delgada introducirá los efectos físicos reales que dominan en sistemas prácticos: apertura, enfoque, profundidad de campo y exposición.

Las cámaras toman la luz de la escena y la convierten en una imagen digital que podamos almacenar o analizar. Entenderemos sus componentes: la óptica (lentes u orificios) que define qué rayos de luz forman la imagen, el control de exposición (qué cantidad de luz dejamos entrar y por cuánto tiempo), el sensor que transforma la luz en señales eléctricas, y el procesado inicial que prepara esa señal para usos posteriores.

### Lesson 6 - ¿Cómo funciona una cámara?

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/F76haM2LatptQotsAL4Xee3whqGwPayy</sub>

¿Cómo funciona una cámara?

Antes de sumergirnos en los modelos matemáticos específicos, es importante desarrollar una comprensión intuitiva de qué hace realmente una cámara desde la perspectiva de un sistema de información.

Una cámara no es simplemente un dispositivo que "toma fotos". Es un sistema sofisticado de selección y conversión de información que realiza múltiples operaciones complejas en una fracción de segundo. Entender estas operaciones como procesos de información nos ayudará a diseñar mejores algoritmos y a diagnosticar problemas cuando las cosas no funcionen como esperamos.

En términos generales, una cámara fotográfica (o de video) capta rayos de luz de la escena y los proyecta en un plano imagen, donde un sensor registra la intensidad de esos rayos para formar una imagen. Veamos los elementos clave del proceso:

Óptica (Lente o sistema de lentes)
Exposición (apertura y tiempo de obturación)
Sensor de imagen
Procesado inicial o ISP (Image Signal Processor)

Resumiendo, cada píxel de una imagen digital es el resultado de decisiones físicas y electrónicas: qué parte de la escena se proyectó en él (óptica), cuánta luz se acumuló (exposición), cómo el sensor tradujo esa luz a un número, y qué correcciones y ajustes se aplicaron en el ISP. Conocer estos pasos nos permite luego diagnosticar problemas (por ejemplo, si una imagen sale oscura sabremos si quizás fue por exposición insuficiente; si sale borrosa, ver si fue enfoque, movimiento o ruido electrónico; si los colores se ven raros, pensar en balance de blancos o iluminación, etc.).

### Lesson 7 - Cámara oscura o pinhole

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/GGl4Wwapkbc5SDWWN-ESTB3CB8zMq1cM</sub>

Cámara oscura o pinhole

El modelo más sencillo de cámara es la cámara oscura (o estenopeica, conocida en inglés como pinhole camera). Es tan simple que ni siquiera tiene lente: consiste en una caja o recinto oscuro con un pequeño orificio en un lado, a través del cual entra la luz y se proyecta una imagen invertida en la pared opuesta dentro de la caja.

Este tipo de cámara consiste en un recinto sellado con un pequeño orificio que deja pasar sólo una fracción de la luz y proyecta en la pared opuesta una imagen invertida de la escena. La cámara oscura es el punto de partida más intuitivo para entender que entender qué es seleccionar rayos.

Imaginemos una escena exterior: cada punto luminoso de la escena emite (o refleja) rayos de luz en muchas direcciones. El agujero de la cámara oscura es tan pequeño que solo deja pasar unos pocos rayos de cada punto. Esos rayos que logran pasar siguen en línea recta y van a dar a un punto específico en la pared interna. En esencia, el agujero está “seleccionando rayos”: por eso decimos que ver es seleccionar rayos. El resultado es una imagen donde cada punto de la escena corresponde a un punto en la pared (invirtiéndose porque los rayos provenientes de la parte superior de la escena viajan hacia abajo en la caja, y viceversa).

Lo extraordinario de este sistema es su simplicidad conceptual: no hay lentes, no hay óptica compleja, solo geometría pura. Cada punto en la imagen corresponde a una dirección específica en el espacio 3D. Esta correspondencia geométrica directa es lo que hace que el modelo pinhole sea tan valioso para aplicaciones de calibración y reconstrucción 3D.

Aunque conceptualmente perfecto, el modelo de cámara oscura nos introduce inmediatamente a uno de los compromisos fundamentales de todos los sistemas de visión: el compromiso entre nitidez y luminosidad.

Con un agujero más grande, entra más luz, así que la imagen será más brillante (más fácil de ver). Sin embargo, al ser grande, el orificio deja pasar rayos no tan bien dirigidos, es decir, de cada punto de la escena pasan rayos que van a parar a diferentes puntos cercanos en la pared, haciendo que se emborronen (se superponen) y la imagen pierda nitidez. Ese borrón debido a que el orificio tiene un diámetro no despreciable se llama borrón geométrico (o círculo de confusión). Por otro lado, ¿qué pasa si hacemos el orificio muy muy pequeño? Tendremos rayos más “ordenados” y la imagen ganará definición geométrica… pero entrará poquísima luz, así que la imagen será extremadamente tenue, posiblemente dominada por el ruido o incluso invisible si no tenemos un sensor suficientemente sensible. Además, cuando el tamaño del orificio se acerca al orden de la longitud de onda de la luz, empiezan a aparecer efectos de difracción: la luz se comporta como onda y se “esparce” al pasar por el agujero minúsculo, generando también un disco de borrón.

Aunque la cámara oscura real es impráctica para la mayoría de las aplicaciones (debido a los largos tiempos de exposición requeridos por la baja cantidad de luz), el modelo pinhole sigue siendo fundamental en aplicaciones modernas:

Calibración de cámaras
Visión estereoscópica
Realidad aumentada
Fotogrametría

En el siguiente video vamos a ver cómo la imagen se forma invertida y cómo la magnificación crece al alejar el plano de imagen. Manipulamos dos parámetros del objeto al orificio y diámetro del orificio D, para ver cómo crece/decrece el borrón geométrico en la imagen capturada.

### Lesson 8 - Lente delgada

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/PQcrmqCi23APc2nOOSUGlZQm-c07L_Sx</sub>

Lente delgada

Para superar las limitaciones de la cámara oscura, se introducen las lentes. Una lente (o combinación de lentes) permite enfocar la luz, es decir, hacer converger los rayos de un punto de la escena hacia un punto del plano imagen. Gracias a esto, logramos imágenes mucho más luminosas (porque podemos usar aperturas grandes dejando pasar mucha luz) sin sacrificar la nitidez en el plano enfocado. La contrapartida es que perdemos la “infinita” profundidad de campo de la pinhole: con una lente, solo los objetos a una cierta distancia quedan perfectamente enfocados, y lo que esté más cerca o más lejos sale borroso. Sin embargo, ganamos la capacidad de escoger qué plano de la escena queremos enfocar y obtener imágenes claras con exposiciones cortas.

El modelo simplificado para entender la óptica real es la lente delgada. Imaginemos una sola lente ideal que converge la luz. Tiene una distancia focal , que es la distancia desde la lente hasta el plano donde enfocarían objetos que están en el infinito (en cámaras reales, el sensor se coloca aproximadamente a esa distancia focal para enfocar cosas lejanas). La distancia focal fija el “zoom” geométrico: lentes de corta focal (e.g. 18 mm en una cámara) dan un campo de visión amplio (imágenes más “abiertas”), mientras focales largas (e.g. 200 mm) dan imágenes ampliadas de zonas pequeñas del espacio, como un telescopio.

El enfoque introduce una nueva dimensión de control y complejidad en la formación de imágenes. A diferencia del sistema pinhole, donde todo está igualmente "enfocado" (o desenfocado), un sistema de lentes permite seleccionar qué distancia estará más nítida en la imagen.

La profundidad de campo es el rango de distancias que aparecerán "aceptablemente" nítidas en la imagen. "Aceptablemente" es subjetivo y depende de la aplicación, pero generalmente se define en términos del círculo de confusión máximo tolerable: el tamaño máximo del disco borroso que se acepta como un "punto" en la imagen.

Un concepto clave introducido con las lentes es el número f o número de apertura. En fotografía se expresa como, por ejemplo, f/2.8, f/4, f/8, etc. Un número f menor (f/2.8, f/1.4...) significa apertura grande (mucho diámetro relativo) y, por tanto, mucha luz entrando; un número f grande (f/16, f/22...) es apertura pequeña, poca luz.

¿Por qué no usamos siempre aperturas enormes para tener mucha luz? Porque la apertura también afecta a la profundidad de campo (DOF) y a la difracción. La profundidad de campo es el rango de distancias en la escena que aparecen enfocadas aceptablemente en la imagen. Cuando enfocamos a una cierta distancia, solo exactamente ese plano está en foco perfecto, pero hay una tolerancia: un objeto un poco más cerca o un poco más lejos aparecerá ligeramente desenfocado, formando un circulito en el sensor en lugar de un punto. Pues bien, una apertura más pequeña (número f grande) aumenta la profundidad de campo: los círculos de confusión de objetos desenfocados son menores, por lo que más distancia cae dentro del rango aceptablemente nítido. Inversamente, una apertura muy grande (número f bajo) produce una profundidad de campo muy estrecha: solo una capa delgada de la escena está enfocada, lo demás sale borroso

En el siguiente video vamos a ver un ejemplo en Python de cómo se comporta la lente delgada. Vamos a usar la distancia focal, número f, longitud de onda y el círculo de confusión aceptable para poder calcular la profundidad de campo, el diámetro Airy y PSF.

Comparativa: ¿cuándo usar qué?

Modelo

Principio

Ventajas

Contras

Usos típicos

Cámara oscura

Proyección por orificio sin lente

Geometría pura, coste mínimo, sin aberraciones de lente

Muy poca luz, imagen tenue, poca resolución útil

Demostración didáctica, arte, experimentos de proyección

Lente delgada

Lente convergente que enfoca y concentra luz

Mucha luz (aperturas grandes), control de enfoque/DOF, mejor, exposiciones cortas

Aberraciones y distorsión para corregir, complejidad y coste óptico

Visión industrial, fotografía/vídeo, embedded y móvil

¡Fantástico! Has completado este apartado.

### Lesson 9 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/E6fZkb6H-yh3i6fXG9EFw2T9yXcuEXbE</sub>

Introducción

Después de entender cómo se forma geométricamente una imagen a través de sistemas ópticos, llega el momento de explorar uno de los aspectos más fascinantes de la visión por computador moderna: cómo se convierte la luz en información digital. Este proceso de conversión no es simplemente técnico; es una cadena compleja de decisiones de ingeniería que afectan profundamente la calidad, características y limitaciones de los datos que finalmente reciben nuestros algoritmos.

Como ya hemos visto cómo la luz de la escena es enfocada por la óptica hacia el plano imagen, ahora toca estudiar qué ocurre en ese plano y cuál es el responsable de convertir la luz captada por la lente en información digital: el sensor de la cámara.

Un sensor de imagen típico está organizado como una matriz de píxeles, muy parecido a una cuadrícula. Cada elemento o píxel del sensor contiene un fotodiodo, que es un dispositivo semiconductor sensible a la luz: cuando le llega luz (fotones), genera electrones (carga eléctrica) en proporción a la intensidad luminosa y al tiempo de exposición. Esa carga acumulada es luego leída como una señal (un voltaje o una cantidad de electrones) que corresponde al nivel de brillo capturado en ese píxel.

Encima de cada píxel suelen encontrarse componentes adicionales integrados:

Un filtro de color (en sensores a color, para filtrar rojo, verde o azul, como veremos más en detalle en el siguiente apartado de captura de color).

Una microlente: una minúscula lente que concentra la luz que cae sobre la superficie del píxel hacia el fotodiodo activo. Sin microlentes, parte de la luz podría incidir en zonas no sensibles del píxel pero con ellas se aprovecha mejor la luz.

Varias capas metálicas de interconexión (propias de la fabricación de los circuitos integrados del sensor) que a veces cubren parcialmente la superficie.

En esta sección vamos a ver dos familias de sensores que vamos a analizar, CCD y CMOS, y compararemos dos formas distintas de procesar la información que nos llega desde la lente, y cómo se convierte en información digital.

### Lesson 10 - ¿Qué es un ADC?

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/4YvbcCheBk-sDQWY0KMOxqcxTlLQKYZ1</sub>

¿Qué es un ADC?

Antes de adentrarnos en los detalles específicos de diferentes tecnologías de sensores, es crucial entender uno de los componentes más fundamentales en cualquier sistema de imagen digital: el Convertidor Analógico-Digital, conocido por sus siglas en inglés como ADC (Analog-to-Digital Converter).

El ADC representa literalmente la frontera entre el mundo físico analógico y el mundo computacional digital; los sensores de imagen, sin importar cuán sofisticados sean, fundamentalmente convierten luz (un fenómeno físico continuo) en carga eléctrica (una señal analógica continua). Para que esta información pueda ser procesada por sistemas digitales, debe ser convertida en números discretos.

¿Por qué es importante el ADC? Porque marca la transición de un mundo analógico (luz, cargas, voltajes) al mundo digital (números, matriz de píxeles digital). De la calidad del ADC (su resolución en bits, su ruido, su velocidad) depende en gran medida la calidad final de la imagen digital. Por ejemplo, un ADC con pocos bits puede introducir banding, es decir, introduce saltos entre los diferentes niveles de color o intensidad. Un ADC ruidoso o mal calibrado puede agregar error a cada medición.

Este proceso de convertir los datos recogidos por los píxeles y convertirlos en números que pueden ser procesados (conversión analógico-digital), involucra dos operaciones fundamentales que introducen limitaciones inherentes:

MUESTREO TEMPORAL
CUANTIFICACIÓN DE AMPLITUD

El ADC no puede leer continuamente la señal analógica; debe tomar "muestras" a intervalos discretos de tiempo. La frecuencia a la que se toman estas muestras (frecuencia de muestreo) determina qué tan rápidamente pueden cambiar las señales que el sistema puede capturar de forma correcta.

¿Cómo funciona un ADC en este contexto? Pensemos en un píxel del sensor al final de la exposición: tiene una cierta carga almacenada (proporcional a los fotones). Esa carga se suele convertir primero a un voltaje por medio de un pequeño amplificador. El ADC toma ese voltaje y lo compara contra niveles de referencia para asignarle un valor digital.

### Lesson 11 - Cómo funciona un sensor CCD

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/GvC1QddGFFhyZ3Sg-z20fY9Vj7Qnt_vZ</sub>

Cómo funciona un sensor CCD

Los sensores CCD (Change-Coupled Device) fueron durante décadas la tecnología dominante en sensores de imagen de calidad. Vamos a describir su funcionamiento conceptual: un CCD es esencialmente una matriz de pozos de potencial en un chip de silicio. La idea central detrás de un CCD es sorprendentemente simple: crear una matriz de "pozos" microscópicos que pueden atrapar y almacenar electrones generados por la absorción de fotones. Cada pozo corresponde a un píxel en la imagen final.

La característica definitoria de un CCD es cómo se lee esa carga acumulada: se utiliza un mecanismo de transferencia de carga por acoplamiento (de ahí su nombre, Charge-Coupled). Imaginemos una fila de cubos llenos de agua (agua = carga). Para leer cuánta agua hay en cada cubo, en lugar de ir con un sensor a cada uno, lo que hacemos es ir volcando el agua de un cubo al siguiente secuencialmente hasta llegar al final de la fila, donde hay un medidor.

Al final, toda la imagen ha sido transferida y leída esencialmente por el mismo camino y a través de (generalmente) uno o pocos amplificadores de salida. Esto tiene una ventaja clave: uniformidad. Como toda la matriz comparte el mismo circuito de lectura, cualquier ruido de lectura o variación tiende a ser global y muy bajo. Los CCD tradicionalmente han tenido un ruido de lectura bajísimo y excelente uniformidad píxel a píxel. Son ideales para capturar imágenes con señales débiles porque introducen muy poco ruido propio. Además, tienden a ser muy lineales en su respuesta y a tener gran full well capacity (cada píxel puede acumular muchos electrones antes de saturar), lo que les da un rango dinámico alto.

Por supuesto, también tienen desventajas:

LENTO
POCO FLEXIBLE
ALTO CONSUMO

Los CCD típicos no pueden leer muy rápido (comparado con CMOS, que veremos a continuación) porque se tiene que desplazar la carga de millones de píxeles a lo largo de distancias largas.

### Lesson 12 - Cómo funciona un sensor CMOS

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/xM_djZUlLHsp_ul3zXwrMQzwaLEDDINO</sub>

Cómo funciona un sensor CMOS

Los sensores CMOS (Complementary Metal-Oxide-Semiconductor) representan la evolución natural de la tecnología de sensores de imagen hacia sistemas más integrados, rápidos y versátiles. La diferencia fundamental con los CCDs no está solo en cómo detectan luz, sino en cómo organizan y procesan la información resultante.

Han ganado enorme popularidad y hoy en día dominan el mercado (especialmente en cámaras de consumo, móviles, etc.) debido a varias ventajas de diseño. La filosofía de un CMOS es casi opuesta a la de un CCD: en lugar de mover la carga por todo el chip hacia un punto de lectura, en un CMOS cada píxel tiene su propio pequeño circuito de lectura activo. Es decir, se introduce electrónica dentro de cada píxel, haciendo que sea un píxel “inteligente” o activo.

En un sensor CMOS típico, cada píxel incluye:

Un fotodiodo que genera la carga (igual que en CCD).

Un transistor de reset que puede vaciar el fotodiodo (estableciendo un nivel inicial antes de la integración).

Un transistor de transferencia (en algunos diseños, para mover la carga del fotodiodo a un pequeño nodo de almacenamiento).

Un transistor fuente seguidora (source-follower) que actúa como un amplificador local: convierte la carga/voltaje en el nodo de almacenamiento en una señal de baja impedancia que se puede leer fuera del píxel.

A veces un transistor de selección que conecta o desconecta el píxel a la línea de lectura de su columna.

En un sensor CMOS, la forma de leer la imagen es muy distinta a la de un CCD. En lugar de ir “pasando la carga” píxel a píxel hasta un único punto de salida (como si fuese una fila de cubos de agua volcándose uno en otro hasta llegar al final), los CMOS tienen un sistema mucho más directo: cada fila se activa de manera independiente.

Imagina que en lugar de una sola puerta de salida hubiera un pasillo completo de puertas: cuando seleccionamos una fila, todos los píxeles de esa fila entregan su información al mismo tiempo a las líneas de columna. Y en esas columnas no se recoge la información de forma pasiva, sino que hay circuitos electrónicos dedicados (amplificadores e incluso convertidores analógico-digitales, los famosos ADC) que transforman la señal luminosa en números.

Esto permite que, en sensores con miles de columnas, podamos leer miles de píxeles en paralelo durante la lectura de una sola fila. El resultado es una gran velocidad de captura: en lugar de esperar a que toda la imagen se desplace hacia un único amplificador (como en el CCD), el CMOS reparte el trabajo entre cientos o miles de “pequeñas salidas” simultáneas.

En otras palabras, si un CCD es como un único cajero atendiendo a toda una cola, un CMOS sería como tener un cajero en cada columna atendiendo a muchos clientes en paralelo. Así se entiende mejor por qué los sensores CMOS son tan rápidos y han terminado imponiéndose en la mayoría de los dispositivos modernos.

Sin embargo, esta velocidad viene con un costo: el rolling shutter. Debido a que diferentes filas se leen en diferentes momentos, objetos en movimiento rápido pueden aparecer distorsionados. Este efecto debe ser considerado cuidadosamente en aplicaciones de visión por computador que involucran movimiento rápido. Como explicamos, un CMOS lee la imagen fila por fila de forma secuencial, mientras otras filas todavía pueden estar exponiéndose. En un CCD, todos los píxeles empiezan y terminan la exposición simultáneamente; en un CMOS, la fila 1 quizás se lee y termina su exposición un par de milisegundos antes que la fila 1000, por ejemplo. Esto significa que, si la escena se mueve rápidamente o si hay una fuente de luz parpadeante, la imagen puede presentar distorsiones geométricas o de brillo: donde los objetos en movimiento pueden salir inclinados o arqueados (efecto “gelatina”), o una hélice puede aparecer partida en segmentos en diferentes posiciones, etc., porque cada fila capturó el objeto en un instante distinto. Igualmente, luces que varían durante el breve intervalo entre leer la fila 1 y la fila 500 producen bandas de diferente iluminación (banding).

Para mitigar esto, existen CMOS con Global Shutter: incorporan un elemento de almacenamiento en cada píxel para poder capturar la carga simultáneamente en todo el sensor y luego leerla con calma, similar conceptualmente a un CCD (pero manteniendo la lectura paralela CMOS). Esto sacrifica un poco de área o añade ruido (porque ese elemento extra ocupa espacio) pero elimina los artefactos de rolling shutter. Muchos sensores CMOS modernos para visión industrial son global shutter o tienen modos de alta velocidad con global shutter, especialmente para aplicaciones donde el movimiento es significativo.

### Lesson 13 - Pipeline de formación de imagen (ISP)

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/U0ZQKotZv9yR1rz33rZdWEcmoWBGwdIG</sub>

Pipeline de formación de imagen (ISP)

Hasta ahora tenemos la escena proyectada, capturada por el sensor y convertida en valores digitales por el ADC. Sin embargo, la imagen que entrega un sensor en bruto no es aún la imagen final “lista para usar”. Requiere una serie de transformaciones y correcciones conocidas en conjunto como ISP (Image Signal Processor) o pipeline de formación de imagen. Entender el ISP es crucial para aplicaciones de visión por computador porque cada etapa del pipeline afecta la información disponible para algoritmos posteriores.

Los datos que salen directamente del sensor (conocidos como datos RAW) están muy lejos de lo que consideraríamos una "imagen" utilizable. Estos datos representan simplemente la cantidad de carga eléctrica acumulada en cada píxel, sin correcciones, sin color, y con varios artefactos y limitaciones del hardware.

El ISP debe realizar una serie de transformaciones complejas para convertir estos datos crudos en imágenes que sean tanto visualmente atractivas como técnicamente útiles para análisis posterior.

El “viaje” que realiza el fotón desde que es captado, hasta que se crea el píxel con la información adecuada se puede enumerar en las siguientes fases,

Captura y nivel de negro. La luz llega al fotodiodo y se convierte en señal eléctrica. Antes de usarla, se quita el offset (nivel negro) para que el “0” sea oscuridad real.

Reconstrucción de color y balance. Como cada píxel mide un solo color (patrón Bayer), se reconstruyen los tres canales (demosaicing) y se aplica balance de blancos para neutralizar el iluminante.

Correcciones ópticas mínimas. Se corrigen sombras de lente (viñeteo) y distorsión si hace falta medida geométrica; se marcan/ interpolan píxeles defectuosos.

Ruido: limpiar sin borrar bordes. Se reduce el ruido (sobre todo en crominancia) con filtros suaves. La idea es estabilizar la señal sin perder detalle útil en contornos.

Color y rango dinámico. Se ajusta el color a un espacio estándar y, si la escena tiene luces y sombras extremas, se combina información (HDR) para no perder detalle.

Preparación para ver o para medir. Para visualizar, se aplica mapeo de tonos y gamma (imagen agradable a ojo). Para visión por computador, lo ideal es mantener la señal lineal (sin gamma ni realce de nitidez) y trabajar con RAW o con un perfil “plano”.

¡Fantástico! Has completado este apartado.

### Lesson 14 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/HPE6ThwfCSNlEhSEqyk2Zo3gvgyO4BZo</sub>

Introducción

Después de entender cómo se captura físicamente la luz y se convierte en señales eléctricas, llegamos a uno de los aspectos más complejos de la visión por computador: cómo representamos y gestionamos la información del color en sistemas digitales.

El color no es simplemente un atributo que existe en la realidad - es una construcción compleja que emerge de la interacción entre luz, materia y percepción. Cuando diseñamos sistemas de visión por computador, debemos navegar cuidadosamente entre la física objetiva de la radiación electromagnética y la experiencia subjetiva del color que experimentan los usuarios humanos.

En este apartado exploraremos cómo los sistemas digitales capturan, representan y manipulan información de color. Veremos que aparentemente simples decisiones sobre espacios de color pueden tener implicaciones profundas para el rendimiento de algoritmos de visión por computador. Entenderemos por qué el mismo objeto puede aparecer con colores completamente diferentes bajo diferentes condiciones de iluminación, y cómo los sistemas artificiales pueden ser más (o menos) robustos que la visión humana a estos cambios.

La gestión apropiada del color es fundamental para aplicaciones que van desde el análisis médico (donde precisión del color puede ser crítica para diagnóstico) hasta la robótica (donde la detección robusta de objetos debe funcionar bajo iluminación variable) y la realidad aumentada (donde objetos virtuales deben integrarse convincentemente con el mundo real).

### Lesson 15 - Captura de color

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/U3LgYQGkOn-RGySY9Dv5sBE6AlYSLnCM</sub>

Captura de color

La captura de color digital enfrenta un desafío fundamental: cómo convertir el espectro continuo de radiación electromagnética en una representación discreta que sea tanto manejable computacionalmente como perceptualmente útil.

La solución adoptada por prácticamente todos los sistemas digitales es inspirada directamente por la visión humana: usar tres mediciones espectrales independientes. Esta reducción de dimensionalidad es simultáneamente poderosa, ya que permite captura práctica de información de color, y limitante, porque diferentes espectros y diferentes combinaciones de colores pueden resultar en el mismo color resultante.

Existen dos aproximaciones principales para capturar información de color en sistemas digitales, cada una con compromisos distintos:

1
1 of 2
Triple-CCD: máxima fidelidad

En sistemas Triple-CCD, un prisma separa la luz entrante en tres haces correspondientes a diferentes bandas espectrales (rojo, verde, azul). Cada haz es dirigido a un sensor separado, permitiendo que cada posición en la imagen sea muestreada simultáneamente en las tres bandas espectrales

START
2 of 2

Las ventajas del sistema Triple-CCD incluyen:

Resolución cromática completa: Cada píxel tiene información completa de los tres canales de color.

Mejor relación señal-ruido: Cada sensor recibe aproximadamente 1/3 de la luz total, pero no hay pérdida adicional por filtros.

Sin embargo, también tiene desventajas significativas:

Complejidad mecánica: Requiere alineación precisa de múltiples sensores.

Tamaño y peso: Significativamente más voluminoso que sistemas de sensor único.

Costo: Mucho más caro que alternativas de sensor único.

1
1 of 2
Sensor único con matriz de filtros Bayer

La mayoría de los sistemas modernos utilizan un sensor único cubierto con una matriz de filtros de color (CFA - Color Filter Array). El patrón más común es el Bayer RGGB, que cubre cada píxel con un filtro que transmite predominantemente rojo, verde o azul.

START
2 of 2

El patrón Bayer utiliza dos píxeles verdes por cada píxel rojo y azul, reflejando la mayor sensibilidad del sistema visual humano a la luz verde y su importancia para la percepción de luminancia.

Por contrapartida, los filtros Bayer introducen varias limitaciones:

Resolución cromática reducida: La resolución efectiva para información de color es menor que para información de luminancia.

Artefactos de false color: Especialmente en bordes de alto contraste entre diferentes colores.

Pérdida de información espectral: Solo tres muestras espectrales limitan la capacidad de distinguir entre diferentes iluminantes.

Ejemplo 1 - Simular captura Bayer y demosaico básico

Por qué: entender que un sensor con CFA no guarda RGB, sino una malla de muestras monocromas con “etiqueta” de color. El demosaico no es decorativo: reconstruye dos tercios de la información.

import numpy as np
import cv2 as cv

def mosaic_bayer_rggb(rgb_lin):
    """Convierte RGB lineal [0,1] en mosaico Bayer RGGB (float32)."""
    H, W, _ = rgb_lin.shape
    assert H % 2 == 0 and W % 2 == 0, "Usar dimensiones pares para el ejemplo."
    mosa = np.zeros((H, W), dtype=np.float32)
    # Máscaras RGGB
    Rm = np.zeros_like(mosa, dtype=bool); Rm[0::2, 0::2] = True
    Gm = np.zeros_like(mosa, dtype=bool); Gm[0::2, 1::2] = True; Gm[1::2, 0::2] = True
    Bm = np.zeros_like(mosa, dtype=bool); Bm[1::2, 1::2] = True
    mosa[Rm] = rgb_lin[...,0][Rm]
    mosa[Gm] = rgb_lin[...,1][Gm]
    mosa[Bm] = rgb_lin[...,2][Bm]
    return mosa

def demosaic_bilinear_rggb(mosa):
    """Demosaico bilineal sencillo usando OpenCV (COLOR_BayerRG2BGR)."""
    # OpenCV espera 8/16-bit; convertimos a 16-bit temporalmente
    mosa16 = np.clip(mosa * 65535.0, 0, 65535).astype(np.uint16)
    bgr = cv.cvtColor(mosa16, cv.COLOR_BayerRG2BGR)  # demosaico bilineal por defecto
    rgb = bgr[..., ::-1].astype(np.float32) / 65535.0
    return np.clip(rgb, 0, 1)

Ejemplo 2 - Simular Triple-CCD ideal (registro perfecto)

Por qué: visualizar el “límite” cuando cada canal está íntegramente muestreado. Útil para comparar artefactos y ruido con Bayer.

# Imagen sintética en RGB lineal [0,1], de 64x64 (dimensiones pares, como exige el mosaico)

H, W = 64, 64
rampa = np.linspace(0.0, 1.0, W, dtype=np.float32)
rgb_lin_example = np.zeros((H, W, 3), dtype=np.float32)
rgb_lin_example[..., 0] = rampa[None, :]          # R crece de izquierda a derecha
rgb_lin_example[..., 1] = rampa[::-1][None, :]    # G decrece
rgb_lin_example[:, W // 2:, 2] = 1.0              # borde vertical nítido en B
# Franja de barras finas rojo/cian de 1 px: el peor caso para el demosaico
rgb_lin_example[H // 2:H // 2 + 8, 0::2] = (1.0, 0.0, 0.0)
rgb_lin_example[H // 2:H // 2 + 8, 1::2] = (0.0, 1.0, 1.0)

def triple_ccd_synthetic(rgb_lin, noise_sigma=0.0):
    """
    Modelo ideal: cada canal se mide a resolución completa + ruido gaussiano opcional.
    """
    out = rgb_lin.copy().astype(np.float32)
    if noise_sigma > 0:
        out += np.random.normal(0, noise_sigma, size=out.shape).astype(np.float32)
    return np.clip(out, 0, 1)

triple_ccd = triple_ccd_synthetic(rgb_lin_example, noise_sigma=0.05)
print(f"Simulación Triple-CCD con ruido:\n{triple_ccd}")

Qué observar

Sin demosaico no aparecen falsos colores por interpolación.

Si se iguala el ruido por canal, el triple-sensor tiende a retener mejor croma en bordes finos.

### Lesson 16 - Imagen digital

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/f8OgFcFfSjS9UbSOmEK0FkDHB8RUc_NJ</sub>

Imagen digital

Una vez obtenemos la imagen capturada y procesada por la cámara, esta se representa en un computador como una matriz digital de píxeles. En esta sub-sección vamos a definir las propiedades fundamentales de esa representación: el tamaño o resolución de la imagen (y cómo se relaciona con su forma y memoria ocupada), el número de canales que contiene y cómo están codificados, y la profundidad de color (bits por canal) que determina la precisión con la que almacenamos los valores de intensidad.

Primero vamos a ver cómo podemos medir cuanto “ocupa” una imagen. El tamaño de una imagen digital se expresa normalmente en píxeles: ancho × alto. A esto nos referimos como la resolución espacial de la imagen. Cada píxel es la unidad mínima representada – se suele imaginar como un cuadradito que tiene un solo color sólido. Cuantos más píxeles haya, más detalle potencialmente se puede representar.

El número de píxeles totales es simplemente ancho × alto. Por ejemplo 1920×1080, eso son 2,073,600 píxeles (~2 megapíxeles). Una cámara de “20 megapíxeles” produce imágenes con ~20 millones de píxeles (por ejemplo 5472×3648 px).

La relación de aspecto o aspect ratio, es la proporción entre ancho y alto. En 1920×1080 es 16:9 (16 unidades de ancho por 9 de alto). El aspecto es importante porque determina la forma de la imagen: una misma escena capturada en 16:9 mostrará más a los lados y menos arriba/abajo que en 4:3.

Depende de la resolución y de la información por píxel (profundidad de bits, canales). Por ejemplo, una imagen de 1920×1080 en RGB de 8 bits por canal ocupa 1920×1080×3 bytes ≈ 6.22 MB sin comprimir. Si fuera en escala de grises 8-bit (1 canal) sería la tercera parte (~2.07 MB).

En el diseño de soluciones de visión, hay que elegir resoluciones adecuadas: más resolución da más detalle, pero requiere más poder de cómputo y almacenamiento; menos resolución aligera el procesamiento, pero puede perder información. A veces se trabaja con pirámides de imágenes (múltiples resoluciones) para compensar esto.

Una parte importante para poder entender cuanto “ocupa”, no solo debemos tener en cuenta la resolución o número de píxeles; si no que también va a influir decidir qué colores estamos almacenando y cómo los estamos representando. El número de canales (C) de una imagen digital indica cuántos valores se almacenan por cada píxel, y qué representan esos valores.

IMÁGENES EN ESCALA DE GRISES (MONOCROMAS)
IMÁGENES RGB A COLOR
IMÁGENES EN ESPACIOS DE COLOR DISTINTOS

Un canal. Cada píxel tiene un solo valor que indica intensidad (del negro al blanco, pasando por grises). Ejemplos: imágenes de sensores monocromos, fotos en blanco y negro, o la luminancia Y' de una imagen a color. A veces se acompaña de una paleta de colores (en índices), pero normalmente 1 canal significa grayscale puro.

La codificación de los canales es importante. Por ejemplo, en una imagen en color típica, asumimos cada canal R, G, B es una intensidad. En sRGB estándar, esos valores están comprimidos. Si uno suma R+G+B en sRGB, no refleja la luminosidad real lineal. Por ello, a veces convertimos a un espacio YUV o similar para separar luminancia.

Un ejemplo de qué ocurre cuando trabajamos en sRGB directamente en lugar de aplicar los cambios en lineal, y luego convertirlo lo podemos ver en el siguiente vídeo.

Por último, una vez que tenemos el tamaño de la imagen en píxeles, y se ha decidido qué colores queremos representar en la imagen; ahora debemos elegir el modelo de color y cómo queremos representar el color. La profundidad de color se refiere al número de bits utilizados para representar el valor de cada canal de un píxel, donde nos determina la precisión y el rango de intensidades o colores que podemos tener.

Con pocos niveles, las transiciones continuas de intensidad se convierten en saltos. Un ejemplo claro: un gradiente de cielo azul en 8-bit a veces muestra bandas (banding). En 10-bit esas bandas desaparecen. La cuantización es básicamente convertir un valor continuo (por ejemplo, intensidad real) a un entero discreto. Esto introduce un pequeño error (de ±0.5 nivel, supongamos en media). 8-bit tiene error de ~0.5/255 ≈ 0.2%; 16-bit, error de 0.5/65535 ≈ 0.0008%. Este error se puede convertir en ruido visible si se amplifica la imagen

Más bits permiten codificar mayor rango dinámico si se planifica bien la escala. Por ejemplo, en 8-bit si calibramos para que 255 sea un blanco de referencia, no podemos representar intensidades 10 veces superiores, saturarían. Con 12-bit podríamos mapear un mayor rango. Aun así, a veces se usan técnicas como companding (curvas logarítmicas) para meter más rango en mismos bits (HDR en 10-bit logarítmico).

En síntesis, usar mayor profundidad de bits reduce la pérdida de información por cuantización y permite manejar mejor las imágenes con amplias diferencias de luminosidad. En la práctica, procesamos a alta profundidad y al final, si es para mostrar o almacenar eficientemente, se suele bajar a 8-bit (con técnicas de dithering en algunos casos para minimizar banding). Para aplicaciones de visión, si el rango dinámico importa (ej. imágenes médicas, científicos) se mantienen 16-bit o formato HDR.

En este vídeo vamos a ver tres ejemplos visuales: cómo convertir de float a uint8, cómo estimar tamaños de memoria y por qué aparece el banding cuando bajamos de 16 a 8 bits. Junto con el ejemplo de convertir de float a uint8, vamos a ver qué ocurre cuando introducimos sin definirlos correctamente; para los tamaños de memoria vamos en los diferentes casos de calidad de imagen y de video; y por último, vamos a observar cómo aparecen bandas en la imagen cuando se baja el número de bits en los que se codifica la imagen.

¡Fantástico! Has completado este apartado.

### Lesson 17 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/R_CW67-FQ4_MhV08fO5gIwN5RESE0Nca</sub>

Introducción

En los apartados anteriores hemos construido los pilares sobre lo que se construye la imagen digital: que una imagen es una matriz de números (píxeles), que esos números pueden organizarse en canales (por ejemplo, RGB) y que distintos espacios de color nos permiten interpretar mejor esos valores según la tarea. Con estas piezas ya colocadas, estamos listos para dar un paso clave: leer la distribución de esos números. Ahí entra el histograma.

El histograma no es más que un resumen estadístico de la imagen: cuenta cuántos píxeles hay en cada nivel de intensidad (en escala de grises) o en cada rango de un canal (en color). Es, por así decirlo, el “pulso” de la imagen. Si los niveles se apilan todos en la zona oscura, la foto estará subexpuesta; si se amontonan en las luces, estará lavada; si casi no hay valores intermedios, faltará contraste; si hay dos “montañitas” separadas, probablemente haya fondo y objeto claramente diferenciables. En otras palabras, antes de modificar una imagen conviene escuchar lo que su histograma nos está diciendo.

Este apartado nos enseñará a operar sobre la imagen guiándonos por su histograma para mejorar la imagen o prepararla mejor para algoritmos posteriores. Ahora nos ocuparemos de que los detalles sean visibles y las diferencias relevantes queden realzadas.

Este apartado nos enseñará a operar sobre la imagen guiándonos por su histograma para mejorar la imagen o prepararla mejor para algoritmos posteriores. Ahora nos ocuparemos de que los detalles sean visibles y las diferencias relevantes queden realzadas.

### Lesson 18 - Operación de negativo (inversión de intensidades)

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/Smtj1gXHfwIfJSWFxFulQKKb_YK5BJRa</sub>

Operación de negativo (inversión de intensidades)

Imaginemos que tomamos una fotografía en blanco y negro y la convertimos en su negativo, como en los antiguos rollos fotográficos. ¿Qué ocurre? Básicamente, lo oscuro se vuelve claro y lo claro se vuelve oscuro. La operación de negativo invierte la escala de intensidades de la imagen: los píxeles negros pasan a blanco y viceversa, con todos los niveles intermedios invertidos proporcionalmente. En términos simples, estamos creando la versión complementaria de la imagen original.

Esta transformación es muy fácil de aplicar y tiene algunas utilidades interesantes. Por ejemplo, si un algoritmo o procedimiento espera por defecto objetos oscuros sobre fondo claro, pero nuestra imagen tiene el objeto claro sobre fondo oscuro, invertir los tonos facilita el procesamiento. También puede usarse para mejorar la visibilidad de ciertos detalles: en imágenes médicas o astronómicas, a veces ver la versión negativa ayuda a resaltar estructuras que en la original pasan desapercibidas.

Veámoslo desde un punto algo matemático. Si
 representa uno de los canales de nuestra imagen, ya sea cualquier canal de RGB; sólo iluminancia Y, si usamos YCbCr; o dependiendo de la codificación de color que hayamos decidido usar, e
 es el resultado después de aplicar la operación de negativo. Entonces la fórmula matemática que relaciona el valor de los pixeles originales, y su resultado es,

Nota matemática: Esta función es una involución, ya que al aplicarlo dos veces, tenemos el resultado original:

Ejemplo - Inversión segura por tipo de dato
import numpy as np
import cv2 as cv

def invert_image(img):
    """
    Invierte una imagen por píxel, respetando el tipo:
    - uint8/uint16: usa bitwise_not
    - float32/float64: asume [0,1] y aplica 1 - x
    """
    if img.dtype == np.uint8 or img.dtype == np.uint16:
        return cv.bitwise_not(img)  # equivalente a (max - x)
    elif np.issubdtype(img.dtype, np.floating):
        return np.clip(1.0 - img, 0.0, 1.0).astype(img.dtype)
    else:
        raise TypeError(f"Tipo no soportado: {img.dtype}")

### Lesson 19 - Corrección de gamma

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/IOkEsNXBaa2mCmPzDqrZptaofCr3IhHS</sub>

Corrección de gamma

La corrección de gamma es una transformación que nos permite aclarar u oscurecer una imagen de forma no lineal, ajustando su brillo percibido. A diferencia de simplemente subir o bajar el brillo de forma uniforme, la corrección gamma aplica una curva exponencial a los valores de intensidad. En términos prácticos, esto significa que modificamos cuánto se enfatizan las sombras o las luces de la imagen sin invertir los valores, solo redistribuyéndolos.

Imaginemos un control deslizante llamado "gamma". Si ajustamos gamma < 1 (por ejemplo 0,5), obtenemos una curva cóncava que aclara las zonas oscuras: las sombras se iluminan más y la imagen en general se ve más clara, sin llegar a saturar las altas luces. En cambio, si usamos gamma > 1 (por ejemplo 2,0), obtenemos una curva convexa que oscurece las zonas claras: reduce el brillo de las partes luminosas y profundiza las sombras, haciendo la imagen más oscura en conjunto.

Nota: En ambos casos el orden de los píxeles de más oscuro a más claro se mantiene (no estamos creando un negativo), pero la distribución del histograma cambia. Con gamma < 1, los valores del histograma se "desplazan" hacia niveles más altos (más claridad en sombras), y con gamma > 1 se desplazan hacia niveles más bajos (más detalle en luces altas).

Luego si volvemos a ver esta transformación desde un punto de vista matemático, si
 vuelve a ser la imagen original, e
 el resultado, la relación entre ambas imágenes es,

〖
〗

La corrección de gamma se utiliza mucho para mejorar fotos subexpuestas o sobreexpuestas. Por ejemplo, si una foto salió muy oscura, aplicar una gamma menor que 1 aclarará las sombras sin quemar las luces existentes. Al revés, si una escena está demasiado clara, una gamma mayor que 1 recuperará detalles en las zonas claras. También es un concepto clave en la visualización correcta de imágenes en pantallas (el estándar de color sRGB incluye una corrección gamma para que las imágenes se vean naturales a nuestros ojos). En edición de imágenes, ajustar la curva de tonos (que es esencialmente ajustar la gamma en distintos rangos) nos permite realzar detalles tanto en sombras como en iluminaciones.

Ejemplo 1 - “Aclarar/oscurecer” correctamente una imagen sRGB
def gamma_on_srgb(img_srgb01, alpha, apply_on_luma=False, rgb2ycbcr=None, ycbcr2rgb=None):
    """
    img_srgb01: float [0,1] en sRGB
    alpha: exponent (alpha<1 aclara)
    apply_on_luma: si True, eleva sólo la Y' (luma) para mantener el color
    """
    if not apply_on_luma:
        # Linealizar -> aplicar gamma -> volver a sRGB
        lin = srgb_to_linear(img_srgb01)
        lin_g = gamma_linear(lin, alpha)
        return linear_to_srgb(lin_g)
    else:
        # Opción simple usando Y' (si se dispone de conversión)
        import cv2 as cv
        u8 = np.clip(img_srgb01*255.0, 0, 255).astype(np.uint8)
        ycrcb = cv.cvtColor((u8[...,::-1]), cv.COLOR_RGB2YCrCb)  # RGB->YCrCb
        Y, Cr, Cb = cv.split(ycrcb)
        Y = np.clip((Y.astype(np.float32)/255.0)**alpha, 0, 1)
        Y = (Y*255.0 + 0.5).astype(np.uint8)
        out = cv.merge([Y, Cr, Cb])
        out = cv.cvtColor(out, cv.COLOR_YCrCb2RGB).astype(np.float32)/255.0
        return out

Ejemplo 2 - Ver el impacto en el histograma
def histogram(img01, bins=256):
    hist, edges = np.histogram(img01.ravel(), bins=bins, range=(0,1))
    return hist, edges

# Ejemplo: comparar histograma antes/después para alpha=0.6 y alpha=1.6

### Lesson 20 - Estiramiento de contraste o stretching

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/RmYcYjc9RS3d6CLXgxiJBaxM0kx7xbkn</sub>

Estiramiento de contraste o stretching

El estiramiento de contraste es una técnica que expande el rango de intensidades de una imagen para usar todo el espectro disponible desde el negro hasta el blanco. Muchas veces tomamos una foto y la vemos "apagada" o poco contrastada: los negros se ven grisáceos, los blancos no son muy brillantes, y en general la imagen luce plana.

Esto suele reflejarse en el histograma: en lugar de ocupar toda la anchura (0 a 255, por ejemplo, en una imagen de 8 bits), los valores están concentrados en un intervalo más estrecho. El estiramiento de contraste toma el valor más oscuro presente en la imagen y lo mapea a negro puro, y el valor más claro lo mapea a blanco puro, redistribuyendo linealmente todos los demás valores entre 0 y el máximo. Como resultado, el histograma "se estira" a lo largo de todo el rango y la imagen gana contraste.

Pensemos en el estiramiento de contraste como en recalibrar la regla con la que mides los tonos. La imagen ocupa sólo un trozo del rango disponible (sombras apretadas, altas luces tímidas); el auto-contraste detecta cuál es el rango “útil” y lo expande para que 0 signifique “negro de verdad” y 1 (o 255) signifique “blanco de verdad”. Así aumentamos la pendiente de los gradientes y los detalles se vuelven legibles… si elegimos bien dónde empiezan y acaban los “extremos”.

Esto aumenta la separación entre tonos oscuros y claros, haciendo que los detalles se distingan mejor. Es un proceso automático sencillo (no requiere decidir muchos parámetros, más allá de detectar mínimos y máximos de intensidad) y muy útil como primer paso de realce en imágenes con poca iluminación.

Ahora volvemos a definir esta operación, pero desde un punto de vista matemático, donde
 es la imagen original,
 es la imagen resultada,

Por lo que podemos deducir por la relación entre ambas imágenes es que, todo lo que quede por debajo de
 caerán a negro; mientras que por encima de
, subirán a blanco; y todo que lo intermedio se estira linealmente.

¿Cuándo aplicarlo? Cuando la imagen original tiene un contraste bajo o está mal aprovechado el rango dinámico. Un caso típico es una foto tomada con niebla o con iluminación muy suave: toda la imagen está en tonos medios y nada es verdaderamente negro ni blanco. Al estirar el contraste, la niebla se atenúa y aparecen negros más profundos y brillos más definidos. Otro caso es al escanear documentos antiguos que se ven grisáceos: el stretching puede mejorar la legibilidad haciendo el fondo más blanco y las letras más negras. Es importante notar que esta técnica no crea detalles nuevos, solo mejora la distribución de intensidades; si una zona estaba completamente plana (sin variación de píxeles), seguirá plana pero ahora en otro nivel.

Ejemplo — Auto-contraste en lineal con soft-knee (evitar cortar altas luces)
import cv2 as cv, numpy as np

def srgb_to_linear(u8):
    u = u8.astype(np.float32) / 255.0
    a = u <= 0.04045
    out = np.empty_like(u, dtype=np.float32)
    out[a]  = u[a] / 12.92
    out[~a] = ((u[~a] + 0.055) / 1.055) ** 2.4
    return out

def linear_to_srgb_f32(v):
    v = np.clip(v, 0.0, 1.0)
    a = v <= 0.0031308
    out = np.empty_like(v, dtype=np.float32)
    out[a]  = 12.92 * v[a]
    out[~a] = 1.055 * (v[~a] ** (1/2.4)) - 0.055
    return out

def autocontrast_softknee_lin(gray_lin, plow=1.0, phigh=99.0, knee_strength=6.0):
    # gray_lin: float32 [0..1] lineal (luminancia aproximada)
    gl = gray_lin.reshape(-1)
    lo, hi = np.percentile(gl, [plow, phigh])
    lo, hi = float(lo), float(hi - 1e-6)
    # tramo lineal normalizado
    t = np.clip((gray_lin - lo) / (hi - lo), 0.0, 1.0)
    # soft-knee en altas luces (logística centrada en 0.85)
    x = t
    k = knee_strength
    knee = 1.0 / (1.0 + np.exp(-k*(x - 0.85)))  # 0..1
    mix = 0.25  # mezcla cuánto de knee aplicas
    t2 = (1 - mix)*x + mix*(x - 0.15*knee)      # compresión suave final
    return np.clip(t2, 0.0, 1.0)

bgr = cv.imread("entrada.png")
rgb = bgr[..., ::-1].astype(np.uint8)
lin = srgb_to_linear(rgb)                       # RGB lineal [0..1]
# Luminancia lineal (Rec.709)
Ylin = 0.2126*lin[...,0] + 0.7152*lin[...,1] + 0.0722*lin[...,2]
# Ajuste en Y lineal y reescala por canal (manteniendo cromas)
Yadj = autocontrast_softknee_lin(Ylin, 1.0, 99.0, knee_strength=6.0)
eps = 1e-6
scale = (Yadj + eps) / (Ylin + eps)
lin_adj = np.clip(lin * scale[..., None], 0.0, 1.0)
srgb = linear_to_srgb_f32(lin_adj)
out = (np.clip(srgb, 0, 1)*255).astype(np.uint8)[..., ::-1]

cv.imwrite("autocontrast_softknee_linear.png", out)

Qué ganamos: contraste global realista en sombras y medios sin “reventar” especulares ni cielos.

### Lesson 21 - Segmentación de histograma o thresholding

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/rXLZSmFrQrCWfrXzM3rryPYP3RVul7KE</sub>

Segmentación de histograma o thresholding

La segmentación de histograma, o comúnmente conocida como umbralización o thresholding, es una operación fundamental para separar elementos dentro de una imagen basándose en su intensidad. Consiste en elegir un valor de umbral y convertir la imagen en blanco y negro (binaria) según ese valor. En otras palabras, decidimos que todos los píxeles por encima de cierto nivel de gris serán blancos (por ejemplo, objetos) y los por debajo serán negros (fondo), o viceversa, dependiendo de lo que nos interese resaltar. Esta transformación simplifica muchísimo la imagen, reduciéndola a dos categorías: píxel activo o inactivo, algo muy útil para reconocer formas, textos u objetos claramente.

¿Cómo sabemos qué umbral elegir? Aquí es donde entra en juego el histograma. Si observamos el histograma de una imagen donde hay objeto y fondo diferenciados, a veces veremos dos grupos de barras separados: uno corresponde a los tonos del fondo y otro a los del objeto. Por ejemplo, imagina una hoja con texto negro sobre papel blanco escaneada: en el histograma habrá un pico hacia la izquierda (negros del texto) y otro hacia la derecha (blancos del papel). En este caso, escoger un umbral en el valle entre ambos picos nos separará casi perfectamente el texto del fondo.

Como podemos ver en este ejemplo, dependiendo de la elección del umbral, vamos a poder identificar correctamente o no los dos tucanes que aparecen en la imagen original. Aunque en este ejemplo debido a los colores de los tucanes, sigue siendo difícil identificar claramente a los tucanes.

De nuevo, matemáticamente, para una imagen
 y un umbral
, tenemos que la imagen resultante
  sigue la relación,

En imágenes más complejas (como la del anterior ejemplo), puede no haber una separación tan clara, pero aún así técnicas automáticas (como el algoritmo de Otsu, que busca el mejor umbral automáticamente analizando la distribución del histograma) pueden ayudar.

Este método es muy utilizado en vision por computador y procesamiento de imágenes. Por ejemplo, para reconocimiento de caracteres (OCR) conviene binarizar la imagen de un documento, de manera que las letras negras queden bien definidas sobre un fondo blanco puro. En control de calidad industrial, si queremos que una máquina detecte piezas sobre una cinta transportadora, podríamos iluminar la escena de forma que las piezas sean mucho más claras que el fondo (o viceversa) y luego umbralizar para obtener una imagen binaria donde las piezas destaquen claramente. También en fotografía científica, como analizar células en un portaobjetos: ajustando un umbral podemos separar las células (digerentes en intensidad) del fondo del porta. Eso sí, la elección del umbral es crítica: si ponemos un valor inadecuado, podríamos perder partes importantes (por ejemplo, si el umbral es demasiado alto, quizá partes oscuras del objeto se confundan con el fondo).

Ejemplo – Umbral multi-clase
import numpy as np

def multi_otsu_2thresholds(img_gray_u8):
    # Búsqueda O(N^2) sobre 256 niveles; suficiente para docencia
    hist, _ = np.histogram(img_gray_u8.ravel(), bins=256, range=(0,256))
    P = hist.astype(np.float64) / hist.sum()
    omega = np.cumsum(P)
    mu = np.cumsum(P * np.arange(256))
    mu_t = mu[-1]

    best = (0.0, 0, 0)
    for t1 in range(1, 255):
        for t2 in range(t1+1, 255):
            w0, w1, w2 = omega[t1], omega[t2]-omega[t1], 1.0-omega[t2]
            if min(w0,w1,w2) <= 1e-12:
                continue
            m0 = mu[t1]/w0
            m1 = (mu[t2]-mu[t1])/w1
            m2 = (mu_t-mu[t2])/w2
            sigma_b = w0*(m0-mu_t)**2 + w1*(m1-mu_t)**2 + w2*(m2-mu_t)**2
            if sigma_b > best[0]:
                best = (sigma_b, t1, t2)
    return best[1], best[2]

### Lesson 22 - Ecualización de histograma (HE)

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/PnG2mtoI9pe4IV9bBardvHR5DGJpt7e6</sub>

Ecualización de histograma (HE)

La ecualización de histograma es una técnica automática muy poderosa para mejorar el contraste de una imagen de forma global. Su objetivo es redistribuir las frecuencias de los niveles de gris de manera más uniforme. Dicho de otro modo, trata de "aplanar" el histograma para que todos los rangos de intensidades tengan, más o menos, la misma cantidad de píxeles (o al menos, una distribución más equilibrada). ¿Y qué se logra con eso? Que las áreas oscuras ganen brillo y las claras quizá se atenúen un poco, revelando detalles que antes no se veían, especialmente en imágenes donde el contraste original es pobre o está muy sesgado hacia un extremo del rango.

Podemos pensar en la ecualización de histograma como un re-encuadre de la imagen en términos de intensidad: si la mayoría de los píxeles estaban concentrados, por ejemplo, en niveles oscuros, la ecualización les dará un "empujón" hacia niveles más altos para expandir esa zona oscura y desplegar detalles. A diferencia del estiramiento de contraste (que es lineal y solo se fija en mínimos y máximos), la ecualización es no lineal y adaptativa: se basa en la forma acumulada del histograma para asignar de nuevo intensidades. En la práctica, cada píxel cambia a un nuevo valor proporcional a cuántos píxeles eran más oscuros que él en la imagen original. El resultado típico es que áreas enteras de la imagen que estaban muy oscuras aparecen más claras y con matices, y las muy claras muestran también más detalle al redistribuirse sus tonos.

Algoritmo de HE (Histogram Equalization)

Pensemos en el histograma como una cola en la que algunos niveles de gris están a rebosar (muchos píxeles) y otros casi vacíos. La ecualización redistribuye esa gente por todas las “taquillas” disponibles (todos los niveles posibles), para que la imagen aproveche mejor el rango: las sombras ganan matices, las luces recuperan detalle y, en general, aparece contraste donde antes no lo había.

Calcular el histograma.

Recorremos la imagen y contamos cuántos píxeles tienen valor 0, cuántos valor 1, …, hasta 255. Eso te da una tabla de 256 números: el histograma, al que llamaremos

 Suma acumulada (la clave).

Construimos la acumulada del histograma: para cada nivel k, sumamos todos los píxeles con valor ≤ k. Esto nos dice “¿cuántos píxeles son tan oscuros o más oscuros que este nivel?”. A esta suma se la suele llamar CDF (distribución acumulada) CDF.

 Una vez tenemos la acumulada en CDF, creamos una función de probabilidad, PMF, donde a cada elemento acumulado le asignamos un valor probabilidad,

Antes de terminar, hacemos la ecualización del histograma acumulativo con la función de probabilidad,

Aplicar la ecualización a la imagen original

¿Por qué a veces no queda “perfectamente plano” el histograma? Porque la imagen tiene valores discretos y muchos píxeles se mueven en bloque a niveles cercanos. Además, si había picos muy marcados (por ejemplo, grandes zonas uniformes), la redistribución puede seguir mostrando montañitas. El objetivo no es un histograma recto como una mesa, sino una ocupación más equilibrada del rango para ganar detalle visible.

¿Dónde se nota su eficacia? En imágenes como radiografías, fotografías aéreas o escenas nocturnas, donde a veces todo está muy concentrado en un rango de intensidad. Por ejemplo, una radiografía puede lucir "apagada": aplicas ecualización de histograma y de repente huesos y tejidos se distinguen mejor porque el algoritmo les ha asignado intensidades aprovechando todo el espectro de gris disponible. Lo mismo con una foto nocturna donde casi todo era negro con algunas luces: tras ecualizar, ves más gradaciones en la oscuridad. Hay que mencionar que la ecualización puede introducir ruido visual o aspecto artificial en algunos casos, ya que al estirar tanto el contraste local puede amplificar el ruido de la imagen. Aun así, es una herramienta muy útil como punto de partida para realzar imágenes automáticamente sin tener que elegir parámetros manualmente.

1 of 2
Ejemplo - Implementación del algoritmo de equalización
import numpy as np

def equalize_hist_uint(img, mask=None):
    assert img.ndim == 2 and img.dtype in (np.uint8, np.uint16)
    L = 256 if img.dtype == np.uint8 else 65536

    if mask is not None:
        m = (mask > 0)
        if not np.any(m):
            return img.copy()
        data = img[m]
    else:
        data = img.reshape(-1)

    hist = np.bincount(data, minlength=L).astype(np.float64)
    cdf = np.cumsum(hist)
    N = cdf[-1]
    if N == 0 or np.count_nonzero(hist) == 1:
        return img.copy()

    cdf_min = cdf[np.nonzero(cdf)][0]
    lut = np.floor((cdf - cdf_min) / (N - cdf_min) * (L - 1) + 0.5)
    lut = np.clip(lut, 0, L-1).astype(img.dtype)

    out = lut[img]
    return out

### Lesson 23 - Ecualización adaptativa de histograma (AHE)

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/dznEFpQJAeuDS0bC0j5zFegYYLeS_s8j</sub>

Ecualización adaptativa de histograma (AHE)

La ecualización global (la que acabamos de ver) tiene un inconveniente: aplica el mismo criterio a toda la imagen, sin distinguir entre regiones que podrían necesitar distintos tratos. ¿Qué pasa si en una misma foto tenemos una zona que ya es bastante clara y otra muy oscura? La ecualización global puede mejorar la parte oscura pero quizás sobreexponga la parte que ya era clara, o al revés. Para abordar este problema existe la ecualización de histograma adaptativa, abreviada AHE por sus siglas en inglés (Adaptive Histogram Equalization). La idea es sencilla: en lugar de calcular un único histograma para toda la imagen, se calculan histogramas por zonas o vecindarios más pequeños, y se ecualiza cada parte por separado. De ese modo, cada región de la imagen realza su contraste localmente.

Podemos imaginar dividir la imagen en una cuadrícula (o tomar para cada píxel su vecindario cercano) y ecualizar esos fragmentos individualmente. Así, las partes oscuras en una esquina se estiran independientemente de las partes claras en otra esquina. Esto logra que detalles locales aparezcan simultáneamente en sombras profundas y en áreas brillantes de la misma imagen. Por ejemplo, piensa en una foto donde el sujeto en primer plano está a contraluz (oscuro) pero el fondo está soleado: la ecualización global tal vez arruine el fondo si intenta aclarar al sujeto. La AHE, en cambio, puede aclarar al sujeto usando el histograma de su vecindario sin tocar tanto el histograma del cielo de fondo.

La ecualización adaptativa potencia muchísimo el contraste local, revelando detalles que ni siquiera la ecualización global podía mostrar. Es excelente para imágenes con iluminación muy heterogénea, como escenas al aire libre con sombras marcadas y áreas soleadas juntas, o imágenes médicas con diferentes tejidos que necesitan distintos niveles de contraste. Sin embargo, esta potencia tiene su lado negativo: AHE tiende a amplificar el ruido y puede generar efectos no deseados (por ejemplo, pequeñas variaciones en zonas originalmente uniformes se pueden convertir en manchas contrastadas). Debido a esto, rara vez se usa AHE pura en aplicaciones prácticas sin algún tipo de control. Como podemos ver en las imágenes de ejemplo, se generan “tiles” o baldosas, donde dependiendo de la información que hay en esa baldosa, la ecualización se genera de manera diferente, provocando saltos entre regiones y no obteniendo una imagen final correcta.

Ejemplo – Implementación de algoritmo AHE
import numpy as np

def _he_lut_uint8(tile):
    # Histograma local y LUT (igual que HE global, pero por baldosa)
    hist = np.bincount(tile.ravel(), minlength=256).astype(np.float64)
    cdf  = np.cumsum(hist)
    if cdf[-1] == 0:  # baldosa vacía (no debería ocurrir en imágenes reales)
        return np.arange(256, dtype=np.uint8)
    cdf_min = cdf[np.nonzero(cdf)][0]
    # Formula de ecualización: (cdf(v) - cdf_min) / (M*N - cdf_min) * (L-1)
    # M*N es el total de píxeles en la baldosa, que es cdf[-1]
    lut = np.floor((cdf - cdf_min) / (cdf[-1] - cdf_min + 1e-12) * 255.0 + 0.5)
    lut = np.clip(lut, 0, 255).astype(np.uint8)
    return lut

def ahe_uint8(gray_u8, tile_h=64, tile_w=64, strength=1.0):
    """
    AHE en luminancia/gris, uint8. Aplica la LUT de cada baldosa.
    (Implementación simplificada sin interpolación entre baldosas para ilustrar el concepto local)
    strength in [0,1]: 1.0 = AHE total, 0.0 = original.
    """
    H, W = gray_u8.shape
    # Definir rejilla de baldosas (bordes incluidos)
    y_edges = list(range(0, H, tile_h)) + [H]
    x_edges = list(range(0, W, tile_w)) + [W]
    ny, nx = len(y_edges)-1, len(x_edges)-1

    out = np.empty_like(gray_u8, dtype=np.uint8)

    # Recorremos por baldosas, calculamos LUT y aplicamos
    for j in range(ny):
        y0, y1 = y_edges[j], y_edges[j+1]
        for i in range(nx):
            x0, x1 = x_edges[i], x_edges[i+1]

            tile = gray_u8[y0:y1, x0:x1]
            lut_current = _he_lut_uint8(tile)

            # Aplicar la LUT de la baldosa a todos los píxeles de esa baldosa
            out[y0:y1, x0:x1] = lut_current[tile]

    if strength < 1.0:
        # Mezcla con la original para contener el realce (si strength < 1)
        out = np.clip((1.0-strength)*gray_u8.astype(np.float32) + strength*out.astype(np.float32), 0, 255).astype(np.uint8)

    return out

### Lesson 24 - Ecualización adaptativa de histograma por contraste (CLAHE)

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/kYwTpicFT_FHGfHc1JH3jMzjWcrFlod5</sub>

Ecualización adaptativa de histograma por contraste (CLAHE)

Finalmente, para evitar los problemas de exceso de contraste y ruido que puede introducir la AHE, se recurre a una variante llamada ecualización adaptativa con limitación de contraste, conocida por sus siglas CLAHE (Contrast-Limited Adaptive Histogram Equalization). La técnica es similar a la AHE descrita anteriormente (divide la imagen en regiones y ecualiza cada una), pero añade un paso importante: limita cuánto se puede amplificar el contraste en cada región. En términos técnicos, esto significa que se fija un umbral de acumulación en el histograma local: si un nivel de gris supera cierta frecuencia (es decir, hay un pico muy alto de píxeles del mismo valor en esa ventana), esa frecuencia extra se redistribuye a otros niveles antes de aplicar la ecualización. Así se evita que en una región pequeña un tono domine exageradamente y produzca artefactos.

¿Qué implicaciones tiene esto visualmente? Que CLAHE suaviza los resultados de la ecualización adaptativa, previniendo la aparición de ruido excesivo o áreas con contrastes artificialmente altos. En esencia obtenemos todavía la mejora de detalle local que aporta AHE, pero controlando los “pies en el acelerador” para que la imagen resultante se vea más natural. Muchos programas de procesamiento de imágenes y visión por computador usan CLAHE por defecto cuando se quiere mejorar contraste local, precisamente porque ofrece un buen equilibrio: mejora detalles en sombras y luces de forma adaptativa, pero sin pasarse al punto de hacer la imagen estridente.

Cuándo usar CLAHE: En la mayoría de las situaciones en las que AHE sería útil pero tenemos preocupación por el ruido. Imágenes médicas como tomografías o resonancias suelen beneficiarse de CLAHE para resaltar estructuras de interés sin amplificar demasiado el grano de la imagen. En fotografía general, CLAHE puede ser muy útil para fotos con iluminación muy desigual (como paisajes con zonas a pleno sol y otras en sombra profunda, o interiores con zonas iluminadas por lámparas y rincones oscuros). Tras aplicar CLAHE, la foto suele lucir con mayor claridad en las sombras y moderación en las luces, pero manteniendo un aspecto realista. Es, en resumen, una de las técnicas más recomendables cuando queremos lo mejor de ambos mundos: contraste local mejorado pero controlado.

Antes de finalizar, en el siguiente video vamos a ver un ejemplo de la implementación de operaciones puntuales de histograma aplicadas a una imagen. Además, vamos a comparar los histogramas de cada una de las operaciones.

¡Fantástico! Has completado este apartado.


## Recursos y enlaces

- [Unidad 1. Fundamentos de Visión por computador e imagen digital.](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/sssOuc1hXgb2pkkXQdugf_EVelPQz9hs)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/RmdqNZMu52kIfQL3c_fvuwgpOS111C99)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/-NCIfYRKc2PIdvaz6wxtbYHqlc8KHjNU)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/NBkfhG_e7DR_VNYb2sV5qrU7Zoa2hy6U)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/jQqNRBTfkH5DE4YcGwMy56qzUzKNxvbz)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/F76haM2LatptQotsAL4Xee3whqGwPayy)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/GGl4Wwapkbc5SDWWN-ESTB3CB8zMq1cM)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/PQcrmqCi23APc2nOOSUGlZQm-c07L_Sx)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/E6fZkb6H-yh3i6fXG9EFw2T9yXcuEXbE)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/4YvbcCheBk-sDQWY0KMOxqcxTlLQKYZ1)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/GvC1QddGFFhyZ3Sg-z20fY9Vj7Qnt_vZ)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/xM_djZUlLHsp_ul3zXwrMQzwaLEDDINO)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/U0ZQKotZv9yR1rz33rZdWEcmoWBGwdIG)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/HPE6ThwfCSNlEhSEqyk2Zo3gvgyO4BZo)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/U3LgYQGkOn-RGySY9Dv5sBE6AlYSLnCM)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/f8OgFcFfSjS9UbSOmEK0FkDHB8RUc_NJ)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/R_CW67-FQ4_MhV08fO5gIwN5RESE0Nca)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/Smtj1gXHfwIfJSWFxFulQKKb_YK5BJRa)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/IOkEsNXBaa2mCmPzDqrZptaofCr3IhHS)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/RmYcYjc9RS3d6CLXgxiJBaxM0kx7xbkn)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/rXLZSmFrQrCWfrXzM3rryPYP3RVul7KE)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/PnG2mtoI9pe4IV9bBardvHR5DGJpt7e6)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/dznEFpQJAeuDS0bC0j5zFegYYLeS_s8j)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/kYwTpicFT_FHGfHc1JH3jMzjWcrFlod5)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/index.html#/lessons/kIIH8ThNKIcgKkNhtbX6lrPNF4u4Xywp)
- [IMG](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/assets/UTAD_ISD_VC_45.jpg)
- [SOURCE](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/assets/UTAD_INSD_VICO_6.mp4?v=1)
- [IMG](https://u-tad.blackboard.com/courses/1/2609_INSD4_VICO_A/content/_783731_1/scormcontent/assets/UTAD_INSD_VICO_6.jpg)