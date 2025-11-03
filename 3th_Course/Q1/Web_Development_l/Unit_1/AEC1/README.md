# Juego del Ahorcado - AEC1 Desarrollo Web I

## Descripción

Este proyecto es una práctica individual de la asignatura de Desarrollo Web I en U-tad. He implementado el clásico juego del ahorcado utilizando únicamente HTML, CSS y JavaScript vanilla, sin frameworks ni librerías externas.

El objetivo principal era cumplir con los requisitos funcionales especificados en el enunciado de la práctica, además de aplicar un diseño visual moderno (en mi caso inspirado en Tron con neones) y coherente con la identidad de U-tad.

## Estructura del Proyecto

```
AEC1/
├── index.html              # Estructura HTML principal del juego
├── scripts/               
│   ├── config.js           # Configuración: palabras y constantes del juego
│   └── game.js             # Lógica completa del juego (clase HangmanGame)
├── styles/                
│   ├── base.css            # Estilos base: reset, body y contenedor
│   ├── game-elements.css   # Elementos visuales: ahorcado, palabra y mensajes
│   └── controls.css        # Controles: inputs, botones y responsive
└── README.md               

## Requisitos Implementados

### Inicio Automático de la Partida

Cuando abres el archivo HTML en el navegador, el juego se inicia automáticamente sin necesidad de hacer nada más. En este momento se resetean todas las variables del juego, se genera una palabra aleatoria del array de palabras disponibles y se crean los huecos correspondientes para cada letra.

He implementado esto en el método `init()` de la clase HangmanGame, que se ejecuta automáticamente cuando se carga el DOM mediante un event listener de 'DOMContentLoaded'.

### Sistema de Entrada, Parseo y Validación

El usuario introduce letras en un campo de texto y confirma su intento mediante el botón "Adivinar" o presionando la tecla Enter. He añadido validaciones exhaustivas para asegurar que solo se procesen letras válidas y únicas:

- Compruebo que se haya introducido exactamente una letra
- Valido que sea una letra del alfabeto español (incluye acentos y ñ)
- Verifico que no se haya usado anteriormente esa misma letra

Si alguna validación falla, muestro un mensaje de error temporal que desaparece después de 2 segundos.

### Lógica de Victoria y Derrota

He implementado la lógica completa del juego con dos posibles finales:

**Si el jugador acierta una letra:**
- La letra se revela en todos los huecos donde aparezca
- Se añade a la lista de letras utilizadas
- Se comprueba si ha completado la palabra

**Si el jugador falla:**
- Se incrementa el contador de errores
- Se añade una nueva parte al dibujo del ahorcado
- Se reduce el contador de intentos restantes
- El input se sacude visualmente para indicar el error

**Victoria:**
Cuando el jugador adivina todas las letras únicas de la palabra, aparece un mensaje de "Has ganado" con estilo verde y se muestra el botón de reiniciar.

**Derrota:**
Cuando el jugador comete 6 errores (máximo de partes del ahorcado), aparece un mensaje de "Has perdido" en rojo revelando cuál era la palabra correcta, y también se muestra el botón de reiniciar.

**Código relevante:** `scripts/game.js` - método `checkGameState()`.

### Reinicio de Partida

El botón de reiniciar permanece oculto durante todo el juego y solo aparece cuando la partida finaliza, ya sea por victoria o derrota. Al hacer clic en él, se ejecuta de nuevo el método `init()` que genera una nueva palabra aleatoria y resetea completamente el estado del juego.

**Código relevante:** `scripts/game.js` - método `init()` vinculado al botón restart.

## Decisiones de Diseño

He optado por un diseño visual inspirado en estética Tron/neón que considero moderno y atractivo. La paleta de colores está basada en tonos neón (cian, magenta, verde) sobre fondos oscuros, lo que crea un buen contraste y facilita la lectura.

**Colores principales:**
- Cian (#00ffff) para elementos principales y bordes
- Verde neón (#00ff7f) para aciertos y victoria
- Rosa/Magenta (#ff0080, #ff00ff) para errores y derrota
- Amarillo (#ffff00) para acentos

He simplificado las animaciones para no sobrecargar visualmente la interfaz, ya que inicialmente me excedí. Solo mantuve las esenciales: efecto de sacudida en errores y transiciones suaves en los botones.

El diseño es completamente responsive, adaptándose a dispositivos móviles, tablets y escritorio mediante media queries.

## Características Adicionales

Más allá de los requisitos obligatorios, he implementado algunas mejoras:

- Validación en tiempo real del input (solo permite letras)
- Feedback visual inmediato en errores (sacudida)
- Contador de intentos restantes con código de colores
- Lista de letras ya utilizadas
- Navegación por teclado completa (Enter para adivinar)
- Enlace a mi perfil de GitHub en el footer

## Cómo Usar

1. Abre el archivo `index.html` en cualquier navegador moderno
2. El juego se inicia automáticamente
3. Escribe una letra en el campo de texto
4. Pulsa "Adivinar" o Enter
5. Continúa hasta ganar o perder
6. Pulsa "Reiniciar Partida" para jugar de nuevo

## Notas de Desarrollo

He organizado el código usando programación orientada a objetos con una clase `HangmanGame` que encapsula toda la lógica del juego. Esto hace que el código sea más mantenible y escalable.

Los archivos CSS están separados por responsabilidad: estilos base, elementos del juego y controles. Lo mismo con JavaScript: configuración separada de la lógica.

Todos los requisitos del enunciado están claramente marcados en los comentarios del código para facilitar la corrección.

---

## Extras

Esta actividad práctica supone un gran punto de partida y nos da como estudiantes una excelente oportunidad para repasar fundamentos del desarrollo web y abrir la puerta a lanzarnos a frameworks mucho mas complejos. 

---
![alt text](image.png)