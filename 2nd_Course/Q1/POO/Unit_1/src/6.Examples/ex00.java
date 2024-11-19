/*
Escribir un programa en Java que calcule el producto de tres números enteros introducidos por el usuario.
*/
import java.util.Scanner;

public class ex00 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n1, n2, n3, result; 

        System.out.println("Introduce first number: ");
        n1 = sc.nextInt(); 
        System.out.println("Introduce second number: ");
        n2 = sc.nextInt(); 
        System.out.println("Introduce third number: ");
        n3 = sc.nextInt(); 

        result = n1 * n2 * n3;
        System.out.println("The result is: " + result);
    }
}