package ex07;

public class ex07 {
    public static void main(String[] args) {
        System.out.println("Letra | Código ASCII");
        System.out.println("--------------------");

        for (char letra = 'a'; letra <= 'z'; letra++) {
            System.out.printf("   %c   |     %d%n", letra, (int) letra);
        }
    }
}

