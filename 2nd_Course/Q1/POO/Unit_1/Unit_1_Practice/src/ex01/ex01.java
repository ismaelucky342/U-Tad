/*
 * Escribir un programa que lea un número entero por la entrada estándar, 
 * lo multiplique por 20 e imprima su división por 10. 
 * A continuación debe sumarlo a la multiplicación y volver a 
 * imprimir su división por 10. 
 * Si el resto no es 0, debe imprimirlo también
 * 
 * */
package ex01;
import java.util.Scanner;

public class ex01 {
	
	public static void main(String[] args) {
		Scanner lector = new Scanner(System.in); 
		System.out.println("introduce un numero entero: ");
		int n1 = lector.nextInt();
		int multi = n1 * 20; 
		double divi = multi / 10; 
		System.out.println("el resultado de la multi es: " + multi + " y el de la divi: " + divi);
		
		int sum = multi + n1; 
		double divi2 = sum / 10; 
		System.out.println("el resultado de la suma mas la divi es: " + divi2);
		
		int rest = sum % 10; 
		if(rest != 0) {
			System.out.println("el resto no es 0 por tanto es: " + rest);
		}
	}
	

}
