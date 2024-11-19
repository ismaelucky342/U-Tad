/*Programar un método que reciba como argumentos dos matrices bidimensionales y devuelva el resultado de multiplicarlas.*/

public class ex09{
    public static int[][] multiplicarMatrices(int[][] matriz1, int[][] matriz2) {
    int filasMatriz1 = matriz1.length;
    int columnasMatriz1 = matriz1[0].length;
    int columnasMatriz2 = matriz2[0].length;
    int[][] resultado = new int[filasMatriz1][columnasMatriz2];
    for (int i = 0; i < filasMatriz1; i++) {
        for (int j = 0; j < columnasMatriz2; j++) {
            for (int k = 0; k < columnasMatriz1; k++) {
                resultado[i][j] += matriz1[i][k] * matriz2[k][j];
            }
        }
    }
    return resultado;
}
}