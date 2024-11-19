/*  Escribir un programa en Java que calcule el valor de la suma de todos los elementos de un array de enteros, e imprima el resultado por pantalla.

Nota: Podéis usar .length en un array para conocer su longitud */

import java.util.Scanner;

public class ex04 {
    public static void main (String[] args) {
        int[] numeros = {1, 2, 3, 4, 5};
        int suma = 0;

        for (int i = 0; i < numeros.length; i++) {
            suma += numeros[i];
        }
        System.out.println("The result is: " + suma);
    }
}