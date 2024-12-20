/*
 * Escribir un programa en Java que calcule el valor de la suma de todos los elementos de un array de enteros,
 *  e imprima el resultado por pantalla.
 * Nota: Podéis usar .length en un array para conocer su longitud
 * */
package ex05;

public class ex05 {
	public static void main(String[] args) {
		int[] num = {1, 2, 3, 4, 5};
		
		int sum = 0; 
		int i = 0; 
			
		while(i < num.length) {
			sum += num[i]; 
			i++; 
		}
		System.out.println("la suma de los elementos del array es: " + sum);
	}
}
