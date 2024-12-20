package ex11;

import java.util.Scanner;

/*DISFRUTALO SARA :)*/

public class ex11 {
    private static final String[] PALABRAS = {"HOLA", "MUNDO", "PROGRAMACION", "JAVA", "COMPUTADORA"}; // Guardo una lista de palabras.
    private static final int VIDAS_INICIALES = 5; // Defino el número de vidas iniciales que tendrá el jugador.
    private static final char CARACTER_OCULTO = '_'; // Uso este carácter para representar las letras ocultas en la palabra.

    private String palabra; // Aquí almaceno la palabra seleccionada para jugar.
    private char[] palabraOculta; // Creo un arreglo que representa la palabra oculta con caracteres.
    private int vidas; // Mantengo el registro de las vidas restantes del jugador.

    // Constructor
    public ex11() {
        // Selecciono una palabra aleatoria de la lista de palabras.
        palabra = PALABRAS[(int) (Math.random() * PALABRAS.length)];
        // Inicializo la palabra oculta con guiones bajos para que no se revele.
        palabraOculta = new char[palabra.length()];
        for (int i = 0; i < palabraOculta.length; i++) {
            palabraOculta[i] = CARACTER_OCULTO;
        }
        // Asigno las vidas iniciales al jugador.
        vidas = VIDAS_INICIALES;
    }

    // Método para jugar
    public void jugar() {
        Scanner sc = new Scanner(System.in);
        boolean terminado = false;

        // Mientras el jugador tenga vidas y no haya adivinado la palabra.
        while (!terminado) {
            // Muestro la palabra oculta al jugador.
            System.out.println("Palabra: " + new String(palabraOculta));
            // Pido al jugador que introduzca una letra.
            System.out.print("Introduce una letra: ");
            char letra = sc.nextLine().toUpperCase().charAt(0);

            // Reviso si la letra ingresada está en la palabra.
            boolean encontrada = false;
            for (int i = 0; i < palabra.length(); i++) {
                if (palabra.charAt(i) == letra) {
                    palabraOculta[i] = letra; // Si la letra está, la revelo en la palabra oculta.
                    encontrada = true;
                }
            }

            // Si la letra no está en la palabra, le quito una vida al jugador.
            if (!encontrada) {
                vidas--;
                System.out.println("La letra " + letra + " no está en la palabra. Vidas restantes: " + vidas);
            }

            // Compruebo si el jugador ha adivinado la palabra completa.
            if (new String(palabraOculta).equals(palabra)) {
                System.out.println("¡Has adivinado la palabra!");
                terminado = true;
            }

            // Si el jugador se queda sin vidas, termino el juego.
            if (vidas == 0) {
                System.out.println("¡Te has quedado sin vidas! La palabra era " + palabra);
                terminado = true;
            }
        }
        sc.close(); // Cierro el scanner después de terminar el juego.
    }

    // Método main para iniciar el juego
    public static void main(String[] args) {
        ex11 ahorcado = new ex11(); // Creo una instancia del juego.
        ahorcado.jugar(); // Inicio el juego.
    }
}
