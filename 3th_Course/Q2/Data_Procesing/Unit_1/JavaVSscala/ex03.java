// flatMap
// conteo
// transformación de texto
// eliminación de duplicados
// ordenación por valor
// maps de frecuencia

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {

        List<String> frases = Arrays.asList(
                "hola mundo hola",
                "java y scala",
                "scala es potente",
                "hola scala"
        );

        Map<String, Long> resultado =
                frases.stream()
                        .flatMap(frase -> Arrays.stream(frase.split(" ")))
                        .map(String::toLowerCase)
                        .filter(palabra -> palabra.length() > 3)
                        .collect(Collectors.groupingBy(
                                Function.identity(),
                                Collectors.counting()
                        ));

        resultado.entrySet().stream()
                .sorted(Map.Entry.<String, Long>comparingByValue().reversed())
                .forEach(entry ->
                        System.out.println(entry.getKey() + ": " + entry.getValue())
                );
    }
}