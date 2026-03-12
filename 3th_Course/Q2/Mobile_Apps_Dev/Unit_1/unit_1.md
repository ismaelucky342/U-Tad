# Unidad 1 — Base del desarrollo móvil con Android

## Introducción y objetivos

Esta unidad cubre los fundamentos del desarrollo de aplicaciones móviles con Android. Vengo de tener algo de experiencia con Java y Kotlin básico, así que la parte del lenguaje no me resulta completamente nueva, pero todo lo específico de Android (ciclo de vida, intents, recursos) sí es terreno nuevo.

Los objetivos principales de la unidad son:

- Entender el ecosistema Android y por qué es relevante hoy
- Saber configurar el entorno de desarrollo desde cero
- Conocer la estructura de un proyecto Android y qué hace cada carpeta
- Manejar Activitys, eventos e intents
- Gestionar el ciclo de vida de una Activity correctamente
- Depurar una app de forma efectiva

---

## Impacto de los teléfonos móviles en la sociedad

### Introducción

Los teléfonos móviles han pasado de ser un dispositivo de comunicación a convertirse en el punto de acceso principal a internet para la mayoría de personas. Esto cambia completamente el enfoque del desarrollo de software: ya no se diseña primero para escritorio y luego se adapta al móvil, sino al revés.

### El teléfono móvil y la sociedad

Algunos datos relevantes para entender el contexto:

- Más del 60% del tráfico web global viene de dispositivos móviles
- Hay más de 6.000 millones de usuarios de smartphones en el mundo
- En países en desarrollo, el móvil es frecuentemente el único dispositivo con acceso a internet (mobile-first societies)
- Las apps dominan frente al navegador móvil: los usuarios pasan ~90% del tiempo en apps y solo ~10% en el browser

Esto tiene implicaciones directas en cómo diseñamos:

- **UX primero**: la pantalla pequeña obliga a priorizar. No todo cabe, hay que decidir qué es lo importante.
- **Conectividad variable**: una app tiene que funcionar bien en 5G pero también degradar bien con 3G lento o sin conexión.
- **Batería y recursos limitados**: el procesamiento excesivo en background mata la batería y el sistema operativo puede matar la app.
- **Interrupciones constantes**: llamadas, notificaciones, cambio de app. El ciclo de vida de una app móvil es mucho más complejo que el de una app de escritorio.

### Opciones de desarrollo móvil

Hay cuatro enfoques principales para desarrollar apps móviles. Cada uno tiene su sitio:

| Tipo | Tecnología | Ventajas | Desventajas |
| --- | --- | --- | --- |
| **Nativo Android** | Kotlin / Java | Máximo rendimiento, acceso completo a APIs del SO | Solo Android |
| **Nativo iOS** | Swift / Objective-C | Máximo rendimiento en iPhone | Solo iOS |
| **Multiplataforma** | Flutter (Dart), React Native (JS), KMP | Un solo código para Android e iOS | Rendimiento algo menor, limitaciones de APIs nativas |
| **Web progresiva (PWA)** | HTML/CSS/JS | Un solo código, sin tienda | Acceso limitado a hardware, experiencia menos nativa |

En esta asignatura trabajamos con **desarrollo nativo Android en Kotlin**. La razón de elegir nativo frente a multiplataforma es que entender bien el modelo de Android es la base para todo lo demás; si luego quieres usar Flutter o React Native, entender el ciclo de vida y el modelo de permisos te ayuda igualmente.

La elección en proyectos reales depende de varios factores: presupuesto, si la empresa ya tiene equipo en una tecnología, si la app necesita acceso intensivo a hardware (cámara, Bluetooth, sensores), o si el rendimiento gráfico es crítico.

---

## Android

### Introducción

Android es el sistema operativo móvil más usado del mundo, con más del 70% de cuota de mercado global. Es desarrollado por Google pero basado en Linux y publicado como código abierto (AOSP — Android Open Source Project). Esto permite que fabricantes como Samsung, Xiaomi o Huawei lo modifiquen y pongan su propia capa encima.

### Historia

| Año | Versión | Nombre clave | API Level | Novedades destacadas |
| --- | --- | --- | --- | --- |
| 2008 | 1.0 | — | 1 | Primera versión pública |
| 2009 | 1.5 | Cupcake | 3 | Teclado virtual, widgets |
| 2010 | 2.2 | Froyo | 8 | JIT compiler, hotspot WiFi |
| 2011 | 3.0 | Honeycomb | 11 | Primera versión para tablets |
| 2011 | 4.0 | Ice Cream Sandwich | 14 | Unificación teléfono/tablet |
| 2014 | 5.0 | Lollipop | 21 | Material Design, ART runtime |
| 2015 | 6.0 | Marshmallow | 23 | Permisos en tiempo de ejecución |
| 2017 | 8.0 | Oreo | 26 | Notificaciones en canales, Autofill |
| 2019 | 10 | (sin nombre) | 29 | Modo oscuro, permisos de localización en background |
| 2021 | 12 | — | 31 | Material You, mejoras de privacidad |
| 2023 | 14 | — | 34 | Predictive back, mejoras de privacidad de fotos |
| 2024 | 15 | — | 35 | Edge-to-edge forzado, más controles de privacidad |

El cambio más importante a nivel de desarrollo fue el paso de Dalvik a **ART** (Android Runtime) en Lollipop: en lugar de compilar el bytecode en tiempo de ejecución cada vez (JIT), ART lo compila al instalar la app (AOT), lo que mejora significativamente el rendimiento.

El otro cambio grande fue el **API Level 23 (Marshmallow)**: antes de esa versión, los permisos se concedían todos en la instalación. A partir de Marshmallow hay que pedirlos en tiempo de ejecución, lo que cambia bastante cómo se escribe el código.

### El sistema operativo

La arquitectura de Android tiene varias capas:

```
┌─────────────────────────────────────────────────────┐
│                   Aplicaciones                       │
│         (las nuestras + apps del sistema)            │
├─────────────────────────────────────────────────────┤
│              Framework de aplicaciones               │
│  Activity Manager, Content Providers, View System    │
├─────────────────────────────────────────────────────┤
│           Librerías nativas + Android Runtime        │
│     SQLite, OpenGL, WebKit, ART, bibliotecas C/C++   │
├─────────────────────────────────────────────────────┤
│                   Kernel Linux                       │
│       Drivers, gestión de memoria, procesos          │
└─────────────────────────────────────────────────────┘
```

Lo relevante para nosotros como desarrolladores es el **Framework de aplicaciones**, que es la capa con la que interactuamos directamente:

- **Activity Manager**: gestiona el ciclo de vida de las Activities y la pila de navegación
- **Content Providers**: mecanismo para compartir datos entre aplicaciones de forma controlada
- **View System**: el sistema de rendering de la interfaz gráfica
- **Notification Manager**: gestión de notificaciones
- **Package Manager**: instalación y desinstalación de apps, información sobre paquetes instalados

Cada app Android corre en su propio **proceso Linux aislado** con su propio espacio de memoria. Esto significa que dos apps no pueden acceder directamente a los datos de la otra; para comunicarse, tienen que usar mecanismos controlados como Intents o Content Providers.

### Instalación y configuración del IDE

El entorno de desarrollo estándar para Android es **Android Studio**, basado en IntelliJ IDEA.

**Instalación:**

1. Descargar desde developer.android.com/studio
2. Instalar el SDK de Android (Android Studio lo hace automáticamente en el primer lanzamiento)
3. Configurar un emulador o conectar un dispositivo físico

**Configuración del emulador (AVD — Android Virtual Device):**

- En Android Studio: Tools > Device Manager > Create Device
- Elegir un dispositivo de referencia (por ejemplo Pixel 6)
- Elegir la API Level (recomendado: la última estable con Google APIs)
- Para que el emulador sea rápido, activar la aceleración por hardware (HAXM en Intel, Hyper-V en AMD/Windows)

**Para usar un dispositivo físico:**

1. En el teléfono: Ajustes > Acerca del teléfono > pulsar 7 veces en "Número de compilación" para activar las opciones de desarrollador
2. Ajustes > Opciones de desarrollador > Depuración USB activada
3. Conectar por USB y aceptar el diálogo de autorización

**Estructura del SDK:**

El SDK se instala en ~/Android/Sdk (Linux/Mac) o C:\Users\[usuario]\AppData\Local\Android\Sdk (Windows). Dentro hay varias carpetas clave:

- platforms/: los JARs de cada API Level
- platform-tools/: adb, fastboot
- tools/: utilidades varias
- emulator/: el binario del emulador

**ADB (Android Debug Bridge)** es la herramienta de línea de comandos para interactuar con dispositivos:

```bash
adb devices                        # listar dispositivos conectados
adb install app-debug.apk          # instalar un APK
adb logcat                         # ver los logs en tiempo real
adb shell                          # abrir una shell en el dispositivo
adb pull /sdcard/fichero.txt .     # copiar un fichero del dispositivo al PC
```

### Conceptos básicos del desarrollo Android

Antes de escribir código hay que entender los bloques fundamentales de una app Android:

**Componentes de una app Android:**

Una app no es un ejecutable con un main() como en Java. Está compuesta de componentes que el sistema instancia según necesite:

- **Activity**: una pantalla con interfaz de usuario. Es el componente más común.
- **Fragment**: un trozo de interfaz reutilizable que vive dentro de una Activity.
- **Service**: proceso en background sin interfaz (sincronización, música, etc.).
- **BroadcastReceiver**: escucha eventos del sistema (batería baja, conexión a WiFi, etc.).
- **ContentProvider**: expone datos de la app a otras apps de forma controlada.

**AndroidManifest.xml:**

Es el fichero de declaración de la app. Cada componente que uses tiene que estar registrado aquí, junto con los permisos que la app necesita:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.ejemplo.miapp">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.CAMERA" />

    <application
        android:label="@string/app_name"
        android:icon="@mipmap/ic_launcher">

        <activity android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>
</manifest>
```

El intent-filter con MAIN y LAUNCHER indica que esta Activity es el punto de entrada de la app (la que aparece al pulsar el icono).

**Gradle:**

Android usa Gradle como sistema de construcción. Hay dos ficheros build.gradle:

- El de nivel de proyecto: configuración global, repositorios
- El de nivel de módulo (app/build.gradle): dependencias, versión de SDK, configuración de la app

```kotlin
// app/build.gradle.kts
android {
    compileSdk = 35
    defaultConfig {
        applicationId = "com.ejemplo.miapp"
        minSdk = 24          // versión mínima de Android que soportamos
        targetSdk = 35       // versión para la que optimizamos
        versionCode = 1
        versionName = "1.0"
    }
}

dependencies {
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("com.google.android.material:material:1.12.0")
}
```

minSdk define hasta qué versiones antiguas de Android soportamos. Subir minSdk significa menos código de compatibilidad; bajarlo significa más usuarios potenciales pero más trabajo.

### Estructura de un proyecto Android

Al crear un proyecto nuevo en Android Studio, la estructura que genera es:

```
MiApp/
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/ejemplo/miapp/
│   │   │   │   └── MainActivity.kt         ← código Kotlin
│   │   │   ├── res/
│   │   │   │   ├── layout/
│   │   │   │   │   └── activity_main.xml   ← interfaz de la Activity
│   │   │   │   ├── values/
│   │   │   │   │   ├── strings.xml         ← textos de la app
│   │   │   │   │   ├── colors.xml          ← colores
│   │   │   │   │   └── themes.xml          ← estilos visuales
│   │   │   │   ├── drawable/               ← imágenes vectoriales y bitmaps
│   │   │   │   └── mipmap/                 ← iconos de la app (varias densidades)
│   │   │   └── AndroidManifest.xml
│   │   └── test/ / androidTest/            ← tests unitarios / instrumentados
│   └── build.gradle.kts
├── build.gradle.kts
└── settings.gradle.kts
```

**La carpeta res/ merece explicación detallada:**

Android gestiona los recursos de forma que la misma app puede adaptarse automáticamente a distintos idiomas, tamaños de pantalla y densidades de píxeles. Para eso usa calificadores en los nombres de carpeta:

```
res/
├── layout/                    ← layout por defecto
├── layout-land/               ← layout en horizontal
├── layout-sw600dp/            ← layout para tablets (ancho mínimo 600dp)
├── values/                    ← strings, colores, etc. por defecto
├── values-es/                 ← strings en español
├── values-en/                 ← strings en inglés
├── drawable-mdpi/             ← imágenes para pantallas de densidad media
├── drawable-hdpi/             ← imágenes para alta densidad
├── drawable-xhdpi/            ← extra alta densidad
└── drawable-xxhdpi/           ← densidad muy alta (la mayoría de móviles actuales)
```

El sistema elige automáticamente el recurso más adecuado según el dispositivo. Si el usuario tiene el móvil en español, carga strings de values-es/; si no existe, cae al values/ por defecto. Lo mismo con las densidades.

**Los recursos se referencian con R:**

En código Kotlin se accede a los recursos a través de la clase R generada automáticamente:

```kotlin
R.string.app_name         // referencia al string "app_name" de strings.xml
R.layout.activity_main    // referencia al layout activity_main.xml
R.drawable.icono          // referencia a una imagen
R.color.azul_primario     // referencia a un color
```

En XML se usa la sintaxis @tipo/nombre:

```xml
android:text="@string/app_name"
android:background="@color/azul_primario"
android:src="@drawable/icono"
```

### Kotlin

Kotlin es el lenguaje oficial para Android desde 2017. Es conciso, seguro en cuanto a nulos y 100% interoperable con Java.

**Puntos clave de Kotlin para Android:**

**Variables y tipos:**

```kotlin
val nombre: String = "Android"    // inmutable
var contador: Int = 0              // mutable
val inferido = "Kotlin"            // el compilador infiere el tipo

// null safety: por defecto ninguna variable puede ser null
var normal: String = "texto"
// normal = null  // error de compilación

var nullable: String? = null       // ? indica que puede ser null
val longitud = nullable?.length    // safe call: devuelve null si nullable es null
val len = nullable?.length ?: 0    // Elvis: si null, usa 0
```

**Clases y data classes:**

```kotlin
// clase normal
class Persona(val nombre: String, var edad: Int) {
    fun saludar() = "Hola, soy $nombre"
}

// data class: equals, hashCode, toString y copy generados automáticamente
data class Usuario(val id: Int, val email: String, val nombre: String)

val u1 = Usuario(1, "ana@mail.com", "Ana")
val u2 = u1.copy(nombre = "Ana García")
```

**Extensiones:**

Una de las características más útiles de Kotlin. Permite añadir funciones a clases existentes sin herencia:

```kotlin
fun String.esPalindromo(): Boolean = this == this.reversed()
fun Int.esPar(): Boolean = this % 2 == 0

"radar".esPalindromo()   // true
4.esPar()                 // true
```

En Android esto es especialmente útil porque muchas librerías de extensiones de Kotlin para Android (KTX) amplían las clases de Android con métodos más convenientes.

**Lambdas y funciones de orden superior:**

```kotlin
val numeros = listOf(1, 2, 3, 4, 5)
val pares = numeros.filter { it % 2 == 0 }
val dobles = numeros.map { it * 2 }
val suma = numeros.reduce { acc, n -> acc + n }

// Con funciones como parámetro
fun operar(a: Int, b: Int, f: (Int, Int) -> Int): Int = f(a, b)
operar(3, 4) { x, y -> x + y }   // 7
```

**Corrutinas (introducción):**

Las corrutinas son la forma idiomática en Kotlin de manejar trabajo asíncrono. En Android se usan para todo lo que no debe bloquear el hilo principal: llamadas de red, acceso a base de datos, operaciones de fichero.

```kotlin
// Sin corrutinas (bloqueante, no hacer en Android):
val datos = llamadaDeRed()  // bloquea el hilo principal, congela la UI

// Con corrutinas:
lifecycleScope.launch {
    val datos = withContext(Dispatchers.IO) { llamadaDeRed() }
    // aquí ya estamos de nuevo en el hilo principal
    actualizarUI(datos)
}
```

Se verán en profundidad en unidades posteriores.

---

## Desarrollo Android

### Introducción

Esta es la parte práctica. Una Activity es la unidad básica de interfaz en Android, y entender su ciclo de vida es fundamental para no tener bugs extraños (datos que desaparecen al rotar el móvil, operaciones que se duplican, fugas de memoria).

### Activitys

Una Activity representa una pantalla de la app. Toda Activity:

1. Extiende la clase AppCompatActivity (o Activity directamente)
2. Tiene un layout XML asociado que define su interfaz
3. Overridea el método onCreate() como mínimo

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // a partir de aquí podemos acceder a las vistas y configurar la Activity
        val texto = findViewById<TextView>(R.id.miTexto)
        texto.text = "Hola Android"
    }
}
```

**Ciclo de vida de una Activity:**

Este es el concepto más importante de Android. El sistema operativo puede destruir y recrear una Activity en cualquier momento (al rotar el móvil, cuando necesita memoria, cuando el usuario cambia de app). Si no gestionamos esto bien, perdemos datos.

```
          ┌──────────────────────────────────────────┐
          │               onCreate()                  │  ← se llama al crear la Activity
          │    (inflar layout, inicializar vistas)    │
          └──────────────────┬───────────────────────┘
                             ↓
          ┌──────────────────────────────────────────┐
          │               onStart()                   │  ← la Activity es visible
          └──────────────────┬───────────────────────┘
                             ↓
          ┌──────────────────────────────────────────┐
          │               onResume()                  │  ← la Activity está en primer plano
          │         (aquí la app interactúa)          │  ← estado RUNNING
          └──────────────────┬───────────────────────┘
                             ↓ (el usuario abre otra app)
          ┌──────────────────────────────────────────┐
          │               onPause()                   │  ← parcialmente visible (multitarea)
          │        (guardar cambios no guardados)     │
          └──────────────────┬───────────────────────┘
                             ↓ (completamente tapada)
          ┌──────────────────────────────────────────┐
          │               onStop()                    │  ← no visible
          │       (liberar recursos pesados)          │
          └──────────────────┬───────────────────────┘
                             ↓ (el sistema necesita memoria)
          ┌──────────────────────────────────────────┐
          │               onDestroy()                 │  ← se va a destruir
          └──────────────────────────────────────────┘
```

Si el usuario vuelve a la app: onRestart() → onStart() → onResume()

**Cuándo usar cada callback:**

- onCreate(): inflar el layout, inicializar vistas, restaurar estado guardado, observar LiveData
- onStart(): registrar listeners que necesitan estar activos mientras la Activity es visible
- onResume(): reanudar animaciones, iniciar la cámara, registrar sensores
- onPause(): pausar animaciones, guardar cambios pendientes que no pueden esperar, liberar la cámara
- onStop(): guardar datos persistentes, liberar recursos que gastan batería
- onDestroy(): limpiar todo lo que quede (aunque si usamos ViewModel esto raramente es necesario)

**Guardar y restaurar estado:**

Si el usuario rota el móvil, Android destruye y recrea la Activity. Los datos en variables se pierden. Para conservarlos:

```kotlin
// Guardar estado antes de destruirse
override fun onSaveInstanceState(outState: Bundle) {
    super.onSaveInstanceState(outState)
    outState.putString("CLAVE_TEXTO", miEditText.text.toString())
    outState.putInt("CLAVE_CONTADOR", contador)
}

// Restaurar en onCreate
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)

    if (savedInstanceState != null) {
        val texto = savedInstanceState.getString("CLAVE_TEXTO", "")
        val cont = savedInstanceState.getInt("CLAVE_CONTADOR", 0)
        miEditText.setText(texto)
        contador = cont
    }
}
```

La forma más moderna de evitar esto es usar **ViewModel**, que sobrevive a las rotaciones:

```kotlin
class ContadorViewModel : ViewModel() {
    var contador: Int = 0
}

// En la Activity:
val viewModel: ContadorViewModel by viewModels()
// viewModel.contador sobrevive a la rotación
```

### Eventos

Los eventos son las interacciones del usuario con la interfaz: pulsar un botón, escribir texto, hacer scroll, etc.

**Click en un botón:**

```kotlin
// Forma 1: listener anónimo
val boton = findViewById<Button>(R.id.miBoton)
boton.setOnClickListener {
    Toast.makeText(this, "Pulsado", Toast.LENGTH_SHORT).show()
}

// Forma 2: View Binding (preferido, más seguro)
// (requiere activar viewBinding en build.gradle)
binding.miBoton.setOnClickListener {
    Toast.makeText(this, "Pulsado", Toast.LENGTH_SHORT).show()
}
```

**View Binding:**

Activar en build.gradle:

```kotlin
android {
    buildFeatures {
        viewBinding = true
    }
}
```

Usar en la Activity:

```kotlin
class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // acceso a vistas sin findViewById, con tipo seguro
        binding.miBoton.setOnClickListener { /* ... */ }
        binding.miTexto.text = "Hola"
    }
}
```

Con View Binding el compilador genera una clase por cada fichero XML. Si renombras una vista en el XML, el código Kotlin falla en compilación, no en runtime. Es mucho más seguro que findViewById.

**Eventos de texto:**

```kotlin
binding.miEditText.addTextChangedListener { texto ->
    binding.contador.text = "Caracteres: ${texto?.length ?: 0}"
}
```

**Eventos táctiles:**

```kotlin
binding.miVista.setOnTouchListener { view, motionEvent ->
    when (motionEvent.action) {
        MotionEvent.ACTION_DOWN -> { /* dedo baja */ true }
        MotionEvent.ACTION_UP   -> { /* dedo sube */ true }
        MotionEvent.ACTION_MOVE -> { /* dedo se mueve */ true }
        else -> false
    }
}
```

**Long click:**

```kotlin
binding.miBoton.setOnLongClickListener {
    Toast.makeText(this, "Pulsación larga", Toast.LENGTH_SHORT).show()
    true  // true indica que el evento fue consumido
}
```

### Gestión de estados

La gestión de estados en Android tiene varias capas. El problema central es que una Activity puede destruirse y recrearse, y hay que distinguir entre:

- **Estado de instancia** (instanceState): datos de la UI que queremos recuperar si el sistema destruye la Activity temporalmente. Se guarda en onSaveInstanceState y se restaura en onCreate.
- **Estado persistente**: datos que deben sobrevivir aunque el usuario cierre la app. Se guardan en SharedPreferences, base de datos o ficheros.

**SharedPreferences** — para configuraciones simples:

```kotlin
// Guardar
val prefs = getSharedPreferences("mis_prefs", Context.MODE_PRIVATE)
prefs.edit() {
    putString("nombre_usuario", "Ana")
    putBoolean("modo_oscuro", true)
    putInt("puntuacion", 1500)
}

// Leer
val nombre = prefs.getString("nombre_usuario", "")     // segundo param: valor por defecto
val oscuro = prefs.getBoolean("modo_oscuro", false)
```

**ViewModel + LiveData** — para estado de UI:

```kotlin
class MainViewModel : ViewModel() {
    private val _contador = MutableLiveData(0)
    val contador: LiveData<Int> = _contador  // solo lectura desde fuera

    fun incrementar() {
        _contador.value = (_contador.value ?: 0) + 1
    }
}

// En la Activity:
val vm: MainViewModel by viewModels()

vm.contador.observe(this) { valor ->
    binding.textoContador.text = valor.toString()
}

binding.botonSumar.setOnClickListener {
    vm.incrementar()
}
```

LiveData solo actualiza la UI cuando la Activity está en estado activo (después de onStart). Esto evita crashes por intentar actualizar una Activity que ya no existe.

### Internacionalización y uso de recursos múltiples

Android tiene soporte nativo para internacionalización sin necesidad de librerías externas.

**Strings localizadas:**

```
res/
├── values/strings.xml          ← idioma por defecto (si no se encuentra el del dispositivo)
├── values-es/strings.xml       ← español
├── values-en/strings.xml       ← inglés
└── values-fr/strings.xml       ← francés
```

```xml
<!-- res/values/strings.xml -->
<resources>
    <string name="app_name">MyApp</string>
    <string name="boton_aceptar">Accept</string>
    <string name="mensaje_error">An error occurred</string>
    <string name="bienvenida">Hello, %1$s!</string>  <!-- con parámetro -->
</resources>

<!-- res/values-es/strings.xml -->
<resources>
    <string name="boton_aceptar">Aceptar</string>
    <string name="mensaje_error">Ha ocurrido un error</string>
    <string name="bienvenida">¡Hola, %1$s!</string>
</resources>
```

Usar en código:

```kotlin
val texto = getString(R.string.boton_aceptar)
val bienvenida = getString(R.string.bienvenida, "Ana")  // reemplaza %1$s por "Ana"
```

**Layouts por orientación:**

```
res/
├── layout/activity_main.xml        ← vertical (portrait)
└── layout-land/activity_main.xml   ← horizontal (landscape)
```

Los IDs de las vistas tienen que coincidir en ambos layouts porque el código Kotlin es el mismo para los dos.

**Recursos para distintas densidades de pantalla:**

Android usa dp (density-independent pixels) para que los tamaños sean iguales visualmente en pantallas con distintas densidades:

| Densidad | Calificador | Escala |
| --- | --- | --- |
| ldpi | drawable-ldpi | 0.75x |
| mdpi | drawable-mdpi | 1x (referencia) |
| hdpi | drawable-hdpi | 1.5x |
| xhdpi | drawable-xhdpi | 2x |
| xxhdpi | drawable-xxhdpi | 3x |
| xxxhdpi | drawable-xxxhdpi | 4x |

Para evitar tener que crear la imagen en cada densidad, se pueden usar **vectores SVG** (Vector Drawables), que escalan sin perder calidad:

```xml
<!-- res/drawable/ic_flecha.xml -->
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="24"
    android:viewportHeight="24">
    <path android:pathData="M8,5v14l11,-7z"
          android:fillColor="#000000"/>
</vector>
```

**Night mode (tema oscuro):**

```
res/
├── values/themes.xml          ← tema claro
└── values-night/themes.xml    ← tema oscuro
```

```kotlin
// Forzar tema oscuro en código
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES)

// Seguir la configuración del sistema
AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_FOLLOW_SYSTEM)
```

### Intents

Los Intents son el sistema de mensajería de Android para comunicar componentes. Se usan para:

- Abrir otra Activity dentro de la misma app
- Abrir una Activity de otra app (el correo, la cámara, el navegador...)
- Pasar datos entre Activities
- Iniciar servicios y BroadcastReceivers

**Intent explícito** — cuando sabemos exactamente qué Activity queremos abrir:

```kotlin
// Abrir otra Activity
val intent = Intent(this, DetalleActivity::class.java)
startActivity(intent)

// Pasar datos con extras
val intent = Intent(this, DetalleActivity::class.java)
intent.putExtra("USUARIO_ID", 42)
intent.putExtra("NOMBRE", "Ana")
startActivity(intent)

// Recibir los datos en DetalleActivity
val id = intent.getIntExtra("USUARIO_ID", -1)
val nombre = intent.getStringExtra("NOMBRE") ?: ""
```

**Intent implícito** — cuando queremos que el sistema busque qué app puede hacer la acción:

```kotlin
// Abrir una URL en el navegador
val url = Uri.parse("https://developer.android.com")
val intent = Intent(Intent.ACTION_VIEW, url)
startActivity(intent)

// Enviar un email
val intent = Intent(Intent.ACTION_SENDTO).apply {
    data = Uri.parse("mailto:contacto@ejemplo.com")
    putExtra(Intent.EXTRA_SUBJECT, "Consulta")
    putExtra(Intent.EXTRA_TEXT, "Hola, ...")
}
startActivity(intent)

// Llamar por teléfono (requiere permiso CALL_PHONE)
val intent = Intent(Intent.ACTION_DIAL, Uri.parse("tel:+34600000000"))
startActivity(intent)

// Compartir texto con la hoja de contenido nativa
val intent = Intent(Intent.ACTION_SEND).apply {
    type = "text/plain"
    putExtra(Intent.EXTRA_TEXT, "Texto a compartir")
}
startActivity(Intent.createChooser(intent, "Compartir con..."))
```

**ActivityResultLauncher** — para recibir un resultado de otra Activity:

La forma antigua era startActivityForResult, que está deprecada. La forma actual usa ActivityResultLauncher:

```kotlin
// Registrar el launcher en la Activity (antes de onCreate)
private val abrirDetalle = registerForActivityResult(
    ActivityResultContracts.StartActivityForResult()
) { resultado ->
    if (resultado.resultCode == RESULT_OK) {
        val datos = resultado.data
        val texto = datos?.getStringExtra("RESPUESTA") ?: ""
        Toast.makeText(this, "Recibido: $texto", Toast.LENGTH_SHORT).show()
    }
}

// Lanzar la Activity
binding.botonAbrir.setOnClickListener {
    val intent = Intent(this, DetalleActivity::class.java)
    abrirDetalle.launch(intent)
}

// En DetalleActivity, devolver resultado
val resultIntent = Intent()
resultIntent.putExtra("RESPUESTA", "datos de vuelta")
setResult(RESULT_OK, resultIntent)
finish()
```

**Verificar antes de lanzar un intent implícito:**

Si no hay ninguna app instalada que pueda manejar el intent, startActivity lanza una excepción. Hay que verificar antes:

```kotlin
val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://ejemplo.com"))
if (intent.resolveActivity(packageManager) != null) {
    startActivity(intent)
} else {
    Toast.makeText(this, "No hay navegador instalado", Toast.LENGTH_SHORT).show()
}
```

### Depuración de código

Android Studio ofrece varias herramientas para depurar. Conocerlas bien ahorra mucho tiempo.

**Logcat:**

El sistema de logs de Android. Se usa para imprimir información de depuración:

```kotlin
import android.util.Log

val TAG = "MainActivity"

Log.d(TAG, "Mensaje de debug")          // DEBUG
Log.i(TAG, "Mensaje informativo")       // INFO
Log.w(TAG, "Advertencia")               // WARNING
Log.e(TAG, "Error crítico")             // ERROR
Log.e(TAG, "Error con excepción", e)    // ERROR + stack trace
```

En Logcat (panel inferior de Android Studio) se puede filtrar por tag, nivel y app. Siempre filtrar por la propia app para no ver el ruido del sistema.

**Debugger:**

Idéntico al de cualquier IDE basado en IntelliJ:

1. Poner breakpoints clicando en el margen izquierdo del editor
2. Ejecutar con el botón de bug (Shift+F9) en lugar del de play
3. Cuando la ejecución llega al breakpoint, pausar e inspeccionar variables
4. Step Over (F8): ejecutar la línea actual sin entrar en funciones
5. Step Into (F7): entrar en la función de la línea actual
6. Step Out (Shift+F8): salir de la función actual

**Breakpoints condicionales:**

Clic derecho en un breakpoint > Condición. El debugger solo para si la condición es verdadera:

```
contador > 10 && nombre.equals("error")
```

Útil cuando el bug solo ocurre en una iteración concreta de un bucle con 1000 iteraciones.

**Inspect Variables:**

Con la ejecución pausada, se puede:
- Pasar el ratón por encima de una variable para ver su valor
- En el panel Variables de la derecha, ver todo el estado actual
- En el panel Watches, escribir expresiones para evaluarlas en tiempo real

**Android Profiler:**

View > Tool Windows > Profiler. Muestra en tiempo real:

- **CPU**: qué métodos se están ejecutando y cuánto tiempo toman
- **Memory**: memoria usada, GC events, posibles memory leaks
- **Network**: solicitudes de red, tiempos, tamaños de respuesta
- **Energy**: consumo estimado de batería

**Análisis de memoria con Memory Profiler:**

Para detectar fugas de memoria: hacer snapshot de heap, buscar clases que tienen más instancias de las esperadas, ver quién retiene referencias a esas instancias.

**Error más común: NullPointerException:**

En Kotlin el compilador previene la mayoría de NPEs, pero en el boundary con Java (el propio SDK de Android está escrito en Java) pueden ocurrir. El stack trace en Logcat dice exactamente en qué línea fue:

```
FATAL EXCEPTION: main
Process: com.ejemplo.miapp, PID: 12345
java.lang.NullPointerException: Attempt to invoke virtual method 'void android.widget.Button.setOnClickListener' on a null object reference
    at com.ejemplo.miapp.MainActivity.onCreate(MainActivity.kt:25)
```

Significa que el botón que buscaste con findViewById es null, probablemente porque el ID no coincide con el del layout.

---

## Ejercicios prácticos

### Ejercicio 1 — Hola Mundo con eventos

Crear una app que tiene un campo de texto, un botón y un TextView. Al pulsar el botón, el texto del campo debe aparecer en el TextView con un saludo. Si el campo está vacío, mostrar un Toast de error.

```kotlin
class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.botonSaludar.setOnClickListener {
            val nombre = binding.campoNombre.text.toString().trim()
            if (nombre.isEmpty()) {
                Toast.makeText(this, "Escribe un nombre", Toast.LENGTH_SHORT).show()
            } else {
                binding.textoSaludo.text = "¡Hola, $nombre!"
            }
        }
    }
}
```

Layout (activity_main.xml):

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <EditText
        android:id="@+id/campoNombre"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Escribe tu nombre"
        android:inputType="textPersonName" />

    <Button
        android:id="@+id/botonSaludar"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Saludar"
        android:layout_marginTop="8dp" />

    <TextView
        android:id="@+id/textoSaludo"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp"
        android:textSize="20sp" />
</LinearLayout>
```

---

### Ejercicio 2 — Contador con ciclo de vida

App con un contador que se incrementa con un botón. El valor debe mantenerse al rotar el dispositivo.

Versión sin ViewModel (con onSaveInstanceState):

```kotlin
class ContadorActivity : AppCompatActivity() {
    private lateinit var binding: ActivityContadorBinding
    private var contador = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityContadorBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // restaurar estado si existía
        contador = savedInstanceState?.getInt("CONTADOR") ?: 0
        actualizarTexto()

        binding.botonSumar.setOnClickListener {
            contador++
            actualizarTexto()
        }

        binding.botonRestar.setOnClickListener {
            if (contador > 0) {
                contador--
                actualizarTexto()
            }
        }
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putInt("CONTADOR", contador)
    }

    private fun actualizarTexto() {
        binding.textoContador.text = contador.toString()
    }
}
```

Versión con ViewModel (más robusta):

```kotlin
class ContadorViewModel : ViewModel() {
    private val _valor = MutableLiveData(0)
    val valor: LiveData<Int> = _valor

    fun incrementar() { _valor.value = (_valor.value ?: 0) + 1 }
    fun decrementar() { if ((_valor.value ?: 0) > 0) _valor.value = (_valor.value ?: 0) - 1 }
}

class ContadorActivity : AppCompatActivity() {
    private lateinit var binding: ActivityContadorBinding
    private val vm: ContadorViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityContadorBinding.inflate(layoutInflater)
        setContentView(binding.root)

        vm.valor.observe(this) { valor ->
            binding.textoContador.text = valor.toString()
        }

        binding.botonSumar.setOnClickListener { vm.incrementar() }
        binding.botonRestar.setOnClickListener { vm.decrementar() }
    }
}
```

---

### Ejercicio 3 — Dos Activities con paso de datos

Crear una app con dos pantallas. En la primera hay un formulario (nombre y edad). Al pulsar un botón se abre la segunda pantalla mostrando un resumen con los datos introducidos. La segunda tiene un botón de volver.

Activity 1:

```kotlin
class FormularioActivity : AppCompatActivity() {
    private lateinit var binding: ActivityFormularioBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityFormularioBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.botonEnviar.setOnClickListener {
            val nombre = binding.campoNombre.text.toString().trim()
            val edadStr = binding.campoEdad.text.toString().trim()

            if (nombre.isEmpty() || edadStr.isEmpty()) {
                Toast.makeText(this, "Rellena todos los campos", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            val intent = Intent(this, ResumenActivity::class.java).apply {
                putExtra("NOMBRE", nombre)
                putExtra("EDAD", edadStr.toIntOrNull() ?: 0)
            }
            startActivity(intent)
        }
    }
}
```

Activity 2:

```kotlin
class ResumenActivity : AppCompatActivity() {
    private lateinit var binding: ActivityResumenBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityResumenBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val nombre = intent.getStringExtra("NOMBRE") ?: "Desconocido"
        val edad = intent.getIntExtra("EDAD", 0)

        binding.textoResumen.text = "Nombre: $nombre\nEdad: $edad años"

        binding.botonVolver.setOnClickListener {
            finish()  // cierra esta Activity y vuelve a la anterior
        }
    }
}
```

---

### Ejercicio 4 — Internacionalización

Crear una app que soporte inglés y español. El idioma cambia automáticamente según la configuración del sistema.

```
res/values/strings.xml:
<resources>
    <string name="app_name">My App</string>
    <string name="saludo">Hello!</string>
    <string name="instruccion">Enter your name below</string>
    <string name="boton_ok">OK</string>
</resources>

res/values-es/strings.xml:
<resources>
    <string name="saludo">¡Hola!</string>
    <string name="instruccion">Escribe tu nombre abajo</string>
    <string name="boton_ok">Aceptar</string>
</resources>
```

En el layout, referenciar siempre los strings del fichero en lugar de hardcodearlos:

```xml
<TextView
    android:text="@string/saludo"
    ... />
```

Para probar sin cambiar el idioma del sistema entero: en el emulador, Settings > System > Language y añadir un segundo idioma.

---

### Ejercicio 5 — Intent implícito: abrir URL y compartir

```kotlin
class IntentsActivity : AppCompatActivity() {
    private lateinit var binding: ActivityIntentsBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityIntentsBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.botonNavegador.setOnClickListener {
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
            if (intent.resolveActivity(packageManager) != null) {
                startActivity(intent)
            }
        }

        binding.botonCompartir.setOnClickListener {
            val intent = Intent(Intent.ACTION_SEND).apply {
                type = "text/plain"
                putExtra(Intent.EXTRA_TEXT, "Aprendiendo Android desde cero")
            }
            startActivity(Intent.createChooser(intent, "Compartir con..."))
        }

        binding.botonEmail.setOnClickListener {
            val intent = Intent(Intent.ACTION_SENDTO).apply {
                data = Uri.parse("mailto:profesor@universidad.es")
                putExtra(Intent.EXTRA_SUBJECT, "Duda de Android")
            }
            if (intent.resolveActivity(packageManager) != null) {
                startActivity(intent)
            } else {
                Toast.makeText(this, "No hay cliente de email instalado", Toast.LENGTH_SHORT).show()
            }
        }
    }
}
```

---

## Resumen y puntos clave

- Android es el SO móvil más usado. Las apps se componen de componentes (Activity, Service, etc.), no de un main().
- El ciclo de vida de una Activity es fundamental. Si no se gestiona bien, los datos se pierden al rotar o al volver de otra app.
- Usar View Binding en lugar de findViewById: más seguro, el compilador detecta errores de tipo y de ID.
- Los recursos en res/ se organizan con calificadores para soportar idiomas, densidades y orientaciones automáticamente. Nunca hardcodear strings directamente en el código o el layout.
- Los Intents son el mecanismo de comunicación entre componentes. Los explícitos abren una Activity concreta; los implícitos piden al sistema que busque quién puede hacer la acción.
- Para depurar: Logcat primero (la mayoría de errores aparecen ahí), debugger cuando hay que inspeccionar estado, Profiler cuando hay problemas de rendimiento o memoria.
