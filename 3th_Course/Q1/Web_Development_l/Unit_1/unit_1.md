# Introducción a la Web

Definimos la web como una plataforma global de información interconectada que utiliza el protocolo HTTP (HyperText Transfer Protocol) para la transferencia de datos. HTTP es el pilar fundamental que permite la comunicación entre clientes y servidores, facilitando el intercambio de información en la red. 

Además de HTTP, existen otros protocolos como FTP (File Transfer Protocol) para la transferencia de archivos y protocolos de correo electrónico como IMAP, POP y SMTP.

En la comunicación web, la arquitectura cliente-servidor juega un papel crucial. El cliente, que puede ser un navegador web, envía una solicitud (request) al servidor, el cual procesa la solicitud y devuelve una respuesta (response). 

## El protocolo HTTP

**HTTP (HyperText Transfer Protocol)** es el protocolo de comunicación fundamental de la web, que define cómo los clientes (como navegadores) y los servidores intercambian información. Fue desarrollado por Tim Berners-Lee en el CERN y ha evolucionado desde HTTP/0.9 hasta HTTP/2, mejorando funciones y rendimiento, incluyendo compresión de encabezados y multiplexación.

HTTP es **sin estado**, lo que significa que cada solicitud se procesa de manera independiente, permitiendo que la web sea escalable. Una **transacción HTTP** incluye:

- **Solicitud del cliente**: línea de solicitud (método, URL, versión), encabezados y opcionalmente un cuerpo con datos (POST, PUT).
- **Respuesta del servidor**: línea de estado (código y frase descriptiva), encabezados y cuerpo con los datos solicitados.

Para comunicaciones seguras se usa **HTTPS**, que cifra los datos con TLS, protegiendo la información frente a interceptaciones y ataques.

---

Además de **HTTP**, la web y las redes utilizan otros protocolos esenciales para la transferencia de datos y la gestión de información:

1. **FTP (File Transfer Protocol)**
    - **Función**: Transferencia y administración de archivos entre cliente y servidor.
    - **Uso**: Subir, descargar, renombrar, borrar y mover archivos en servidores.
    - **Puertos**: 20 y 21.
    - **Modos**: Activo y pasivo, que determinan cómo se establece la conexión.
2. **IMAP (Internet Message Access Protocol)**
    - **Función**: Acceso y gestión de correos directamente en el servidor.
    - **Uso**: Mantener los correos en el servidor, permitiendo sincronización en múltiples dispositivos.
    - **Puertos**: 143 (no cifrado) y 993 (cifrado, IMAPS).
3. **POP3 (Post Office Protocol 3)**
    - **Función**: Descarga de correos electrónicos desde el servidor a un dispositivo.
    - **Uso**: Guardar correos localmente y eliminarlos del servidor, útil cuando no se requiere acceso desde varios dispositivos.
    - **Puertos**: 110 (no cifrado) y 995 (cifrado, POP3S).
4. **SMTP (Simple Mail Transfer Protocol)**
    - **Función**: Envío de correos electrónicos desde clientes a servidores y entre servidores.
    - **Uso**: Fundamental para el enrutamiento de correos en Internet.
    - **Puertos**: 25 (estándar), 587 (envío con autenticación), 465 (cifrado, SMTPS).

## **Arquitectura Cliente-Servidor**

Es un modelo de diseño de aplicaciones en red que **divide las tareas** entre:

- **Clientes:** dispositivos o aplicaciones que solicitan recursos o servicios (ej. navegadores web).
- **Servidores:** dispositivos o aplicaciones que proporcionan los recursos o servicios solicitados, atendiendo múltiples clientes simultáneamente.

**Funcionamiento:**

1. **Solicitud del Cliente:** El cliente envía una petición al servidor (página web, archivo, consulta a base de datos).
2. **Procesamiento en el Servidor:** El servidor procesa la solicitud, accediendo a datos, ejecutando scripts o preparando archivos.
3. **Respuesta del Servidor:** El servidor envía los datos o mensajes de estado al cliente.
4. **Recepción y Procesamiento en el Cliente:** El cliente recibe y procesa la respuesta (ej. renderiza una página web).

**Ventajas:**

- **Escalabilidad:** Los servidores pueden manejar múltiples clientes y crecer con la demanda.
- **Mantenimiento centralizado:** La mayoría del procesamiento se realiza en el servidor, facilitando actualizaciones y administración.
- **Seguridad:** Los datos sensibles se gestionan en el servidor, controlando el acceso y la protección de información.

**Ejemplos de aplicaciones:**

- **Navegadores web y servidores web:** Solicitan y reciben páginas web vía HTTP/HTTPS.
- **Clientes de correo y servidores de correo:** Gestionan correos mediante IMAP, POP y SMTP.
- **Aplicaciones de base de datos:** Los clientes envían consultas SQL y reciben resultados desde el servidor.

## **Direcciones IP y DNS**

La comunicación en redes y en la web se basa en **direcciones IP** y el **Sistema de Nombres de Dominio (DNS)**, que permiten localizar y acceder a recursos de manera eficiente.

### **Direcciones IP**

Identifican de manera única a cada dispositivo conectado a una red.

- **IPv4:**
    - Direcciones de 32 bits (~4.3 mil millones posibles).
    - Formato: cuatro números decimales separados por puntos (ej. 192.168.0.1).
- **IPv6:**
    - Direcciones de 128 bits, prácticamente ilimitadas.
    - Formato: ocho grupos de cuatro dígitos hexadecimales separados por dos puntos (ej. 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

### **DNS (Sistema de Nombres de Dominio)**

Convierte nombres de dominio legibles por humanos en direcciones IP comprensibles por las máquinas. Facilita la navegación web sin necesidad de recordar direcciones numéricas.

**Funcionamiento:**

1. El usuario ingresa un nombre de dominio en el navegador.
2. Se consulta un servidor DNS para resolver el nombre en una IP.
3. Si no está en la caché, el servidor recursivo consulta otros servidores DNS hasta obtener la IP correcta.
4. La IP se devuelve al navegador, que se conecta al servidor web.

**Tipos de servidores DNS:**

- **Recursivos:** realizan consultas a otros servidores para resolver un dominio.
- **Autoritativos:** contienen la información definitiva de un dominio y responden con la IP correspondiente.

## **HTTP en detalle**

### Formato de una petición HTTP

Una petición HTTP es ante todo un mensaje que el cliente envía al servidor para solicitar un recurso o realizar una acción. Se compone de tres partes:

**Línea de solicitud:**

- Indica el método (GET, POST, PUT, DELETE…) y el recurso solicitado.

**Encabezados de solicitud:**

- Proporcionan información adicional sobre la petición y el cliente.
- Ejemplos comunes:
    - `Host`: dominio del servidor.
    - `Accept`: tipos de medios que el cliente puede procesar.
    - `Accept-Language`: idiomas preferidos.
    - `Accept-Encoding`: codificaciones soportadas.
    - `Connection`: control de la conexión.

**Cuerpo de la solicitud (opcional):**

- Incluye datos enviados al servidor (ej. JSON, XML, formularios) en métodos como POST o PUT.

💡 **Clave:** Una petición bien formada (línea, encabezados y cuerpo correctos) asegura una comunicación eficiente entre cliente y servidor.

### Métodos HTTP

| Método | Propósito |
| --- | --- |
| **GET** | Solicita un recurso, solo lectura, no modifica el servidor. |
| **POST** | Envía datos para crear un nuevo recurso. |
| **PUT** | Reemplaza completamente un recurso existente. |
| **DELETE** | Elimina un recurso. |
| **HEAD** | Solicita solo las cabeceras de un recurso, sin el cuerpo. |
| **OPTIONS** | Consulta los métodos soportados para un recurso. |
| **PATCH** | Modifica parcialmente un recurso existente. |

```jsx
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"  # Ejemplo de API de prueba
data = {"title": "Prueba", "body": "Contenido", "userId": 1}

# GET
r_get = requests.get(url)
print("GET:", r_get.status_code)

# POST
r_post = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print("POST:", r_post.status_code, r_post.json())

# PUT
r_put = requests.put(url, json=data)
print("PUT:", r_put.status_code, r_put.json())

# DELETE
r_delete = requests.delete(url)
print("DELETE:", r_delete.status_code)

# HEAD
r_head = requests.head(url)
print("HEAD:", r_head.headers)

# OPTIONS
r_options = requests.options(url)
print("OPTIONS:", r_options.headers)

# PATCH
r_patch = requests.patch(url, json={"title": "Actualizado"})
print("PATCH:", r_patch.status_code, r_patch.json())

```

### **Respuestas HTTP**

Cuando un cliente hace una petición, el servidor responde con un **mensaje HTTP** que indica si la solicitud fue procesada correctamente o si hubo algún problema. La respuesta incluye:

- **Código de estado**: número que indica el resultado de la solicitud.
- **Encabezados**: información adicional sobre la respuesta.
- **Cuerpo (opcional)**: datos solicitados o información sobre el error.

---

### **Códigos de respuesta HTTP**

| Clase | Significado | Ejemplos |
| --- | --- | --- |
| **1xx – Informativos** | La solicitud fue recibida y el proceso continúa. | 100 Continue, 101 Switching Protocols |
| **2xx – Éxito** | La solicitud fue entendida y procesada correctamente. | 200 OK, 201 Created, 202 Accepted, 204 No Content |
| **3xx – Redirección** | Se requiere acción adicional del cliente. | 301 Moved Permanently, 302 Found, 304 Not Modified |
| **4xx – Error del cliente** | La solicitud tiene un problema. | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 405 Method Not Allowed |
| **5xx – Error del servidor** | El servidor falló al cumplir una solicitud válida. | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout |

💡 **Clave:**

- Los códigos **2xx** indican éxito.
- Los **4xx** son problemas del cliente (por ejemplo, URL mal escrita o falta de permisos).
- Los **5xx** son problemas del servidor.
- Los **1xx** y **3xx** son menos comunes, pero útiles para saber si continuar o redirigir la petición.

## **Web estática y dinámica**

Las webs se pueden clasificar en dos categorías principales: webs estáticas y webs dinámicas. Esta clasificación se basa en cómo se generan y entregan las páginas web al usuario final. Cada tipo de web tiene sus propias características, ventajas y desventajas, y se utiliza en contextos diferentes dependiendo de los requisitos del proyecto y las necesidades del usuario.

- **Web estática:**
    
    Son páginas web cuyo contenido no cambia al cargarlas. Cada usuario ve la misma información y los cambios requieren editar el código HTML directamente.
    
- **Web dinámica:**
    
    Son páginas web que generan contenido en tiempo real según la interacción del usuario, consultas a bases de datos o lógica del servidor. Cada usuario puede ver información diferente.
    

---

### **Comparativa**

| Característica | Web Estática | Web Dinámica |
| --- | --- | --- |
| **Contenido** | Fijo, no cambia automáticamente | Generado dinámicamente según usuario o contexto |
| **Lenguajes** | HTML, CSS, imágenes | HTML, CSS + JavaScript, PHP, Python, bases de datos |
| **Interactividad** | Muy limitada | Alta, permite formularios, login, personalización |
| **Actualización** | Manual, editando archivos | Automática, mediante programación o bases de datos |
| **Rendimiento** | Rápida, ligera | Puede ser más lenta, depende del servidor y consultas |
| **Ejemplos** | Portafolios, páginas informativas simples | Redes sociales, tiendas online, blogs con usuarios |

---

## **4. HTML básico**

## **HTML Básico**

HTML (HyperText Markup Language) es el lenguaje estándar para crear páginas web. Define la estructura de los contenidos mediante **etiquetas** (tags), que indican al navegador cómo mostrar texto, imágenes, enlaces, formularios y otros elementos.

---

### **Etiquetas (tags)**

- Son los **bloques fundamentales** de HTML que delimitan contenido y le dan significado.
- Suelen escribirse entre `< >` y normalmente vienen en **pares**: una de apertura y otra de cierre.
- Ejemplo básico:

```
<p>Este es un párrafo</p>
```

lgunas etiquetas comunes:

- `<h1>` a `<h6>`: títulos.
- `<p>`: párrafos.
- `<a>`: enlaces.
- `<img>`: imágenes.
- `<div>`: contenedores generales.

### **Estructura básica de un documento HTML**

Un documento HTML sigue una **estructura estándar** que indica al navegador qué es el contenido y cómo interpretarlo.

```jsx
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <title>Mi primera página</title>
  </head>
  <body>
    <h1>Hola Mundo</h1>
    <p>Este es un párrafo de ejemplo.</p>
  </body>
</html>

```

**Partes importantes:**

- `<!DOCTYPE html>`: define la versión de HTML (HTML5).
- `<html>`: etiqueta raíz que contiene todo el documento.
- `<head>`: metadatos, título, enlaces a CSS o scripts.
- `<body>`: contenido visible en la página (texto, imágenes, enlaces…).

### **Elementos simples y compuestos**

- **Elementos simples:** no tienen contenido interno ni etiqueta de cierre, suelen **auto-cerrarse**.
    - Ejemplos:

```jsx
<img src="imagen.jpg" alt="Descripción">
<br> <!-- salto de línea -->
<hr> <!-- línea horizontal -->
```

**Elementos compuestos:** tienen apertura y cierre, y contienen otros elementos o texto.

- Ejemplos:

```jsx
<p>Este es un párrafo <strong>importante</strong></p>
<ul>
  <li>Elemento 1</li>
  <li>Elemento 2</li>
</ul>
```

### **Atributos**

- Son **información adicional** que se agrega a las etiquetas para modificar su comportamiento o estilo.
- Se escriben dentro de la etiqueta de apertura: `nombre="valor"`.
- Ejemplos:
    - `<a href="https://www.ejemplo.com">Enlace</a>` → `href` indica la URL del enlace.
    - `<img src="foto.jpg" alt="Foto de ejemplo" width="300">` → `src` indica la imagen, `alt` texto alternativo, `width` ancho.
    - `<div id="contenedor" class="principal">Contenido</div>` → `id` identifica un elemento, `class` lo clasifica para CSS/JS.

### **Comentarios en HTML**

- Los comentarios permiten **anotar código** sin que se muestre en el navegador.
- Se usan para explicar el código, dejar recordatorios o desactivar temporalmente partes del HTML.
- Sintaxis:

```jsx
<!-- Esto es un comentario -->
<p>Este párrafo sí se mostrará</p>
<!-- <p>Este párrafo está comentado y no se ve</p> -->
```

💡 **Consejo práctico:**

- Siempre cierra las etiquetas compuestas.
- Usa atributos descriptivos (`alt`, `title`, `id`) para mejorar accesibilidad y control del contenido.
- Comenta secciones complejas para ti o para otros desarrolladores.
    
    ---
    

## **Texto y estructura**

### **Títulos (headings)**

- Los títulos organizan el contenido jerárquicamente.
- Hay 6 niveles: `<h1>` (más importante) a `<h6>` (menos importante).
- Ejemplo:

```jsx
<h1>Título principal</h1>
<h2>Subtítulo</h2>
<h3>Sección menor</h3>
```

💡 **Tip:** `<h1>` solo debe usarse una vez por página para SEO y accesibilidad.

### **Párrafos y saltos de línea**

- `<p>` define un párrafo.
- `<br>` inserta un salto de línea sin iniciar un nuevo párrafo.

```jsx
<p>Este es un párrafo de texto.</p>
<p>Otro párrafo separado.</p>

<p>Línea 1<br>Línea 2<br>Línea 3</p>
```

### **Texto en negrita y cursiva**

- `<strong>` o `<b>` → negrita (importancia o estilo).
- `<em>` o `<i>` → cursiva (énfasis o estilo).

```jsx
<p>Este texto es <strong>importante</strong> y este es <em>enfático</em>.</p>
```

---

### **Subíndices y superíndices**

- `<sub>` → subíndice (abajo).
- `<sup>` → superíndice (arriba).

```jsx
<p>H<sub>2</sub>O es agua.</p>
<p>E = mc<sup>2</sup> es la fórmula de Einstein.</p>
```

### **Agrupaciones con `<div>` y `<header>`**

- **`<div>`**: contenedor genérico para agrupar elementos y aplicar estilos o scripts.
- **`<header>`**: se usa para agrupar encabezados, menús o introducciones de secciones.

```jsx
Agrupaciones con <div> y <header>

<div>: contenedor genérico para agrupar elementos y aplicar estilos o scripts.

<header>: se usa para agrupar encabezados, menús o introducciones de secciones.
```

**Tip:**

- Usa `<div>` para organizar secciones sin significado semántico especial.
- Usa `<header>` para contenido que funciona como encabezado de una sección.

## **ablas, listas y formularios en HTML**

HTML permite organizar la información en **tablas**, **listas** y **formularios**, facilitando la presentación de datos y la interacción con el usuario.

---

### **Tablas y sus elementos**

- Se usan para mostrar datos en **filas y columnas**.
- Etiquetas principales:
    - `<table>` → contenedor de la tabla.
    - `<tr>` → fila de la tabla.
    - `<th>` → celda de encabezado (generalmente en negrita y centrada).
    - `<td>` → celda de datos.

ejemplo: 

```jsx
<table border="1">
  <tr>
    <th>Nombre</th>
    <th>Edad</th>
    <th>Ciudad</th>
  </tr>
  <tr>
    <td>Juan</td>
    <td>25</td>
    <td>Madrid</td>
  </tr>
  <tr>
    <td>María</td>
    <td>30</td>
    <td>Barcelona</td>
  </tr>
</table>

```

💡 **Tip:** Añade `border`, `cellpadding` o `style` para mejorar el diseño visual.

### **Listas ordenadas y no ordenadas**

- **Listas ordenadas `<ol>`**: los elementos se numeran automáticamente.
- **Listas no ordenadas `<ul>`**: los elementos se muestran con viñetas.
- **Elementos de lista `<li>`**: cada ítem de la lista.

ejemplo:

```jsx
<h3>Lista ordenada:</h3>
<ol>
  <li>Primer elemento</li>
  <li>Segundo elemento</li>
  <li>Tercer elemento</li>
</ol>

<h3>Lista no ordenada:</h3>
<ul>
  <li>Manzanas</li>
  <li>Naranjas</li>
  <li>Plátanos</li>
</ul>

```

💡 **Tip:** Las listas pueden ser **anidadas** para crear sublistas:

```jsx
<ul>
  <li>Frutas
    <ul>
      <li>Manzanas</li>
      <li>Peras</li>
    </ul>
  </li>
</ul>

```

### **Formularios y sus elementos**

- Se usan para **recoger datos del usuario** y enviarlos al servidor.
- Etiquetas principales:
    - `<form>` → contenedor del formulario (`action` y `method` determinan a dónde y cómo se envían los datos).
    - `<input>` → campo de entrada (tipo: text, password, email, checkbox, radio, submit…).
    - `<textarea>` → área de texto multilinea.
    - `<select>` → lista desplegable.
    - `<option>` → elemento de la lista desplegable.
    - `<label>` → etiqueta para un input, mejora accesibilidad.

**Ejemplo:**

```jsx
<form action="/enviar" method="POST">
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" name="nombre"><br><br>
  
  <label for="email">Email:</label>
  <input type="email" id="email" name="email"><br><br>
  
  <label>Género:</label>
  <input type="radio" name="genero" value="M"> Masculino
  <input type="radio" name="genero" value="F"> Femenino<br><br>
  
  <label for="comentario">Comentario:</label><br>
  <textarea id="comentario" name="comentario" rows="4" cols="50"></textarea><br><br>
  
  <label for="pais">País:</label>
  <select id="pais" name="pais">
    <option value="es">España</option>
    <option value="mx">México</option>
    <option value="ar">Argentina</option>
  </select><br><br>
  
  <input type="submit" value="Enviar">
</form>
```

---

## **Enlaces e imágenes**

### **Creación de enlaces con `<a>`**

- La etiqueta `<a>` (anchor) se utiliza para **crear hipervínculos** hacia otras páginas, secciones internas o correos electrónicos.
- Atributos importantes:
    - `href`: URL de destino del enlace.
    - `target`: dónde se abrirá el enlace (`_self` predeterminado, `_blank` nueva pestaña).
    - `title`: texto descriptivo al pasar el cursor.

**Ejemplos:**

```jsx
<!-- Enlace a otra página web -->
<a href="https://www.ejemplo.com" target="_blank" title="Ir a ejemplo.com">Visitar ejemplo.com</a>

<!-- Enlace interno a otra sección de la misma página -->
<a href="#seccion2">Ir a Sección 2</a>

<!-- Enlace de correo electrónico -->
<a href="mailto:contacto@ejemplo.com">Enviar correo</a>

```

💡 **Tip:** Usar `target="_blank"` para enlaces externos y `title` para mejorar accesibilidad.

### **Inclusión de imágenes con `<img>`**

- La etiqueta `<img>` permite **insertar imágenes** en la página web.
- Es un **elemento vacío**, no necesita etiqueta de cierre.
- Atributos importantes:
    - `src`: ruta de la imagen (local o URL externa).
    - `alt`: texto alternativo si la imagen no se carga (importante para accesibilidad y SEO).
    - `width` y `height`: dimensiones de la imagen.
    - `title`: texto que aparece al pasar el cursor.

**Ejemplos:**

```jsx
<!-- Imagen local -->
<img src="imagen.jpg" alt="Descripción de la imagen" width="300">

<!-- Imagen desde URL externa -->
<img src="https://www.ejemplo.com/logo.png" alt="Logo Ejemplo" height="100">

<!-- Imagen con título -->
<img src="foto.jpg" alt="Foto de ejemplo" title="Foto de ejemplo">
```

💡 **Tip:** Siempre incluir `alt` para accesibilidad y buenas prácticas de SEO.