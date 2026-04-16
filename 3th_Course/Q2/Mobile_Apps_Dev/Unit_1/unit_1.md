# Unidad 1. Base del desarrollo móvil con Android.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Impacto De Los Teléfonos Móviles En La Sociedad](#2-impacto-de-los-teléfonos-móviles-en-la-sociedad)
  - [2.1 Introducción](#21-introducción)
  - [2.2 El teléfono móvil y la sociedad](#22-el-teléfono-móvil-y-la-sociedad)
  - [2.3 Opciones de desarrollo móvil](#23-opciones-de-desarrollo-móvil)
- [3. Android](#3-android)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Historia](#32-historia)
  - [3.3 El sistema operativo](#33-el-sistema-operativo)
  - [3.4 Instalación y configuración del IDE](#34-instalación-y-configuración-del-ide)
  - [3.5 Conceptos básicos del desarrollo Android](#35-conceptos-básicos-del-desarrollo-android)
  - [3.6 Estructura de un proyecto Android](#36-estructura-de-un-proyecto-android)
  - [3.7 Kotlin](#37-kotlin)
- [4. Desarrollo Android](#4-desarrollo-android)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Activitys](#42-activitys)
  - [4.3 Eventos](#43-eventos)
  - [4.4 Gestión de estados](#44-gestión-de-estados)
  - [4.5 Internacionalización y uso de recursos múltiples](#45-internacionalización-y-uso-de-recursos-múltiples)
  - [4.6 Intents](#46-intents)
  - [4.7 Depuración de código](#47-depuración-de-código)
- [5. Conclusiones](#5-conclusiones)
  - [5.1 Conclusiones de la unidad](#51-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



Hoy en día, el uso de dispositivos móviles ha transformado radicalmente la forma en que interactuamos con la tecnología y el mundo que nos rodea. Este cambio ha impulsado la demanda de aplicaciones móviles, generando un campo de desarrollo con una demanda en el mercado muy importante y en constante crecimiento. El desarrollo móvil abarca diferentes posibilidades desde el punto de vista de sistemas para los que desarrollar, siendo Android e IOs los más demandados en el mercado

En esta unidad veremos cuales son todas las posibilidades que se pueden utilizar en el desarrollo móvil, tanto nativo como no nativo realizando un análisis detallado de cada una las plataformas, frameworks y herramientas que los desarrolladores pueden emplear. Desde el desarrollo nativo hasta las soluciones multiplataforma, pasando por las tecnologías emergentes como Progressive Web Apps (PWAs) y las opciones de desarrollo sin código. De todas estas posibilidades, haremos hincapié en el desarrollo nativo Android, con kotlin como lenguaje de programación, por lo que veremos su sintaxis uso y el desarrollo mediante el IDE oficial de Google Android Studio

Los apartados a tratar en esta unidad didáctica serán:



- **Impacto de los teléfonos móviles en la sociedad**  
  El desarrollo móvil se erige como una disciplina esencial para satisfacer las crecientes demandas de una sociedad cada vez más conectada y demandante. Los desarrolladores móviles desempeñan un papel fundamental en la creación de aplicaciones innovadoras que mejoran la eficiencia, simplificando tareas cotidianas y generando aplicaciones útiles válidas para multitud de campos. La capacidad de llegar a audiencias masivas a través de plataformas móviles ha posicionado al desarrollo móvil como una herramienta estratégica para empresas y organizaciones que buscan destacarse en el competitivo panorama digital.
- **Android**  
  El sistema operativo Android es uno de los más utilizados en el mundo, no solo por su carácter libre, sino también por su facilidad de uso y la gran cantidad de componentes ya desarrollados. Como toda compañía y/o tecnología que tiene a Google como propietaria, Android se ha convertido hoy en día en uno de los buques insignia del desarrollo móvil, teniendo una larga carrera en el desarrollo desde que fue fundada en 2008. Su núcleo Linux y la arquitectura del sistema operativo, hacen de Android una apuesta segura para el desarrollo. A lo largo de este apartado trataremos sobre la historia del sistema operativo, las versiones del mismo así como la arquitectura que soporta toda la ejecución del código.
- **Desarrollo Android**  
  Una vez ya tenemos claros cuales son los conceptos base del desarrollo móvil en Android y conocemos cual es la estructura base de un proyecto, podemos pasar a desarrollar. A lo largo de este punto aprenderemos a trabajar con Activities, el paso de datos entre ellas, asociar partes gráficas y lógicas, etc.



#### Objetivos



Los objetivos que se persiguen en esta unidad son:



1. Conocer la importancia del desarrollo móvil.
2. Conocer y diferenciar las diferentes tecnologías que permiten un desarrollo móvil.
3. Conocer la estructura del sistema operativo Android, así como las diferentes capas que permiten la interactuación entre el código y las librerías disponibles.
4. Conocer y manejar la estructura de un proyecto Android, diferenciando entre parte gráfica y parte lógica, manejando cada una de las vistas disponibles.
5. Conocer y manejar los diferentes tipos de eventos que existen dentro de Android y asociarlos de forma eficiente a las vistas.



## 2. Impacto De Los Teléfonos Móviles En La Sociedad



### 2.1 Introducción



![image](assets/cm6dvxkt8005a3570wdglj43i-stock-image.jpg)



En la última década, los dispositivos móviles han experimentado una expansión sin precedentes, convirtiéndose en elementos indispensables en la vida de millones de personas. Esta expansión ha redefinido la forma en la que las personas nos comunicamos, trabajamos, aprendemos y nos entretenemos. Este fenómeno ha generado una demanda exponencial de aplicaciones móviles, colocando el desarrollo móvil como un tipo de desarrollo muy a tener en cuenta en la industria tecnológica.

Esta importancia de las aplicaciones móviles ha florecido junto con la penetración de los dispositivos en la sociedad. Desde la productividad hasta el entretenimiento, las aplicaciones móviles se han convertido en elementos claves para la transformación digital de las empresas, la mejora de la eficiencia y la creación de entornos de trabajo cooperativos. La diversidad de aplicaciones disponibles abarca desde soluciones empresariales y educativas hasta plataformas de redes sociales y juegos, reflejando versatilidad de los dispositivos móviles en la vida moderna.

En este contexto, el desarrollo móvil se erige como una disciplina esencial para satisfacer las crecientes demandas de una sociedad cada vez más conectada y demandante. Los desarrolladores móviles desempeñan un papel fundamental en la creación de aplicaciones innovadoras que mejoran la eficiencia, simplificando tareas cotidianas y generando aplicaciones útiles válidas para multitud de campos. La capacidad de llegar a audiencias masivas a través de plataformas móviles ha posicionado al desarrollo móvil como una herramienta estratégica para empresas y organizaciones que buscan destacarse en el competitivo panorama digital.



### 2.2 El teléfono móvil y la sociedad



Como se comentaba en la introducción, el teléfono móvil hoy en día es uno de los elementos más importantes dentro de la sociedad y la vida cotidiana de todos y cada uno de nosotros. Si atendemos a cifras oficiales, según el INE el teléfono móvil está presente en el 99,5% de los hogares en España con miembros de entre 16 y 76 años, por encima del uso de conexión de banda ancha y muy lejos del resto de tecnologías del sector



![image](assets/cm6dw24wc009g357081tzl7wt-Imagen1.png)



Si nos fijamos en el gráfico anteriores, podemos ver que la tendencia del uso del teléfono móvil es contante e incrementa, a diferencia del resto de tecnologías, qué salvo el uso de banda ancha, tienen un uso cada vez menor y su tendencia no es ir hacia la desaparición o el desuso. Esto nos indica la importancia que tiene prestar especial atención a este tipo de tecnología y en concreto al desarrollo de aplicaciones destinada a los dispositivos destinada a cualquier ámbito. Si miramos los datos en números globales, podemos ver que, en todo el mundo, cerca del 70% de la población cuenta con un teléfono móvil con acceso a internet



![image](assets/cm6dw2scn00at3570mylzga3x-Imagen3.jpg)



Parece claro que este nicho de mercado es clave en el desarrollo tecnológico, por lo que entender y dominar las tecnologías que permiten el generar aplicaciones móviles es clave en el futuro de todo desarrollador. Antes de empezar a analizar cada una de las soluciones disponibles, es importante focalizar el uso de los teléfonos móviles teniendo en cuenta el sistema operativo para el que estará destinado el desarrollo. En la actualidad, aunque existen multitud de sistemas operativos, son dos los que tienen un uso dominante: IOs y Android. Estos dos sistemas operativos acaparan la mayoría de los teléfonos en el mundo, teniendo un número de 257 billones de descargas de app en el año 2023



![image](assets/cm6dw4nof00ci3570re5i2l0a-Imagen6.png)



Si diferenciamos ambos sistemas operativos, nos encontramos que Android es el sistema predominante en el mercado, con una penetración de mercado del 70%. De forma global, las cifras son las que se muestran, siendo reseñable que en estados Unidos el sistema operativo IOs es dominante sobre Android, con una penetración del 57% con respecto al 41% de Andriod



![image](assets/cm6dw5u3800dw35704j9fc4m0-Imagen7.jpg)



### 2.3 Opciones de desarrollo móvil



El mundo del desarrollo móvil ha sufrido avances muy grandes en los últimos años, siendo muchas las posibilidades existentes para poder crear app. Entre todas las tecnologías disponibles, podemos clasificarlas según la forma que tienen de generarse y como el código se ejecuta en el dispositivo. Entre todas las posibilidades encontramos:



- **Desarrollo Nativo**  
  Se trata de un desarrollo donde el código se ejecuta de forma directa dentro del dispositivo, sin necesidad de que lo ejecute una máquina virtual o un sistema intermedio. Al tratarse de una ejecución nativa, esta esmucho más rápida. La principal ventaja de este tipo de desarrollo es la capacidad de acceso al hardware sin necesidad de librerías externas, lo que hace un rendimiento más optimizado, así como una eficiencia en el uso de la memoria. En lo relativo al código nativo encontramos dos grandes sistemas: Android e IOs. El primero utiliza Java o Kotlin como lenguaje nativo de programación, siendo este segundo el que se adopta más frecuentemente debido a su rapidez de desarrollo e implementación. En cuanto a los sistemas IOs utilizan Objective-C o Switf para sus desarrollos, siendo este segundo el más utilizado.

  En cuanto a las desventajas del desarrollo nativo está la portabilidad, ya que el desarrollo de una aplicación solo estará destinado a un solo sistema operativo
- **Desarrollo Multiplataforma**  
  Se trata de desarrollos destinados a una multitud de plataformas, utilizando un proyecto core como base del desarrollo, y si bien el código se ejecuta de forma directa en el dispositivo, para su creación es necesario utilizar lenguajes de programación no nativos, lo que hace que el acceso a los recursos del sistema no sea directo. Las tecnologías que se utilizan para este tipo de desarrollo son frameworks y/o librerías que permiten la generación de código cross. Entre estas tecnologías podemos encontrar ReactNative, IONIC, Vue Mobile, Flutter, Xamarin, MAUI. Los tres primeros utilizan JavaScript como lenguaje de programación (aunque alguno utiliza su evolución TypeScript), mientras que los dos últimos utilizan C#. Mención especial con Flutter, librería mantenida por Google que utiliza dart como lenguaje de programación y que veremos a lo largo del curso
- **PWA (Progressive Web Apps)**  
  Se trata de aplicaciones que se ejecutan directamente en el navegador del móvil o en un WebView. Podemos decir que se trata de una página web adaptada para su renderización dentro de un teléfono móvil. Las aplicaciones que permiten la realización de PWD son HTML, CSS y JS como elementos de desarrollo, además de utilizar librerías que permiten el acceso a recursos del teléfono desde el WebView



Durante el curso nos centraremos en el desarrollo de aplicaciones nativas Android mediante el IDE Android Studio y de aplicaciones cross mediante la librería Flutter, aprovechando el IDO Android Studio para el desarrollo de las aplicaciones.



## 3. Android



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



El sistema operativo Android es uno de los más utilizados en el mundo, no solo por su carácter libre, sino también por su facilidad de uso y la gran cantidad de componentes ya desarrollados. Como toda compañía y/o tecnología que tiene a Google como propietaria, Android se ha convertido hoy en día en uno de los buques insignia del desarrollo móvil, teniendo una larga carrera en el desarrollo desde que fue fundada en 2008. Su núcleo Linux y la arquitectura del sistema operativo, hacen de Android una apuesta segura para el desarrollo. A lo largo de este apartado trataremos sobre la historia del sistema operativo, las versiones del mismo así como la arquitectura que soporta toda la ejecución del código.



### 3.2 Historia



Android es un sistema operativo desarrollado por Google que más penetración de mercado tiene hoy en día. Sus orígenes se remontan a principios del 2003 donde la compañía Android Inc fue fundada. Años más adelante, debido al éxito de la compañía, Google decidió adquirirla en 2005 marcando un hito importante en la historia de los dispositivos móviles, ya que sería el punto de partida de lo que hoy conocemos como el sistema operativo.

Durante todos estos años de historia, el sistema operativo ha ido evolucionando con las necesidades y posibilidades que los dispositivos otorgan a los desarrolladores. Por eso, no es de extrañar que el número de versiones del sistema sea de 14, más o menos a versión por año. Aunque hoy en día la versión más actual es la conocida como estamos en DownCake, en la actualidad números dispositivos utilizan versiones anteriores.

| Nombre comercial | Versión | Año lanzamiento | Nivel API |
| --- | --- | --- | --- |
| Apple Pie | 1.0 | 2008 | 1 |
| Banana Bread | 1.1 | 2009 | 2 |
| Cupcake | 1.5 | 2009 | 3 |
| Donut | 1.6 | 2009 | 4 |
| Eclair | 2.0 - 2.1 | 2009 | 5-7 |
| Froyo | 2.2 - 2.2.3 | 2010 | 8 |
| Gingerbread | 2.3 - 2.3.7 | 2010 | 9-10 |
| Honeycomb | 3.0 - 3.2.6 | 2011 | 11-13 |
| Ice Cream Sandwich | 4.0 - 4.0.5 | 2011 | 14 - 15 |
| Jelly Bean | 4.1 - 4.3.1 | 2012 | 16 - 18 |
| KitKat | 4.4 - 4.4.4 | 2013 | 19 - 20 |
| Lollipop | 5.0 - 5.1.1 | 2014 | 21 - 22 |
| Marshmallow | 6.0 - 6.0.1 | 2015 | 23 |
| Nougat | 7.0 - 7.1.2 | 2016 | 24 - 25 |
| Oreo | 8.0 - 8.1 | 2017 | 26 - 27 |
| Apple Pie | 9.0 | 2018 | 28 |
| Quince Tart | 10.0 | 2019 | 29 |
| Red Velvet Cake | 11.0 | 2020 | 30 |
| Snow Cone | 12.0 - 12.1 | 2021 – 2022 | 31 - 32 |
| Tiramisu | 13.0 | 2022 | 33 |
| UpsideDown cake | 14.0 | 2023 | 34 |

En la actualidad, a fecha de inicio de 2024, ya está disponible una versión beta de la API 35, por lo que en pocos meses estará disponible en el mercado. Como se comentaba en los puntos anteriores, no todos los dispositivos del Android ejecutan la versión más actual, siendo un porcentaje realmente bajo los que sí lo hacen. Esto es muy importante y un tema a tener en cuenta ya que para desarrollar es necesario indicar cual es el API mínima que un dispositivo debe ejecutar para poder correr la aplicación sin problema. Es por ello que no es necesario hacer desarrollos para el último API publicada (un uso actual inferior el 3% de los dispositivos actuales), sino que es necesario englobar a la mayoría de los usuarios



![image](assets/cm6dwcopr00jm3570iwk928oo-Imagen8.jpg)



Como podemos ver en el gráfico proporcionado por Statcounter, en mayo del 203 las versiones más utilizadas eran la 10, 11, 12 pese a que la 13 ya estaba liberada. Como se verá más adelante, identificar el target de usuarios para el que se desarrollará la aplicación es básico.



### 3.3 El sistema operativo



Una vez visto la historia de Android, vamos a pasar a hablar del sistema propiamente dicho. Estamos ante un sistema muy robusto y flexible basado en un kernel de Linux y que incorpora una máquina virtual llamada Dalvik para la ejecución de las aplicaciones. Entre sus principales características podemos destacar:



- **Android SDK (Software Development Kit)**  
  El sistema cuenta con un conjunto de herramientas, bibliotecas y componentes que posibilitan el desarrollo tes y depuración de las aplicaciones.
- **Soporte para multitud de dispositivos**  
  Android es compatible con una amplia variedad de dispositivos, desde teléfonos inteligentes y tabletas hasta televisores, relojes inteligentes y dispositivos IoT (Internet de las cosas).
- **Google Play Store**  
  El sistema cuenta con la principal plataforma de distribución de aplicaciones a nivel mundial, Google Play Store, que permite a los desarrolladores llegar a millones de usuarios en todo el mundo.
- **Acceso a funcionalidades del dispositivo**  
  El desarrollo permite el acceso a las diferentes funciones del dispositivo, como la cámara, GPS, sensores, servicios de ubicación, almacenamiento externo y otros, a través de las API proporcionadas por el propio sistema.
- **Seguridad**  
  Android incorpora medidas de seguridad que garantiza el núcleo Linux como el modelo de permisos, el cifrado de datos y la verificación de aplicaciones. De esta forma se puede proteger la privacidad del usuario y la integridad de las aplicaciones.
- **Actualizaciones Continuas**  
  Google lanza regularmente nuevas versiones del sistema con mejoras en rendimiento, seguridad y características. Los desarrolladores pueden aprovechar estas actualizaciones para mejorar sus aplicaciones.



En cuanto a la estructura de capas del sistema operativo, podemos diferenciar 5 grandes capas, cada una de ellas interactuando con sus vecinas. Son las siguientes:



- **Nucleo (Kernel)**  
  El núcleo de Linux es la base del sistema operativo Android. Proporciona los servicios fundamentales de bajo nivel, como la gestión de memoria, la administración del procesador, los controladores de dispositivos y la gestión del sistema de archivos. Además, proporciona una capa de abstracción para el hardware subyacente, permitiendo que el sistema operativo interactúe con los componentes del dispositivo.
- **Capa de librerías (Libraries)**  
  Incluye una variedad de librerías escritas en C/C++ que proporcionan funcionalidades esenciales al sistema y a las aplicaciones. Estas librerías incluyen la implementación del lenguaje Java, la gestión de gráficos (OpenGL), la gestión de bases de datos SQLite, la conectividad de red y otras funciones esenciales del sistema.
- **Máquina Virtual (JVM)**  
  Android utiliza una versión personalizada de la máquina virtual de Java. Esta capa es responsable de ejecutar el código de las aplicaciones Android. Convierte el código compilado de Java en instrucciones que el hardware puede entender y ejecutar.
- **Capa de aplicaciones (Application Framework)**  
  Proporciona un conjunto de API y herramientas que permiten a los desarrolladores crear aplicaciones para Android. Incluye componentes como Activity Manager, Content Providers, View System, Package Manager, entre otros. Estos componentes facilitan la creación de aplicaciones interactivas y permiten que las aplicaciones interactúen entre sí.
- **Capa de aplicaciones (Applications)**  
  Capa superior del sistema operativo Android y comprende las aplicaciones que los usuarios instalan y ejecutan en sus dispositivos. Esto incluye aplicaciones preinstaladas como el navegador web, el cliente de correo electrónico, el calendario, así como las aplicaciones descargadas desde Google Play Store u otras fuentes. Las aplicaciones pueden variar en funcionalidad y propósito, desde juegos hasta aplicaciones de productividad, redes sociales, etc.



![image](assets/cm6dwni2500o43570u8h3t0w0-Imagen9.png)



### 3.4 Instalación y configuración del IDE



Para poder hacer un desarrollo con Android, existen multitud de posibilidades en lo que a IDEs se refiere: desde trabajar con Visual Studio Code utilizando las extensiones necesarias para poder compilar y emular código java con las librerías Android, hasta utilizar Intellij Idea con los plugins de Android. Sin embargo, la solución más práctica es la de trabajar con el IDE oficial Android Studio, desarrollado por JetBrain y basado en IntelliJ IDEA con todas las configuraciones necesarias realizadas por defecto. Para poder descargarlo basta con ir a la página oficial y seleccionar el instalador correspondiente a nuestro sistema operativo y arquitectura. Para la descarga podemos utilizar el siguiente link, siendo la versión actual a día de hoy la de Iguana ([https://developer.android.com/studio?hl=es-419](https://developer.android.com/studio?hl=es-419)). Para poder comprobar el proceso de instalación podemos ver el video que del siguiente enlace de la documentación oficial: [https://developer.android.com/studio/install?hl=es-419](https://developer.android.com/studio/install?hl=es-419)

Antes de continuar es importante diferenciar un par de nombres:



- **IDE**  
  El entorno de desarrollo integrado que permite la ejecución y compilación de programar realizados para un desarrollo Android.
- **SDK**  
  Conjunto de librerías que permiten el desarrollo Android.
- **AVD**  
  Dispositivo virtual que permite emular aplicaciones Android.



Cuando instalamos Android Studio, tal y como se ha visto en el video, en el proceso se requiere de la descarga de una serie de librerías necesarias para continuar. Estas son las SDK o niveles de api para los cuales haremos el desarrollo. Es importante tener en cuenta que no es necesario hacer una descarga de todas las disponibles, sino que basta con un par de ellas para hacer el desarrollo. En este caso, siempre es recomendable descargar de los últimos niveles disponibles, ya que así nuestras apps estarán disponibles para todas las APIS anteriores. En el caso de que queramos probar el desarrollo para alguna específica podremos descargarla más adelante. Una vez realizada la instalación para poder probar nuestras aplicaciones tendremos la posibilidad de emular en un dispositivo virtual, llamado AVD, para lo cual lo tendremos que crear desde el entorno. Otra de las posibilidades es la de emular nuestras aplicaciones desde un dispositivo físico, para lo cual tendremos que habilitar las opciones de desarrollador siguiendo los pasos:

1. Desde el menú de Ajustes del teléfono accedemos a la parte de configuración
2. Una vez allí seleccionamos la opción Acerca del teléfono
3. Localizar la información que corresponde con el número de compilación y realizar 7 toques repetidos. Con el último, saltará un aviso indicando que las opciones de desarrollador han sido habilitadas
4. Por último, tendremos que entrar en el nuevo menú Opciones de desarrollador que habrá aparecido en los Ajustes del teléfono y habilitar la opción depuración por USB

Una vez realizado todos estos pasos, cuando conectemos el teléfono por USB (hay posibilidad de hacerlo por WIFI para versiones 11 o superiores, pero no es muy recomendable por la estabilidad de la conexión) tendremos que aceptar la clave RSA de manera que ambos dispositivos confíen entre sí. Con todo esto realizado cada vez que nuestra aplicación sea compilada se ejecutará dentro de nuestro teléfono



### 3.5 Conceptos básicos del desarrollo Android



Antes de comenzar a crear proyectos, es importante tener muy claro algunos conceptos de los que estaremos hablando a lo largo de la asignatura. Algunos de estos conceptos son:

- **Intents:** Aquellas acciones que pueden arrancar o disparar una acción concreta dentro de una aplicación Android. Existen intent implícitos o explícitos, entre los que nos podemos encontrar acciones como arrancar una segunda pantalla, abrir el navegador con una url cargada, abrir Google maps posicionando el mapa en una ubicación concreta, realizar una llamada de teléfono, abrir la aplicación de envío de correo configurada por defecto y mandar un mail, etc… Muchas de estas acciones requieren de permisos que tendrán que ser gestionados tanto en código mediante mensajes al usuario como pedidos al sistema a la capa de frameworks



```scala
1. // Intent que cambia entre dos pantallas
2. Intent i = new Intent(this, SecondActivity::java.class)
3. // Intent que realizar una llamada de telefono mediante la app de telefonía
4. Intent intent = Intent(Intent.ACTION_DIAL);
5. intent.setData(Uri.parse("tel:" + 123456789));
```



- **Activity:** Componente de la aplicación que representa una pantalla única con una interfaz de usuario. En pocas palabras, cada pantalla en una aplicación de Android es representada por una "Activity". Estos componentes se utilizan para interactuar con el usuario y presentar información de manera visual. Cada una de estas pantallas tiene dos elementos: una parte gráfica definida en un archivo XML o en el propio código kotlin (si se utiliza Android compose) y una parte lógica definida en un archivo .kt o .java. Una aplicación como mínimo tendrá una pantalla para que esta pueda funcionar.
- **View:** Objeto que es utilizado para crear una interfaz de usuario y mostrar contenido en la pantalla. Las view son los componentes básicos utilizados para construir la interfaz de usuario en una aplicación Android, pudiendo ser desde elementos con una representación gráfica como botones, campos de texto, imágenes, listas desplegables, etc… mediante los cuales el usuario tiene una interacción directa, como layouts.
- **Layouts:** Views que no tienen una representación gráfica específica, pero son fundamentales, ya que se encargan de gestionar la colocación y posicionamiento de cada uno de los elementos dentro de la interfaz gráfica. Existen diferentes tipos, teniendo cada uno de ellos unas características totalmente diferentes.
- **Fragment:** Componente de la interfaz de usuario (por lo tanto, categorizado dentro de las views) pero que cuenta con un comportamiento especial ya que representa una parte completa de la pantalla. A grandes rasgos, podríamos decir es como una pantalla dentro de una activity. A diferencia de una activity que representa una pantalla completa con la que un usuario puede interactuar, un fragment es una porción de la interfaz de usuario que funciona de manera modular y puede ser reutilizable en diferentes partes, Estos componentes permiten crear interfaces de usuario más flexibles y escalables en las aplicaciones Android al dividir la interfaz en partes más pequeñas y modulares.
- **Broadcast Receiver:** componente que permite a la aplicación escuchar y responder a mensajes del sistema o de otras aplicaciones, facilitando la comunicación entre distintas partes del sistema y la ejecución de acciones en respuesta a diversos eventos.
- **AndroidManifers:** Archivo que indica cual es la estructura de los elementos que forman parte de una aplicación Android, asigna recursos en tiempo de ejecución, administrar permisos y verificar la seguridad de la aplicación, etc. Cada vez que se crea una nueva aplicación Android o se modifican componentes clave de esta, es fundamental mantener actualizado y correctamente configurado el archivo de manifiesto. Podemos decir que representa el punto de inicio de toda aplicación.



### 3.6 Estructura de un proyecto Android



Cuando se crea un proyecto de Android estudio se genera una cantidad de contenido importante de forma automática. Muchas veces, uno de los principales problemas es no entender cuál es el uso que se le tiene que dar a cada uno de los archivos / directorios creados o como poder generar nuevos del mismo tipo. Antes de empezar a comentar la estructura hay que tener en cuenta que todo aquello que sea utilizado por el proyecto tendrá que estar enlazado o bien mediante archivos colocados en su sitio o bien mediante librerías / conexiones de red.



Para poder crear un proyecto de Android, es necesario seguir los siguientes pasos:

1. En la pantalla principal seleccionar New Proyect
2. Android Studio da la posibilidad de crear un proyecto desplegado en diferentes plataformas, como es teléfonos y tablets, wareables, televisiones o coches. En esta asignatura nos centraremos en proyectos destinados a teléfonos y tables.
3. El siguiente paso indica la creación mediante una plantilla. Estas se diferencias entre cada una en el número de elementos o disposición que trae configurado por defecto. Para poder empezar de 0, utilizaremos una EmptyActivity, la cual trae una pantalla creada por defecto, pero sin nada más asociado.
4. El último paso es la selección de los siguientes datos:

   1. **Nombre del proyecto:** Será el nombre que se le otorga al proyecto y por defecto el nombre que tendrá el icono de la pantalla de inicio cuando instalemos la aplicación en en teléfono. Esto se podrá cambiar más adelante.
   2. **Nombre del paquete del proyecto:** Configuración muy importante, ya que es el nombre que utilizará el teléfono para ubicar la aplicación. Su estructura debería ser ambito.compañia.nombre_proyecto todo ello sin espacios
   3. **Ubicación del proyecto:** carpeta donde se creará el proyecto
   4. **Lenguaje de programación:** Pudiendo seleccionar Kotlin o Java. Nosotros nos centraremos en Kotlin
   5. **SDK Mínimo:** API para la cual nuestro proyecto funcionará. En el caso de seleccionar un nivel muy elevado, el proyecto solo funcionará para teléfonos que tengan instalado ese sistema. Por defecto seleccionaremos api 24, por lo que nuestra aplicación funcionará para teléfonos con Android 7.0 en adelante
   6. **Build configuration:** configuración que tendrán los scripts del proyecto. Por defecto seleccionaremos Kotlin DSL



Una vez creado el proyecto, en la parte de la izquierda del espacio de trabajo aparecen todos los elementos generados



![image](assets/cm6dx8q2i00yx3570vfplbe3b-Imagen11.jpg)



En la parte de la izquierda encontraremos todos los ficheros con los que podemos trabajar, teniendo en cuenta que podemos poner la vista Android (la que esá activada en la foto que se muestra) o la vista proyecto. Es recomendable trabajar con la vista Android ya que es la que mostrará los elementos más importantes del proyecto. En cuanto a la organización de carpetas y los elementos que guardan cada una de estas, podemos destacar las siguientes:



- **Manifest**  
  Carpeta que guarda el fichero AndroidManifest.xml. Se trata del archivo más importante del proyecto ya que sin él la aplicación no sería capaz de comprender los elementos que forman parte de este. Podemos decir que se trata del punto de entrada de la aplicación donde se declaran parte de los contenidos de la aplicación. Los elementos se definen mediante etiquetas donde cada una tiene sus propios atributos y es importante saber que al menos debe existir una activity que sea main y launcher para así poder arrancar el proyecto cuando se pinche el icono de la aplicación. Cada una de las activity generada dentro de la aplicación tendrá que estar reflejada en este fichero indicando sus particularidades si las tienen. Además, también se declararán en este archivo elementos como servicios, permisos, broadcast, etc.…
- **Carpeta java acompañada del nombre del paquete**  
  En esta parte se situarán todos los archivos .java o .kt que darán funcionalidad al proyecto. Es muy recomendable crear subpaquetes para organizar el código de forma lógica ya que cuando existan numerosos elementos la claridad en el código y en el proyecto será básica. Inicialmente nos encontramos con un archivo MainActivity.kt que hace referencia a la empty activity que generada en la creación del proyecto.
- **Carpeta res**  
  Carpeta donde se van a ubicar todos los archivos utilizados como recursos dentro del proyecto, como son las imágenes, strings, valores constantes, menús, layouts, etc… Inicialmente tan solo aparecen 4 elementos dentro de esta carpeta res

  - **drawable:** Se guardarán gráficos que pueden ser escalados dentro la activity dependiendo de cosas como densidad de pixels, posición, tamaño de pantalla, etc…Pueden aparecer elementos en png o archivos en xml que definan el comportamiento de una imagen (animación)
  - **layout:** Se puede definir como la interfaz gráfica que muestra los elementos de una pantalla. Por lo general está asociado a una activity, pero multitud de elementos utilizan este tipo de archivo: fragments, adaptadores, etc… Está escrito en xml y se puede manejar o bien de forma gráfica o bien mediante código.
  - **mipmap:** muy parecida a la carpeta de drawable, con la diferencia que aquí se guardarán elementos vectoriales. Para evitar que se puedan escalar los elementos, dentro de esta carpeta se crearán subcarpetas con categorizados para asignar elementos dependiendo de factores como por ejemplo tamaño de pantalla, densidad de pixeles, etc.
  - **values** carpeta que guarda los datos que constantes del sistema como palabras, colores, estilos, etc. Inicialmente se crea un fichero string.xml donde se guardan todas las palabras que son utilizadas, colors.xml donde se guardarán todos los colores que son utilizados y theme.xml donde se guardan la definición de todos los estilos utilizados.

  Estas son las carpetas que inicialmente encontramos en res, pero se irán creando más según vayamos avanzando en la creación de nuestra aplicación, donde necesitaremos elementos como menus, navegaciones, videos, etc.
- **Gradle scripts**  
  Guarda los archivos de configuración del proyecto, definiendo la forma en la que se compila este. Además de estas configuraciones, también se pueden descargar dependencias en forma de librería, activar características adicionales al desarrollo, etc.



### 3.7 Kotlin



Una vez creado el proyecto, ya estamos preparados para empezar a desarrollar, pero antes vamos a repasar las principales características del lenguaje Kotlin.



#### Variables



Las variables representan los espacios en memoria donde se almacenan los datos que serán reutilizados en cualquier momento. Para poder definir variables en kotlin se utiliza la siguiente nomenclatura



```ini
nombre: tipo = valor
```



El tipado no es obligatorio, ya que el propio compilador puede definir el tipo de la variable dependiendo de cuál sea el valor asignado. En cuanto a los tipos de variables, podemos encontrar dos: var y val. Var se trata de una variable mutable, es decir que puede alterar su valor a lo largo del programa, mientras que val se trata de una variable constante que no puede cambiar su valor una vez ha sido asignado.



```kotlin
var numero: Int = 0;
val VARIABLE_CONSTANTE = "VALOR FIJO"
fun main(arg: Array<String>) {
    // esto provocaría un fallo de compilación
    VARIABLE_CONSTANTE = "Cambio de valor"
    // esto reasigna el valor de la variable a 9
    numero = 9;
}
```



A la hora de declarar variables, kotlin tiene un mecanismo para evitar las excepciones de nullpointer. Se conoce como null safety y permite asignar un posible valor nulo a una variable sin que al utilizarlo se rompa la ejecución. Para ello se utiliza el símbolo de ? después del tipo de la variable;



```ini
var nombre: String? = null
```



Esto indica que la variable tiene asignada un valor de null. Con esta declaración cada vez que se quiera utilizar la variable se tendrá que indicar la posibilidad de obtener un null en la ejecución.



```kotlin
var nombre: String? = null
fun main(arg: Array<String>) {
    println(nombre?.length)
}

SALIDA
null
```



Hay en otros casos que no se puede obviar el fallo por uso de null. En estos casos es necesario indicar al compilador que si se encuentra con un elemento null que continue con la ejecución normal.



```kotlin
var totalFacturado: Int? = null
fun main(arg: Array<String>) {
    if (totalFacturado!! <0){
        println("Estamos en perdidas");
    }
}
```



En el caso de querer utilizar el null safety indicado anteriormente también se podría, siempre teniendo que llamar a una función después de la variable que puede ser nula.



```kotlin
fun main(arg: Array<String>) {
    if (totalFacturado?.compareTo(0) ==0){
        println("Estamos en perdidas");
    }
}
```



En algunas ocasiones puede ser muy interesante sustituir el valor del posible null por otro valor. Para ello, se utiliza lo que se conoce como el operador condicional, poniendo ?: = valor cuando es null.



```ini
totalFacturado?.compareTo(0) ?: -1
```



En este caso se está intentando utilizar el método comparteTo de la variable totalFacturado y comparándolo con 0. En el caso en el que la variable sea null, el valor se sustituirá por -1.

Otra de las posibilidades a la hora de declarar variables es la de utilizar el modificador lateinit, el cual indica que la variable a la hora de declararla no es necesario asignarle un valor, pero que durante la ejecución si se hará.



#### Funciones



Las funciones son las partes de código que se pueden ejecutar de forma individual para realizar una acción en concreto. En kotlin se declaran con la palabra reservada fun



```ini
fun nombreFuncion(){}
```



Para poder declarar parámetros dentro de una función se definen con un nombre y el tipo de este



```kotlin
fun funcionParamentros(arg1: String, arg2: Int){
    println("$arg1 es el primer parámetro")
    println("$arg2 es el segundo parámetro")
}
 
fun main(arguments: Array<String>) {
    funcionParametros("Uno",2)
}
```



A la hora de pasar parámetros a una función se puede hacer de forma posicional (la forma tradicional) o de forma nominal, lo que permite utilizar parámetros por defecto en cualquier posición.



```kotlin
fun main(arguments: Array<String>) {
    funcionParametros(arg1="Uno",arg2=2);
}
```



Del mismo modo, cuando se declaran argumentos dentro de una función, también se le pueden dar valores por defecto asignándolos de forma directa. En el caso de llamar a la variable y no pasar parámetros, serán estos los valores que se le asignarán al argumento.



```kotlin
fun funcionParametros(arg1: String="valor por defecto", arg2: Int=3){
    println("$arg1 es el primer parámetro")
    println("$arg2 es el segundo parámetro")
}
 
fun main(arguments: Array<String>) {
    funcionParametros()
}
 
// SALIDA
valor por defecto es el primer parámetro
```



En cuanto al tipo de retorno que tienen la función, este se declarará tras la declaración de argumentos y en el caso de no tenerlo, este será Unit (no siendo necesario ponerlo).



```kotlin
fun declaracionFuncion(): String{
 // cuerpo de la funcion
 return "Retorno"
}
fun sumaRetorno(op1: Int, op2:Int): Int{
    return op1 + op2
}
fun main(arguments: Array<String>) {
    println("La función de suma ha retornado "+sumaRetorno(4,5));
}
// SALIDA
La función de suma ha retornado 9
```



#### Funciones lambda



Dentro de la declaración de funciones, existen un tipo llamado funciones lambda o funciones de flecha que permiten una codificación rápida e intuitiva. Este tipo de funciones se suelen ejecutar pasadas como parámetros o asignadas a una variable. La sintaxis utilizada para su creación es la siguiente



```ini
{arg1: Tipo, arg2: Tipo) -> // cuerpo de la funcion}
```



Como se ha comentad, en algunos casos la función lambda se suele asociar a una variable. Para ello se puede definir el tipo al que se le asigna.



```scala
var lambdaSuma = {arg1: Int, arg2: Int -> print("la suma entre $arg1 y $arg2 es "+arg1.plus(arg2))}
// la misma definición que el anterior, pero declarando el tipo
var lambdaSumaValida: (Int,Int)->Unit = {arg1: Int, arg2: Int -> print("la suma entre $arg1 y $arg2 es "+arg1.plus(arg2))}
```



En el caso de querer que la función lambda retorne algo, se puede indicar al igual que las funciones



```kotlin
var funcionLambdaNormal: ((Int) -> Int) = { argumento1: Int ->
    if (argumento1 > 0) {
        1
    } else {
        0
    }
}
```



#### Clases



La programación orientada a objetos representa uno de los principales paradigmas dentro de la programación actual. Para ello las clases actual como elemento clave, representando el “molde” de los elementos (objetos) que conforman el programa. Su uso y creación es muy similar al de java, teniendo en cuenta que a la hora de utilizar constructores tenemos dos diferentes tipos: primarios y secundarios

Si se quiere crear un constructor con parámetros, se utiliza la palabra reservada constructor, siendo este el constuctor secundario.



```typescript
class ClaseA{
    var nombre: String;
    constructor(nombre: String){
        this.nombre = nombre;
    }
}
```



Si tan solo se quiere utilizar un constructor se puede obviar la palabra `constructor` indicando los parámetros al lado del nombre de la clase, utilizando así el constructor primario.



```kotlin
fun main(arg: Array<String>){
    var clase: ClaseA = ClaseA("Ejemplo");
}
 
class ClaseA (var nombre: String){
}
```



En el caso de querer contar con más de un constructor,  es necesario que todos los constructores secundarios dependan del primario.



```kotlin
fun main(arg: Array<String>){
var lenguaje = Lenguaje("java","multi",18)
println(lenguaje.plataforma);
}
 
class Lenguaje{
    var nombre: String
    var plataforma: String;
    var version: Int;
    constructor(nombre: String, plataforma: String, version: Int)  {
        this.nombre = nombre
        this.plataforma = plataforma;
        this.version = version;
    }
}
```



En el ejemplo anterior, tenemos un constructor secundario el cual permite crear un objeto de tipo Lenguaje pasando como parámetros nombre, plataforma y versión. En este caso se podría haber sustituido el constructor secundario por el primario.



```kotlin
class Lenguaje(var nombre: String, var plataforma: String, var version: Int) {}
```



Existe la posibilidad de crear varios consctructores. Para ello a la hora de crearlos, es enecesario se basa en la existencia del primario, sobre el cual el resto depende. Para ello se utiliza la notación corta para el constructor "base" y la palabra constructor para el resto, teniendo en cuenta que todos deberán de devolver un objeto de la clase. En este ejemplo se creará un constructor base que recibe un parámetro String que representará el nombre. Adicionalmente se utilizarán dos constructores, uno que además aportará la plataforma, y otro que aportará la plataforma y la versión.



```kotlin
fun main(arg: Array<String>) {
    var java = Lenguaje("java", "multi", 18)
    var kotlin = Lenguaje( nombre="Kotlin", plataforma = "multi")
    var cSharp = Lenguaje ("C#");
    println(java.plataforma);
    println(kotlin.version);
    println(cSharp.plataforma)
}
 
class Lenguaje (var nombre: String){
    var plataforma: String? = null;
    var version: Int? = null;
 
    constructor(nombre: String, plataforma: String, version: Int): this(nombre) {
        this.plataforma = plataforma;
        this.version = version;
    }
 
    constructor(nombre: String, plataforma: String): this(nombre){
        this.plataforma = plataforma;
    }
}
```



En este caso como se ha utilizado un constructor base ocurren dos cosas:

- Todas las propiedades de la case se tienen que inicializar con un valor (existe la posibilidad de utilizar lateinit que se verá más adelante)
- Todos los constructores adicionales tienen que devolver el constructor base, y que además realizarán las acciones que hayan definido en su definición

Al igual que se pueden crear constructores, también se pueden crear tantas funciones como sean necesarias dentro de una clase, para así poder utilizarlo.



```kotlin
fun main(arg: Array<String>) {
    var java = Lenguaje("java", "multi", 11)
    var kotlin = Lenguaje( nombre="Kotlin", plataforma = "multi")
    var cSharp = Lenguaje ("C#");
    java.clasificar()
    java.mostrarDatos()
    kotlin.mostrarDatos()
    cSharp.mostrarDatos()
}
 
class Lenguaje (var nombre: String){
    var plataforma: String? = null;
    var version: Int? = null;
 
    constructor(nombre: String, plataforma: String, version: Int): this(nombre) {
        this.plataforma = plataforma;
        this.version = version;
    }
 
    constructor(nombre: String, plataforma: String): this(nombre){
        this.plataforma = plataforma;
    }
 
    fun clasificar(){
        if (this.nombre.lowercase().equals("java")){
            if (this.version?:12<14){
                println("versión obseleta")
            }
        }
    }
 
    fun mostrarDatos(){
        println("Nombre ${this.nombre}")
        println("Plataforma ${this.plataforma?: "no definida"}")
        println("Versión ${this.version?: "no definida"}")
    }
}
 
// SALIDA
versión obsoleta
Nombre java
Plaraforma multi
Versión 11
Nombre Kotlin
Plaraforma multi
Versión no definida
Nombre C#
Plaraforma no definida
Versión no definida
```



#### Herencia



Al igual que pasa en java, kotlin es un lenguaje de programación que da la posibilidad de configurar herencia entre clases para que estas aprovechen propiedades y funciones de una clase superior. Sin embargo, a diferencia de java, en kotlin por defecto las clases no pueden heredan entre si a no sé qué se ponga el modificador `open` antes del nombre de la clase, ya que si no esta será `final`



```kotlin
open class Persona (var nombre: String) {
 
     var apellido: String?=null;
     var dni: String?=null
 
    constructor(): this("Sin definir"){
 
    }
 
    constructor(nombre: String, apellido: String, dni: String): this(nombre){
        this.apellido = apellido;
        this.dni = dni;
    }
 
    fun mostrarDatos(){
        println("nombre: $nombre")
        println("apellido")
        println("dni: $dni")
    }
}
```



Una vez una clase está marcada como open, el siguiente paso será crear una clase que herede de esta. Para ello se utiliza el operados `:`seguido del nombre de la clase de la que se quiere heredar en un archivo nuevo



```json
class Trabajador: Persona() {
 
}
```



En este caso la clase Trabajador hereda de la clase Persona y utiliza el constructor por defecto de la misma (ya que se ha indicado con los paréntesis). Si se quieren sobreescribir constructores secundarios, es necesario indicarlo sin los paréntesis en la extensión de la clase.



```kotlin
class Trabajador: Persona {
    constructor(): super()
    constructor(nombre: String) : super(nombre)
    constructor(nombre: String, apellido: String, dni: String) : super(nombre, apellido, dni)
}
```



Si se quiere añadir propiedades a la clase se puede hacer e inicializarla en alguno de los constructores que se tengan.



```typescript
class Trabajador : Persona  {
    var numeroSS: Int?=null
 
    constructor(nombre: String, apellido: String, dni: String, numeroSS: Int) : super(nombre, apellido, dni){
        this.numeroSS = numeroSS;
    }
}
```



Si se quieren cambiar la definición de algún método de los creados en superclases es necesario dos cosas:

- Que el método cuando se define tenga la palabra reservada `open` (obligatorio aunque la clase sea `open`)
- En el método que se quiera sobrescribir utilizar la palabra reservada override antes de la definición de la función.



```kotlin
open class Persona (var nombre: String) {
 
     var apellido: String?=null;
     var dni: String?=null
 
    constructor(): this("Sin definir"){
 
    }
 
    constructor(nombre: String, apellido: String, dni: String): this(nombre){
        this.apellido = apellido;
        this.dni = dni;
    }
 
    open fun mostrarDatos(){
        println("nombre: $nombre")
        println("apellido $apellido")
        println("dni: $dni")
    }
}
 
class Trabajador : Persona  {
    var numeroSS: Int?=null
 
    constructor(nombre: String, apellido: String, dni: String, numeroSS: Int) : super(nombre, apellido, dni){
        this.numeroSS = numeroSS;
    }
 
    override fun mostrarDatos(){
        super.mostrarDatos()
        println("Número SS: $numeroSS")
    }
 
}
```



En muchas ocasiones no interesa tener una clase para que pueda ser creada como objeto, sino que se necesita como la base para el resto de subclases que irán por debajo en la linea de herencia. Para ello existe el concepto de clase abstracta, la cual puede tener entre 0 y n métodos abstractos (solo con firma y sin definición). Para poder crear una clase abstracta se debe utilizar antes del nombre de la clase la palabra reservada `abstract`, siendo open por defecto. En el caso de tener un método abstracto se utilizar la misma palabra reservada antes de la declaración del método



```kotlin
abstract class Persona (var nombre: String) {
 
     var apellido: String?=null;
     var dni: String?=null
 
    constructor(): this("Sin definir"){
 
    }
    constructor(nombre: String, apellido: String, dni: String): this(nombre){
        this.apellido = apellido;
        this.dni = dni;
    }
    abstract fun mostrarDatos();
 
class Trabajador : Persona  {
    var numeroSS: Int?=null
 
    constructor(nombre: String, apellido: String, dni: String, numeroSS: Int) : super(nombre, apellido, dni){
        this.numeroSS = numeroSS;
    }
 
    override fun mostrarDatos(){
        println("Nombre: $nombre")
        println("Apellido: $apellido")
        println("DNI: $dni")
        println("Número SS: $numeroSS")
    }
 
}
```



#### Interfaces



Uno de los puntos que no permite kotlin (al igual que java) es la herencia múltiple. Para paliar esta desventaja existe el concepto de interfaz, utilizando la palabra reservada `interface` en vez del de `class`. Hay que recordad que una interfaz tiene un conjunto de métodos no definidos (por defecto abstractos) que serán declarados en aquellas clases donde sean utilizadas las interfaces.



```kotlin
interface Directivo {
    fun realizarVoto(voto: Int);
}
```



Una vez se tiene declarada la interfaz, en el caso de querer utilizarla se pone detrás de los : que se utiliza para la herencia.



```kotlin
class Jefe:Persona, Directivo {
    constructor(nombre: String) : super(nombre)
    constructor() : super()
    constructor(nombre: String, apellido: String, dni: String) : super(nombre, apellido, dni)
 
    override fun realizarVoto(voto: Int) {
        var numero = (0..10).random()
        println("El vóto emitido es de $voto")
        println("$numero")
        println("El resultado con el random obtenido es de ${numero*voto}")
 
    }
 
    override fun mostrarDatos() {
        println("Nombre: $nombre")
        println("Apellido: $apellido")
        println("DNI: $dni")
    }
}
```



## 4. Desarrollo Android



### 4.1 Introducción



![image](assets/cm6dygqfd025x3570u8i23jor-stock-image.jpg)



Una vez ya tenemos claros cuales son los conceptos base del desarrollo móvil en Android y conocemos cual es la estructura base de un proyecto, podemos pasar a desarrollar. A lo largo de este punto aprenderemos a trabajar con Activities, el paso de datos entre ellas, asociar partes gráficas y lógicas, etc.



### 4.2 Activitys



Las Activitys son los componentes base del desarrollo Android, ya que se trata del componente principal de la interfaz de usuario, representando una pantalla con interfaz.  Como tal, toda pantalla consta de dos partes: parte lógica, representada mediante un archivo .kt o .java, y parte gráfica, representada por un fichero .xml o por nodos en el caso de utilizar Android compose. Antes de explica en detalle cada uno de ellos, se muestra un video de cómo se entiende el desarrolla Android y la relación que tiene la parte gráfica con la parte lógica.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652019_1/scormcontent/assets/INSD_DM_Unidad1_Apartado5_2_Video.mp4?v=1)



#### Parte gráfica



Como se ha dicho, toda pantalla tiene una parte gráfica la cual interactúa de forma directa con el usuario. Esta vista está compuesta de elementos llamados views los cuales se organizan internamente y se declaran en un fichero .xml. Antes de empezar a explicar la creación del fichero, es importante conocer que los elementos de tipo view pueden ser de dos grandes tipos:



- **views finales**  
  Aquellos que tienen una representación gráfica final como botones, desplegables, listas, etc…
- **Views contenedores**  
  Aquellos que organizan el espacio, gestionando como deben colocarse cada una de los elementos que forman parte del mismo. Estos elementos se conocen como layouts y anque existen números principalmente se usan los siguientes:

  - LinearLayout: Los elementos que pertenezcan a este layout se colocarán según la orientación indicada, pudiendo ser horizontal o vertical
  - ConstraintLayout: Los elementos que pertenezcan a este layout se colocarán restringidos a otros elementos, teniendo como mínimo una restricción por eje.



Como se ha comentado para poder definir una parte gráfica, se utiliza un fichero xml ubicado dentro de la carpeta layouts donde a través de nodos se identifican cada uno de los elementos de la interfaz. Estos elementos constan de una serie de características que marcan el comportamiento de este. Para poder crear un fichero gráfico, dentro de la carpeta correspondiente creamos un layout resource file mediante botón derecho y se definen cada uno de los elementos. Para poder trabajar con los elementos que forman parte del fichero, podremos activar en la parte superior izquierda la vista diseñador, código y partida.



```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="<http://schemas.android.com/apk/res/android>"
    xmlns:app="<http://schemas.android.com/apk/res-auto>"
    xmlns:tools="<http://schemas.android.com/tools>"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">
 
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        android:id="@+id/texto_main"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
 
</androidx.constraintlayout.widget.ConstraintLayout>
```



Como se puede ver en el ejemplo anterior, tenemos como elemento principal un Constraint layout donde dentro ubicamos un TextView (elemento que actúa como etiqueta de texto), el cual está restringido en todos los ejes.



![image](assets/cm6dyofol02ch3570ok13lzlw-Imagen12.jpg)



Además de las restricciones, en cada uno de los nodos hay una serie de atributos que son obligatorios para el correcto funcionamiento de estos y son los siguientes:



- **android: layout_width:**  
  Este atributo marca cual es el comportamiento del elemento en ancho. Sus tres posibles configuraciones son wrap_content (el elemento ocupará en ancho lo que necesite, por lo que el espacio se acoplará a sus necesidades), match_parent (el elemento se pegará en ancho a su padre, en este caso la pantalla) o una cantidad de px determinada, siendo la opción menos recomendable. En el caso de querer optar por esta última configuración, es recomendable utilizar la medida dp (densidad de píxeles) en vez de px (píxeles) o utiliza pesos mediante el atributo weigth.
- **android: layout_heigth**  
  Sería exactamente igual, pero definiendo el comportamiento en altura
- **android: id**  
  Este atributo no es literalmente obligatorio, pero permitirá acceder al elemento definido en el fichero gráfico desde el fichero donde se define la lógica de la aplicación. Al tratarse de un atributo que debe quedarse guardado en la aplicación es necesario asignarlo como recurso en el momento de la compilación, para ello se le asigna el valor @+id/nombreId



En el siguiente video, podemos ver como configurar un layout, incorporando los atribútos básicos comentados anteriormente:



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652019_1/scormcontent/assets/INSD_DM_Unidad1_Apartado5_2_Video1.mp4?v=1)



Además de los layouts, dentro de las pantallas están los elementos finales mediante los cuales los usuarios pueden interactuar de forma directa con ellos. Los principales elementos y sus características son los siguientes:



#### Button



Se trata de una de las vistas más utilizadas dentro de la interfaz. Ya se ha visto alguna de las construcciones en los temas anteriores.



```ruby
    <Button
        android:id="@+id/botonPulsar"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Pulsar!!"
        />
```



En el caso de querer crear un botón con un estilo personalizado se configuraría el atributo style. En el caso de querer ponerle una imagen al botón se utilizaría una vista de tipo ImageButton y se configuraría el atributo src



#### EditText



Los EditText representan uno de los elementos más utilizados en las interfaces gráficas de android, ya que permiten recoger datos introducidos por el usuario en el campo de texto. Cuando se quiere declarar un elemento xml se realizaría de la siguiente forma:



```xml
<EditText
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/editTexto"
        android:hint="Por favor introduce un dato"
        android:inputType="text"
        />
```



El atributo hint representa la pista que pone en el edit nada más arrancar y que desaparecerá cuando se seleccione el elemento. El atributo inputType marca los elementos que se podrán poner dentro de campo (números, letras, etc...).



#### CheckBox



Se trata de una vista que consta de dos elementos: estado seleccionado y estado no seleccionado. Esta vista es muy similar al botón, por lo que muchas de las opciones que se pueden incluir en los button también se pueden utilizar aquí. Para poder utilizarlo se utilizaría el siguiente código xml



```xml
<CheckBox
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Opción a seleccionar"
        android:id="@+id/checkSeleccionar"
        />
```



#### RadioButton



Se trata de un componente muy parecido al visto anteriormente. Cuenta con dos posibles estados: seleccionado y no seleccionado. La diferencia con los checkbox es que su uso por lo general está asociado a un grupo y además el usuario tan solo puede seleccionarlo, no deseleccionarlo. En el caso de querer utilizarlo de forma individual se declararía en el xml de la siguiente forma.



```ruby
<RadioButton
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Seleccionado"
        android:id="@+id/radioIndividual"
        />
```



Como se puede ver existe la posibilidad de declararlo individualmente, lo que pasa es que no tiene mucho uso real, ya que como se ha dicho en el momento que se selecciona el radio, no podría deseleccionarse. Lo que si tiene mucho uso es declararlo dentro de un grupo de elementos:



```xml
<RadioGroup
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:id="@+id/grupoRadios">
 
        <RadioButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Opción 1"
            android:id="@+id/radioUno"/>
        <RadioButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Opción 2"
            android:id="@+id/radioDos"/>
        <RadioButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Opción 3"
            android:id="@+id/radioTres"/>
    </RadioGroup>
```



Como se puede ver, todos los elementos de tipo Radio están englobados dentro de una etiqueta de tipo RadioGroup. Tanto los elementos finales como el grupo tienen id, ya que a la hora de trabajar los eventos disponibles se puede: analizar el clic en un radio, analizar el cambio de estado de un radio (ambas opciones funcionan exactamente igual que los casos vistos en los componentes anteriores) o también se puede analizar el cambio de selección de algún elemento del RadioGroup.



#### Spinner



Se trata de elementos desplegables que pueden contener tanto elementos de una lista o array declarado en el código como de un recurso de tipo string-array declarado dentro de la carpeta res. Para poder utilizarlo, gráficamente se debería utilizar el siguiente código dentro del fichero xml



```ruby
<Spinner
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/spinnerSeleccion"
        />
```



Una vez está declarado elemento, es necesario llevarlo a la parte lógica y añadirle la parte de datos. Esta parte de datos es lo que se conoce como adaptador y permite juntar un elemento gráfico con una parte de datos. Para ello es necesario crear el objeto ArrayAdapter y asociarlo mediante el método setAdater. Sin embargo, la forma más sencilla de hacerlo es crear un array de string como recurso dentro del fichero strings.xml ubicado en res -> values -> strings.xml de la siguiente forma.



```xml
<string-array name="perfiles">
        <item>Administrador</item>
        <item>Usuario</item>
        <item>Invitado</item>
    </string-array>
```



Una vez creado el recurso, tan solo sería necesario agregarle la propiedad entries al código xml del spinner apuntando al recurso creado.



```xml
<Spinner
        android:id="@+id/spinnerPerfil"
        android:entries="@array/perfiles"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"/>
```



Existen multitud de elementos que forman parte de la gráfica de una pantalla, sin embargo, aquí hemos visto los principales. La unión de layouts junto con los elementos gráficos posibilitan la creación de los principales elementos.

Mención aparte tienen los elementos que muestra un listado de datos que se verán más adelante. Estos elementos reciben el nombre de RecyclerView.



#### Parte lógica



Una vez se tiene clara la gestión de la parte gráfica el siguiente punto a trabajar es programar la lógica de la aplicación. Para ello lo primero que debemos tener claro es que todos los elementos gráficos (representados en el xml que hemos explicado en el punto anterior) se asocian en una pantalla (llamada activity) con un ciclo de vida, donde cada uno de los métodos de este se ejecutan de forma automática. Este ciclo de vida es el siguiente:



![image](assets/cm6dzjzr902yw3570i4e89j1y-Imagen13.jpg)



A continuación, se muestra un video entendiendo cómo funcionan cada uno de los métodos del ciclo de vida y donde se ejecutan.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652019_1/scormcontent/assets/INSD_DM_Unidad1_Apartado5_2_Video2.mp4?v=1)



Dentro de todo este ciclo, el único método obligatorio de sobrescribir es el método onCreate, ya que es el encargado de asociar la parte lógica con la parte gráfica.



```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
```



Por defecto, este es el código que trae la actividad, asociando el xml creado con la activity mediante la ejecución del método setContetView pasando como parámetros el recurso creado con el nombre activity_main. El siguiente paso sería crear las variables de cada uno de los elementos definidos en el xml y asociarlas mediante un método llamado findViewById pasando como parámetros el id declarado en el archivo. Sin embargo, este proceso se hace muy tedioso, debido a la cantidad de líneas de código que serían necesairas para poder inicializar todas las variables de las que consta una pantalla. Para poder ahorrarnos todo este proceso existe una técnica llamada binding, la cual permite un acceso directo a todos los elementos de la parte gráfica. Para poder utilizar dicha técnica tendremos que hacer los siguientes pasos:



1. Activar la función dentro del archivo build.grade ([module.app](http://module.app)), para lo cual hay que incluir el siguiente código después de la definición de las kotlinOptions



```groovy
kotlinOptions {
    jvmTarget = "1.8"
}

viewBinding {
    enable = true;
}
```



Una vez incorporado el código será necesario actualizar el gradle, pulsando el botón Sync Now que aparecerá en la parte superior.



2. Crear una variable de: Una vez tengamos activada la característica de binding, tendremos que crear una variable en la activity tipada con el nombre de fichero xml acompañado de binding.



```ini
private lateinit var binding: ActivityMainBinding
```



Es muy importante el tipado de la variable y su declaración como lateinit. Dicho tipado siempre va a ser acompasado con el nombre del fichero del xml. En el caso en el que el fichero se llama activity_main, el tipado será el nombre del fichero en formato CamelCase con la palabra Binding. Esto hace que la asociación sea directa, por lo que no tendremos que preocuparlos de inicializar individualmente cada una de las variables. La asignación como lateinit indica que será iniciada más adelante, concretamente en el método onCrete.



3. Una vez la variable está creada, tendremos que inicializarla mediante un método llamado inflate. Para ello utilizaremos el siguiente código.



```kotlin
private lateinit var binding: ActivityMainBinding

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    binding = ActivityMainBinding.inflate(layoutInflater);
    setContentView(R.layout.activity_main)
}
```



Es muy importante que esta inicialización se realice en el método onCreate ya que es cuando la aplicación empieza a tomar forma, y el primer paso es poner la interfaz gráfica.



4. Como último paso tendremos que realizar la asociación de la parte lógica con la parte gráfica. Para ello en el método setContentView indicaremos que es la variable binding la encargada de esta parte.
   En concreto indicaremos que es su propiedad root, por lo que indicamos que el elemento principal del layout (y por lo tanto el resto) es el gestiona el elemento gráfico



```ini
setContentView(binding.root)
```



Una vez realizados estos pasos, podremos acceder a cada uno de los elementos declarados en el xml mediante su id, ya que esta está incorporada en la variable binding



### 4.3 Eventos



Otra de las partes básicas de toda aplicación es la gestión de las acciones que se realizan tras la consecución de una acción sobre un elemento gráfico, como por ejemplo puede ser una pulsación, la selección de un elemento en una lista, el cambio de un elemento dentro de un spinner. En Android estas acciones se manejan mediante listener, pudiendo definirlo como un patrón de diseño que permite a un objeto recibir notificaciones sobre eventos que ocurren en otro objeto. La función de los listener se realiza mediante la implementación de interfaces específicas que contienen métodos relacionados con los eventos que se escuchan.

Vamos a poner un ejemplo. Imaginemos que tenemos una aplicación que cuenta con un botón, el cual queremos que realice una acción en el momento que este sea pulsado, por lo que tendremos que asignar un listener al botón para poder escuchar el clic. Este listener en este caso recibe el nombre View.OnClickListener, teniendo un método llamado onClick

A la hora de asociar listener los pasos a seguir son los siguientes.



1. Tener creada la variable donde queremos asociar el evento correspondiente. En este ejemplo lo haremos sobre un botón que previamente estará declarado en el xml de la parte gráfica con un id llamado botonPulsar el cual será accesible de forma directa desde la variable binding tal y como se ha explicado en puntos anteriores.
2. Asignar el método setOnClickListener al botón y definir la funcionalidad de lo que queremos que pase cuando se pulse el botón.



```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    binding = ActivityMainBinding.inflate(layoutInflater);
    setContentView(binding.root)
    binding.botonPulsar.setOnClickListener {    
      // accione que queramos realizar tras la pulsación del botón teniendo el parámetro it
    }
}
```



En este ejemplo se ha realizado una asignación de forma directa indicando la función dentro de las {}, obteniendo como parámetro una vista (la que ha generado el evento, este caso el botón) que al ser un solo parámetro se puede obviar y se toma como it.

Otra de las opciones es implementar la interfaz dentro de la clase y pasarle como parámetros al método this. Esto lo utilizaremos cuando queramos asociar el mismo escuchador a varios objetos, tal y como se explicará en siguientes videos.



```kotlin
class MainActivity : AppCompatActivity(), OnClickListener{

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater);
        setContentView(binding.root)
        /*binding.botonPulsar.setOnClickListener {
            // accione que queramos realizar tras la pulsación del botón
        }*/         binding.botonPulsar.setOnClickListener(this)
    }

    override fun onClick(v: View?) {
        TODO("Not yet implemented")
    }
}
```



Cuando ocurre el evento (por ejemplo, cuando se presiona el botón), el método correspondiente del "listener" se ejecuta, permitiendo que la aplicación responda adecuadamente al evento. Esto proporciona un mecanismo efectivo para manejar la interacción del usuario en las aplicaciones Android.

Para comprobar que todo ha funcionado, podemos ejecutar el emulador y pulsar el botón, viendo que ocurre la acción codificada dentro del método onClick. Una de las comprobaciones básicas es la de sacar una notificación emergente llamada Snackbar.  Para crearla se utiliza el siguiente código.



```kotlin
override fun onClick(v: View?) {
    Snackbar.make(binding.root, "Notificacion mostrada con éxisto", Snackbar.LENGTH_SHORT).show()
}
```



La construcción de la notificación tiene la siguiente estructura en parámetros:

- Vista que ha provocado el evento: aquí se podría poner tanto v como binding.root. Si tenemos disponible la variable binding es recomendable utilizar esta opción ya que la vista general siempre estará disponible
- Texto que queremos que se muestra
- Duración de la notificación: En este caso se ha optado por una longitud corta (3-4 segundos), pero se puede configurar como larga (LONG, 6-7 segundos) o indefinida (INDEFINITE)

Todos los eventos tienen la misma estructura, una función que se ejecuta en el momento de provocar la acción, pero esta función puede cambiar dependiendo del tipo de evento que se provoque. En el caso de la pulsación de un botón o cualquier elemento estamos hablando de que la función ejecutada es la de onClick, pero tenemos multitud de posibilidades. Aquí tenemos algún ejemplo de los principales que podemos utilizar:

| Nombre | Métodos asociados | Uso |
| --- | --- | --- |
| OnClickListener | onClick(view: View); | Detecta la pulsación de un elemento. Sobre todo, es utilizado en la pulsación de botones |
| OnLongClickListener | onLongClick(v: View): boolean | Detecta la pulsación prolongada sobre un elemento. Sobre todo, es utilizado en la pulsación larga de botones |
| OnCheckedChangeListener | onCheckedChanged(buttonView: CompoundButton, isChecked: boolean) | Detecta el cambio de estado en un elemento que tenga varios, como por ejemplo un checkbox, radiobuttons, switch, et… |
| OnItemSelectedListener | onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) onNothingSelected(parent: AdapterView<*>?) | Detecta el cambio de selección dentro de un elemento de tipo spinner |
| OnTouchListener | onTouch(v: View?, event: MotionEvent?): Boolean | Detecta un toque en cualquier elemento. No se trata de una acción de pulsación, simplemente de toque en pantalla como por ejemplo un zoom |

Como podemos ver en la tabla anterior, hay una cosa común a todos los métodos de los listenes y es que todos los métodos asociados tienen un parámetro que es de tipo View o ButtonView. Esto es porque cuando se genera un evento uno de los parámetros que genera el evento es la vista que ha provocado dicho evento. Mediante este parámetro podríamos definir por ejemplo el origen y actuar de forma diferente ante ellos.



```kotlin
class MainActivity : AppCompatActivity(), OnClickListener{

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater);
        setContentView(binding.root)
                 binding.botonUno.setOnClickListener(this)
        binding.botonDos.setOnClickListener(this)
    }

    override fun onClick(v: View?) {
        when(v?.id){
            binding.botonUno.id->{
                // acción especifica para el boton uno
            }
            binding.botonDos.id->{
                // acción especifica para el boton dos
            }
        }
    }
}
```



Otra de las cosas importantes a tener en cuenta cuando se tratan eventos, es el número de métodos asociados que tiene la interfaz. En el caso de tener solo un método asociado se puede hacer una asociación directa o la implementación de la interfaz. En el caso de la asociación directa quedaría de la siguiente forma:



```bat
binding.checkComprobar.setOnCheckedChangeListener { buttonView, isChecked ->  }
binding.botonUno.setOnClickListener {  }
```



En el primer ejemplo se ha realizado una asociación directa sobre un checkbox, aplicando el listener de comprobar el estado del botón. Los dos parámetros que tiene la función (onCheckedChanged) son el elemento que ha provocado el cambio y el estado de este. En el segundo ejemplo se ha asociado la pulsación sobre un botón, si tener ningún parámetro escrito ya que al ser una función (onClick) que solo tiene uno se puede utilizar it.

Sin embargo, si queremos hacer esto con interfaces que tienen más de un método asociado no podemos hacerlo de esta forma. Las opciones que tenemos son la de la asociación con la implementación de la interfaz como hemos contado antes o la asociación de objeto anónimo tipado como el elemento que queremos comunicar. Un claro ejemplo es el tratamiento de la selección dentro de un spinner. El evento en cuestión a tratar es la interfaz OnItemSelectedListener con dos métodos asocidos. Las formas de tratarlo son la implementación de la interfaz:



```kotlin
class MainActivity : AppCompatActivity(), OnItemSelectedListener{

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater);
        setContentView(binding.root)
        binding.spinnerSeleccion.onItemSelectedListener = this;
    }
         override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        TODO("Not yet implemented")
    }

    override fun onNothingSelected(parent: AdapterView<*>?) {
        TODO("Not yet implemented")
    }
}
```



A diferencia de casos anteriores, ahora se trata como propiedad al tener los dos métodos comentados. La otra posibilidad es crear el objeto anónimo que permite implementar directamente ambos métodos



```kotlin
binding.spinnerSeleccion.onItemSelectedListener = object : OnItemSelectedListener{
    override fun onItemSelected(
        parent: AdapterView<*>?,
        view: View?,
        position: Int,
        id: Long     ) {
        TODO("Not yet implemented")
    }

    override fun onNothingSelected(parent: AdapterView<*>?) {
        TODO("Not yet implemented")
    }

};
```



Ambas posibilidades son totalmente válidas, siendo más recomendable la primera en el caso de querer asignar la misma acción sobre spinner diferentes, tal y como se muestra en el video.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652019_1/scormcontent/assets/INSD_DM_Unidad1_Apartado5_3_Video.mp4?v=1)



### 4.4 Gestión de estados



Como se ha visto antes, toda activity cumple un ciclo de vida, por lo que de forma automática se ejecutan métodos dependiendo de cuales sean los eventos que ocurren en el teléfono. Por ejemplo, si estamos ejecutando una aplicación y nos llega una llamada a nuestro teléfono, la aplicación pasará a estar pausada y al terminar la llamada pasará por los estados stop, destroy y luego onCreate por lo que volverá a ejecutar todo lo que tenemos en el dicho método como la asociación del layout, inicialización de valores, etc… Esto puede provocar una pérdida de datos, en el proceso de reconstrucción de la aplicación no ha sido persistidos de ninguna forma. Este escenario nos lo vamos a encontrar en el caso de que nuestra aplicación sea movida a segundo plano o cuando la configuración del dispositivo cambie (tal y como se mostró en un video anterior) de configuración, bien sea cambiar idioma, orientación, etc…

Para evitar la pérdida de los datos es necesario guardar el estado de todos aquellos datos que queramos mantener. Para ello imaginemos el siguiente ejemplo: una aplicación que consta de dos botones y un contador donde al pulsar cada uno de los mismos incrementa o decrementa el texto de la etiqueta. En su parte gráfica tendríamos lo siguiente:



![image](assets/cm6e0e3s004h63570l8sk3nbu-Imagen14.jpg)



En cuanto a la parte lógica tendríamos el siguiente código:



```kotlin
class MainActivity : AppCompatActivity(), OnClickListener {

    private lateinit var binding: ActivityMainBinding     
    private var contador: Int = 0;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.textoContador.text = contador.toString()
        binding.botonIncremento.setOnClickListener(this)
        binding.botonDecremento.setOnClickListener(this)
   
    }

    override fun onClick(v: View?) {
        when(v!!.id){
            binding.botonIncremento.id->{
                contador++
            }
            binding.botonDecremento.id->{
                contador--
            }
        }
        binding.textoContador.text = contador.toString()
    }
}
```



En el caso de realizar una serie de pulsaciones en cada uno de los botones, según la lógica programada, el contador se moverá, mostrando el resultado actual. Pero en en el caso de girar el móvil se provocará un cambio de configuración, una nueva ejecución del método onCreate y por lo tanto una nueva asignación de la variable contador por lo que su valor se reiniciaría a 0. Para poder guardad el dato antes del cambio de configuración existe un método que guarda el conjunto de datos que queramos mediante un par clave – valor. Dicho método lo podemos sobrescribir y se ejecutará automáticamente en el momento anterior a la destrucción de la activity. Este método se llama onSaveInstanceState



```kotlin
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    outState.putInt("contador",contador)

}
```



El parámetro outState que nos ofrece el método servirá para guardar el valor indicado con la clave indicada. En el ejemplo, se asigna una clave llamada “contador” y el valor guardado es el clave contador mediante el método putInt(). Una cosa importante es que esta “persistencia” tan solo se trata de algo temporal, ya que no se mantiene si la aplicación se destruye de forma completa (es decir se cierra de forma definitiva). Lo último que quedaría es recuperarlo, utilizando el parámetro savedInstanceState del método onCreate. Hay que recordad que este guardado del estado se utiliza para recuperarlo cuando la aplicación se crea. Para poder recuperarlo se hace de la misma forma que el guardado, preguntando por la clave del dato que queramos obtener:



```ini
contador = savedInstanceState?.getInt("contador") ?: 0
```



En este caso, como el parámetro savedInstanceState puede ser nulo (por ejemplo cuando arranca la activity) hay que tratar el posible nulo con la ?. En el caso que el elemento sea nulo, no se ejecutará el valor y por lo tanto se le asignará a la variable contador un valor de 0.



### 4.5 Internacionalización y uso de recursos múltiples



En Android Studio, la internacionalización se logra principalmente a través del uso de archivos de recursos de cadena (strings.xml). Estos archivos contienen todas las cadenas de texto utilizadas en la aplicación. Para cada idioma que se quiera soportar, se crea un archivo strings.xml separado en una carpeta de recursos específica del idioma (por ejemplo, values-es para español, values-fr para francés, etc.).

Cuando la aplicación se ejecuta, Android selecciona automáticamente el archivo strings.xml apropiado basándose en la configuración de idioma y región del dispositivo del usuario. Si no existe un archivo de recursos para el idioma del dispositivo, Android utilizará el archivo de recursos predeterminado (values/strings.xml).

Además de los archivos de recursos de cadena, Android Studio también permite la internacionalización de otros tipos de recursos, como imágenes y diseños, mediante el uso de carpetas de recursos específicas de la configuración.

Es importante tener en cuenta que la internacionalización es solo el primer paso para hacer que una aplicación sea verdaderamente global. El siguiente paso, la localización, implica la traducción y adaptación efectiva de la aplicación al idioma y las convenciones culturales de cada región objetivo.

En el siguiente video se muestra como poder hacer dicha internacionalización.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652019_1/scormcontent/assets/INSD_DM_Unidad1_Apartado5_5_Video.mp4?v=1)



Otro de los aspectos que se pueden tratar con la gestión de recursos múltiples es la orientación de la pantalla. Imaginemos una aplicación que se ve de la misma forma en horizontal y en vertical. En este caso la apariencia va a ser muy poco amigable en una de las dos orientaciones ya que el espacio es totalmente diferente en cada una de ellas. Por ello la orientación de la pantalla es un aspecto crucial en el diseño de aplicaciones móviles. Los dispositivos móviles pueden ser utilizados en orientación vertical (portraint) y horizontal (landscape), y los usuarios a menudo cambian entre estas orientaciones mientras usan una aplicación. Por lo tanto, es importante que tu aplicación pueda adaptarse a ambos modos de visualización para proporcionar una experiencia de usuario óptima.

Crear diferentes layouts para cada orientación de pantalla permite optimizar el uso del espacio disponible y garantizar que la interfaz de usuario se vea bien y funcione correctamente en ambas orientaciones. Por ejemplo, en la orientación de paisaje, puedes aprovechar el espacio adicional para mostrar más contenido o para presentar el contenido existente de una manera diferente.



En Android Studio, puedes crear diferentes layouts para cada orientación de pantalla utilizando carpetas de recursos específicas de la configuración. Para ello se realizan los siguientes pasos:

1. En primer lugar, debes crear un layout básico en la carpeta de recursos res/layout. Este será el layout predeterminado que se utilizará si no hay un layout específico para la orientación de la pantalla actual.
2. A continuación, puedes crear una nueva carpeta de recursos para la orientación de paisaje (res/layout-land) o retrato (res/layout-port).
3. Copia el archivo de layout que creaste en el primer paso en la nueva carpeta de recursos y modifícalo para optimizarlo para la orientación correspondiente. En este paso es muy importante que todos aquellos elementos que sean compartidos por ambas orientaciones tengan el mismo id tanto en el fichero del layout de orientación portraint como landscape.
4. Cuando la aplicación se ejecuta y cambia la orientación de la pantalla, Android seleccionará automáticamente el layout apropiado basándose en la orientación actual del dispositivo.



### 4.6 Intents



Otro de los elementos básicos de una aplicación android son los intents. Este tipo de objeto permite desde código realizar tareas como navegar entre pantallas, lanzas aplicaciones del sistema como el navegador, mapas, cámara, etc..., en resumen una acción que puede ser definida por el usuario o definida en la URI con la que se configura el el propio objeto. Antes de empezar a ver las opciones de este tipo de elementos, comentar que su creación y lanzamiento se puede realizar de forma explícita (creando el objeto y sus datos en la parte lógica con el constructor del intent) o implícitos (definiendo sus acciones en el fichero AndroidManifest.xml o desde la URI que define la acción). A continuación, vamos a ver los principales usos que tiene este tipo de objetos.



#### Comunicación entre activitys



Uno de los principales usos de los intents es el de navegar a otra actividad, con o sin datos asociados. Para ello es necesario tener dos activitys, cada una con su parte gráfica y su parte lógica. Para poder serguir el ejemplo cada una de las pantallas tendrá a siguiente funcionalidad:



- **MainActivity**  
  Tendrá un botón que al ser pulsado llevará a la segunda pantalla.
- **SecondActivity**  
  Contará de una etiqueta en el centro de la pantalla con el texto Pantalla dos. Para poder crear una segunda pantalla es necesario crear tanto el fichero .kt como el .xml y declarar la activity dentro del fichero AndroidManifest.xml. Además de este proceso, también es posible utilizar el asistente de creación pulsando botón derecho new -> activity -> empty activity indicando el nombre de la actividad. Este proceso creará automáticamente todos los ficheros relacionados y actualizará el fichero AndroidManifest con la nueva actividad.



Una vez creadas las dos activitys es hora de crear el intent que permite realizar la acción de cambio de pantalla. Para ello, en la pulsación del botón de la primera activity crearemos el siguiente código



```kotlin
val intent: Intent = Intent(this, SecondActivity::class.java)
startActivity(intent)
```



En el intent, es necesario pasarle dos parámetros, siendo el primero el contexto desde donde estamos ejecutando la aplicación (en este caso la MainActivity) y como segundo parámetro la clase que representa la activity destino, siendo la SecondActivity la del ejemplo. Tras la creación y con la ejecución del método startActivity pasando como parámetro el intent creado se realizará el cambio de pantalla.

En el caso de querer realizar un intent implícito, es el sistema el que se encarga de decidir que pantalla es la que se tiene que hacer. Generalmente, el sistema realiza esto dependiendo de la acción que se indique y de la URI (Universal Resource Identifier) configurada. Para ellos y al igual que se ha hecho antes es necesario crear una variable de tipo intent, indicando en el constructor la acción (Action_View es la más genérica). Además de esto es necesario indicar los datos que acompañarán a la petición (ya que al abrir una pantalla como por ejemplo el navegador, es necesario indicar la página que será mostrada)



```kotlin
val intent: Intent = Intent(Intent.ACTION_VIEW);
intent.setData(Uri.parse("<https://www.u-tad.es"))
startActivity(intent)
```



Además de poder arrancar una sengunda activity, el uso de los intents también permite el paso de parámetros entre ellas, siendo muy útil en el caso de querer procesar datos en pantallas diferentes. Esto es posible si al intent utilizar para pasar de pantalla se se agregan los datos utilizando el método putExtra(), identificando los datos con un par clave valor al igual que en un map. Para poder verlo mejor realizaremos un ejemplo donde se pasará un texto entre la primera y segunda pantalla. Los pasos a seguir sería.



1. En el archivo activity_main donde definimos la ui de la primera pantalla se va a incluir un editText con el id editNombre



```xml
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="<http://schemas.android.com/apk/res/android>"
    xmlns:app="<http://schemas.android.com/apk/res-auto>"
    xmlns:tools="<http://schemas.android.com/tools>"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">
 
    <EditText
        android:id="@+id/edit_nombre"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:hint="Introduce tu nombre"
        android:layout_marginBottom="16dp"
        app:layout_constraintBottom_toTopOf="@+id/boton_pasar"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent" />
 
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Pasar pantalla"
        android:id="@+id/boton_pasar"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
 
</androidx.constraintlayout.widget.ConstraintLayout>
```



2. En el archivo MainActivity.kt realizamos el paso entre pantallas, pero antes de ejecutar el método startActiviy es necesario acompañar al intent con los datos que se quieran pasar. Esto se hace con el método putExtra, indicando la clave asociada y el dato a pasar. Una ves estamos en este punto los datos ya se han pasado al destino



```kotlin
val intent = Intent(this, SecondActivity::class.java)
intent.putExtra("nombre", binding.editNombre.text.toString())
startActivity(intent)
```



3. Para poder recuperar los datos, en el archivo SecondActivity.kt se podrá capturar mediante el intent que ha arrancado la pantalla y el método getExtra, indicando la clave del dato que se quiere recuperar



```ini
intent.extras?.getString("nombre").toString();
```



Es muy importante que entendamos que todas las pantallas tienen una variable llamada intent, ya que todas las pantallas son arrancadas de una manera y otra. Mediante el atributo extras se recuperan todos los datos pasados y en concreto utilizando el método getString con la clave asociada al dato que queramos capturar tendremos dicho elemento. Tiene especial relevancia la ? que acompaña al intent.extra ya que el dato puede ser nulo por varios motivos:

1. La pantalla que ha arrancado no ha pasado datos extras: hay que tener en cuenta que una activity se puede arrancar desde varios sitios y de formas diferentes
2. La pantalla que se arranca al pulsar el icono de la aplicación también tiene un intent que la ha arrancado (en este caso implícito), por lo que en este caso es imposible que tenga extras.

Con este tipo de cosas nos aseguramos de que los datos han llegado y en caso contrario poder tratarlos de alguna manera para que no tengamos problemas de nulos.



### 4.7 Depuración de código



Uno de los aspectos claves cuando se programa, es la comprensión y generación de código limpio. Pero es normal que, durante la codificación de un programa, determinadas partes fallen y sea necesario realizar una depuración de código para determinar el fallo y ponerle solución. Android Studio, además del depurador tradicional que incorporan todos los IDEs, tiene una herramienta llamada LogCat que permite ver la parte de código así como un filtrado de los datos que se generan desde la ejecución. Para poder ver la herramienta es necesario acceder a ella a través de menú View -> Tools Window -> Logcat. Una vez activada, aparecerá en la parte inferior del IDE.



![image](assets/cm6e2mo32052n3570xnue24kd-Imagen16.jpg)



En esta herramienta, podremos seleccionar el emulador o dispositivo desde el cual queremos evaluar los datos, hacer un filtrado de los datos que queremos ver, así como el tipo de mensaje que queremos mostrar. Si introducimos los siguientes filtros de búsqueda en el input asociado obtendremos la siguiente información:



- **package:mine**  
  Mensajes exclusivos de la aplicación que estamos ejecutando.
- **package:mine level:error**  
  Mensajes de la aplicación que estamos ejecuntando y que sean de tipo error.
- **package:mine tag:mensaje**  
  Mensajes de la aplicación que estamos ejecutando y que están asociados a la etiqueta mensaje. Ahora vemos como poder asociar esta etiqueta.



Con estos filtros podemos visualizar solo la parte de información que nos interesa dentro de la aplicación, pudiendo tener muy claro que parte de esta ha fallado o si los datos están siguiendo el flujo que nosotros hemos marcado.

Para poder sacar mensajes en el Logcat, desde código debemos utilizar la clase Log de la librería android.util, pudiendo indicar el tipo de nivel que queremos asociar y el mensaje para mostrar. De esta forma podremos forzar un log de la siguiente forma.



```kotlin
override fun onClick(v: View?) {
    Log.v("mensaje", "Este mensaje aparecerá en el logcat cuando el boton sea pulsado")
}
```



La v indica el nivel del mensaje, siendo v verbose, pero también tenemos disponible error, warn, info, assert, debug. Si ejecutamos este código y pulsamos el botón veremos que aparece en el logcat el mensaje con la etiqueta asociada, pudiendo filtrar por ella.



![image](assets/cm6e2sdk1056p3570e8k4fus5-Imagen17.png)



En el caso de producirse un error, el proceso sería el mismo, pudiendo filtrar por leven y obteniendo el motivo del error y la línea donde se ha producido el mismo. Imaginemos que tenemos el siguiente código.



```kotlin
class MainActivity : AppCompatActivity(), OnClickListener{

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        binding.botonUno.setOnClickListener(this)
    }

    override fun onClick(v: View?) {
        Log.v("mensaje", "Este mensaje aparecerá en el logcat cuando el boton sea pulsado")
    }
}
```



En este caso, el error al ejecutar lo obtenemos de la utilización de la variable binding cuando no se ha inicializado, obteniendo el siguiente mensaje dentro del logcat.



![image](assets/cm6e2vcau059a3570qk1imc7m-Imagen19.jpg)



Si analizamos con detalle el mensaje, indica que el error está en la línea 22 con el mensaje de: “lateinit property binding has not been initialized”.

Una de las cosas básicas a la hora de programar es ser capaz de identificar los errores, la parte del código que lo provocan y entender la solución. Errores no hay infinitos, por lo que, si somos capaces de identificarlos y ponerles solución, tan solo tendremos que adaptarlos al proyecto y sus necesidades.



## 5. Conclusiones



### 5.1 Conclusiones de la unidad



Como se ha podido comprobar el desarrollo de aplicaciones Android es un campo apasionante y en constante evolución. A medida que los dispositivos móviles se han convertido en una parte integral de nuestras vidas, la demanda de aplicaciones intuitivas y funcionales ha aumentado significativamente. Dominar el desarrollo en esta plataforma es algo totalmente necesario debido a su alta demanda. Entender conceptos como la gestión de pantallas, creación de interfaces gráficas consistentes y responsive, así como mantener los datos y configurar de forma correcta las acciones que se quieren llevar a cabo dentro de la ejecución es algo básico en este campo. A lo largo de la unidad hemos tratado todos estos conceptos que marcan la base de desarrollo

Algo muy importante para tener en cuenta y que se ha comentado es que todos los elementos están en constante cambio. Estamos ante una disciplina que todos los años lanza una o dos actualizaciones de sistema, por lo que es clave mantenernos actualizados ya que muchas de las cuestiones que hoy en día son básicas, pueden sustituirse en un futuro.
