# Unidad 2 - Introducción a JS 

JavaScript es un lenguaje de programación de alto nivel que permite agregar interactividad a las páginas web. A través de JavaScript, podemos manipular el Document Object Model (DOM), gestionar eventos de usuario, realizar validaciones de formularios, crear animaciones y mucho más. Es el motor detrás de las aplicaciones web dinámicas y una habilidad esencial para cualquier desarrollador web.

## Breve Historia de Javascript

JavaScript  es un lenguaje de programación que ha evolucionado desde su creación y que tiene mucha importancia en el desarrollo web. Creado por Brendan Eich en mayo de 1995, mientras trabajaba en Netscape Communications Corporation. Originalmente, desarrollado en solo 10 días y fue lanzado con el nombre de Mocha. 

Poco después, fue renombrado a LiveScript y finalmente a JavaScript en  diciembre de 1995. Este cambio de nombre fue parte de una estrategia de 
marketing para capitalizar la popularidad de Java, otro lenguaje de programación muy conocido en ese momento.

Desde su lanzamiento, JavaScript ha pasado por varias fases de evolución que han ampliado sus capacidades y mejorado su rendimiento: 

- Estandarización (1996-1999)
    - En 1996, JavaScript fue estandarizado por Ecma International bajo el nombre de ECMAScript.
    - ECMAScript 1 fue lanzado en 1997, proporcionando una base estándar para el lenguaje.
- Mejoras Iniciales y ECMAScript 3 (1999)
    - ECMAScript 3, lanzado en 1999, introdujo mejoras significativas como expresiones
    regulares, manejo de excepciones y funciones de formato de cadena
- Crecimiento y Popularidad (2000-2008)
    - Durante estos años, JavaScript se consolidó como el lenguaje principal para el
    desarrollo de scripts del lado del cliente en navegadores web.
    - Surgieron bibliotecas y frameworks populares como jQuery, que simplificaron la manipulación del DOM y la gestión de eventos.
- Revolución con ECMAScript 5 (2009)
    - ECMAScript 5 introdujo características como el modo estricto, los métodos de
    objetos nativos, y la definición de propiedades de objetos, mejorando la seguridad y el manejo de errores en JavaScript
- Moderno JavaScript: ECMAScript 6 y más allá (2015-presente)
    - ECMAScript 6 (ES6), también conocido como ECMAScript 2015, marcó una revolución en el lenguaje con la introducción de características como las clases, los módulos, las funciones flecha, let y const.
    - Desde entonces, se han lanzado actualizaciones anuales (ES2016, ES2017,
    etc.), añadiendo nuevas características como async/await, objetos de
    tipo mapa y conjuntos, y mejoras de rendimiento.

JavaScript  es popular en el desarrollo web debido a su interactividad ya que permite a los desarrolladores crear interfaces de usuario interactivas y  dinámicas. Es posible actualizar el contenido de una página web en tiempo real sin necesidad de recargar la página completa. JavaScript también se ejecuta en todos los navegadores actuales, lo que lo convierte en una buena opción para el desarrollo de aplicaciones web que funcionen en diversas plataformas y dispositivos.

# Características del lenguaje JavaScript

A  continuación, se describen las principales características que definen a
 JavaScript y que lo hacen populares en el desarrollo web:

- Es un lenguaje interpretado, lo que significa que el código se ejecuta 
línea por línea en lugar de ser compilado en un archivo binario antes de
 su ejecución. Esto permite una mayor flexibilidad y facilita la 
depuración del código, ya que los errores se pueden identificar y 
corregir rápidamente durante la ejecución.
- Las variables no tienen un tipo fijo. Esto se conoce como 
tipado dinámico o débilmente tipado. Una variable en JavaScript puede 
contener diferentes tipos de datos a lo largo de su ciclo de vida. Por 
ejemplo, una variable que inicialmente contiene un número puede 
posteriormente almacenar una cadena de texto sin necesidad de declarar 
un nuevo tipo.
- Está basado en objetos, lo que significa que utiliza objetos como bloques de construcción para la mayoría de las funcionalidades. Sin embargo, no es puramente orientado a objetos como lenguajes como Java o C++. Los objetos en JavaScript son colecciones de propiedades y métodos, y se pueden crear de manera literal o mediante constructores.
- Aunque JavaScript es más conocido por su uso en el desarrollo web, es un lenguaje de propósito general. Se puede utilizar para una amplia 
variedad de aplicaciones.
- Se ejecuta principalmente en el entorno del navegador web, lo que 
permite manejar eventos del usuario, validar formularios y realizar 
comunicaciones asincrónicas con el servidor.
- La sintaxis de JavaScript es similar a la de lenguajes como C y Java, lo 
que facilita su aprendizaje para desarrolladores que ya están 
familiarizados con estos lenguajes.
- Es conocido por su modelo de programación basado en eventos, lo que 
significa que puede responder a acciones del usuario, como clics de  ratón, pulsaciones de teclas y eventos de temporización. Además, 
JavaScript soporta operaciones asincrónicas, lo que permite manejar 
tareas como solicitudes de red sin bloquear la ejecución del programa.
- JavaScript cuenta con una comunidad de desarrolladores y un ecosistema de bibliotecas y frameworks. Además, existen muchos recursos online, como documentación, tutoriales y foros, que apoyan el aprendizaje y la resolución de problemas.

## Sintaxis del lenguaje

La sintaxis de JavaScript es el conjunto de reglas que define cómo se debe escribir el código en este lenguaje de programación. A continuación, se describen los aspectos fundamentales de la sintaxis de JavaScript.

- **Sensible a Mayúsculas y Minúsculas:** JavaScript  distingue entre mayúsculas y minúsculas (es case sensitive). Esto 
significa que las variables `variable`, `Variable` y `VARIABLE` se 
consideran distintas entre sí.
- **Declaración de Variables:** Las variables en JavaScript se pueden declarar utilizando las palabras clave ‘var’, ‘let’ y ‘const’.
- **Palabras reservadas:** En JavaScript tenemos las siguientes palabras reservadas:
    
    ![image.png](attachment:5402045d-17ea-4d7a-bee1-d6ef900062a2:image.png)
    

### Tipos de datos en JavaScript

JavaScript  maneja varios tipos de datos, que se dividen principalmente en dos categorías: tipos de datos primitivos y objetos. Entender estos tipos de datos es fundamental para trabajar de manera efectiva con JavaScript. A continuación, se describen los tipos de datos más importantes en JavaScript.

- **Tipos de Datos Primitivos:** Los tipos de datos primitivos son los más básicos y se accede a ellos directamente. Los principales tipos de datos primitivos en JavaScript son los siguientes: Número, String, boolean, Null e indefinido.
- **Objetos:** Los objetos son estructuras complejas de datos que pueden contener colecciones de valores de distintos tipos, incluidos otros objetos. Los objetos se crean utilizando la sintaxis de llaves `{}` y pueden tener 
propiedades y métodos.

JavaScript permite la conversión entre diferentes tipos de datos. Esta conversión puede ser implícita o explícita.

- Implicita: convierte automáticamente los tipos de datos según sea necesario.
- Explicita: Utilizando funciones como `Number()`, `String()`, y `Boolean()`.

### Operadores

| **Tipo de operador** | **Descripción** |
| --- | --- |
| **Operadores de asignación** | Asignan valores a las variables (ej.: `=`, `+=`, `-=`, `*=`). |
| **Operadores aritméticos** | Realizan operaciones matemáticas (ej.: `+`, `-`, `*`, `/`, `%`, `**`). |
| **Operadores de comparación** | Comparan valores y devuelven un booleano (ej.: `==`, `===`, `!=`, `>`, `<`). |
| **Operadores lógicos** | Realizan operaciones lógicas y devuelven un booleano (ej.: `&&`, ` |
| **Operadores de tipo** | Devuelven el tipo de dato de una variable (ej.: `typeof`, `instanceof`). |
| **Operadores bit a bit** | Operan a nivel de bits de los números (ej.: `&`, `) |

## Control de Flujo y Funciones de JS

### Condicionales

Los condicionales permiten ejecutar código según si se cumple o no una condición. Los más usados son `if`, `else if`, `else` y `switch`.

- **if / else if / else**: ejecutan bloques de código según una condición booleana.

```jsx
let edad = 20;
if (edad < 18) {
    console.log("Eres menor de edad");
} else if (edad === 18) {
    console.log("Acabas de ser mayor de edad");
} else {
    console.log("Eres mayor de edad");
}
```

**switch**: permite evaluar una variable frente a múltiples valores posibles.

```jsx
let dia = "martes";
switch(dia) {
    case "lunes":
        console.log("Inicio de semana");
        break;
    case "martes":
        console.log("Segundo día");
        break;
    default:
        console.log("Otro día");
}
```

### Bucles

Los bucles se utilizan para repetir un bloque de código mientras se cumpla una condición.

- **for**: repite un número determinado de veces.

```jsx
for (let i = 0; i < 5; i++) {
    console.log("Iteración", i);
}

```

**while**: repite mientras la condición sea verdadera.

```jsx
let i = 0;
while (i < 5) {
    console.log("Iteración", i);
    i++;
}
```

**do...while**: ejecuta al menos una vez y luego verifica la condición.

```jsx
let j = 0;
do {
    console.log("Iteración", j);
    j++;
} while (j < 5);
```

**Sentencias de control de salida**:

- `break` detiene el bucle inmediatamente.
- `continue` salta a la siguiente iteración.

```jsx
for (let i = 0; i < 5; i++) {
    if (i === 3) break;
    if (i === 1) continue;
    console.log(i); // imprime 0, 2
}
```

### Funciones

Las funciones son bloques de código reutilizables que realizan tareas específicas. Se pueden declarar de varias formas:

- **Declaración tradicional:**

```jsx
function saludar(nombre) {
    return "Hola " + nombre;
}
console.log(saludar("Ana"));
```

**Expresión de función:**

```jsx
const multiplicar = function(a, b) {
    return a * b;
};
console.log(multiplicar(2, 3));
```

**Función flecha (ES6):**

```jsx
const sumar = (a, b) => a + b;
console.log(sumar(5, 7));
```

- **Parámetros y argumentos:**
    - Parámetros son las variables que se definen en la función.
    - Argumentos son los valores reales que se pasan al llamar la función.

```jsx
function dividir(a, b) {
    return a / b; // a y b son parámetros
}
console.log(dividir(10, 2)); // 10 y 2 son argumentos
```

**Funciones con valores por defecto:**

```jsx
function saludar(nombre = "Invitado") {
    console.log("Hola " + nombre);
}
saludar(); // Hola Invitado

```

### Algunas funciones y métodos importantes

- **Funciones de interacción con el usuario:**
    - `alert("mensaje")`: muestra un mensaje emergente.
    - `prompt("mensaje")`: pide un dato al usuario y lo devuelve como cadena.
    - `confirm("mensaje")`: devuelve `true` o `false` según la respuesta del usuario.

```jsx
let nombre = prompt("Ingresa tu nombre:");
alert("Hola " + nombre);
```

**Métodos de Strings:**

- `.length`: devuelve la longitud del texto.
- `.toUpperCase()`, `.toLowerCase()`: cambia el caso de las letras.
- `.includes("texto")`: verifica si un texto está contenido.
- `.replace("viejo", "nuevo")`: reemplaza parte del texto.

```jsx
let texto = "Hola Mundo";
console.log(texto.length); // 10
console.log(texto.toUpperCase()); // HOLA MUNDO
console.log(texto.includes("Mundo")); // true
console.log(texto.replace("Mundo", "JS")); // Hola JS
```

**Métodos de Arrays:**

- `.push(elemento)`: agrega al final.
- `.pop()`: elimina el último elemento.
- `.shift()`: elimina el primer elemento.
- `.unshift(elemento)`: agrega al inicio.
- `.forEach(función)`: recorre todos los elementos.
- `.map(función)`: genera un nuevo array aplicando la función a cada elemento.

```jsx
let numeros = [1, 2, 3];
numeros.push(4);
numeros.forEach(n => console.log(n)); // 1 2 3 4
let dobles = numeros.map(n => n * 2);
console.log(dobles); // [2, 4, 6, 8]
```

**Métodos de objetos:**

- `Object.keys(obj)`: devuelve un array con las claves.
- `Object.values(obj)`: devuelve un array con los valores.
- `Object.entries(obj)`: devuelve un array de pares [clave, valor].

```jsx
let persona = {nombre: "Ana", edad: 25};
console.log(Object.keys(persona)); // ["nombre", "edad"]
console.log(Object.values(persona)); // ["Ana", 25]
console.log(Object.entries(persona)); // [["nombre","Ana"],["edad",25]]
```

### Inclusión de JavaScript en una web

- **Interno:** dentro de la etiqueta `<script>` en el HTML.

```jsx
<script>
console.log("JavaScript interno");
</script>
```

**Externo:** archivo `.js` vinculado con `src`.

```jsx
<script src="script.js"></script>
```

# Modelo BOM

El Browser Object Model (BOM) es una representación jerárquica de los objetos proporcionados por el navegador web, que permite interactuar y controlar el entorno del navegador. A través del BOM, los desarrolladores pueden acceder y manipular elementos como la ventana del navegador, la barra de direcciones, el historial, entre otros. Veamos en el video a continuación que es el BOM:

![image.png](attachment:341dd8d5-ad23-41ab-a356-ac1be3959ace:image.png)

### Objeto `window`

El objeto de más alto nivel del BOM que representa la ventana del navegador. Todos los demás objetos del BOM son propiedades del objeto `window`.

### Propiedades importantes

```jsx
console.log(window.innerWidth);   // Ancho del área visible de la ventana
console.log(window.innerHeight);  // Alto del área visible
console.log(window.outerWidth);   // Ancho total de la ventana (barras incluidas)
console.log(window.outerHeight);  // Alto total de la ventana
```

### Métodos importantes

```jsx
alert("Mensaje de alerta");                      // Muestra un cuadro de alerta
let respuesta = confirm("¿Continuar?");         // Devuelve true o false según la opción del usuario
let nombre = prompt("Escribe tu nombre:", "Invitado"); // Devuelve el texto ingresado por el usuario

setTimeout(() => console.log("Hola después de 2s"), 2000); // Ejecuta función una vez después de un retraso
let intervalID = setInterval(() => console.log("Hola cada 3s"), 3000); // Ejecuta función repetidamente
clearInterval(intervalID); // Detiene el setInterval
```

### Objeto `document`

Representa el documento HTML cargado y permite acceder y manipular el contenido de la página

```jsx
console.log(document.title);                   // Título de la página
console.log(document.URL);                     // URL completa
document.body.style.backgroundColor = "lightblue"; // Cambiar color de fondo
let elemento = document.getElementById("miDiv");   // Acceder a un elemento por ID
elemento.innerText = "Hola mundo!";                // Cambiar el texto de un elemento
```

### Objeto `location`

Contiene información sobre la URL actual y permite redirigir el navegador.

```jsx
console.log(location.href);       // URL completa
console.log(location.hostname);   // Nombre del host
console.log(location.pathname);   // Ruta del documento

// Redirigir a otra página
// location.href = "https://www.ejemplo.com";
```

### Objeto `history`

Permite acceder al historial de navegación.

```jsx
history.back();    // Ir a la página anterior
history.forward(); // Ir a la página siguiente
history.go(-2);    // Ir dos páginas atrás
```

### Objeto `navigator`

Proporciona información sobre el navegador y el sistema operativo.

```jsx
console.log(navigator.userAgent); // Información del navegador y sistema
console.log(navigator.platform);  // Sistema operativo
console.log(navigator.language);  // Idioma del navegador
```

### Objeto `screen`

Proporciona información sobre la pantalla del dispositivo.

```jsx
console.log(screen.width);       // Ancho de la pantalla
console.log(screen.height);      // Alto de la pantalla
console.log(screen.availWidth);  // Ancho disponible
console.log(screen.availHeight); // Alto disponible
console.log(screen.colorDepth);  // Profundidad de color en bits
```

## Modelo DOM

El **DOM (Document Object Model)** es una interfaz que permite acceder y manipular el contenido, la estructura y el estilo de los documentos HTML y XML.

El DOM representa el documento como un **árbol de nodos**, donde cada nodo corresponde a una parte del documento.

El nodo raíz del árbol es el objeto `document`. Cada elemento HTML es representado como un nodo en este árbol, permitiendo acceder y modificar cualquier parte del documento.

---

## Métodos para acceder a elementos del DOM

### Obtener por ID

```jsx
let elemento = document.getElementById("miId"); // Devuelve el elemento con el ID especificado

```

### Obtener por clase

```jsx
let elementos = document.getElementsByClassName("miClase"); // Devuelve una colección de elementos
```

### Obtener por etiqueta

```jsx
let parrafos = document.getElementsByTagName("p"); // Devuelve todos los elementos <p>
```

### Selectores CSS

```jsx
let primerElemento = document.querySelector(".miClase");      // Devuelve el primer elemento que coincide con el selector CSS
let todosElementos = document.querySelectorAll(".miClase");   // Devuelve todos los elementos que coinciden con el selector CSS
```

## Métodos para modificar elementos del DOM

### Contenido HTML

```
let div = document.getElementById("miDiv");
div.innerHTML = "<p>Nuevo contenido</p>"; // Modificar contenido HTML
console.log(div.innerHTML);               // Obtener contenido HTML
```

**Atributos**

```jsx
div.setAttribute("data-id", "123"); // Establecer atributo
console.log(div.getAttribute("data-id")); // Obtener atributo
```

**Estilos CSS**

```jsx
div.style.backgroundColor = "lightblue"; // Modificar estilo
console.log(div.style.backgroundColor);  // Obtener estilo
```

### Añadir o elminar nodos

```jsx
// Crear un nuevo elemento y añadirlo como hijo
let nuevoParrafo = document.createElement("p");
nuevoParrafo.textContent = "Hola desde el DOM";
div.appendChild(nuevoParrafo);

// Eliminar un nodo hijo
div.removeChild(nuevoParrafo);
```

## Manejadores de Eventos

Los manejadores de eventos (event handlers) en JavaScript son funciones que se ejecutan en respuesta a eventos específicos que ocurren en el navegador. Los eventos pueden ser acciones del usuario, como hacer clic en un botón, mover el ratón, presionar una tecla, o eventos del navegador, como la carga completa de una página.

### Tipos de Eventos en JavaScript

JavaScript permite manejar numerosos eventos que ocurren en la página web. A continuación se describen los eventos más comunes y su función:

**Eventos de ratón**

- `click`: Se dispara al hacer clic en un elemento.
- `dblclick`: Se dispara al hacer doble clic en un elemento.
- `mouseover`: Se dispara cuando el puntero del ratón entra en un elemento.
- `mouseout`: Se dispara cuando el puntero del ratón sale de un elemento.

**Eventos de teclado**

- `keydown`: Se dispara al presionar una tecla.
- `keyup`: Se dispara al soltar una tecla.
- `keypress`: Se dispara mientras se presiona una tecla (antes de soltarla).

**Eventos de formulario**

- `submit`: Se dispara al enviar un formulario.
- `reset`: Se dispara al restablecer un formulario.
- `change`: Se dispara cuando el valor de un elemento de formulario cambia.
- `input`: Se dispara cada vez que se cambia un valor de entrada.

**Eventos de carga y renderizado**

- `DOMContentLoaded`: Se dispara cuando el HTML se ha cargado y parseado, sin esperar a que se carguen recursos externos como imágenes o hojas de estilo.
- `load`: Se dispara cuando toda la página, incluyendo imágenes, estilos y recursos externos, ha sido completamente cargada.

**Eventos de ventana**

- `resize`: Se dispara al redimensionar la ventana del navegador.
- `scroll`: Se dispara cuando se desplaza la barra de desplazamiento de la ventana o de un elemento.

### Añadir Manejadores de Eventos

Los manejadores de eventos se pueden añadir de varias maneras en JavaScript:

- Mediante atributos: Se puede añadir un manejador de eventos directamente en el HTML mediante atributos como 'onclick', ‘onmouseover', etc. Este método se considera una práctica menos recomendada, ya que mezcla HTML con JavaScript.
- Se puede asignar una función a una propiedad del objeto del evento del elemento.
- Es la forma más recomendada de añadir manejadores de eventos. Permite añadir múltiples manejadores de eventos para un solo evento sin 
sobrescribir los existentes y proporciona mayor control sobre el evento.

### Propagación y Manipulación de Eventos en JavaScript

La **propagación de eventos** se refiere a cómo los eventos se distribuyen a través del DOM. Existen dos fases principales:

- Primero, el evento se propaga desde el **nodo más externo** del DOM hacia el **nodo objetivo**.
- Después de que el evento alcanza el nodo objetivo, se propaga de vuelta hacia el **nodo más externo**.

El método `addEventListener` permite especificar si el manejador de eventos debe ejecutarse durante la **fase de captura** o la **fase de burbuja**, utilizando un tercer argumento booleano. Por defecto, los eventos se manejan en la **fase de burbuja**.

---

### Prevención y manipulación de eventos

JavaScript permite **controlar el comportamiento de los eventos** mediante métodos específicos:

- **Prevenir el comportamiento predeterminado**: útil para evitar que, por ejemplo, un formulario se envíe o un enlace sea seguido automáticamente.
- **Detener la propagación del evento**: se utiliza para evitar que un evento active múltiples manejadores en los elementos parent, controlando así cómo se propaga a través del DOM.

Estos mecanismos permiten un control más fino sobre la interacción del usuario y el flujo de eventos en la página.

## Formularios

Un **formulario web** está compuesto por varios elementos que permiten al usuario introducir datos. Los formularios se utilizan junto con JavaScript para validar, enviar y manipular la información ingresada.

---

### Elementos y atributos principales de un formulario

- **`<form>`**: Define el formulario HTML. Debe contener todos los elementos de entrada y debe incluir los atributos **`action`** y **`method`**.
- **`action`**: Especifica la URL a la que se enviarán los datos del formulario.
- **`method`**: Define el método HTTP que se usará al enviar los datos (**GET** o **POST**).

---

### Elementos de entrada

- **`<input>`**: Se utiliza para crear varios tipos de campos de entrada. El atributo **`type`** especifica el tipo de entrada (texto, contraseña, correo electrónico, número, etc.).
- **`<label>`**: Proporciona una etiqueta para los elementos de entrada. Asociar un `<label>` con un `<input>` usando el atributo **`for`** mejora la accesibilidad.
- **`<textarea>`**: Crea un área de texto de varias líneas.
- **`<button>`**: Crea un botón que envía el formulario o realiza otras acciones.
- **`<select>`**: Crea una lista desplegable de opciones.

---

### Atributos importantes de los elementos de formulario

- **`type`**: Define el tipo de dato que el campo de entrada aceptará (texto, número, correo electrónico, fecha, etc.).
- **Otros atributos comunes**:
    - `name`: Nombre del campo, usado para enviar los datos.
    - `value`: Valor predeterminado del campo.
    - `required`: Indica que el campo es obligatorio.
    - `placeholder`: Texto que aparece como guía en el campo.