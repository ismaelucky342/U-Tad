package ex08;

public class e08 {

	public static void main(String[] args) {

		 // Declarar las variables String
        String str1 = "Hola";
        String str2 = "lector";

        // Comparar si son iguales
        boolean sonIguales = str1.equals(str2);
        System.out.println("¿Son iguales?: " + sonIguales);

        // Imprimir la longitud de cada cadena
        System.out.println("Longitud de \"" + str1 + "\": " + str1.length());
        System.out.println("Longitud de \"" + str2 + "\": " + str2.length());

        // Obtener y mostrar el segundo carácter de cada cadena
        char segundoCharStr1 = str1.charAt(1); // Índice 1 = segundo carácter
        char segundoCharStr2 = str2.charAt(1);
        System.out.println("Segundo carácter de \"" + str1 + "\": " + segundoCharStr1);
        System.out.println("Segundo carácter de \"" + str2 + "\": " + segundoCharStr2);

        // Concatenar las dos cadenas
        String concatenado = str1 + str2;
        System.out.println("Concatenación: " + concatenado);

        // Obtener el substring de 2 a 6 del concatenado
        String substring = concatenado.substring(2, 6);
        System.out.println("Substring (2, 6) del concatenado: " + substring);
    }
}