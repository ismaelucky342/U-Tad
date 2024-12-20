/*Escribir en Java un programa que lea de forma repetida un número N. 
 * Para cada número leído el programa calculará la suma 1+2+3…+N. 
 * Una vez mostrado el resultado, el programa preguntará al usuario si desea continuar; 
 * si se introduce “s” el programa continuará con la ejecución, en caso contrario finalizará.
 * Nota: La clase String tiene un método String.charAt() que permite conocer un carácter dentro 
 * de la cadena de dicho string. Por ejemplo, si tengo un String llamado cadena que contiene un “hola”, 
 * al hacer cadena.charAt(0) tendré como resultado el carácter “h”
 * 
 */
package ex02;

import java.util.Scanner;

public class ex02 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in); 
		
		char respuesta = 's'; 
		
		while(respuesta == 's') {
			System.out.println("introduce un numero entero: ");
			
			int n = scanner.nextInt(); 
			int sum = 0; 
			int i = 1; 
			while(i <= n)
			{
				sum += i; 
				i++; 
			}
			System.out.println("la suma de los primeros" + n + "numero de enteros es: " + sum);
			System.out.println("desea continuar? (y/n)");
			respuesta = scanner.next().charAt(0); 
		}
		scanner.close();
	}
}
