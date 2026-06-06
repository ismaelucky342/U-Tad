# Unidad 1. Experiencia de Usuario e Interfaces de Usuario.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Introducción A La Experiencia De Usuario](#2-introducción-a-la-experiencia-de-usuario)
  - [2.1 Introducción](#21-introducción)
  - [2.2 ¿Por qué es necesario que un ingeniero informático sepa de experiencia de usuario?](#22-por-qué-es-necesario-que-un-ingeniero-informático-sepa-de-experiencia-de-usuario)
  - [2.3 Experiencia de Usuario e Interfaz de Usuario](#23-experiencia-de-usuario-e-interfaz-de-usuario)
  - [2.4 ¿A qué se debe el éxito del UX?](#24-a-qué-se-debe-el-éxito-del-ux)
  - [2.5 Breve historia del origen de UX](#25-breve-historia-del-origen-de-ux)
- [3. La Evolución De Los Interfaces Digitales](#3-la-evolución-de-los-interfaces-digitales)
  - [3.1 Introducción](#31-introducción)
  - [3.2 CLI, Command Line Interface](#32-cli-command-line-interface)
  - [3.3 GUI, Graphic User Interface](#33-gui-graphic-user-interface)
  - [3.4 NUI, Natural User Interface](#34-nui-natural-user-interface)
  - [3.5 OUI, Organic User Interface](#35-oui-organic-user-interface)
- [4. Usabilidad](#4-usabilidad)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Definición de usabilidad](#42-definición-de-usabilidad)
  - [4.3 Medición de la usabilidad](#43-medición-de-la-usabilidad)
  - [4.4 La curva de aprendizaje](#44-la-curva-de-aprendizaje)
- [5. Accesibilidad](#5-accesibilidad)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Definición de accesibilidad](#52-definición-de-accesibilidad)
  - [5.3 Actores y bases principales de la accesibilidad](#53-actores-y-bases-principales-de-la-accesibilidad)
  - [5.4 Principios de la accesibilidad](#54-principios-de-la-accesibilidad)
  - [5.5 Buenas prácticas en desarrollo web](#55-buenas-prácticas-en-desarrollo-web)
  - [5.6 Marco regulatorio de la accesibilidad](#56-marco-regulatorio-de-la-accesibilidad)
- [6. Conclusiones](#6-conclusiones)
  - [6.1 Conclusiones de la unidad](#61-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad de esta asignatura se sientan las bases de lo que es el concepto experiencia de usuario y se enfrenta a otro concepto próximo como es el de interfaz de usuario. Se recorre la historia de experiencia de usuario desde sus orígenes a mediados de la década de los 90 del siglo pasado y su importancia actual. Conoceremos la evolución de los interfaces desde CLI, Command Line Interface, hasta OUI, Organic User Interface, con un recorrido por los últimos 50 años en el mundo de la informática

También se profundiza en el concepto de usabilidad, tanto en su definición, como en las metodologías que tenemos actualmente para medir su grado de presencia en un sistema; metodologías como son los test de usuario o los análisis de expertos en los que la lista de 10 heurísticos de usabilidad creada por Jakob Nielsen es el documento de referencia

Se explica el valor que tiene trabajar con enfoque de experiencia de usuario para que los productos digitales sean exitosos y a la vez accesibles para el mayor número de personas y porqué los ingenieros deben tener muy presente estos conceptos en su formación y trabajo.

Los apartados a tratar en esta unidad didáctica serán:



- **Introducción a Experiencia de Usuario**  
  En este apartado empezaremos con una visión general de la definición de experiencia de usuario, las diferencias con otras disciplinas cercanas y las características que son importantes considerar a la hora de crear experiencias de usuario útiles y necesarias para las personas.
- **La evolución de los interfaces digitales**  
  Una vez que conocemos la definición de interfaz de usuario vamos a descubrir cómo ha sido su evolución en los diferentes productos digitales a lo largo de la historia de la informática.
- **Accesibilidad**  
  En este último apartado de la unidad vamos a ver que es muy importante que construyamos productos adaptados a todo tipo de usuarios independientemente de sus habilidades. La accesibilidad es un derecho de las personas y una responsabilidad social para las empresas ya que de ese modo están participando en que el mundo sea más equitativo e inclusivo.



#### Objetivos



1. Conocer los principios en los que se basa la experiencia de usuario.
2. Entender qué es el interfaz, cómo ha evolucionado y de qué forma ayuda al usuario en el producto.
3. Profundizar en el concepto de usabilidad y entender cómo se pueden medir.
4. Comprender las bases de la accesibilidad, su importancia y regulación legal, e incorporarlas como buena práctica en el desarrollo de software.



## 2. Introducción A La Experiencia De Usuario



### 2.1 Introducción



![image](assets/cm5qsqmcf004i35710b60u9a4-stock-image.jpg)



En este apartado empezaremos con una visión general de la definición de experiencia de usuario, las diferencias con otras disciplinas cercanas y las características que son importantes considerar a la hora de crear experiencias de usuario útiles y necesarias para las personas.



### 2.2 ¿Por qué es necesario que un ingeniero informático sepa de experiencia de usuario?



Quizá te estés preguntando por qué es necesario que un ingeniero tenga conocimientos de experiencia de usuario cuando a priori puede parecer una disciplina más cercana al arte, al diseño o al marketing y de la que los ingenieros no tienen que preocuparse ya que es un trabajo que nos viene hecho por otros departamentos. Es importante que sepas que cuando todos los participantes en la creación de un producto digital trabajan pensando en el usuario que utilizará el sistema, es más fácil que desarrollemos un software de calidad.

Vamos a ver algunos ejemplos de sistemas desarrollados sin un enfoque de experiencia de usuario y en los cuales comprobarás la importancia que tiene esta disciplina.

Observa la siguiente imagen:



![image](assets/cm5qstrz6008o3571dljy8x6v-Imagen1.jpg)



En este formulario podemos comprobar cómo se ha preferido colocar un elemento desplegable para algunos de los valores numéricos que tiene que introducir el usuario generando de esta forma un aumento exponencial del número de clics que se tienen que realizar. Sin conocer en profundidad este producto podríamos pensar que de este modo los ingenieros se aseguraban una mayor fiabilidad de los datos introducidos por el usuario, pero con un altísimo coste de tiempo y esfuerzo por parte de este.

**CONCLUSIÓN:** Con este ejemplo podemos aprender la importancia que tendrá poner en una balanza el trabajo que le pedimos al usuario y los condicionantes técnicos que necesitamos para de ese modo llegar a un equilibrio perfecto en el que ninguna de las dos partes se vea perjudicada.

Observa ahora esta otra imagen:



![image](assets/cm5qsvqg100a235719nbznkks-Imagen2.jpg)



Probablemente te estés preguntando cómo es posible que una disposición de elementos como los que muestra esta imagen haya llegado publicarse en un producto digital. ¿Se te ocurre la razón? Las razones pueden ser diversas. La más probable es que el equipo que desarrolló esta aplicación móvil no consideró que hay usuarios que tienen pantallas más estrechas que en las que ellos hicieron las pruebas y por eso una persona con un móvil quizá más antiguo, de una marca o fabricante minoritario o simplemente diferente no podría utilizar está app.

**CONCLUSIÓN:** Es importante considerar el máximo de casuísticas posibles, o por lo menos las más habituales, para de ese modo construir un diseño y una tecnología integradora que no excluya a ningún usuario. Hay que pensar que los usuarios pueden no disponer del mismo hardware que tenemos nosotros como creadores del producto digital.

Observa ahora la siguiente:



![image](assets/cm5qsxbof00bf35714k41wg5z-Imagen3.jpg)



Estamos demasiado acostumbrados a que los sistemas digitales nos hablen en un idioma diferente al que hablamos los humanos. Muchas veces traspasamos conceptos técnicos a los usuarios y les generamos dudas a la hora de utilizar el producto digital. Estas dudas en ocasiones desembocan en una mala imagen del producto o la empresa, en la búsqueda de otras alternativas e incluso en pérdida de ingresos cuando el producto es transaccional.

**CONCLUSIÓN:** Tenemos que entender el uso de un producto digital como una conversación entre un humano y una máquina y por eso hay que tratar de que esa conversación se produzca en el idioma que hablan las persona y no en el de las máquinas. Solo podremos crear una buena experiencia de usuario cuando la persona entienda lo que está pasando en la pantalla.

Espero que estos 3 ejemplos te hayan servido para ser más consciente de la importancia que tiene el crear software que no solo se ejecute con rapidez y eficiencia, sino que también esté orientado en las necesidades que tienen las personas. Solo teniendo en cuenta quién está detrás del dispositivo y entendiendo sus objetivos y contexto seremos capaces de hacer software útil, rentable y memorable.



### 2.3 Experiencia de Usuario e Interfaz de Usuario



El acrónimo más popular para referirnos a experiencia de usuario es el de UX que proviene de la expresión inglesa “user experience”. UX lo encontramos a menudo unido a las siglas UI, que también provienen del inglés y hacen referencia a la interfaz de usuario o “user interface”.

Antes de enunciar una definición académica sobre el concepto de experiencia de usuario vamos a ver qué características generales hay dentro de UX y cuáles dentro de UI.

En UX encontramos conceptos como la intuición, la facilidad de uso, la satisfacción, la navegación fácil o la accesibilidad, mientras que dentro de UI podemos encontrarnos otros como el aspecto, los colores de marca, la tipografía o las imágenes

A menudo se engloba la disciplina de experiencia de usuario dentro del mundo del diseño, pero vamos a ver que, aunque hay muchas personas que lo confunden UX no es solo diseño.

Para entender las diferencias entre experiencia de usuario e interfaz de usuario vamos a utilizar algunos ejemplos del mundo físico y que puedes ver en este vídeo.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_FUUX_A/content/_652060_1/scormcontent/assets/INSD_FUUX_U1_Apartado1_Video1.mp4?v=1)



Como habrás percibido en el vídeo estamos hablando de UX y de UI en sentido metafórico. El interfaz en un producto digital es la parte que permite al usuario su utilización. Es el puente entre el producto y la experiencia.

Una Interfaz de Usuario (UI) es un conjunto de elementos de hardware y software de un ordenador u otro sistema informático que presentan información al usuario y le permiten interactuar con la información y con el producto. Es decir, es la cara que presenta el ordenador y dentro de él cada aplicación software.

Desde el punto de vista del usuario, la interfaz es todo el sistema: es la parte que el usuario ve, oye, toca y con la que se comunica. Siendo todavía más genéricos podemos definir interfaz como el espacio por medio del cual se pueden comunicar las personas con las máquinas para que así los usuarios puedan operar y controlar a la máquina.

Una interfaz de usuario pobre origina problemas como la reducción de la productividad, el incremento del tiempo de aprendizaje o niveles de errores inaceptables. Desde un punto de vista más genérico decimos que un mal interfaz provoca al usuario un aumento de TIEMPO y ESFUERZO para resolver una tarea en un sistema digital.

Como veremos más adelante los interfaces están en constante evolución, pero estas son algunas de las principales funciones que tienen:

•          Puesta en marcha y apagado.

•          Control de las funciones manipulables del equipo.

•          Manipulación de archivos y directorios.

•          Herramientas de desarrollo de aplicaciones.

•          Comunicación con otros sistemas.

•          Información de estado.

•          Configuración de la propia interfaz y entorno.

•          Intercambio de datos entre aplicaciones.

•          Control de acceso.

•          Sistema de ayuda interactivo.

La definición más acertada de Experiencia de Usuario es la que la que afirma que UX es el conjunto de factores relativos a la interacción del usuario con un entorno o dispositivo concretos, cuyo resultado es la generación de una percepción de dicho servicio o producto. En esta definición de UX hay dos características importantes y únicas que son: la interacción (digital) y la percepción.

La experiencia de usuario busca comprender el contexto para mejorar la efectividad y es por ello por lo que el diseño de productos digitales orientados en las personas comienza desde la comprensión de la necesidad y el entorno, momento y estado en el que se encuentra el usuario.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_FUUX_A/content/_652060_1/scormcontent/assets/INSD_FUUX_U1_Apartado1_Video2.mp4?v=1)



Cuando diseñamos cualquier interfaz de usuario lo que estamos haciendo es modelar, delimitar y conducir la interacción del usuario determinando:

·         De qué opciones dispondrá el usuario en cada momento

·         Cómo responderá el producto a cada una de sus acciones.

Por esta razón el concepto central en la experiencia de usuario es precisamente el de la interacción.

Si atendemos al modelo propuesto por el psicólogo especializado en interacción digital, Donald Norman, en su libro “The Design of Everyday Things” (1988), podemos considerar la interacción como un proceso iterativo y cíclico divisible en 3 etapas principales y sus consiguientes sub-etapas:



1. - **Reconocimiento de la necesidad:** El usuario identifica un problema o una necesidad que desea satisfacer.
   - **Definición del objetivo:** El usuario establece un objetivo claro y específico que desea alcanzar.
2. - **Planificación de la acción:** El usuario desarrolla un plan para alcanzar el objetivo y considera las posibles acciones y sus consecuencias.
   - **Ejecución de la acción:** El usuario lleva a cabo las acciones planificadas para interactuar con el sistema.
3. - **Percepción del resultado:** El usuario observa el resultado de sus acciones y compara si se ajusta a sus expectativas.
   - **Interpretación de la ejecución:** Asigna un significado al resultado y evalúa si ha alcanzado su objetivo.
   - **Aprendizaje:** Actualiza su conocimiento sobre el sistema y ajusta sus futuras acciones en base a la experiencia adquirida.



El marco teórico propuesto por Norman para el estudio de la interacción humano-computadora (HCI o Human Computer Interaction) incluye la identificación de puntos de fricción en el proceso de interacción.

Estas 'brechas' son situaciones en las que las expectativas y acciones del usuario no se alinean con las respuestas del sistema, lo que puede generar dificultades en la comunicación y la consecución de los objetivos. Estas son:



- **Brecha de ejecución**  
  La brecha de ejecución es esa sensación de frustración que siente el usuario cuando una herramienta no responde a las necesidades concretas que tiene. Es como si hubiera un muro invisible entre lo que queremos hacer y lo que el sistema nos permite. Sabemos que un sistema permite hacer algo, pero no somos capaces de realizarlo.

  - **Ejemplo:** Un usuario quiere devolver un pedido en una tienda online pero no encuentra en la interfaz el lugar desde el que realizar esa acción.
- **Brecha de evaluación**  
  Se produce cuando el usuario no puede interpretar correctamente el estado del sistema o los resultados de sus acciones. una información insuficiente o ambigua proporcionada por el sistema, una representación visual poco intuitiva de los elementos de la interfaz o una falta de retroalimentación adecuada sobre las acciones del usuario. Esta brecha dificulta que el usuario comprenda si ha alcanzado sus objetivos y puede generar frustración y confusión.

  - **Ejemplo:** El usuario está comprando unas entradas para un concierto, ha introducido su tarjeta correctamente, pero no recibe notificación del pago por ningún canal y no sabe si realmente podrá asistir o no.



### 2.4 ¿A qué se debe el éxito del UX?



Durante los últimos 10 años la mayoría de las empresas de éxito a nivel mundial han ido adoptando metodologías de trabajo en experiencia de usuario a la hora de construir sus productos. Esta tendencia no es simplemente una moda, sino que tenemos algunas evidencias que nos indican la razón por la que tener en cuenta la experiencia de usuario repercute directamente en una mejora del producto.



- **Reduce los costes de los productos**  
  Las estadísticas han demostrado que existe una tasa de retorno de la inversión de entre 10 y 100 dólares por cada dólar que una empresa invierte en experiencia de usuario. Además, las inversiones en Experiencia de Usuario se mantienen y amortizan a largo plazo, a diferencia de los costes relacionados con la adquisición de una empresa.
- **La satisfacción de los clientes incrementa las ventas**  
  Ofrecer una buena experiencia de usuario reduce las solicitudes de asistencia al cliente y los esfuerzos de atención al cliente. Si el proceso es claro y limpio, con facilidades de pago, y con una experiencia fluida, solventando los puntos críticos, se aumentarán las ventas considerablemente
- **Fidelización del cliente**  
  Una buena experiencia de usuario hace que el usuario aumente su satisfacción y por tanto su fidelidad, convirtiéndose incluso en prescriptor de nuestra marca.
- **Producto competitivo y con menos riesgos**  
  Ofrecer una buena experiencia de usuario reduce las solicitudes de asistencia al cliente y los esfuerzos de atención al cliente. Si el proceso es claro y limpio, con facilidades de pago, y con una experiencia fluida, solventando los puntos críticos, se aumentarán las ventas considerablemente.
- **La productividad del equipo se aumenta**  
  Las prácticas de investigación de usuarios, creación de prototipos y estudios de usabilidad garantizan que el equipo de desarrollo tenga una idea clara de los resultados esperados en todo momento. Esto ayuda a reducir las iteraciones en el desarrollo y también a comprender los puntos de dolor de los usuarios. La reducción del tiempo de desarrollo está directamente relacionada con los beneficios monetarios y la rentabilidad.



### 2.5 Breve historia del origen de UX



El origen de la expresión Experiencia de Usuario es relativamente nuevo, aunque el concepto ha existido de forma implícita desde que las personas se relacionan con las máquinas. Su creador fue el reconocido psicólogo cognitivo y tecnólogo Donald Norman
(opens in a new tab)
 nacido en 1935 y que en la década de los años 90 del siglo pasado definió de forma concreta la experiencia de usuario.

 

En el año 1993 Donald Norman comienza a trabajar en Apple y denomina su puesto dentro de la compañía como “Arquitecto de Experiencia de Usuario” un título creado exclusivamente para él y considerado la primera vez en la historia que alguien tiene un trabajo con la denominación de Experiencia de Usuario.

 

Preguntado por el propósito de la creación del término Norman dijo: “Inventé el término porque pensé que interfaz y usabilidad eran demasiado limitados. Quise cubrir todos los aspectos de la experiencia de una persona con un sistema, incluyendo el diseño industrial, gráficos, la interfaz, la interacción física, y el manual”

Otra de las personas relevantes en el origen de la experiencia de usuario es Jakob Nielsen. Ingeniero y doctor especializado en diseño de interfaces nacido en Dinamarca en 1957 y que está considerado como el padre de la usabilidad. De Nielsen es el listado de validación de usabilidad de interfaces más popular y del que hablaremos más adelante.

 

Norman y Nielsen crearon en 1998 la empresa de consultoría Nielsen Norman Group
(opens in a new tab)
 (NN/g) especializada en mejorar la experiencia de usuario y generadora de una gran cantidad de artículos de investigación que son referencia en la profesión. Norman abandonó la consultora en 2019 aunque sigue siendo colaborador de contenidos y miembro de la junta directiva.

La tercera personalidad importante que es importante que conozcas es Steve Krugg
(opens in a new tab)
 (1950), un profesional de la usabilidad y la experiencia de usuario y escritor de uno de los manuales más populares de la historia sobre la disciplina.

 

Su libro “Don’t make me think” (No me hagas pensar), se publicó por primera vez en el año 2000, está traducido a 15 idiomas, el español entre ellos, y ha vendido más de 700.000 copias en todo el mundo. En el año 2014 Krugg publicó una edición extendida y completada con conceptos de usabilidad móvil, algo que en el origen del manual ni siquiera existía. El enfoque del libro es práctico y claro, está escrito de un modo divertido y tiene un alto enfoque en los usuarios destacando los comportamientos más obvios, la sobrecarga de contenidos o la importancia de la jerarquización de la información entre otros aspectos que facilitan el uso de los productos digitales.



## 3. La Evolución De Los Interfaces Digitales



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



Una vez que conocemos la definición de interfaz de usuario vamos a descubrir cómo ha sido su evolución en los diferentes productos digitales a lo largo de la historia de la informática.



### 3.2 CLI, Command Line Interface



El estándar Command Line Interface o Interfaz de Línea de Comandos existe prácticamente desde los comienzos de la informática y para su manejo la persona tiene que introducir una serie de caracteres en una línea para que el ordenador cumpla determinadas acciones. En informática, el Shell o intérprete de comandos es el programa informático que provee una interfaz de usuario para acceder a los servicios del sistema operativo. Los shell son necesarios para invocar o ejecutar los distintos programas disponibles en el ordenador. La siguiente imagen es un ejemplo de un interfaz CLI.



![image](assets/cm5s6qyqu00t13571cnia2x5e-Imagen4.png)



Los primeros Sistemas Operativos creados para el primer IBM PC en el año 1981, para el Apple II de 1977 y otras máquinas, no se parecían en nada a los ordenadores de hoy en día. Si algo tenían en común estos ordenadores es que usaban el formato CLI como interfaz de comunicación con el usuario. El monitor estaba dividido en 24 filas y 80 columnas de texto en blanco y negro.



1. MS-DOS o Microsoft Disk Operative System es quizá el sistema operativo basado en CLI más popular de la historia. Revolucionó la forma en que interactuamos con las computadoras personales en la década de 1980 y principios de 1990.

   Nació en 1980 cuando IBM encargó a Microsoft desarrollar un sistema operativo para su nueva línea de computadoras personales IBM PC. Microsoft compró **QDOS**(Quick and Dirty Operating System) a Tim Paterson, un programador de Seattle, por 50.000 dólares, cambiándole el nombre a **MS-DOS.**

   La primera versión de MS-DOS se lanzó en 1982 y rápidamente se convirtió en el sistema operativo estándar para los PC compatibles con IBM. No soportaba multitarea, ni multiprocesamiento.
2. Su interfaz de línea de comandos ofrecía un gran control sobre el sistema, permitiendo a los usuarios personalizarlo y automatizar tareas, aunque era exigente para los usuarios más novatos que en aquellos tiempos comenzaba a relacionarse con los ordenadores.

   En 1984, Microsoft había otorgado licencias de **MS-DOS** a 200 fabricantes de equipos informáticos y así este sistema operativo se convirtió en el más utilizado para PCs, lo que permitió a Microsoft crecer vertiginosamente en la década de 1980. La alianza entre IBM y Microsoft se rompió en 1991 pero para entonces Microsoft ya había hecho un trabajo estratégico importante.

   Microsoft descontinuó el soporte para MS-DOS en el año 2001.



### 3.3 GUI, Graphic User Interface



GUI, o Graphic User Interface, es una interfaz de usuario que emplea elementos gráficos como iconos, ventanas, menús y punteros para representar la información y las acciones que un usuario puede realizar en un dispositivo digital. Es la forma visual y amigable que tenemos para interactuar con nuestros ordenadores, smartphones y otros dispositivos que, a diferencia del interfaz basado en CLI, genera una mejor experiencia de usuario por su facilidad.

Su origen se remonta a los años 60, pero no fue hasta la década de los 70 cuando comenzaron a tomar forma en laboratorios de investigación como Xerox PARC (Palo Alto Research Center). El ordenador Xerox Alto (imagen 5) fue uno de los primeros en contar con una GUI rudimentaria. Este anuncio comercial [https://youtu.be/M0zgj2p7Ww4?si=36tWBOJt2LjnK8hJ](https://www.youtube.com/watch?v=M0zgj2p7Ww4) del año 1979 refleja lo innovadora que era la propuesta de Xerox que de haber enfocado su trabajo en la informática de consumo podía haber sido una empresa tan relevante como Apple o Microsoft.



![image](assets/cm5s87goi010i3571w9qttw1q-Imagen5.jpg)



El S.O de los populares ordenadores Macintosh fue pionero en la adopción de la interfaz gráfica de usuario denominada WIMP (del inglés Ventana / Window, Icono / Icon, Menú, Puntero / Pointer). Esta combinación, junto con el hardware innovador de Apple, lo convirtió en un referente en la industria por su facilidad de uso y estabilidad.



![image](assets/cm5s88lbp011v3571iw95yz4k-Imagen7.jpg)



En GUI el ordenador controla cada píxel de la pantalla, no hay ni filas ni columnas. En lugar de leer los comandos, el ordenador determina qué es lo que quiere hacer el usuario controlando el movimiento táctil o del puntero del ratón.

El uso de metáforas es muy relevante en GUI y conceptos como: copiar, cortar o pegar, papelera, escritorio o explorador de archivos entre otros, se representan con elementos reconocibles por el usuario en el mundo analógico.

En resumen, las GUI han revolucionado la forma en que interactuamos con los dispositivos digitales. Gracias a su intuitividad y facilidad de uso, podemos decir que son el estándar de facto en la industria de la informática de consumo.



### 3.4 NUI, Natural User Interface



Es la interfaz de usuario más reciente, en la **NUI** el usuario interactúa con el equipo sin utilizar dispositivos de entrada o sistemas de mando como teclados o ratones, sino que utiliza las manos, la voz o los movimientos gestuales del cuerpo del usuario.

El objetivo principal de la NUI es proporcionar un entorno visual más natural e intuitivo que el ofrecido por la GUI para la comunicación entre el usuario y el equipo. Crean una sensación de inmersión en la experiencia digital, haciendo que la interacción sea más fluida y agradable ya que la fricción con la tecnología es casi inexistente.

Son ejemplos de dispositivos con interfaces NUI:



- **Pantallas táctiles**  
  Permiten interactuar con los dispositivos a través del tacto, como deslizar, pellizcar o hacer zoom.
- **Reconocimiento de voz**  
  Utilizan comandos de voz para controlar aplicaciones y dispositivos. Los altavoces que incluyen interfaces conversacionales son un ejemplo de uso de NUI.
- **Realidad aumentada**  
  Superponen información digital en el mundo real, como ver las instrucciones de montaje de un mueble mientras lo armamo.
- **Gestos**  
  El uso de movimientos de las manos para controlar dispositivos, como cambiar de canción o responder una llamada.



Las NUI son más accesibles para un público más amplio, incluyendo niños y personas mayores. Al ser más intuitivas, permiten realizar tareas de manera más rápida y eficiente.

Aunque las interfaces NUI son muy populares cada tipo de interacción o dispositivo tiene un desarrollo particular y algunos retos que superar. La precisión de los sistemas de reconocimiento de gestos y voz puede verse afectada por variaciones en el entorno o en la forma de interactuar del usuario. Además, el uso de datos biométricos y de seguimiento para estas interfaces plantea preocupaciones importantes en cuanto a la privacidad. El desarrollo de interfaces NUI suele ser más costoso en comparación con las interfaces tradicionales, debido a la complejidad de las tecnologías involucradas.



### 3.5 OUI, Organic User Interface



Las Interfaces de Usuario Orgánicas (OUI) representan una evolución significativa en la forma en que interactuamos con la tecnología. A diferencia de las interfaces CLI, GUI o NUI, basadas en su mayoría en pantallas planas, gestos, voz o comandos, las OUIs buscan emular la naturalidad y fluidez de las interacciones humanas con el mundo físico.



![image](assets/cm5s8kd5c016e35716kx77d5v-Imagen8.jpg)



Este tipo de interfaces OUI pueden cambiar activa o pasivamente sus formas de vía de entradas físicas analógicas y en ocasiones los medios de salida también son la entrada. La superficie de visualización es siempre el lugar de interacción.

Las características principales de las interfaces OUI son:



- **Construidas de material tangible**  
  Usan materiales físicos como son la madera, la tela o la arcilla, permitiendo una interacción más táctil y sensorial.
- **Se adaptan de modo dinámico**  
  Las OUI se adaptan en tiempo real a las acciones del usuario y a las condiciones del entorno que son capaces de entender.
- **Están centradas en el cuerpo del usuario**  
  La interacción se produce a través de todo el cuerpo, involucrando gestos, movimientos y sensaciones.



Las Interfaces de Usuario Orgánicas buscan crear experiencias tan naturales como respirar. Imaginemos una tecnología que se amolda a nuestras necesidades, que nos entiende y responde sin esfuerzo a lo que queremos hacer. Las OUI logran esto comunicándose de forma clara y directa con nuestros sentidos, adaptándose a cada persona, a su forma de ser y hacer. Al considerar cómo pensamos y sentimos, las OUI hacen que interactuar con la tecnología sea tan intuitivo como hablar con un amigo.

Las OUI están actualmente en una etapa muy temprana de su desarrollo y se enfrentan a hándicaps relacionados con los materiales, el hardware y software e incluso a los estándares de diseño. Su potencial es muy grande y cuando se popularicen ofrecerán una experiencia de usuario en la que la tecnología será casi transparente permitiendo un aumento de la productividad de un modo mucho más accesible para todo tipo de usuarios.

La conexión entre NUI y OUI es más que evidente y podemos considerar ambos tipos de interfaz como complementarios. La NUI está centrada en la intuición y la naturalidad en la interacción utilizando voz o gestos para desarrollar la acción, mientras que OUI busca crear una experiencia más sensorial interactuando con objetos físicos.

Organic User Interface es una buena solución para entornos de diseño industrial, terapéuticos o educativos en los que la interacción con algo físico y tangible aporte un alto valor a la experiencia y un beneficio a los usuarios.



## 4. Usabilidad



### 4.1 Introducción



![image](assets/cm5s8ptyn019r3571avbk8byw-stock-image.jpg)



Hemos visto que el interfaz es de algún modo el puente entre el producto y el usuario, ahora nos adentraremos en las características que deben tener esos interfaces para que los usuarios puedan hacer un buen uso del producto. Uno de los aspectos fundamentales que hay que considerar cuando construimos un producto digital es la usabilidad.



### 4.2 Definición de usabilidad



La usabilidad no es algo desconocido para el gran público y probablemente ya tengas una idea aproximada de lo que es. Es un término que se utiliza muy habitualmente incluso entre personas que no tienen una formación técnica o de diseño para referirse a alguna característica que tiene un sistema digital.

De modo muy genérico podemos definir a la usabilidad como la característica que tiene un objeto que permite hacer uso de él. Cuando algo es fácil de usarse decimos que tiene una buena usabilidad.

De nuevo Donald Norman, padre del concepto Experiencia de Usuario al que ya nos hemos referido anteriormente, apunta en su libro “The Design of Everyday Things” de 1988 que: “Los seres humanos no siempre se equivocan. Pero sí lo hacen cuando las cosas están mal **concebidas y diseñadas.** Esta reflexión de Norman previa a la llegada de Internet ya nos pone sobre la pista de la importancia que tiene que los objetos tengan una correcta usabilidad, o ergonomía, para que los usuarios pueda utilizarlos sin cometer errores.

Definimos la usabilidad como la rapidez con que se puede aprender a utilizar algo, la eficiencia al utilizarlo, cuan memorable es, cuál es su grado de propensión al error y cuánto les gusta a los usuarios.

Las características que encontramos en esta definición se dividen en dos dimensiones:



- **1. DIMENSIÓN OBJETIVA**  
  - **Rapidez.** ¿Cómo de fácil resulta para los usuarios llevar a cabo tareas básicas la primera vez que se enfrentan al diseño? Una mejor usabilidad permitirá aumentar la velocidad en la que los usuarios resuelven una determinada tarea en el sistema.
  - **Eficiencia.** Una vez que los usuarios han aprendido el funcionamiento básico del diseño, ¿cuánto tardan en la realización de tareas? ¿Cuánto recursos consumen para terminar un proceso? El tiempo y el esfuerzo son los dos componentes que el usuario emplea para resolver un problema en un sistema digital y la buena usabilidad lo hace más eficiente ya que necesitaría emplear menos recursos.
  - **Memorabilidad o cualidad de ser recordado.** Cuando los usuarios vuelven a usar el diseño después de un periodo sin hacerlo, ¿cuánto tardan en volver a adquirir el conocimiento necesario para usarlo eficientemente? Lo ideal es que la forma de usar un producto sea tan intuitiva que el usuario no tenga que recordar nada. Es mejor el reconocimiento que el recuerdo.
  - **Propensión al error.** Durante la realización de una tarea, ¿cuántos errores comete el usuario?, ¿cómo de graves son las consecuencias de esos errores?, ¿cómo de rápido puede el usuario deshacer las consecuencias de sus propios errores? En los sistemas poco usables el usuario tiende a cometer más errores que en los que tienen una buena usabilidad. El porcentaje de errores es una de las características que puede hacer que un usuario abandone un producto y que le provoque una mala sensación de la empresa o de la marca.
- **2. DIMENSIÓN SUBJETIVA**  
  - **Belleza** ¿Cómo de agradable y sencillo le ha parecido al usuario la realización de las tareas? Cuando un usuario utiliza un sistema digital más cercano a sus gustos suele percibir en él una mayor usabilidad. El utilizar estándares gráficos o elementos que son tendencia en el mercado hace que las personas asocien ese producto con otros entornos que les gustan y eso les permite tener una mayor familiaridad con él y utilizarlo de modo más eficiente.



Los objetivos que tiene la buena usabilidad son:



•

Lograr el resultado.
La dimensión del “qué”. Hacer un sistema eficaz en el que se puedan resolver las tareas que busca el usuario.

EJEMPLO: Si estamos en la web de una compañía aérea ¿podemos comprar un billete a avión? ¿podemos consultar un horario? Independientemente de si se requiere mucho o poco tiempo o esfuerzo el sistema nos permite hacer lo que promete.

•

Lograr el resultado con el mínimo de recursos
La dimensión del “cómo”. Un sistema eficiente es el que permite al usuario resolver la tarea empleando el mínimo de esfuerzo y tiempo.

EJEMPLO: En la misma web de la compañía aérea que comentamos antes queremos modificar una reserva de un vuelo que ya tenemos comprado. ¿Qué cantidad de información nos ofrece el sistema para decidir dónde realizar esa acción? ¿Está expresado de forma correcta? ¿Los enlaces u opciones son comprensibles? ¿El número de clicks es razonable? Estas y otras preguntas nos dirán si un sistema es eficiente o no.



![image](assets/cm5s8zpqr01e23571qhbdaudo-Imagen9.png)



Cuando un producto digital es eficaz, cumple el objetivo para lo que fue creado, y es eficiente, lo hace utilizando pocos recursos para el usuario (tiempo y esfuerzo), decimos que se trata de un producto efectivo. La creación de productos efectivos y adaptados a las necesidades de los usuarios debería ser nuestro objetivo a la hora de trabajar.



### 4.3 Medición de la usabilidad



Aunque pueda parecer que la usabilidad es un concepto subjetivo hemos visto desgranando las características de la buena usabilidad (rapidez de aprendizaje, eficacia, memorabilidad, grado de propensión al error y belleza) que la mayoría de ellas son conceptos objetivos y por ellos cuantificables, valorables y medibles.

Ahora conoceremos algunos modos que empleamos para medir la usabilidad en diferentes momentos de la creación de un producto digital.



#### Test de Usabilidad



Un test de usabilidad es una prueba de investigación que se centra en la **observación directa** de cómo los usuarios (target users) **interactúan con el producto** o con una aproximación al producto. Para realizar un test de usuario de usabilidad no necesitamos tener el producto totalmente diseñado y programado, lo podemos realizar con un prototipo funcional interactivo sobre el que advertiremos al usuario que puede encontrarse funciones inactivas.

Un test de usuario de usabilidad es un tipo de experimento **individual** en el que la persona que participa tiene que comportarse de la forma más natural posible.

Los investigadores se centran en las reacciones de los usuarios, los problemas encontrados o las dudas que les genere. En un test de usabilidad a menudo se hacen preguntas al acabar o se pide al usuario rellenar cuestionarios para completar la información para entender con mayor profundidad los porqués de su comportamiento.



- **Los objetivos principales de un un test de usabilidad**  
  - **Encontrar problemas de usabilidad en la interfaz gráfica (UI)** Este es el principal objetivo de un test de usabilidad. Tenemos que pensar que los errores recogidos en la fase de pruebas con usuarios son problemas que nos ahorraremos cuando el producto esté en producción.
  - **Verificar que la herramienta es fácil de utilizar para la persona objetivo.** El test se realiza a usuarios lo más parecidos a los reales. Por ejemplo, si nuestro producto es una aplicación móvil de fitness realizaremos el test a usuarios interesados por el deporte, el ejercicio físico y que ya usen otras aplicaciones similares.
  - **Asegurarse de que la creación de contenidos o la consecución de una tarea se puede realizar de forma relativamente rápida.** El tiempo es una de las variables más relevantes cuando testamos productos ya que la posibilidad de que el usuario pueda resolver una tarea en un corto espacio de tiempo nos estará asegurando en parte su permanencia y conexión con el sistema.
  - **Recoger feedback cualitativo.** En forma de opiniones o comentarios de los usuarios participantes que nos ayude a mejorar la experiencia.Medir la eficacia a la hora de resolver tareas. Tanto el tiempo empleado como el número de errores generados son datos muy importantes que nos darán información valiosa sobre cómo los usuarios emplearán el producto cuando esté a su disposición.
  - **Medir la eficacia a la hora de resolver tareas.** Tanto el tiempo empleado como el número de errores generados son datos muy importantes que nos darán información valiosa sobre cómo los usuarios emplearán el producto cuando esté a su disposición.



Una de las grandes dudas cuando nos planteamos realizar un test de usabilidad es el tamaño de la muestra de usuarios a los que tenemos que realizarlo para que los resultados sean concluyentes. Aquí es importante mencionar la relevante investigación realizada por Jakob Nielsen (2000) titulada [Por qué solo necesitas 5 usuarios para tu test.](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)Este documento de Nielsen es quizá el mas relevante de la profesión a la hora de planificar un test de usabilidad y su lectura y aprendizaje es muy importante.

Según Nielsen, con un test de usabilidad de 5 usuarios encuentras el 85% de los problemas, mientras que necesitarías 15 usuarios para encontrar todos los problemas. Las pruebas de usuario con muchos participantes son un desperdicio de trabajo y dinero y por eso es mejor realizar tantas pruebas pequeñas como sea posible. Jakob Nielsen y Tom Landauer demostraron que la cantidad de problemas de usabilidad encontrados en una prueba de usabilidad con n usuarios es:



![image](assets/cm5s9lajl01jr3571h9gwikjz-Imagen10.png)



donde N es el número total de problemas de usabilidad en el diseño y L es la proporción de problemas de usabilidad descubiertos durante la prueba de un solo usuario. El valor típico de L es 31%, promediado en una gran cantidad de proyectos que estudiaron. Al trazar la curva para L = 31% se obtiene el siguiente resultado:



![image](assets/cm5s9m1tf01l43571cuoapqxu-Imagen11.jpg)



Para entender la lógica de por qué con solo 5 usuario encontraremos un alto porcentaje de errores podemos ejemplificar que si una interfaz tiene 12 errores supongamos que el **primer usuario** encuentra 4 de ellos. 
El **segundo usuario** participante también encuentra 4 errores, pero 2 de ellos son los mismos que los que ya encontró el primero con lo cual tendríamos 6, la mitad de los errores con solo 2 tests. El **tercer usuario** encontrará los errores que ya observaste con el primer usuario o con el segundo usuario e incluso algunas cosas que ya has visto dos veces. Además, el tercer usuario generará una pequeña cantidad de datos nuevos, aunque no tantos como los que te ofrecieron los dos primeros usuarios.

Al añadir más usuarios aprenderás muchas menos cosas y será menos probable que los usuarios encuentren nuevos errores. Nielsen dice que después del quinto usuario estás perdiendo el tiempo con los tests ya que estás observando continuamente que los usuarios cometen los mismos errores.

Algo que debemos tener muy en cuenta es el coste de realización de cada prueba. Un test de usabilidad requiere una inversión económica que podríamos detallar en los siguientes aspectos:



- **Investigadores que preparen y realicen el test**  
  Profesionales especializados en la realización de este tipo de pruebas.
- **Medios e infraestructura**  
  Alquiler de un local, si fuera necesario, y del software y hardware que van a utilizar los participantes.
- **Incentivos para los participantes**  
  Habitualmente se suele recompensar a los participantes con una pequeña cantidad de dinero o una tarjeta regalo. Siempre hay que considerarlo como un detalle de agradecimiento a los participantes por el tiempo dedicado.
- **Analítica de datos**  
  Una vez realizado el test será necesario analizar en detalle los resultados y extraer conclusiones. Este coste puede ser de software, de personas o de tiempo.



#### Análisis de click, scroll o ratón



Estos tipos de análisis que vamos a ver a continuación muchas veces se realizan con productos que ya están a disposición de los usuarios y para los cuales se utiliza software especializado con el que trazar el comportamiento por el sistema. Normalmente se suele lanzar una cookie en el navegador para avisar al usuario de este tipo de acciones Y cumplir con las normativas legales.

Algunas de las ventajas de estas técnicas son que se pueden obtener una gran cantidad de datos en un corto espacio de tiempo e incluso analizar en tiempo real lo que están haciendo los usuarios por una web.



- **Click test**  
  Una manera eficaz de determinar el comportamiento de los usuarios es mediante el registro y análisis de clics. El objetivo de estas pruebas es determinar qué enlaces, contenido o elementos del menú u otros elementos de la interfaz reciben la mayor cantidad de clics.

  Al mismo tiempo, es posible obtener información sobre el interés específico del usuario en determinadas áreas de la web que, a la vez, **pueden resultar poco funcionales.**
- **Movimiento de ratón**  
  Esta forma de visualizar el comportamiento del usuario no se basa en el movimiento de los ojos, en su desplazamiento por la web o en la cantidad de clics, sino en los movimientos hechos por los usuarios con el cursor del ratón.

  Por lo general, este tipo de análisis arroja una imagen muy precisa sobre las áreas que un usuario estuvo observando en un momento determinado. Al igual que en el eye tracking, este método requiere un registro completo de la sesión del usuario.
- **Scroll tracking**  
  Aunque las herramientas tradicionales de análisis web te muestran el tiempo de permanencia de un usuario, estas no siempre dan información sobre si este se ha desplazado hasta el final o solo ha percibido la parte superior.

  El llamado scroll tracking es un indicador importante a la hora de determinar si el contenido es recibido correctamente por parte de los visitantes de la web.

  Si los resultados arrojados por el scroll tracking no son tan favorables para el ámbito inferior de la página, esto puede ser una señal de que la calidad general del texto y otros contenidos deben mejorarse o de que, tal vez, la longitud elegida no es la ideal.



#### El análisis de expertos



Este tipo de análisis de la evaluación de la usabilidad se basa en principios ampliamente reconocidos y en la experiencia de expertos en usabilidad y diseño de interfaces. En un análisis de expertos no participan los usuarios si no que los expertos interactúan con el producto y emiten una valoración en base a unos criterios previamente establecidos y avalados por su amplia experiencia de criterios de usabilidad.

Los expertos realizan un recorrido por el producto, tratando de comportarse como si fueran usuarios, y durante el proceso van identificando problemas potenciales que los compara con una lista de principios de usabilidad, las llamadas heurísticas. Las heurísticas son reglas generales que describen prácticas comunes en los interfaces a las cuales en analizador experto puede añadir las que considere que son beneficiosas para el uso del producto.

Aunque no hay una norma fija sí que se suele aconsejar que los evaluadores revisen por lo menos 2 veces la interfaz que están analizando.

El análisis de expertos es una forma razonablemente rápida de encontrar problemas de usabilidad en un sistema digital ya que no es necesario contrastar la propuesta que estamos validando a un grupo de usuarios y evitamos todos los procesos necesarios en ese tipo de test que vimos en el punto anterior. Si disponemos de acceso rápido a expertos podremos detectar errores en una fase temprana y eso nos permitirá agilizar el desarrollo del producto.

Incorporar el análisis de expertos aporta una visión más global sobre la usabilidad ya que al analizarlo diferentes personas cada uno incorporará su punto de vista. SI bien en muchos casos este tipo de análisis es bueno que sea complementario a las pruebas realizadas con usuarios.



#### Los heurísiticos de usabilidad de Jakob Nielsen



- **1. Visibilidad y estado del sistema**  
  El usuario debe de tener conocimiento de qué está pasando y qué está haciendo en todo momento, aunque sea subconscientemente.

  EJEMPLOS:
  Los títulos en las secciones o páginas, las barras de carga o los cambios de estado de un elemento suelen ser buenos indicadores del estado del sistema.
- **2. Coincidencia entre el sistema y el mundo real**  
  El sistema debe de hablar el mismo idioma que el usuario, para que así éste no se sienta marginado, especialmente si no es un programa para una actividad especializada o de un nicho muy concreto. El diseño tiene que seguir convenciones y conceptos existentes en el mundo real para que de esa forma el usuario lo entienda más fácilmente.

  También es importante que la información se muestre en un orden natural y lógico, y además, debe de comprenderse de forma sencilla.

  EJEMPLOS:

  El uso de metáforas reconocibles en los iconos como puede ser una lupa para buscar o una papelera para elementos eliminados
- **3. Control y libertad del usuario**  
  A menudo los usuarios comenten errores utilizando una interfaz y por esa razón ninguna acción que se realice debería de ser irreversible, especialmente las que tengan un impacto grande o consecuencias negativas en el usuario. Además, hay que tratar de ofrecer vías de acceso o salidas alternativas para poder realizar la tarea que necesita o conviene. Tantas como complejo sea el entorno.

  EJEMPLOS:

  Tener la opción de recuperar un correo electrónico que se borró por error o poder deshacer una determinada acción.
- **4. Consistencia y estándares**  
  El sistema debe tener unas normas que informen al usuario cómo se utiliza sin necesidad de aprender desde cero. Si dos elementos hacen la misma función, deben de representarse de la misma forma, y esta forma debe de diseñarse acorde a los lugares donde se encuentre y el contexto de uso del producto. Lo mismo con hay que hacer con textos, términos y otros componentes que den información al usuario.

  EJEMPLOS:

  Que todos los botones de acción tengan un mismo color o colocar el acceso al carrito de la compra en un comercio electrónico arriba a la derecha.
- **5. Prevención de los errores**  
  Aunque parezca complicado hay que tratar de que los errores no ocurran ofreciendo al usuario toda la información necesaria para realizar una acción.

  EJEMPLO:

  En esta imagen vemos un registro que al pedir al usuario crear su contraseña le va informando de la validez de lo que va haciendo en base a los criterios establecidos por el propio sistema.
- **6. Reconocimiento mejor que recuerdo. Minimizar la memoria del usuario.**  
  Va muy de la mano con el heurístico de consistencia y estándares. Nuestro producto debe de reconocerse fácilmente o explicarse por sí solo. El usuario debe poder entenderlo sin un gasto de memoria y análisis excesivo. El usar elementos visuales y no solo textuales ayuda al usuario a identificarlos más fácilmente con un escaneo rápido de la pantalla.

  EJEMPLO:

  La búsqueda de Spotify no solo muestra los títulos de los álbumes, sino que también ofrece las portadas de los discos para que así el usuario los encuentre más fácilmente.
- **7. Flexibilidad y eficiencia de uso**  
  Se recomienda analizar y reconocer cuáles son los elementos más usados de tu producto (o cuáles te conviene que cumplan el objetivo principal) y jerarquizar la información de forma que tengan un lugar y apariencia privilegiada. El usuario tiene que poder acceder a determinados contenidos o funcionalidades más usadas de diferentes modos

  El sistema tiene que adaptarse a los diferentes niveles de experiencia que pueden tener los usuarios y no por ello penalizar a los más novatos sobre los expertos o viceversa.

  EJEMPLOS:

  Muchos sitios de comercio electrónico ofrecen una gran variedad de filtros que hacen que los usuarios puedan encontrar lo que buscan por diferentes vías según su forma de moverse por el sistema. Las denominadas “landing page” destacan los botones de llamada a la acción de forma que el usuario no tenga duda y pulse sobre ellos.
- **8. Diseño estético y minimalista**  
  Si la interfaz es sencilla, usar el producto será sencillo. Recargar con colores, elementos y formas innecesarias que además no consigan comunicar bien sólo servirá para hacer más difícil su uso.

  Esto también aplica al texto. Los productos con un diseño sencillo transmiten una mayor sencillez de uso y,la mayoría de las veces, una mejor usabilidad.

  EJEMPLOS:

  El portal inmobiliario Idealista es un muy buen ejemplo de cómo el diseño minimalista y estético ayuda a una usabilidad excelente en el que la funcionalidad tiene una presencia proporcionada sin descuidar una imagen gráfica con razonable personalidad.
- **9. Ayudar al usuario a reconocer, entender y recuperarse de los errores**  
  El heurístico 5 nos hablaba sobre la prevención de errores, pero sabemos que no siempre es posible que los errores no existan. Si suceden, deben expresarse siempre en lenguaje comprensible para el usuario y sin tecnicismos, si es posible, debemos darle opción de solucionarlos con el mínimo esfuerzo posible.

  EJEMPLOS:

  Páginas de error en las que el usuario tiene alternativas para seguir navegando o que el mensaje no está expresado en modo técnico.
- **10. Ayuda y documentación**  
  Si el usuario necesita más información para usar el sistema, démosle ese contenido de forma ordenada y con un acceso fácil desde un lugar esperado. Para esto puede ser útil una documentación sobre el producto, un chat de soporte, una sección de ayuda…

  EJEMPLOS:

  Muchas plataformas digitales disponen de manuales, preguntas frecuentes, videotutoriales, secciones de ayuda o guías de navegación.



Al igual que ya Jakob Nielsen concluyó con que con solamente con 5 test de usabilidad éramos capaces de encontrar el 85% de los errores de una web, también fijó sobre cuántos tests necesitaríamos para encontrar el máximo de errores utilizando la metodología del análisis de expertos.

En su investigación argumenta el por qué únicamente con 5 expertos puedes llegar a encontrar el 75% de los errores utilizando una prueba de análisis heurístico. Aunque la variable del costo-beneficio es la que marcaría cuántos tests podemos hacer para avanzar en la usabilidad de nuestro producto y asegurarnos de que no tiene errores de usabilidad. Si creemos que nuestro producto va a generar menos ingresos porque tiene algún problema grave de usabilidad lo correcto sería invertir más tiempo y presupuesto en contratar expertos que vayan refinándolo hasta el máximo.



> La investigación de Nielsen es del año 1994 y la puedes consultar en el siguiente enlace.
>
> [Link](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/theory-heuristic-evaluations/)



![image](assets/cm5sacm8401v33571bgl5q7yp-Imagen19.gif)



### 4.4 La curva de aprendizaje



La curva de aprendizaje representa la relación existente entre el tiempo invertido por un usuario en aprender a utilizar un sistema y su aprendizaje para realizar tareas dentro del mismo.

Es un concepto muy importante cuando trabajamos el interfaz ya que la curva de aprendizaje es el resultado de la cantidad de tiempo y esfuerzo que tiene que aportar el usuario para resolver una tarea. Realmente cualquier usuario podría emplear cualquier interfaz simplemente con tiempo y esfuerzo, pero la clave es que lo haga con la curva de aprendizaje óptima en relación a lo que va a obtener del sistema.

En el siguiente vídeo veremos la conexión de la curva de aprendizaje con otros elementos del mundo físico, lo que supone su existencia cuando los usuarios van a utilizar un interfaz y descubriremos algunos modos para reducir su impacto y hacer el sistema más sencillo para las personas.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_FUUX_A/content/_652060_1/scormcontent/assets/INSD_FUUX_U1_Apartado5_Video1.mp4?v=1)



## 5. Accesibilidad



### 5.1 Introducción



![image](assets/cm5salc1m01xh3571xuvfibkp-stock-image.jpg)



En este último apartado de la unidad vamos a ver que es muy importante que construyamos productos adaptados a todo tipo de usuarios independientemente de sus habilidades. La accesibilidad es un derecho de las personas y una responsabilidad social para las empresas ya que de ese modo están participando en que el mundo sea más equitativo e inclusivo.



### 5.2 Definición de accesibilidad



En términos genéricos decimos que la accesibilidad es el grado en el que todas las personas pueden utilizar un objeto, visitar un lugar o acceder a un servicio, independientemente de sus capacidades **técnicas, cognitivas o físicas.**

Discapacidad o diversidad funcional es un término general que abarca las distintas deficiencias o las limitaciones de la actividad y las restricciones de la participación. Es una experiencia individual, personal y diferente**por eso no hay discapacitados sino personas con discapacidad.** Puede afectar a la naturaleza, duración y/o calidad de las actividades. Influye el tipo de la deficiencia, pero también los recursos de los que se cuenta y las tareas a las que debe enfrentarse la persona.

La accesibilidad tecnológica trata de asegurar que los ordenadores, la web, los contenidos digitales, etc. puedan ser usados por todo tipo de personas independientemente de sus capacidades, especialmente las personas mayores o con algún tipo de discapacidad.

Cuando hablamos de accesibilidad podemos cometer el error que todas las personas con alguna discapacidad con iguales y eso no es así. Hay diferentes tipos de discapacidad dependiendo de la parte del organismo que esté afectada.

Como creadores de productos digitales nuestro propósito tiene que ser que cualquier persona pueda usar nuestro producto y eso, como muestra la siguiente imagen, solo se consigue cuando todos los usuarios llegan al mismo nivel de funcionalidad porque el sistema se lo permite.



![image](assets/cm5sarthx01zl3571u5ku2rvx-Imagen20.jpg)



### 5.3 Actores y bases principales de la accesibilidad



La accesibilidad no es una disciplina que afecte a una parte de la compañía, sino que hay muchos perfiles que tienen que considerarla en su trabajo. Solamente unificando el conocimiento y la sensibilidad de todas las partes podremos construir productos accesibles.

Los actores que participan para que la accesibilidad de un producto sea correcta son:



- **Desarrolladores**  
  Tienen la responsabilidad de la maquetación, html, css y tecnologías.
- **Creadores de contenido**  
  Crean imágenes, textos, audio, vídeo y los publican en la web.
- **Diseñadores**  
  Deciden la estructura, organización, interacción y aspecto gráfico.



En el caso del trabajo de experiencia de usuario este rol es responsable en concreto de:

- Diseñar elementos fáciles de identificar.
- Optimizar el contraste de color de los elementos. Usar combinaciones de color diferenciables para personas que tengan dificultades como el daltonismo.
- Facilitar la lectura de textos.
- Cuidar la consistencia, la claridad y la sencillez
- Organización y presentación de contenidos. Diseñar navegaciones claras y consistentes en las que no se pierda ningún usuario.
- Diseño apropiado de los formularios. Que las etiquetas sean claras y que dispongan de las ayudas necesarias.
- Prevenir e informar de los errores.



### 5.4 Principios de la accesibilidad



La accesibilidad de un producto digital no es algo subjetivo que pueda quedar al arbitrio de sus creadores, dueños o desarrolladores. En el siguiente vídeo vamos a ver cuáles son los principios de la accesibilidad y profundizar en cómo se regulan.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_FUUX_A/content/_652060_1/scormcontent/assets/INSD_FUUX_U1_Apartado6_Video1.mp4?v=1)



En el video se hace referencia a los niveles de accesibilidad dependiendo del grado de cumplimiento de cada 1 de los principios. Los niveles son:



- **Nivel A. Accesibilidad básica**  
  Este nivel es el más básico en la accesibilidad y lo cumple una web que simplemente garantiza que los usuarios puedan acceder a la información principal. Se asegura de que las imágenes tengan texto alternativo y de que los encabezados estén bien organizados para estructurar el contenido. Está lejos de considerarse una web accesible
- **Nivel AA. Accesibilidad mejorada**  
  En este nivel se incluyen todos los requisitos vistos en el nivel A y añade otros que mejoren la experiencia de interacción del usuario con el sistema preocupándose de que pueda ser utilizado por teclado o que el contraste de color sea suficiente.

  Muchos usuarios, incluyendo los que tienen las discapacidades más comunes, podrían utilizar un sitio web de nivel AA.
- **Nivel AAA. Máxima accesibilidad**  
  Cumple los criterios de los niveles A y AA, y además este nivel es el que considera la accesibilidad de un modo más riguroso, con prácticas como tener distintas formas de encontrar el contenido u ofrecer transcripciones en texto, audio o lengua de signos para el contenido audiovisual.



Ahora que ya conoces los principios de la accesibilidad y la escala para validar si un producto digital es o no es accesible y en qué grado, te preguntarás quién otorga estos 3 niveles A, AA, AAA. Realmente no hay un organismo que lo conceda y queda en manos de los propietarios del producto el hacer la revisión de los principios, pautas y criterios y con eso concederse el nivel correspondiente y , en muchos casos, comunicarlo en algún lugar de la web.



### 5.5 Buenas prácticas en desarrollo web



En el desarrollo web impactan muchos aspectos para que un producto sea accesible. Si bien la mejor recomendación es que tengas siempre presente la accesibilidad en todo lo que hagas, podemos concretar las buenas prácticas bajo estas categorías:



- **Diseño**  
  - El contraste de color tiene que ser suficiente para que no haya confusión entre los elementos. También es importante que se diferencien los objetos y el fondo.
  - La jerarquía tipográfica tiene que ser lo suficientemente amplia para que usuarios que que tienen problemas de lectura no necesiten ampliar la pantalla.
  - El color no puede ser el único modo de información por eso, al igual que en un semáforo, tenemos que dar los mensajes con color y forma.
  - Hay que estructurar el contenido para que el usuario pueda entenderlo fácilmente Y con poco esfuerzo.
  - En los textos es importante que tanto el espaciado entre líneas como entre letras sea lo suficiente para que la lectura sea clara.
- **Desarrollo**  
  - El HTML tiene que ser lo más semántico posible y para ello el uso de encabezados (H1, H2, H3…) y etiquetas de HTML 5 es una buena práctica.
  - Ofrece textos alternativos que describan las imágenes con la etiqueta “alt” para que lo puedan leer los lectores de pantalla. Escribe estos textos de modo descriptivo y evita que simplemente ponga “imagen”, piensa que una persona que no ve lo que se escuchará en su software de voz es imagen, pero no sabrá qué es lo que hay en la imagen.
  - Si trabajas con Javascript tienes que tratar que tu código sea accesible y recuerda que hay usuarios de sistemas que tienen el Javascript desactivado.
  - El uso de listas ordenadas o no ordenadas sirve para agrupar elementos que tienen relación entre sí.
  - Emplea tablas solamente cuando necesites tabular datos pero no para crear el diseño de tu página. Vigila que tu tabla tenga encabezados en las filas y en las columnas.
  - Considera utilizar los atributos ARIA (Accessible Rich Internet Applications) [https://www.w3.org/WAI/standards-guidelines/aria/](https://www.w3.org/WAI/standards-guidelines/aria/)en tu HTML para dotarlo de una información adicional de accesibilidad que lo hará muy útil para lectores de pantallas y otras herramientas de asistencia a usuarios con problemas de acceso.
- **Interacción**  
  - Intenta que la navegación de tu producto sea posible mediante teclado y no solo utilizando ratón.
  - Ten especial cuidado cuando vayas a crear un formulario para que todos los campos sean descriptivos y pueda rellenarse utilizando el tabulador.
  - El tiempo de carga de la web o de la interacción sobre determinados elementos puede suponer un problema para algunos usuarios y es otro aspecto que tienes que considerar.



### 5.6 Marco regulatorio de la accesibilidad



Como futuro ingeniero del software es importante que sepas que en algunos países la implantación de la accesibilidad en productos digitales está regulada por la legislación. Estas medidas tienen como objetivo que todos los ciudadanos puedan acceder a los servicios y productos digitales independientemente de sus capacidades. Los marcos regulatorios de accesibilidad obligan a empresas, organizamos e instituciones a cumplir determinados niveles en sus desarrollos y, en el caso de no hacerlo, enfrentarse a sanciones económicas.

En muchos países se toman como estándar de referencia las normas WCAG (Web Content Accessibility Guidelines), que vimos anteriormente, y que aseguran que un producto es perceptible, operable, comprensible y robusto. El cumplimiento de normas de accesibilidad además es un argumento de reputación para las empresas ya que con ello comunican que se preocupan de todas las personas por igual.

En la Unión Europea la directiva (UE) 2016/2102 publicada en octubre del año 2016 (https://eur-lex.europa.eu/eli/dir/2016/2102/oj) obliga hacer accesibles todos los sitios web y aplicaciones móviles del sector público y sirve como margo regulatorio para que cada país establezca normas más estrictas.



## 6. Conclusiones



### 6.1 Conclusiones de la unidad



Como conclusiones a esta unidad didáctica podemos enumerar que el alumno dispone de conocimientos suficientes sobre:

- Qué es la experiencia de usuario y la importancia dentro de la creación de productos digitales.
- La historia y la evolución de los diferentes tipos de interfaces que han existido en el mundo de la informática.
- La importancia y definición de la usabilidad y diferentes técnicas para obtener análisis para medirla.
- Los 10 heurísticos de la usabilidad de Jakob Nielsen y cómo emplearlos en un proyecto para mejorar la usabilidad.
- Cómo incorporar la accesibilidad al trabajo de desarrollo del software y las normativas técnicas, sociales y legales que recoge esta disciplina.
