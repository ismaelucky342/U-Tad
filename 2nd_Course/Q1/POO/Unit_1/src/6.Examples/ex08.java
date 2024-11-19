/*Programar un método que reciba como argumento un array de enteros y devuelva un nuevo array idéntico al anterior (un método clonador).*/

import java.util.Arrays;

public class ex08 {
    public static int[] clonarArray(int[] array) {
        int[] newArray = new int[array.length];
        for (int i = 0; i < array.length; i++) {
            newArray[i] = array[i];
        }
        return newArray;
    }
}