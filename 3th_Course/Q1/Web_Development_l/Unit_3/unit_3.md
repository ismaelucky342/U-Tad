# CSS y AJAX

Creado: 16 de noviembre de 2025 22:35

![image.png](unit_3/image.png)

CSS, o Cascading Style Sheets (Hojas de Estilo en Cascada), es un lenguaje de diseño utilizado para describir la presentación de un documento escrito en HTML o XML. CSS se encarga de la apariencia de la página web, separando la estructura y el contenido (HTML) de la presentación y el diseño. Esta separación facilita el mantenimiento y la actualización de los estilos de una página web.

Sus componentes básicos son:

- Selectores: como patrones utilizados para seleccionar los elementos HTML que se desea estilizar.
- Propiedades y Valores: definen que aspecto se desea estilizar y los valores como se debe hacer.
- Reglas CSS: compuestas por un selector y un bloque de declaraciones cada una con una propiedad y valor.

CSS se puede aplicar a los documentos HTML de tres maneras principales:

- Estilos Inline: Los estilos se aplican directamente a los elementos HTML mediante el atributo `style`.
- Estilos internos: Los estilos se colocan dentro de una etiqueta `<style>` en la sección `<head>` del documento HTML.
- Estilos Externos: Los estilos se definen en un archivo CSS separado, que se enlaza al documento HTML mediante la etiqueta `<link>`.

## Sintaxis de CSS

Una regla CSS tiene **dos partes**:

1. **Selector** → Elige qué elementos HTML se van a estilizar.
2. **Bloque de declaraciones** → Entre `{ }`, contiene propiedades y valores.

Ejemplo:

```css
p {
  color: red;
  font-size: 20px;
}
```

---

### **Tipos de selectores**

- **Selector de tipo** → selecciona etiquetas HTML.
    
    Ej: `h1 { ... }`
    
- **Selector de clase** → empieza con `.`
    
    Ej: `.destacado { ... }`
    
- **Selector de ID** → empieza con `#`
    
    Ej: `#cabecera { ... }`
    
- **Selector universal** →  selecciona todo
    
    Ej: `* { margin: 0; }`
    
- **Selector por atributo**
    
    Ej: `input[type="text"] { ... }`
    
- **Selector descendiente**
    
    Ej: `div span { ... }`
    

**Propiedades y valores**

Una propiedad define qué cambias; el valor dice cómo.

Ejemplos típicos:

- `color: blue;` (color del texto)
- `background: black;`
- `margin: 10px;`
- `font-size: 16px;`

## Tipos de datos en CSS

Los tipos de datos permiten definir los valores de las propiedades CSS. Cada propiedad admite ciertos tipos según lo que se quiera representar: colores, tamaños, funciones, palabras clave, etc.

### Colores

Formas comunes de definir colores:

- Nombres de color: `red`, `blue`, `black`
- Hexadecimales: `#ff0000`
- RGB: `rgb(255, 0, 0)`
- RGBA (RGB con transparencia): `rgba(255, 0, 0, 0.5)`
- HSL: `hsl(0, 100%, 50%)`
- HSLA: `hsla(0, 100%, 50%, 0.5)`

---

### Longitudes

Se usan para tamaños, márgenes, rellenos, bordes, etc.

**Unidades absolutas (no dependen del entorno)**

- `px` (píxeles)
- `cm`
- `mm`
- `in` (pulgadas)
- `pt` (puntos)
- `pc` (picas)

**Unidades relativas (dependen del elemento o ventana)**

- `em` (relativo al font-size del elemento padre)
- `rem` (relativo al font-size del elemento raíz)
- `%` (porcentaje del contenedor)
- `vw` (1 % del ancho de la ventana)
- `vh` (1 % de la altura de la ventana)

---

### Texto

Propiedades relacionadas con fuentes y formato:

- `font-family`
- `font-size`
- `font-weight`
- `line-height`
- `text-align`

---

### URLs

Se usan para cargar recursos externos:

- `background-image: url("imagen.png");`
- `@font-face` para fuentes
- `@import` para cargar otros CSS

---

### Funciones de CSS

Funciones que permiten valores dinámicos:

- `calc()` para cálculos matemáticos
- `var()` para usar variables CSS
- `linear-gradient()` para generar gradientes

---

### Palabras clave especiales

Usadas para controlar herencia o valores por defecto:

- `inherit` (hereda del padre)
- `initial` (restablece al valor inicial)
- `unset` (combina inherit/initial según corresponda)
- `auto` (deja que el navegador decida el valor)

---

## Modelo de Caja (Box Model)

El modelo de caja (Box Model) en CSS describe cómo se estructuran y se comportan los elementos HTML como cajas rectangulares en la página web. 

### Contenido (content)

Es el área donde se muestra el contenido del elemento: texto, imágenes, vídeos, etc.

Su tamaño se define con `width` y `height`.

---

### Relleno (padding)

Espacio entre el contenido y el borde.

Puede definirse por lado:

- `padding-top`
- `padding-right`
- `padding-bottom`
- `padding-left`

También se puede usar la forma abreviada: `padding: 20px;`

---

### Borde (border)

Es el contorno que rodea contenido + padding.

Se personaliza mediante:

- `border-width`
- `border-style`
- `border-color`

O abreviado: `border: 5px solid black;`

---

### Margen (margin)

Es el espacio exterior que separa la caja de otros elementos.

También admite propiedades por lado:

- `margin-top`
- `margin-right`
- `margin-bottom`
- `margin-left`

O abreviado: `margin: 10px;`

---

### Ejemplo de caja

```css
.div-ejemplo {
  width: 200px;
  height: 100px;
  padding: 20px;
  border: 5px solid black;
  margin: 10px;
}
```

La dimensión total no es solo `200x100`:

Se suman padding + border + margin.

---

### Box-sizing

Controla cómo se calcula el tamaño total del elemento.

`box-sizing: content-box` (valor por defecto)

- `width` y `height` **solo** incluyen el contenido.
- El padding y border **se suman** aparte.

`box-sizing: border-box`

- `width` y `height` **incluyen contenido + padding + border**.
- Facilita maquetar porque evita cálculos manuales.

---

## Estilizando Textos y Fuentes

Las propiedades de texto y fuentes permiten controlar la apariencia, legibilidad y estilo del contenido dentro de una página web.

### `font-family`

Define la familia tipográfica que usará el elemento.

Es buena práctica incluir varias fuentes de respaldo y una fuente genérica al final.

Ejemplo:

```css
font-family: "Roboto", "Arial", sans-serif;
```

---

### `font-size`

Establece el tamaño de la fuente.

Puede usar unidades absolutas como `px` o `pt`, o relativas como `em`, `rem` o `%`.

Ejemplo:

```css
font-size: 16px;
```

---

### `font-weight`

Controla el grosor del texto.

Acepta valores como `normal`, `bold`, `lighter`, `bolder` o valores numéricos entre 100 y 900.

Ejemplo:

```css
font-weight: bold;
```

---

### `font-style`

Define el estilo de la fuente: normal, cursiva o inclinada.

Ejemplo:

```css
font-style: italic;
```

---

### `text-transform`

Controla la capitalización del texto.

Puede convertirlo a mayúsculas, minúsculas o capitalizar cada palabra.

Ejemplo:

```css
text-transform: uppercase;
```

---

### `text-decoration`

Añade decoraciones como subrayado, línea superior o tachado.

Ejemplo:

```css
text-decoration: line-through;
```

---

### `line-height`

Ajusta la altura de la línea, afectando el espacio vertical entre líneas.

Ejemplo:

```css
line-height: 1.5;
```

---

### `text-align`

Alinea el texto dentro de su contenedor.

Opciones comunes: izquierda, derecha, centrado o justificado.

Ejemplo:

```css
text-align: center;
```

---

### `letter-spacing`

Ajusta el espaciado entre caracteres.

Ejemplo:

```css
letter-spacing: 1px;
```

---

### `word-spacing`

Ajusta el espacio entre palabras.

Ejemplo:

```css
word-spacing: 4px;
```

---

## Fondos y Bordes

Los fondos y bordes permiten mejorar la apariencia visual de los elementos HTML, añadiendo color, imágenes y contornos decorativos.

### Propiedades de Fondo

### `background-color`

Define el color de fondo de un elemento.

### `background-image`

Establece una imagen de fondo mediante `url()`.

### `background-repeat`

Controla cómo se repite la imagen de fondo.

Valores comunes: `repeat`, `repeat-x`, `repeat-y`, `no-repeat`.

### `background-position`

Define la posición inicial de la imagen de fondo.

Ejemplos: `center`, `top left`, `50% 50%`.

### `background-size`

Define el tamaño de la imagen de fondo.

Valores: `auto`, `cover`, `contain`, o medidas específicas.

### `background-attachment`

Controla si la imagen se desplaza con la página o permanece fija.

Valores: `scroll`, `fixed`, `local`.

### `background`

Propiedad abreviada para definir varias propiedades de fondo en una sola línea.

Ejemplo:

```css
background: url("fondo.jpg") no-repeat center/cover;
```

---

### Propiedades de Bordes

### `border-width`

Define el grosor del borde.

Puede aplicarse a cada lado con `border-top-width`, etc.

### `border-style`

Define el estilo del borde.

Valores comunes:

`none`, `solid`, `dotted`, `dashed`, `double`, `groove`, `ridge`, `inset`, `outset`.

### `border-color`

Define el color del borde.

También puede aplicarse por lado si se desea.

### `border-radius`

Define esquinas redondeadas.

Permite valores simples o combinaciones para esquinas específicas.

### `border`

Propiedad abreviada para definir ancho, estilo y color en una sola declaración.

Ejemplo:

```css
border: 3px solid black;
```

---