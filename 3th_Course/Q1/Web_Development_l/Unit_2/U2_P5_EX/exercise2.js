/*
Crea un programa en JavaScript que determine si un número ingresado por el usuario es par o impar. El programa debe:

    Pedir al usuario que ingrese un número.

    Verificar si el número es par o impar utilizando una sentencia condicional (`if`).

    Mostrar un mensaje en la consola indicando si el número es par o impar.

Deberás:

    Utilizar el operador de módulo (%) para determinar si el número es divisible entre 2.

    Usar una estructura condicional `if-else` para verificar el resultado.

    Mostrar un mensaje claro en la consola.

Ejemplo de salida:

Número ingresado: 8

El número es par.
*/

// Pedir al usuario que ingrese un número
const numero = parseInt(prompt("Ingresa un número:"));

// Verificar si el número es par o impar
if (numero % 2 === 0) {
    console.log("Número ingresado: " + numero);
    console.log("El número es par.");
} else {
    console.log("Número ingresado: " + numero);
    console.log("El número es impar.");
} 