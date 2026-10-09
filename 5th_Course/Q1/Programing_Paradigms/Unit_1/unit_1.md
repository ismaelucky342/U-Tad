# 2609_INSD4_PAPR_A

**SCORM:** _739661_1
**URL del contenido:** https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormdriver/indexAPI.html

## Contenido

### INTRODUCCIÓN Y OBJETIVOS

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/preview</sub>

Unidad 1. Programación funcional.
COMENZAR CURSO
INTRODUCCIÓN Y OBJETIVOS
Introducción y objetivos
INTRODUCCIÓN A LOS PARADIGMAS DE PROGRAMACIÓN
Introducción
Programación imperativa
Programación declarativa
Programación multiparadigma
Aplicaciones prácticas y tendencias futuras
PREPARACIÓN DEL ENTORNO DE TRABAJO
Introducción
Instalación del entorno de trabajo
Entornos virtuales
PROGRAMACIÓN FUNCIONAL. USO DE CALLBACKS
Introducción
Paradigma de programación funcional
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

### Lesson 1 - Introducción y objetivos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/WC5N7v4_XJ0OTfAci5aMPMNbTOk0hmbV</sub>

Introducción y objetivos

Introducción

A lo largo de esta unidad haremos un repaso a los diferentes paradigmas de programación que existen y se utilizan en la actualidad, así como por las necesidades que cubre cada uno de ellos. Muchos de ellos ya son conocidos y los utilizamos en nuestro día a día, pero no les hemos puesto una etiqueta que los identifique como tal. Conocerlos y diferenciarlos será una labor clave en el proceso de desarrollo y mantenimiento de software.

Esta asignatura será totalmente práctica, y nos centraremos en Python como lenguaje de programación. Es un lenguaje muy versátil que permitirá explorar los diferentes paradigmas que existen. Para ello veremos una pequeña introducción a Python, principalmente a las características que necesitamos. También haremos uso de entornos virtuales de Python, los cuales están muy extendidos en los equipos de desarrollo actuales, y nos permitirán reducir las dependencias con la maquina en la que ejecutemos nuestro software. En el apartado 2 dispondremos de instrucciones para preparar el entorno de prácticas utilizando Visual Studio Code con entornos virtuales, ficheros .py y .ipynb

Finalmente nos centraremos en el paradigma de programación funcional dentro de Python. Aunque no es el lenguaje que mejor encaja con este paradigma, nos permitirá implementar ciertas funciones como callbacks o wrappers para funciones.

Haz clic para voltear

Introducción a los paradigmas de programación

Haz clic para voltear

Todos los paradigmas de programación tienen algo en común: Buscan la modularidad del software para mejorar su eficiencia y costes de mantenimiento. Además, esta modularización permite limitar el alcance del software dentro del equipo donde este se ejecuta, lo que proporciona un punto muy importante de seguridad.

Haz clic para voltear

Preparación del entorno de trabajo

Haz clic para voltear

Tras haber visto los distintos paradigmas de programación que existen en la actualidad, vamos a preparar nuestro entorno de desarrollo. En este caso trabajaremos con Python, el cual es un lenguaje multiparadigma que nos permite una gran flexibilidad a la hora de desarrollar software. Python es un lenguaje de programación interpretado, es decir, un lenguaje de programación que no se compila para poder ejecutar las instrucciones en el propio lenguaje de la máquina, sino que debe existir un software instalado en el equipo que interprete las instrucciones de nuestro programa y las traduzca en tiempo real.

Haz clic para voltear

Programación funcional. Uso de Callback

Haz clic para voltear

En este apartado veremos en detalle en que se basa el paradigma de programación funcional, y veremos los distintos mecanismos funcionales existentes en Python para aprovecharlos de manera adecuada

Objetivos

Al finalizar esta unidad el alumno:

1

Comprenderá la definición de un paradigma de programación: Será capaz de definir que es un paradigma de programación y de definir su importancia en el desarrollo de software. Sabrá identificar las diferencias entre los paradigmas y como estos influyen en la forma de estructurar, organizar y resolver problemas en un programa. Además, habrá analizado ejemplos prácticos que muestren como la elección de un paradigma afecta a la claridad, la eficiencia y el mantenimiento del código

2

Conocer los principales paradigmas de programación que existen actualmente. Podrá reconocer los distintos paradigmas entendiendo sus principales características y ámbitos de aplicación. Tendrá la capacidad de comparar ventajas y desventajas de cada paradigma en función del tipo de problema a resolver. Además, sabrá identificar lenguajes de programación representativos de cada paradigma, relacionando sus características con el enfoque que proponen

3

Se introducirá en el desarrollo en Python y el uso de entornos virtuales. Aprenderá a instalar y configurar Python en su entorno de trabajo, manteniendo una serie de buenas prácticas. Comprenderá el concepto de “entorno virtual” y su importancia para aislar dependencias y gestionar versiones de paquetes. Sabrá crear y gestionar entornos virtuales para diferentes herramientas y librerías.

4

Entenderá en profundidad el paradigma de programación funcional en Python y sus aplicaciones. Conocerá las características de la programación funcional, y aprenderá a utilizar las distintas construcciones funcionales de las que dispone Python. Aplicará la programación funcional a la resolución de problemas reales, combinándola con otros paradigmas de Python de forma efectiva. Además, será capaz de identificar aquellos casos en los que conviene utilizar un enfoque funcional, viendo cómo puede mejorar la legibilidad y mantenibilidad del código

¡Comenzamos!

### Lesson 2 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/I1lyHm-uskytA7A6Jdy49tsYS0RBpWJV</sub>

Introducción
SEGÚN LA RAE, UN PARADIGMA ES:

Ejemplo o ejemplar

Teoría o conjunto de teorías cuyo núcleo central se acepta sin cuestionar y que suministra la base y modelo para resolver problema y avanzar en el conocimiento. (Ej: Paradigma Newtoniano)

Relación de elementos que comparten un mismo contexto fonológico, morfológico o sintáctico en función de sus propiedades lingüísticas

Esquema formar en el que se organizan las palabras que admiten modificaciones flexivas o derivativas

Como se puede ver, ninguna de las definiciones formales hace referencia al desarrollo de software o programación, pero todas ellas tienen algo en común: Todas las definiciones hacen referencia a un conjunto de entidades que comparten una base, y que sirven como modelo para una clasificación. Quizá la definición más aproximada al ámbito del desarrollo de software sea “Teoría o conjunto de teorías cuyo núcleo central se acepta sin cuestionar y que suministra la base y modelo para resolver problema y avanzar en el conocimiento”.

Por lo tanto, diremos que un Paradigma de Programación es un modelo que nos permite definir un estilo fundamental de programación, sirviendo como base para avanzar en el desarrollo de software.

El concepto de “paradigma de programación” surge en 1978, y busca clasificar los distintos estilos fundamentales de programación ofreciendo múltiples conceptos y abstracciones que los desarrolladores pueden utilizar para definir el software. Estas abstracciones en la actualizad nos son bastante conocidas. Conceptos como funciones, variables, objetos, flujos de datos… nos sirven para definir los distintos estilos de desarrollo, y abstraernos de la arquitectura básica del sistema para el que estamos desarrollando.

Un lenguaje de programación no tiene por qué cumplir un solo paradigma. De hecho, la mayoría de lenguajes modernos son multiparadigma. Esto quiere decir que normalmente implementan conceptos de diferentes paradigmas fundamentales.

Todos los paradigmas de programación tienen algo en común: Buscan la modularidad del software para mejorar su eficiencia y costes de mantenimiento. Además, esta modularización permite limitar el alcance del software dentro del equipo donde este se ejecuta, lo que proporciona un punto muy importante de seguridad.

Actualmente los paradigmas de programación se dividen en dos bloques principales: Programación imperativa y Programación declarativa

¿Todo listo? ¡Empezamos!

### Lesson 3 - Programación imperativa

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/ZwVJdEJRA5eYQM7mlOA8Blys6QxXj6zB</sub>

Programación imperativa

El paradigma de programación imperativa se trata del paradigma de programación más antiguo, y del primero que se definió.  El termino viene de Imperae (ordenar), por lo que podemos deducir que el paradigma consistirá en dar ordenes especificas para que nuestro equipo las procese y ejecute.

En este paradigma se definirá paso a paso como se va a obtener el resultado mediante sentencias o instrucciones que deben estar claramente definidas. A través de las sentencias que definamos en nuestro programa se cambiará el estado de este, es decir, modificaremos sus datos. El programa ejecutará siempre las sentencias de forma secuencia, una detrás de otras, lo que nos proporcionará siempre un claro determinismo en la salida de nuestro software.

Para hacer una analogía, podemos pensar en una receta de cocina para una tarta, donde debemos tener los pasos a seguir bien definidos y desglosados, de manera que siguiéndolos uno a uno podremos llegar al resultado final (La tarta perfectamente cocinada y decorada). Por cada paso que llevemos a cabo estaríamos modificando la tarta (el estado de nuestro programa), y siempre debemos seguir la receta secuencialmente.

Los lenguajes que trabajan con programación imperativa suelen encontrarse a un nivel bastante cercano al sistema. Esto quiere decir que generalmente nos obligan a gestionar memoria, instrucciones, datos a nivel de bit o incluso registros de CPU. Trabajar a tan bajo nivel supone la necesidad de una gran cantidad de líneas de código fuente para definir tareas que, en otros paradigmas, se pueden conseguir con una pequeña parte de las instrucciones que se ejecuten. Algunos ejemplos de lenguajes que implementan el paradigma de programación imperativa son:

C/C++

Java

Pascal

Cobol

FORTRAN

C#

Python

Dentro de la programación imperativa podemos encontrar los paradigmas de programación estructurada, la procedimental y la programación orientada a objetos

Programación estructurada

1
2
3
4
1 de 4

Es un paradigma dentro de la programación imperativa que se orienta en la mejora de la claridad, calidad y tiempo de desarrollo de software utilizando únicamente subrutinas y funciones. Surge en 1966 con el teorema de la programación estructurada.

En los paradigmas anteriores a la programación estructurada era muy común el uso de la instrucción GoTo. Su funcionamiento es muy similar a la instrucción JUMP en ensamblador de MIPS: Definimos una etiqueta/línea de código y nuestro programa continúa la ejecución desde el punto que hemos definido. Esto, aunque parece muy útil al darnos una gran capacidad de reutilización de código, no es nada eficiente en términos de mantenibilidad y legibilidad del código. A continuación, se muestra un ejemplo escrito en Fortran para calcular el valor de Pi, utilizando la instrucción GoTo. ¿Alguien se atreve a tratar de descifrar cómo funciona? (No os preocupéis, no es necesario)

2 de 4

Imagen 1 Ejemplo de Spaguethi Code con saltos de instruccion

3 de 4

Este modelo de programación era muy común, y si no se trataba con cuidado generaba lo que conocemos como Spaghetti Code, o “código espagueti”. Normalmente ponemos este nombre a código con muchos saltos, que es muy difícil de seguir y nos lleva muchas veces a puntos por los que ya hemos pasado, dificultando mucho la legibilidad y, por lo tanto, aumentando drásticamente el coste de mantenimiento del software.

La principal revolución llegó con el teorema de la programación estructurada, o teorema de Böhm-Jacopini: Cualquier algoritmo computable puede ser expresado utilizando únicamente las siguientes tres estructuras básicas de control:

Secuencia: Ejecución de un conjunto de instrucciones una tras otra, en orden lineal

Selección o condicional: Ejecución de una secuencia u otra dependiendo de una condición (if/then/else)

Iteración (ciclo o bucle): Repetición de una secuencia mientras se cumpla una condición (while/do-while/for)

4 de 4

Imagen 2 Estructuras fundamentales de la programación estructurada

Aunque el campo de la programación pueda parecer mucho más complejo, cualquier estructura extra que queramos se puede definir con una de las tres anteriores.

El paradigma de programación estructurada aporta una serie de ventajas en el ámbito del desarrollo y diseño de software:

Los programas son mucho más sencillos de entender: desaparece la necesidad de rastrear los complejos saltos de líneas (desaparecen los Goto)

Los programas siguen una estructura mucho más clara. Ahora las sentencias están ligadas y relacionadas entre si

Se optimiza la fase de prueba y depuración de los programas. Se facilita en gran medida el seguimiento de los fallos y errores

Se reduce el coste de mantenimiento de software, puesto que pasa a ser mucho más fácil de modificar

Podemos crear software mucho más rápido y por lo tanto a menor coste

Programación procedimental

El paradigma de programación procedimental se deriva directamente del de programación estructurada, y surge de forma natural tras el teorema de la programación estructurada. Este se basa en un concepto que actualmente es algo indispensable en el desarrollo de software: la “llamada a procedimientos”.

Aquí se introduce el concepto de procedimiento (o lo que coloquialmente conocemos como “función”): Tipo de rutina o subrutina que contiene una serie de pasos computacionales a realizar.

Cualquiera de estos procedimientos puede ser llamado en cualquier momento durante la ejecución del programa, lo que aumenta el grado de reutilización del código, reduce los tiempos de desarrollo, simplifica la legibilidad y la longitud de los programas.

Este paradigma se vuelve tan significativo que incluso los procesadores empiezan a proporcionar soporte hardware para su uso a través de un registro de pila e instrucciones para realizar procedimientos de llamada, permitiendo almacenar prácticamente sin penalización el punto de retorno de la llamada en cualquier momento.

La aparición de estos procedimientos da lugar a un nuevo concepto dentro de las variables a utilizar:

Por un lado, las variables locales son aquellas que solo existen en el contexto de un procedimiento. Se crean dentro del propio procedimiento y se borran una vez que este finaliza

Por otro lado, las variables globales son aquellas que no están ligadas a un procedimiento concreto. Su ciclo de vida no tiene por qué ser el mismo que el de todo el programa, sino que se puede crear, modificar y eliminar en cualquier punto de la ejecución sin depender del contexto de un procedimiento

Programación orientada a objetos

La programación orientada a objetos se basa en organizar el diseño de software en torno a datos u objetos, en lugar de funciones y lógica. Un objeto se define como un campo de datos que tiene atributos y comportamientos únicos

Este paradigma se centra en el objeto y en sus datos antes que en la lógica para su manipulación. Se trata de un enfoque muy adecuado para programas grandes, complejos y que se tengan que actualizar y mantener de forma activa. Además, es muy beneficioso para el desarrollo colaborativo ya que permite un alto nivel de modularización del software, facilitando el proceso de división de tareas.

Los principios en los que se basa la programación orientada a objetos son:

Encapsulación: implementación dentro de cada objeto. Otros objetos no tienen acceso o autoridad, pero pueden llamar a métodos públicos (seguridad)

Abstracción: Solo se muestran los mecanismos internos de los objetos que son relevantes para su manipulación

Herencia: Reutilización

Polimorfismo: Los objetos pueden adoptar más de una “forma” según el contexto. El programa determina el significado o uso para cada ejecución de ese objeto

### Lesson 4 - Programación declarativa

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/aTVyUuN7mBjsfN84UHrlLKSVEfhVHzJb</sub>

Programación declarativa

En contraposición al paradigma de programación imperativa visto en el punto anterior, el paradigma de programación declarativa se basa en describir que solución queremos en nuestro programa mediante condiciones, proposiciones, afirmaciones o transformaciones, pero no especificamos en ningún momento cuales son los pasos necesarios para encontrar la solución. Esto permite evitar posibles efectos secundarios de las funciones que estamos desarrollando. Normalmente definimos como programación declarativa como cualquier estilo que no sea imperativo. Vamos a ilustrarlo con un ejemplo sencillo en JavaScript:

En programación imperativa:

Imagen 3 Ejemplo básico de programación imperativa

Mientras que en programación declarativa:

Imagen 4 Ejemplo básico de programación declarativa

Como podemos ver, utilizando el paradigma de programación imperativa debemos definir paso a paso todo el procedimiento que deseamos realizar. Esto nos obliga a trabajar más a bajo nivel dentro del propio lenguaje, y podemos afectar a los datos con los que estamos trabajando. En contraposición el ejemplo de programación declarativa muestra como el desarrollador simplemente describe como quiere el resultado, y es el lenguaje/framework/librería quien se encarga de proporcionar dicho resultad.

Debemos notar que los dos paradigmas no son excluyentes entre sí. De hecho, muchas veces tendremos que desarrollar múltiples procedimientos utilizando programación imperativa para luego hacer uso del paradigma de programación declarativa.

Este modelo de programación:

Nos permite disponer de un alto nivel de abstracción, permitiendo representar programas complejos de manera comprimida, puesto que, a más extensa es la ejecución, más complejo suele ser su flujo de control.

Permite llevar a cabo optimizaciones y mejoras de software sin necesidad de modificar el algoritmo. Solo necesitamos sustituir los procedimientos a los que se accede (ejemplo: Cambiar un método de ordenación por otro que sabemos que está más optimizado)

El desarrollo es muy rápido, por lo que es perfecto para prototipado en métodos agiles de desarrollo

Existen múltiples lenguajes que implementan únicamente el paradigma de programación declarativa:

HTML/CSS

SQL

Haskell

Prolog

Todos estos lenguajes tienen en común que no nos permiten definir cómo se va a obtener el resultado, solo describimos cual es el resultado que queremos y existe una implementación ajena al desarrollador que lleva a cabo este trabajo. Por ejemplo:

En una query de SQL indicamos que elementos queremos obtener o insertar, y la implementación de SQL se encarga de llevar a cabo ese proceso.

En las páginas web en HTML, describimos que elementos queremos y cuál va a ser su aspecto, pero en ningún momento tenemos que encargarnos del proceso de renderizado de los pixeles en el navegador.

Dentro de la programación declarativa existen múltiples paradigmas, como son el Paradigma de programación funcional y el Paradigma de programación reactiva

Programación funcional

El paradigma de programación funcional deriva de la programación procedimental, y busca trabajar directamente con funciones y procedimientos, utilizándolas como si se trataran de cualquier otra entidad dentro del lenguaje. Este paradigma lo veremos en profundidad en el apartado 3 de esta unidad.

Programación reactiva

El paradigma de programación reactiva se enfoca en el trabajo con flujos de datos de manera asíncrona. El objetivo es que los datos se propaguen produciendo los cambios que sean necesarios en el estado del software. Los distintos modulos de software que tengamos en nuestro programa “reaccionan” a los datos, ejecutando una serie de eventos cuando estos se reciben. Veamos un ejemplo

En un paradigma imperativo:

while(!exit){
    if(checkDataReceive()){
        receiveData();
    }
}

Tenemos siempre la CPU en uso, comprobando continuamente si se han recibido nuevos datos. Si se han recibido se lleva a cabo un procedimiento, pero si no el programa sigue comprobando continuamente hasta que reciba información

El paradigma de programación reactiva sin embargo se basa en un patrón de diseño muy conocido, el patrón Observer:

Imagen 5 Diagrama del patrón Observer

Esto nos permite liberar la CPU, de forma que solo esté ocupado cuando un módulo de software ha sido notificado con algún dato. En caso contrario no tiene que hacer ninguna comprobación. Simplemente espera a recibir nueva información.

Este método hace que los nuevos datos se notifiquen directamente a los clientes, en lugar de tener que solicitarlos. El cliente se libera para realizar otras tareas mientras espera estas notificaciones, lo que hace que se invierta el diseño tradicional del procesamiento de entrada y salida.

Si esto lo sumamos a la programación asíncrona disminuimos drásticamente el uso ineficiente de recursos, permitiendo que se utilicen por otros procesos o componentes del software.

El uso de la programación reactiva permite que los sistemas sean:

Responsivos: Aseguran la calidad del servicio cumpliendo unos tiempos de respuesta establecidos. En caso de problemas de rendimiento son muy fáciles de detectar

Resilientes: Se mantienen responsivos incluso en situaciones de error

Elásticos: Se mantienen responsivos incluso ante aumentos de carga de trabajo

Orientados a mensajes: minimizan el acoplamiento entre componentes al establecer interacciones basadas en el intercambio de mensajes de manera asíncrona

### Lesson 5 - Programación multiparadigma

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/Yvx9wFuetxsUPvOu3WCAwLqkpnRCNMgy</sub>

Programación multiparadigma

La gran mayoría de lenguajes de programación que modernos implementan más de un paradigma. Esto permite una gran flexibilidad a la hora de implementar nuestro software, pudiendo elegir un paradigma u otro según el proyecto, o incluso combinar varios en el mismo. Esto significa que la decisión de utilizar un paradigma de programación u otro no viene determinado tanto por el lenguaje que estemos utilizando, sino por las decisiones del desarrollador a la hora de diseñar la arquitectura de software que se va a implementar.

Veamos una comparativa con las ventajas y desventajas de cada paradigma, así como sus ámbitos de aplicación:

Paradigma

Principios clave

Ventajas

Desventajas

Casos de uso habituales

Imperativo

Secuencia de instrucciones que modifican el estado del programa.

Control detallado, ejecución determinista, fácil de seguir para problemas simples.

Mayor riesgo de errores por efectos secundarios, menos expresivo en tareas de alto nivel.

Programas de sistemas, videojuegos, software con alta interacción con hardware.

Estructurado

Subparadigma del imperativo; uso de secuencias, condicionales y bucles en lugar de saltos incontrolados.

Código más claro y fácil de mantener, evita 'spaghetti code'.

Menos flexible para tareas muy específicas de bajo nivel.

Desarrollo de software de propósito general, algoritmos educativos.

Procedimental

Subparadigma del estructurado; divide el programa en procedimientos o funciones reutilizables.

Mayor reutilización de código, claridad y modularidad.

Dependencia de variables globales si no se estructura bien.

Aplicaciones científicas, scripts utilitarios, herramientas de línea de comandos.

Orientado a objetos

Organiza el software en torno a objetos con datos y comportamientos.

Modularidad, reutilización (herencia), encapsulación, polimorfismo.

Curva de aprendizaje, riesgo de incremento de la complejidad.

Aplicaciones empresariales, videojuegos, sistemas complejos y colaborativos.

Declarativo

Describe el 'qué' sin indicar el 'cómo'.

Mayor abstracción, menor cantidad de código, facilidad para cambios de implementación.

Menor control sobre el flujo, dependencia de optimizaciones internas.

Consultas a bases de datos, interfaces web, reglas de negocio.

Funcional

Funciones puras, inmutabilidad, composición de funciones.

Código más predecible, fácil de testear, ideal para paralelismo.

Curva de aprendizaje inicial, a veces menos eficiente en memoria.

Procesamiento de datos, algoritmos matemáticos, programación concurrente.

Reactivo

Procesamiento asíncrono basado en flujos de datos y propagación de eventos; patrón Observer

Escalabilidad, respuesta en tiempo real, bajo acoplamiento, buen manejo de E/S y concurrencia.

Complejidad conceptual (asíncronía, errores), depuración más difícil, curva de aprendizaje.

Interfaces reactivas, streaming de datos, sistemas event-driven, IoT, notificaciones y tiempo real.

Multiparadigma

Combina características de varios paradigmas.

Flexibilidad, adaptabilidad, aprovecha ventajas de cada enfoque.

Riesgo de mezcla incoherente de estilos si no hay disciplina.

Aplicaciones complejas que requieren diferentes enfoques en distintas capas.

Completa la siguiente tabla indicando que paradigmas de programación crees que puede implementar cada lenguaje

Lenguaje

Paradigmas que implementa

C

Java

C++

Python

Javascript

SQL

CSS

HTML

Resultado
Explicación

### Lesson 6 - Aplicaciones prácticas y tendencias futuras

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/Riubn64KhKZWluZk-EfHQYGne0KHVSR2</sub>

Aplicaciones prácticas y tendencias futuras

El conocimiento sobre paradigmas de programación no es únicamente teórico: tiene un impacto directo en el desarrollo de proyectos reales. Por ejemplo:

Procesamiento de datos: el paradigma funcional es muy útil para transformar y filtrar grandes volúmenes de información de forma concisa y paralelizable.

Desarrollo web: el paradigma declarativo es fundamental en la definición de interfaces y estilos (HTML, CSS) y en frameworks reactivos que describen el estado deseado de la UI.

Automatización de tareas: el paradigma imperativo es práctico cuando se requiere un control detallado sobre cada paso del proceso.

Aplicaciones híbridas: Python permite, en un mismo proyecto, utilizar programación orientada a objetos para la estructura general, imperativa para el control de flujo, y funcional para operaciones sobre colecciones de datos.

Un ejemplo ilustrativo podría ser un sistema de comercio electrónico:

Declarativo para definir la interfaz y las consultas de base de datos.

Imperativo para gestionar la lógica de negocio paso a paso.

Funcional para filtrar y transformar datos de productos y pedidos.

Tendencias futuras

La evolución del desarrollo de software apunta hacia un crecimiento de los lenguajes y entornos multiparadigma, ya que la complejidad de los sistemas modernos exige soluciones flexibles. Algunas tendencias destacables son:

Mayor integración de la programación funcional en lenguajes tradicionalmente imperativos (como Java, Python o C#), impulsada por la necesidad de paralelismo y programación reactiva.

Orientación a datos y flujos: la popularidad de arquitecturas reactivas y sistemas distribuidos favorece el uso de paradigmas declarativos y funcionales.

Herramientas inteligentes y generación automática de código: los paradigmas podrían adaptarse dinámicamente según el problema, combinando instrucciones imperativas con descripciones declarativas optimizadas por IA.

Enfoque en mantenibilidad y escalabilidad: la modularidad y la reducción de efectos secundarios (principios funcionales) serán cada vez más valorados en equipos grandes y proyectos a largo plazo.

En definitiva, conocer a fondo los paradigmas de programación no solo facilita el desarrollo actual, sino que prepara al programador para adaptarse a las herramientas y enfoques que marcarán el futuro del software.

¡Fantástico! Has completado este apartado.

### Lesson 7 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/eIP91XNYB-mLFYOtHYhQ0O2QLjWx64wT</sub>

Introducción

Tras haber visto los distintos paradigmas de programación que existen en la actualidad, vamos a preparar nuestro entorno de desarrollo. En este caso trabajaremos con Python, el cual es un lenguaje multiparadigma que nos permite una gran flexibilidad a la hora de desarrollar software. Python es un lenguaje de programación interpretado, es decir, un lenguaje de programación que no se compila para poder ejecutar las instrucciones en el propio lenguaje de la máquina, sino que debe existir un software instalado en el equipo que interprete las instrucciones de nuestro programa y las traduzca en tiempo real.

A lo largo de este apartado veremos como instalar correctamente el intérprete de Python, los complementos necesario de VSCode y el uso de entornos virtuales

Existen múltiples versiones de Python y de sus librerías. Esto sumado a la gran cantidad de dependencias que genera cualquier proyecto desarrollado en este lenguaje hace necesario un sistema de compartimentado y modularización de los paquetes que vamos a utilizar. Ahí es donde entran lo entornos virtuales, los cuales aprenderemos a utilizar y gestionar adecuadamente

### Lesson 8 - Instalación del entorno de trabajo

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/TBSCu05ISUMhzn_SE7nCV_-Wm8agLtk_</sub>

Instalación del entorno de trabajo

A lo largo de la asignatura vamos a trabajar con Python. Para ello debemos instalar en interprete desde su web o repositorio oficial. Podemos trabajar con cualquier versión igual o superior a la 3.9. En todo momento consideraremos que estamos en un entorno Windows, aunque no debería haber problema en trabajar en cualquier otro sistema operativo. Cuando instalemos el intérprete debemos asegurarnos de incluir las librerías tcl/tk, como vemos en la imagen:

Imagen 6 Ventana de instalación de Python en Windows

También utilizaremos Visual Studio Code, donde tendremos que instalar las extensiones “Python” y “Jupyter”:

1 de 2

Imagen 7 Extensión de Python para VSCode

Finalmente, en Windows 10 y 11 se encuentra desactivada la capacidad de ejecutar scripts sin firmar de Powershell. Esta característica va a ser muy recomendable para trabajar con entornos de Python, por lo que la activaremos modificando las políticas de privacidad. Para ello debemos abrir una terminal de Powershell como administrador y ejecutar el comando:

Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

### Lesson 9 - Entornos virtuales

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/nQ8rxb0hIbSfJc4fZSP5xUympPFRt2iz</sub>

Entornos virtuales

Como hemos visto, podemos disponer de múltiples paquetes en nuestra interprete de Python, lo que puede crear inconsistencias entre las diferentes versiones que utilizamos.

Por ejemplo: Imagina que tenemos un programa escrito en Python que necesita la versión 1.2.3 de la librería requests. Sin embargo, otro programa requiere una versión >= 2.0.0. Solo podemos disponer de una versión, por lo que uno de nuestros programas no podría funcionar.

Este es un ejemplo muy básico, fácilmente solucionable cambiando la versión en cada momento, sin embargo, un programa en Python habitualmente tiene cientos de dependencias, por lo que es inviable gestionar las versiones.

Los entornos virtuales en Python vienen a solucionar este problema, permitiendo disponer de un entorno aislado para cada programa o proyecto que deseemos, de forma que las dependencias y librerías de un programa no interfieran en ningún momento con las de otros. La herramienta utilizada habitualmente es venv. La mayoría de los gestores de entornos virtuales actuales (Como Anaconda o Miniforge) dependen de la herramienta venv.

Para crear un nuevo entorno virtual ejecutaremos:

python -m venv nombre_del_entorno

Esto nos creará un directorio con el nombre que hayamos asignado. Este contendrá todos los archivos necesarios del entorno virtual. Estos archivos no son más que una copia de la instalación de Python que tengamos en nuestro equipo, de manera que se encuentra totalmente aislada.

Para poder utilizar el entorno debemos activarlo. Para ello disponemos de varias opciones según el SO que estemos utilizando:

En Windows (CMD):

nombre_del_entorno\Scripts\activate

En PowerShell:

nombre_del_entorno\Scripts\Activate.ps1

En macOS o Linux (bash/zsh):

source nombre_del_entorno/bin/activate

Por ejemplo, vamos a crear un entorno llamado venv:

python -m venv venv
source venv/Scripts/Activate.ps1

puedes probarlo en el entorno de prácticas que hemos preparado anteriormente

Una vez tenemos activado nuestro entorno virtual, podemos ejecutar el comando para instalar requests:

pip install requests

Y vemos que únicamente se instala en nuestro entorno virtual, pero no existe en nuestra instalación de Python

Imagen 11 Detalle de instalación del paquete "requests"

Ahora, cada vez que intentemos ejecutar en Visual Studio Code un script de Python nos preguntará por el entorno virtual que queremos utilizar.

En el siguiente video podemos ver paso a paso como crear y utilizar un entorno virtual en Python:

Reproducir Vídeo
¡Fantástico! Has completado este apartado.

### Lesson 10 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/QcR7h98Wyi0YL2iXw8AzCv77cCWdlboK</sub>

Introducción

El paradigma de programación funcional es uno de los paradigmas más influyentes en el desarrollo de software, ya que soluciona grandes problemas que surgen del enfoque de la programación imperativa tradicional. En lugar de centrarse en cómo resolver una tarea paso a paso, este paradigma se enfoca en qué resultado se desea obtener, apoyándose en conceptos como las funciones puras y la inmutabilidad de los datos. Aunque no todos los lenguajes de programación están diseñados para trabajar exclusivamente bajo este enfoque, muchos incorporan elementos funcionales que pueden aprovecharse para escribir código más claro, conciso y fácil de mantener. Python es un ejemplo de lenguaje multiparadigma en el que, sin ser la programación funcional su eje principal, es posible aplicar varios de sus principios.

En este apartado veremos en detalle en que se basa el paradigma de programación funcional, y veremos los distintos mecanismos funcionales existentes en Python para aprovecharlos de manera adecuada

### Lesson 11 - Paradigma de programación funcional

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/es_-TbDyRBTQ8X5WVd_eNZdLPMDH9hyj</sub>

Paradigma de programación funcional

El paradigma de programación funcional se basa en la evaluación de funciones puras y en la inmutabilidad de los datos como método principal de computación, inspirándose en los principios de la matemática funcional. En Python no juega un papel fundamental, pero podemos sacar provecho de este paradigma en muchas situaciones. Definamos algunos términos:

Función pura: Función que siempre devuelve el mismo resultado si recibe los mismos argumentos. Esto significa que su valor de salida se deriva únicamente de sus valores de entrada. Además, no tiene efectos secundarios (ejemplo: No modifica variables globales, no escribe datos en disco, …)

Inmutabilidad de datos: Los datos no se modifican, si es necesario modificar información se crea una nueva estructura con esos cambios. Esta característica simplifica las tareas concurrentes y la depuración de software

La programación funcional consiste enteramente en la evaluación de funciones puras, lo que hace que exista mucha recursividad y llamadas de funciones anidadas. El uso de este tipo de funciones hace que no exista modificación de los datos como si ocurre en los paradigmas de programación imperativa.

Este paradigma nos ofrece múltiples ventajas:

Lenguaje de alto nivel: Se describe el resultado que se desea, en ligar de indicar los pasos necesarios para llegar a ese resultado. Se utilizan sentencias simples, pero que implican una alta carga computacional

Transparencia: El comportamiento de una función pura depende únicamente de sus entradas y salidas, sin que afecte en ningún caso a valores intermedios y sin que las salidas se vean afectadas por estos. Desaparecen los posibles efectos secundarios y se facilita la depuración y el mantenimiento del software

Alto nivel de paralelización: Como las rutinas no causan ningún tipo de efecto secundario ni dependen de datos que no se reciban como argumento, es mucho más fácil que puedan ser ejecutadas de manera concurrente

La mayoría de lenguajes de programación admiten cierto nivel de programación funcional. Existen otros lenguajes donde prácticamente todo el código sigue el paradigma funcional (Haskell, Clojure, …). Python soporta múltiples paradigmas de programación, entre ellos la programación funcional, sin ser este su principal aplicación. Sin embargo, por simplicidad y coherencia con el resto de la asignatura, explotaremos en la medida de lo posible las características funcionales de Python, que serán aplicables a cualquiera de los otros lenguajes más específicos.

Programación funcional en Python

Para soportar el paradigma de programación funcional, una función de un determinado lenguaje debe cumplir dos características fundamentales:

Debe poder recibir una función como argumento

Debe poder devolver una función a quien haya hecho la llamada

En Python TODAS las entidades se encapsulan dentro de una estructura de datos que se pueden modificar mediante sus propios métodos, es decir, se tratan como un objeto. Esto significa que si definimos una primitiva (int, float, bool, …) se creará un nuevo objeto. Esto se extiende también a las funciones: Todas las funciones definidas se encapsulan dentro de un objeto de Python con un atributo que nos indica que ese objeto puede ser invocado o ejecutado. Esto implica que podemos tratar a las funciones como si fueran cualquier otro objeto, y por lo tanto trabajar con ellas como con cualquier otra variable

Por ejemplo, podemos asignar una función a una variable para, a continuación, utilizar esa variable de la misma forma que utilizaríamos la propia función:

def func():
	print("I am function func()!")

func()
another_name = func
another_name()

Si ejecutamos este bloque de código, vemos que ahora la función puede ser invocada desde “another_name”. Es decir, hemos creado un alias de la función. Sin embargo, si ahora probamos a imprimir el alias (ojo, sin invocarla con los paréntesis):

print(another_name)

vemos que sigue hacienda referencia al nombre inicial:

<function func at 0x0000019425632CA0>

Hagamos uso de la función como si fuera una variable:

def func():
	print("I am function func()!")

print("cat", func, 42)

Vemos que podemos utilizar nuestra función como cualquier otra variable. Incluso guardarla en una lista:

objects = ["cat", func, 42]

Si queremos acceder a ella lo hacemos como si accediésemos a cualquier otro elemento de la lista

myfunc = objects[1]
myfunc()

O directamente la podemos invocar desde la lista

objects[1]()

Incluso podemos incluirlo como clave o valor de un diccionario, de manera que podemos asociar funciones a valores específicos de una variable

d = {"cat": 1, func: 2, 42: 3}
print(d[func])

Callbacks

Un callback es una referencia una función que se proporciona como argumento a otra función o método, con el fin de que esta ultima la invoque en un momento determinado de su ejecución, normalmente como respuesta a un evento, al completar una operación o para delegar parte de su lógica. La función callback conserva el contexto y las variables accesibles en el momento de su definición (clausura), y su invocación queda bajo el control de la función receptora.

En otras palabras, un callback es una función que se pasa como argumento a otra función para que esta ultima la ejecute más tarde, normalmente cuando ocurra un evento o se complete una tarea. Esto se llama también Composición de funciones

def inner():
	print("I am function inner()!")
def outer(function):
	function()
outer(inner)

Hay que tener cuidado con esto. Si nos fijamos bien vemos que, cuando pasamos la función inner no estamos ejecutándola. Es decir, no le hemos puesto los “()”. La única forma que tenemos de ejecutar la función es con los paréntesis y pasándole los argumentos adecuados, como podemos ver que se hace en la llamada function()

Hagamos un pequeño ejercicio práctico. La función sorted de Python recibe como parámetro una lista y nos devuelve como resultado una nueva lista con todos los elementos ordenados

animals = ["ferret", "vole", "dog", "gecko"]
sorted_animals = sorted(animals)
print(sorted_animals)
# resultado: ['dog', 'ferret', 'gecko', 'vole']

Pero, ¿cuál es el criterio de ordenación? En este caso parece sencillo: es un orden alfabético. Sin embargo, no es del todo así. Esta ordenándolo numéricamente de menor a mayor, y como no vemos números utiliza los valores ASCII de los caracteres. Esto supone varios problemas. Por ejemplo, ¿Qué ocurre si una de las palabras empieza en mayúscula? Nuestro sistema fallaría porque el valor ASCII es superior al de cualquiera de las letras en minúscula.

Otra situación que se puede dar es ¿Qué ocurre si quiero otro criterio de ordenación? Para ello la función sorted recibe un argumento key. Esta key es una función que debe devolver un valor numérico, y dicho valor se utiliza como criterio para la ordenación:

animals = ["ferret", "vole", "dog", "gecko"]
sorted_animals = sorted(animals, key=len)
print(sorted_animals)
# resultado: ['dog', 'vole', 'gecko', 'ferret']

En este caso, la función len se aplica sobre cada uno de los elementos de la lista de manera individual, y el resultado obtenido es el valor utilizado para la ordenación. Si queremos que la ordenación se realice al revés (en este caso según la longitud de cada palabra de manera descendente), podemos utilizar el argumento reverse para indicarlo

animals = ["ferret", "vole", "dog", "gecko"]
sorted_animals = sorted(animals, key=len, reverse=True)
print(sorted_animals)
# resultado: ['ferret', 'gecko', 'vole', 'dog’]

Ahora vamos a realizar el ejercicio mencionado. La idea es implementar una pequeña función que podamos pasar como key a la función sorted y que nos devuelva la en orden descendente utilizando como criterio la longitud de cada palabra SIN utilizar en ningún caso el argumento reverse

animals = ["ferret", "vole", "dog", "gecko"]
sorted_animals = sorted(animals, key=<completar)
print(sorted_animals)

La solución es sencilla:

def reverse_len(s):
	return -len(s)
animals = ["ferret", "vole", "dog", "gecko"]
sorted_animals = sorted(animals, key=reverse_len)
print(sorted_animals)

Otra de las condiciones necesarias para que un lenguaje soporte el paradigma de programación funcional es la capacidad de devolver una en el retorno. Veamos un ejemplo:

def outer():
	def inner():
		print("I am function inner()!")
	# Function outer() returns function inner()
	return inner
function = outer()
function
function()
outer()()

Aquí vemos que la función outer define una función (lo que también nos sirve para ver que podemos crear funciones dentro de otras funciones). Esta función inner solo estará disponible en el contexto de la función outer. Una vez que esta finaliza, la función dejaría de existir. En este caso estamos devolviendo la función inner, y se guarda en la variable function. Por lo tanto, la función se mantiene accesible y puede seguir utilizándose. Se debe notar que, si queremos invocar directamente a la función inner, debemos hacerlo mediante “()()”. El primer par de paréntesis ejecuta la función outer. Esta devuelve la función inner que se ejecuta mediante el segundo par de paréntesis.

Cuidado, no debemos confundir el paso de una función como parámetro con el paso del resultado de una función como parámetro. Veámoslo en el siguiente ejemplo en C:

void printText(char* text){
	printf(“%s\n”, text);
}
char* helloText(){
	return “Hello World!”;
}
int main(){
	printText(helloText());
	return 0;
}

La llamada printText(helloText()) no implementa el paradigma de programación funcional, ya que primero se ejecuta helloText y el resultado se pasa como argumento a printText. Sería equivalente al siguiente bloque de código:

void printText(char* text){
	printf(“%s\n”, text);
}
char* helloText(){
	return “Hello World!”;
}
int main(){
	char* mText = helloText();
	printText(mText);
	return 0;
}

A continuación, vamos a realizar una serie de ejercicios sobre callbacks en Python:

Es bastante conocido que la edad de una mascota no es equivalente directamente a la edad de una persona, por lo que, con los conocimientos que hemos adquirido de programación funcional, vamos a implementar la función edad_de_mi_mascota que nos devuelva su edad en años humanos. Las equivalencias que utilizaremos son:

Perro: 1 año equivale a 7 años humanos

Gato: 1 año equivale a 5 años humanos

Pez: 1 año equivale a 12 años humanos

Vamos a crear una función principal edad_de_mi_mascota que reciba dos parámetros. Un numero entero que represente la edad de la mascota, y una función que convierta a la edad correspondiente de cada animal. Por lo tanto, crearemos una función que calcule la edad para cada tipo de mascota.

Solución

Ahora pasemos a un ejercicio más habitual: Vamos a implementar un callback aprovechando la librería requests. El objetivo será crear un programa que nos devuelva los resultados de búsqueda de una película. Para ello vamos a utilizar la API de OMDB. OMDB es una API gratuita que ha obtenido datos de IMDB sobre películas, y nos los ofrece a través de peticiones HTTP. Podemos acceder a ella mediante la web: https://www.omdbapi.com/
(se abre en una nueva pestaña)

Para poder utilizarla necesitamos registrarnos y obtener una API KEY. Para ello accedemos a la web y seleccionamos la sección adecuada:

Imagen 12 Acceso a API key en OMDB

Una vez dentro tendremos que registrarnos. Podemos hacerlo con nuestro correo de U-Tad. También indicaremos que vamos a utilizar la API para educación:

Imagen 13 Ventana de registro de OMDB

Nos llegará un email como el de la imagen con la API KEY, lo primero será activar nuestra clave, y a partir ahí podremos empezar a utilizarla

Imagen 14 Detalle del email de registro en OMDB

Realizaremos una llamada de prueba para ver qué datos nos devuelve, en este caso buscaremos la película “Interstellar”, con la URL http://www.omdbapi.com/?apikey=<API_KEY>&s=interstellar
(se abre en una nueva pestaña)
. El parámetro s lo utilizaremos para indicar que queremos realizar una búsqueda:

Imagen 15 Respuesta en formato JSON desde OMDB

Como podemos ver, nos devuelve un fichero json con todos los contenidos en la base de datos que contengan la palabra clave introducida.

Ahora veamos como obtener estos datos desde Python utilizando la librería requests. El primer paso es crear un entorno virtual y activarlo, como ya vimos en el apartado anterior

Una vez disponemos del entorno, lo activamos e instalamos la librería con

pip install requests

Ahora veamos un ejemplo de como utilizar la librería requests. Vamos a realizar una request GET a la API de OMDB

from requests import get

response = get("http://www.omdbapi.com/?apikey=API_KEYc&s=interstellar")
print(response.text)

recuerda sustituir API_KEY por la clave que obtuviste al registrarte en la web

Para confirmar que la request se realizó correctamente podemos acceder a la variable status code. Por ejemplo:

if response.status_code is 200:
    …
else:
    …

Si queremos acceder a los datos como si se tratase de un diccionario, podemos utilizar la librería json, incluida directamente en el estándar de Python

import json
data_dict = json.loads(response.content)
print(data_dict["Search"][0])

O llamar a la función correspondiente dentro de la respuesta:

print(response.json()["Search"][0])

Ahora que sabemos cómo realizar nuestra request, vamos a pasar al ejercicio:

Vamos a implementar una función llamada get_movie_data que debe realizar una petición a OMDB sobre un título de película o serie introducido por teclado. Si la petición se realiza correctamente y la película/serie existe, nos mostrará los resultados (Por ejemplo: Titulo – Año: URL_de_poster”). En cambio, si ocurre un error, nos debe mostrar el mensaje de error.

El ejercicio tiene una condición. La función get_movie_data no se encarga ni de tratar los datos recibidos, ni mostrar el resultado ni de mostrar el error. Utilizaremos un callback para, una vez realizada la request, se ejecute la acción que nosotros hayamos definido en otra función

Solución

Como podemos ver, la función get_movie_data está totalmente desacoplada de la funcionalidad. Podríamos utilizarla para cualquier otra tarea donde haya que realizar una petición get. De hecho, el nombre de la función deja de tener sentido. Tendríamos que cambiarlo a algo como:

def make_get_request(url, on_success, on_error):
    …

Ahora podemos utilizar esta función para realizar cualquier petición GET. Vamos a realizar una nueva modificación. Ahora queremos obtener la información de OMDB y, una vez la tenemos, descargarnos el poster asociado a la película. Para aprovechar correctamente la capacidad de los callbacks, la función get solo se debe invocar desde la función make_get_request que ya hemos creado.

Para guardar la imagen desde un conjunto de bytes, instalaremos la librería PIL con el comando:

pip install Pillow

Y lo usaremos con:

from PIL import Image
from io import BytesIO

img = Image.open(BytesIO(<Image_bytes>))

La solución pasa por crear nuevas funciones para tratar los datos. Primero crearemos una primera función para ejecutar cuando la request tenga éxito, que obtendrá la url del poster, y luego crearemos otra que recibirá los bytes del poster

Solución

Como vemos, mantenemos una sola función para hacer peticiones get, pero la invocamos dos veces. Hemos creado una función success_get_movie_func que, a partir de los datos de OMDB, obtiene la url del poster. Por otro lado, la función success_get_poster_func, a partir de los bytes devueltos a través de data, crea un nuevo objeto Image y lo guarda en disco.

En el siguiente video se analiza el ejercicio corregido:

Reproducir Vídeo

Funciones anónimas

El paradigma de programación funcional se basa en llamar y pasar funciones como argumento, lo que suele implicar definir muchas funciones dentro de nuestro programa, llegando muchas veces a tener una gran cantidad de funciones muy cortas que realizan tareas que se invocan pocas veces (a veces solo una) en nuestro programa.

Aquí es donde entran la funciones anónimas o funciones lambda. En lugar de definir las funciones de manera habitual (utilizando la palabra reservada def, podemos definir las funciones de manera anónima, es decir, sin un nombre definido, y sobre la marcha. Una función lambda sigue la estructura:

lambda <parameter_list>: <expression>

por ejemplo:

lambda s: s[::-1]

al igual que el resto de funciones, las funciones lambda también se tratan como objectos dentro de Python, cosa que podemos ver si tratamos de imprimir la función. Así que, ¿Cómo podemos identificar que objectos son funciones y, por lo tanto, pueden ser invocados? Para eso existe la función callable:

callable(lambda s: s[::-1])

Que nos devuelve True si su argumento es algo a lo que se puede invocar

Como una función lambda es una función más dentro de Python, y se trata y gestiona de la misma forma que el resto de objetos y entidades, podemos guardarla para más adelante dándole un alias:

reverse = lambda s: s[::-1]
reverse("I am a string")
#Output: ‘gnirts a ma I’

Esto es equivalente a definir una función reverse mediante un método tradicional:

def reverse(s):
	return s[::-1]

reverse("I am a string")
reverse = lambda s: s[::-1]
reverse("I am a string")
#Output: ‘gnirts a ma I

Sin embargo, una función lambda no tiene por que asignarse a una variable, y está pensada para que se pueda utilizar de forma directa

(lambda s: s[::-1])("I am a string")

Incluso puede recibir múltiples parámetros

(lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6)
(lambda x1, x2, x3: (x1 + x2 + x3) / 3)(1.4, 1.1, 0.5)

Sin embargo, están limitadas a una única expresión, por lo que no podremos aplicarlas en un caso complejo como el que hemos visto anteriormente

El siguiente video muestra en detalle cómo utilizar una función lambda:

Reproducir Vídeo

Operadores funcionales. Operador map()

En Python tenemos una serie de operadores que nos permiten aprovechar al máximo las capacidades de programación funciona que tiene el lenguaje. Uno de ellos es el operador map

El operador map es una función integrada en Python que se aplica sobre un iterable (ej.: Lista). El operador aplica una función especificada por nosotros sobre cada elemento del iterable, y nos devolverá un iterador con los resultados. El operador map se utiliza para sustituir el uso de un bucle for o while explicito. La estructura del operador es:

map(<f>, <iterable>)

Y devuelve un iterador que produce el resultado de aplicar la función <f> sobre cada elemento dentro de <iterable>

Veamos un ejemplo sobre como utilizarlo: Supongamos que hemos definido la función reverse, que recibe un string y lo invierte:

def reverse(s):
	return s[::-1]

reverse("I am a string")

Si tenemos una lista de strings, podemos utilizar map para aplicar la función reverse sobre cada uno de los elementos que hay en la lista

animals = ["cat", "dog", "hedgehog", "gecko"]
iterator = map(reverse, animals)
print(iterator)

Si nos fijamos en la salida, map no nos devuelve directamente una lista con el resultado, sino un iterador del tipo map object. Para poder obtener todos los elementos del iterador tenemos varias opciones:

Recorrer el iterador:

iterator = map(reverse, animals)
for i in iterator:
    print(i)

Convertir en una lista:

iterator = map(reverse, animals)
print(list(iterator))

Dado que estamos trabajando con funciones sencillas, podemos reducirlo utilizando funciones lambda

animals = ["cat", "dog", "hedgehog", "gecko"]
iterator = map(lambda s: s[::-1], animals)
list(iterator)

Y como Python nos permite hacer muchas agrupaciones:

list(map(lambda s: s[::-1], ["cat", "dog", "hedgehog", "gecko"]))

Veamos un ejemplo práctico: La función str.join nos permite concatenar un string con otro, o con una lista de strings. Si le pasamos una lista nos concatenará todos ellos, dejando el valor almacenado en str entre cada uno:

print("+".join(["cat", "dog", "hedgehog", "gecko"]))
#Output: 'cat+dog+hedgehog+gecko'

Hasta aquí parece sencillo de utilizar, pero si queremos hacer lo mismo sobre una lista de números tenemos un problema:

print("+".join([1, 2, 3, 4, 5]))
#Output: Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sequence item 0: expected str instance, int found

Estamos intentando concatenar strings con números enteros, y la función nos arroja un error¿Como podemos solucionar este problema con map?

print("+".join(map(str, [1, 2, 3, 4, 5])))
#Output: ‘1+2+3+4+5’

Podemos utilizar la función map para convertir todos los elementos que hay dentro de la lista de números a string. De esta manera evitamos que haya un error y la función realizará la tarea de concatenar adecuadamente

Hasta este punto hemos visto el uso del operador map con un solo iterable, pero, podemos utilizarlo con multiples iterables:

map(<f>, <iterable₁>, <iterable₂>, ..., <iterableₙ>)

La función se aplicará sobre todos los elementos de cada iterable en paralelo, y devuelve un iterador que recorre el resultado final. Para poder utilizar esta característica, el numero de iterables que queramos pasar como argumento debe coincidir con el número de argumentos de la función que se va a aplicar. Veamos un ejemplo para ilustrarlo:

def f(a, b, c):
	return a + b + c
print(list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300])))
#Output: [111, 222, 333]

El operador map aplica la función f sobre el índice correspondiente de cada iterable. Si nuestros iterables fueran A, B y C, el resultado se obtendría sumando A[0] + B[0] + C[0], A[1] + B[1] + C[1], A[2] + B[2] + C[2]. A continuación, podemos ver una imagen que ilustra mejor su funcionamiento:

Imagen 16 Funcionamiento del operador "map" con multiples iterables

Vamos a realizar una serie de ejercicios haciendo uso del operador map:

Escribir un programa que triplique todos los elementos de una lista de enteros

Escribir un programa que imprima por pantalla todos los elementos de una lista de strings

Escribir un programa que convierta los caracteres de una lista a mayúsculas y a minúsculas, y elimine las letras duplicadas de una secuencia

Veamos las soluciones a los ejercicios:

1
2
3

Operadores funcionales. Operador filter ()

El operador filter funciona de manera muy similar al operador map, ya que aplica una función sobre todos los elementos de un iterable. Sin embargo, en este caso nos permite seleccionar o filtrar los elementos según el resultado obtenido en dicha función. En este caso la función devolverá siempre un booleano y filter nos devolverá todos aquellos elementos de la lista cuyo resultado al aplicar la función sea True

filter(<f>, <iterable>)

Por ejemplo:

def greater_than_100(x):
	return x > 100
list(filter(greater_than_100, [1, 111, 2, 222, 3, 333]))
#Output:[111,222,333]

Al igual que en casos anteriores, podemos implementar la misma funcionalidad utilizando una función lambda:

list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333]))
#Output: [111,222,333]

Al contrario de lo que ocurre con map, filter solo puede recibir un iterable como argumento.

Vamos a implementar algunos ejercicios aplicando la función filter

Escribir un programa que devuelva los números pares de una lista (utilizar range para definir la lista)

Escribir un programa que imprima por pantalla todas las palabras de una lista que estén escritas en MAYUSCULA (.isupper). ["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"]

Veamos las soluciones a los ejercicios:

1
2

Operadores funcionales. Operador reduce ()

Reduce funciona de manera similar a los dos operadores vistos anteriormente, pero en este caso aplica una función a los elementos de una lista por pares, combinándolos hasta obtener un resultado simple. Esta función no forma parte del core de Python, sino que tenemos que importarla desde la librería functools, la cual ya está instalada por defecto

from functools import reduce

Y la estructura de reduce es:

reduce(<f>, <iterable>)

donde se aplica la función <f> sobre cada dos elementos de <iterable>, combinándolos de manera progresiva

Veamos un ejemplo sencillo:

def f(x, y):
	return x + y

from functools import reduce
reduce(f, [1, 2, 3, 4, 5])
#Output: 15

Como hemos comentado, se aplica un proceso de reducción. En este caso el resultado será [(1+2)+(3+4)+5], como podemos ver en la ilustración:

Imagen 17 Funcionamiento de la función "reduce"

La función no define los tipos necesarios, así que no necesariamente tiene por qué resolver operaciones aritméticas:

def f(x, y):
	return x + y

from functools import reduce

reduce(f, ["cat", "dog", "hedgehog", "gecko"])
#Output: 'catdoghedgehoggecko'

Si quisiéramos espacios entre cada palabra podíamos hacerlo con map:

def f(x, y):
	return x + y

from functools import reduce

lista = ["cat", "dog", "hedgehog", "gecko"]
spaced_list = map(lambda s: s + " ", lista)

reduce(f, spaced_list)
#Output: 'cat dog hedgehog gecko '

VAMOS A IMPLEMENTAR UN PEQUEÑO EJERCICIO UTILIZANDO EL OPERADOR REDUCE

1.       Implementar una función que, mediante el uso del operador reduce, calcule el valor máximo de una lista

Veamos la solución al ejercicio:

A continuación podemos ver un resumen de los 3 operadores:

Reproducir Vídeo
¡Fantástico! Has completado este apartado.

### Lesson 12 - Conclusiones de la unidad

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/TGinRZfzPtW4nRyAdfUTDXOuavgYicSo</sub>

Conclusiones de la unidad

A lo largo de esta unidad hemos visto los distintos paradigmas de programación que forman la base del desarrollo de software moderno. Se han analizado los paradigmas imperativo, declarativo, reactivo, orientado a objetos, funcional y multiparadigma, identificando sus principios, características y ámbitos de aplicación, así como sus ventajas y limitaciones en diferentes contextos. Este conocimiento nos permitirá agilizar la toma de decisiones fundamentadas a la hora de abordar un proyecto, escogiendo el enfoque más adecuado o combinando varios para obtener soluciones más eficaces.

El estudio de la programación imperativa nos muestra la necesidad de definir instrucciones secuenciales claras, así como la relevancia de subparadigmas como la programación estructurada, procedimental y orientada a objetos. Por su parte, el paradigma declarativo nos ha permitido comprender el valor de centrarse en saber describir nuestros resultados, más allá que el proceso de desarrollo, favoreciendo un alto nivel de abstracción y la posibilidad de optimizar y adaptar el software sin modificar su lógica principal.

Dada la naturaleza de esta asignatura, hemos realizado una introducción y repaso de Python que han servido para reforzar conceptos clave del lenguaje y poner en valor su carácter multiparadigma y sus capacidades para la programación estructurada, orientada a objetos y funcional. Además, hemos indagado en la creación y uso de entornos virtuales, proporcionando herramientas esenciales para garantizar entornos de desarrollo aislados, consistentes y fáciles de reproducir, mejorando la calidad y la estabilidad de los proyectos.

También nos hemos analizado en profundidad el paradigma funcional, que promueve el uso de funciones puras, la inmutabilidad de los datos y la composición de funciones (callbacks) para lograr un código más predecible, modular y fácil de mantener. El uso de Python como lenguaje de estudio ha permitido ejemplificar la implementación de este paradigma a través de funciones como callbacks, funciones anónimas (lambda) y operadores funcionales (map, filter, reduce), todo ello en un contexto práctico y aplicable a problemas reales.

En conjunto, los contenidos de la unidad dotan al alumno de una visión más amplia y flexible del desarrollo de software, en la que vemos que no existe un único enfoque correcto, sino que la elección del paradigma y las técnicas de programación dependerán de la naturaleza del problema a resolver, las restricciones del proyecto y las características del lenguaje empleado. Este conocimiento, unido a la práctica adquirida, constituye una base sólida para abordar retos de programación más complejos y avanzar hacia modelos de desarrollo más eficientes y escalables.

¡Felicidades! Has finalizado la unidad. Y ahora, ¡a por las prácticas!


## Recursos y enlaces

- [CONTINUAR CURSO](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/WC5N7v4_XJ0OTfAci5aMPMNbTOk0hmbV)
- [IMG](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/assets/Q2w5wIITym-sffux.png)
- [Introducción](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/I1lyHm-uskytA7A6Jdy49tsYS0RBpWJV)
- [Programación imperativa](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/ZwVJdEJRA5eYQM7mlOA8Blys6QxXj6zB)
- [Programación declarativa](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/aTVyUuN7mBjsfN84UHrlLKSVEfhVHzJb)
- [Programación multiparadigma](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/Yvx9wFuetxsUPvOu3WCAwLqkpnRCNMgy)
- [Aplicaciones prácticas y tendencias futuras](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/Riubn64KhKZWluZk-EfHQYGne0KHVSR2)
- [Introducción](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/eIP91XNYB-mLFYOtHYhQ0O2QLjWx64wT)
- [Instalación del entorno de trabajo](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/TBSCu05ISUMhzn_SE7nCV_-Wm8agLtk_)
- [Entornos virtuales](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/nQ8rxb0hIbSfJc4fZSP5xUympPFRt2iz)
- [Introducción](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/QcR7h98Wyi0YL2iXw8AzCv77cCWdlboK)
- [Paradigma de programación funcional](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/es_-TbDyRBTQ8X5WVd_eNZdLPMDH9hyj)
- [Conclusiones de la unidad](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739661_1/scormcontent/index.html#/lessons/TGinRZfzPtW4nRyAdfUTDXOuavgYicSo)