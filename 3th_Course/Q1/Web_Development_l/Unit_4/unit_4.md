# JQuery

Creado: 18 de diciembre de 2025 10:17

![image.png](unit_4/image.png)

## **Introducción**

Desde su lanzamiento en 2006 por John Resig, jQuery se popularizó porque soluciona muchos problemas de compatibilidad entre navegadores, permitiendo escribir un mismo código que funcione correctamente en todos ellos. Además, se apoya en la idea de *“escribir menos, hacer más”*, ya que con pocas líneas de código se pueden conseguir funcionalidades complejas.

A lo largo del temario aprenderemos a usar selectores, muy parecidos a los de CSS, para acceder y modificar elementos HTML; veremos cómo manejar eventos para responder a las acciones del usuario; aplicaremos efectos y animaciones para mejorar la experiencia visual; y utilizaremos AJAX con jQuery para actualizar el contenido de una página sin necesidad de recargarla.

Gracias a su sintaxis clara, su gran comunidad y la amplia variedad de plugins disponibles, jQuery sigue siendo una herramienta útil para añadir interactividad y dinamismo a las páginas web. En el siguiente vídeo se presenta una introducción práctica a estos conceptos que servirá como punto de partida para la unidad.

## ¿Qué es jQuery?

jQuery es una biblioteca de JavaScript diseñada para simplificar las tareas de programación web del lado del cliente. Su propósito principal es facilitar la manipulación del DOM, el manejo de eventos, la creación de animaciones y la realización de peticiones AJAX. Esta biblioteca se 
distribuye como un solo archivo JavaScript, el cual puede ser incluido en cualquier proyecto web.

Una de las características clave de jQuery es su sintaxis concisa. Por ejemplo, seleccionar elementos HTML y aplicarles cambios con jQuery es más simple que con JavaScript puro. Además, jQuery facilita la implementación de efectos visuales y la manipulación del contenido de la
 página.

Otra ventaja importante de jQuery es su extensibilidad. Existen numerosos plugins desarrollados por la comunidad que amplían las funcionalidades de jQuery, permitiendo a los desarrolladores agregar fácilmente características avanzadas a sus aplicaciones web sin tener que escribir código desde cero.

## **Cómo incluir jQuery en un proyecto**

Incluir jQuery en un proyecto web es un proceso sencillo y puede hacerse principalmente de dos formas: mediante un CDN o mediante descarga y alojamiento local.

El uso de un CDN consiste en enlazar jQuery directamente desde un servidor externo. Esta opción ofrece ventajas como una carga más rápida de la página y la posibilidad de que el navegador ya tenga la biblioteca en caché, mejorando el rendimiento. Basta con añadir una etiqueta `<script>` que apunte a la URL de jQuery en el CDN.

La descarga y alojamiento local implica bajar la biblioteca desde el sitio oficial de jQuery y guardarla dentro del proyecto. Esta opción es útil cuando se trabaja sin conexión a internet o cuando se desea un mayor control sobre las dependencias. Una vez descargado el archivo, se incluye en el HTML mediante una etiqueta `<script>` que apunte a su ubicación local.

Por último, es importante comprobar que jQuery se ha cargado correctamente. Para ello, se puede usar un pequeño script con `$(document).ready()` que ejecute código jQuery una vez cargado el DOM. Si el código funciona correctamente, significa que jQuery está bien integrado en el proyecto.

### **Ventajas de usar jQuery**

jQuery facilita el desarrollo web al ofrecer una solución consistente frente a las diferencias entre navegadores, permitiendo escribir un único código que funcione correctamente en todos ellos. Esto reduce errores y ahorra tiempo de desarrollo.

Su sintaxis es clara y concisa, lo que permite realizar tareas complejas con pocas líneas de código, mejorando la legibilidad y el mantenimiento. Además, cuenta con una amplia comunidad y una gran cantidad de plugins, que permiten añadir funcionalidades avanzadas sin necesidad de desarrollarlas desde cero.

La curva de aprendizaje de jQuery es baja, lo que lo convierte en una herramienta accesible tanto para principiantes como para desarrolladores con experiencia. Destaca también por la facilidad para seleccionar y manipular el DOM, gracias a selectores similares a CSS y métodos simples para modificar elementos dinámicamente.

jQuery simplifica el manejo de eventos, ofreciendo una forma flexible y eficiente de responder a las interacciones del usuario, así como la creación de animaciones y efectos visuales que mejoran la experiencia de uso. Por último, facilita las peticiones AJAX, permitiendo actualizar el contenido de una página sin recargarla y gestionar datos de forma asíncrona de manera sencilla.

### Ejercicio práctico: Incluir jQuery en una página web

A continuación se muestra un ejemplo completo de un archivo HTML que incluye **jQuery mediante un CDN** y realiza una **manipulación básica del DOM**.

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejercicio jQuery</title>

    <!-- Incluir jQuery desde un CDN -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>

    <!-- Párrafo inicial -->
    <p id="texto">Hola, mundo</p>

    <script>
        // Código jQuery
        $(document).ready(function () {
            $("#texto").text("Hola, jQuery");
        });
    </script>

</body>
</html>
```

---

### Explicación del ejercicio

- Se crea un **archivo HTML básico**.
- Se incluye **jQuery desde un CDN** usando la etiqueta `<script>`.
- Se añade un **párrafo** con el texto inicial *“Hola, mundo”*.
- Con **jQuery**, se espera a que el DOM esté cargado (`$(document).ready()`).
- Se selecciona el párrafo por su **id** y se cambia su texto a *“Hola, jQuery”*.

Si al abrir el archivo en el navegador el texto aparece modificado, significa que **jQuery se ha incluido correctamente y el ejercicio funciona como se espera**.

## Selectores JQuery

Los selectores en jQuery son una herramienta que permite a los desarrolladores seleccionar y manipular elementos HTML. Utilizan una sintaxis similar a la de CSS, lo que facilita su aprendizaje y uso para aquellos que ya están familiarizados con los estilos en CSS. Los selectores de jQuery son importantes para trabajar con el DOM, permitiendo realizar tareas como cambiar el contenido de un elemento, modificar sus atributos, o aplicarle efectos visuales.

La capacidad de seleccionar elementos es importante para cualquier interacción con el DOM. jQuery tiene diferentes selectores que permiten seleccionar elementos basados en sus etiquetas, clases, IDs, atributos, y relaciones con otros elementos. Esta flexibilidad hace que jQuery sea una buena herramienta para el desarrollo web, simplificando tareas que de otro modo serían complejas y propensas a errores.

## Tipos de selectores en jQuery

jQuery ofrece distintos **selectores** que permiten acceder a los elementos HTML de forma flexible. A continuación se explican **todos los tipos mencionados**, con ejemplos claros.

---

### Selectores básicos

**Selector por etiqueta**

Selecciona todos los elementos de un tipo específico.

```jsx
$("p")        // Selecciona todos los párrafos
```

**Selector por clase**

Selecciona todos los elementos que tienen una clase específica.

```jsx
$(".destacado")   // Selecciona todos los elementos con la clase "destacado"
```

**Selector por ID**

Selecciona un elemento con un ID específico (debe ser único).

```jsx
$("#titulo")   // Selecciona el elemento con id="titulo"
```

---

## Selectores jerárquicos

**Selector descendiente**

Selecciona todos los elementos que están dentro de otro, sin importar el nivel.

```jsx
$("div p")    // Selecciona todos los <p> dentro de un <div>
```

**Selector de hijo directo**

Selecciona solo los hijos inmediatos de un elemento.

```jsx
$("ul > li")  // Selecciona los <li> que son hijos directos de <ul>
```

**Selector de hermano inmediato**

Selecciona el elemento hermano que aparece justo después.

```jsx
$("h1 + p")   // Selecciona el primer <p> inmediatamente después de un <h1>
```

**Selector de hermanos siguientes**

Selecciona todos los hermanos que siguen a un elemento.

```jsx
$("h1 ~ p")   // Selecciona todos los <p> que siguen a un <h1>

```

---

### Selectores de atributos

**Selector por atributo**

Selecciona elementos que tengan un atributo específico.

```jsx
$("input[type]")   // Selecciona inputs que tengan el atributo type
```

**Selector por atributo con valor exacto**

Selecciona elementos cuyo atributo tenga un valor concreto.

```jsx
$("input[type='text']")   // Selecciona inputs de tipo texto
```

**Selector por atributo que contiene un valor**

Selecciona elementos cuyo atributo contiene un texto determinado.

```jsx
$("a[href*='google']")   // Selecciona enlaces que contienen "google" en el href
```

---

### Selectores de posición

**Primer hijo**

Selecciona el primer hijo de un elemento.

```jsx
$("li:first-child")   // Selecciona el primer <li> de cada lista
```

**Último hijo**

Selecciona el último hijo de un elemento.

```jsx
$("li:last-child")    // Selecciona el último <li> de cada lista
```

**Elemento en una posición concreta**

Selecciona el elemento según su índice (empieza en 0).

```jsx
$("li:eq(2)")         // Selecciona el tercer <li>
```

**Elementos pares e impares**

Selecciona elementos según su posición.

```jsx
$("li:even")   // Selecciona elementos en posiciones pares
$("li:odd")    // Selecciona elementos en posiciones impares
```

---

### Ejercicio práctico: Uso de selectores jQuery

A continuación se muestra un **ejemplo completo** que cumple todos los puntos del ejercicio y permite practicar distintos **selectores jQuery**, manipulación del DOM y aplicación de estilos.

---

### Archivo HTML de ejemplo

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejercicio Selectores jQuery</title>

    <!-- Incluir jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <style>
        body {
            font-family: Arial, sans-serif;
        }
        div {
            margin: 10px 0;
        }
    </style>
</head>
<body>

    <h1 id="titulo">Ejercicio con jQuery</h1>

    <p class="texto">Este es el primer párrafo</p>
    <p class="texto">Este es el segundo párrafo</p>

    <div id="contenedor">
        <p>Texto dentro del div</p>
    </div>

    <ul id="lista">
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
    </ul>

    <button id="btnOcultar">Ocultar párrafos</button>
    <button id="btnMostrar">Mostrar párrafos</button>
    <button id="btnCambiar">Cambiar contenido</button>

    <script>
        $(document).ready(function () {

            // Ocultar elementos usando selector de clase
            $("#btnOcultar").click(function () {
                $(".texto").hide();
            });

            // Mostrar elementos ocultos
            $("#btnMostrar").click(function () {
                $(".texto").show();
            });

            // Cambiar contenido y aplicar estilos
            $("#btnCambiar").click(function () {

                // Cambiar texto usando selector por ID
                $("#titulo").text("Contenido modificado con jQuery");

                // Aplicar estilos CSS con jQuery
                $("#contenedor").css({
                    "background-color": "#e0e0e0",
                    "padding": "10px",
                    "border": "1px solid #000"
                });

                // Selector de posición
                $("#lista li:first-child").css("color", "red");
                $("#lista li:last-child").css("font-weight", "bold");
            });

        });
    </script>

</body>
</html>

```

---

### Explicación del ejercicio

- Se crea una página HTML con **párrafos, un div, una lista y botones**.
- Se utilizan **selectores por ID y clase** para ocultar y mostrar elementos (`.hide()` y `.show()`).
- Se modifica el **contenido de texto** de un elemento con `.text()`.
- Se aplican **estilos CSS dinámicamente** usando el método `.css()`.
- Se usan **selectores de posición** para modificar el primer y último elemento de una lista.

Este ejercicio demuestra cómo jQuery permite **manipular elementos, cambiar contenidos y aplicar estilos** de forma sencilla utilizando distintos tipos de selectores.

## **Introducción al manejo de eventos en jQuery**

El manejo de eventos es fundamental para crear páginas web interactivas, ya que permite responder a las acciones del usuario, como clics, movimientos del ratón, pulsaciones de teclas o la carga de una página. jQuery simplifica este proceso ofreciendo una interfaz clara y fácil de usar para asociar manejadores de eventos a los elementos del DOM.

Gracias a jQuery, los desarrolladores pueden definir funciones que se ejecutan cuando ocurre un evento específico, mejorando la interacción y la experiencia del usuario. La biblioteca incluye métodos para gestionar eventos comunes, delegar eventos y crear eventos personalizados, ocupándose además de las diferencias entre navegadores para garantizar un funcionamiento consistente.

## Manejadores de eventos en jQuery

jQuery simplifica la forma de asociar **manejadores de eventos** a los elementos del DOM, haciendo que el código sea más claro, corto y fácil de mantener. A continuación se describen los métodos más utilizados para gestionar eventos, junto con ejemplos prácticos.

---

## Método `.on()`

Es el método **más versátil y recomendado** para manejar eventos. Permite asociar uno o varios eventos a un elemento y también se utiliza para la **delegación de eventos**.

```jsx
$("#boton").on("click", function () {
    alert("Botón pulsado");
});
```

También puede manejar varios eventos a la vez:

```jsx
$("#caja").on("mouseenter mouseleave", function () {
    $(this).toggleClass("activo");
});
```

---

## Método `.click()`

Es una forma abreviada para manejar el evento `click`.

```jsx
$("#boton").click(function () {
    $("#mensaje").text("Has hecho clic en el botón");
});
```

---

## Método `.hover()`

Permite definir dos funciones:

- Una cuando el ratón entra en el elemento.
- Otra cuando el ratón sale.

```jsx
$("#caja").hover(
    function () {
        $(this).css("background-color", "lightblue");
    },
    function () {
        $(this).css("background-color", "white");
    }
);
```

---

## Métodos `.keydown()` y `.keyup()`

Se utilizan para manejar eventos de teclado.

```jsx
$(document).keydown(function () {
    console.log("Tecla presionada");
});

$(document).keyup(function () {
    console.log("Tecla liberada");
});
```

---

## Métodos `.focus()` y `.blur()`

Se activan cuando un elemento recibe o pierde el foco, como un campo de formulario.

```jsx
$("input").focus(function () {
    $(this).css("border", "2px solid green");
});

$("input").blur(function () {
    $(this).css("border", "1px solid gray");
});
```

---

## Delegación de eventos

La **delegación de eventos** permite manejar eventos en elementos que aún no existen en el DOM en el momento de cargar la página. Se logra usando el método `.on()` sobre un contenedor existente.

```jsx
$("#contenedor").on("click", "button", function () {
    alert("Botón dinámico pulsado");
});
```

En este ejemplo:

- El evento `click` se asigna al elemento `#contenedor`.
- El manejador solo se ejecuta cuando se hace clic en un `<button>` dentro del contenedor.
- Funciona incluso con botones añadidos dinámicamente después de cargar la página.

---

## Eventos comunes en jQuery

jQuery proporciona una amplia variedad de **eventos predefinidos** que permiten reaccionar a acciones del usuario y cambios en la página. A continuación se resumen los más utilizados, organizados por tipo, con explicación de su uso:

---

### Eventos de ratón

- **`click`**: Se activa al hacer clic en un elemento.
    
    ```jsx
    $("#boton").click(function() {
        alert("Has hecho clic");
    });
    ```
    
- **`dblclick`**: Se activa al hacer doble clic en un elemento.
    
    ```jsx
    $("#boton").dblclick(function() {
        alert("Doble clic");
    });
    ```
    
- **`mouseenter`**: Se activa cuando el puntero entra en el área de un elemento.
    
    ```jsx
    $("#caja").mouseenter(function() {
        $(this).css("background-color", "yellow");
    });
    ```
    
- **`mouseleave`**: Se activa cuando el puntero sale del área de un elemento.
    
    ```jsx
    $("#caja").mouseleave(function() {
        $(this).css("background-color", "white");
    });
    ```
    
- **`hover()`**: Método combinado que define dos funciones: entrada y salida del ratón.
    
    ```jsx
    $("#caja").hover(
        function() { $(this).css("background-color", "lightblue"); },
        function() { $(this).css("background-color", "white"); }
    );
    ```
    

---

### Eventos de teclado

- **`keydown`**: Se activa al presionar una tecla.
    
    ```jsx
    $(document).keydown(function() {
        console.log("Tecla presionada");
    });
    ```
    
- **`keyup`**: Se activa al soltar una tecla.
    
    ```jsx
    $(document).keyup(function() {
        console.log("Tecla liberada");
    });
    ```
    
- **`keypress`** *(deprecated)*: Se activaba al presionar y soltar una tecla; se recomienda usar `keydown` o `keyup`.

---

### Eventos de formulario

- **`submit`**: Se activa cuando un formulario se envía.
    
    ```jsx
    $("form").submit(function(e) {
        e.preventDefault(); // Evita que se recargue la página
        alert("Formulario enviado");
    });
    ```
    
- **`focus`**: Se activa cuando un elemento recibe el enfoque (ej. un input).
    
    ```jsx
    $("input").focus(function() {
        $(this).css("border", "2px solid green");
    });
    ```
    
- **`blur`**: Se activa cuando un elemento pierde el enfoque.
    
    ```jsx
    $("input").blur(function() {
        $(this).css("border", "1px solid gray");
    });
    ```
    

---

### Eventos del documento y ventana

- **`ready`**: Se activa cuando el DOM está completamente cargado.
    
    ```jsx
    $(document).ready(function() {
        console.log("DOM listo");
    });
    ```
    
- **`resize`**: Se activa al cambiar el tamaño de la ventana del navegador.
    
    ```jsx
    $(window).resize(function() {
        console.log("Ventana redimensionada");
    });
    ```
    
- **`scroll`**: Se activa cuando se desplaza el contenido de la ventana.
    
    ```jsx
    $(window).scroll(function() {
        console.log("Se ha hecho scroll");
    });
    ```
    

---

## Ejercicio práctico: Implementar manejadores de eventos con jQuery

A continuación se presenta un ejemplo completo de cómo **adjuntar manejadores de eventos** a distintos elementos de una página web, siguiendo todas las instrucciones del ejercicio.

---

### Archivo HTML de ejemplo

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejercicio Eventos jQuery</title>

    <!-- Incluir jQuery desde CDN -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        input, button {
            margin: 5px 0;
            padding: 5px 10px;
        }
        #mensaje {
            margin-top: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1 id="titulo">Eventos con jQuery</h1>

    <form id="miFormulario">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre">
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email">
        <br>
        <button type="submit">Enviar</button>
    </form>

    <button id="btnClic">Haz clic aquí</button>
    <button id="btnHover">Pasa el ratón</button>

    <p id="mensaje">Mensaje de prueba</p>

    <script>
        $(document).ready(function() {

            // Evento click
            $("#btnClic").click(function() {
                $("#mensaje").text("Botón clickeado").css("color", "blue");
            });

            // Evento hover
            $("#btnHover").hover(
                function() {
                    $(this).css("background-color", "lightgreen");
                    $("#mensaje").text("Ratón sobre el botón");
                },
                function() {
                    $(this).css("background-color", "");
                    $("#mensaje").text("Ratón fuera del botón");
                }
            );

            // Eventos de formulario
            $("#miFormulario").submit(function(e) {
                e.preventDefault(); // Evita recargar la página
                let nombre = $("#nombre").val();
                let email = $("#email").val();
                $("#mensaje").text(`Formulario enviado: ${nombre}, ${email}`).css("color", "green");
            });

            // Evento focus y blur en inputs
            $("input").focus(function() {
                $(this).css("border", "2px solid green");
            });
            $("input").blur(function() {
                $(this).css("border", "1px solid gray");
            });

            // Evento keyup en el input nombre
            $("#nombre").keyup(function() {
                $("#mensaje").text(`Escribiendo: ${$(this).val()}`).css("color", "orange");
            });

        });
    </script>

</body>
</html>

```

---

### Explicación del ejercicio

- Se crean **formularios, botones y un párrafo de mensaje** para interactuar.
- Se utilizan **eventos de ratón** (`click`, `hover`) para cambiar texto y estilos.
- Se manejan **eventos de formulario** (`submit`) para capturar datos sin recargar la página.
- Se aplican **estilos dinámicos** con `.css()` y se modifica el contenido del párrafo con `.text()`.
- Se usan **eventos de teclado** (`keyup`) y de **foco** (`focus` y `blur`) para mejorar la interactividad y la experiencia del usuario.

Este ejercicio permite practicar cómo **jQuery simplifica la gestión de eventos** y cómo se puede responder a distintas acciones del usuario de manera dinámica y visual.

# Jquery para manipulación del DOM

jQuery ofrece una serie de métodos que facilitan la **manipulación de elementos del DOM**, permitiendo añadir, eliminar, modificar o mover elementos de manera sencilla. A continuación se presentan los métodos más comunes con ejemplos prácticos.

---

### Seleccionar elementos

**`.find()`**: Busca todos los elementos descendientes de un elemento que coincidan con un selector.

```jsx
$("#contenedor").find("p"); // Selecciona todos los <p> dentro de #contenedor
```

---

### Añadir elementos

**`.append()`**: Inserta contenido al **final** de los elementos seleccionados.

```jsx
$("#lista").append("<li>Nuevo elemento final</li>");
```

**`.prepend()`**: Inserta contenido al **inicio** de los elementos seleccionados.

```jsx
$("#lista").prepend("<li>Nuevo elemento inicial</li>");
```

---

### Eliminar elementos

**`.remove()`**: Elimina los elementos seleccionados completamente del DOM.

```jsx
$(".eliminar").remove(); // Elimina todos los elementos con clase "eliminar"
```

**`.empty()`**: Elimina todos los hijos de los elementos seleccionados, dejando el contenedor vacío.

```jsx
$("#contenedor").empty(); // Borra todos los elementos dentro de #contenedor
```

---

### Modificar elementos

**`.html()`**: Obtiene o establece el contenido HTML de los elementos seleccionados.

```jsx
$("#mensaje").html("<strong>Texto en negrita</strong>");
```

**`.text()`**: Obtiene o establece el contenido de texto (sin HTML).

```jsx
$("#mensaje").text("Texto plano");
```

**`.attr()`**: Obtiene o establece el valor de un atributo.

```jsx
$("#imagen").attr("src", "nueva-imagen.jpg");
```

**`.css()`**: Obtiene o establece una o varias propiedades CSS.

```jsx
$("#mensaje").css("color", "red"); // Una propiedad
$("#mensaje").css({ "font-size": "20px", "background-color": "yellow" }); // Varias propiedades
```

---

### Mover elementos

**`.appendTo()`**: Mueve un elemento al **final** de otro.

```jsx
$("#nuevo").appendTo("#contenedor");
```

**`.prependTo()`**: Mueve un elemento al **inicio** de otro.

```jsx
$("#nuevo").prependTo("#contenedor");
```

**`.insertBefore()`**: Inserta un elemento **antes** de otro.

```jsx
$("#nuevo").insertBefore("#elementoExistente");
```

**`.insertAfter()`**: Inserta un elemento **después** de otro.

```jsx
$("#nuevo").insertAfter("#elementoExistente");
```

---

# Ajax con Jquery

jQuery ofrece formas de realizar peticiones AJAX, facilitando la comunicación asíncrona entre el cliente y el servidor. A continuación, se presentan los métodos más comunes para realizar peticiones AJAX con jQuery, junto con ejemplos prácticos de su uso.

---

### Método `.ajax()`

Es el método más **flexible y completo**, ya que permite especificar múltiples opciones como tipo de petición, URL, datos, formato de respuesta y manejo de errores.

```jsx
$.ajax({
    url: "https://api.ejemplo.com/datos",
    method: "GET",
    dataType: "json",
    success: function(respuesta) {
        console.log("Datos recibidos:", respuesta);
    },
    error: function(error) {
        console.error("Ocurrió un error:", error);
    }
});

```

---

### Método `.get()`

Forma abreviada para realizar peticiones **GET**, ideal para solicitudes simples.

```jsx
$.get("https://api.ejemplo.com/datos", function(respuesta) {
    console.log("Datos recibidos:", respuesta);
});

```

---

### Método `.post()`

Se utiliza para enviar datos al servidor mediante **POST**.

```jsx
$.post("https://api.ejemplo.com/guardar", { nombre: "Juan", edad: 30 }, function(respuesta) {
    console.log("Servidor respondió:", respuesta);
});

```

---

### Método `.load()`

Carga contenido HTML desde una URL y lo inserta directamente en el elemento seleccionado.

```jsx
$("#contenedor").load("contenido.html");

```

---

### Método `.getJSON()`

Realiza una petición **GET** y espera que la respuesta sea en **formato JSON**.

```jsx
$.getJSON("https://api.ejemplo.com/datos.json", function(datos) {
    console.log("Datos JSON:", datos);
});

```

---

### Manejo de errores

Es fundamental manejar los errores en las peticiones AJAX para mejorar la experiencia del usuario y detectar problemas de manera eficiente.

```jsx
$.ajax({
    url: "https://api.ejemplo.com/datos",
    method: "GET",
    success: function(respuesta) {
        console.log("Éxito:", respuesta);
    },
    error: function(xhr, status, error) {
        alert("Error al cargar los datos: " + status);
    }
});

```

---

## Ejercicio práctico: Realizar una petición AJAX con jQuery

A continuación se muestra un ejemplo completo que cumple los requisitos del ejercicio: hacer una petición AJAX al hacer clic en un botón y mostrar los datos recibidos en una lista.

---

### Archivo HTML de ejemplo

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ejercicio AJAX con jQuery</title>

    <!-- Incluir jQuery desde CDN -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        #listaDatos li {
            margin: 5px 0;
        }
        button {
            padding: 5px 10px;
        }
    </style>
</head>
<body>

    <h1>AJAX con jQuery</h1>

    <button id="btnCargar">Cargar Datos</button>

    <ul id="listaDatos">
        <!-- Los datos se mostrarán aquí -->
    </ul>

    <script>
        $(document).ready(function() {

            $("#btnCargar").click(function() {

                // Petición AJAX GET
                $.ajax({
                    url: "https://jsonplaceholder.typicode.com/users", // API de ejemplo
                    method: "GET",
                    dataType: "json",
                    success: function(datos) {

                        // Limpiar lista antes de añadir los datos
                        $("#listaDatos").empty();

                        // Recorrer datos y agregarlos a la lista
                        datos.forEach(function(usuario) {
                            $("#listaDatos").append("<li>" + usuario.name + " (" + usuario.email + ")</li>");
                        });

                    },
                    error: function(xhr, status, error) {
                        alert("Ocurrió un error al cargar los datos: " + status);
                    }
                });

            });

        });
    </script>

</body>
</html>

```

---

### Explicación del ejercicio

1. Se crea un **archivo HTML básico** con un botón (`#btnCargar`) y una lista (`#listaDatos`) donde se mostrarán los resultados.
2. Se utiliza **jQuery** para escuchar el evento `click` sobre el botón.
3. Se realiza una **petición AJAX** usando `$.ajax()` a un servidor de ejemplo (JSONPlaceholder).
4. En caso de éxito, se recorren los datos recibidos y se agregan como elementos `<li>` dentro de la lista.
5. Se maneja el **error** mostrando una alerta si la petición falla.

Este ejemplo demuestra cómo **cargar datos de un servidor de manera asíncrona** y mostrarlos dinámicamente en la página usando jQuery y AJAX.