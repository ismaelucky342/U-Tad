/*
 * Escribir un programa en Java que calcule el 
 * producto de tres números enteros introducidos por el usuario.
 * syso ctrl espacio -> system out print
**/

package ex00;

import java.util.Scanner;

public class ex00 {
	
	public static void main(String[] args) {
		try (Scanner lector = new Scanner(System.in)) {
			int n1, n2, n3, result; 
			
			System.out.println("introduce primer numero: ");
			n1 = lector.nextInt();
			
			System.out.println("introduce segundo numero: ");
			n2= lector.nextInt();
			
			System.out.println("introduce tercer numero" );
			n3= lector.nextInt();
			
			result = n1 * n2 * n3;
			System.out.println("El producto de los tres numeros es: " + result );
		}
		
	}
}
