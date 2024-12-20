package ex09;

public class ex09 {
    public static void main(String[] args) {
        // Array original
        int[] originalArray = {1, 2, 3, 4, 5};

        // Clonar el array
        int[] clonedArray = cloneArray(originalArray);

        // Imprimir ambos arrays para verificar
        System.out.println("Array original: ");
        printArray(originalArray);

        System.out.println("Array clonado: ");
        printArray(clonedArray);
    }

    // Método para clonar un array de enteros
    public static int[] cloneArray(int[] array) {
        if (array == null) {
            return null; // Manejo de array nulo
        }
        // Crear un nuevo array del mismo tamaño
        int[] clonedArray = new int[array.length];

        // Copiar los elementos
        for (int i = 0; i < array.length; i++) {
            clonedArray[i] = array[i];
        }

        return clonedArray;
    }

    // Método auxiliar para imprimir un array
    public static void printArray(int[] array) {
        if (array == null) {
            System.out.println("null");
            return;
        }
        for (int value : array) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}

