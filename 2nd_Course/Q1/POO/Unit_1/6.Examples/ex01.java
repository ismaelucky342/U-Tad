/*
Escribir un programa que lea un número entero por la entrada estándar, lo multiplique por 20 e imprima su división por 10. A continuación debe sumarlo a la multiplicación y volver a imprimir su división por 10. Si el resto no es 0, debe imprimirlo también
*/

import java.util.Scanner;

public class ex01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Introduce un número entero: ");
        int numero = scanner.nextInt();
        
        int multiplicacion = numero * 20;
        int division1 = multiplicacion / 10;
        System.out.println("Resultado de la división por 10 de la multiplicación: " + division1);
        
        int suma = numero + multiplicacion;
        int division2 = suma / 10;
        System.out.println("Resultado de la división por 10 de la suma: " + division2);
        
        int resto = suma % 10;
        if (resto != 0) {
            System.out.println("El resto es: " + resto);
        }
        
        scanner.close();
    }
}
