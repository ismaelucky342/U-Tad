//Programar un juego del ahorcado.

import java.util.Scanner;

public class ex10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] words = {"programacion", "java", "ahorcado", "computadora"};
        String word = words[(int) (Math.random() * words.length)];
        char[] guessedWord = new char[word.length()];
        for (int i = 0; i < guessedWord.length; i++) {
            guessedWord[i] = '_';
        }
        int attempts = 6;
        boolean wordGuessed = false;

        while (attempts > 0 && !wordGuessed) {
            System.out.println("Palabra: " + new String(guessedWord));
            System.out.println("Intentos restantes: " + attempts);
            System.out.print("Introduce una letra: ");
            char guess = scanner.next().charAt(0);
            boolean correctGuess = false;

            for (int i = 0; i < word.length(); i++) {
                if (word.charAt(i) == guess) {
                    guessedWord[i] = guess;
                    correctGuess = true;
                }
            }

            if (!correctGuess) {
                attempts--;
            }

            wordGuessed = true;
            for (char c : guessedWord) {
                if (c == '_') {
                    wordGuessed = false;
                    break;
                }
            }
        }

        if (wordGuessed) {
            System.out.println("¡Felicidades! Has adivinado la palabra: " + word);
        } else {
            System.out.println("Lo siento, has perdido. La palabra era: " + word);
        }

        scanner.close();
    }
}