/*Escribe un programa que declare dos variables String con valores “Hola” y “lector” y que compruebe si son iguales, su longitud, cuál es su segundo carácter, las concatene e imprima el substring de 2 a 6 del concatenado.

El método .substring() de la clase String permite obtener el substring de esa cadena. Por ejemplo, si tengo un String llamado cadena que contiene un “hola” si hago cadena.substring(0,2) el resultado será “hol”.*/ 

public class ex07 {
    public static void main(String[] args) {
        String s1 = "Hola";
        String s2 = "lector";

        boolean sonIguales = s1.equals(s2);
        System.out.println("Are they equal? " + sonIguales);

        int longitud1 = s1.length();
        int longitud2 = s2.length();
        System.out.println("The length of the first string is: " + longitud1);
        System.out.println("The length of the second string is: " + longitud2);

        char segundoCaracter1 = s1.charAt(1);
        char segundoCaracter2 = s2.charAt(1);
        System.out.println("The second character of the first string is: " + segundoCaracter1);
        System.out.println("The second character of the second string is: " + segundoCaracter2);

        String concatenado = s1.concat(s2);
        System.out.println("The concatenated string is: " + concatenado);

        String subString = concatenado.substring(2, 6);
        System.out.println("The substring from 2 to 6 is: " + subString);
    }
}