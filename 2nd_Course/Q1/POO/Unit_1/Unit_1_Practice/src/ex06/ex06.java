/*
 * Crea dos arrays multidimensionales de 2×3 y rellénalos como quieras.
 * Haz un método que sume los arrays multidimensionales, es decir, la posición 0 del array1 con la posición 0 del array2 y así sucesivamente.
 * Este método no debe devolver nada, haciendo que deba pasarse el array multidimensional de suma como parámetro.
 * Muestra el contenido de cada array multidimensional.
*/
package ex06;

import java.util.Arrays;

public class ex06 {
	public static void main(String[] args) {
		int[][] array1 = {{1, 2, 3},{4, 5, 6}}; 
		int[][] array2 = {{7, 8, 9},{10, 11, 12}};
		int[][] suma = new int[2][3]; 
		
		sumarArrays(array1, array2, suma);
		
		/*
		 * convierte un array multidimensional en una representación de cadena (string)
		 * que incluye su contenido de forma jerárquica.
		 * */
		System.out.println("Array 1: " + Arrays.deepToString(array1));
		System.out.println("Array 2: " + Arrays.deepToString(array2));
		System.out.println("Suma: " + Arrays.deepToString(suma));
	}
	public static void sumarArrays(int[][] a, int[][] b, int[][] result) {
		for (int i = 0; i < a.length; i++) {
			for(int j = 0;  j < a[0].length; j++) {
				result[i][j] = a[i][j] + b[i][j]; 
			}
		}
		
	}
}
