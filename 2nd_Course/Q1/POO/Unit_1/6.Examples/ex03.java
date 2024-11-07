/*
Escribir un programa que calcule el mínimo, el máximo y la media de una lista de números enteros positivos introducidos por el usuario. 
La lista finalizará cuando se introduzca un número negativo.
*/

import java.util.Scanner;

public class ex03{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int suma = 0;
        int n = 0;
        int contador = 0;
        System.out.println("Introduce un número: ");
        n = sc.nextInt();
        while(n >= 0){
            if(n < min){
                min = n;
            }
            if(n > max){
                max = n;
            }
            suma += n;
            contador++;
            System.out.println("Introduce un número: ");
            n = sc.nextInt();
        }
        if(contador > 0){
            System.out.println("Mínimo: " + min);
            System.out.println("Máximo: " + max);
            System.out.println("Media: " + (double)suma/contador);
        }else{
            System.out.println("No se ha introducido ningún número");
        }
    }
}