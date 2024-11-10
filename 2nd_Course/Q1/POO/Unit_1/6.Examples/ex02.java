/*
Escribir en Java un programa que lea de forma repetida un número N. Para cada número leído el programa calculará la suma 1+2+3…+N. Una vez mostrado el resultado, el programa preguntará al usuario si desea continuar; si se introduce “s” el programa continuará con la ejecución, en caso contrario finalizará.

Nota: La clase String tiene un método String.charAt() que permite conocer un carácter dentro de la cadena de dicho string. Por ejemplo, si tengo un String llamado cadena que contiene un “hola”, al hacer cadena.charAt(0) tendré como resultado el carácter “h”
 */

import java.util.Scanner;

public class ex02{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        char continuar = 's';
        while(continuar == 's'){
            System.out.println("Introduce un número: ");
            int n = sc.nextInt();
            int suma = 0;
            for(int i = 1; i <= n; i++){
                suma += i;
            }
            System.out.println("La suma de los primeros " + n + " números es: " + suma);
            System.out.println("¿Desea continuar? (s/n)");
            continuar = sc.next().charAt(0);
        }
        sc.close();
    }
}