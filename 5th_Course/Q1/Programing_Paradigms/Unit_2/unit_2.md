# 2609_INSD4_PAPR_A

**SCORM:** _739662_1
**URL del contenido:** https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormdriver/indexAPI.html

## Contenido

### INTRODUCCIÓN Y OBJETIVOS

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/preview</sub>

Unidad 2. Paradigma de programación reactiva y aplicaciones con GUI.
COMENZAR CURSO
INTRODUCCIÓN Y OBJETIVOS
Introducción y objetivos
INTRODUCCIÓN A LA PROGRAMACIÓN REACTIVA
Introducción
Pasos previos a la programación reactiva
El Paradigma de Programación Reactiva. Una evolución necesaria
PROGRAMACIÓN REACTIVA CON REACTIVEX
Introducción
ReactiveX en Python
INTERFACES GRÁFICAS CON TKINTER
Introducción
TKInter
Integración de TKInter y ReactiveX
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

### Lesson 1 - Introducción y objetivos

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/TVC9lvG5jGJgirv66x8EdXaW3Q_Wi_X_</sub>

Introducción y objetivos

Introducción

En esta unidad veremos los fundamentos básicos del paradigma de programación reactiva, sus aplicaciones y las necesidades que cubre dentro del ámbito de desarrollo de software. Saber en que momentos debemos aplicar el modelo reactivo de programación nos permitirá mejorar la robustez, estabilidad y escalabilidad de nuestros programas.

Veremos que el paradigma de programación reactiva se basa en el patrón Observer. Nuestros programas deben reaccionar a los cambios ocurridos dentro de nuestro programa. No comprobaremos cambios continuamente, sino que los módulos de software serán notificados con los cambios que ocurran en los datos. Además veremos que podemos gestionar y modificar estos flujos de datos según los requisitos de nuestro software, sin tener que diseñar todo nuestro software en base al formato de los datos recibidos.

Uno de los principales campos de aplicación del paradigma de programación reactiva es la implementación de software con interfaz gráfica. Aprenderemos a implementar GUIs en Python utilizando TKInter y veremos como podemos integrar la programación reactiva con nuestra interfaz para que responda a los cambios de datos de manera adecuada.

Haz clic para voltear

Introducción a la programación reactiva

Haz clic para voltear

En el ámbito del desarrollo de software, cada paradigma de programación ha ido surgiendo como respuesta a los retos tecnológicos que han ido existiendo. El más conocido siempre ha sido el paradigma de programación imperativa, que domina la mayoría de lenguajes tradicionales, pasando por la programación orientada a objetos, donde nos centramos principalmente en los datos y no en las funciones, hasta la programación orientada a eventos, cada uno de estos paradigmas ha ofrecido soluciones a problemas concretos.

Haz clic para voltear

Programación reactiva con Ractivex

Haz clic para voltear

En programación imperativa tenemos un estado y una secuencia de instrucciones que la máquina ejecuta consecutivamente de una en una (síncrono).

Haz clic para voltear

Interfaces gráficas con Tkinter

Haz clic para voltear

Una de las principales aplicaciones del paradigma de programación reactiva está en el uso de interfaces gráficas. Generalmente una GUI debe ser robusta y estable, mostrando siempre datos actualizados sin interferir en el flujo de trabajo de nuestro software. En este apartado utilizaremos TKInter, que es la biblioteca estándar de Python para crear interfaces gráficas, para crear nuestras GUIs e integrarlas con el paradigma de programación reactiva

Objetivos

Al finalizar esta unidad, el alumno:

1

Comprenderá el paradigma de programación reactiva: Será capaz de identificar que es la programación reactiva y de aplicarla adecuadamente en los casos en los que sea necesario. Además, aprenderá a diseñar una arquitectura software basada en este modelo de programación, descomponiendo el desarrollo del software en los módulos y componentes adecuados para que puedan reaccionar correctamente a los cambios de datos.

2

Se introducirá en el desarrollo con la librearía ReactiveX: La librería reactiveX nos permite implementar el paradigma de programación reactiva en multiples lenguajes de programación. Implementa una serie de clases y métodos basadas en la arquitectura observable-observer que nos proporcionará una herramienta muy potente para crear arquitecturas que cumplan con el modelo de programación reactiva en nuestro software.

3

Aprenderá como implementar una GUI con TKInter: TKInter es la librería estándar de Python para crear interfaces gráficas. Esta nos permite aplicar un modelo de programación declarativa para crear interfaces de manera sencilla, sin preocuparnos por como es el proceso de dibujado en pantalla o la gestión de eventos de esta.

4

Entenderá como integrar una GUI adecuadamente utilizando programación reactiva: El punto de interacción entre un software y el usuario es su interfaz. Para que un usuario sienta que el programa es robusto, este debe funcionar adecuadamente, ser responsivo y no interferir con las acciones del usuario, por ejemplo, bloqueándose mientras este realiza una acción. El paradigma de programación reactiva nos ayudará a cumplir estos objetivos si sabemos como integrarlo adecuadamente con nuestra interfaz de usuario.

¡Comenzamos!

### Lesson 2 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/CEv11GQ8CPclZo3LzK46l05i-AycNReb</sub>

Introducción

En el ámbito del desarrollo de software, cada paradigma de programación ha ido surgiendo como respuesta a los retos tecnológicos que han ido existiendo. El más conocido siempre ha sido el paradigma de programación imperativa, que domina la mayoría de lenguajes tradicionales, pasando por la programación orientada a objetos, donde nos centramos principalmente en los datos y no en las funciones, hasta la programación orientada a eventos, cada uno de estos paradigmas ha ofrecido soluciones a problemas concretos. En este caso, el crecimiento de los sistemas distribuidos, la masificación de las aplicaciones en la nube y la necesidad de gestionar millones de interacciones en tiempo real, han hecho emerger el paradigma de programación reactiva como un modelo de programación más adecuado para el panorama actual de desarrollo de software.

En este apartado profundizaremos en el paradigma de programación reactiva, veremos sus bases y posibles aplicaciones.

¿Todo listo? ¡Empezamos!

### Lesson 3 - Pasos previos a la programación reactiva

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/GOf0j5fqjQHNvH4znbLx-6B5JKXJv9mH</sub>

Pasos previos a la programación reactiva

El paradigma de programación reactiva surge de la necesidad de mejorar las características y capacidades de los anteriores. Siendo el paradigma de programación imperativa el predominante en el ámbito del desarrollo del software, este presenta serias limitaciones al trabajar con modelos de programación y flujos de datos asíncronos. A continuación, veremos su evolución hasta llegar al paradigma de programación reactiva actual:

Paradigma de programación imperativa: ventajas y límites
Paradigma de programación orientada a eventos: un paso intermedio

### Lesson 4 - El Paradigma de Programación Reactiva. Una evolución necesaria

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/0ScE-lwaO8Bnu1UQeDTImDlW85HkspTs</sub>

El Paradigma de Programación Reactiva. Una evolución necesaria

El paradigma de programación reactiva puede considerarse como una evolución de la programación orientada a eventos, pero con una diferencia fundamental: no se limita a reaccionar a eventos aislados, sino que los eventos pasan a ser flujos continuos de datos (streams)..

En este paradigma, en lugar de manejar eventos puntuales con funciones independientes, los datos se representan como secuencias de información que pueden ser observadas, transformadas y combinadas de forma declarativa. Esto permite que la lógica del programa se centre más en qué hacer con los datos que en los detalles de cómo manejar las operaciones asíncronas con las que se trabaja.

Por ejemplo, en un sistema que haga uso de paradigma de programación imperativa, el programador debería centrarse en escribir y adaptar los mecanismos de concurrencia necesarios para procesar datos entrantes desde múltiples fuentes (Disco duro, API, Base de datos, …). En un paradigma orientado a eventos, tendría que definir manejadores para cada posible tipo de evento. En cambio, en un sistema basado en programación reactiva, únicamente es necesario definir un flujo de transformación y reacción, de manera declarativa, dejando que la infraestructura de programación (como RxPY en Python) gestione la asincronía y la propagación de cambios.

Ejemplo comparativo:

Paradigma de programación imperativa: “Lee este archivo, luego procesa sus datos, después guarda el resultado.”

Paradigma de programación orientada a eventos: “Cuando llegue un archivo nuevo, ejecuta la función de procesamiento.”

Paradigma de programación reactiva: “Considera los archivos como un flujo de datos; cada vez que aparezca uno nuevo, aplícale automáticamente la transformación definida y almacénalo en la salida.”

De esta forma, la programación reactiva combina lo mejor de los paradigmas anteriores, ofreciendo un modelo más conciso y robusto para sistemas modernos donde la asincronía y la concurrencia se están convirtiendo en la norma

¡Fantástico! Has completado este apartado.

### Lesson 5 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/6xjxGSVu1jXQ69v9eSm8QmwfN_ccJYwq</sub>

Introducción

En programación imperativa tenemos un estado y una secuencia de instrucciones que la máquina ejecuta consecutivamente de una en una (síncrono). Veamos un ejemplo de código muy sencillo:

num1 = input(“introduce el primer número: “)
num2 = input(“introduce el segundo número: ”)
print(num1 + num2)

Cuando ejecutamos este ejemplo, vemos que el programa se bloquea hasta que termine la primera sentencia (leer “num1”). Una vez se ejecuta pasa a la segunda y se vuelve a bloquear hasta que la segunda finalice. Cuando se han leído los dos números, la ejecución continua normalmente.

Este comportamiento es muy habitual cuando desarrollamos aplicaciones basadas en línea de comandos. Sin embargo, en la actualidad se desarrollan aplicaciones con múltiples interfaces y modelos de entrada de datos. El modelo de programación imperativa se ha quedado anticuado en este aspecto, puesto que bloquea el programa hasta haber recibido y tratado todos los datos necesarios. En un software con interfaz gráfica lo más probable es que la GUI se bloquee, proporcionando una experiencia deficiente al usuario

Dentro del paradigma de programación reactiva, nuestro código va a reaccionar a cambios. Generalmente utilizaremos operaciones asíncronas, permitiendo que el código continue su ejecución habitual. También gestionaremos los resultados o errores en otros puntos de la ejecución del código mediante callbacks.

Una alternativa al ejemplo de código anterior, basada en programación reactiva podría ser:

...
num1 = leerValor(“introduce un número: “)
num1.ready = (v) => { operar(num1) }
...

De esta manera nuestro software continuará ejecutándose después de haber indicado que queremos leer un valor, y desencadenará una acción (“operar”) cuando haya leído dicha información.

Por lo general, el software desarrollado mediante programación reactiva responde también a modelos de flujos de datos asíncronos, como se puede ver en la siguiente imagen:

Imagen 1 Multiples flujos de datos concurrentes

Los datos que recibamos pueden fluir a diferentes ritmos, y necesitaremos encontrar la forma de sincronizar todos estos flujos de datos.

### Lesson 6 - ReactiveX en Python

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/WytwaHH6YQshXjRvlQGQGe1P_Q1Cpv1t</sub>

ReactiveX en Python

RectiveX es una API de programación reactiva que permite utilizar flujos observables para comunicar cambios de datos entre los diferentes modulos de nuestro software. Para poder instalar la librería lo haremos a través de pip (recordad utilizar un entorno virtual):

pip install rx

Aunque vamos a utilizar la versión para Python (RxPy), la API ReactiveX existe para una gran cantidad de lenguajes de programación, por lo que podemos utilizar para casi cualquier tipo de proyecto:

Java: RxJava

JavaScript: RxJS

C#: Rx.NET
(se abre en una nueva pestaña)

C#(Unity): UniRx

Scala: RxScala

Clojure: RxClojure

C++: RxCpp

Ruby: Rx.rb

Groovy: RxGroovy

Jruby: RxJRuby

Kotlin: RxKotlin

Aunque ya deberíamos conocer su funcionamiento, repasemos brevemente en que consiste una función lambda en Python: Son funciones anónimas, lo que significa que no tienen nombre, por lo que solo podemos acceder a ellas desde el lugar donde la definimos. Además, tienen restricciones con respecto a las funciones tradicionales:

Solo podemos utilizar expressions

Constan de una única expresión

No pueden utilizarse o declararse variables locales

La programación reactiva incita al uso de lambdas, ya que tenemos operadores que toman como entrada funciones

x= lambda a:a+ 10
print(x(5))

Conceptos básicos en ReactiveX

Vamos a empezar con un ejemplo sencillo. En ReactiveX existen dos conceptos fundamentales:

Observable: Objeto que va obteniendo nuevos datos y envía notificaciones cuando ocurre un cambio en estos (Por ejemplo, lee algo desde teclado)

Observer: Entidad que se suscribe al observable, y actúa cuando recibe una notificación de cambio

En el siguiente bloque de código podemos ver como utilizar estos dos conceptos en ReactiveX:

from rx import create

def generador(observer, scheduler):
    observer.on_next('Hola’)
    observer.on_next('Adiós’)
    observer.on_completed()

observable = create(generador)

observable.subscribe(
    on_next=lambda v: print(f'Recibido: {v}’),
)

La función create nos permite crear un nuevo observable. Vemos que recibe como parámetro una función que más adelante ejecutará. Esta debe recibir como parámetro dos variables: observer y scheduler. La función que le estamos pasando es generador. Generador es una función muy sencilla que nos sirve como ejemplo. Simplemente emite dos strings a todos los observers que se encuentren suscritos al observable. Para emitir un nuevo dato utiliza el método .on_next(). Este método, que pertenece al objeto observer, envía nuevos datos a todos los observers suscritos. Finalmente utilizamos .on_completed() para indicar que se ha terminado de emitir datos.

Tambien vemos que el observable dispone de un método .subscribe(). Este permite agregar un observer que será notificado cada vez que ocurra un evento. En este caso, suscribimos una función lambda al tipo de evento on_next, de forma que imprimirá por pantalla cada mensaje que reciba. Podemos modificarlo para que realice otra acción cuando ocurre un evento on_completed:

…
observable.subscribe(
    on_next=lambda v: print(f'Recibido: {v}’),
    on_completed=lambda : print(“El observable ha finalizado”),
)

De esta manera, nuestro observer también puede realizar acciones cuando la ejecución del observable finaliza.

Por simplicidad hemos asignado funciones lambda a on_next y on_completed, pero una buena practica sería crear una nueva clase que herede de Observer (clase incluida en rx) e implementar ahí toda la lógica del observador:

…
from rx.core import Observer

class Printer(Observer):
    def on_next(self, v):
      print(v)

    def on_completed(self):
        print(“El observable ha finalizado”)

def on_error(self, e):
        print(f“Error: {e}”)

…

También podemos indicar que acción realizar cuando se envía un mensaje de error. Para crear y suscribir nuestro nuevo objeto de tipo Printer:

…
printer = Printer()
observable.subscribe(printer)

Ahora que ya sabemos cómo interactúan los observers y observables veamos formas de crearlos para los patrones más habituales:

La función of de reactivex nos permite crear un Observable Factory, al cual le pasaremos como argumentos los datos que queremos emitir, y nos dará la misma funcionalidad que en el caso anterior:

from rx import of

observable = of('Hola', 'Adiós')

observable.subscribe(lambda v: print(f'Recibido: {v}'))

En este ejemplo podemos notar que, si no necesitamos suscribirnos a on_completed ni a on_error, el observer se suscribe por defecto a on_next.

La función from_ es similar al caso anterior, pero esta vez generando un observable a partir de una lista que le pasemos como parámetro:

from rx import from_

l = [1, 2, 3, 4, 5]
# Esta vez utilizamos la factoría from
observable = from_(l)

# Nos suscribimos a los cambios del observable
observable.subscribe(
    on_next=lambda v: print(f'Recibido: {v}'),
    on_completed=lambda: print('Terminado'),
    on_error=lambda e: print(f'Error: {e}')
)

Veamos ahora un ejemplo un poco más completo, donde el observable se encarga de pedir al usuario un mensaje por teclado. Cuando el mensaje llega, el programa notifica al observer para que lo imprima por pantalla. Aunque no está implementado sistemas asíncronos, es un buen punto de partida para entender cómo funciona:

from rx import create
from rx.core import Observer

class Printer(Observer):
  def on_next(self, v):
    print(v)

def observer_teclado(observer, scheduler):
    while 1:
        msg = input('Introduce un mensaje')
        if msg:
            observer.on_next(msg)
        else:
            observer.on_completed()
            return

observable = create(observer_teclado)

# Nos suscribimos con un Observer custom
observable.subscribe(Printer())

Repasemos las funciones de rx en el siguiente video:

Reproducir Vídeo

Pipes, Operadores y Chaining

En este punto ya sabemos cómo crear una arquitectura observer-observable, pero, ¿qué podemos hacer con los datos recibidos desde el observable? ¿Tengo que adaptar todo mi software al formato de datos que me proporciona? La respuesta es No, ReactiveX proporciona mecanismo que permiten modificar los datos que salen del observable antes de que lleguen al observer. Estos son los pipes

En el ámbito del software y Sistemas Operativos, un pipe es un mecanismo que permite comunicar dos procesos mediante un modelo de paso de mensajes. En este caso lo podemos considerar como algo similar: un mecanismo que permite comunicar el observable y el observer modificando los datos que se pasan entre ellos.

Dentro del pipe podemos incluir una serie de operadores que se encargarán de hacer las modificaciones que queramos. Por ejemplo, el operador map nos permite aplicar una función nueva sobre cada nuevo dato que llegue. En este caso convertiremos todos los strings a letras mayúsculas, y añadiremos el prefijo “En mayúscula: ”:

from rx import of, operators

observable = of('Hola', 'Adiós')

observable_pipe = observable.pipe(
  operators.map(lambda s: s.upper()),
  operators.map(lambda s: f'En mayúscula: {s}')
)

observable_pipe.subscribe(lambda v: print(f'Recibido: {v}'))
#Output: Recibido: En mayúscula: HOLA
#               Recibido: En mayúscula: ADIÓS

Como vemos, en lugar de suscribir nuestro observer directamente al observable, lo hacemos directamente al pipe que hemos creado. Debemos darnos cuenta de que ahora tenemos dos observables. Uno que emite los datos en cuanto están disponibles (observable), y otro que recibe esos datos y los modifica para, tras la modificación, emitirlos. Podríamos decir que estamos encadenando observable-observer/observable-observer. Veamos que ocurre si nos suscribimos al primer observable:

from rx import of, operators

observable = of('Hola', 'Adiós')

observable_pipe = observable.pipe(
  operators.map(lambda s: s.upper()),
  operators.map(lambda s: f'En mayúscula: {s}')
)

observable.subscribe(lambda v: print(f'Recibido: {v}'))
#Output: Recibido: Hola
#               Recibido: Adiós

Como vemos, si nos suscribimos al primer observable recibimos los datos que se han emitido sin modificar. Esto nos permite disponer de los datos en todos sus formatos si fuera necesario. Incluso podemos tener dos observers haciendo que uno esté suscrito al observable original y otro al pipe:

from rx import of, operators

observable = of('Hola', 'Adiós')

observable_pipe = observable.pipe(
  operators.map(lambda s: s.upper()),
  operators.map(lambda s: f'En mayúscula: {s}')
)

observable.subscribe(lambda v: print(f'Recibido: {v}'))
observable_pipe.subscribe(lambda v: print(f'Recibido2: {v}'))
#Output: Recibido: Hola
#               Recibido: Adiós
#               Recibido2: En mayúscula: HOLA
#               Recibido2: En mayúscula: ADIÓS

Como esto es Python, podemos simplificar mucho nuestro código teniendo todo esto en una sola línea:

from rx import of, operators

of('Hola', 'Adiós').pipe(
  operators.map(lambda s: s.upper()),
  operators.map(lambda s: f'En mayúscula: {s}')
).subscribe(lambda v: print(f'Recibido: {v}'))

Existen múltiples operadores que podemos aplicar dentro de un pipe. Aunque hemos visto el operador map, existen varios más, clasificados según sus tipos:

Operadores de combinación (Combination Operators)
Operadores de filtrado (Filtering Operators)
Otros operadores comunes en ReactiveX

Podemos consultar su funcionamiento a través de sus Marble Diagrams, los cuales podemos encontrar en https://rxmarbles.com/
(se abre en una nueva pestaña)
 . Aunque en este caso utilicemos los Marble Diagrams

Los Marble Diagrams (MD) constan de 3 partes principales:

Línea de tiempo de entradas: Nos muestra como llegan los datos de entrada a nuestro operador, teniendo en cuenta el punto de inicio y de fin.

Descripción de la transformación: Normalmente la función o el operador que estamos describiendo.

Línea de tiempo de salidas: Nos muestra como salen los datos tras pasar por la transformación, indicando el punto de inicio y de fin.

Imagen 2 Detalle de un Marble Diagram

Normalmente solo hay una línea de tiempo de entrada y otra de salida, pero se pueden dar casos en los que tenemos varias. Por ejemplo:

Imagen 3 Marble Diagram con múltiples salidas

También podemos saber si una línea de tiempo termina con éxito o con un error, según como aparece la flecha:

Imagen 4 Tipos de finalización de un flujo de datos en un Marble Diagram

Veamos un ejemplo con el operador map. Este modifica los datos que llegan por la entrada para emitirlos en la salida, pero en el medio aplica una función a cada uno de los elementos que llegan, emitiendo el resultado. En este caso podemos ver un ejemplo de como “multiplicar por diez”:

Imagen 5 Ejemplo de un Marble Diagram que multiplica todos los números por 10

Repasemos el los pipes en el siguiente video:

Reproducir Vídeo

Veamos un ejercicio como ejemplo: Vamos a construir una aplicación de búsqueda de películas utilizando la API de OMDB (http://www.omdbapi.com
(se abre en una nueva pestaña)
). En este punto de la asignatura debemos habernos registrado y disponer de una API KEY. Nuestra aplicación desarrollada en Python debe lanzar una petición de búsqueda encuentre todo el contenido que encaje con un título. Por ejemplo, si buscamos la película “Interstellar”, utilizaremos la petición GET https://www.omdbapi.com/?apikey=[API_KEY]&s=interstellar
(se abre en una nueva pestaña)
 nos devuelve el siguiente resultado, con un total de 44 resultados, aunque solo nos muestra 10:

{
  "Search": [
    {
      "Title": "Interstellar",
      "Year": "2014",
      "imdbID": "tt0816692",
      "Type": "movie",
      "Poster": "https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_SX300.jpg"
    },
    {
      "Title": "The Science of Interstellar",
      "Year": "2014",
      "imdbID": "tt4415360",
      "Type": "movie",
      "Poster": "https://m.media-amazon.com/images/M/MV5BZDU5NTJkMjQtNGYyZC00NjYwLWJlNWMtODk5NDI5MDE3NDJiXkEyXkFqcGc@._V1_SX300.jpg"
    },
    …
    {
      "Title": "Interstellar",
      "Year": "2005",
      "imdbID": "tt0758429",
      "Type": "movie",
      "Poster": "https://m.media-amazon.com/images/M/MV5BMTgyNzUyMTQ3OV5BMl5BanBnXkFtZTgwNDg0OTE2MzE@._V1_SX300.jpg"
    }
  ],
  "totalResults": "44",
  "Response": "True"
}

La API implementa paginación, por lo que si necesitamos acceder a más elementos tenemos que indicar en que página se encuentran. Si tenemos 44 resultados y nos muestra 10 resultados por página habrá un total de 5 páginas. Podemos indicar que página vamos a descargar con https://www.omdbapi.com/?apikey=[API_KEY]&s=interstellar&page=2
(se abre en una nueva pestaña)
 .

El objetivo del ejercicio es descargar todos los contenidos relacionados con un titulo, accediendo a todas las páginas que sea necesario. Por cada resultado debemos imprimir por pantalla solo aquellos que tengan un type == ‘movie’, dándoles el formato: (ID) – TITULO: URL_POSTER (AÑO).

Para lograr esto debemos utilizar el paradigma de programación reactiva mediante Reactivex. Desarrollaremos una función observable que haga las peticiones correspondientes a la web y, tras obtener un resultado, debe emitir uno por uno los resultados. El pipe se encargará de filtrar aquellos elementos que no sean del tipo “movie”, para luego transformarlos al formato indicado. Finalmente, el observer se encargará de imprimirlo por pantalla

Veamos la solución a este ejercicio:

Como vemos en el código, cada vez que se descarga una página, se emiten por separado todas las entidades que se han encontrado. Si hay más páginas vuelve a realizar la petición get. Si no las hay, las peticiones finalizan. Después pasamos por un pipe los resultados, descartando con el operador filter aquellas que no sean de tipo “movie”. También utilizamos otro operador map para dar el formato correcto. Si ejecutamos el código, vemos que no se imprime todo el resultado de golpe, sino que va haciéndolo secuencialmente. Esto es debido a la característica principal del paradigma de programación reactiva. Nuestro programa reacciona a los cambios en los datos. Que se obtenga nueva información sobre una película es un cambio que se notifica, y nuestro software actúa en consecuencia, en este caso imprimiendo por pantalla el dato que se ha emitido.

Debemos tener en cuenta que podemos tener varios flujos de datos como estos, y que nuestra interfaz no tiene por qué ser una terminal, por lo que será necesario trabajar de manera asíncrona como veremos más adelante en la asignatura.

¡Fantástico! Has completado este apartado.

### Lesson 7 - Introducción

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/TCYF20CZD5WVXxxTXpJeUUmN64MUeUAk</sub>

Introducción

Una de las principales aplicaciones del paradigma de programación reactiva está en el uso de interfaces gráficas. Generalmente una GUI debe ser robusta y estable, mostrando siempre datos actualizados sin interferir en el flujo de trabajo de nuestro software. En este apartado utilizaremos TKInter, que es la biblioteca estándar de Python para crear interfaces gráficas, para crear nuestras GUIs e integrarlas con el paradigma de programación reactiva

### Lesson 8 - TKInter

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/O7STPG4m6fqMjS2ltXLm_i0qcGUAkswZ</sub>

TKInter

TKInter es una librería que forma parte del estándar de Python, por lo que generalmente no necesita instalaciones adicionales. En Windows debemos haber instalado Python indicando que deseamos que también se instalen los modulos “tcl/tk”.

TKInter se basa en la colocación de Widgets dentro de una ventana, por lo que trabajaremos a alto nivel utilizando programación declarativa: nosotros le indicaremos que widget queremos y en que posición, y la librería se encargará de “dibujarlos” en nuestra interfaz.

Veamos el primer ejemplo de interfaz que podemos desarrollar:

import tkinter as tk

root = tk.Tk()
root.title("Hola Tkinter")
root.geometry("300x150")         # ancho x alto
root.mainloop()

Esto nos muestra la siguiente ventana vacía:

Imagen 6 Ventana principal de TKInter

Veamos los diferentes pasos para crear la interfaz:

root=tk.Tk
(se abre en una nueva pestaña)
():  Crea la ventana principal de nuestra GUI

root.title("Hola Tkinter"): Asigna un titulo a nuestra ventana

root.geometry("300x150"): Asigna el tamaño de la ventana. Hay que hacerlo pasandole como argumento directamente un string que contenga “ANCHOxALTO”

root.mainloop(): Inicia el bucle principal de TKInter. Este bucle se encarga de actualizar y detectar todos los posibles cambios que puedan ocurrir en la interfaz. Por ejemplo: detecta la pulsación de botones o el cambio de posición de la ventana, o cambia un texto si los datos se alteran.

Ahora que ya tenemos nuestra ventana principal, vamos a añadir un Widget. En este caso un Label o texto:

import tkinter as tk

root = tk.Tk()
root.title("Hola Tkinter")
root.geometry("300x150")
hello = tk.Label(text='Hola!')
hello.pack()
root.mainloop()

Dando como resultado:

Imagen 7 "Hola Mundo" en TKInter

En este caso, hemos incluido el texto “Hola!”. Para ello simplemente creamos el widget con los argumentos correspondientes. Luego invocamos a la función .pack() la cual se encarga de colocar de manera automática los widgets dentro de la ventana.

Existen muchos más widgets que podemos utilizar, como Label, Button, Entry, ComboBox, CheckButton, Radio, Menu Bar… aunque durante esta unidad nos quedaremos solo con los más básicos.

Ahora añadiremos un botón. Para ello necesitamos crear una función adicional que se ejecute cada vez que lo pulsemos. En este caso haremos que imprima por pantalla un texto:

import tkinter as tk

def mostrar_texto():
    print("Boton pulsado")

root = tk.Tk()
root.title("Hola Tkinter")
root.geometry("300x150")

hello = tk.Label(text='Hola!')
hello.pack()

btn = tk.Button(root, text="Mostrar", command=mostrar_texto)
btn.pack(pady=5) # pady añade un margen vertical
root.mainloop()

Teniendo como resultado:

Vamos a agregar ahora un par de widgets mas, que serán un Entry (Campo de entrada de texto) y un ComboBox (Selector de opciones):

import tkinter as tk
from tkinter import ttk   # ttk es necesario para usar Combobox

def mostrar_texto():
    print("Boton pulsado")

root = tk.Tk()
root.title("Hola Tkinter")
root.geometry("300x150")

hello = tk.Label(text='Hola!')
hello.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

combo = ttk.Combobox(root, values=["Opción 1", "Opción 2", "Opción 3"])
combo.current(0)   # valor por defecto
combo.pack(pady=5)

btn = tk.Button(root, text="Mostrar", command=mostrar_texto)
btn.pack(pady=5)

root.mainloop()

Dándonos como resultado:

Imagen 9 Mas widgets en TKInter

Haciendo una modificación en la función mostrar_texto podemos hacer que el Label muestre los datos que hemos introducido en el Entry y en el ComboBox:

def mostrar_texto():
    texto = entry.get()
    seleccionado = combo.get()
    hello.config(text=f"{texto} | {seleccionado} ")
…

Donde la interfaz nos mostraría:

Imagen 10 Modificar widgets en TKInter

Finalmente, vamos a añadir un CheckButton. Vamos a trabajar de una forma un poco diferente: crearemos una variable booleana que bindearemos al widget, de manera que cada vez que cambiemos el widget, la variable cambiará y viceversa. Para obtener el contenido de la variable utilizaremos la función get() de esta variable. Veamoslo en el siguiente ejemplo:

import tkinter as tk
from tkinter import ttk   # ttk es necesario para usar Combobox

def mostrar_texto():
    texto = entry.get()
    seleccionado = combo.get()
    aceptado = "Sí" if check_var.get() else "No"
    hello.config(text=f"{texto} | {seleccionado} | Acepta: {aceptado}")

root = tk.Tk()
root.title("Hola Tkinter")
root.geometry("300x250")

hello = tk.Label(text='Hola!')
hello.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

combo = ttk.Combobox(root, values=["Opción 1", "Opción 2", "Opción 3"])
combo.current(0)   # valor por defecto
combo.pack(pady=5)

check_var = tk.BooleanVar(value=False)
check = tk.Checkbutton(root, text="Aceptar términos", variable=check_var)
check.pack(pady=5)

btn = tk.Button(root, text="Mostrar", command=mostrar_texto)
btn.pack(pady=5)

root.mainloop()

Creando la siguiente GUI:

Imagen 11 Variables bindeadas en TKInter

Como hemos comentado, la función pack se encarga de posicionar los widgets en nuestra ventana en el orden en el que se añaden. Sin embargo, podemos utilizar distintas distribuciones para mostrar los elementos.

Una de estas posibles distribuciones es la división de la ventana en un grid. Utilizando el método .grid podemos asignar las posiciones de nuestro widget dentro del grid, incluso indicando cuantas celdas de ese grid queremos ocupar. Veamos un ejemplo:

from tkinter import Tk, Label, Button, Entry, BooleanVar, Checkbutton
from tkinter.ttk import Combobox

class GUITest:

    def __init__(self):
        self.root = Tk()
        self.root.title("TKinter Grid")
        self.root.geometry("500x200")

        self.hello = Label(text='Hola!', font=('Arial Bold', 50))
        self.hello.grid(column=0, row=0)

        self.sub = Label(text='Esto sale más pequeño', font=('Arial', 24))
        self.sub.grid(column=1, row=0)

        self.btn = Button(text='Pulsa', command=self.onButtonClick).grid(column=1, row=1)

        self.entry = Entry(bg='#eeeeee', fg='#111111')
        self.entry.grid(column=0, row=2)

        Button(text='Pulsa', command=self.onButtonClick).grid(column=1, row= 2)

        self.combo = Combobox(values=['Cero', 'Uno', 'Dos', 'Tres', 'Cuatro'], state='readonly')
        self.combo.grid(column=0, row=3)
        self.combo.current(2)

        Button(text='Pulsa', command=self.onButtonClick).grid(column=1, row=3)

        self.checkState = BooleanVar()
        self.checkState.set(True)
        self.chk = Checkbutton(text='Sí o No', var=self.checkState).grid(column=0, row=4)

        self.root.mainloop()

    def onButtonClick(self):
        print("Button Clicked!")

gui = GUITest()

Veremos cómo nos los distribuye adecuadamente en el grid, según la fila (row) y columna (column) que le hemos indicado:

Imagen 12 Grid en TKInter

El siguiente video nos resume como colocar los widgets dentro del grid:

Reproducir Vídeo

Vamos a hacer un ejercicio básico que nos permitirá experimentar con TKInter y el desarrollo de interfaces gráficas. En este caso desarrollaremos una pequeña aplicación que será una calculadora como la que vemos en la imagen:

Imagen 13 Ejercicio calculadora

Esta debe incluir todos los botones de operación que vemos, así como los números. Cada vez que pulsemos sobre un botón, su símbolo se escribirá en el panel superior. Cuando pulsemos en el botón “=”, dicho panel superior deberá mostrar el resultado de la operación que hemos añadido previamente. Aprovecharemos este ejercicio para experimentar con los argumentos y configuraciones que les podemos pasar a los diferentes widgets, para lo que os recomiendo revisar la documentación de TKInter: https://docs.python.org/3/library/tkinter.html
(se abre en una nueva pestaña)

Aunque con los conocimientos que tenemos hasta ahora podemos desarrollarla adecuadamente, no sabemos pasar como parámetro una función con un argumento. Siempre hemos asumido que los argumentos se los proporciona quien hace el callback, pero en este caso, para que cada botón realice una acción diferente deberíamos crear una nueva función por cada uno de los botones que tenemos, creando un código grande y difícil de leer. Aquí es donde entra la función partial de Python. Esta nos permite crear funciones parciales, es decir, nos permite crear una nueva función, basándonos en otra que ya existe, pero manteniendo uno de sus argumentos fijo. Veamos un ejemplo:

from functools import partial

def f(a, b, c, x):
    return 1000*a + 100*b + 10*c + x

# Fijamos los argumentos a, b y c
g = partial(f, 3, 1, 4)

print(g(5))
# Output: 3145

Si no queremos mantener el orden de los argumentos, debemos indicar cual estamos modificando, como podemos ver a continuación:

from functools import *

def add(a, b, c):
    return 100 * a + 10 * b + c

# Fijamos los argumentos b y c
add_part = partial(add, c = 2, b = 1)

print(add_part(3))
#Output: 312

Podemos utilizar tanto funciones lambda como funciones parciales para indicar que botón hemos pulsado en nuestra interfaz

Veamos la solución a este ejercicio:

### Lesson 9 - Integración de TKInter y ReactiveX

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/SA72EK-wi035ICwDPbFw9KQatAvGVMNY</sub>

Integración de TKInter y ReactiveX

Ahora que ya sabemos crear nuestras propias GUIs, vamos a integrarlas con un flujo continuo de datos. Utilizaremos un bus Kafka para recibir un flujo de mensajes a medida que estos llegan, emitiéndolos a la interfaz. Para ello empezaremos viendo cómo funciona una arquitectura basada en un bróker de mensajes Kafka.

Apache Kafka

Apache Kafka es una plataforma distribuida para la transmisión de datos que permite no solo publicar, almacenar y procesar flujos de eventos de forma inmediata, sino también suscribirse a ellos. Está diseñado para administrar flujos de datos de varias fuentes y enviarlos a distintos usuarios. En pocas palabras, transfiere grandes cantidades de datos entre todos los posibles nodos que se encuentren conectados. Generalmente se utiliza para conectar distintos microservicios.

Suponiendo que trabajamos en un sistema Windows, vamos a instalar un bróker Kafka utilizando WSL2 (Si tenemos Linux el proceso será más sencillo)

Lo primero que necesitamos es instalar WSL. Este proceso seguramente lo habremos realizado varias veces, pero repasemos el proceso. (Si ya lo tienes no es necesario)

Abrimos una terminal (por ejemplo, Powershell) con permisos de administrador, y ejecutamos el siguiente comando:

wsl --install

Por defecto nos instalará una distribución Ubuntu. Ahora podemos ir al menú inicio y buscar la instalación de Ubuntu como vemos en la imagen:

Imagen 15 Instalación de WSL

Ahora nos pedirá la configuración inicial, que será el nombre de usuario y la contraseña que queramos poner (no tiene por que ser la del equipo). Tras ello nos pedirá reiniciar el equipo.

Tras reiniciar, volvermos a buscar “Ubuntu” en nuestro sistema y nos abrirá una terminal Ubuntu como las que ya estaremos habituados a ver. Pasemos a instalar el bróker Kafka. Para ello empezaremos por actualizar los repositorios APT de Ubuntu:

sudo apt update

debemos instalar java:

sudo apt install default-jre

Y ahora podemos descargar el paquete:

wget https://dlcdn.apache.org/kafka/4.1.0/kafka_2.13-4.1.0.tgz
tar -xzf kafka_2.13-4.1.0.tgz
cd kafka_2.13-4.1.0

Tras la descarga, podemos arrancar el bróker. Para ello utilizaremos los siguientes comandos:

KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
bin/kafka-server-start.sh config/server.properties

Kafka se basa en topics. Cada cliente conectado puede escribir y leer del topic que desee simplemente indicando el nombre. Para hacer la prueba ejecutaremos el siguiente comando, que nos permite crear el topic “paradigmasdeprogramación”. Ten en cuenta que la terminal que habíamos abierto antes está ocupada por el bróker, así que tendremos que abrir una nueva en Ubuntu, y volver a acceder a la carpeta.

bin/kafka-topics.sh --create --topic paradigmasdeprogramacion --bootstrap-server localhost:9092

Ahora recibiremos los mensajes. Abriremos una tercera terminal para poder ir viendo el proceso. Accederemos a la carpeta y ejecutaremos el comando

bin/kafka-console-consumer.sh --topic paradigmasdeprogramacion --from-beginning --bootstrap-server localhost:9092

Y con el siguiente comando podemos enviar un mensaje al mismo topic (Ten en cuenta que tendrás que abrir otra terminal de Ubuntu):

bin/kafka-console-producer.sh --topic paradigmasdeprogramacion --bootstrap-server localhost:9092

Esto nos ejecuta una consola en la que podemos escribir mensajes, y estos llegarán al receptor que habíamos ejecutado antes. Veríamos como resultado:

Imagen 16 Receptor de mensajes Kafka

Como vemos, cada vez que un cliente envía un mensaje, todos los que estén escuchando lo reciben correctamente.

En Python podemos utilizar Kafka mediante la librería kafka-python. Vamos a volver a Windows (Sin cerrar las terminales de Ubuntu) para crear un entorno virtual y a instalarla:

python -m venv venv
pip install kafka-python

Ahora podemos crear un script de Python que reciba los mensajes del bróker Kafka:

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "paradigmasdeprogramacion",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest' # Indicamos que queremos recibir solo los ultimos mensajes
    )

for msg in consumer:
    print(msg.value.decode("utf-8"))

Si lo ejecutamos y enviamos mensajes a través de la terminal, vemos que los podemos recibir adecuadamente en Python. Podemos ver el funcionamiento de este servicio en el siguiente video:

Reproducir Vídeo

Ahora que tenemos el bróker Kafka configurado, pasemos a realizar un ejercicio. Vamos a implementar una aplicación basada en una arquitectura reactiva. Crearemos una interfaz gráfica con un campo Entry donde tendremos que introducir el topic del que queremos leer. También incluiremos un Button y un Text (Similar a un Entry pero con tamaño variable, para textos largos). Al pulsar el botón, nuestra aplicación debe conectarse al bróker Kafka y recibir todos los mensajes que vayan llegando. A medida que se reciban utilizaremos ReactiveX para emitirlos a la GUI. El widget Text deberá actualizarse mostrando en orden los mensajes que vayan llegando.

Aunque un poco tedioso, no parece difícil, ¿cierto? Vamos a intentar resolverlo y veamos que ocurre.

Una posible solución al ejercicio podemos verla a continuación

Sin embargo, si ejecutamos esto la interfaz se bloquea al pulsar el botón Conectar, aunque si vemos como se imprimen los mensajes por consola. Esto se debe principalmente al funcionamiento de la interfaz gráfica, en concreto a la función mainloop. Cuando invocamos a la función, nuestra interfaz se pone en marcha, y se encarga de gestionar todos los posibles eventos que ocurren. Esto lo hace mediante un bucle infinito que va comprobando cada acción y pintando la interfaz cuando se actualiza. Sin embargo, el bucle … for msg in consumer: … también es infinito, y se encuentra dentro del mainloop. Así que no deja que el bucle principal de la GUI siga haciendo comprobaciones y actualizaciones.

Aunque veremos en profundidad como solucionar este problema más adelante en la asignatura, de momento podemos crear un thread que se encargue de escuchar los mensajes que llegan desde el bróker Kafka:

…
import threading
…
…
    def on_button_click(self):
        t1 = threading.Thread(target=self.create_observable_and_subscribe)
        t1.start()

    def create_observable_and_subscribe(self):
        topic = self.entry.get()
        kafka_listener = KafkaListenerReact(topic)
        observable = create(kafka_listener.observable_kafka)
        observable.subscribe(TextUpdater(self.text_box))
…

Esto evitará que la interfaz se bloquee, pudiendo tener ambos bucles en ejecución al mismo tiempo, teniendo como resultado la siguiente interfaz:

Veamos la explicación en el siguiente video:

Reproducir Vídeo
¡Fantástico! Has completado este apartado.

### Lesson 10 - Conclusiones de la unidad

<sub>https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/CC9SJ1IjjRP9n_46EiF-ao_qYxUDofUZ</sub>

Conclusiones de la unidad

A lo largo de esta unidad hemos profundizado en el paradigma de programación reactiva, identificando su origen, sus fundamentos y la forma en la que responde a las necesidades actuales del desarrollo de software. Hemos analizado cómo este modelo supone una evolución natural respecto a la programación imperativa y orientada a eventos, tratando estos eventos como flujos de datos continuos que pueden ser observados, transformados y combinados de manera declarativa.

El estudio de la librería ReactiveX nos ha permitido comprender de forma práctica cómo implementar arquitecturas basadas en observables y observadores, donde será necesario gestionar a asincronía y la concurrencia de forma adecuada. A través de ejemplos en Python hemos explorado el uso de funciones lambda, pipes y operadores como map, filter o merge, lo que facilita la transformación y sincronización de flujos de datos complejos, mejorando la modularidad y la legibilidad del código.

Asimismo, hemos visto cómo la integración de este paradigma con el desarrollo de interfaces gráficas mediante TkInter permite crear GUIs más dinámicas, estables y reactivas a los cambios de estado o datos en tiempo real. La utilización de widgets y el bucle principal de la librería se complementan con el enfoque reactivo, ofreciendo un nuevo marco de desarrollo para aplicaciones interactivas que requieren gestionar múltiples fuentes de información sin bloquear la experiencia del usuario.

En conjunto, los contenidos de la unidad nos proporcionan herramientas conceptuales y prácticas para abordar problemas actuales de programación, donde la asincronía y la concurrencia son habituales. El dominio del paradigma reactivo, unido a su implementación con librerías como ReactiveX y a su integración en GUIs, forma una base sólida para desarrollar aplicaciones modernas, escalables y centradas en la experiencia del usuario.

¡Felicidades! Has finalizado la unidad. Y ahora, ¡a por las prácticas!


## Recursos y enlaces

- [Unidad 2. Paradigma de programación reactiva y aplicaciones con GUI.](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/TVC9lvG5jGJgirv66x8EdXaW3Q_Wi_X_)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/CEv11GQ8CPclZo3LzK46l05i-AycNReb)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/GOf0j5fqjQHNvH4znbLx-6B5JKXJv9mH)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/0ScE-lwaO8Bnu1UQeDTImDlW85HkspTs)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/6xjxGSVu1jXQ69v9eSm8QmwfN_ccJYwq)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/WytwaHH6YQshXjRvlQGQGe1P_Q1Cpv1t)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/TCYF20CZD5WVXxxTXpJeUUmN64MUeUAk)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/O7STPG4m6fqMjS2ltXLm_i0qcGUAkswZ)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/SA72EK-wi035ICwDPbFw9KQatAvGVMNY)
- [A](https://u-tad.blackboard.com/courses/1/2609_INSD4_PAPR_A/content/_739662_1/scormcontent/index.html#/lessons/CC9SJ1IjjRP9n_46EiF-ao_qYxUDofUZ)