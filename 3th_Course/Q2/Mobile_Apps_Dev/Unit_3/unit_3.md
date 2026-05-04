# Unidad 3. Desarrollo móvil híbrido con Flutter.



## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Desarrollo Híbrido Vs Desarrollo Nativo](#2-desarrollo-híbrido-vs-desarrollo-nativo)
  - [2.1 Introducción](#21-introducción)
- [3. Flutter](#3-flutter)
  - [3.1 Introducción](#31-introducción)
  - [3.2 ¿Qué son los Widgets en Flutter?](#32-qué-son-los-widgets-en-flutter)
  - [3.3 Instalación y herramientas de SDK](#33-instalación-y-herramientas-de-sdk)
- [4. Dart](#4-dart)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Variables](#42-variables)
  - [4.3 Funciones](#43-funciones)
  - [4.4 Clases](#44-clases)
- [5. Desarrollo De Proyectos En Flutter](#5-desarrollo-de-proyectos-en-flutter)
  - [5.1 Introducción](#51-introducción)
  - [5.2 Estructura de una aplicación en Flutter](#52-estructura-de-una-aplicación-en-flutter)
  - [5.3 Widget](#53-widget)
- [6. Gestión De Estados](#6-gestión-de-estados)
  - [6.1 Introducción](#61-introducción)
  - [6.2 Stateless vs Statefull](#62-stateless-vs-statefull)
  - [6.3 TextEdit](#63-textedit)
  - [6.4 Spinner](#64-spinner)
  - [6.5 CheckBox](#65-checkbox)
  - [6.6 ListView](#66-listview)
- [7. Navegación](#7-navegación)
  - [7.1 Introducción](#71-introducción)
  - [7.2 Navegando](#72-navegando)
  - [7.3 Paso de parámetros](#73-paso-de-parámetros)
- [8. Conclusiones](#8-conclusiones)
  - [8.1 Conclusiones de la unidad](#81-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



Como se ha visto en las unidades anteriores, el desarrollo móvil es una modalidad muy extendida en el mundo del desarrollo software. Por ello es importante conocer todas las posibilidades que existen dentro de este mundo, por lo que esta unidad nos centraremos en un tipo de desarrollo nativo espacial, lo que permite crear proyectos Android, IOs, web y escritorio en un solo desarrollo, utilizando las características de la herramienta Flutter.



- **Desarrollo híbrido vs Desarrollo nativo**  
  Dentro del mundo del desarrollo móvil existen dos grandes vertientes: desarrollo hibrido y desarrollo nativo. La diferencia entre amos tipos de desarrollo es la manera en la que el programador accede a cada uno de los elementos del teléfono sobre el que desarrolla. En el caso de un desarrollo nativo, el acceso se realiza de forma directa, ya que se programa con un lenguaje nativo del sistema operativo, por lo que el acceso es mucho más rápido, lo que hace que la ejecución de la aplicación sea mucho más fluida, así como el acceso a los diferentes componentes del teléfono.
- **Flutter**  
  Flutter es un SDK de código abierto desarrollador por Google que permite crear aplicaciones multiplataforma para Android, IOs, Web y escritorio de forma nativa, con la posibilidad de reutilizar el código en cada una de las plataformas para las que se quiera desarrollar.
- **Desarrollo del proyecto en Flutter**  
  Para poder entender un proyecto flutter, lo primero que hay que hablar es de la composición de una aplicación. Hay un concepto básico en flutter que todo gira alrededor de él, que son los widgets.
- **Gestión de estados**  
  En Flutter, los widgets se dividen en dos grandes categorías: stateless y statefull. Antes de profundizar en sus diferencias, es importante destacar que un mismo widget puede implementarse de ambas formas, dependiendo del propósito que se le quiera dar. En el caso de interesarnos que una pantalla con elementos de tipo Text y botones no conserve los datos introducidos, sino que simplemente se ejecute una acción, como navegar a otra pantalla al presionar un botón, estaríamos ante un widget sin estado.
- **Navegación**  
  Uno de los puntos básicos en una aplicación es la posibilidad de tener más de una pantalla que permita realizar una navegación entre diferentes pantallas tras la pulsación de un botón o cualquier acción. Hasta este momento lo que se ha visto es como poder crear un widget general que representa la pantalla y dentro de éste la organización de diferentes tipos de elementos.



#### Objetivos



Los objetivos que se persiguen en esta unidad son:



1. Conocer el lenguaje de programación DART y sus características.
2. Instalar y configurar Flutter como herramienta de desarrollo móvil multiplataforma.
3. Comprender los diferentes tipos de widgets stateless y statefull.
4. Conocer y utilizar los diferentes tipos de widgets gráficos.
5. Utilizar listas de datos provenientes de la consulta a un API.
6. Gestionar datos desde diferentes tipos clases.



## 2. Desarrollo Híbrido Vs Desarrollo Nativo



### 2.1 Introducción



![image](assets/cm8p29bal004p356x27p80xth-stock-image.jpg)



Dentro del mundo del desarrollo móvil existen dos grandes vertientes: desarrollo hibrido y desarrollo nativo. La diferencia entre amos tipos de desarrollo es la manera en la que el programador accede a cada uno de los elementos del teléfono sobre el que desarrolla. En el caso de un desarrollo nativo, el acceso se realiza de forma directa, ya que se programa con un lenguaje nativo del sistema operativo, por lo que el acceso es mucho más rápido, lo que hace que la ejecución de la aplicación sea mucho más fluida, así como el acceso a los diferentes componentes del teléfono. Lo malo que tiene este tipo de desarrollo es que, en el caso de querer hacer una aplicación para más de un dispositivo, habría que hacer diferentes proyectos utilizando los lenguajes de programación propios de cada sistema operativo o desarrollo, siendo estos los principales:

- **Android:** utilizando el IDE Android Studio y como lenguaje de programación Java o Kotlin
- **IOS:** utilizando el IDE XCODE y como lenguaje de programación Swift o Objective – C

El caso de querer hacer también una aplicación escritorio y web, el problema se multiplicaría ya que estaría hablando de más lenguajes de programación a utilizar

- **Web:** Utilizando HTML y JS como lenguaje de programación, pudiendo usar también Python, PHP, etc….
- **Escritorio:** Utilizando Java, Python, C#, etc. como lenguaje de programación dependiendo del sistema operativo para el que queramos desarrollar

Por tanto, desarrollar aplicaciones para distintas plataformas supone realizar varios tipos de proyectos cada uno de ellos adecuado a cada una de dichas plataformas

En el caso de hacer un desarrollo hibrido, estamos hablando de un desarrollo que permite hacer un solo desarrollo que permite distribuir la aplicación en diferentes plataformas tan solo con un desarrollo. Estas plataformas (Android, IOs, web, escritorio), utilizan un framework común de desarrollo como javascript para poder hacer esto. Es evidente que lo bueno que tiene el desarrollo de este tipo es que solo es necesario un proyecto que será necesario para la distribución a diferentes plataformas. Lo malo que tiene es que el acceso sobre los componentes que programamos no se realiza de forma nativa ya que se realiza a través de librerías, lo que hace que la ejecución no sea tan fluida y eficiente como el desarrollo nativo. Para este tipo de desarrollos existen diferentes tipos de frameworks, siendo los principales IONIC, ReactNative y VUE Mobile, todos ellos basados en navegador y por lo tanto JavaScript.

Sin embargo, existe una solución intermedia que permite hacer un desarrollo nativo cross-platform sin necesidad de tener que crear un proyecto para cada plataforma. Se trata de Flutter una herramienta desarrollada por Google que permite un desarrollo nativo para cada plataforma, reutilizando código. Con esto, seguimos teniendo las ventajas de un código nativo para poder tener un acceso rápido y fluido, al mismo tiempo que tenemos la posibilidad de crear tantos proyectos como sean necesarios.



![image](assets/cm8p2cbht005a356xss0se7ci-Imagen2.jpg)



## 3. Flutter



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



Flutter es un SDK de código abierto desarrollador por Google que permite crear aplicaciones multiplataforma para Android, IOs, Web y escritorio de forma nativa, con la posibilidad de reutilizar el código en cada una de las plataformas para las que se quiera desarrollar. Aunque por defecto siempre la decisión sea realizar un desarrollo nativo para nuestras aplicaciones, soluciones como la que propone Flutter es una opción sería a tener en cuenta para poder minimizar gastos y esfuerzos para llevar a cabo el proyecto de forma correcta. Por defecto, flutter está desarrollado en C/C++ lo que hace que se pueda acoplar fácilmente a cada una de las plataformas. Sin embargo, cuenta también con una llamada a un API de alto nivel, por lo que cuando se escriben proyectos en Flutter en realidad se hacen en el lenguaje de programación Dart, del que hablaremos más adelante. Además de esto, Flutter cuenta con un motor de renderizado propio llamado Skia que permite que la renderización nativa en cada una de las plataformas.

Esta arquitectura de capas independientes permite que cada una de ellas trabaje de forma independiente, donde cada una de ellas tiene la siguiente funcionalidad:



![image](assets/cm8p2jhvf00bv356xayyztbr5-Imagen3.jpg)

- **Capa framework**  
  Desarrollada en lenguaje de programación Dart, posibilitando a los programadores un manejo de los elementos mediante un lenguaje claro y moderno. Dentro de esta capa, podemos diferencias:

  - Bibliotecas Material y Cupertino, encargadas de diferenciar los diseños para Android e IOs respectivamente.
  - Widgets, los grandes pilares de Flutter de los que hablaremos más adelante. De forma general se trata de los controles de la aplicación.
  - Rendering, encargado de la representación de cada uno de los componentes de la aplicación
  - Bibliotecas básicas, encargadas de animaciones, control de gestos, etc…
- **Engine**  
  El motor de Futter, escrito en C++ y responsable de la renderización de cada uno de los frames de la aplicación. Se trata de un acceso de bajo nivel, utilizando el motor gráfico SKIA para la renderización de componentes a cada una de las plataformas.
- **Embeded**  
  Capa encargada de empaquetar la aplicación final al formato nativo correspondiente. En realidad, esta capa es la que realiza toda la “magia” de generar diferentes proyectos partiendo de un nexo común.



Una vez comprendido cual es la estructura interna de flutter, se va a explicar ahora uno de los conceptos más importantes de la herramienta: los widgets.



### 3.2 ¿Qué son los Widgets en Flutter?



Como en cualquier herramienta de desarrollo de aplicaciones, uno de los principales elementos que forman parte de ésta son los elementos gráficos. En unidades pasadas vimos que en Android estos elementos recibían el nombre de widgets y podemos representar con ellos botones, listas, desplegables, etc. En flutter es exactamente lo mismo, con la diferencia que podemos definir un widget como los elementos de interfaz gráfica de usuario, pero no solo aquellas cosas que se ven como los mencionados anteriormente, sino todos los elementos que están dentro de la aplicación: pantallas, columnas, zona de exclusión de los elementos, etc. Al principio este concepto es algo diferente a lo que estamos acostumbrados a ver, por lo que podemos decir que un widget es todo aquello que forma parte de una aplicación de flutter. Se explicará más adelante con detalle, pero los widgets básicos de una aplicación flutter son:

- **Scaffold:** Estructura visual básica de una aplicación con elementos Material Design, dentro de la cual se colocan el resto de los elementos.
- **Container:** Elemento que permite acotar el espacio físico que ocupan los componentes que están dentro.
- **AppBar:** Parte superior de la aplicación, también llamada barra de aplicaciones.
- **Column:** Gestor del espacio que permite colocar los elementos de forma vertical.
- **Row:** Gestor del espacio que permite colocar los elementos de forma horizontal.
- **Text:** Elemento que muestra un texto concreto, pudiendo modificarlo mediante lógica
- **TextField:** Elemento que permite la captura de un texto por parte del usuario.

De forma general, estos widgets se pueden clasificar en dos grades grupos:



- **Stateless**  
  Aquellos que no necesitan guardar ningún dato ni persistir datos, simplemente los muestran en pantalla.
- **Statefull**  
  Aquellos que si requieren persistir algún dato para poder procesarlos en algún momento. Hay que tener en cuenta que un widget no tiene por qué ser un solo elemento, sino que puede ser el conjunto de unos cuantos, como por ejemplo un formulario completo formado a su vez por varios widgets.



### 3.3 Instalación y herramientas de SDK



Para poder instalar flutter como herramienta de desarrollo no existe un instalador donde con un asistente quede instalado, sino que se descarga en formato librería, para más adelante incorporarlo dentro del IDE que consideremos oportuno. Para la instalación del SDK hay que realizar los siguientes pasos:

1. Descargar flutter de la página web oficial [https://docs.flutter.dev/get-started/install](https://docs.flutter.dev/get-started/install)
2. Una vez descargado el fichero, es necesario descomprimirlo en la carpeta llamada flutter. En este punto es importante la ruta donde lo hacemos, ya que más adelante la necesitaremos para poder iniciar el proyecto.
3. Configurar el comando flutter como variable de entorno. Este paso no es obligatorio, pero si recomendable ya que luego facilitará la creación de proyectos y compilación. Para configurarlo podemos ver cómo hacerlo en la página web de instalación, dependiendo del sistema operativo ([https://docs.flutter.dev/get-started/install/macos/mobile-ios](https://docs.flutter.dev/get-started/install/macos/mobile-ios)).
4. Una vez seguidos estos pasos, lo último que queda es (tanto en windows como en mac) ejecutar el comando flutter doctor (ejecutado desde la ruta donde se descomprimió la carpeta descargada). Este comando saltará un aviso de todas las instalaciones necesarias que deberemos tener para poder desarrollar en flutter. Entre estos requisitos esta:

   - Visual Studio Code con extensiones de Dart y Flutter
   - Android Studio con licencias de android aceptadas y plataformas instaladas
   - Virtual devices desplegados
   - Chrome
   - Cocoa y XCode en el caso de MacOS

   Además de instalaciones locales, habrá que aceptar las licencias de Android mediante la ejecución del siguiente comando flutter doctor --android-license



El último punto es seleccionar el IDE mediante el cual queremos realizar los desarrollos. Si bien en el proceso de instalación se requiere de Visual Studio Code, también podemos utilizar cualquiera de los IDES oficiales de desarrollo de aplicaciones. En nuestro caso utilizaremos Android Studio. Para lo cual es necesario instalar los plugins de Dart y Flutter dentro del mismo. En el siguiente video, además de la instalación se muestra la instalación de dichos plugins y la creación de un primer proyecto.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652025_1/scormcontent/assets/INSD_DM_Unidad3_Apartado4_2_Video.mp4?v=1)



Con todo esto, podremos empezar el desarrollo de nuestras aplicaciones



## 4. Dart



### 4.1 Introducción



![image](assets/cm8p34yvv00ko356x9q3eidsp-stock-image.jpg)



Flutter se base en un lenguaje de programación llamado Dart desarrollado por Google. Se trata de un lenguaje de ejecución y codificación rápida, que mezcla características de muchos de los lenguajes de programación existentes hoy. Antes de empezar con la sintaxis del lenguaje, hay que comentar que al igual que otros lenguajes de programación, flutter cuenta con un método main sobre el cual comienza todas las ejecuciones



```css
void main() {
    print('Hola Mundo');
}
```



### 4.2 Variables



Existen dos grandes tipos de variables en dart en cuanto a su creación: variables mutables y no mutables. Las variables mutables utilizan la palabra reservada var. Una cosa importante a tener en cuenta es que si definimos una variable con un tipo concreto, ya no podremos utilizar la declaración como var, ya que su tipo le acompañará en toda la vida de la variable.



```bat
var nombre = "Borja"
```



Las variables no mutables son aquellas que no cambian en ningún momento. Existen dos tipos, cuya diferencia es el momento en el que se crean:

- **const:** inicializado en compilación
- **final:** inicializado en ejecución

Otras de las características que tiene el lenguaje de programación es el uso de valores por defecto o null safety, conocido en otros lenguajes como Kotlin. Para poder utilizar esta características se utiliza el signo ? después del tipo de la variable, para indicar que no tiene un valor asignado.



```ini
int? edad;
```



### 4.3 Funciones



Las funciones representan la parte de código reutilizables que son ejecutadas con la llamada de esta. Para poder definir una función se utiliza la siguiente sintaxis:



```css
void nombreFuncion(){

}
```



Donde void es el tipo de retorno que tendrá. Del mismo modo, las funciones pueden admitir parámetros los cuales pueden ser llamados de muy diferentes formas.

- Parámetros normales



```lua
void main() {
    registrarUsuario("Borja", "Informática")
}

void registrarUsuario(nombre, departamento){
  print('El usuario con nombre $nombre, ha quedado registrado en el departamento $departamento');
}
```



- Parámetros optativos

Son aquellos que no son obligatorios pasar a la función para que esta se ejecute con normalidad. En el caso de que no sean pasados obtendrán el valor por defecto puesto.



```sql
void registrarUsuario(nombre, departamento, [salario=0]){
  print('El usuario con nombre $nombre, ha quedado registrado en el departamento $departamento');
  if (salario!=0){
    print('Con un salario asignado de $salario');
  }
}
```



En ambos casos, a los parámetros se les puede indicar el tipo, para así forzar al compilador a que se asigne un valor de tipo concreto.

- Parámetros nominales

En vez de pasar los parámetros por posición, se pueden pasar mediante nombres. En este caso se engloban entre {}



```dart
void main() {
    registrarUsuario(nombre: "Borja",departamento: "Informática", salario: 100);
}

void registrarUsuario({required nombre, required departamento, salario}){
  print('El usuario con nombre $nombre, ha quedado registrado en el departamento $departamento');
  if (salario!=0){
    print('Con un salario asignado de $salario');
  }
}
```



### 4.4 Clases



A la hora de trabajar con clases, como todo lenguaje programado a objetos, una clase representa el molde de un tipo. Para crear una clase basta con utilizar la palabra reservada class y el nombre que le queramos dar.



```css
class Usuario {
  var nombre;
  var apellido;
  var telefono;
}
```



En el caso de querer declarar alguna de ellas como privada para que no sean visibles desde fuera del paquete, tendremos que marcarla con el carácter _

Para poder utilizar un objeto de forma correcta, es necesario utilizar un constructor. Hay varios tipos de constructores:

- **Constructor de clase**

Se trata del constructor "normal", donde se indican los parámetros que deben ser pasados y estos se igualan a cada una de las propiedades



```dart
class Usuario {
  var _dni;
  var nombre;
  var apellido;
  var telefono;

    Usuario(String nombre, String apellido, int telefono){
        this.nombre = nombre;
        this.apellido = apellido;
        this.telefono = telefono;
    }
}
```



Una vez declarado el constructor, ya se podría crear un objeto con dichos datos.



```dart
void registrar({nombre, apellido}) {
  var usuario = new Usuario("Borja", "Martin", 1234);
  print(usuario.nombre);
  print(usuario.apellido);
  print(usuario.telefono);
}
```



De la misma forma se podrían crear constructores con parámetros nominales



```javascript
Usuario(String nombre, String apellido, int telefono, {required dni}) {
    this.nombre = nombre;
    this.apellido = apellido;
    this.telefono = telefono;
    _dni = 123;
  }
// llamándolo de la siguiente forma
new Usuario(dni: 123,"Borja", "Martin", 1234)
```



- **Constructores resumido:**

Otra de las formas de crear un constructor es inicializar directamente cada una de las propiedades de la clase. Para ello, además de existir cada una de las propiedades como variables de clase, se creará un constructor con la siguiente forma:



```dart
class Usuario {
  var _dni;
  var nombre;
  var apellido;
  var telefono;

  Usuario(this.nombre, this.telefono, this.apellido);
}
```



- **Constructores nominales**

Además de los dos tipos de constructores vistos en los puntos anteriores, existe una tercera posibilidad de crear un objeto. Con los vistos hasta este momento, es imposible tener más de un constructor. Para hacerlo, se puede crear un constructor, siempre y cuando, se cree de forma nominal, utilizándolo como si fuese un método más, de la siguiente forma



```javascript
class Usuario {
  var _dni;
  var nombre;
  var apellido;
  var telefono;
  var correo;

  Usuario({this.nombre, this.telefono, this.apellido = 0000, required this.correo});
  Usuario.sinApellido(this.nombre, this.telefono, this.correo);
  Usuario.sinCorreo(this.nombre, this.telefono, this.apellido);
}
```



Con el código anterior, tendríamos la posibilidad de crear un objeto de tres diferentes formas:



```typescript
  var usuario1 = new Usuario(correo: "borja@correo.es",nombre: "borja",apellido: "Martin");
  var usuario2 = new Usuario.sinCorreo("borja",123, "Martin");
  var usuario3 = new Usuario.sinApellido("borja",123, "borja@correo.com");
```



Uno de los métodos más importantes y utilizados dentro de las clases son los getter y setter. Estos métodos proveen de acceso y modificación a las variables de la clase, los cuales pueden ser privados (colocando un _ antes de la definición de la variable). En el caso de querer accederlas, es necesario utilizar los métodos getter y setter, los cuales se acceden como si fuesen una variable, aunque son métodos



```dart
void set nombre(String nombre){
    this._nombre = nombre;
  }

  String get nombre{
    return this._nombre;
  }
```



## 5. Desarrollo De Proyectos En Flutter



### 5.1 Introducción



![image](assets/cm8p3q8r401a4356x00kvoqts-stock-image.jpg)



Para poder entender un proyecto flutter, lo primero que hay que hablar es de la composición de una aplicación. Hay un concepto básico en flutter que todo gira alrededor de él, que son los widgets. Se dice que en flutter todo son widgets y en realidad es así. Un widget es cada elemento que se puede ver dentro de la pantalla, desde el elemento más simple (una etiqueta de texto) hasta la propia pantalla, depende de cuál sea el cometido de éste, más adelante veremos también que hay widgets con estado y sin estado.



### 5.2 Estructura de una aplicación en Flutter



Podríamos decir, que, una aplicación de flutter es un árbol de widgets, los cuales combinados forman una aplicación funcional:



![image](assets/cm8p3t11z01c8356xpvzjxpxe-Imagen4.png)



Como se puede ver en la imagen todo parte de un elemento llamado MyApp, terminando en los widgets finales de texto e icono. En esta jerarquía, podemos diferenciar entre widgets finales (aquellos que representan un elemento como texto o icono) y widgets contenedores (aquellos que tienen otros widgets dentro). Esta diferenciación es sobre elementos gráficos, pero en cuanto a funcionalidad existen dos tipos de widgets:



- **Stateless**  
  Aquellos widgets que no tienen estado, es decir que tan solo se utilizan para mostrar información y no recogerla y/o guardarla para tratarla de alguna forma.
- **Statefull**  
  Aquellos widgets que, sí tienen estado, por lo que pueden recoger información y guardarla para procesarla. Para ello, este tipo de widgets tienen un método especial llamado setState() que modifica esta condición.



En cuanto a rendimiento, el uso de statefull es mucho más pesado ya que cada vez que cambia el estado de la aplicación se debe recargar internamente, por lo que se recomienda en la medida de lo posible utilizar stateless. En el siguiente video se muestra cómo se crea el proyecto y tanto la estructura de carpetas como la estructura básica de la aplicación



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652025_1/scormcontent/assets/INSD_DM_Unidad3_Apartado6_Video.mp4?v=1)



Antes de empezar con el proyecto, merece la pena detenernos en la estructura del código que representa un widget



```dart
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}
```



En este ejemplo podemos que ver el widget principal es de tipo stateless. Todo widget tiene un método llamado build que admite un contexto y que retorna un widget. Este retorno es un widget ya creado llamado MaterialApp, el cual tiene como parámetros en el constructor (nominales) un title, un theme y un home (que a su vez es otro widget). MaterialApp es el widget básico creado por Flutter para utilizar elementos de tipo material.

El siguiente paso sería crear la clase llamada MyHomePage, la cual está situada en el home. Dicha clase será otro widget representado con el código que se muestra a continuación:



```dart
class MyHomePage extends StatelessWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(title)),
      floatingActionButton:
          FloatingActionButton(onPressed: () {}, child: const Icon(Icons.comment)),
      body: const Center(child: Text("Primera app en Flutter"),),
    );
  }
}
```



La clase extiende de stateless widget por lo que no puede guardar estado. En este caso el widget retorna un Scaffold, el cual representa el contenedor (a diferencia de MaterialApp que representa la pantalla) del resto de widgets. Como se puede ver, los elementos que se pasan en el constructor son: appbar, floatingactionbutton y body.

Esta sería la estructura básica de una aplicación que tiene elementos que no guardan estado. En el caso de querer utilizar algún elemento de este tipo deberíamos crear una clase que extendiese de statefull , cuya estructura es la siguiente:



```dart
class FormState extends StatefulWidget{
  @override
  State<StatefulWidget> createState() {
    return _FormWidgetState
  }
}

class _FormWidgetState extends State<FormWidgetState> {
  String name = "";
  int number = 0;
}
```



Siempre que se crea un widget StateFull, hay que tener dos clases:

- Una primera clase que extiende de StatefulWidget, la cual representa el widget completo. Esta clase tienen que sobrescribir el método createState para retornar un estado.
- Una segunda clase que extiende de State con el tipado de la clase creada en el punto anterior para que se pueda crear un estado. Esta clase actúa como los widgets sin estado, sobrescribiendo el método build el cual retorna un widget. La particularidad de esta clase es que tienen un método setState que permite cambiar el valor de alguna de las variables que forman parte de la clase.

Más adelante veremos ejemplos reales de cada uno de los de estos widgets.

Una vez que tenemos creado el proyecto, vamos a empezar de cero, por lo que dentro del archivo main.dart ubicado en la carpeta lib eliminaremos todo el contenido. Lo primero que se creará es la función main, que representa el punto de entrada de la aplicación:



```json
void main(){
  
}
```



Dentro de este método será necesario llamar al método runApp que es el principal de la aplicación, pasando como parámetros un widget. Para ello será necesario crear una clase que represente a éste. Aquí es donde se debe tomar la primera decisión: crear un widget con estado o sin estado. De forma general la pantalla completa se suele utilizar como widget sin estado ya que en el caso de necesitarlo se podría utilizar en uno creado internamente. Por ello se creará un widget sin estado llamado MyApp



```dart
class ContadorApp extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
  }
}
```



Como todos los widgets sin estado, es necesario sobreescribir el método build que retorna el widget ya configurado, con cada uno de los componentes que se quieren incluir dentro. Como  se muestra en la imagen de la jerarquía de componentes, lo normal es comenzar con elemento llamado MaterialApp.



### 5.3 Widget



#### MaterialApp



Este componente representa el contenedor general de la aplicación. Toda aplicación es necesario que tenga al menos un contenedor principal y este es el contenedor por defecto en las aplicaciones que utilizan elementos de tipo MaterialDesing. Las características más comunes de este widget son:



- **Title**  
  Nombre que aparecerá en la parte superior de la barra.
- **Theme**  
  Se trata de la estructura visual base de la aplicación. Por defecto está configurado con material3
- **Home**  
  Parte principal de la aplicación. Podemos decir que es la zona central. Aquí es necesario indicar un widget que actúe como contenedor. Lo normal es utilizar un Scaffold



```dart
Widget build(BuildContext context) {
  return MaterialApp(
    title: "Aplicacion contador",
    theme: ThemeData(
      colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      useMaterial3: true,),
    home: // aquí se incluiré el Scaffold,
  )
}
```



#### Scaffold



Este componente representa la estructura visual básica de la aplicación MaterialDesign, diferenciando entre parte superior, parte central y parte inferior tal y como podemos ver en la imagen.

Los componentes principales del Scaffold son:



![image](assets/cm8p46l7e01qr356xyfriulfh-INSO_U3_Apartado6_Imagen2.jpg)

- **AppBar**  
  Barra de aplicaciones superior que muestra el título de esta además de un menú en el caso de que esté disponible. Como parámetro es necesario pasarle el texto que aparecerá en la misma.
- **Body**  
  Parte central del componente. Aquí será necesario indicar los elementos que se quieren mostrar dentro de la aplicación.
- **FloatingActionButton**  
  Botón circular, generalmente colocado en el parte inferior y destinado para acciones principales sobre la aplicación. Dentro de este botón es necesario indicar la acción onPressed encargada de gestionar la pulsación de este.



```dart
class ContadorApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Aplicacion contador",
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: Scaffold(
          appBar: AppBar(
            title: const Text("Aplicación contador"),
          ),
          floatingActionButton: FloatingActionButton(onPressed: () => {}),
          body:
        // aquí iran aquellos elementos que queramos mostrar en la parte centrel,
      ),
    );
  }
}
```



Dentro del body podemos poner cualquier tipo de widget, teniendo en cuenta que es muy recomendable utilizar un contenedor como elemento primario



#### Container / Center / Row / Column



Existen multitud de posibilidades de indicar el espacio general donde se representarán el resto de los componentes. Podemos decir que dentro del body, el primer elemento marcará como se colocan el resto. Dentro de estos elementos iniciales podemos destacar:

- **Container:** Widget que representa elementos teniendo la posibilidad de limitar su espacio en todas las coordenadas. Al representar un espacio que maneja espacios tanto interiores como exteriores, una de sus principales características es: margin – padding



```ini
Container(margin: EdgeInsets.all(20.0),child: Text("Esto es una prueba"),)
```



- **Center:** Widget que permite representar elementos en la parte central de la pantalla.



```bat
Center(child: Text("Elemento colocado en el centro"),)
```



- **Row:** Widget que permite organizar los elementos de forma horizontal.



```dart
Container(
  padding: EdgeInsets.all(20.0),
  child: Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [Text("Elemento 1"), Text("Elemento 2"), Text("Elemento 3")]),
)
```



Como se puede ver en el código, este componente en vez de tener una característica children, tiene childrens donde se indican cada uno de los elementos que forman parte de la fila. Además, se podrá indicar la alineación que tendrá todos los elementos que forman parte de la fila. Como se puede comprobar, la concatenación de elementos es necesaria para poder gestionarlos de forma correcta

- **Column:** Widget muy similar al anterior, con la diferencia que los elementos se agrupan verticalmente.



```dart
body: Container(
  padding: EdgeInsets.all(20.0),
  child: Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [Text("Elemento 1"), Text("Elemento 2"), Text("Elemento 3")]),
)
```



En los dos widgets anteriores, se pueden alinear los hijos de dos formas: mainAxis, crossAxis. Depende de cuál es el widget que queremos aplicar, los ejes cambian. En el caso de Row, el mainAxis es el eje de las x, mientras que en el caso de Column, el mainAxis es el eje de las y.



#### Text



Se trata del componente por excelencia donde se muestran textos. Por defecto, este componente tan solo necesita que se le indique en el constructor el texto que se quiere mostrar en la interfaz.

**Text("Texto que se quiere mostar")**

Además de esta configuración, es posible modificar el tipo de letra, tamaño, estilo, etc., configurando esto en el propio componente



```dart
Text(
  "Texto que se quiere mostar",
  style: TextStyle(
      fontStyle: FontStyle.italic,
      fontSize: 20,
      fontWeight: FontWeight.bold),
)
```



#### TextField



Se trata del componente por excelencia para la introducción de datos por parte del usuario. Por defecto no requiere de ningún elemento en el constructor, pero si es muy recomendable utilizar el atributo controller para poder gestionar lo que se escribe dentro del componente (esto se verá más adelante).



```dart
Center(
    child: Column(
  mainAxisAlignment: MainAxisAlignment.center,
  children: [Text("Introducción de datos"), TextField()],
))
```



Alguna de las características comunes de este elemento es:

- **maxLength:** longitud máxima de caracteres
- **obscureText:** enmascarar los caracteres que se escriban dentro del componente
- **decoration:** permite agregar elementos adicionales al componente tal como un hint, borde, label, etc…



```python
TextField(
    obscureText: true,
    decoration: InputDecoration(
      prefixIcon: Icon(Icons.password),
        border: OutlineInputBorder(),
        label: Text("Password"),
        hintText: "Introduce la contraseña"))
```



Como se ha comentado antes, este componente además de las características mo



#### Button



Se trata del componente por excelencia a la hora de gestionar acciones lanzadas por el usuario. Existen diferentes tipos de botones, siendo la diferencia el aspecto gráfico. Los diferentes tipos son:

FilledButton.tonal, OutlinedButton, TextButton. El código de cada uno de ellos sería el siguiente



```rust
body: Padding(
            padding: EdgeInsets.all(20.0),
            child: Center(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  ElevatedButton(
                      onPressed: () {}, child: const Text("Elevated")),
                  FilledButton(onPressed: () {}, child: Text("Filled")),
                  OutlinedButton(onPressed: () {}, child: Text("Outliner")),
                  TextButton(onPressed: () {}, child: Text("Text")),
                ],
              ),
            )));
```



La construcción de todos ellos es bastante sencilla, lo única diferencia como tal por defecto es el aspecto gráfico. El resultado es el siguiente:



![image](assets/cm8p4p0br02lm356x8v5ymkoe-Imagen7.jpg)



Como se puede comprobar todos los botones tienen la misma función onPressed. En el caso de querer incorporar un icono a cada uno de los botones se podría hacer indicándolo en la creación del botón



```kotlin
ElevatedButton.icon(
onPressed: () {},
label: Text("Elevated icon"),
icon: Icon(Icons.add)),
```



En el caso de querer utilizar solo botones que tengan icono (y no label) se tendría que utilizar la clase IconButton



```markdown
IconButton(
onPressed: () {}, icon: const Icon(Icons.access_alarms))
```



De la misma forma que a los botones normales se les puede indicar la posibilidad de icono indicando el .icon, al contrario pasa exactamente lo mismo, pudiendo indicar el aspecto que tienen cada uno de los botones con icono de la siguiente forma.

En cuanto a la función que tienen de forma requerida los botones, se puede asociar de dos formas: directamente en el propio componente o creando una función en el fichero y referenciándola. De carácter general, se creará en el mismo componente como función de flecha, indicando la tarea que se quiere realizar:



```dart
body: Builder(
  builder: (contexto) {
    return Center(
        child: Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children:[ElevatedButton(onPressed: (){
        ScaffoldMessenger.of(contexto).showSnackBar(SnackBar(content: Text("Mostrando")));
      }, child: Text("Pulsar"))]
    ));
  }
)
```



En el ejemplo anterior, se puede ver como se configura la pulsación del botón para que, al ser pulsado, se muestra una notificación a modo de snackbar en la parte inferior de la pantalla. También es importante reseñar el uso del widget builder, el cual crea un contexto nuevo, necesario para muchas de las acciones que lo requiere, ya que el creado desde la función builder no es suficiente al pertenecer a un widget superior.

Muchas de las acciones que se van a relacionar con la pulsación de los botones tendrán que ver con la captura y gestión de los datos provenientes de campos de texto, listas, etc. Para ello es necesario utilizar componentes que gestionen estado (statefull component), lo que se verá más adelante.



#### Checkbox



Los checkbox tienen un comportamiento muy similar a un elemento de tipo  Radio Button   explicados en el punto anterior, la diferencia es que normalmente suelen actuar de forma individual, es decir, no van en un grupo de opciones donde si se selecciona una de ellas, se deselecciona otra. Para poder utilizarlo, hay que tener en cuenta que hablamos de un widget que necesita un estado para poder guardar la selección (en este caso verdadero o falso)



```kotlin
Row(
children: [
  Text("¿Tienes mail?"),
  Checkbox(
    value:,
    onChanged: (bool? value) {
    },
  )],
),
```



De las cosas que hay que tener en cuenta es que tan solo son dos las propiedades que son requeridas: value y onChanged. La primera de ellas es necesario asociarla a una variable booleana (esto se verá con la gestión de los estados más adelante), para cuando el valor de esta variable cambie, también cambie el estado y por lo tanto su aspecto gráfico.



#### ListView



Si hay un componente que siempre estará presente dentro de las aplicaciones ese componente son las listas. Toda aplicación maneja una cantidad de datos importantes, y estos tienen que ser representados al usuario de la manera más visual posible y en un espacio lo suficientemente acotado para que la aplicación sea utilizable. Por ello, las listas representan el elemento perfecto para poder mostrar datos al usuario y que este pueda interaccionar con ellos. Para poder crear una lista de elementos debemos tener varias cosas en cuenta:

- El elemento que representa la lista se llama ListView y conforma el marco común donde serán representadas cada una de las filas.
- Los elementos o filas, se pueden representar bien como elementos individuales (Text, Button, etc) o como una fila real, para lo que se utiliza un componente especialmente creado para las listas, llamado ListTile.



```kotlin
body: Builder(builder: (contexto) {
  return Center(
      child: ListView(children: const [
    ListTile(title: Text("Elemento 1")),
    ListTile(title: Text("Elemento 2")),
    ListTile(title: Text("Elemento 3"))
  ]));
})
```



Dentro de la configuración de la lista, el atributo más importante es el de children, ya que este especifica cuales son cada uno de los elementos que se mostrarán en las filas de la lista. En el caso de que estas estén representadas por ListTile (recomendable), tienen un atributo llamado title donde se especifica el contenido de cada fila. Este puede ser cualquier elemento, desde texto, hasta algo más complejo como puede ser una imagen seguida de un texto y un botón. Para esto último sería necesario juntarlo dentro de un elemento contenedor como puede ser un Row



```dart
ListTile(
    title: Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
  children: [
    Icon(Icons.usb),
    Text("Elemento"),
    ElevatedButton(onPressed: (){}, child: Text("Pulsar"))
  ],
)),
```



El aspecto gráfico que tendría la fila sería el siguiente:



![image](assets/cm8p4xfeb02yo356xmzl7qr0d-Imagen8.png)



Del código que representa la fila, es reseñable la característica mainAxisAlignment, la cual vimos en puntos anteriores e indicaba como se colocaban los elementos en la fila, con la posibilidad de centrarlos. En este caso la configuración puesta hace que cada uno de los elementos de la fila tenga un espacio entre ellos.

Esta es una forma sencilla de hacer listas, pero por lo general no se sabe cuántas filas hay que pintar ya que los datos provienen de una lista con un tamaño variable, por lo que en muchos casos hay que descartar la creación de los elementos ListTile de forma manual. En este caso tendríamos que utilizar un creador de filas, también llamado ListView.Builder, el cual permite crear listas de datos con tan solo pasarle el molde de la fila y la lista de datos que se quiere representar. Para poder utilizar este componente, hay que realizar los siguientes pasos:

**1.**	Crear el modelo que se va a querer representar dentro de la fila. Este paso es optativo, pero por lo general todas las filas de una lista muestran un objeto con datos comunes. Para este ejemplo se va a utilizar un producto que tiene como propiedades nombre, precio y categoría, por lo que se crea una clase llamada Producto dentro de un fichero separado, con el siguiente código



```dart
class Producto{

  String nombre;
  int precio;
  String categoria;  
  Producto(this.nombre, this.precio, this.categoria);
 
}
```



**2.**  Una vez creado el modelo, se puede crear una lista con todos los elementos que se quieren representar dentro de la lista. Para ello en el fichero donde queremos crear el widget creamos la lista introduciendo todos los productos a mostrar



```lua
List<Producto> lista = [
  Producto("Iphone 15", 700, "Telefonia"),
  Producto("Ipad", 400, "Electrónica"),
  Producto("Asus E456", 1200, "Ordenadores"),
  Producto("Galaxy S20", 900, "Telefonia")
];
```



**3.**    Con la lista creada, se puede generar de forma automática la lista con los elementos que forman parte de ella. Para esto se puede utilizar el elemento ListView.Builder. Este elemento cuenta con numerosas configuraciones, siendo las más usadas itemCount e itemBuilder



```typescript
ListView.builder(
    itemCount: lista.length,
    itemBuilder: (contexto, index){
  return ListTile(title: Text(lista[index].nombre));
})
```



El element itemCount recibe el número de elementos que tendrá que representar dentro de la lista, mientras que el elemento itemBuilder se trata de la función encargada de generar cada uno de los elementos o filas de la lista. Se trata de una función que tiene como parámetros el contexto y el index del elemento que debe utilizar, retornando el ListTile con su configuración.

Si este ejemplo lo unimos con la creación gráfica de la fila que hemos realizado antes, podríamos tener un método que se encarga de retornar la fila construida y que sea llamado en cada construcción con el siguiente resultado final:



![image](assets/cm8p50xf50351356x4diuocub-Imagen9.jpg)



```dart
class ComprasApp extends StatelessWidget {


  @override
  Widget build(BuildContext context) {
    List<Producto> lista = [
      Producto("Iphone 15", 700, "Telefonia"),
      Producto("Ipad", 400, "Electrónica"),
      Producto("Asus E456", 1200, "Ordenadores"),
      Producto("Galaxy S20", 900, "Telefonia")
    ];
    return MaterialApp(
      title: "Aplicacion contador",
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: Scaffold(
          appBar: AppBar(
            title: const Text("Aplicación de compras"),
          ),
          floatingActionButton: FloatingActionButton(onPressed: () {}),
          body: Builder(builder: (contexto) {
            return Center(
              child: ListView.builder(
                  itemCount: lista.length,
                  itemBuilder: (contexto, index) {
                    return createListTile(lista[index], contexto);
                  }),
            );
          })
      ),
    );
  }
}

Widget createListTile(Producto p, BuildContext context) {
  return ListTile(
      title: Text(p.categoria),
      subtitle: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Icon(Icons.usb),
          Text(p.nombre),
          ElevatedButton(onPressed: () {
            ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text("El precio del ${p.nombre} son ${p.precio}")));
          }, child: Text("Comprar"))
        ],
      ));

}
```



## 6. Gestión De Estados



### 6.1 Introducción



![image](assets/cm8p52xvv036m356xtml7t7ai-stock-image.jpg)



En Flutter, los widgets se dividen en dos grandes categorías: stateless y statefull. Antes de profundizar en sus diferencias, es importante destacar que un mismo widget puede implementarse de ambas formas, dependiendo del propósito que se le quiera dar. En el caso de interesarnos que una pantalla con elementos de tipo Text y botones no conserve los datos introducidos, sino que simplemente se ejecute una acción, como navegar a otra pantalla al presionar un botón, estaríamos ante un widget sin estado. Por otro lado, si necesitamos que los textos ingresados en los campos se mantengan, por ejemplo, para completar un proceso de inicio de sesión más adelante, sería necesario emplear widgets con estado.



### 6.2 Stateless vs Statefull



Por lo tanto, podemos decir que la diferencia entre utilizar un widget con y sin estado es mantener los datos que están incorporados dentro de el: campos de texto, estado de la selección, etc… Como se ha ido haciendo hasta este punto, todos los widgets que se han utilizado se han configurado sin estado, por lo que su estructura era la siguiente: clase que extiende statelesswidget, y que tiene un método sobreescrito build que retorna el widget que queremos crear. Esto quiere decir que en ningún momento podemos tener una variable que vaya actualizando su estado y que sea utilizada, ya que estamos hablando de un widget sin estado. Sin embargo, si queremos crear un widget con estado su estructura será la siguiente: clase que extienda de statefullwidget que tiene sobrescrito un método llamado createState el cual retorna un objeto de tipo State. Adicionalmente se crea otra clase que extienda de State con un método sobrescrito llamado build que retorna un wigdet. Este último método se comporta igual que los de los widget sin estado, con la diferencia que tenemos disponible un método llamado setState para poder guardar el estado de aquellas cosas que queramos.



![image](assets/cm8p54p1i038q356xgq1db4ij-Imagen10.jpg)



En el siguiente video se explica como poder hacer una pantalla de login mediante el uso de widgets con estado para poder así utilizar la persistencia de los datos introducidos en un formulario. Para ello se combinan diferentes elementos, predominando los elementos stateless y el método setState para poder guardar los elementos de los inputs, los cuales tienen asociados controladores que permiten evaluar los textos introducidos :



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652025_1/scormcontent/assets/INSD_DM_Unidad3_Apartado7_Video.mp4?v=1)



En algunas ocasiones, además de gestionar el estado como se ha comentado en el vídeo anteriores, también podemos hacer uso de los controladores. Estos elementos se encargan de gestionar el estado interno de algunos widgets como por ejemplo TextEdits, ListView, CheckBox, de forma que cuando una acción se produce sobe estos, es posible gestionar los datos internos de los mismos. Depende de cómo queramos gestionar los estados y cuando queramos acceder a ellos podremos utilizar diferentes momentos del ciclo de un widget. Para explicar la gestión de estos elementos, se creará un widget con estado al cual se irán incorporando elementos, por lo que el código base será el siguiente:



```dart
class FormularioAplicacion extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: "Aplicacion contador",
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
            colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
            useMaterial3: true),
        home: FormularioWidget());
  }
}

class FormularioWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return FormularioState();
  }
}

class FormularioState extends State<FormularioWidget> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Gestion de estados"),
        backgroundColor: Colors.deepOrange,
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [],
      ),
    );
  }
}
```



En el Código se puede ver que partimos de un widget sin estado, el cual representa toda la aplicación, para poner en el home un widget con estado, llamado FormularioWidget asociado a una clase llamada FormularioState.

A continuación, se explicarán los principales elementos para poder gestionar el estado de diferentes componentes.



### 6.3 TextEdit



El primer elemento del que es interesante guardar su estado es el de los campos de texto, ya que estos nos dan la posibilidad re recoger datos que el usuario introduzca. Para ello seguiremos los siguientes pasos:

1. Creamos un TextEdit y lo ubicamos donde consideremos necesario
2. Se crea una variable de tipo TextEditController en la clase: esta variable será la encargada de recoger los datos cuando algo cambie dentro del TextEdit
3. La variable creada en el punto anterior la asociamos a la característica controller del TextEdit. Con esto garantizamos que los datos serán guardados en el controlador en momento del cambio.
4. Accedemos a los datos en el momento en el que consideremos oportuno, como por ejemplo con la pulsación de un botón



```dart
class FormularioState extends State<FormularioWidget> {
  TextEditingController controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Gestion de estados"),
        backgroundColor: Colors.deepOrange,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              decoration: InputDecoration(
                  label: Text("Nombre"), border: OutlineInputBorder()),
              controller: controller,
            ),
            ElevatedButton(
                onPressed: () {
                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                      content: Text(
                          "El dato del campo de texto es: ${controller.text}")));
                },
                child: Text("Comprobar estado"))
          ],
        ),
      ),
    );
  }
}
```



En este caso se accede a los datos con la pulsación de un botón, pero si se quisiera acceder a los datos en otro momento tan solo sería necesario asociar el método correspondiente dentro del TextEdit, como por ejemplo cuando los datos cambian.

**onChanged: (str){print(str);},**



### 6.4 Spinner



Otro de los elementos típicos para poder recoger sus datos, son los DropDownButton Se trata de unos botones especiales que tienen aspecto de lista desplegable, donde solo un elemento al mismo tiempo puede estar seleccionado. Para poder utilizarlo y obtener su estado, tendremos que seguir los siguientes pasos:

1. Creamos una lista con todas aquellas cosas que queramos mostrar dentro del botón desplegable
2. Creamos un componente DropDownButton y lo ubicamos donde consideremos necesario
3. Dentro del componente se configura la opción ítems, indicando cada uno de los DropDownMenuItem del elemento



```rust
DropdownButton(
    items: [
      DropdownMenuItem(child: Text("Opcion 1")),
      DropdownMenuItem(child: Text("Opcion 2")),
      DropdownMenuItem(child: Text("Opcion 3")),
      DropdownMenuItem(child: Text("Opcion 4")),
    ],
    onChanged: (item) {}),
```



Como se puede ver el método onChange es obligatorio y obtiene como parámetro el elemento que está seleccionado cuando se cambia algo dentro del selector. Este tipo de elemento no tiene un controlador asociado, por lo que será necesario utilizar el método setState para gestionar de forma correcta los datos

1. Creamos una variable de clase que servirá para guardar el elemento seleccionado del desplegable
2. En el método onChange del desplegable, ejecutamos el método setState para asignar el elemento seleccionado pasado por parámetros a la variable creada en el punto anterior



```dart
List<String> opciones = <String>[
  "Opcion 1",
  "Opcion 2",
  "Opcion 3",
  "Opcion 4"
];
class FormularioState extends State<FormularioWidget> {
  TextEditingController controller = TextEditingController();
  String seleccion = opciones.first;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Gestion de estados"),
        backgroundColor: Colors.deepOrange,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              onChanged: (str) {
                print(str);
              },
              decoration: InputDecoration(
                  label: Text("Nombre"), border: OutlineInputBorder()),
              controller: controller,
            ),
            DropdownButton(
                onChanged: (item) {
                  setState(() {
                    seleccion = item.toString();
                  });
                },
                value: seleccion,
                items: opciones.map<DropdownMenuItem<String>>((String value) {
                  return DropdownMenuItem<String>(
                    value: value,
                    child: Text(value),
                  );
                }).toList()),
            ElevatedButton(
                onPressed: () {
                  ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                      content: Text(
                          "Producto comprado: ${controller.text}\nCantidad: $seleccion")));
                },
                child: Text("Comprobar estado"))
          ],
        ),
      ),
    );
  }
}
```



### 6.5 CheckBox



Otro de los componentes que suele acompañarse de un controlador es el checkbox. Este componente permite gestionar la selección de una casilla de verificación, obteniendo un booleano cuando el elemento cambia de selección. Para ello hay que crear una variable boolean donde quedará recogido el estado y cambiarla cuando se provoque un cambio en la selección mediante el método onChange de widget



```dart
class FormularioState extends State<FormularioWidget> {

  TextEditingController controller = TextEditingController();
  bool estadoCheck = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Gestion de estados"),
        backgroundColor: Colors.deepOrange,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              onChanged: (str) {
                print(str);
              },
              decoration: InputDecoration(
                  label: Text("Nombre"), border: OutlineInputBorder()),
              controller: controller,
            ),
            Checkbox(
                value: estadoCheck,
                onChanged: (estado) {
                  setState(() {
                    estadoCheck = estado!!;
                  });
                }),
            ElevatedButton(
                onPressed: () {
    
                  if (estadoCheck) {
                    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
                        content: Text(
                            "Producto comprado: ${controller.text}\nCantidad: $seleccion")));
                  }
                },
                child: Text("Comprobar estado")),
           
          ],
        ),
      ),
    );
  }
}
```



En este ejemplo, se ha creado la variable boolean para gestionar el estado del componente, que a su vez sirve para poder asignarle el estado directamente. Dentro del componente, es necesario asignar el método onChage con un parámetro boolean, que será utilizado para gestionar el estado.



### 6.6 ListView



En las listas, existe un controlador como el que hemos visto en los textEdit, encargado de escuchas el comportamiento del scroll de la lista, movimientos, etc, pero no existe uno funcional para gestionar la pulsación de los elementos de una lista. Sin embargo, como ya hemos visto, se puede gestionar el estado de una variable según la pulsación de un elemento de la fila, ubicando el elemento que queramos cambiando el estado de este. Así, utilizando el ejemplo que hemos realizado antes de la lista de productos, podríamos hacer lo siguiente:



```dart
class FormularioState extends State<FormularioWidget> {
  Producto? producto = null;

  List<Producto> lista = [
    Producto("Iphone 15", 700, "Telefonia"),
    Producto("Ipad", 400, "Electrónica"),
    Producto("Asus E456", 1200, "Ordenadores"),
    Producto("Galaxy S20", 900, "Telefonia")
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Gestion de estados"),
        backgroundColor: Colors.deepOrange,
      ),
      body: Center(
        child: ListView.builder(
            scrollDirection: Axis.vertical,
            itemCount: lista.length,
            itemBuilder: (contexto, index) {
              return createListTile(lista[index], contexto);
            }) 
      ),
    );
  }

  Widget createListTile(Producto p, BuildContext context) {
    return ListTile(
        title: Text(p.categoria),
        subtitle: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Icon(Icons.usb),
            Text(p.nombre),
            ElevatedButton(
                onPressed: () {
                  setState(() {
                    this.producto = p;
                  });
                },
                child: Text("Comprar"))
          ],
        ));
  }
```



## 7. Navegación



### 7.1 Introducción



![image](assets/cm8p5hcj503lj356x97snt0vu-stock-image.jpg)



Uno de los puntos básicos en una aplicación es la posibilidad de tener más de una pantalla que permita realizar una navegación entre diferentes pantallas tras la pulsación de un botón o cualquier acción. Hasta este momento lo que se ha visto es como poder crear un widget general que representa la pantalla y dentro de éste la organización de diferentes tipos de elementos. Sin embargo, con una sola pantalla estamos reduciendo en gran medida las posibilidades a la hora de darle funcionalidad a nuestra aplicación, ya que tan solo contaremos con un marco o pantalla para incluir elementos, lo que limita mucho al programador.



### 7.2 Navegando



Para poder realizar una navegación lo que necesitamos es de dos clases que representen dos pantallas (por lo general la pantalla será stateless), las cuales están creadas mediante dos clases las cuales pueden o no estar en el mismo fichero. En este ejemplo crearemos dos pantallas simulando un login, donde en la primera pantalla se mostrará el típico login con campos de nombre y contraseña además de un botón y en el caso de realizarlo de forma correcta, mostrará una segunda pantalla con una lista de usuarios. Para ello crearemos dos ficheros llamados LoginScreen y MainScreen



![image](assets/cm8p5iwo603nn356xkut4lgn2-Imagen11.jpg)



El primero de los ficheros tendrá el siguiente código



```dart
class LoginScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Login Screen",
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
          useMaterial3: true),
      home: LoginWidget(),
    );
  }
}

class LoginWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return LoginState();
  }
}

class LoginState extends State<LoginWidget> {
  TextEditingController controllerName = TextEditingController(text: "");
  TextEditingController controllerPass = TextEditingController(text: "");

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Login"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              TextField(
                controller: controllerName,
                decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    label: Text("Name"),
                    hintText: "Please enter your name"),
              ),
              Padding(padding: EdgeInsets.only(bottom: 16.0)),
              TextField(
                controller: controllerPass,
                obscureText: true,
                decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    label: Text("Pass"),
                    hintText: "Please enter your password"),
              ),
              Padding(padding: EdgeInsets.only(bottom: 32.0)),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  ElevatedButton(
                      onPressed: () {
                        if (controllerName.text.toLowerCase() == "admin" &&
                            controllerPass.text.toLowerCase() == "pass") {
                          // realizar login
                          ScaffoldMessenger.of(context).showSnackBar(
                              SnackBar(content: Text("Login correcto")));
                        } else {
                          ScaffoldMessenger.of(context).showSnackBar(
                              SnackBar(content: Text("Datos incorrectos")));
                        }
                      },
                      child: Text("Log in")),
                  ElevatedButton(
                      onPressed: () {
                        controllerPass.text = "";
                        controllerName.text = "";
                      },
                      child: Text('Clear'))
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
```



Como se puede comprobar, se trata de una clase general de tipo stateless que dentro tiene la llamada a otra clase statefull. Esto se debe a que es necesario mantener el contenido de los TextField para poder analizarlos tras la pulsación de botón Log In. Para esto se ha simulado un login con datos Admin Pass como usuario y contraseña. Además, el botón Clear elimina el contenido de los campos de texto, simplemente eliminando el texto que está guardado dentro de los controladores.

Antes de crear el segundo fichero, vamos a crear la clase que se utilizará para representar todos los elementos dentro de la lista. En este caso se representarán usuarios, por lo que la clase queda configurada de la siguiente manera



```dart
class User {
  String name;
  String surname;
  String mail;
  String gender;
  int? phone;
  User(this.name, this.surname, this.mail, this.gender);
  User.phone(this.name, this.surname, this.mail, this.gender,this.phone);
}
```



En esta clase se ha incorporado un constructor nominal para poder crear usuarios con y sin teléfono

Ahora sí, podemos crear el contenido del segundo fichero que representa la lista y será mostrado una vez se realice el login. Será el siguiente:



```dart
List<User> listaUsuarios = <User>[
  User.phone("Borja", "Martin", "borja@desarrollo.com", "male", 9333333),
  User("Juan", "Lopez", "juan@desarrollo.com", "male"),
  User.phone("Celia", "Martin", "celia@desarrollo.com", 'famale', 9111111),
  User("Carlos", "Perez", "celia@desarrollo.com", "male"),
  User.phone(
      "Claudia", "De Diego", "claudia@desarrollo.com", 'famale', 9222222),
  User("Jesús", "Gomez", "jesus@desarrollo.com", "male"),
];

class Mainscreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return MaterialApp(
        title: "Main screen",
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
            colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
            useMaterial3: true),
        home: Scaffold(
          appBar: AppBar(title: Text("Main screen")),
          body: ListView.builder(
              itemCount: listaUsuarios.length,
              itemBuilder: (ctx, index)

              {
                return ListTile(
                  onTap: (){
                    ScaffoldMessenger.of(ctx).showSnackBar(SnackBar(content: Text("User mail: ${listaUsuarios[index].mail}")));
                  },
                  title: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      listaUsuarios[index].gender =="male" ? Icon(Icons.male_sharp) : Icon(Icons.female_sharp),
                      Text(listaUsuarios[index].name)
                    ],
                  ),
                );
              }),
        ));
  }
}
```



En este caso, no es necesario utilizar ninguna clase de tipo statefull ya que en el ejemplo no interesa guardad el estado de ningún dato, simplemente aparecerá el correo en una notificación en el caso de que alguna de las filas sea pulsada. Mención aparte merece la gestión del icono de la fila, ya que éste dependerá de la característica gender del usuario. Para ello se utiliza un operador ternario, indicando que en el caso de ser true la condición ponga un tipo de icono, y en el caso de ser false ponga otro.

Una vez tenemos las pantallas creadas tendremos que realizar lo siguiente

**1.** En un tercer archivo llamado main, sobreescribiremos el método main que será el encargado de llamar a la primera pantalla que queramos mostrar, en nuestro caso LoginScreen, mediante su constructor



```dart
void main() {
  runApp(LoginScreen());
}
```



**2.**  En aquellas acciones desde donde queramos lanzar la nevageción, se utiliza el método push del elemento Navigator. En el ejemplo que estamos realizando lo incluiremos en el fichero LoginScreen al pulsar el botón de Log In



```scala
ElevatedButton(
    onPressed: () {
      if (controllerName.text.toLowerCase() == "admin" &&
          controllerPass.text.toLowerCase() == "pass") {
        // realizar login
        /*ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text("Login correcto")));*/
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => Mainscreen()),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text("Datos incorrectos")));
      }
    },
```



Si estando en la segunda pantalla, en algún momento queremos volver a la primera, tendríamos que ejecutar el método pop de Navigator.



```dart
appBar: AppBar(
    title: Row(
  children: [
    IconButton.filledTonal(
      onPressed: () {
        Navigator.pop(context);
      },
      icon: Icon(Icons.arrow_back),
    ),
    Padding(padding: EdgeInsets.only(right: 16.0)),
    Text("Main screen"),
  ],
)),
```



Para poder similar el comportamiento, se ha incorporado un botón dentro de la barra superior de la pantalla principal, donde al pulsarlo se ejecuta el método comentado.



### 7.3 Paso de parámetros



En el caso de querer pasar datos entre pantallas, tendríamos que crear una variable en la pantalla destino. En esta variable guardaremos los datos que llegan en la navegación. Para poder hacer esto realizaremos los siguientes pasos:

**1.**      En la pantalla destino donde queramos obtener el dato correspondiente, crear la variable indicada y crear un constructor donde se requiera el dato a comunicar.



```dart
class Mainscreen extends StatelessWidget {
  
  late String nombre;

  Mainscreen({required this.nombre});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: "Main screen",
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
            colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
            useMaterial3: true),
        home: Scaffold(
          appBar: AppBar(
              title: Row(
            children: [
              IconButton.filledTonal(
                onPressed: () {
                  Navigator.pop(context);
                },
                icon: Icon(Icons.arrow_back),
              ),
              Padding(padding: EdgeInsets.only(right: 16.0)),
              Text("Welcome $nombre"),
            ],
          )),
          body: ListView.builder(
              itemCount: listaUsuarios.length,
              itemBuilder: (ctx, index) {
                return ListTile(
                  onTap: () {
                    ScaffoldMessenger.of(ctx).showSnackBar(SnackBar(
                        content:
                            Text("User mail: ${listaUsuarios[index].mail}")));
                  },
                  title: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      listaUsuarios[index].gender == "male"
                          ? Icon(Icons.male_sharp)
                          : Icon(Icons.female_sharp),
                      Text(listaUsuarios[index].name)
                    ],
                  ),
                );
              }),
        ));
  }
}
```



**2.**   Donde se quiere realizar la navegación, se llama a la pantalla destino utilizando el constructor creado anteriormente.



```dart
ElevatedButton(
    onPressed: () {
      if (controllerName.text.toLowerCase() == "admin" &&
          controllerPass.text.toLowerCase() == "pass") {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => Mainscreen(nombre: controllerName.text,)),
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text("Datos incorrectos")));
      }
    },
    child: Text("Log in")),
```



En el siguiente video se muestra cómo funciona el paso de parámetros y la utilización de estos en el destino.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652025_1/scormcontent/assets/INSD_DM_Unidad3_Apartado8_Video.mp4?v=1)



## 8. Conclusiones



### 8.1 Conclusiones de la unidad



El desarrollo hibrido es una opción muy a tener en cuenta a la hora de realizar una aplicación móvil. Este permite reducir el tiempo de desarrollo gracias a la posibilidad de tener aplicaciones crossplatform en un solo proyecto. Antes de tomar la decisión de utilizar este tipo de desarrollo hay que tener en cuenta las necesidades que tendrá dicho desarrollo y las características del proyecto, ya que se necesitarán librerías y elementos adicionales para poder acceder a parte de los recursos.

En el mercado existen multitud de frameworks que permiten el uso de estas características. IONIC, ReactNative, Vue Mobile y Flutter son ejemplos claros. Sin embargo, los tres primeros se basan en un desarrollo WEB, permitiendo hacer una aplicación sobre navegador. Sin embargo, Flutter permite un desarrollo nativo sobre el sistema operativo de forma directa, lo que permite el acceso a los elementos directamente, lo que facilita no solo el desarrollo, sino también los tiempos de ejecución.

Dentro del desarrollo Flutter, hay que comprender muy bien el tipo de diseño que tienen las aplicaciones, siendo todos los elementos (tanto visibles como no visibles) que forman parte de la aplicación los denominados widgets, los cuales permiten una estructura jerárquica de muy fácil implementación.
