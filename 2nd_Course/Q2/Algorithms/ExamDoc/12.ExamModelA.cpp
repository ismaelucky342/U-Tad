/*
Problema 1. Desarrollar una función para calcular la media de un vector de floats con al menos un
elemento. Por ejemplo, dado el vector:
1.2 2.0 -1.0 0.0 2.8 -0.5 3.2
La función deberá devolver el valor 1.1
La implementación propuesta deberá seguir el esquema de divide y vencerás. La función deberá tener la
siguiente cabecera:
float obtenerMedia (float *valores, int n) {
}
Se podrán crear tantas funciones auxiliares como sean necesarias. También podrá crearse un main para
comprobar el correcto funcionamiento de la solución planteada. No es obligatorio, pero es recomendable.
Pista. Dada la lista de L números con media mL, es posible calcular la media de la misma lista de números
tras añadir un nuevo elemento N sin necesidad de recorrer toda la lista. Para ello usaremos la siguiente
expresión: mL+1 = (L * mL + N) / (L + 1)
Por ejemplo, si a la lista de números del ejemplo anterior le añadimos el número 4.2 la media pasará a ser:
media = (7 * 1.1 + 4.2) / (7 + 1) = 1.4875
*/

