/*
Escribir un programa en Java que calcule el producto de tres números enteros introducidos por el usuario.
*/

import  java.util.Scanner; 

public class ex00 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int num1, num2, num3, resultado; 

        System.out.println("Insert first digit: ");
        num1 = entrada.nextInt();

        System.out.println("Insert second digit: ");
        num2 = entrada.nextInt();

        System.out.println("Insert third digit: ");
        num3 = entrada.nextInt();

        resultado = num1 * num2 * num3; 

        System.out.println("The product is: " + resultado);

    }


}