//Escribe un programa que imprima por pantalla las letras minúsculas y su código ASCII.

import java.util.Scanner;

public class ex06 {
    public static void main(String[] args) {
        for (char c = 'a'; c <= 'z'; c++) {
            System.out.println("The ASCII code of " + c + " is: " + (int) c);
        }
    }
}