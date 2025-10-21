/*
Crea un programa en JavaScript que simule una calculadora simple. El programa debe:

    Pedir al usuario que ingrese dos números.

    Aplicar las siguientes operaciones aritméticas: suma, resta, multiplicación, y división.

    Mostrar el resultado de cada operación en la consola.

Deberás:

    Utilizar variables para almacenar los números ingresados por el usuario.

    Utilizar operadores aritméticos para realizar las operaciones.

    Mostrar los resultados de cada operación en la consola.

Ejemplo de salida:

Número 1: 10

Número 2: 5

Suma: 15

Resta: 5

Multiplicación: 50

División: 2
*/

// Pedir al usuario que ingrese dos números
const numero1 = parseFloat(prompt("Ingresa el primer número:"));
const numero2 = parseFloat(prompt("Ingresa el segundo número:"));

// Realizar las operaciones aritméticas
const suma = numero1 + numero2;
const resta = numero1 - numero2;
const multiplicacion = numero1 * numero2;
const division = numero1 / numero2;

// Mostrar los resultados en la consola
console.log("Número 1: " + numero1);
console.log("Número 2: " + numero2);
console.log("Suma: " + suma);
console.log("Resta: " + resta);
console.log("Multiplicación: " + multiplicacion);
console.log("División: " + division);

