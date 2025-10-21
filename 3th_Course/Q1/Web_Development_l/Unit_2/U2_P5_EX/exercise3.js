/*
Crea una función en JavaScript llamada `calcularPromedio` que tome tres notas de un estudiante como parámetros y devuelva el promedio de las notas. El programa debe:

    Pedir al usuario que ingrese tres notas.

    Usar la función `calcularPromedio` para calcular el promedio de las tres notas.

    Mostrar el promedio en la consola.

Deberás:

    Crear una función llamada `calcularPromedio` que reciba tres parámetros.

    Calcular el promedio dentro de la función y retornar el resultado.

    Mostrar el promedio utilizando la función en el programa principal.

Ejemplo de salida:

Nota 1: 85

Nota 2: 90

Nota 3: 78

Promedio: 84.33
*/

// Función para calcular el promedio de tres notas
function calcularPromedio(nota1, nota2, nota3) {
    return (nota1 + nota2 + nota3) / 3;
}

// Pedir al usuario que ingrese tres notas
const nota1 = parseFloat(prompt("Ingresa la primera nota:"));
const nota2 = parseFloat(prompt("Ingresa la segunda nota:"));
const nota3 = parseFloat(prompt("Ingresa la tercera nota:"));

// Calcular el promedio usando la función
const promedio = calcularPromedio(nota1, nota2, nota3);

// Mostrar el promedio en la consola
console.log("Nota 1: " + nota1);
console.log("Nota 2: " + nota2);
console.log("Nota 3: " + nota3);
console.log("Promedio: " + promedio.toFixed(2));

