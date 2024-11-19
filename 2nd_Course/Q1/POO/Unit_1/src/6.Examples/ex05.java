/* Crea dos arrays multidimensionales de 2×3 y rellénalos como quieras.
    Haz un método que sume los arrays multidimensionales, es decir, la posición 0 del array1 con la posición 0 del array2 y así sucesivamente.
    Este método no debe devolver nada, haciendo que deba pasarse el array multidimensional de suma como parámetro.
    Muestra el contenido de cada array multidimensional. */

import java.util.Arrays;

public class ex05 {
     public static void main(String[] args) {
          // Declaración de un arreglo bidimensional (matriz) llamado array1 con valores iniciales
          int[][] array1 = {{1, 2, 3}, {4, 5, 6}};

          // Declaración de otro arreglo bidimensional (matriz) llamado array2 con valores iniciales
          int[][] array2 = {{7, 8, 9}, {10, 11, 12}};

          // Declaración de un arreglo bidimensional (matriz) llamado arraySum para almacenar la suma de array1 y array2
          // Inicialmente, todos los elementos de arraySum son 0
          int[][] arraySum = new int[2][3];

          // Imprime el contenido de array1 en la consola
          System.out.println("Array 1: " + Arrays.deepToString(array1));

          // Imprime el contenido de array2 en la consola
          System.out.println("Array 2: " + Arrays.deepToString(array2));

          // Llama al método sumArrays para sumar array1 y array2 y almacenar el resultado en arraySum
          sumArrays(array1, array2, arraySum);

          // Imprime el contenido de arraySum en la consola
          System.out.println("Array Sum: " + Arrays.deepToString(arraySum));
     }

     // Declaración de un método estático llamado sumArrays que toma tres matrices bidimensionales como parámetros
     public static void sumArrays(int[][] array1, int[][] array2, int[][] arraySum) {
          // Itera sobre cada fila de array1
          for (int i = 0; i < array1.length; i++) {
                // Itera sobre cada columna de la fila actual de array1
                for (int j = 0; j < array1[i].length; j++) {
                     // Suma los elementos correspondientes de array1 y array2 y almacena el resultado en arraySum
                     arraySum[i][j] = array1[i][j] + array2[i][j];
                }
          }
     }
}
