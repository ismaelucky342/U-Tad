// otro ejemplo basico de solucion en java

import java.util.*;
import java.util.stream.*;

public class Main {

    public static void main(String[] args) {

        List<String> nombres = Arrays.asList(
                "Ana",
                "Luis",
                "Alberto",
                "Lucia",
                "Andres",
                "Maria",
                "Alicia"
        );

        Map<Character, List<String>> resultado =
                nombres.stream()
                        .filter(nombre -> nombre.length() > 4)
                        .map(String::toUpperCase)
                        .sorted()
                        .collect(Collectors.groupingBy(nombre -> nombre.charAt(0)));

        resultado.forEach((letra, lista) -> {
            System.out.println(letra + " -> " + lista);
        });
    }
}