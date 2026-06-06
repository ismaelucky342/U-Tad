# Unidad 3. Validación y Futuro de Interfaces.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. ¿Cómo Validamos?](#2-cómo-validamos)
  - [2.1 Introducción](#21-introducción)
  - [2.2 Validación en laboratorio](#22-validación-en-laboratorio)
  - [2.3 Validación con usuarios](#23-validación-con-usuarios)
  - [2.4 Validación en producción](#24-validación-en-producción)
- [3. Análisis De Interfaces](#3-análisis-de-interfaces)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Métodos de evaluación](#32-métodos-de-evaluación)
- [4. Interfaces Móviles](#4-interfaces-móviles)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Interacción móvil](#42-interacción-móvil)
  - [4.3 Principios y patrones de usabilidad móvil](#43-principios-y-patrones-de-usabilidad-móvil)
  - [4.4 Patrones](#44-patrones)
- [5. El Futuro De Las Interfaces Y La Ux](#5-el-futuro-de-las-interfaces-y-la-ux)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Interfaces conversacionales](#52-interfaces-conversacionales)
  - [5.3 Realidad virtual, aumentada y mixta](#53-realidad-virtual-aumentada-y-mixta)
  - [5.4 Interfaces gestuales](#54-interfaces-gestuales)
- [6. Conclusiones](#6-conclusiones)
  - [6.1 Conclusiones de la unidad](#61-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



En esta unidad nos adentraremos en el crucial proceso de validación de interfaces. Con su estudio consolidarás los conocimientos adquiridos previamente y podrás aplicarlos en un contexto práctico y riguroso.

Aprenderemos a evaluar la usabilidad de los interfaces digitales asegurando que la UX sea óptima y satisfactoria. Exploraremos métodos y herramientas que nos permitirán tomar decisiones informadas, tanto a nivel tecnológico como estratégico, para el negocio.

Conscientes de la diversidad de dispositivos y plataformas, dedicaremos un espacio específico a la usabilidad de interfaces móviles, un área en constante evolución y de gran relevancia en el panorama actual que tiene características, terminología y principios propios.

Finalmente, exploraremos el futuro de las interfaces anticipando las tendencias y tecnologías emergentes que están transformando la interacción entre usuarios y productos digitales comprendiendo su impacto y potencial en la creación de experiencias innovadoras y envolventes.

Los apartados a tratar en esta unidad didáctica serán:



- **¿Cómo validamos?**  
  Validar una interfaz es el proceso por el que se determina el valor o la calidad de esta en relación con unos objetivos marcados. El objetivo básico habitual de la evaluación es conseguir el grado máximo de usabilidad, aunque también podemos tener otros relacionados con la percepción que los usuarios tienen del sistema.
- **Análisis de Interfaces**  
  El análisis de interfaces es un aspecto primordial en el desarrollo de productos digitales ya que va más allá de contemplar el aspecto estético y profundiza en la organización, la interacción o las sensaciones que le provocan las interfaces al usuario. Busca comprender cómo se relaciona la persona con el sistema evaluando tanto la eficacia como la eficiencia de las soluciones planteadas. También considera el contexto en el que se utiliza el producto y se tienen en cuenta aspectos como el dispositivo, el entorno o las preferencias culturales de los usuarios.
- **Interfaces móviles**  
  En este apartado vamos a ver como el diseño y trabajo con interfaces móviles presenta un reto para los desarrolladores de productos digitales derivado de la limitación del espacio, los diferentes contextos de uso que tienen los productos y el paradigma de la interacción táctil que es muy diferente al de ordenador.
- **El Futuro de las Interfaces y la UX**  
  La computación espacial es una tecnología emergente que integra el mundo digital y en físico permitiendo a las personas interactuar con las máquinas de modo inmersivo y natural. Este concepto es muy relevante cuando hablamos del futuro de las interfaces y la experiencia de usuario ya que, si recuerdas, el interfaz era el puente con el cual las personas pueden operar y controlar a las máquinas y sus paradigmas, CLI, GUI, NUI o OUI, están en constante evolución



#### Objetivos



1. Conocer y aplicar diversas herramientas de validación útiles para el futuro profesional.
2. Comprender la importancia de fundamentar las decisiones de diseño en datos obtenidos en las fases de investigación, en lugar de en opiniones o creencias.
3. Aprender los principios y patrones de usabilidad específicos para dispositivos móviles, así como el comportamiento de los usuarios en estos dispositivos.
4. Prepararse para trabajar en áreas emergentes como interfaces conversacionales, realidad aumentada y virtual, e interfaces gestuales.
5. Unir todos los conceptos aprendidos durante la asignatura para desarrollar productos digitales con experiencias de usuario excelentes.



## 2. ¿Cómo Validamos?



### 2.1 Introducción



![image](assets/cm8vlsndu004h356ygu19qj8t-stock-image.jpg)



Validar una interfaz es el proceso por el que se determina el valor o la calidad de esta en relación con unos objetivos marcados. El objetivo básico habitual de la evaluación es conseguir el grado máximo de usabilidad, aunque también podemos tener otros relacionados con la percepción que los usuarios tienen del sistema.

Desde un punto de vista conceptual hay cuatro formas básicas y complementarias de evaluar:

- La **evaluación automática** es aquella en la que se mide la usabilidad a través de un recuento computarizado de datos.
- La **evaluación empírica** se realiza a través de tests con usuarios reales.
- La **evaluación formal** que usa fórmulas para calcular la usabilidad.
- La **evaluación informal**, que tiene en cuenta diversas variables tales como la experiencia de los evaluadores o el nivel de formación de los usuarios

Para validar interfaces y experiencia de usuario tenemos diferentes canales dependiendo del objetivo, del tipo de producto que estemos desarrollando o del presupuesto que tengamos establecido para la fase de validación. Algunas de estas pruebas las podemos realizar con recursos personales o de software que ya tengamos y para otras necesitaremos subcontratar a una empresa especializada que disponga del conocimiento, de los medios y del personal cualificado.



### 2.2 Validación en laboratorio



Al igual que en otras disciplinas un laboratorio de UX es un entorno controlado donde se pueden realizar pruebas con usuarios reales y recopilar datos muy valiosos de cómo estos interactúan con un producto o una interfaz. En un laboratorio el usuario no tiene las distracciones del mundo exterior y se pueden controlar variables como el ruido, la luminosidad o el tipo de dispositivo empleado, aspectos que inciden en la rigurosidad de los datos generados en este tipo de pruebas.

Los investigadores tienen la opción de observar de modo directo como los usuarios que interactúan con el producto y detectar patrones de comportamiento que podrían pasar desapercibidos en un test remoto. También se aseguran del conocimiento previo que tienen los usuarios y de su pertinencia como participantes válidos en la investigación.

Desde un punto de vista cualitativo un laboratorio también nos permite interactuar directamente con los usuarios y preguntarles sobre su experiencia con la interfaz para conocer mejor sus necesidades y motivaciones. Si esas opiniones nos generarán alguna duda un laboratorio también es el lugar idóneo para realizar otras técnicas de investigación como las entrevistas o los focus group.

Los componentes o espacios que podemos encontrarnos habitualmente en un laboratorio de UX son:



- **Sala de pruebas**  
  Espacio desde el que el usuario realiza las tareas propuestas. Dispone de ordenadores, móviles u otros dispositivos.
- **Sala de observación**  
  Desde la que los investigadores observan en directo lo que sucede en la sala de pruebas mediante un espejo unidireccional que para los participantes pasa desapercibido y hace que no compartan espacio.
- **Equipo de grabación**  
  Cámaras y micrófonos con los que grabar las reacciones de los usuarios participantes.
- **Software especializado**  
  Herramientas para grabar el movimiento del ratón, la mirada, el scroll… También se emplea software de prototipado interactivo o de encuestas para recoger otro tipo de datos.



Ya que se realizan grabaciones es importante garantizar la privacidad y confidencialidad de los participantes y estos deben de ser informados del propósito de la prueba y firmar un consentimiento del uso de sus acciones.

Los laboratorios tienen también algunos inconvenientes que es importante que conozcas. Puede existir una falta de realidad que haga que los usuarios nos en comporten del mismo modo que lo harían en el contexto real. Por eso es importante tener siempre en cuenta que a las pruebas de laboratorio a menudo le faltan los componentes externos en los que se usa el sistema y por eso tenemos que elegir bien si nuestro producto es susceptible de investigarse en laboratorio. Por ejemplo, una aplicación para registrar la actividad física en directo necesitaría poder probarse en exterior y en movimiento.

Otro problema que tienen las investigaciones en laboratorio es que el presupuesto económico que tenemos que destinar no es especialmente barato ya que se necesitan instalaciones, dispositivos y personal cualificado.

Por último, cabe señalar que la presencia de investigadores puede influir en el modo en cómo se comportan los usuarios e introducir ciertos sesgos en los resultados obtenidos.



### 2.3 Validación con usuarios



Como tantas cosas en esta disciplina la idea de realizar pruebas con usuarios fue de Jacob Nielsen quien. en un artículo del año 1997, argumentaba que la ausencia de la ingeniería de usabilidad en proyectos de desarrollo de software le costaba a la economía estadounidense unos 30.000 millones de dólares al año en productividad. Nielsen decía que era necesario que los equipos de ingeniería pudieran tuvieran tiempo y presupuesto para probar sus desarrollos con uno o dos usuarios y de ese modo ahorrarían millones de dólares.

La validación con usuarios es quizá la piedra angular de la investigación en UX. En algunas de las técnicas que vimos en las unidades anteriores participaban usuarios en la fase de descubrimiento y detección de necesidades. En un proyecto con un enfoque honesto centrado en los usuarios, contar con ellos no es un paso opcional, sino que es el modo de generar veracidad y salir de las suposiciones para entender y comprobar como las personas usan el producto.

Las razones por las que validamos con usuarios son:



- **Minimizar riesgos**  
  Que un usuario real pueda terminar una tarea o utilizar una determinada funcionalidad nos evita errores en producción y minimiza costes y tiempo de corrección.
- **Enfocarnos en la persona**  
  Cuando probamos nuestro trabajo con usuarios reales y además tenemos la ocasión de verlos en directo generamos la empatía necesaria para pensar en ellos en cada decisión que tomemos. También sirven para recordarnos que nosotros no somos el usuario.
- **Argumentación interna**  
  Las pruebas con usuarios generan unos argumentos convincentes con los cuales mostrar el valor del trabajo de experiencia de usuario a los stakeholders (personas internas interesadas en el proyecto). Es habitual desmontar creencias y mitos después de validar con usuarios y sirven para impulsar internamente el enfoque de trabajo centrado en las personas.
- **Innovación**  
  La validación con usuarios nos puede hacer ver otros modos de resolver los problemas. Con ella a menudo detectamos oportunidades de diseño más difíciles de encontrar en el trabajo individual ya que los modelos mentales de los usuarios y los diseñadores son distintos.



### 2.4 Validación en producción



Las pruebas de validación en producción son transparentes para los usuarios ya que habitualmente ellos no son conscientes de que con su comportamiento los creadores del producto están obteniendo datos.

Cuando vimos el proceso de metodología de diseño centrado en el usuario recordarás que en la última fase hablábamos de la monitorización de lo que hacen los usuarios con el producto una vez publicado. Esta forma de validar en producción es un paso crucial para asegurarnos la calidad de nuestro interfaz puesto que, a diferencia de las pruebas en entornos controlados, se hace con el producto en vivo y en condiciones reales.

La principal ventaja obvia de este tipo de pruebas es la veracidad de los datos obtenidos, pero también lo es la posibilidad de obtener grandes volúmenes de datos en un tiempo razonablemente corto lo que hace la muestra más representativa. Para los ingenieros también es interesante considerar que esta monitorización en entornos reales sirve para encontrar mejoras en el rendimiento o la compatibilidad de sistemas o dispositivos, aspectos más difíciles de testar en ambientes controlados.

Entre los riesgos que podemos considerar en las pruebas en producción tenemos las siguientes:



- **Dificultad de contexto**  
  Desconocemos por completo las variables que pueden impactar en el comportamiento del usuario más allá de las concretas y relativas a su dispositivo, navegador, hora o localización entre otras. Los aspectos cualitativos suelen quedar fuera de este tipo de validación.
- **Impacto en los usuarios**  
  Estamos jugando con fuego real y por eso hay que medir muy bien cada elemento de la interfaz que queremos medir ya que pueden dificultad las tareas del usuario E incorporar ruido innecesario en el producto.
- **Análisis de datos**  
  Requeriremos de herramientas de software especializado para analizar los datos recopilados y poder interpretarlos.
- **Aplicabilidad de los datos**  
  Es más habitual de lo que podríamos imaginar el almacenar montañas de datos obtenidos de los usuarios que no somos capaces de transformar en iniciativas concretas que mejoren el producto.



La validación en producción es una metodología continua que debería estar siempre presente en cualquier proyecto y ser uno de los primeros canales de obtención de información para las mejoras del interfaz.

En el siguiente apartado veremos técnicas concretas de validación de interfaces en producción, y de otros tipos, que te resultarán interesantes cuando te enfrentes a un proyecto real.



## 3. Análisis De Interfaces



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



El análisis de interfaces es un aspecto primordial en el desarrollo de productos digitales ya que va más allá de contemplar el aspecto estético y profundiza en la organización, la interacción o las sensaciones que le provocan las interfaces al usuario. Busca comprender cómo se relaciona la persona con el sistema evaluando tanto la eficacia como la eficiencia de las soluciones planteadas. También considera el contexto en el que se utiliza el producto y se tienen en cuenta aspectos como el dispositivo, el entorno o las preferencias culturales de los usuarios. El fin último de analizar los interfaces es que los productos digitales sean intuitivos y agradables de utilizar para que la experiencia del usuario sea memorable y eso revierta en el éxito del producto.

Vamos a profundizar en diferentes procedimientos que nos ayudan analizar los interfaces en distintas etapas del desarrollo del producto, todos ellos orientados a la mejora continua.



### 3.2 Métodos de evaluación



Un método de evaluación es aquel procedimiento en el que se recogen datos relevantes sobre la operabilidad y usabilidad de un sistema. La evaluación puede ayudar a la interfaz a ser usable, y debe tenerse en cuenta que los aspectos problemáticos o de otra índole detectados no sólo van a mejorar esta interfaz sino la experiencia con el producto en su conjunto.

A menudo la evaluación de la interfaz es uno de los aspectos que se elimina cuando los tiempos empiezan a comprometerse o directamente se la evita desde la planificación inicial del proyecto. Esto es un gran error. La evaluación siempre es necesaria, aunque se tenga poco tiempo y se considere que es un proceso que requiere demasiados recursos. El plan de evaluación debe ir acorde a la etapa de diseño en la que se encuentre la interfaz y puede adaptarse a los presupuestos y plazos de los que dispongamos.

La evaluación de la interfaz debe realizarse en diferentes etapas del proceso de diseño para identificar problemas y mejorar la usabilidad. Esto permite ajustar la interfaz a las necesidades de los usuarios y garantizar que el producto final sea efectivo y eficiente. Además, la evaluación continua ayuda a identificar áreas de mejora y asegurar que la interfaz se mantenga actualizada y relevante a lo largo del tiempo.

Como ya vimos en el planteamiento de la metodología de diseño centrado en el usuario existe una fase concreta para la evaluación, después del planteamiento de la solución de diseño y antes de la implementación del desarrollo, y otra para la monitorización en la que se obtienen datos del comportamiento de los usuarios con el producto. En esos dos momentos se obtienen evidencias que permiten mejorar el diseño para mejorar la experiencia del usuario con el producto.

Dado que la usabilidad de un interfaz a veces es una cualidad demasiado abstracta, habitualmente se divide su concreción en estos 3 atributos:



- **Facilidad de aprendizaje**  
  Está dado por la facilidad con que los usuarios puedan realizar las tareas en el sistema. Cómo de fácil les resulta aprender a manejar el sistema considerando los diferentes momentos de conocimiento de cada tipo de usuario.
- **Facilidad de uso**  
  Facilidad con la que el usuario hace uso de la herramienta, con menos pasos o más naturales a su formación específica. Tiene que ver con la eficacia y eficiencia de la herramienta. Cuántos pasos hacen falta para hacer una tarea.
- **Satisfacción tras el uso**  
  Medida en que los usuarios están satisfechos con los objetivos logrados una vez terminada la interacción con la interfaz.



Podemos establecer una clasificación de diferentes métodos de evaluación dependiendo de los tipos de datos que generan y el enfoque que establezcamos:



- **Métodos cuantitativos**  
  Persiguen recopilar grandes volúmenes de datos numéricos y métricas con los que validar la interfaz. Cuando estamos validando un producto que utilizan muchos usuarios podemos obtener cantidades altas de datos en un espacio corto de tiempo.
- **Métodos cualitativos**  
  Se centran en comprender las necesidades opiniones y motivaciones de los usuarios a menudo mediante la observación de la interacción en directo o en diferido. Al igual que vimos en los tipos de investigación en experiencia de usuario los métodos cualitativos generan resultados pequeños, pero no por eso menos valiosos.
- **Métodos de usabilidad**  
  Son aquellos que evalúan exclusivamente la facilidad de uso de la interfaz y la eficiencia que tiene el producto o el servicio. Para poder aplicarlos es necesario que tengamos un producto terminado o un prototipo funcional.
- **Métodos de investigación**  
  Exploran creencias, expectativas, necesidades o hipótesis en las primeras fases de creación del producto.



A continuación, vamos a profundizar en los principales métodos de evaluación de interfaces para que los conozcas en detalle y los puedas utilizar cuando estés desarrollando un producto digital.



#### Datos y uso de navegación



Este tipo de análisis se basa en el uso que hacen los usuarios de páginas o apps reales a través del seguimiento por medio de diferentes herramientas que registran las interacciones con una interfaz. El análisis de datos y de navegación es un método cuantitativo tremendamente valioso ya que proporciona información objetiva sobre el comportamiento real de los usuarios.

Para registrar esta información es importante disponer del consentimiento del usuario y hacerlo de forma transparente y respetuosa. En algunos casos la aceptación de las cookies está permitiendo al sistema registrar datos personales y de comportamiento entre otros.



#### Google Analytics:



- **De usuario**  
  Ofrece datos totales de los usuarios que han interactuado con el sitio, los que han tenido una sesión activa en un periodo de tiempo determinado, los que interactúan por primera vez o los usuarios recurrentes que lo hacen a menudo.
- **De sesiones**  
  Podemos conocer el número total de sesiones en un período, el promedio de sesiones por usuario y la duración media de la sesión.
- **De eventos**  
  Los eventos son cada una de las interacciones específicas que hace el usuario con la web. Google Analytics ofrece datos como el número total de eventos o la relación de estos con acciones determinadas como pueden ser una compra o un registro. Ofrece la posibilidad de tener identificadores de cada acción como el click o la página vista entre otros.
- **De páginas y pantallas**  
  En este tipo de métricas sabremos las vistas que ha tenido una página, el promedio de páginas vistas por sesión o la tasa de rebote, concepto referido a una sesión en la que el usuario solamente ha visto una página y ha abandonado la web.
- **De adquisición de tráfico**  
  Es importante saber por qué medio llega a los usuarios a nuestro sitio Y Google analytics nos los detalla entre orgánico, que es el proveniente de búsquedas, social, el que llega por redes sociales o directo que son los usuarios que teclean directamente la URL en un navegador. También ofrece información sobre campañas de marketing que tengamos activas para de ese modo medir su efectividad.
- **De comercio electrónico**  
  Si conectamos nuestra tienda online A Google analytics tendremos datos del número de transacciones, el valor medio por pedido, los ingresos totales, qué productos han visto más los usuarios o cuáles han añadido al carrito.
- **Otras métricas**  
  Dispondremos de datos relativos al tipo de dispositivo, al navegador o al sistema operativo de los usuarios. Cuando estos naveguen con la sesión de Google abierta o desde Android o Chrome, Analytics ofrecerá datos demográficos como la edad, el sexo o la ubicación geográfica.



#### Pruebas A/B



Se trata de un experimento aleatorio y en tiempo real que utiliza dos o más variantes de la misma página web (A y B). Cada variante se publica en momentos parecidos para que su rendimiento se pueda observar y medir independientemente de otros factores externos.

Es importante tener claro qué se quiere medir (objetivo) para poder evaluar cada una de las versiones. Las pruebas A/B resultan especialmente útiles para evaluar comparativamente variaciones del diseño como: cambios de posición de los elementos, cambios de tamaño/color, variaciones en los rótulos, pequeñas modificaciones de layout...

Este tipo de pruebas ayudan a los equipos de UX a determinar las mejoras en la experiencia de usuario que mejor se adaptan a sus objetivos comerciales. Les permiten tomar decisiones basadas en datos que suelen ser más fáciles de comunicar a las partes interesadas que los métodos cualitativos.

En el siguiente video vamos a aprender cuáles son los pasos para ejecutar un test A/B y veremos algunos ejemplos:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_FUUX_A/content/_652066_1/scormcontent/assets/INSD_FUUX_U3_Apartado4_Video1.mp4?v=1)



#### Card Sorting



El card sorting o clasificación de tarjetas es una técnica de validación e investigación de usuarios que se utiliza para comprender cómo los usuarios categorizan y ordenan la información de un producto digital en base a su modelo mental. El objetivo es asegurarnos la mejor forma de plantear el acceso y la navegación a través de la ingente cantidad de información que puede albergar un producto digital. Esta técnica es útil para definir o validar la arquitectura de la información de un sitio web, aplicación u otro producto digital.

El procedimiento consiste en solicitar a los participantes que organicen una serie de tarjetas, cada una con un concepto o elemento de contenido o información, en grupos que tengan sentido para ellos. El participante realiza el ejercicio de modo individual, nunca en grupo, y puede disponer del todo el tiempo que necesite dentro de lo razonable.

Tipos de card sorting:



- **Abierto**  
  Los participantes hacen libremente tantos grupos de tarjetas como quieran.
- **Cerrado**  
  Se definen previamente una serie de grupos o categorías, y el participante debe ubicar cada tarjeta en aquella categoría que crea mejor representa el concepto.
- **Híbrido**  
  Combina los dos tipos anteriores ya que, aunque hay algunas categorías establecidas, el usuario también puede crear las que considere.



Aunque tradicionalmente el ejercicio de Card Sorting se ha realizado de modo físico con tarjetas de cartulina, desde hace ya unos años existen procedimientos digitales que nos agilizan tremendamente el proceso y nos permiten abaratar costes y tiempos. En online utilizamos software específico de experiencia de usuario como Optimal Workshop [https://www.optimalworkshop.com/](https://www.optimalworkshop.com/), UX Tweak [https://www.uxtweak.com/](https://www.uxtweak.com/) o kardSoft [https://kardsort.com/](https://kardsort.com/) entre otros. Este tipo de plataformas suelen tener modelos de suscripción y también ofrecen posibilidad de usarlas de modo gratuito.



1
2
3
4
5
6

Con respecto al procedimiento para realizar un ejercicio de card sorting podemos establecer los siguientes pasos:

COMENZAR
1
Preparación de las tarjetas

Ya sea en físico o en digital el primer paso es decidir cada uno de los elementos de contenido que Irán en cada tarjeta. Podríamos hacer tarjetas con elementos como “catálogo”, “contacto”, “productos y servicios” o “departamentos” dependiendo del objetivo y la temática de nuestro producto. Es importante remarcar que no colocamos acciones sino contenidos o información, Por eso evitamos hacer tarjetas con textos como “imprimir catálogo” o “enviar formulario de contacto” ya que esos son acciones que suceden sobre el contenido y lo que buscamos en este ejercicio tiene que ver con la estructura.

En la siguiente imagen puedes ver un ejemplo de tarjetas físicas utilizadas para un card sorting real del sitio web de una universidad.

2
Decidir el tipo de card sorting

Ya hemos visto que podemos hacer uno abierto en el que los usuarios pueden hacer todos los grupos que quieran o cerrado en el que definimos unos grupos específicos y los usuarios colocan las tarjetas en ellos. Incluso uno híbrido que mezcla los dos.

3
Reclutamiento de participantes

Las personas que participen en el experimento tienen que adaptarse a nuestro público objetivo y para ello en la unidad anterior aprendimos un recurso que nos puede resultar de utilidad. En el “user persona” construimos un arquetipo ficticio de nuestro usuario que ahora nos puede servir de referencia para reclutar participantes que se le parezcan. Veamos un ejemplo: si nuestro user persona era mujer, tenía 30 años, vivía en un pueblo y estaba interesada por los animales No es buena idea que el card sorting lo realicen hombres mayores y que sean urbanitas porque su modelo mental de organización de información será distinto.

En cuanto al número de participantes estamos ante una técnica más cualitativa que cuantitativa y por ello buscaremos en torno a 15 personas para el experimento.

4
Preparación de los materiales

Si realizas el card sorting físico tendrás que:

Imprimir las tarjetas en papel o cartulina.

Concretar día y hora con cada participante.

Fotografiar o documentar de algún modo el resultado de cada ejercicio.

Si lo haces online tus tareas serán:

Elegir la plataforma y adquirir licencias o usar una versión gratuita. A menudo las versiones gratuitas están limitadas en funcionalidades o número de participantes.

Crear el ejercicio en la plataforma.

Enviar el enlace a cada participante.

5
Realizar el ejercicio

Explica en detalle a los participantes que tienen que organizar las tarjetas en grupos siguiendo su criterio y que no hay una ordenación buena y otra mala, lo que se busca es aplicar el modelo mental de cada persona. Recuerda que no tienen límite de tiempo y que no se les juzgará por ello ya que pueden tomarse el tiempo que necesiten.

Si lo estás haciendo en modo presencial puedes pedirles que piensen en voz alta mientras lo hacen, pero con cuidado de no condicionar sus acciones. En online puedes considerar un formulario final en el que te den información sobre cómo se han sentido o si han tenido alguna dificultad.

6
Analizar los resultados

Tanto en físico como en digital tendrás que analizar los resultados obtenidos y encontrar patrones de ordenación que te ayuden a tener conclusiones sobre la ordenación del sistema. Habrá agrupamientos que hayan sucedido más veces y serán esos los que deberás tener en cuenta para tú producto.

En esta en esta imagen ves un ejemplo de cómo una plataforma online de card sorting ofrece las agrupaciones más recurrentes en base a los ejercicios realizados por los usuarios. Este tipo de gráficos son más sencillos de obtener en un experimento online que en un presencial donde deberás utilizar métodos más artesanales para generarlos.



Card sorting ayuda a los diseñadores a:



- **Comprender cómo los usuarios piensan sobre la información**  
  Descubrir los modelos mentales que los usuarios tienen para diferentes tipos de información. Esos datos se pueden utilizar para concretar el diseño de la arquitectura de información, la navegación y el etiquetado.
- **Identificar áreas de confusión**  
  Sirve para identificar áreas donde los usuarios tienen dificultades para categorizar la información. Mejora la claridad y organización del contenido.
- **Priorizar el contenido**  
  Identificar qué elementos son más importantes para los usuarios y qué elementos es más probable que se confundan entre sí.



El resultado de una investigación o validación con card sorting es lo que llamamos un diagrama de sitio o mapa web que es la representación esquemática de toda la información que tiene el sistema. Como puedes ver en la siguiente imagen en un diagrama se plasma la relación que existe entre las diferentes partes desde un punto de vista estructural ya que no tiene que condicionarnos a la hora de plantear el diseño visual.



![image](assets/cm8vs468w01ee356yjhkb58ou-Imagen4.jpg)



#### Tree testing



Un tree test se encarga de evaluar la categorización jerárquica de un árbol de contenidos, haciendo que los usuarios encuentren categorías específicas dentro de él para completar determinadas tareas. A diferencia de las pruebas de usabilidad tradicionales, el tree test se enfoca en la estructura de la información y no en el diseño visual.

En este video vamos a ver en detalle a lo que se enfrenta un usuario en una prueba de Tree Test y a conocer los resultados que nos genera la plataforma.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_FUUX_A/content/_652066_1/scormcontent/assets/INSD_FUUX_U3_Apartado4_Video2.mp4?v=1)



Entre las ventajas de realizar experimentos de Tree Testing podemos encontrar las siguientes:

- Detectar problemas críticos de navegación y estructura de la información en una etapa muy temprana del proyecto.
- Generar los errores previos que pueden tener los usuarios antes de lanzar el producto y así tener opción de corregirlos antes de avanzar en el desarrollo.
- Aporta datos cuantitativos sobre tareas concretas.
- Se trata de un ejercicio rápido y razonablemente barato que se realiza sin moderación.



#### Mapas de calor



El mapa de calor o también llamado “heatmap” es un tipo de representación analítica utilizado para visualizar datos. En usabilidad los mapas de calor pueden ser de visualización, de click o de movimiento.

Los colores indican las zonas de mayor acción para el usuario. Al igual que con una cámara de imagen térmica, los colores representan diferentes grados de temperatura en las que las áreas donde los usuarios interactúan más se muestran en colores cálidos (rojo, naranja, amarillo), mientras que las áreas con menos interacción se muestran en colores fríos (verde, azul).



![image](assets/cm8vsb83q01ip356y9fse93lo-Imagen5.jpg)



Los mapas de calor sirven para identificar las áreas de interés y mostrar qué elementos del sistema atraen más la atención de los usuarios. También son útiles para detectar problemas de usabilidad ya que nos informan de las áreas donde los usuarios tienen dificultades para interactuar o encontrar información que creemos relevante. Ayudan a los diseñadores a tomar decisiones basadas en datos sobre la ubicación de elementos importantes, como botones de llamada a la acción o menús de navegación, optimizando así la estructura y disposición de la página.

Al identificar los puntos débiles de una página web los mapas de calor pueden contribuir a mejorar la tasa de conversión guiando a los usuarios hacia los objetivos deseados de manera más efectiva.



#### Eye Tracking



Es un método de análisis ampliamente utilizado en el mundo de la publicidad y cuya popularidad en la validación de interfaces ha ido aumentando. Este sistema utiliza equipos especiales, habitualmente presentes en laboratorio, que registran, graban y procesan el movimiento de los ojos y las fijaciones de los usuarios.

Con el software apropiado y basándose en la duración y la frecuencia con la que las personas participantes en la prueba fijan la mirada en ciertos elementos es posible crear un mapa de calor clásico como los que vimos anteriormente.



![image](assets/cm8vsdd8o01la356yec7pmllg-Imagen6.jpg)



#### Escala SUS



Un **Sistema de Escalas de Usabilidad** o simplemente **SUS** por sus siglas en inglés *(System Usability Scale)* es una herramienta metodológica que se usa para medir la usabilidad de un objeto, dispositivo o aplicación.

Aunque esta escala es extraordinariamente simple de usar, diferentes pruebas han demostrado que los resultados obtenidos a partir de la misma suelen ser muy confiables y acertados, razón por la cual es uno de los métodos de medición de usabilidad más utilizados en experiencia de usuario.



1
2
3

El procedimiento de trabajo es sencillo, pero para que sus resultados sean correctos es importante ajustarnos a la metodología establecida y no generar innovaciones sobre ella.

Los pasos que tenemos que realizar son:

COMENZAR
1

En primer lugar, presentamos el sistema, objeto, dispositivo o aplicación que deseamos medir a los usuarios de prueba.

2

Ofrecemos un cuestionario que deben realizar y que tiene que contener las siguientes 10 preguntas redactadas de modo literal:

1)      Creo que me gustaría utilizar este sistema con frecuencia

2)      Encontré el sistema innecesariamente complejo

3)      Pensé que el sistema era fácil de usar

4)      Creo que necesitaría el apoyo de un técnico para poder utilizar este sistema

5)      Encontré que las diversas funciones de este sistema estaban bien integradas

6)      Pensé que había demasiada inconsistencia en este sistema

7)      Me imagino que la mayoría de la gente aprendería a utilizar este sistema muy rápidamente

8)      Encontré el sistema muy complicado de usar

9)      Me sentí muy seguro usando el sistema

10)   Necesitaba aprender muchas cosas antes de empezar con este sistema.

La contribución de cada pregunta valdrá entre 1 y 5 en base a la siguiente escala de respuestas:

Totalmente en desacuerdo

En desacuerdo

Neutro

De acuerdo

Totalmente de acuerdo

Si el usuario no se siente capaz de responder a alguna cuestión en particular, habrá de señalar el valor central de la escala (3, neutro)

3

Sumamos los resultados promediados obtenidos de los cuestionarios realizados a nuestros usuarios considerando lo siguiente:

Las preguntas impares (1,3,5,7 y 9) tomarán el valor asignado por el usuario, y se le restará 1.

Para las preguntas pares (2,4,6,8,10), será de 5 menos el valor asignado por nuestros entrevistados.

Una vez obtenido el número final, se lo multiplica por 2,5.

El máximo teórico es de 100 puntos (valor global del SUS).

Tras un estudio realizado en más de 500 webs y aplicaciones, Jeff Sauro
(se abre en una nueva pestaña)
 concluye que el puntaje promedio es 68. Un resultado por debajo de esta cifra indica que hay varios aspectos a corregir y analizando las respuestas obtenidas tendremos información para acometer las mejoras.



Aunque las puntuaciones SUS varían de 0 a 100 no deben interpretarse como porcentajes. Una puntuación de 70 no significa que la aplicación tenga un 70% de usabilidad. De hecho, 70 es un valor cercano al promedio de 68, lo que sugiere que el sistema digital está en un nivel de usabilidad promedio, no por encima del promedio como podría interpretarse erróneamente.

Para evitar confusiones, especialmente al comunicar los resultados a personas no familiarizadas con las escalas SUS, es recomendable convertir las puntuaciones brutas a percentiles. De esta manera, una puntuación de 70 se traduciría a su percentil correspondiente, que en este caso sería alrededor del 50%, reflejando su posición en relación con otras puntuaciones.

Al presentar los resultados del SUS, es importante enfatizar que la escala no es un porcentaje y explicar claramente el significado de los percentiles. Esto garantizará que las partes interesadas comprendan correctamente el nivel de usabilidad del sistema evaluado y evitará interpretaciones erróneas.



## 4. Interfaces Móviles



### 4.1 Introducción



![image](assets/cm8vvb79k0004356xnmjssqxa-stock-image.jpg)



En este apartado vamos a ver como el diseño y trabajo con interfaces móviles presenta un reto para los desarrolladores de productos digitales derivado de la limitación del espacio, los diferentes contextos de uso que tienen los productos y el paradigma de la interacción táctil que es muy diferente al de ordenador.

El conocimiento de las áreas de interacción y lectura más efectivas nos ayudará a comprender como la localización de los elementos afecta a la usabilidad. Desde el punto de vista de la interacción del usuario aprenderemos la denominación y uso de los gestos táctiles más habituales en este tipo de diseños. Exploraremos los principios y patrones de la usabilidad móvil que nos servirán de marco de referencia a la hora de crear interfaces intuitivas y de fácil uso ya que al ponerlos en práctica estamos utilizando referencias conocidas por los usuarios y haciendo que su curva de aprendizaje del sistema sea mucho menor.



### 4.2 Interacción móvil



Para profundizar en los interfaces móviles empezaremos comprendiendo como es el paradigma de interacción que nos ayudará a entender los desafíos y oportunidades que entraña el desarrollo para smartphones.

El disponer de un tamaño reducido de pantalla hace que sea crítico aprender a optimizar la disposición de la información y saber que cada área del móvil tiene un diferente nivel de facilidad para la interacción del usuario.  Los gestos táctiles tienen un papel fundamental en la interacción móvil ya que son los que permiten que las personas usen los interfaces de modo intuitivo y eficiente. Conocer y aplicar estos gestos en tu día a día te permitirá desarrollar productos digitales con una usabilidad y experiencia de usuario satisfactoria.



#### Áreas



En un estudio de investigación del año 2020 ([https://doi.org/10.3233/WOR-203095](https://doi.org/10.3233/WOR-203095)) realizado en la Universidad de Nuevo León en Monterey, México, en el que se investigaban los cambios morfológicos asociados a la sujeción de los smartphones, se realizó una encuesta entre estudiantes universitarios para determinar los modos más habituales de utilización del móvil.

En la siguiente imagen puedes ver cuáles fueron esas 6 técnicas de sujeción de teléfonos inteligentes.



![image](assets/cm8vvg6wt003g356x4hzvr3tk-Imagen8.jpg)



A diferencia de los interfaces de escritorio u otros dispositivos digitales, el uso de los interfaces móviles está condicionado por dos aspectos que suelen escaparse de nuestro control como desarrolladores de sistemas. Se trata de:



- **El tamaño de la mano y los dedos del usuario**  
  Así como en interfaces de escritorio todos los usuarios transforman su movimiento del ratón en un cursor siempre del mismo tamaño, en un smartphone los dedos hacen las veces de cursores y la forma de sujetar el dispositivo condiciona la efectividad para acceder a la información. El modo de usar el sistema está condicionado por el tamaño de la mano del usuario.
- **Las dimensiones del dispositivo**  
  En un mercado con una gran variedad de marcas y modelos de teléfonos inteligentes, a menudo las personas eligen su teléfono dependiendo del tamaño en relación con las dimensiones de sus manos.



Si bien las seis formas de sujetar un móvil que vimos antes no son las únicas, en la siguiente imagen conoceremos algunas otras con las que probablemente te verás identificado en alguna de ellas.



![image](assets/cm8vviwok006m356x37b2fstu-Imagen9.png)



En la imagen anterior ves que aparecen 3 colores que nos indican el grado de facilidad de acceder a ellos dependiendo de la forma en la que sujetemos el dispositivo.



- **Verde: acceso fácil**  
  Esta zona corresponde a menudo al centro y la parte inferior central de la pantalla y es la más accesible para el pulgar. Suele ser donde se encuentran los botones de navegación o los gestos principales. También las esquinas inferiores son fáciles de alcanzar con el pulgar y se utilizan a menudo para realizar acciones como volver atrás o cambiar de aplicación. Es interesante colocar los elementos interactivos al alcance de los pulgares.
- **Amarillo: acceso medio**  
  Esta zona se extiende hacia los lados y en la parte media superior de la pantalla, los elementos son accesibles, aunque requieren un pequeño estiramiento del pulgar para llegar a ellos. Es una zona correcta para situar elementos secundarios a la navegación o de uso menos frecuente.
- **Rojo: acceso difícil**  
  Se trata de la zona más alejada del alcance del pulgar y corresponde a la parte superior y a las esquinas de la pantalla. Hay que tratar de evitar el situar elementos importantes en esta zona ya que porque son difíciles de alcanzar para usuarios con dedos cortos y pantallas grandes. En esta zona roja se suelen colocar contenidos menos importantes como son los ajustes o informaciones secundarias.



Es importante conocer cómo las personas sujetan los dispositivos ya que eso condiciona la facilidad o dificultad de acceso para información y a cómo tendremos que colocarla dentro de nuestra propuesta de interfaz y dependiendo del contexto de uso. Viendo la imagen anterior podemos deducir que dependiendo de si el uso es con una mano o con dos esas zonas serán diferentes

Con respecto a la lectura y visualización de los contenidos tenemos que saber que lo que parezca en la parte central y en la mitad superior de la pantalla es más fácil de ver que el contenido en la mitad inferior donde puede ser bloqueado por las manos o ignorado.



#### Gestos



A diferencia de los interfaces de escritorio donde la interacción está supeditada al uso del ratón y el teclado en los dispositivos táctiles aparece un nuevo paradigma en la forma en la que los usuarios se relacionan con el dispositivo, crean contenido y acceden a la información.

En la siguiente imagen mostramos las principales formas de interacción sobre una pantalla táctil generadas con uno o dos dedos y que dependiendo de la presión, número o movimiento de estos realizan acciones diferentes.



![image](assets/cm8vvmyu800b5356xt7ytub7e-Imagen10.jpg)

- **Pulsar (tap)**  
  Un toque rápido en la pantalla se usa para abrir aplicaciones o seleccionar elementos.
- **Doble toque (double tap)**  
  Realizar dos toques rápidos y consecutivos suele realizar un zoom sobre una imagen, texto o pantalla completa.
- **Pulsar y mantener (press and hold)**  
  Manteniendo pulsado el dedo sobre la pantalla se accede a funciones adicionales o menús contextuales relacionados con un elemento.
- **Deslizar (swipe o flick)**  
  Consiste en desplazar el dedo sobre la pantalla y se usa para diferentes acciones entre las que están navegar o eliminar elementos
- **Pellizcar (pinch o stretch)**  
  Juntando o separando dos dedos sobre la pantalla es posible ampliar o reducir una imagen o la pantalla completa
- **Deslizamiento vertical u horizontal (vertical slide y horizontal slide)**  
  Es uno de los gestos más habituales en interacción móvil. Similar a swipe pero con un recorrido específico en horizontal o vertical. Se emplea para deslizar el contenido y navegar, ver las imágenes de una galería de fotos o moverse entre los elementos de una lista.
- **Agitar (shake)**  
  Dependiendo del sistema operativo y de la aplicación tiene acciones diferentes, aunque los más habituales son deshacer, borrar o reportar un error. Si quieres probarlo puedes abrir la app de Instagram desde tu móvil, agitarlo y verás que te aparece la pantalla de informar de un problema.



### 4.3 Principios y patrones de usabilidad móvil



#### Principios



Los principios de usabilidad móvil son un conjunto de recomendaciones y normas que tienen como objetivo que los usuarios tengan una experiencia agradable al utilizar los sistemas digitales como aplicaciones o sistemas operativos de smartphones o tablets. Vamos a conocer cuáles son los principios más relevantes para que los tengas presentes cuando tengas que desarrollar un producto digital móvil.



#### Tender a la simplicidad



La simplicidad es algo valioso en cualquier interfaz, pero tiene una importancia máxima cuando las pantallas son pequeñas, la interacción únicamente es táctil y los usuarios pueden estar en movimiento o distraídos realizando otras actividades.

La interacción táctil requiere que los elementos de interfaz tengan el suficiente espacio entre ellos para que no se cometan errores al manipularlos y para ello la simplicidad en el sistema es algo primordial. Lo mismo sucede con el contexto en el que puede encontrarse el usuario ya que muchos de ellos utilizan los móviles cuando se desplazan y eso requiere interfaces muy fáciles de usar en las que encontrar rápidamente las acciones principales. Una interfaz simple reduce la carga cognitiva necesaria para realizar una acción ya que la persona tiene menos elementos qué procesar.

Para aplicar simplicidad podemos considerar los siguientes aspectos:



- **Reducir los textos a su mínima expresión**  
  La presencia de demasiado texto en una aplicación genera fatiga al usuario que normalmente en lugar de leer escanea la pantalla. Mide cada palabra y cada letra y busca siempre la opción más corta y sencilla. Casi siempre podemos encontrar una alternativa más breve. Utilizar un lenguaje sencillo y evitar expresiones técnicas hará que los usuarios entiendan mejor lo que pueden hacer dentro de la aplicación.
- **Diseño minimalista**  
  Esta característica ya aparecía en los principios de la usabilidad de Jakob Nielsen y tiene especial importancia en dispositivos móviles. Genera espacios en blanco en los que la vista del usuario pueda descansar y que servirán para diferenciar las partes que componen el sistema. Busca la jerarquía de los elementos para que se perciban según la importancia que tienen. Si vas a utilizar elementos decorativos piensa si van a aturdir o despistar al usuario.
- **Centrarse en la funcionalidad**  
  Aunque el diseño visual es importante recuerda que en una aplicación móvil la funcionalidad está por encima de la forma y por eso las funciones principales tienen que estar lo suficientemente claras y que no las eclipse el diseño. Prioriza las acciones principales que realizarán los usuarios con el sistema y elimina o reduce las características innecesarias.
- **Navegación y estructura sencilla**  
  Moverse por una aplicación no siempre es sencillo y menos cuando tiene tantas partes que no somos conscientes de la dimensión de lo que tenemos entre manos. Usa una arquitectura de la información contenida y sin demasiada profundidad, y organiza la información de forma entendible y lógica para los usuarios. Trata de emplear patrones de navegación con los que estén familiarizados y que sean fáciles de comprender y recordar.



![image](assets/cm8vw01j500lh356xytb3nank-Imagen12.png)



#### Elegir bien los clics to action



Desde el punto de vista del diseño de interacción una de las dificultades que tenemos en la usabilidad móvil es informar al usuario sobre qué elementos se puede pulsar y sobre cuáles no. En interfaces de ordenador el cursor transforma la flecha en la mano y de ese modo el usuario es consciente de que algo es pinchable, pero eso es algo que no sucede en pantallas táctiles. Por esta razón es muy importante elegir bien sobre qué elementos el usuario podrá hacer clic y desencadenar una acción, los que llamamos clic to action o llamada a la acción.

En el siguiente vídeo vamos a ver un ejemplo práctico en el que el rediseño de los elementos de interacción de una app hace que mejore su usabilidad.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_FUUX_A/content/_652066_1/scormcontent/assets/INSD_FUUX_U3_Apartado5_Video1.mp4?v=1)



#### Vuelta a la portada



En todos los sistemas digitales hay que considerar la portada como un elemento más de la navegación, pero es en los dispositivos de pantalla pequeña donde este elemento cobra una importancia primordial. El usuario debe tener visible la opción de volver al punto de partida, que habitualmente suele ser la portada, y no depender de los botones de regresar para deshacer su camino.



![image](assets/cm9s66o740065357crpqza9es-imagen_2013.jpg)



#### Diseñar a una columna



Diseñar a una columna es el estándar actual en interfaces móviles, ya que los usuarios están acostumbrados a él, pero también es la forma más eficiente de colocar los elementos y que nos permite ofrecer la misma experiencia a usuarios con diferentes resoluciones en sus dispositivos. Esta forma de trabajar simplifica el proceso de diseño y desarrollo ya que no necesita adaptarlo a los distintos anchos de pantalla.

También es un aspecto que facilita la lectura y la navegación empleando la verticalidad de la pantalla para hacer scroll con los dedos de forma más intuitiva. El diseño a una columna permite priorizar el contenido sobre otros elementos menos importantes, debido a que no hay espacio para estos, y consigue apps más efectivas.



![image](assets/cm9s69cj4008g357cuzg46x2j-imagen_2014.jpg)



#### El contenido en el medio



Colocar el contenido en el centro es un principio de diseño que busca la optimización del espacio de la pantalla. La zona central es la más accesible con el pulgar cuando el usuario sostiene el móvil con una mano y de esa forma puede acceder al contenido principal.

Desde un punto de vista visual el contenido centrado provoca una sensación de equilibrio que resulta más agradable a la vista y que ayuda al usuario a dirigir su visión hacia la información más importante y a comprender mejor el sistema.

Con esta estructura se relegan los extremos de la pantalla para acciones secundarias a las que el usuario tiene que realizar un esfuerzo mayor para llegar a. Por ejemplo, la colocación de elementos de configuración, perfil o alertas suelen ser en la parte superior mientras que la parte central sirve para mostrar el contenido.

Esta práctica es una estrategia de diseño que prioriza la ergonomía generando un equilibrio visual Que revierte en una mejor usabilidad y experiencia de usuario.



![image](assets/cm9s6bmhk00aa357ch9ntc33d-imagen_2015.jpg)



### 4.4 Patrones



Un patrón de interacción es un resumen práctico de una solución de diseño que se ha demostrado que funciona más de una vez. Es importante utilizarlos como guía ya que son soluciones conocidas por los usuarios y sobre las que existen evidencias de su utilidad. El utilizar patrones de interacción genera experiencias más intuitivas que reducen el esfuerzo al usuario.

A continuación, vamos a conocer los principales patrones en interacción móvil que nos ayudarán a desarrollar interfaces más eficientes.



#### Splash Screen



La bienvenida siempre es importante, y una buena splash screen puede marcar el camino a una buena experiencia. Llamamos así a la pantalla de presentación que se muestra al abrir una aplicación y que de algún modo “saluda” o introduce al usuario en el producto que quiere utilizar. Es el primer punto de atención del usuario con el sistema y por eso suele tener un diseño elegante y sencillo, el logo con una breve animación y una estética conectada con la imagen gráfica de la marca. No suele durar más de 2 o 3 segundos y si los sobrepasara tendría un indicador de carga para que el usuario sepa qué es lo que está sucediendo.



![image](assets/cm8vwe80w016j356x0ryivaqf-Imagen16.png)



#### Íconos de menú



Las interfaces móviles tienen algunos elementos de interacción propios que, aunque son muy populares y seguro que los has visto en muchos sitios, puede que desconozcas cuál es su denominación. Vamos a dedicar el siguiente video a profundizar en los 5 tipos de iconos de menú.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_FUUX_A/content/_652066_1/scormcontent/assets/INSD_FUUX_U3_Apartado5_Video2.mp4?v=1)



La existencia de estos elementos de menú viene dada por la escasez de pantalla a la que nos enfrentamos cuando diseñamos para dispositivos móviles. Por eso estos iconos, basados en metáforas y conceptos reconocibles para los usuarios, son idóneos para ofrecer información o funcionalidades complementarias sin penalizar el espacio de la pantalla.



![image](assets/cm8vwmbxq019m356xfyyu2gk9-Imagen17.png)



#### Navegación por pestañas



Las pestañas o “tabs” se usan para filtrar contenidos o cambiar entre pantallas que, de acuerdo con la arquitectura de información, tienen el mismo nivel jerárquico, indicando siempre dónde se está y hacia dónde más se puede ir.

Entre las buenas prácticas a la hora de emplear una navegación por pestañas tenemos estas:

- Marcar siempre la pestaña seleccionada con resalte de tipografía o color.
- Mantener el orden y ubicación inicial.
- No usarlas para otras acciones diferentes a la navegación



![image](assets/cm8vwp5bq01bg356xe6z9pfzs-Imagen18.png)



#### Tab bar



El “tab bar” o “barra de pestañas” es un patrón de interacción móvil que se suele colocar en la parte inferior de la pantalla y que permite a los usuarios moverse entre las distintas secciones de la aplicación convirtiéndose en un acceso rápido y comprensible. Los ítems se mantienen en todo el sistema en el mismo lugar y así los usuarios no necesitan buscarlos.

Hay un número limitado de los que podemos poner, debido al ancho de la pantalla móvil, que suele ser un máximo de 5 aunque, como en el caso de X (antes Twitter) puedes ver en la imagen siguiente que han usado 6.



![image](assets/cm8vwqh3101da356xbq24rbx7-Imagen19.png)



Debido al fácil acceso de la zona inferior de la pantalla, como vimos cuando hablamos de las áreas de interacción, a menudo el centro de la tab bar puede servir para una acción principal. En el caso de Strava sirve para registrar una actividad o en el de Instagram para subir una publicación.



#### Navegación por listas



Cualquier contenido estructurado dispuesto verticalmente puede conformar una lista. Esta forma de mostrar tantos ítems como sea necesario permite al usuario tocar alguno de ellos para obtener información complementaria.

Esta solución resulta muy intuitiva ya que utiliza el principal modo de navegación sobre una página, que es el scroll vertical, considerando la lista completa como superficie interactiva sobre la que el usuario puede deslizar su dedo.



![image](assets/cm8vxd7xo01fv356xfcqplohr-Imagen20.png)



#### Botón de volver



A medida que el usuario va avanzando en profundidad de contenidos es necesario contar con una forma de retroceder o volver a niveles superiores. En el mundo móvil, con la navegación pantalla a pantalla, el uso del botón «volver» es muy frecuente. Normalmente se sitúa en la parte superior izquierda de la pantalla y tiene una presencia suficiente para que no pase desapercibido pero que tampoco moleste.

Es importante saber que, aunque hay sistemas operativos que ofrecen un botón de volver en la parte inferior, otros no lo hacen y esa vuelta se realice bien mediante gestos o usando botones que ofrecen las propias aplicaciones. De ahí su importancia.



![image](assets/cm8vxei5i01hp356xr4w7xehm-Imagen21.png)



## 5. El Futuro De Las Interfaces Y La Ux



### 5.1 Introducción



![image](assets/cm8vxg13n01it356xk1n18xs7-stock-image.jpg)



La computación espacial es una tecnología emergente que integra el mundo digital y en físico permitiendo a las personas interactuar con las máquinas de modo inmersivo y natural. Este concepto es muy relevante cuando hablamos del futuro de las interfaces y la experiencia de usuario ya que, si recuerdas, el interfaz era el puente con el cual las personas pueden operar y controlar a las máquinas y sus paradigmas, CLI, GUI, NUI o OUI, están en constante evolución

Exploraremos como la interacción tiene un gran reto bajo el concepto de tridimensionalidad y la ausencia de pantallas planas sobre las que posar texto, cursor y dedos, o la ausencia de ellas en interfaces sobre los que el usuario no dispone de los elementos y los tiene que descubrir.



### 5.2 Interfaces conversacionales



Llamamos interfaz conversacional a aquella que emplea la conversación, en texto o en voz, como conexión entre la persona y la máquina. Al no existir elementos gráficos, más allá del texto, la interacción se antoja más natural y conectada con la persona.

Los dos tipos principales de interfaces conversacionales son:



- **Chatbots**  
  Software que interactúa mediante el texto simulando una conversación real con una persona. Es habitual encontrarlos en redes sociales, tiendas online o aplicaciones de mensajería.
- **Asistentes de voz**  
  Son sistemas más avanzados que utilizando inteligencia artificial entienden el contexto y permiten no solo responder preguntas sino también realizar tareas. Según [Statista](https://es.statista.com/estadisticas/1012695/asistentes-virtuales-de-voz-mas-usados-en-espana/) en 2023 “Alexa encabezaba el ranking de los asistentes virtuales líderes en el mercado nacional con un 55,3% de usuarios, seguido de cerca por Google Assistant. Completaba el podio Siri, desarrollado por Apple, con más de un 33% de usuarios.”



![image](assets/cm8vxzpjp01lq356xzrf95uyr-Imagen22.png)



Para crear interfaces conversacionales tenemos que considerar aspectos como el diseño de la personalidad, tanto en texto como en voz, para que la experiencia sea atractiva y creíble. También es importante definir muy bien el flujo de la conversación para no caer en bucles y anticiparse a posibles interacciones del usuario. La velocidad de respuesta es un aspecto que concierne tanto a desarrolladores como a diseñadores y que sabemos que supone un punto de fricción importante cuando la conversación no transcurre al ritmo esperado.

Desde un punto de vista de ventajas e impacto para la experiencia de usuario las interfaces conversacionales cambian por completo el modo en el que las personas se relacionan con la tecnología. Estas son algunas de las principales ventajas para el usuario a la hora de utilizarlas:



- **Accesibilidad**  
  Los usuarios con alguna discapacidad motora o visual emplean la voz como modo de interacción con el sistema lo cual les permite tener una experiencia más eficiente e independiente.
- **Personalización**  
  Muchos de estos asistentes permiten generar experiencias únicas y crear conexiones muy cercanas con los usuarios. El uso reiterado de la asistente aprende de la persona y moldea las respuestas con un importante grado de adaptación a sus gustos
- **Convivencia con otras tareas**  
  Es un aspecto relevante sobre todo en los asistentes de voz que permiten emplearlos mientras conducimos, cocinamos o vemos la televisión. Los chatbots también permiten cierto grado de convivencia con otras tareas ya que funcionan como un robot con máxima paciencia a nuestros tiempos de espera.



### 5.3 Realidad virtual, aumentada y mixta



La realidad virtual (VR), la realidad aumentada (RA) y la realidad mixta (RX) representan un grupo de tecnologías que cambian el modo en el que los usuarios interactúan con la información y el mundo que les rodea. A pesar de que estos sistemas también son digitales, tanto su concepción, objetivo y uso son diametralmente opuestos a las que encontramos en ordenadores, móviles o tablets. En términos de usabilidad, el desafío está en crear interfaces intuitivas y experiencias fluidas que aprovechen las capacidades de cada tecnología y garanticen la comodidad y seguridad del usuario.

Vamos a descubrir brevemente lo que son cada una de estas realidades:

- La realidad virtual es una simulación interactiva por ordenador desde el punto de vista del participante en la cual se sustituye o se aumenta la información sensorial que recibe. Para acceder a ella es necesario un visor de VR, dispositivos de control y software especializado entre otros elementos.
- La realidad aumentada es una tecnología que añade elementos virtuales como imágenes, vídeos o gráfica que aportan algún tipo de información sobre objetos o posiciones reales. A diferencia de la realidad virtual la aumentada complementa el mundo real con información adicional. Aunque hay muchos ejemplos sobre esta tecnología socialmente se popularizó gracias al juego para móvil de Pokémon GO.



![image](assets/cm8vy7jdh01om356xoexxqcdq-Imagen23.jpg)



- La realidad mixta o híbrida es una tecnología que combina mundos virtuales con el mundo real. Permite combinar ámbitos reales y virtuales, es interactiva y en tiempo real y se puede registrar en tres dimensiones. Para experimentar este tipo de realidad también es necesario un visor, como en el caso de la virtual, con el que el usuario ve simultáneamente elementos virtuales integrados en el entorno real generando una experiencia realista a la vez que inmersiva. Dos de los dispositivos más populares de realidad mixta son Microsoft Hololens y Apple Vision Pro.



![image](assets/cm8vy9t4101pz356xs2zq1r2u-Imagen24.jpg)



Aunque cada una de estas tecnologías tiene características propias comparten algunas problemáticas y retos desde el punto de vista de la experiencia de usuario:



1
2
3
1
Diversidad de inputs

El relativo control del que disponemos en un entorno de ordenador o móvil con respecto a las formas de manejo del sistema nada tiene que ver con la variedad y complejidad que existe en estos nuevos entornos.

2
Nuevos esquemas espaciales

La forma habitual de trabajar en dos dimensiones y la posición del usuario con respecto al sistema nada tiene que ver con una experiencia en la que la información rodea a la persona y en la que existen diferentes capas con las que poder interactuar. Pasamos del concepto diseño para tocar o para observar, al de diseño que envuelve al usuario y se adapta a su realidad espacial.

3
Distancia física

La distancia entre la persona y los objetivos condicionan el tamaño, el color o la forma que deben tener los elementos de lectura o interacción. Venimos de trabajar en contextos que podemos denominar de proximidad entre los ojos y el sistema para adentrarnos en interfaces que pueden tener amplias distancias o situarse incluso a 360º alrededor del usuario.



### 5.4 Interfaces gestuales



Este tipo de interfaces son quizá el ejemplo más claro del paradigma natural NUI, y de una aproximación al orgánico OUI, Organic User Interface, debido a que la forma en la que interactuamos con la tecnología no depende de ningún periférico como un ratón coma un teclado o una pantalla táctil. En estas interfaces las máquinas atienden a las peticiones de los usuarios entendiendo y los gestos de las manos, las expresiones de la cara o los movimientos del cuerpo.

En estas interfaces las máquinas tienen asociados determinados movimientos a los que responden después de haberlos captado a través de cámaras o sensores. Acciones como maximizar una ventana ampliándola con los dedos sin necesidad de buscar un botón que indique que se hace grande o desplazar una ventana moviendo la mano de derecha a izquierda son comportamientos naturales e intuitivos que anulan la fricción interpretativa que a veces tiene una interfaz gráfica.

Podemos enumerar algunos retos y desafíos que tienen los interfaces gestuales por delante.



- **Accesibilidad**  
  En determinados contextos o para algunos usuarios pueden ser interfaces poco accesibles que no garantizan la usabilidad universal ya que no siempre las personas tienen el mismo nivel de capacidad motora de modo permanente o transitorio. Que no existan estándares gestuales como sí existen en las interfaces gráficas también es un problema de acceso.
- **Interacción por descubrimiento**  
  En este contexto el usuario no dispone de elementos sobre los que seleccionar y eso hace que toda la interacción tenga que ser descubierta lo cual genera una curva de aprendizaje importante.
- **Contexto físico y relacional**  
  Mientras esta tecnología sea minoritaria, su uso en público puede resultar algo incómodo como pasó con los primeros móviles. El sentirse observado también puede tener problemas de privacidad y seguridad debido a que alguien puede observarnos y replicar esos movimientos. Además, necesita de unas características de iluminación y movimiento muy concretas que en determinados contextos puede que no sean posibles.
- **Cansancio**  
  Cuando en la primera unidad hablábamos de tiempo y esfuerzo como dos elementos a tener en cuenta cuando un usuario interactúa con una interfaz nos referíamos al esfuerzo cognitivo. En el caso de los interfaces gestuales podríamos considerar el cansancio físico como un factor a tener en cuenta en la interacción del usuario con el sistema.
- **Precisión**  
  Las zonas interactivas o los periféricos que usamos en interfaces gráficos permiten cierto grado de imprecisión lo que hace una interacción más cómoda, algo que los interfaces gestuales requiere que exista un software altamente preciso. La falta de diferenciación entre los gestos intencionales del usuario y otros movimientos accidentales pueden provocar experiencias no satisfactorias.



Probablemente los avances tecnológicos de los próximos años solucionen estos retos y ofrezcan una experiencia de usuario fluida y amigable en contextos en los que la interacción gestual suponga una mejora para las personas.



## 6. Conclusiones



### 6.1 Conclusiones de la unidad



Como conclusiones a esta unidad didáctica podemos enumerar que el alumno dispone de conocimientos suficientes sobre:

- Métodos para validar interfaces en diferentes momentos del proceso de desarrollo y las herramientas principales que se usan en esta disciplina primordial en experiencia de usuario.
- Técnicas cuantitativas y cualitativas para medir la efectividad de los interfaces empleando tanto la participación de los usuarios como los datos que generan los sistemas tras su uso.
- Los principios generales de la usabilidad para dispositivos móviles que nos muestran el diferente enfoque que debemos tener cuando estamos trabajando en movilidad.
- Los principales patrones de diseño móvil nos servirán para desarrollar interfaces más efectivos y adaptados a los estándares habituales existentes en el mercado
- Las interfaces para áreas emergentes como conversacionales, realidad aumentada y virtual e interfaces gestuales tienen características propias que nos plantean importantes retos de diseño y desarrollo. Conocer la realidad de estas tecnologías nos ayudará a ser conscientes del futuro que está por venir.
- Trabajar con enfoque de usuario te hará ser un desarrollador mucho más competente ya que ahora eres consciente de la importancia de conocer el comportamiento, necesidades y características de las personas que van a utilizar los sistemas que desarrolles.
