/*
Escribir un programa que lea un número entero por la entrada estándar, lo multiplique por 20 e imprima su división por 10. A continuación debe sumarlo a la multiplicación y volver a imprimir su división por 10. Si el resto no es 0, debe imprimirlo también
*/

import java.util.Scanner;

public class ex01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduce a number: \n");
        int number = scanner.nextInt();

        int result = number * 20;
        double division = result / 10; 
        System.out.println("The result is: " + division);

        int sum = result + number;
        double result2 = sum / 10;
        System.out.println("The result is: " + result2);

        int resit = sum % 10;
        if (resit != 0) {
            System.out.println("The rest is: " + resit);
        }
        scanner.close();
    }
}
