# CAPÍTULO 1: Construcción de Algoritmos de eficiencia

### Construcción de Sofware

consideraremos los siguientes elementos que también deberán cumplir nuestros programas, para considerar que están “bien” programados:

- Bien comentado. Se esperan comentarios con una buena redacción (sin faltas ortográficas, claros y sin ambigüedades, y concisos (sin paja)).
- Nomenclatura correcta.
- Máxima cohesión.
- Mínimo acoplamiento.
- Seguir el patrón MVC.
- Mínimo acoplamiento.
- Seguir el patrón MVC.
- Bien dividido en ficheros, clases y métodos/funciones.
- Buena presentación.
- Precondiciones.
- Indicada la complejidad temporal y espacial.

### ¿Cómo comentar el código?

Los comentarios son una herramienta fundamental para asegurar mantenimiento y reutilización del código, debemos tener en cuenta que en un trabajo en equipo el ingeniero de software debe asegurar que los desarrollos son fáciles de pasar a sus compañeros que no tienen porque conocer previamente su desarrollo o partes. Un uso correcto de los comentarios reduce drásticamente el tiempo necesario para que un nuevo integrante del equipo rinda al 100% en un proyecto software. Diferenciamos los siguientes tipos 

- Comentarios iniciales en cada clase antes de su cabecera
- Comentarios en cada declaración de método.
- Comentarios en cada declaración de atributo de una clase.
- Comentarios en partes complejas como bucles anidados.

Lo normal al desarrollar en un determinado lenguaje es que se acuerde una nomenglatura común, la cual es muy importante seguir para garantizar la reutilización de código la cual añadiremos a todos los nombres en la primera letra de cada nombre, a nombres de clases y variables (que deben ser siempre sustantivos). 

```agda
Un buen programa debe cumplir con:
✅ Código bien comentado y redactado.
✅ Nomenclatura correcta.
✅ Alta cohesión y mínimo acoplamiento.
✅ Seguir el patrón MVC.
✅ Organización en ficheros, clases y funciones.
✅ Buena presentación y documentación de complejidad.

¿Cómo comentar el código? 📝
Los comentarios facilitan el mantenimiento y la reutilización del código. Se deben incluir en:
📌 Clases (antes de la cabecera).
📌 Métodos y atributos.
📌 Partes complejas (ej. bucles anidados).

💡 Además, es clave seguir una nomenclatura común para facilitar la colaboración y la reutilización del código.
```

### Principio de mínimo acoplamiento

El principio de mínimo acoplamiento sugiere que los módulos o componentes de un sistema deben ser lo menos dependientes posible unos de otros. Cuando hablamos de módulos nos referimos a piezas software, que a su vez pueden ser o bien un programa entero, una parte de un programa, un conjunto de líneas de código, una clase… En este caso el acoplamiento se refiere a la interdependencia entre dichos módulos. Un bajo acoplamiento implica que los cambios en un módulo tienen un impacto mínimo o nulo en otros módulos. El objetivo del mínimo acoplamiento es crear sistemas más mantenibles, escalables y comprensibles.

En UML (Lenguaje Unificado de Modelado), una pieza de software se representa por un rectángulo con el nombre de la pieza de software escrito dentro de él. Una pieza de software “A” depende de una pieza de software “B” cuando “A” necesita que se haya ejecutado previamente “B” para que “A” funcione bien. Ejemplo 1: “A” depende de “B” si “A” llama a un procedimiento de “B”. Ejemplo 2: Un bucle que recorre un array de enteros para imprimirlo (pieza “A”) necesita que previamente se haya declarado y llenado dicho array de enteros (pieza “B”). Cuando “A” depende de “B”, en UML se representa con una flecha desde “A” a “B”.

![image.png](attachment:4a5cb4b1-11ce-436f-ba42-c233bc952748:image.png)

Se dice que dos piezas de software “A” y “B” (“A” depende de “B”) están altamente acoplados cuando, al cambiar “B”, nos vemos forzados a cambiar “A” si queremos que “A” siga funcionando. Cuantos más cambios haya que hacer en “A”, mayor acoplamiento. Si el acoplamiento es alto, cuando queremos cambiar algo, lo tenemos que cambiar en varios sitios en el código. Esto es malo porque entorpece el mantenimiento debido a que:

- Tardamos más en hacer el mantenimiento, al tener que cambiar el código en muchos sitios
- Al tener que cambiar el código en varios lugares, aumentamos la probabilidad de un error humano (nos podemos equivocar o despistar al cambiar el código en muchos lugares)

Ejemplo: Un programa imprime los 10 primeros números naturales, entre otras operaciones. Podemos dividir el código en al menos tres piezas de software relacionadas entre ellas:

- A: declarar un array de 10 componentes
- B: llenar el array
- C: imprimir el array

![image.png](attachment:35108626-b334-4b39-b8d4-e94b1f99e4c7:image.png)

¿Cuál de los dos programas, divididos cada uno de ellos en tres piezas de software, es mejor desde el punto de vista del principio de mínimo acoplamiento, si no sabemos nada más?

Opcion A ✅:

![image.png](attachment:d43bb1a3-5ef2-46a4-a6a0-b1e5bfc8054d:image.png)

```agda
🔗 Principio de Mínimo Acoplamiento 🔗

El objetivo es que los módulos de un software sean lo menos dependientes posible entre sí, lo que permite:
✅ Mayor mantenimiento 🛠️
✅ Mejor escalabilidad 📈
✅ Código más comprensible 🧠

📌 ¿Qué es el acoplamiento?
Es la interdependencia entre módulos. Un bajo acoplamiento significa que un cambio en un módulo afecta mínimamente a otros.

📌 Ejemplo en UML 📊
En UML, cada pieza de software se representa con un 📦 rectángulo. Si el módulo A necesita que B se ejecute antes, se dibuja una flecha → de A a B.

📌 ¿Por qué evitar el alto acoplamiento? ❌
🔴 Más tiempo en mantenimiento ⏳
🔴 Mayor riesgo de errores 🐛
🔴 Código difícil de modificar 😵‍💫

💡 Mejor opción: módulos independientes y bien estructurados! 🏗️✨
```

### Principio de máxima cohesión

El principio de máxima cohesión establece que los elementos de un módulo, como clases, funciones o métodos, deben estar fuertemente relacionados y enfocados en una tarea o propósito específico. La cohesión se refiere a cómo de estrechamente relacionadas están las responsabilidades de un módulo. Una alta cohesión significa que las tareas realizadas por un módulo son altamente relacionadas y enfocadas. **En resumen: una tarea está muy cohesionada cuando realiza sólo una tarea bien definida, y no varias.** De este modo podremos reutilizar esa pieza en cualquier lugar en donde se necesite justamente esa tarea.

**Ejemplo:** Un programa obtiene, de una base de datos de alumnos, los datos de un alumno concreto con el fin de imprimirlo por pantalla. ¿Cuál de las dos alternativas en pseudocódigo es mejor desde el punto de vista del principio de la máxima cohesión?

![image.png](attachment:987a4615-4e4f-4cea-87be-bb9eed3783e5:image.png)

![image.png](attachment:b42e9bb4-d813-4e5c-b819-372428933333:image.png)

```agda
🎯 Principio de Máxima Cohesión 🎯

📌 ¿Qué significa?
Los elementos de un módulo (clases, funciones o métodos) deben estar fuertemente relacionados y centrados en una sola tarea bien definida.

✅ Alta cohesión significa que el módulo realiza una única tarea de manera clara y eficiente.
❌ Baja cohesión ocurre cuando un módulo realiza varias tareas no relacionadas, lo que dificulta su reutilización y mantenimiento.

💡 Beneficio clave: Módulos reutilizables y fáciles de mantener 🔄🛠️
```

## Patrón modelo vista controlador (MVC)

El patrón **MVC (Modelo-Vista-Controlador)** es un patrón de diseño utilizado comúnmente en el desarrollo de software para aplicaciones. Este patrón divide la aplicación en tres componentes interconectados, lo que facilita la separación de responsabilidades dentro de la aplicación, mejorando así la mantenibilidad, escalabilidad y facilidad para realizar pruebas. Los tres componentes del patrón MVC son:

- **MODELO:** Representa la lógica de negocio y los datos de la aplicación. El modelo es responsable de acceder a la capa de almacenamiento de datos, definir las reglas de negocio, y manipular los datos que se presentan al usuario. No tiene conocimiento directo de la vista o el controlador.
- **VISTA:** Corresponde a la interfaz de usuario. La vista muestra los datos al usuario y envía las acciones del usuario (como clics de botones o entradas de texto) al controlador. Su responsabilidad es presentar los datos proporcionados por el modelo de una manera que sea comprensible y usable por el usuario.
- **CONTROLADOR:** Actúa como intermediario entre la vista y el modelo. Recibe las entradas del usuario a través de la vista, procesa estas entradas (posiblemente actualizando el modelo), y devuelve la salida adecuada a la vista. En resumen, controla la dinámica de cómo la entrada del usuario se convierte en una respuesta en la interfaz.

La principal ventaja del patrón MVC es la separación clara de responsabilidades, lo que facilita la modificación, el mantenimiento y la prueba de las aplicaciones. Por ejemplo, el modelo puede ser modificado sin afectar a la vista, o se puede cambiar la interfaz de usuario sin alterar la lógica de negocio subyacente. Además, este patrón es especialmente útil en equipos donde diferentes desarrolladores o grupos de desarrolladores trabajan en el modelo, la vista y el controlador, respectivamente. En UML se expresaría así:

![image.png](attachment:ad90249a-a14a-4bf1-8bdf-38d4a86a1b3c:image.png)

Nuestros programas tienen que dividirse bien entre ficheros **.h** y .**cpp**:

- **Los archivos .h:** Contienen las declaraciones de clases, atributos y métodos, junto con los comentarios de cabecera.
- **Los archivos .cpp:**Contienen las definiciones de los métodos, junto con los comentarios internos de cada uno (de las variables locales y de las partes complicadas del código).

Además, tendremos que dividir correctamente el programa en clases. El reparto de responsabilidades entre las clases es «natural». Cada clase es un «ser» que hace sólo lo que tiene que hacer ¿Cómo hacerlo bien?

- Primero, ante el enunciado del problema, subrayamos los sustantivos principales. En principio cada uno es una clase.
- Ahora rechazamos las clases que sean demasiado pequeñas (uniéndolas a otras) y rechazamos las clases que sean demasiado grandes (dividiéndolas en clases más pequeñas).

El tamaño de una clase se mide por el número de atributos y métodos que contiene. No debemos olvidar el patrón MVC cada clase debe ser únicamente uno de los tres tipos. Una vez establecidas las clases, hay que dividir correctamente cada clase en métodos siguiendo los principios de máxima cohesión y mínimo acoplamiento.

```agda
🎭 Patrón MVC (Modelo-Vista-Controlador) 🎭

📌 ¿Qué es?
Un patrón de diseño que divide una aplicación en tres componentes interconectados, facilitando la separación de responsabilidades. Esto mejora la mantenibilidad, escalabilidad y facilidad de pruebas.

🔹 MODELO 📊
👉 Gestiona los datos y la lógica de negocio.
👉 Accede a la base de datos y define reglas de negocio.
👉 No interactúa directamente con la vista ni el controlador.

🔹 VISTA 🎨
👉 Se encarga de la interfaz de usuario.
👉 Muestra los datos y envía las acciones del usuario al controlador.

🔹 CONTROLADOR 🎮
👉 Intermediario entre el modelo y la vista.
👉 Recibe las entradas del usuario y actualiza el modelo.
👉 Retorna una respuesta adecuada a la vista.

💡 Ventajas de MVC
✅ Separación de responsabilidades 🚀
✅ Facilita modificaciones sin afectar otros componentes 🔄
✅ Ideal para trabajo en equipo 👥

📂 Organización del código en archivos
🟢 .h (headers): Declaraciones de clases, atributos y métodos.
🔵 .cpp (implementación): Definiciones de métodos y comentarios internos.

🛠️ División correcta en clases
🔍 Pasos:
1️⃣ Identificar los sustantivos clave en el enunciado (posibles clases).
2️⃣ Ajustar clases muy grandes o pequeñas.
3️⃣ Asegurar máxima cohesión y mínimo acoplamiento.

🔥 Regla de oro: Cada clase debe ser Modelo, Vista o Controlador, nunca más de uno. 🚀
```

### Presentación de algoritmos

Debemos seguir las siguientes directrices de buena presentación de los programas:

- Dividir el código en partes lógicas, separadas por líneas en blanco.
- Comentar cada parte lógica al principio de esta diciendo para qué sirve.
- El código debe estar correctamente indentado.
    - El compilador nos puede indentar automáticamente el código.
    - Es aconsejable hacerlo a menudo.
- Uso de precondiciones. Una precondición de un método es una condición booleana que se debe cumplir antes de poder usar (llamar) a dicho método, si queremos que dicho método funcione.
    - Por ejemplo, en el método obtenerAlumno() que vimos en el principio de máxima cohesión, podemos establecer la precondición de que exista dicho alumno que queremos recuperar de la base de datos. La precondición está pensada para que la sepa el usuario del método (el que llama al método), por lo tanto, hay que documentar

La precondición en los comentarios del método, con lenguaje matemático y preciso siempre que sea posible. Le decimos al usuario en qué casos funciona dicho método (cuando se cumple la precondición) y en qué casos no (cuando no se cumple la precondición). Si no se cumple la precondición, el programador no asegura que el método funcione apropiadamente (se lava las manos). El que se cumpla la precondición antes de llamar al método es responsabilidad del usuario de dicho método. De este modo, el método se programa pensando en que la precondición se está cumpliendo esto facilita mucho la programación del método.

- Por ejemplo, obtenerAlumno() no tiene que preocuparse de que el alumno existe en la base de datos. Asume que sí existe. Y esto ayuda a que el método pueda tener máxima cohesión, como veremos posteriormente.

• Al inicio del cuerpo del método, deben también estar programados uno o más métodos “assert()”. El método assert() recibe como parámetro una expresión booleana en C que se evaluará como verdadero o falso. Si se evalúa como verdadero, no se hace nada y el programa continúa. Si se evalúa como falso, se interrumpe automáticamente el programa entero, especificando el assert que lo hizo. Los assert sólo se compilan (y por lo tanto funcionan) cuando compilamos en “modo debug”. Es el modo que utilizamos cuando se está construyendo o probando (versiones alfa o beta) un programa. Una vez que el programa es estable y lo ponemos en producción, compilamos en “modo release”, lo que significa que los asserts no se compilarán, y por lo tanto el programa se ejecutará más rápido. Hay lenguajes (por ejemplo, Eiffel) que siempre compilan los assert, para que el código sea más fiable incluso en producción. 

Consideremos el ejemplo que vimos en el principio de máxima cohesión ponemos la precondición tanto en los comentarios como en los assert() de obtenerAlumno() ¿Quién es el responsable de que la precondición de obtenerAlumno() se cumpla antes de llamar a obtenerAlumno()? El usuario de obtenerAlumno(), que en este caso es el método main(). Si obtenerAlumno() no tuviera la precondición, obtenerAlumno() tendría que comprobar internamente (con un if) que el alumno existe, lo cual:

- Disminuiría la cohesión de obtenerAlumno(), pues ahora este método haría dos tareas: comprobar que el alumno existe, y sacar sus datos de la BD.
- Plantearía nuevos problemas: si no existe el alumno, ¿De qué modo se devuelve un error? El método obtenerAlumno() sólo puede devolver un objeto de tipo “Alumno”, no un error. Podríamos devolver un alumno vacío para indicar error, pero esto es antinatural y además incrementa el acoplamiento, pues el usuario (el método main) tendría que conocer y manejar el hecho de que obtenerAlumno() devuelva un alumno vacío.

![image.png](attachment:36bcbb0d-e4ae-4e57-a188-e04646c5de79:image.png)

```agda
📌 Buenas prácticas en la presentación del código

✅ Estructura clara

📏 Dividir el código en partes lógicas con líneas en blanco.
📝 Comentar cada parte lógica indicando su propósito.
🔄 Indentación correcta (puede hacerse automáticamente con el compilador).
✅ Uso de precondiciones
📌 ¿Qué son?
Una condición booleana que debe cumplirse antes de ejecutar un método.
Ejemplo: 🏫 obtenerAlumno() debe recibir un alumno existente en la base de datos.

💡 Beneficios de usar precondiciones
🚀 Permiten que el método se enfoque en su tarea principal (mayor cohesión).
⚠️ Evitan validaciones innecesarias dentro del método (menor acoplamiento).

✅ Uso de assert()
🔹 Se usa para comprobar precondiciones en tiempo de ejecución.
🔹 Si la condición es falsa ❌, el programa se detiene e informa el error.
🔹 Solo se compila en modo debug, por lo que no afecta el rendimiento en producción.

🎯 ¿Quién debe verificar la precondición?
💡 El usuario del método (por ejemplo, main()).
Si obtenerAlumno() validara la existencia del alumno internamente, tendría que manejar errores y devolver un valor especial (como un alumno vacío), lo que incrementa el acoplamiento innecesariamente.

🔹 En resumen:
✅ Código más limpio y modular 🏗
✅ Métodos más cohesivos y eficientes ⚡
✅ Menos errores en producción 🔥
```

# Algoritmos y estrucutras de datos

La definición clásica de algoritmo lo describe como un método o proceso para resolver un problema generalmente iterativo, bien sea a mano o a través de un computador. Para ello, se aplican un conjunto de reglas objetivas (no subjetivas) para efectuar algún cálculo bien sea a mano, o a través de un computador. Generalmente se aplican sobre un conjunto de datos, relacionados entre sí, que tienen un propósito y uso común, lo que conocemos como estructura de datos. Una estructura de datos viene siempre acompañada por varios algoritmos para manipularla. Por ejemplo, una clase es una estructura de datos (conjunto de sus atributos) más los algoritmos para manipularla (conjunto de métodos).

Existen multitud de algoritmos ya conocidos para la manipulación d ellos datos, lo que ha hecho que surjan diferentes clasificaciones. Según la clasificación más extendidas, tenemos los siguientes tipos de algoritmos de manipulación de estructuras de datos:

- **De creación de la estructura de datos:** Es lo que comúnmente se llama “Constructor”.
- **De creación de un nuevo racional a partir de otros racionales:** Por ejemplo: sumar, multiplicar…
- **De obtención de información de la estructura:** Por ejemplo: getNumerador, getDenominador
- **De modificación de la estructura:** Por ejemplo: hacer una simplificación
- **De conexión con una interfaz:** Por ejemplo, escribir (en pantalla). OJO: Que un algoritmo de manipulación de estructura de datos printe algo viola los principios de separar interfaz del modelo, por lo cual una estructura de datos no debería incluir este tipo de algoritmos de conexión con la interfaz, pero es solo un ejemplo. En su lugar, otras clases o métodos (ej: main) se encargarían de esto. Por ejemplo, una solución para escribir por pantalla el racional sería que el método main pidiera el numerador y el denominador a un objeto de la clase Racional, y a continuación el main imprima estos datos por pantalla según un determinado formato.

```agda
🔍 Definición de Algoritmo:
Un algoritmo es un método o proceso diseñado para resolver un problema de manera sistemática, aplicando un conjunto de reglas objetivas. Estos pueden ejecutarse manualmente o a través de un computador.

🔗 Relación con las Estructuras de Datos:
Una estructura de datos es un conjunto de datos relacionados entre sí, organizados para facilitar su uso y manipulación. Toda estructura de datos está acompañada de algoritmos que permiten realizar diversas operaciones sobre ella.

Ejemplo:
🔹 Una clase es una combinación de:
- Atributos (estructura de datos)
- Métodos (algoritmos para manipular los datos)

🏷 Clasificación de los Algoritmos de Manipulación de Estructuras de Datos:
1️⃣ Creación de la estructura de datos
Se encarga de inicializar una estructura de datos. Es comúnmente conocido como constructor en programación orientada a objetos.

2️⃣ Creación de un nuevo objeto a partir de otros
Permite generar una nueva instancia de una estructura de datos combinando o transformando otras.
Ejemplos comunes incluyen operaciones matemáticas como suma, multiplicación o combinación de datos.

3️⃣ Obtención de información de la estructura
Se utilizan para acceder a los datos almacenados dentro de la estructura sin modificarlos.
Por ejemplo, en una estructura que representa un número racional, podríamos obtener su numerador o denominador sin alterarlos.

4️⃣ Modificación de la estructura
Son algoritmos que cambian el estado de la estructura de datos, ajustando sus valores internos.
Un ejemplo sería simplificar una fracción, modificar atributos o cambiar el orden de los elementos en una lista.

5️⃣ Conexión con una interfaz
Permiten que los datos de la estructura sean utilizados en otros sistemas o mostrados al usuario.
🚨 Advertencia: En el diseño de software, se recomienda separar la manipulación de datos de la interfaz.
Una estructura de datos no debería incluir funciones para imprimir información; en su lugar, otros métodos o clases (como el main) deberían encargarse de esta tarea.

✅ Los algoritmos permiten la manipulación eficiente de estructuras de datos.
✅ Clasificar correctamente los algoritmos facilita la organización del código.
✅ La separación entre datos y su representación es clave para un diseño limpio y escalable. 🚀
```

### Eficiencia de un algoritmo

Un algoritmo es más eficiente cuantos menos recursos (tiempo y memoria) emplee para la resolución de su tarea, en relación con el tamaño de sus datos de entrada. Los ordenadores son cada vez más potentes, ¿por qué entonces importa tanto la eficiencia? Las ambiciones crecen más rápido que la potencia del hardware, los problemas a resolver son cada vez más complejos. Por ejemplo, cuanto más ancho de banda y rapidez tenemos en Internet, más vídeos y de más calidad vemos. Si el algoritmo es ineficiente, aumentar la velocidad del ordenador no es muy significativo en cuanto a la reducción de tiempo.

La eficiencia de los programas no debería entrar en conflicto con los principios de la Ingeniería del Software. Los programas deben seguir siendo legibles y bien estructurados, siguiendo máxima cohesión y mínimo acoplamiento. Ahorrar algunas variables no hace mucho más eficiente el algoritmo, pero sí disminuye mucho la legibilidad. Igualmente, poner menos líneas de código y hacerlas más densas disminuye mucho la legibilidad, pero no aumenta sustancialmente la eficiencia.

El tiempo de ejecución de un programa depende de:

- La calidad del algoritmo.
- La potencia del hardware.
- El tamaño y la complejidad de los datos de entrada.

Respecto a la complejidad de los datos:

- No es lo mismo ordenar un vector ya ordenado (caso mejor), uno invertido (caso peor) o uno aleatorio (caso medio).
- Si no se especifica, se calcula la eficiencia en el **caso peor**.
- Para el **caso medio**, se requiere conocer la probabilidad de cada entrada, lo que no siempre es posible.

```agda
🚀 ¿Por qué es Importante la Eficiencia?
Un algoritmo se considera más eficiente cuando consume menos recursos (tiempo y memoria)
en relación con el tamaño de los datos de entrada. Aunque el hardware mejora constantemente,
las necesidades computacionales crecen aún más rápido.

Ejemplo:
📡 Cuanto mayor es el ancho de banda y la velocidad de Internet, más contenido multimedia de alta calidad consumimos.
📈 Un algoritmo ineficiente seguirá siendo lento, sin importar cuán potente sea el hardware.

⚖ Balance entre Eficiencia y Buenas Prácticas
✏ Optimizar no debe comprometer la legibilidad del código.

Evitar código denso e ilegible: Reducir líneas no siempre mejora la eficiencia, pero sí dificulta el mantenimiento.
Cohesión y acoplamiento: Un código bien estructurado facilita optimizaciones futuras sin afectar su funcionalidad.
Evitar micro-optimizaciones innecesarias: Ahorrar unas pocas variables rara vez tiene impacto significativo en el rendimiento.

⏳ Factores que Afectan el Tiempo de Ejecución
1️⃣ Calidad del Algoritmo: Algoritmos bien diseñados pueden mejorar el rendimiento exponencialmente.
2️⃣ Potencia del Hardware: Una mejor CPU/GPU ayuda, pero no compensa un algoritmo deficiente.
3️⃣ Tamaño y Complejidad de los Datos de Entrada:

Caso Mejor: Datos ya ordenados → el algoritmo trabaja más rápido.
Caso Peor: Datos en el peor estado posible → el tiempo de ejecución aumenta.
Caso Medio: Se calcula con probabilidades, pero no siempre es predecible.
📌 Si no se especifica, se asume el caso peor para garantizar la eficiencia en el peor escenario posible.
```

### ¿Como decidir el mejor algoritmo?

Para un mismo problema es posible que haya disponibles varios algoritmos para resolverlo… ¿cuál elegimos? Pues:

- Si solamente tenemos que resolver uno o dos casos pequeños de un problema más bien sencillo, o bien el programa se va a ejecutar pocas veces, podríamos seleccionar el algoritmo más sencillo de programar, o aquél para el que ya exista un programa.
- Pero si tenemos que resolver muchos casos, o el problema es difícil, o el tamaño de la entrada puede llegar a ser muy grande, tendremos que seleccionar de forma más cuidadosa, **generalmente el más eficiente.**
- Un algoritmo complicado puede no ser conveniente si se necesita mantenimiento (algo que casi siempre ocurre.
- En los algoritmos numéricos (por ejemplo, calcular una integral), la precisión es más importante que la eficiencia.
- Si reducir tiempo y reducir memoria entran en contradicción, elegiremos de forma general el reducir tiempo a costa de aumentar la memoria.

# **Enfoques de decisión**

A la hora de decantarse por una solución, es muy importante pensar en el enfoque que vamos a usar como programadores. Principalmente existen dos:

**Enfoque empírico o «a posteriori»**

- Consiste en programar en la misma máquina los diferentes algoritmos candidatos y elegir el que menos tiempo o memoria gaste. No es un enfoque muy adecuado porque:
    - Requiere un esfuerzo de programación.
    - Lo ideal sería que pudiéramos elegir sólo con el pseudocódigo, sin necesidad de programar nada.
    - La ejecución de los algoritmos puede durar mucho.
    - Incluso la misma máquina nos puede dar distintos resultados según su carga actual, si estamos en un entorno multitarea.

**Enfoque teórico «a priori»**

- Determinar matemáticamente la cantidad de recursos necesarios para el algoritmo como función del tamaño de los casos de entrada.
    - La ventaja es que no depende de la computadora que se use, ni del lenguaje de programación, ni de las habilidades del programador.
    - **A partir de ahora nos centraremos en este enfoque.**

```agda
⚖ Factores a Considerar:
Casos Pequeños: Si solo necesitas resolver uno o dos casos sencillos, elige el algoritmo más sencillo de implementar o uno que ya esté disponible.
Casos Muchos o Problemas Complejos: Si se deben resolver múltiples casos o el tamaño de la entrada es grande, es fundamental optar por un algoritmo más eficiente.
Mantenimiento:

Un algoritmo complejo puede ser difícil de mantener, lo que puede ser problemático a largo plazo. La facilidad de mantenimiento debe ser parte de la decisión.
Precisión vs. Eficiencia:
En problemas numéricos (como el cálculo de integrales), la precisión es más importante que la eficiencia.
Compromiso entre Tiempo y Memoria:

Si se presentan conflictos entre reducir el tiempo de ejecución y la memoria utilizada, es común priorizar la reducción del tiempo a costa de un mayor uso de memoria.

🛠 Enfoques de Decisión:
1. Enfoque Empírico o "A Posteriori"
Consiste en implementar diferentes algoritmos y medir su rendimiento en la misma máquina. Sin embargo, presenta desventajas:
Esfuerzo Adicional: Requiere tiempo y esfuerzo para programar y ejecutar.
Inconveniente en la Elección: Lo ideal sería decidir solo con pseudocódigo.
Variabilidad de Resultados: La carga del sistema y el entorno multitarea pueden afectar los resultados.
2. Enfoque Teórico "A Priori"
Se basa en determinar matemáticamente los recursos necesarios para un algoritmo en función del tamaño de los datos de entrada.
Independiente de Factores Externos: No depende del hardware, del lenguaje de programación ni de la experiencia del programador.
Preferido para Análisis: Este enfoque es más confiable y permite una evaluación más objetiva de la eficiencia del algoritmo.
```

## Definición de la función de Tiempo T(n)

Una vez que sabemos que vamos a necesitar un enfoque teórico para programar en esta asignatura, ya siempre tendremos que andar calculando la eficiencia de nuestros programas. Entonces tendremos que aprender una serie de herramientas matemáticas que nos ayudarán a tomar decisiones. Una de las más importantes, es la que nos permite calcular el tiempo que consume un algoritmo en función de su entrada, la Funcion de TIempo T(n). 

La función de tiempo de un algoritmo es una **expresión matemática** que describe la cantidad total de tiempo que tarda un algoritmo en ejecutarse en función del tamaño de su entrada. Esta función es fundamental para el análisis de algoritmos, ya que proporciona una medida cuantitativa de la eficiencia de un algoritmo en términos de tiempo. La función de tiempo se centra en cómo el tiempo de ejecución del algoritmo aumenta con el aumento del tamaño de la entrada. En todos los casos, T(n) > 0 para todo valor de n, ya que un algoritmo no puede tardar un tiempo negativo en ejecutarse.

- Es habitual que un algoritmo en diferentes ejecuciones tenga diferentes rendimientos (por ejemplo, porque hay una bifurcación que en una condición es muy leve y en la otra muy pesada). En ese caso siempre nos quedamos con el caso peor, y para ello, deberemos tener en cuenta la máxima complejidad de la entrada.
- El tiempo no será “exacto”, ni será medido en segundos u otras medidas, sino que es un cálculo “a priori”. Entonces, no es necesario programar ni ejecutar el algoritmo para demostrarlo.

En el contexto de la eficiencia de algoritmos, una "operación elemental" se refiere a una operación básica que el procesador puede realizar en un tiempo constante, es decir, el tiempo que toma realizar la operación no depende del tamaño de los datos de entrada. Estas operaciones son fundamentales para entender cómo se evalúa la eficiencia de un algoritmo, especialmente en términos de tiempo de ejecución. 

Una operación elemental es típicamente una operación que no requiere de un proceso complejo o de múltiples pasos para ser completada por la CPU.  Matemáticamente, cada **operación elemental tiene un T(n)=1.**

**Las operaciones elementales suelen ser de muchos tipos:**

- Sumas, restas, multiplicaciones, divisiones o módulos
- Operaciones booleanas
- Comparaciones
- Asignaciones a variables a posiciones de un array
- Leer de una variable o posición de un array
- Bucles
- Decisiones
- Saltos en el código
- Llamadas a funciones
- Declaraciones
- Reservas de trozos de memoria de cualquier tamaño (malloc, new) …

### Cálculo general de T(n)

Cuando tenemos varias líneas de código seguidas en un bloque, primero se calculan los T(n) individuales de cada línea, y después se suman todos los T(n) para obtener el T(n) del algoritmo completo. En el resultado, si tenemos alguna constante mayor que 1, se cambia por 1.

¿Cómo quedaría el T(n) en este fragmento considerando los T(n) individuales de cada línea?

![image.png](attachment:188f0e1d-cc61-4d96-a2d0-44e5bc249336:image.png)

Solución: T(n)=5n2+3n+10log(n)+1

### Cálculo de T(n) de una condición

El **T(n) de una condición** es el T(n) de la condición más el mayor de los T(n) de cada alternativa (cuando n es muy grande) más **1**.

- Escogemos el T(n) más grande de las alternativas porque recordemos que estamos midiendo T(n) para el peor caso.
- El 1 es por el salto que implica cualquiera de las dos alternativas. Si se ejecuta el “if”, al terminar hay que saltar hasta el final del “else”. Si se ejecuta el “else”, es necesario saltar hasta él desde la línea en donde está la evaluación de la condición.

Ejemplo: 

```cpp
if (funcionCOmpleja(n) == a*b) 
{
	intruccionCompleja2(n); 
	instruccionCompleja3(n); 
	int j = 10*a+b; 
} else {
		instruccionCompleja1(n); 
		int i = 5 + 10; 
}
```

- Condición tiene T(n) = n+1
- Bloque “if” tiene T(n) = 2n+10log(n)+1
- Bloque “else” tiene T(n) = 5n2+1. Su curva es más grande que el T(n) del “if” cuando n es muy grande
- Por lo tanto, el T(n) total del algoritmo es el T(n) de la evaluación de la condición sumado al T(n) del else (peor caso) más 1. Será entonces T(n) = 5n2+n+1.

En los **bucles while** se siguen los siguientes pasos:

1. Multiplicar las vueltas que da el bucle en el peor caso por la suma de la T(n) de la evaluación, la T(n) de cada iteración, y un 1 por el salto hasta la línea en donde está la condición inicial para volver a evaluarla.
2. Finalmente se suma 1 por el salto desde la línea en donde está la condición que no se cumple hasta el final del while, para seguir ejecutando las instrucciones que haya después del bucle.

```cpp
while (i < n)
{
	intruccionCompleja2(n); 
	instruccionCompleja1(n);
	i++; 
}
```

- La condición es T(n)=1 porque es una comparación
- Cada iteración es T(n)=5n2+2n+10log(n)+1 (incluyendo el salto hasta el inicio)
- Se ejecutan n iteraciones siempre
- Por lo tanto, el total es T(n)=5n3+2n2+10nlog(n)+n+1

Un bucle “do-while” se puede convertir en un bucle “while”, con propósitos de evaluarlo:

![image.png](attachment:fec521a2-0fe7-4e0c-940c-1c79c3df62ef:image.png)

### Cálculo de T(n) en funciones

En general, la función de tiempo de un algoritmo se calcula en función de todos aquellos parámetros que vemos que influyen en su tiempo de ejecución. Tendremos que deducir en cada caso qué parámetros influyen y cuáles no.

**Veamos los casos más comunes que vamos a encontrar:**

- Llamar a una función implica un salto hasta el lugar de la memoria en donde empiezan sus instrucciones. Este salto es una operación elemental y se computa en el bloque desde el que se llama a la función.
- Cuando la función termina, hay un salto hasta el lugar del código desde que se llamó a la función. Este salto es otra operación elemental y se computa cuando calculamos el T(n) interno de la función.
- Al comienzo de la función, se declaran los parámetros formales y se copia en ellos los parámetros reales con los que la función se llama realmente en ese caso. Esto también son operaciones elementales.
- Las declaraciones y las copias generalmente serán operaciones elementales, aunque podría no ser así si los parámetros son objetos complejos con constructores y constructores de copia complicados, los cuales podrían tener un tiempo de ejecución que dependiera de n.
- Igualmente, cuando la función devuelve un valor, realmente el valor se copia y es esta copia la que se devuelve. Como antes, la copia será casi siempre una operación elemental, pero podría no ser así si implica una copia de un objeto complejo.

En algunos casos es posible calcular la función de tiempo en función de varios parámetros en vez de uno solo (por ejemplo, T(a,b) = 5a3+2b2+10blog(n)+ab+a+1). Las reglas en este caso son las mismas que hemos visto antes.

## Orden de un algoritmo

El orden de un algoritmo es su consumo “a priori” de tiempo o de memoria adicional en función del tamaño de los operandos, poniéndonos en el caso peor.

Como ejemplo, lo que tarda un algoritmo de ordenación, en función del tamaño del vector a ordenar, cuando dicho vector a ordenar está justamente ordenado al revés (caso peor). Además, calculamos su consumo de tiempo cuando el tamaño de los operandos es muy grande o tiende a infinito. Cuando el tamaño de los operandos es pequeño, hemos dicho que nos da igual escoger un buen o mal algoritmo. Además, nos interesa pensar en operandos grandes porque hemos dicho que los problemas son cada vez más complejos. Denominaremos T(n) al tiempo de ejecución de un programa con una entrada de tamaño n, en el caso peor en cuanto a complejidad de la entrada ¿Qué T(n) son más grandes (y por lo tanto peores) cuando “n” es grande?

A continuación, se muestra una lista, ordenada de los T(n) más rápidos a los más lentos:

![image.png](attachment:01089825-57d1-4df1-bdf4-ea82289c43f1:image.png)

Según vimos, si el algoritmo es ineficiente, aumentar la velocidad del ordenador no es muy significativo en cuanto a la reducción de tiempo.

Decimos que el **“orden de un algoritmo**” es el orden de su T(n). La constante multiplicativa del término mayor de una T(n) nunca puede ser negativa, pues entonces el algoritmo tardaría un tiempo negativo al tender n a infinito. Si el orden de una T(n) de un algoritmo es una función g(n), decimos que el algoritmo es de orden temporal O(g(n)) (asumiendo que T(n) E O(g(n))). También podemos decir que el algoritmo tiene una complejidad computacional en tiempo de O(g(n)), o de forma resumida podemos decir que la complejidad temporal del algoritmo es O(g(n)). O(g(n)), matemáticamente, es el conjunto de funciones cuyo orden es g(n). Por eso decimos que T(n) E O(g(n)). Veamos algunos ejemplos:

- **Ejemplo 1:** Si tenemos un algoritmo con T(n) = log(n)+3n2+8n3+1, decimos que su complejidad temporal es O(n3)
- **Ejemplo 2:** Si tenemos un algoritmo con T(n) = log(n)+3n2-8n3+8·22n+1, decimos que su complejidad temporal es O(4n).
- **Ejemplo 3:** Si tenemos un algoritmo con T(n) = 1, entonces decimos que su complejidad temporal es O(1).

La “implementación de un algoritmo” es llevarlo a un lenguaje, sistema operativo y máquina concreta. Definición del “Principio de invarianza”:

- Los valores de las constantes de T(n) sólo dependen de la implementación del algoritmo, y no del algoritmo en sí mismo
- Estas constantes se llaman “constantes ocultas”, porque son despreciables en el infinito y por lo tanto no nos interesan, por lo tanto no aparecen en el O(…), están “ocultas”. Por lo tanto, ¿en qué influye mejorar la implementación (por ejemplo, mejorar el hardware)?
    - Obviamente nos permite resolver un problema más rápido, pues las constantes son menores.
    - Sin embargo, cuando n es muy grande o tiende a infinito, sabemos que las constantes son despreciables, y que por lo tanto la implementación concreta es despreciable.

### Ejemplos de orden temporal

**Cálculo de determinantes**

- Basado en el teorema de Laplace: O(n!)
- Por eliminación de Gauss-Jordan: O(n) (muchísimo mejor)
    
    3
    

**Ordenación**

- Algoritmo de selección: O(n)
    
    2
    
- Algoritmo QuickSort: O(n·logn)
- Si los componentes del vector están acotados: O(n)

**Operaciones matemáticas**

- Multiplicar dos números muy grandes (de “m” y “n” cifras respectivamente): O(m·n)
- Sucesión de Fibonacci (0,1,1,2,3,5,8,13,21…): O(i) si se quiere calcular el elemento i-ésimo
- Transformada de Fourier (típico algoritmo que se usa constantemente para telecomunicaciones e inteligencia artificial):
    - Algoritmo clásico: O(n)2
    - Transformada rápida de Fourier: O(n·logn)
    - En algunos casos particulares, se llega a la increíble O(n/logn)

## Complejidad espacial

Hasta ahora hemos calculado la complejidad temporal de un algoritmo, es decir, el tiempo que tarda cuando el tamaño de su entrada tiende a infinito, pero no podemos olvidar el otro gran recurso (aunque sea menos importante que el tiempo) por el cual se mide la eficiencia de los algoritmos: la memoria que se usa. Se dice que un algoritmo tiene complejidad computacional en memoria (también llamado “complejidad espacial”) de O(g(n)), si su T(n), midiendo la cantidad de memoria adicional, es de orden g(n). 

La memoria adicional es la memoria extra máxima que el algoritmo necesita en algún momento de su ejecución. En “extra” no incluimos la memoria que, de por sí, ocupan los parámetros inicialmente. Tampoco incluimos la memoria que ocupe el objeto sobre el que se llama al algoritmo, en el momento inicial del mismo. Por lo tanto, el constructor de una clase VectorEnteros tendría una complejidad espacial de O(n), pues el array interno de VectorEnteros no existía al empezar a ejecutar el constructor.

La memoria adicional, al igual que el tiempo, se mide en función del tamaño de los parámetros, y también se puede calcular en el caso mejor, peor y medio. Veamos un par de ejemplos:

- **Ejemplo 1:** Los algoritmos de ordenación por inserción o selección no necesitan memoria adicional, por lo tanto son O(1) en memoria.
- **Ejemplo 2:** Si tenemos un algoritmo de ordenación (vector de tamaño n) que crea internamente otro array de tamaño n y va poniendo en él sucesivamente los mínimos encontrados en el vector pasado como parámetro, tiene O(n) en memoria adicional.

Una vez calculado un T(n) de memoria adicional, el cálculo de su O(…) y las operaciones con O(…) se realizan igual que con la complejidad temporal.