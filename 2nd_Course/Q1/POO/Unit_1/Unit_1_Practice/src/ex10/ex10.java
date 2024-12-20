package ex10;

public class ex10 {

    // Método para multiplicar dos matrices
    public static int[][] multiplyMatrices(int[][] mat1, int[][] mat2) {
        int rows1 = mat1.length;
        int cols1 = mat1[0].length;
        int rows2 = mat2.length;
        int cols2 = mat2[0].length;

        // Verificar si las dimensiones son compatibles
        if (cols1 != rows2) {
            throw new IllegalArgumentException("Dimensiones incompatibles para multiplicar matrices");
        }

        // Crear la matriz resultado
        int[][] result = new int[rows1][cols2];

        // Multiplicar las matrices
        for (int i = 0; i < rows1; i++) {
            for (int j = 0; j < cols2; j++) {
                for (int k = 0; k < cols1; k++) {
                    result[i][j] += mat1[i][k] * mat2[k][j];
                }
            }
        }

        return result;
    }

    // Método para imprimir una matriz
    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int value : row) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
    }

    // Ejemplo de uso
    public static void main(String[] args) {
        // Matriz 1: 2x3
        int[][] mat1 = {
            {1, 2, 3},
            {4, 5, 6}
        };

        // Matriz 2: 3x2
        int[][] mat2 = {
            {7, 8},
            {9, 10},
            {11, 12}
        };

        // Multiplicar matrices
        try {
            int[][] result = multiplyMatrices(mat1, mat2);

            // Imprimir la matriz resultado
            System.out.println("Resultado de la multiplicación:");
            printMatrix(result);
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}
