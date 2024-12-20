package ex03;

/*
 * Escribir un programa que calcule el mínimo, el máximo 
 * y la media de una lista de números enteros positivos introducidos por el usuario. 
 * La lista finalizará cuando se introduzca un número negativo.
 * 
 * */
import java.util.Scanner;

public class ex03 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in); 
		int numero, maximo, minimo, suma = 0, cantidad = 0; 
		
		System.out.println("introduce un numero positivo: ");
		numero = scanner.nextInt(); 
		minimo = maximo = numero; 
		
		while(numero >= 0) {
			suma += numero; 
			cantidad++; 
			if(numero < minimo)
				minimo = numero; 
			if(numero > maximo)
				maximo = numero; 
			System.out.println("introduce otro numero positivo para continuar o negativo si quieres terminar: ");
			numero = scanner.nextInt(); 	
		}
		if (cantidad > 0) {
			double media = (double) suma / cantidad; 
			System.out.println("Mínimo: " + minimo);
			System.out.println("Maximo: "+ maximo);
			System.out.println("Media: " + media);
		} else {
			System.out.println("no se introdujeron numeros positivos!");
		}
	}
}
