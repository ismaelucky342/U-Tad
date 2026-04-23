# Unidad 2. Funciones avanzadas y persistencia de datos en Android.

## Index

- [1. Introducción Y Objetivos](#1-introducción-y-objetivos)
  - [1.1 Introducción y objetivos](#11-introducción-y-objetivos)
- [2. Elementos Avanzados Ui](#2-elementos-avanzados-ui)
  - [2.1 Introducción](#21-introducción)
  - [2.2 RecyclerView](#22-recyclerview)
  - [2.3 Menús](#23-menús)
  - [2.4 Diálogos](#24-diálogos)
- [3. Fragments](#3-fragments)
  - [3.1 Introducción](#31-introducción)
  - [3.2 Estructura de un fragment](#32-estructura-de-un-fragment)
  - [3.3 Navegando entre fragments](#33-navegando-entre-fragments)
  - [3.4 Basic view Activity](#34-basic-view-activity)
- [4. Persistencia De Datos](#4-persistencia-de-datos)
  - [4.1 Introducción](#41-introducción)
  - [4.2 Firebase](#42-firebase)
  - [4.3 Consultas a API](#43-consultas-a-api)
- [5. Conclusiones](#5-conclusiones)
  - [5.1 Conclusiones de la unidad](#51-conclusiones-de-la-unidad)



## 1. Introducción Y Objetivos



### 1.1 Introducción y objetivos



#### Introducción



Una vez ya hemos visto como poder generar interfaces gráficas en Android mediante Kotlin y XML, en este tema veremos como poder utilizar elementos avanzados de la interfaz gráfica como son los RecyclerView para poder representar listados de datos de forma eficiente, los menús, los cuadros de diálogo y sus diferentes tipos para presentar información e interacción con el usuario de forma adicional a como lo hacen las pantallas y por último el uso y concepto de los fragments, los cuales permiten la creación de interfaces graficas modulares

Otro de los temas que se tratan en esta unidad es la persistencia de datos. Todas las aplicaciones manejan una cantidad de datos muy importante, los cuales tienen que estar siempre disponibles para que el usuario pueda acceder a ellos. Para esto, es necesario que nuestras aplicaciones tengan una comunicación contra base de datos, pudiendo utilizar las diferentes posibilidades que el sistema nos ofrece: SQLIte, Firebase y consumos de API REST.



- **Elementos Avanzados UI**  
  Además de los elementos que ya se han tratado en la otra unidad, existen una cantidad importante de elementos que requieren de un conocimiento más profundo. Estos permiten la gestión y mostrado de datos que son prácticamente obligatoria dentro de una aplicación Android. Los elementos de los que se hablan son:

  - RecyclerView
  - Menús
  - Cuadros de diálogo
- **Fragments**  
  Los fragments son elementos que permiten la modulación dentro de la pantalla. En grandes rasgos, un fragment es un elemento individual (con xml propio) que se incorpora dentro de una activity. Esta incorporación puede ser de dos tipos: estática (se declara el elemento en el xml de la pantalla) o dinámica (no se declara el elemento, sino que puede ser cambiante). Dependiendo de cuál sea el uso que se quiera dar, utilizaremos uno u otro. Por ejemplo, si todas las pantallas de nuestra aplicación tienen la misma cabecera, podremos crear un fragment estático para agregarlo en cada una de las pantallas. En el caso de tener una aplicación donde la parte central queremos que cambien en un momento determinado (sin necesidad de que cambie la activity), utilizaremos un fragment dinámico.
- **Persistencia de Datos**  
  Cuando hablamos de cualquier tipo de aplicación, es evidente que esta no tendría ningún tipo de sentido sin los datos. Por ello esta es una parte crucial dentro del desarrollo. En una ejecución normal, la cantidad de datos que son mostrados y procesados por la aplicación es muy grande, y estos se le deben presentar al usuario de forma consistente tantas veces como éste considere necesarias. Si como desarrolladores no tenemos la capacidad de asegurar esta disponibilidad de los datos al usuario, nuestra aplicación no tendrá mucho valor. Por ello guardar la información y saberla gestionar es esencial en cualquier aplicación de Android.



#### Objetivos



Los objetivos que se persiguen en esta unidad son:



1. Conocer los elementos UI avanzados.
2. Crear y renderizar listado de datos con adaptadores personalizados.
3. Crear y utilizar menús con sus diferentes tipos de configuraciones.
4. Conocer los diferentes tipos de cuadro de diálogo que existen y utilizarlos de forma consistente dentro de una aplicación.
5. Entender el concepto de fragment, su ciclo de vida y la diferencia que estos tienen con las activities.
6. Aprender a utilizar la plantilla BaseActivity, con cada uno de los componentes que esta tiene.
7. Aprender a utilizar los diferentes tipos de base de datos que existen dentro del desarrollo: bases de datos internas como SQLite y bases de datos basadas en servicios de terceros como Firebase.
8. Aprender a realizar peticiones de red API REST, leyendo su respuesta e interpretar los datos para utilizarlos dentro de nuestras aplicaciones.



## 2. Elementos Avanzados Ui



### 2.1 Introducción



![image](assets/cm6xkwqtq005d356z7gq0y1cx-stock-image.jpg)



Además de los elementos que ya se han tratado en la otra unidad, existen una cantidad importante de elementos que requieren de un conocimiento más profundo. Estos permiten la gestión y mostrado de datos que son prácticamente obligatoria dentro de una aplicación Android. Los elementos de los que se hablan son:

- **RecyclerView:** se trata de uno de los elementos más recurrentes dentro de toda aplicación, ya que muestra un listado con una cantidad alta de datos, utilizando un patrón viewholder para que dicha renderización se haga de la forma más eficiente posible. Este tipo de listado son personalizados, por lo que el aspecto que tendrá cada una de las filas es diseñada por el desarrollador, repitiéndose de forma automática tantas veces como filas tenga el listado.



![image](assets/cm6xky7iy005y356zllh2uywo-Captura_20de_20pantalla_202025-02-09_20131016.jpg)



- **Menús:** Cuando no queremos sobrecargar la información que se muestra en la pantalla y se quiere tener siempre disponible una serie de acciones, es necesario utilizar menús que permitan al usuario de forma rápida e intuitiva el acceso a dichas acciones. Existen varios tipos de menú como son los laterales, inferiores, de barra y contextuales. En este tema nos centraremos en los menús de barra que son los que común mente se asocia a los tres puntos ubicados en la parte superior derecha.



![image](assets/cm6xl30il007e356z0odsdrp5-Imagen3.jpg)



- **Cuadros de diálogo:** Los cuadros de diálogo son componentes fundamentales en las aplicaciones Android, ya que permiten interactuar con los usuarios a través de ventanas emergentes que solicitan información, muestran opciones, o proporcionan alertas. Existente diferentes tipos de cuadro de diálogo, pero cabe destacar aquellos que son creados por el desarrollador utilizando la clase DialogFragment, la cual tiene su propio ciclo de vida.



### 2.2 RecyclerView



Toda aplicación que maneja datos tiene una parte donde estos deben ser mostrados en un formato de lista. Por ello, es importante poder utilizar el componente más adecuado para este tipo de representaciones. Antiguamente en Android, existía el componente ListView, que permite dicha representación de datos, pero en las bibliotecas de soporte se incorporó desde la versión 5.0 el componente RecyclerView. Dicho componente realiza las mismas funciones, pero con una manera de gestionar los datos más eficientes, lo que hace que la memoria no se sobre cargue tanto.

Como se verá en este punto, el elemento recycler permite mostrar una lista de datos tan larga como sea necesaria aprovechando al máximo la memoria, ya que se basa en un patrón view holder para la representación de los datos. Antes de empezar a explicar el proceso de creación y gestión del elemento, hay que comentar que al ser un componente que maneja datos, estos serán gestionados por una clase externa de tiempo RecyclerView.Adapter, que será la encargada de pintar – repintar los datos, así como trabajar con las acciones que se quieran realizar sobre estos

// IMAGEN DE UNA LISTA CON LA PARTE DE DATOS Y DISEÑANDO EL RECYCLER

Otra cosa que debemos tener en cuenta es como se configura el componente. Además de incluirlo en la interfaz gráfica y asociarle un adaptador para poder representar los datos de forma correcta, también será necesario indicar como se distribuyen los componentes de forma interna en la lista, pudiendo ser esta horizontal, vertical, en forma de grid, etc.… Esto se detallará más adelante

Una vez comprendido cual es la estructura gráfica y de datos del componente, vamos a pasar a ver cuál es su uso. Una vez que se ha detectado la necesidad de utilizar una lista para representar una lista de datos tendremos que seguir los siguientes pasos:



1. **Incorporar el componente dentro de la parte gráfica de la actividad**

   En este punto, al igual que todos los elementos vistos en temas anteriores, lo que tendremos que hacer es incorporar en el XML de la actividad en cuestión el componente RecyclerView. Al ser un componente de soporte se agrega a través de la librería androidx



```xml
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">
    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerProductos"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>
```



Como se puede ver en el código, el elemento es necesario que tenga un id para que en la parte lógica de la pantalla pueda ser representado de forma correcta. El siguiente paso será la creación del modelo o elemento que se quiera representar dentro de cada una de las filas, así como el aspecto que tendrá



2. **Creación del modelo de datos y UI de la fila**

   Una vez creado el recyclerview, el siguiente punto es el de crear el modelo de datos que se quiere presentar en cada una de las filas. En este ejemplo crearemos una clase que representa un producto para que más adelante podamos representarlos dentro del listado. Para ello, creamos una clase llamada Producto en un paquete llamado model. Esta clase tendrá los atributos de nombre, precio, descripción e imagen



```kotlin
package com.example.tienda.model

class Producto (var nombre: String, var precio: Double, var descripcion: String, var imagen: Int)
```



Esta clase tiene todos los atributos. Especial interés tiene la imagen, que en este caso se tipa como entero ya que lo pondremos como un recurso local, y por ello Android lo gestiona como un número al ser referenciado desde el código con la clase R

Una vez tenemos el modelo creado, el siguiente paso es la creación del patrón que queremos que tenga las filas. Esta representación podemos decir que es la plantilla que seguirá cada una de las filas para que luego se puedan acoplar cada uno de los datos que se quiere representar. El XML creado será utilizado por el adaptador de datos para realizar esta tarea. El XML creado se ubicará dentro de la carpeta layout dentro de res y en el ejemplo se le dará el nombre de item_producto.xml



![image](assets/cm6xlcdc900ge356zk36g6wa5-Imagen5.jpg)



En la disposición de la fila que se muestra en la imagen, el atributo text es simplemente para ver la disposición en diseño, ya que en ejecución este atributo será incluido mediante el adaptador. En este fichero hay que tener en cuenta una serie de cosas:

- Todos los elementos que queramos rellenar automáticamente desde el adaptador deben tener id
- El alto del layout completo (layout_heigth) nunca debe ser match_parent, ya que sino cada fila ocuparía una pantalla completa.
- La disposición de los elementos es totalmente personalizada, por lo que es el desarrollador el que marca la disposición de los mismo.

Una vez tenemos el modelo y la plantilla de la fila, el siguiente paso es crear el adaptador que permite generar cada una de las filas de forma automática



3. **Creación del adaptador mediante el patrón view holder**

   Como se ha comentado al principio de este punto, los recycler view tienen dos partes diferenciadas. Por un lado tenemos la parte gráfica que ya ha sido tratada en los puntos anteriores, y por otro lado tenemos los adaptadores que manejan los datos. Este objeto actúa como intermediario entre la parte gráfica y el conjunto de datos que se quiere representar y será creado como una clase adicional la cual extiende de RecyclerView.Adapter. De forma adicional, ésta tiene una clase anidada denominada ViewHolder conexión entre las filas y los datos. La estructura base de la clase será la siguiente



```kotlin
class AdapterProductos: RecyclerView.Adapter<AdapterProductos.HolderProducto>() {
         
    class HolderProducto(itemView: View) : RecyclerView.ViewHolder(itemView){}

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): HolderProducto {
        TODO("Not yet implemented")
    }

    override fun getItemCount(): Int {
        TODO("Not yet implemented")
    }

    override fun onBindViewHolder(holder: HolderProducto, position: Int) {
        TODO("Not yet implemented")
    }
}
```



Cada uno de los elementos de la clase se encargará de lo siguiente:

- Clase anidada HolderProducto: será la encargada de crear la plantilla con el XML creado en el punto anterior. Será en enlace con los datos
- Método onCreateViewHolder: será el encargado de crear el objeto de la clase anidada para poder tener disponible la plantilla y vincularla con los datos
- Método getItemCount: será el encargado de indicar cuantos datos son necesarios representar
- Método onBindViewHolder: será el encargado de asociar el holder creado con los datos ubicado en una lista.

A continuación, se muestra un video del proceso y explicación de la creación de la clase que permite representar los datos en la lista.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652022_1/scormcontent/assets/INSD_DM_Unidad2_Apartado3_2_Video1.mp4?v=1)



Es muy importante indicar que todos estos métodos se ejecutan de forma automática, por lo que no es necesarios llamarlos en ningún momento.



4. **Creación del recycler en la parte lógica y asociación con los datos**

   Como último punto, falta por crear el recycler dentro de la pantalla y asociarle los datos que se quieren representar dentro del mismo, siendo el adaptador el encargado de ello.

   Para poder crear el recycler, tenemos disponible la variable binding vista en el tema anterior, que se encarga de asociar de forma directa la parte gráfica y la parte lógica. Lo que si tenemos que crear nosotros de forma manual es el objeto adaptador, mediante la clase creada en el punto anterior:



```kotlin
class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding     
    private lateinit var adaptadorProducto: AdapterProductos

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        //binding.recyclerProductos
    }
}
```



En este punto es importante tener en cuenta cual es el origen de los datos que queremos representar en la lista y como poder pasarlas al adaptador en el caso de ser necesario. Si se quiere consultarlos a base de datos o directamente desde una lista, será necesario pasárselo como parámetro en el constructor. Recordad que en el video de la creación del adapter ya se dejó preparado dicho constructor para admitir como parámetro tanto una lista como el contexto de ejecución. En el ejemplo se creará una lista de productos en el activity, para lo que se crea un arraylist en cual es rellenado con datos de prueba. Una vez creada la lista de datos, es momento de crear el adaptador pasándole tanto la lista como el contexto, de forma que esté capacitado de generar la representación de cada una de las filas siguiente el patrón indicado en su clase.



```kotlin
class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var adaptadorProducto: AdapterProductos
    private lateinit var listaProductos: ArrayList<Producto>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
 setContentView(binding.root)

        rellenarLista();
        asociarDatos();
    }

    private fun asociarDatos() {
        adaptadorProducto = AdapterProductos(this, listaProductos)
    }

    private fun rellenarLista() {
        listaProductos = ArrayList()
        listaProductos.add(Producto("Camiseta deporte",30.0, "Camiseta de alta transpiración, muy comoda para poder hacer deporte", R.drawable.camiseta))
        listaProductos.add(Producto("Vaqueros",100.0, "Pantalones vaquero con tejido de calidad para uso diario", R.drawable.vaqueros))
        listaProductos.add(Producto("Jersey",60.0, "Jersey con motivos navideños realizado en lana de primera calidad", R.drawable.jersey))
    }
}
```



Sobre la creación de la lista, remarcar que el último parámetro de los objetos de tipo producto se ha configurado como Int, ya que, al ser un recurso local, este es manejado desde la clase R y se toma como un número, no como un string ni como un drawable

Una vez se cree el objeto de tipo adaptador, el último paso es el de asociar parte gráfica (recycler) y parte lógica (adapter), así como indicar cual será la disposición de los datos de forma interna dentro de la lista.



```groovy
private fun asociarDatos() {
    adaptadorProducto = AdapterProductos(this, listaProductos)
    binding.recyclerProductos.adapter = adaptadorProducto;
    binding.recyclerProductos.layoutManager = LinearLayoutManager(applicationContext, LinearLayoutManager.VERTICAL, false)
}
```



Como disposición interna, en el ejemplo se ha utilizado una gestión Linear vertical, pero las opciones disponibles son las siguientes:

- **LineaLayout:** Disposición donde los elementos van de arriba abajo (VERTICAL) u izquierda derecha (HORIZONTAL). Como último parámetro se indica que los elementos de la lista no son reversibles



```ini
binding.recyclerProductos.layoutManager = LinearLayoutManager(applicationContext, LinearLayoutManager.VERTICAL, false)
```



- **GridLayout:** Disposición donde los elementos se colocan en un número de columnas indicado, pudiendo ser una disposición horizontal o vertical.



```ini
binding.recyclerProductos.layoutManager = GridLayoutManager(applicationContext,2, GridLayoutManager.VERTICAL, false)}
```



- **StaggeredGridLayout:** Disposición muy similar a la anterior, con la diferencia que cada elemento de la fila terminará en la parte donde sea necesario, sin necesidad de mantener un aspecto de tabla con el resto de los elementos de la misma fila



```ini
binding.recyclerProductos.layoutManager = StaggeredGridLayoutManager(2, StaggeredGridLayoutManager.VERTICAL)
```



El aspecto que tendría cada una de las disposiciones es el siguiente:



![image](assets/cm6xlnuc000vh356zormlshlm-Imagen6.jpg)



Como resultado final en la aplicación generada tendríamos la siguiente lista de datos:



![image](assets/cm6xloqtm00wu356zcggfgxc5-Imagen7.jpg)



Con esto tendríamos creada una gestión base de una lista. En el caso de querer añadir elementos a posteriori como por ejemplo cargar productos nuevos que se incorporan a la lista cuando están disponibles (tras la pulsación de un botón o gesto similar), tendríamos que crear un método en el adaptador que se encargue de añadir los elementos a la lista. Esto es importante que se haga en la lista que está en el adaptador y no en la de la activity, ya que sino el trabajo de la aplicación será el doble.

Para poder hacer esto basta con crear una función que obtenga por parámetros el objeto a añadir y lo meta dentro de la lista. Además de esto es muy importante que se ejecute el método notifyDataInserted indicando la última posición de la lista. Este método se encargará de notificar un cambio en la última posición y actualizar solo esa.



```r
public fun addProducto(producto: Producto){
    lista.add(producto)
    notifyItemInserted(lista.size-1)
}
```



Por último, tendríamos que llamar a este método desde la activity u origen de la acción que lanza la tarea de añadir el producto



```kotlin
private fun lanzarTarea(){
    adaptadorProducto.addProducto(Producto("Zapatillas", 150.0, "Zapatillas de deporte preparadas para cualquier tipo de terreno", R.drawable.zapatillas))
}
```



En el caso de querer gestionar la pulsación de alguno de los elementos de la lista, es necesario realizarlo directamente en la clase donde se ha generado el adaptador, ya que es ahí donde se encuentran cada uno de los elementos gráficos. Si quiérenos llevar datos desde la clase adaptador hasta la clase de la activity, necesitaríamos utilizar una interfaz de callback.

En el siguiente video podemos ver cómo realizar tanto la gestión de pulsaciones en las filas del recycler como el uso de las interfaces de comunicación



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652022_1/scormcontent/assets/INSD_DM_Unidad2_Apartado3_2_Video2.mp4?v=1)



### 2.3 Menús



Otro de los elementos genéricos dentro de una aplicación son los menús. Estos permiten incorporar funcionalidad sin tener que desperdiciar gran parte de la interfaz. Por regla general los menús suelen estar situados en la parte superior de la interfaz, bien sea en el toolbar o en el actionbar.

Para poder crear el menú, es necesario crear un recurso XML donde se indique cada una de las opciones del menú. Este recurso estará ubicado en la carpeta menú dentro de la carpeta res. Para poder crearlo es necesario seleccionar desde la carpeta res, botón derecho y new -> Android Resource Directory



![image](assets/cm6xlvlpj0126356zamugmh9j-Imagen8.jpg)



Una vez creada la carpeta podremos crear en ella el fichero XML que representa el menu. Cada uno de los elementos que forman parte del fichero serán las opciones, englobadas dentro de la etiqueta item. Algunas características importantes de estos elementos son:



- **title**  
  Será el título de la opción y que aparecerá en el menú. Es el único atributo que es obligatorio.
- **id**  
  Será el elemento que se utilice para poder gestionar la pulsación del elemento. No es un elemento obligatorio, pero si muy recomendable, ya que sin es sería imposible detectar su pulsación.
- **showAsAction**  
  Este elemento indica si el item se representará como icono en la barra superior en el caso de tener espacio disponible. En el caso de estar puesto en portrait la cantidad de elementos será aproximadamente 2, y en el caso de ser vertical será una cantidad de 3. Las opciones disponibles son:

  - ifRoom: los elementos aparecerán en la parte superior si hay espacio
  - never: no aparecerán nunca. Es la opción por defecto
  - always: se fuerza la aparición de los elementos
- **icon**  
  Indica cual es el elemento icono, que aparecerá junto con el título del elemento.



![image](assets/cm6xm0u5q014a356zgeubyj1j-Imagen10.jpg)



El siguiente paso sería asignar el fichero en la parte superior. En este punto hay dos opciones:

- **Utilizar un ActionBar:** es el elemento que está puesto en la parte superior por defecto. Para poder activarla, es necesario poner el tema correspondiente. Por defecto está puesto uno que no tiene barra superior. Para poder activarlo hay que entrar en el fichero ubicado en res -> values -> themes y en el style que tiene como nombre Base.Theme.NombreAplicacion habrá que quitar NoActionBar



```xml
<style name="Base.Theme.Tienda" parent="Theme.Material3.DayNight">
    <!-- Customize your light theme here. -->
    <!-- <item name="colorPrimary">@color/my_light_primary</item> -->
</style>
```



- **Utilizar un Toolbar:** se trata de un elemento que sustituye al ActionBar. Gráficamente es el mismo funcionamiento, pero funcionalmente tiene muchas más capacidades como por ejemplo incorporar un menu lateral que se despliega con deslizar hacia un lado. A diferencia del ActionBar, en este caso es necesario indicar en el XML de la activity el Toolbar como elemento del layout



```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <androidx.appcompat.widget.Toolbar
        android:titleTextColor="@color/white"
        android:id="@+id/toolbar"
        android:layout_width="match_parent"
        android:layout_height="?attr/actionBarSize"
        android:background="@color/material_dynamic_primary40"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <androidx.recyclerview.widget.RecyclerView
        android:id="@+id/recyclerProductos"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@id/toolbar" />
</androidx.constraintlayout.widget.ConstraintLayout>
```



Como se puede ver en el código, el elemento toolbar (de la librería de androidx) tiene un id asignado. Este atributo no solo vale para poder colocarlo con respecto a otros dentro de un coonstraint layout, sino que también es necesario para poder asignarlo. Esta asignación se realiza en la parte lógica, ya que el toolbar aparecerá, pero no está configurado como parte superior de la pantalla donde se pone tanto menú como título. Para ello, tendremos que ejecutar el método setSupportActionBar dentro del fichero kotlin:



```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    binding = ActivityMainBinding.inflate(layoutInflater)
    setContentView(binding.root)
    setSupportActionBar(binding.toolbar)
}
```



Con esto, la parte superior de la aplicación estará preparada para poder gestionar el menú. El siguiente paso es configurar la pantalla para que represente el menú. Para ello es necesario sobrescribir dos métodos: onCreateOptionMenu y onOptionItemSelected. Ambos se encargan de los siguiente:

- **onCreateOptionMenu:** se encarga de renderizar el menú creado en el punto anterior en el Toolbar o ActionBar configurado
- **onOptionItemSelected:** se encarga de identificar que opción del menú ha sido pulsado para ejecutar la acción concreta en cada momento

Estos dos métodos son sobrescritos, ya que están disponibles dentro de la clase AppCompactActivity



```kotlin
override fun onCreateOptionsMenu(menu: Menu?): Boolean {
    
    menuInflater.inflate(R.menu.main_menu, menu)
    return true
}

override fun onOptionsItemSelected(item: MenuItem): Boolean {
    
    when(item.itemId){
        R.id.menu_info->{
            // tarea a realizar tras la pulsación
        }
        R.id.menu_login->{
            // tarea a realizar tras la pulsación
        }
        R.id.menu_logout->{
            // tarea a realizar tras la pulsación
        }
    }
    return true
}
```



En el método onCreateOption se pasa un parámetro de tipo menu, que representa el menú que todo Toolbar / Actiobar tiene, aunque puede que no se represente. Mediante el método inflate se asocia el fichero creado con este menu

En el método onOptionItemSelected, se pasa como parámetro un MenuItem, que es el elemento pulsado dentro del menú. Mediante un when y preguntando por el id de dicho elemento, se puede gestionar la pulsación del elemento concreto.



### 2.4 Diálogos



El último que suelen aparecer dentro de una interfaz son los cuadros de diálogo. Estos permiten a la aplicación mostrar y obtener información de manera modal mediante ventanas emergentes. Existen dos grandes tipos de cuadro de diálogo:



- **Preconstruidos**  
  Aquellos que el SDK de Android permite gestionar de manera sencilla.
- **Personalizados**  
  Son muy similares a los anteriores, con la diferencia que la parte visual es personalizada, ya que tendría un XML donde se representa la información.



En este punto nos vamos a centrar en los preconstruidos. Antes de empezar a construirlos, es importante tener en cuenta cual es la estructura básica que tienen los diálogos. Sería la siguiente:



![image](assets/cm6xmikk801dk356z4lu8ishv-Imagen11.png)



Para poder crear un cuadro de diálogo, lo podríamos hacer en una clase independiente que extendiese de DialogFragment (siempre de androidx), o crearlo directamente asociándolo a una variable. En el caso de los diálogos preconstruidos esta segunda opción es muy viable, ya que tan solo tendremos que utilizar un objeto de tipo AlertDialogBuider que representará el elemento que permite crear el diálogo y un objeto de tipo AlertDialog que representará el propio diálogo.



```ini
var builderDialogo = AlertDialog.Builder(applicationContext)
var dialogoAlerta = builderDialogo.create()
```



Una vez creado estos elementos, bastaría con configurar cada una de las partes que queremos que tenga el cuadro de diálogo, siguiendo la estructura que queremos que tenga. Dentro de las posibilidades, podremos utilizar los siguientes métodos:



- **setTitle**  
  Indicando un string que aparecerá en la zona del cuadro de diálogo.
- **setMessage**  
  Indicando un string que aparecerá en la zona de mensaje o lista.
- **setItem**  
  Indicando una lista de opciones y como se gestiona la pulsación de estas, detectando cual es la seleccionada y ejecutando de forma directa la acción final.
- **setMultiChoice**  
  Indicando una lista opciones y como se gestiona la pulsación de estas. Además, es necesario indicar cuales de ellas están seleccionadas de inicio mediante un array de booleans.

  La diferencia con la lista anterior es que en este caso se pueden seleccionar varias al mismo tiempo y que es necesario tener un botón positivo, negativo o neutral para poder lanzar la acción final.
- **setSingleSelection**  
  Muy similar al anterior, con la diferencia que solo se puede seleccionar un elemento al mismo tiempo. Como parámetros hay que darle una lista de opciones, cual es la seleccionada al arrancar y como se maneja la pulsación de estas. A diferencia del cuadro de diálogo anterior, no es necesario ningún botón ya que se puede arrancar la opción final al seleccionar una opción.
- **setOnPositiveButton**  
  Indica la existencia de un botón con acción positiva, además de la pulsación de este.
- **setOnNegativeButton**  
  Idéntico método que el anterior, pero indicando acción negativa.
- **setOnNeutralButton**  
  Idéntico método que el anterior, pero indicando acción neutral.



Algunas cosas que hay que tener en cuenta sobre los métodos comentados anteriormente son:

- El método de los botones es indiferente a las acciones que se le atribuyen. Son más para colocación, siendo esta de izquierda a derecha: neutra, negativo y positivo
- En la parte central del cuadro de diálogo tan solo puede aparecer un elemento, por lo que tan solo se puede ejecutar un método que configure un mensaje o una lista de selección (simple, múltiple o directa)

Un ejemplo de código con todos los métodos comentados sería el siguiente



```markdown
var builderDialogo = AlertDialog.Builder(applicationContext)
builderDialogo.setTitle("Indica el título del diálogo que quieres crear")
builderDialogo.setMessage("Indica el mensaje que quieres transmitir en el cuadro de diálogo")
val opciones = arrayOf("Opcion1","Opcion2","Opcion3")
builderDialogo.setItems(opciones, DialogInterface.OnClickListener { dialog, which ->  })
builderDialogo.setSingleChoiceItems(opciones, 0, DialogInterface.OnClickListener { dialog, which ->  })
builderDialogo.setMultiChoiceItems(opciones, null, DialogInterface.OnMultiChoiceClickListener { dialog, which, isChecked ->  })
builderDialogo.setPositiveButton("OK", DialogInterface.OnClickListener { dialogdialog, which ->  })
builderDialogo.setNegativeButton("NO", DialogInterface.OnClickListener { dialogdialog, which ->  })
var dialogoAlerta = builderDialogo.create()
```



Una vez el objeto del cuadro de diálogo creado, tan solo falta mostrarlo. Para ello se ejecuta el método show sobre dicho objeto



```ini
dialogoAlerta.show()
```



El aspecto que tendrá cada uno de los cuadros de diálogo es el siguiente:



![image](assets/cm6xmtbmg01lg356zcy9uusg8-Imagen12.jpg)



Además de este tipo de creación, también existe la posibilidad de hacerlo mediante clases externas, extendiéndolas de DialogFragment y sobrescribiendo los métodos necesarios, siendo el onCreateDialog el encargado de hacer todas las tareas que hemos visto en este punto.



## 3. Fragments



### 3.1 Introducción



![image](assets/cl3isuljk005x396ljvqiqoc5-stock-image.jpg)



Los fragments son elementos que permiten la modulación dentro de la pantalla. En grandes rasgos, un fragment es un elemento individual (con xml propio) que se incorpora dentro de una activity. Esta incorporación puede ser de dos tipos: estática (se declara el elemento en el xml de la pantalla) o dinámica (no se declara el elemento, sino que puede ser cambiante). Dependiendo de cuál sea el uso que se quiera dar, utilizaremos uno u otro. Por ejemplo, si todas las pantallas de nuestra aplicación tienen la misma cabecera, podremos crear un fragment estático para agregarlo en cada una de las pantallas. En el caso de tener una aplicación donde la parte central queremos que cambien en un momento determinado (sin necesidad de que cambie la activity), utilizaremos un fragment dinámico. De forma general los fragments que se utilizan son los dinámicos por la versatilidad que ofrecen a la hora de crear interfaces de usuario. A diferencia de las activitys, estos elementos no se tienen que declarar dentro de AndroidManifest, ya que se incorporar como elementos gráficos dentro de la pantalla.

Para poder aclararnos con el concepto de fragment, imaginemos una aplicación que tiene un menú inferior que muestra un menú con tres posibles opciones. Con la pulsación de cada una de estas, la parte central de la pantalla cambia y se muestran elementos diferentes. Esta parte central estará formada por un elemento especial de tipo fragment que permite mostrar diferentes elementos según la pulsación del menú.



![image](assets/cm6xn28bu01o6356zuawlius7-Imagen13.png)



En este caso tanto el fragment lista como el fragment form aparecerán con la pulsación de alguno de los botones del botón inferior.

Como elemento individual, los fragment se representan con clases que extienden de fragment, teniendo en cuenta que esta debe ser de soporte (librería androidx) para que puedan ser utilizados en cualquier dispositivo con nivel de api. Es importante tener en cuenta, que al igual que las activitys, los fragment tienen su propio ciclo de vida ya que se incorporar dentro de la pantalla. Este ciclo es el siguiente:



![image](assets/cm6xn32mw01pj356z9f0cic81-Imagen14.png)



Como se puede observar en la imagen, los métodos coinciden en gran medida con los de las activitys, incorporando algunos para poder gestionar de forma correcta la aparición – desaparición de los elementos. Entre ellos caben destacar los siguientes:

- **onAttach:** durante este método el fragment se vincula con la actividad. Se suele utilizar para poder trabajar con el contexto, ya que es parámetro pasado por el método.
- **onCreate:** durante este método el fragmento ya está asociado, pero no cuenta con interfaz gráfica. Se suele utilizar para poder instanciar elementos lógicos
- **onCreateView:** una vez el fragmento queda creado, el fragmento se asocia a la parte gráfica. Tiene la misma funcionalidad que el método onCreate de las activitys
- **onActivityCreated:** el fragmento ya está disponible y empieza a ser visto, por lo que se utiliza para poder utilizar los elementos gráficos e interactuar con ellos

La misma metodología se produce cuando el fragment deja de ser visto. Para ello existen los métodos onDestroyView, onDestroy, onDettach los cuales permiten la liberación de memoria, gestión de estados, etc.

En el siguiente video se puede ver un ejemplo de funcionalidad de los fragments, explicando su ciclo de vida y su gestión.



### 3.2 Estructura de un fragment



Una vez se ha entendido cual es cometido y funcionalidad de los fragments, se va a explicar ahora cuál es la estructura. Los fragments, al igual que las activitys, están representados por una clase separada, la cual extiende de Fragments. Al ser un elemento lógico, no es necesario declararlo en el AndroidManifest.xml como ya se ha comentó, pero si es necesario que tenga una parte gráfica por lo que los elementos que lo forman son:

- fragment_layout.xml: fichero que representa la parte lógica del fragment
- MainFragment.kt: fichero que representa la parte lógica del fragment

El tema de los nombrados es importante, ya que cuando se configura la vista del fragment en la clase, utilizaremos la característica de binding para asociar la parte gráfica

Para poder crear uno, teniendo en cuenta las dependencias de archivos que acabamos de comentar quedaría de la siguiente forma:

- El fichero gráfico representa como se verá esa parte de la aplicación. Para este ejemplo se mostrará un texto y un botón para su posterior pulsación



```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="FRAGMENT LISTADO"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:layout_marginTop="20dp"
        android:id="@+id/botonNavegarFListado"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Ver detalle"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/textView" />

</androidx.constraintlayout.widget.ConstraintLayout>
```



De este fichero, simplemente hay que destacar que incorporaremos todas aquellas cosas que queramos que aparezcan en un momento determinado.

- El fichero lógico, el cual permite asociar la parte gráfica y gestionar cada una de las interacciones que se quiere tener, así como todos los datos que queramos



```kotlin
class ListadoFragment: Fragment() {
    
    private lateinit var binding: FragmentListadoBinding

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentListadoBinding.inflate(inflater,container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        // método destinado a la gestión de los elementos de la interfa<
        binding.botonNavegarFListado.setOnClickListener { 
            // acción a ejecutar con la pulsación del botón
        }
    }
}
```



Como se puede ver en el código, el método onCreateView se utiliza para hacer la asociación del fichero gráfico mediante la instancia del binding, mientras que el método onViewCreates se utiliza para poder utilizar todos los elementos gráficos que sean necesarios ya que durante la ejecución del método ya están disponibles.

Al igual que se ha comentado en el fichero gráfico, en este tendríamos que configurar todos los escuchadores, gestión de elementos lógicos como adaptadores, consultas con bases de datos, etc… que se consideren necesarios.

Teniendo en cuenta el ejemplo que hemos seguido antes, en este fragment podríamos incorporar el recycler realizado al principio de la unidad para hacer que, en vez de pertenecer a la activity, este pertenezca al fragment y así hacerlo aparecer - desaparecer en un momento dado sin necesidad de tener que cambiar de pantalla.

Una vez creados tantos fragments como sean necesarios, es el momento de realizar el cambio de los mismos en la interfaz cuando sea necesario. Para ello, se puede realizar de dos formas:



- **Manualmente**  
  Para ello es necesario agregar dentro del XML de la activity un layout que permita realizar el remplazo de los fragments que se quieren mostrar por los que están visibles. Para poder utilizar esta característica, es necesario tener una serie de cosas claras:

  - El layout utilizado dentro de la activity tiene que ser de tipo FrameLayout, ya que es el que permite superponer elementos y mostrar solo uno de ellos, a modo pila. Imaginemos una
  - Dentro de la parte lógica, es necesario utilizar una variable de tipo fragmentmSupportManager para poder gestionar la pila comentada en el punto anterior y una variable de tipo fragmentTransaction para poder realizar las acciones que se quieran ejecutar sobre los fragment (agregarlos, eliminarlos, remplazarlos, etc.)
- **Automática**  
  Se trata de la opción más recomendable ya que permita realizar una navegación más intuitiva gracias a la creación de un gráfico de navegación donde se indican los fragments que forman parte del flujo y conectar cada uno de ellos con los caminos que se necesiten. Para poder utilizar esta forma de gestión es necesario:

  - El layout utilizado dentro de la activity puede ser cualquiera, pero dentro del mismo tiene que hacer un elemento de tipo fragment con el atributo name como androidx.navigation.fragment.NavHostFragment para que se pueda cumplir la navegación. Este elemento es el que antes hemos calificado como parte central que se irá modificando.
  - Además del elemento comentado anteriormente, es necesario tener creado y configurado un gráfico de navegación, donde se indicarán los fragments navegables y las transiciones entre cada uno de ellos. Gracias a este gráfico de navegación, la gestión de los fragments es mucho más sencilla.



### 3.3 Navegando entre fragments



Para facilitar las cosas, a continuación, se explicará la gestión automática de los fragments. Antes de empezar, el escenario de partida es una aplicación con dos fragments, los cuales tienen los siguientes aspectos gráficos:



![image](assets/cm6xnfpkx01v1356zftrhh9w6-Imagen15.jpg)



La navegación que se configurará es la siguiente: Al pulsar el botón del fragment uno, se sustituirá este por el fragment 2 y cuando se pulse el botón que está en el fragment 2 se sustituirá este por el fragment 1.

Una vez configurado esto, el siguiente paso es incorporar en el XML de la activity donde se quiera gestionar la navegación de los dos fragments, un elemento de tipo fragment:



```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".FragmentActivity">

    <fragment
        android:name="androidx.navigation.fragment.NavHostFragment"
        android:id="@+id/navhost"
        android:layout_width="0dp"
        android:layout_height="0dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```



Como se puede ver en el código, dentro del elemento fragment que servirá como el panel que soporte la navegación, debe tener de forma obligatoria un atributo name con la configuración del NavHostFragment. Esto en un primer momento dará error, ya que se trata de un elemento adicional al SDK de Android, por lo que es necesario incorporar la dependencia dentro del fichero build.gradle (a nivel de módulo), incorporando la siguiente línea de código en el bloque de dependecies:



```ini
implementation("androidx.navigation:navigation-fragment:2.7.7")
```



Una vez incorporada la dependencia y sincronizado el proyecto, se puede crear un gráfico de navegación que permita gestionar el flujo de la ampliación. Para ello será necesario los siguientes pasos:

- Crear el gráfico de navegación: dentro de la carpeta res, crearemos un recurso llamado navigation. Para esto, pulsando botón derecho en la carpeta res -> créate Android resource directory -> indicando que es de tipo navegación. Cuando la carpeta esté disponible, podremos crear dentro un recurso de navegación, pulsando botón derecho sobre ella y new -> navigation resource file. Se le dará el nombre main_navigation y tendremos un recurso XML.
- Dentro del layout de la actividad, referenciaremos el fichero que acabamos de crear dentro del nodo fragment. Para ello, se añade el atributo navGraph asociándolo al recurso creado. Además, lo marcaremos como el elemento de navegación por defecto.



```ruby
<fragment
    android:name="androidx.navigation.fragment.NavHostFragment"
    android:id="@+id/navhost"
    android:layout_width="0dp"
    android:layout_height="0dp"
    app:defaultNavHost = "true"
    app:navGraph =  "@navigation/main_navigation"
    app:layout_constraintBottom_toBottomOf="parent"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintTop_toTopOf="parent" />
```



Con estas configuraciones está el proyecto para poder realizar la navegación. Lo primero que será necesario es crear el gráfico de navegación dentro del recurso que se creó. En este fichero tenemos la posibilidad de crear cada uno de los destinos mediante código XML o hacerlo gráficamente.

Por último, será necesario realizar cada una de las acciones en la parte lógica de la activity. Para ello, lo primero que será es utilizar el navhost creado en la activity y ejecutar el método. Esta tarea es muy sencilla, ya que basta con ejecutar el método findNavController para poder obtenerlo, pasando como parámetro el id del fragment, en nuestro caso llamado navHost. Esto puede valer para guardarlo en una variable y es gracias a que se marcó la propiedad defaultNavHost a true, por lo que es el elemento de navegación por defecto. Una vez encontrado el elemento de navegación, hay que ejecutar el método navigate cuando se quiera realizar la acción, pasando el id de la navegación que se quiera. En el caso de querer hacer la navegación desde un fragment, es necesario buscar el elemento de navegación desde el método requireActivity. En nuestro ejemplo lo haremos en el fichero que representa el fragment listado, tras la pulsación del botón:



```kotlin
class ListadoFragment : Fragment() {
    private lateinit var binding: FragmentListadoBinding

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentListadoBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        
        binding.botonNavegarFListado.setOnClickListener {
            
         val navHostFragment =
                requireActivity().findNavController(com.example.tienda.R.id.navhost)
            navHostFragment.navigate(com.example.tienda.R.id.action_listadoFragment_to_detalleFragment)
        }
    }
}
```



En el siguiente video se muestra la funcionalidad completa junto con el código de ambos fragments explicado.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652022_1/scormcontent/assets/INSD_DM_Unidad2_Apartado4_3_Video.mp4?v=1)



Una de las cosas interesantes cuando se trabaja con fragments es la gestión de la pila. Esta actúa como un contenedor que va apilando los fragments según se van sustituyendo por otros o eliminarlos directamente. Esto depende del programador, por lo que es necesario gestionarlo.

Por defecto cuando se navega a un fragment, se realiza un proceso de reemplazo del fragment anterior por el existente que se carga automáticamente en la pila. Este proceso puede ser controlado desde las propiedades de las acciones, seleccionando las mismas y modificando los atributos pupUpTo y popUpToInclusive. Vamos a explicar cómo funcionan ambos atributos:

- En el caso del atributo popUpTo, se indica cual es el fragment que será cargado en el caso de dar al botón de atrás (acción de onBackPressed), dejando el resto de la pila descargada. De esta forma si realizamos una navegación entre diferentes fragment y llegamos a uno que tiene configurado dicho atributo, al dar al boton de atrás se cargará en la pila solo el fragment indicado.
- En el caso del atributo popUpTo incluse tiene dos posibilidades. En el caso de configurado como true, aunque el atributo popUp esté configurado con algo el fragment actual será el último y al dar al botón atrás se cerrará la aplicación. En el caso de configurado como false, se cargará el fragment indicado en el atributo popUp pero no se mantendrá en la pila.

Además de este manejo de estado de la pila, se puede controlar las animaciones de entrada y salida de cada una de las acciones indicando que animación se ejecutaré en cada momento. Todas estas opciones se pueden configurar desde el gráfico de navegación.

Como último punto para poder tener una funcionalidad completa de la navegación, tenemos la posibilidad de pasar parámetros entre fragments. Al igual que ocurrió en el tema anterior, es posible que cuando queremos realizar un cambio de fragment, además de realizar esta acción de remplazo, se quiera pasar algún tipo de dato para que sea procesado en el fragment destino.



![image](assets/cm6xnmfbk022j356zzj1ucozf-Imagen16.jpg)



Esta comunicación, jamás puede ser directa entre clases, ya que de esta forma los datos pueden perderse en el proceso de comunicación. Para poder hacerlo de forma correcta, el proceso tiene que pasar siempre por el único elemento común que tienen ambos fragments y este es la activity. De forma manual es complejo ya que tendríamos que crear un objeto de tipo companion (los static de java) y lanzar dicho fragment de esta forma. Sin embargo, de forma automática mediante el grafico de navegación es un proceso sencillo que consta de dos pasos:

**Creación de las dependencias que tiene el fragment destino:** Estas dependencias reciben el nombre de argumentos y lo primero que hay que hacer es marcar cuales son aquellos que va a recibir el destino. En este caso el fragment detalle recibe un objeto de tipo producto, indicando el tipo que tiene el dato y si tiene posibilidad de ser nulo. Esta configuración se realiza seleccionando en el gráfico de navegación el destino



![image](assets/cm6xvrtjs02b8356zjshl54l4-Imagen17.jpg)



En esta configuración el argumento recibirá un nombre o tag que será el utilizado para poder recuperarlo desde la parte lógica. Es importante tener en cuenta que, si el dato es un objeto no primitivo, será necesario que implemente la interfaz serializable o parcelable. En la configuración del fichero XML de navegación se creará el siguiente nodo:



```ini
<argument
    android:name="producto"
    app:argType="com.example.tienda.model.Producto" />
```



Con esto se indica que ese fragment tiene la capacidad de recuperar argumentos con el tipo de dato indicado y el tag asociado (configurado como producto en el ejemplo. Para que esto se pueda llevar a cabo, lo siguiente sería realizar el envió y gestionar la recepción del dato:

- **El envío de los datos:** se realizará desde el fragment que provoca el remplazo y es origen de la transición. En el ejemplo estaríamos hablando del fragment listado. Para ello, y tras la pulsación de o ejecución de la acción que queremos que provoque la navegación, se ha visto antes que mediante el método navigate se provoca dicha acción. En este caso, a ese método se le tiene que pasar un objeto de tipo Bundle donde va incorporado el dato que se quiere pasar mediante un par clave – valor. Para este ejemplo, tras la pulsación del botón, se pasará un objeto cualquiera:



```kotlin
binding.botonNavegarFListado.setOnClickListener {

    val bundle: Bundle = Bundle()
    bundle.putSerializable("producto",Producto("Camiseta",30.0,"Camiseta de deporte realizada en tejido transpirable 100%",com.example.tienda.R.drawable.camiseta))
    val navHostFragment =
        requireActivity().findNavController(com.example.tienda.R.id.navhost)
        navHostFragment.navigate(com.example.tienda.R.id.action_listadoFragment_to_detalleFragment, bundle)
}
```



Como se puede ver en el código, el objeto de tipo producto es incorporado a la variable budle y esta a su vez pasada como segundo parámetro al método navigate. De esta forma el elemento de navegación realiza la sustitución indicada en la acción y además el paso de parámetro entre fragments

- **Recepción de los datos:** una vez producida el remplazo de un fragment por otro, el primer paso en el destino es obtener el parámetro pasado. Para ello se utiliza el método onAttach (se recuerda que es el primer método del ciclo de vida de un fragment) para poder recuperar el parámetro y guardarlo en una variable.



```kotlin
class DetalleFragment: Fragment() {

    private lateinit var binding: FragmentDetalleBinding
    private lateinit var producto: Producto

    override fun onAttach(context: Context) {
        super.onAttach(context)
        producto = requireArguments().getSerializable("producto") as Producto
        Log.v("dato",producto.nombre.toString())
    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentDetalleBinding.inflate(layoutInflater, container, false)
        return binding.root
    }
}
```



En el método onAttach se puede observar como se recoge el dato pasado mediante requireArguments, indicando el tipo de dato a recuperar y el tag con el que se registró en el gráfico de navegación. En el caso de haber indicado que el dato pudiese ser nulo, se hubiese realizado mediante la variable arguments e indicando que la variable tenía la posibilidad de ser nula (con el operador null safety ?). De esta forma el parámetro está disponible en cualquier parte de la ejecución del fragment y utilizable como por ejemplo para mostrar sus datos cuando la vista del fragment ya ha sido cargada



```kotlin
override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
    super.onViewCreated(view, savedInstanceState)
    binding.imagenDetalle.setImageResource(producto.imagen)
    binding.textoDetalle.text = producto.nombre
}
```



Cabe recordar que todas estas configuraciones son compatibles con el resto de los componentes vistos a lo largo del tema. Un claro ejemplo sería el lanzar un cuadro de diálogo tras la pulsación del botón en el fragment de detalle que muestre más información del producto actual.



### 3.4 Basic view Activity



Como es lógico, en la mayoría de los proyectos que se llevan a cabo, lo normal no es empezar desde 0 implementando y configurando todos los elementos que son comunes en una aplicación. En esta unidad hemos visto como poder realizar todas estas implementaciones ya que es necesario tener la base de cómo funciona todo, sin embargo, existen plantillas en Android Studio que incorporar la mayoría de estas cosas ya implementadas. Una de ellas y posiblemente la más importante es la plantilla Basic View Activity.

Si hacemos un breve repaso dentro de las configuraciones que toda aplicación suele tener nos encontramos con los siguientes elementos:

Barra superior configurada como toolbar para que se puedan incorporar elementos adicionales como menús laterales desplegables, vistas en la barra superior, cambios de texto, etc.

Menú de opciones en la parte superior derecha que parte seleccionar menuItems para la ejecución de funciones

Parte central donde se posibilita la navegación mediante fragments utilizando un gráfico de navegación.

Adicionalmente y aunque no lo hemos visto, también es usual encontrarnos con un botón en la parte inferior derecha a modo de elemento flotante que puede aparecer y desaparecer según acciones de la propia interfaz. Este elemento recibe el nombre de FloatingActionButton

Activada la funcionalidad binding para poder hacer una asociación directa entre la parte gráfica y la parte lógica. Esta característica queda activada dentro del fichero build.gradle



![image](assets/cm6xw0ure02i9356zhilev4oy-Imagen18.jpg)



Para poder presentar y ver toda la funcionalidad de la plantilla, se adjunta un video donde se explica su funcionamiento y los componentes de esta.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652022_1/scormcontent/assets/INSD_DM_Unidad2_Apartado4_4_Video.mp4?v=1)



## 4. Persistencia De Datos



### 4.1 Introducción



![image](assets/cm6xw3zpw02km356zq2imteem-stock-image.jpg)



Cuando hablamos de cualquier tipo de aplicación, es evidente que esta no tendría ningún tipo de sentido sin los datos. Por ello esta es una parte crucial dentro del desarrollo. En una ejecución normal, la cantidad de datos que son mostrados y procesados por la aplicación es muy grande, y estos se le deben presentar al usuario de forma consistente tantas veces como éste considere necesarias. Si como desarrolladores no tenemos la capacidad de asegurar esta disponibilidad de los datos al usuario, nuestra aplicación no tendrá mucho valor. Por ello guardar la información y saberla gestionar es esencial en cualquier aplicación de Android. Este manejo de los datos permite a las aplicaciones recordar datos clave, guardar información del usuario para futuras sesionas, así como manejar toda la información compartida tanto con otros usuarios como con otros dispositivos. En el caso de no disponer de un sistema de almacenamiento, la vida de los datos terminará en el momento en el que la aplicación se cierre, por lo que no tendremos consistencia alguna. Para ello, Android ofrece una serie de servicios que permite esta gestión y almacenamiento de los datos, siendo cada una de ellas válida para diferentes escenarios que nos podamos encontrar. Las posibilidades de base de datos son:



- **Shared Preferences / DataStore**  
  Se trata de una de las soluciones más sencillas de implementar, pero a la vez la que menos servicios ofrece. Se trata de un servicio interno del teléfono que guardar datos simples como booleans, floats, ints, longs y strings con formato de clave-valor. Al tratarse de un servicio donde los datos que se pueden guardar no son completos y se asocia a cada aplicación, se suele utilizar para la gestión de sesiones, recordar preferencias de selección del usuario, etc. Tanto el servicio de Shared Preferences como el de DataStore coexisten, pero es más recomendable DataStore ya que aporta más seguridad a los datos
- **SQLite**  
  Es la base de datos interna de cada una de las aplicaciones, utilizando estructura SQL, lo que permite guardar datos complejos con relaciones entre las diferentes tablas. Se trata de un servicio muy eficaz a la hora de guardar los datos, pero con la contraprestación de que estamos hablando de un servicio individual para cada aplicación, ya que es una base de datos que se guarda en local. Cuenta con un potente ORM llamado Room que permite reducir la complejidad de la gestión del dato y mejora el funcionamiento de los datos.
- **Ficheros**  
  Al igual que cualquier otro dispositivo, Android cuenta con un sistema de almacenamiento externo que puede ser utilizado para guardar y recuperar ficheros. Como sistema de base de datos no es muy utilizado, pero si como sistema de almacenamiento y recuperación de imágenes / videos.
- **Firebase**  
  Se trata de un poderoso servicio de Google que proporciona una serie de herramientas en la nube para gestionar no solo datos que pueden ser compartidos entre usuarios, sino que también ofrece servicios de autenticación, almacenamiento, etc. Alguna cosa muy interesante a tener en cuenta a la hora de trabajar con este tipo de servicios es:

  - Estamos hablando de servicios a tiempo real, por lo que el usuario no tendrá que refrescar pantalla para poder actualizar los datos
  - Las bases de datos son No SQL, lo que imposibilita las relaciones de forma nativa y que permite la utilización de servicios de proveedores externos para poder loguear un usuario como por ejemplo cuentas de Google, Facebook, etc. Este servicio será en el que nos centremos en este punto.
  - Se trata de servicios independientes, por lo que podemos utilizar el que mejor se acople a nuestra aplicación sin tener que utilizar el resto.
- **Consumo de API personalizada**  
  Por último, es posible que necesitemos una consulta de datos sobre un sistema con una solución personalizada, por lo que sería necesario, utilizando el modelo de 3 capas, realizar peticiones HTTP al API en cuestión para que se puedan resolver las acciones configuradas. El uso de esta solución es también muy extendido ya que ofrece una mayor personalización de la gestión de los datos. Para poder realizar este tipo de acciones se suelen utilizar librerías externas como RetroFit o Volley para facilitar el proceso.



Nos centraremos en estos últimos servicios a la hora de gestionar los datos.



### 4.2 Firebase



Como se ha comentado antes, Firebase representa una solución cloud desarrollada por Google que ofrece multitud de servicios y pone a disposición de los desarrolladores herramientas backend con una implementación realmente sencilla. Una de las cosas importantes a tener en cuenta a la hora de elegir este tipo de soluciones, es que ofrece servicios multidispositivo, es decir que un mismo proyecto firebase puede estar enlazado a un proyecto Android, IOs, Web, Unity y Flutter. Esta característica es importante, ya que los datos podrán ser accesibles desde cualquier parte gracias a esta gestión.

Antes de empezar a conectar nuestra aplicación a los servicios de Firebase, es necesario crear un proyecto en su plataforma. En el siguiente video se explica cómo realizar el proceso tanto de creación como de activación de cada uno de los servicios.



> [Link al vídeo](https://u-tad.blackboard.com/courses/1/2602_INSD3_DAMO_A/content/_652022_1/scormcontent/assets/INSD_DM_Unidad2_Apartado4_Video.mp4?v=1)



Una vez creado el proyecto firebase y activados todos los servicios que se quieren utilizar dentro de la aplicación, el siguiente paso es asociar el proyecto Android con el proyecto Firebase creado. Como ambas soluciones son de Google, en Android Studio se incorpora un asistente que permite de manera sencilla asociar ambas soluciones. Este asistente lo podemos encontrar dentro del menú tolos -> firebase. Aparecerá en la parte izquierda un asistente donde seleccionando el servicio que queramos activar quedará ya disponible dentro de nuestra aplicación. De forma general los pasos que habrá que seguir dentro de este asistente son los siguientes:

- Conectar nuestro proyecto Android con el proyecto Firebase: Esto solo será necesario hacerlo en el primer servicio. En el proceso, nos pedirá iniciar sesión con nuestra cuenta Google en la consola firebase donde tengamos el proyecto creado. Al finalizar este paso avisará que el proyecto ya está asociado correctamente.
- Descargar las dependencias necesarias en para que el servicio seleccionado funcione correctamente. Estas dependencias se incorporarán automáticamente en el fichero build.gradel y se actualizará para su descarga. Esto será necesario hacerlo por cada servicio, ya que cada uno tiene unas librerías diferentes
- Además de estos pasos, en el asistente se muestra un ejemplo de uso del servicio en cuestión, mostrando códigos de ejemplo de cada una de las funcionalidades

Una vez hecho esto, tendremos nuestro proyecto Android preparado para utilizar cada uno de los servicios seleccionados.



#### Autenticación



Una de las primeras cosas que son necesarias a la hora de hacer una aplicación que gestiona usuarios, es crear el servicio de registro y login en la aplicación. En el caso de firebase, este servicio ofrece de forma directa el cifrado de la contraseña, validación de correo, así como no duplicidad de los usuarios. Esto permite que muchas de las tareas necesarias se realicen de forma automática. Antes de empezar a crear e iniciar sesión a usuarios, es importante mencionar que el servicio de autenticación es independiente del servicio de base de datos, por lo que si queremos guardad datos de los usuarios más allá de los bases (momento de login, correo) será necesarios guardarlos en la base de datos mediante programación.

Cuando hablamos de autenticación mediante firebase, el servicio ofrece multitud de posibilidades, siendo sobre todo dos las predominantes: usuario – contraseña o mediante cuenta de proveedor externo (Google). Para poder activar estos métodos de autenticación tendremos que seleccionarlos. En el caso de seleccionar usuarios/contraseña (como será nuestro caso), tendremos una lista de los usuarios registrados, junto con su correo, fecha de registro, fecha de último inicio e identificador, que nos será muy útil para hacer relacionar datos con ese usuario.



![image](assets/cm6xwjg2c02qw356zricwk2kr-carousel1-Imagen19.jpg)

![image](assets/cm6xwjg2c02qw356zricwk2kr-carousel2-Imagen20.jpg)

![image](assets/cm6xwjg2c02qw356zricwk2kr-carousel3-Imagen21.jpg)



Una vez creado esto, podemos pasar a la implementación. Para este ejemplo, utilizaremos una pantalla donde mediante un formulario el usuario se podrá tanto loguear como registrar, dependiendo de la pulsación de los botones.



```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:gravity="center"
    android:padding="16dp">

   
    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="INICIO DE SESION"
        android:gravity="center"
        />
    <EditText
        android:id="@+id/login_username"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Nombre de usuario" />

    <EditText
        android:id="@+id/login_password"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Contraseña"
        android:inputType="textPassword" />

    <Button
        android:id="@+id/login_button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Iniciar sesión" />

    <!-- Formulario de registro -->
    <TextView
        android:layout_marginTop="50dp"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="REGISTRO"
        android:gravity="center"
        />
    <EditText

        android:id="@+id/register_username"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Nombre de usuario" />

    <EditText
        android:id="@+id/register_password"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Contraseña"
        android:inputType="textPassword" />

    <EditText
        android:id="@+id/register_confirm_password"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Confirmar contraseña"
        android:inputType="textPassword" />

    <Button
        android:id="@+id/register_button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Registrarse" />

</LinearLayout>
```



Antes de realizar tanto el inicio de sesión como el registro, es necesario tener disponible una instancia del servicio. Para ello se creará una variable de tipo FirebaseAuth que se inicializará en el servicio para poder utilizarlo.



```kotlin
class MainActivity : AppCompatActivity() {

    private lateinit var firebaseAuth: FirebaseAuth
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        firebaseAuth = FirebaseAuth.getInstance()
    }
}
```



Con el servicio disponible, lo que podremos hacer es:

- **Registrar un usuario:** Para ello se capturan todos los datos desde el formulario correspondiente y mediante el método createUserWithEmailAndPassword pasando como parámetros los datos capturados del formulario.



```kotlin
binding.registerButton.setOnClickListener {
    if (binding.registerPassword.text.toString() == binding.registerPassword.toString()) {
        firebaseAuth.createUserWithEmailAndPassword(
            binding.registerUsername.text.toString(),
            binding.registerPassword.text.toString()
        ).addOnCompleteListener { 
            if (it.isSuccessful){
                Snackbar.make(binding.root, "Usuario creado correctamente", Snackbar.LENGTH_SHORT).show()
            } else {
                Snackbar.make(binding.root, "Error en la creación del usuario", Snackbar.LENGTH_SHORT).show()
            }
        }
    }
}
```



De este código cabe destacar el procesamiento de la salida del método que permite crear al usuario. Al retornar un Task (no se sabe cuánto tardará en crear el usuario, depende de factores como la conexión a internet) es necesario evaluar mediante un listener cuál es la salida y actuar en consecuencia. En el ejemplo se mostrará una notificación con un mensaje u otro dependiendo de la respuesta. Hay que tener en cuenta que la creación del usuario puede ser incorrecta en los siguientes casos: email ya registrado, falta de datos y/o contraseña con baja complejidad (menos de 6 caracteres y/o sin combinación de letras - números).

En el caso de que todo se haya realizado correctamente, el servicio guardará un usuario en la nube con un UID único y generado de forma automática. De este usuario, en el momento que se registra se puede obtener a través del método firebaseAuth.currentUser, pudiendo así obtener parte de la información de este.

- **Logear un usuario:** Funcionalidad muy similar a la anterior, ejecutando el método sigInWithMailAndPassword y evaluando la salida de este método. En caso de ser correcta, el sistema podrá obtener datos del usuario y/o ejecutar una tarea determinada para el usuario en cuestión.



```kotlin
binding.loginButton.setOnClickListener {
    firebaseAuth.signInWithEmailAndPassword(
        binding.loginUsername.text.toString(),
        binding.loginPassword.text.toString()
    ).addOnCompleteListener {
        if (it.isSuccessful) {
            Snackbar.make(
                binding.root,
                "Usuario logeado correctamente",
                Snackbar.LENGTH_SHORT
            ).show()
            // ejecutar acción para un usuario dentro del sistema
        } else {
            Snackbar.make(
                binding.root,
                "Fallo en el inicio de sesión",
                Snackbar.LENGTH_SHORT
            ).show()
        }
    }
}
```



De esta forma, el usuario quedaría logeado y el siguiente paso sería realizar las tareas específicas como pasar de pantalla, mostrar datos adiciones, etc.



#### Base de datos



Para trabajar con bases de datos, lo primero que hay que saber es que se trata de bases de datos NoSQL, teniendo dos posibilidades: RealTime Database y Firestore. Ambas soluciones son en tiempo real, teniendo la diferencia entre ambas en la estructura de los datos:

- La primera de ella basa su estructura en un árbol de nodos con nodos rama de los cuales penden nodos hijo que tienen un valor asociado. Cada uno de estos nodos tienen que tener un nombre para poder tanto guardar datos sobre el cómo recuperarlo
- La segunda tiene consta de una serie de colecciones donde se guardan documentos, con un formato de JSON. Este tipo de base de datos es muy similar a la gestión de la base de datos MongoDB

En nuestro caso nos vamos a centrar en el uso de firestore database. Lo primero que debemos hacer es además de activar el servicio tanto en Android Studio como en firebase, es configurar las reglas. Estas indican que nivel de seguridad queremos que tenga nuestra base de datos. Por defecto y mientras dure el desarrollo seleccionaremos test mode, ya que nuestra aplicación tan solo será usada por nosotros a modo prueba.

Como se ha comentado antes, este tipo de base de datos cuenta con los siguientes elementos:



- **Colecciones**  
  Se trata de un grupo de archivos, donde cada uno puede incluir información en diferentes tipos de valores, como números, cadenas de caracteres, listas, objetos y enlaces a otros documentos. Si lo comparamos con una base de datos relacional, estaríamos hablando de las tablas.
- **Documentos**  
  Son cada uno de los datos estructurados que se guardan dentro de las colecciones. Estos representan los datos a guardar. Si los comparamos con una base de datos relacional estaríamos hablando de los registros de las tablas



Para este ejemplo nos basaremos en una pantalla con un formulario para poder introducir datos como nombre, description, prioridad y responsable.



```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".CreateActivity">

    <?xml version="1.0" encoding="utf-8"?>
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical"
        android:padding="16dp">

        <EditText
            android:id="@+id/nombre"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Nombre de la tarea"
            android:inputType="text" />

        <EditText
            android:id="@+id/descripcion"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Descripción"
            android:inputType="textMultiLine" />

        <Spinner
            android:entries="@array/prioridad"
            android:id="@+id/prioridad"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Prioridad" />

        <EditText
            android:id="@+id/responsable"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:hint="Responsable"
            android:inputType="text" />

        <Button
            android:id="@+id/btn_guardar"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Guardar"
            android:layout_gravity="center_horizontal" />

    </LinearLayout>


</androidx.constraintlayout.widget.ConstraintLayout>
```



Antes de empezar con la funcionalidad, será necesario además de activar el servicio dentro de Android Studio, será necesario tener una variable de tipo Firestore.



```kotlin
class CreateActivity : AppCompatActivity() {

    private lateinit var binding: ActivityCreateBinding
    private lateinit var firestore: FirebaseFirestore
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityCreateBinding.inflate(layoutInflater)
        setContentView(binding.root)
        firestore = FirebaseFirestore.getInstance()
    }
}
```



Con esto hecho, podemos proceder a la creación de colecciones y documentos.



```kotlin
binding.btnGuardar.setOnClickListener {
    firestore.collection("tareas").add(
        Tarea(
            binding.nombre.text.toString(),
            binding.descripcion.text.toString(),
            binding.prioridad.selectedItem.toString(),
            binding.responsable.text.toString()
        )
    ).addOnSuccessListener {
        Snackbar.make(binding.root, "Datos guardados correctos", Snackbar.LENGTH_SHORT).show()
    } .addOnFailureListener {
        Snackbar.make(binding.root, "Ha ocurrido un error en el proceso", Snackbar.LENGTH_SHORT).show()
    }
}
```



Como se puede ver en el código, se utiliza el método collection para acceder a la colección (en el caso de que la colección no esté creada el sistema la creará de forma automática y en el caso en el que la colección ya esté creada, simplemente actualizará los datos que están incluidos en ella), utilizando el método add para poder agregar un documento. Como parámetro es necesario pasar el objeto que se quiere guardar en la colección, mapeándose este con clave – valor, siendo la clave el nombre de la propiedad. Al igual que pasa con la autenticación, es posible analizar el resultado de la ejecución, para poder así actuar de manera concreta. El resultado en la base de datos de la ejecución anterior será el siguiente



![image](assets/cm6xwxpa6033u356zsoimc1w7-Imagen22.jpg)



En el caso de querer obtener datos, es necesario ejecutar el método get sobre la colección que se quiera consultar:



```kotlin
firestore.collection("tareas").get().addOnSuccessListener {
    val lista:  List<DocumentSnapshot> =  it.documents
    for (i in lista){
        val tarea = i.toObject(Tarea::class.java)
        Log.v("doc", tarea?.nombre.toString())
    }
}
```



Después de ejecutar el método get, es necesario evaluar el resultado. Este es la consulta completa de la colección, pero en realidad lo que nos interesa del resultado es el conjunto de documentos que está dentro de la colección. Para poder obtenerlos, se ejecuta el método documents del resultado, obteniendo la lista de estos. Lo normal en este punto es que nos interese tratar dichos documentos como objetos de kotlin, no como un simple JSON. Para ello podemos recorrer la lista obtenida y convertir cada uno de los documentos en objetos mediante el método toObject. Una cosa muy importante para que esta tarea tenga éxito es que el modelo tenga un constructor vacío, ya que, si no sería imposible hacer la conversión de objeto JSON a objeto Kotlin, al igual que la implementación de la interfaz serializable. Este constructor vació se puede poner en el constructor primario del objeto indicando la posibilidad de null o primitivo en todas las variables:



```kotlin
class Tarea(
    var nombre: String?=null,
    var descripcion: String?=null,
    var prioridad: String?=null,
    var responsable: String?=null
) : Serializable
```



En el caso de querer actualizar los datos, tan solo habría que realizar tareas de actualización o borrado, lo que tendríamos que hacer es utilizar los métodos update o delete indicando la key asociada al documento sobre el que queremos actuar. En el caso del ejemplo anterior, el tag del documento es howPrzaonMmNSd3Hj63l , por lo que el código para las tareas de actualización y borrado sería el siguiente:



```lua
firestore.collection("tareas").document("howPrzaonMmNSd3Hj63l")
    .update("Prioridad", "Baja")

firestore.collection("tareas").document("howPrzaonMmNSd3Hj63l")
    .delete()
```



Según lo que se ha explicado, en el caso de querer guardar en la base de datos información de los usuarios, lo que sería recomendable es tener una colección llamada usuarios donde cada documento tuviese el id del usuario (recordamos que lo otorga firebase), donde dentro del documento tendremos toda la información de esta. De la misma forma, en el caso de querer relacionar documentos con otros elementos de otra colección, podríamos utilizar el tag del documento para poder hacer la relación.



### 4.3 Consultas a API



Otra de los métodos de trabajo con almacenamiento en base de datos, es utilizar un servicio web al que conectarse mediante HTTP y que ejecute tareas sobre la base de datos. Esta metodología utiliza el conocido como modelo de tres capas, donde un servidor web intermedio actúa como gestor de las peticiones y es el que se pone en contacto con la base de datos, para como último paso responder con los datos pedidos.



![image](assets/cm6xx6c5g03ae356z33x87v4f-Imagen23.jpg)



Los pasos que se siguen en este tipo de servicios son los siguientes:

1. Se realiza una petición desde la aplicación Android hacia el servidor. Para ello se utiliza el protocolo HTTP utilizando un HTTPConexion o una librería de gestión de peticiones. En nuestro caso utilizaremos la librería Volley
2. Una vez el servidor recibe la petición, analiza el endpoint y ejecuta el código necesario para realizar las tareas correspondientes contra la base de datos.
3. Una vez la base de datos ha realizado las tareas correspondientes contesta al servidor web con los datos generados – borrados – actualizados
4. El servidor web transforma estos datos en comprensibles para la aplicación y se los devuelve en formato JSON para que sean interpretados por la misma

Antes de empezar a codificar, es necesario incorporar la dependencia de Volley para que se puedan resolver las peticiones de forma correcta. Para ello tendremos que incorporar la siguiente dependencia dentro del fichero build.gradle



```ini
    Implementation(“com.android.volley:volley:1.2.1”)
```



Una vez la librería está implementada, podemos pasar a la creación de peticiones. Para el ejemplo, vamos a utilizar un API ya creada que muestra datos fake de usuarios. Este api es [http://dummyjson.com/users](http://dummyjson.com/users) donde el documento muestra un objeto que contiene un array de usuarios. Para poder realizar las interpretaciones de forma correcta hay que tener un par de cosas en cuenta:

- Aquellos elementos que empiecen por llave ( { ) serán JSONObjecto
- Aquellos elementos que empiecen por corchete ( [ ) serán JSONArrays
- Los datos de los JSONObects están estructurados mediante par clave – valor
- Los datos de los JSONArray están estructurados mediante posiciones
- Al realizar peticiones a través de internet, es necesario que nuestra aplicación tenga acceso (que es diferente a que el teléfono lo tenga). Para poder dar estos permisos, dentro del fichero AndroidManifest, incorporaremos la siguiente declaración:



```ini
<uses-permission android:name="android.permission.INTERNET"/>
```



Con estos aspectos claros podemos empezar con las peticiones. Éstas tienen dos partes:



1. **Crear la petición mediante un objeto de tipo Request.** Dependiendo de cuál sea la contestación lo podremos tipar como JSONRequest o ArrayRequest. En esta petición habrá que indicar la url de conexión, la función a ejecutar en caso de respuesta correcta y la función a ejecutar en el caso de que error en la petición por cualquier motivo



```kotlin
class ApiActivity : AppCompatActivity() {

    private lateinit var binding: ActivityApiBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityApiBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val peticion: JsonObjectRequest = JsonObjectRequest("https://dummyjson.com/users", {
            procesarPeticion(it)
        }, {
            Snackbar.make(binding.root, "Algo ha fallado!", Snackbar.LENGTH_SHORT).show()
        })
    }

    private fun procesarPeticion(result: JSONObject) {
        val usuarios = result.getJSONArray("users")
        for (i in 0..usuarios.length() - 1) {
            val user: JSONObject = usuarios.getJSONObject(i)
            // para sacar los datos que se necesiten se realiza mediante referencia al tag
            val name = user.getString("username")
            val surname = user.getString("email")
        }
    }
}
```



Como se puede ver, los datos quedan recogidos mediante una petición clave valor, obteniendo el dato asociado a la clave pasada. Al igual que pasaba cuando se explicó firebase, es posible hacer una conversión directa de JSONObject a objeto kotlin, pero para lo cual necesitamos

- Una librería que realice dicho trabajo, como por ejemplo GSON
- Que el modelo cuente con un constructor vacío
- Que el modelo tenga como nombre de las variables exactamente el mismo que tienen los tags del API



2. El último paso antes de obtener los datos es lanzar la petición. Con el punto anterior lo que se ha configurado es como se recepcionan los datos y como se interpretan, pero no se ha lanzado petición alguna. Para ello tendremos que ejecutar el siguiente código.



```ini
Volley.newRequestQueue(applicationContext).add(peticion)
```



Una vez ejecutado esto, ahora si los datos ya están disponibles dentro de la aplicación. Hay que tener en cuenta que las peticiones no se pueden resolver todas al mismo tiempo, ya que producirían un posible cuello de botella. Para poder solventar eso, Android tiene las llamadas corrutinas, que permiten ejecutar código asíncrono. Sin embargo estas no son obligatorias con librerías como Volley ya que incorporar un mecanismo que permite la ejecución de las peticiones al mismo tiempo que se ejecutan en resto de elementos de la aplicación, además de procesar las peticiones en forma de cola sin que estas puedan saturar la conexión.



## 5. Conclusiones



### 5.1 Conclusiones de la unidad



En esta unidad se han vistos elementos avanzados, destacando entre ellos los recyclerview. No podemos imaginar una aplicación que no tenga listado de datos para la representación de estos. Este elemento permite gestionarlos y mostrarlos en una lista de la manera más eficiente posible, facilitando así la ejecución de la aplicación.

En cuanto a formas de trabajar los elementos de la UI, existen dos principalmente dos posibilidades: la tradicional de gestión y trabajo de Activitys simples o el trabajo con elementos avanzados como son los fragments. Estos facilitan la posibilidad de visualizar una aplicación de diferentes formas, dependiendo de múltiples aspectos como el tamaño de la pantalla, disposición del dispositivo, etc. sin necesidad de hacer un código muy pasado.

Otro de los aspectos que se han visto en esta unidad y tienen una importancia vital en el desarrollo de aplicaciones es la gestión de los datos. No existe una aplicación completa si los datos que manejan no son persistentes o al menos hay alguna manera de gestionarlos. Es aquí donde entra la necesidad de introducir un sistema que permita el manejo de estos, siendo las posibilidades bases de datos locales o distribuidas. Por su uso y características, las bases de datos distribuidas ofrecen características que se adaptan mucho mejor a las aplicaciones en entornos reales, pudiendo compartir datos en tiempo real. Firebase es una magnifica opción para este tipo de base de datos, ya que no solo ofrece servicio de base de datos no relacional, sino que ofrece un conjunto de servicios backend de muy fácil implementación que hacen que las aplicaciones puedan agregar funcionalidad clave para su implementación en un entorno real.
