// Version ex03 scala puro 

/*

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
*/

val frases = List("hola mundo hola", "java y scala", "scala es potente", "hola scala")

val resultado = frases
  .flatMap(frase => frase.split(" "))
  .map(_.toLowerCase)
  .filter(_.length > 3)
  .groupBy(identity)
  .view.mapValues(_.size.toLong)
  .toMap

resultado.toSeq.sortBy(-_._2).foreach { case (palabra, count) =>
    println(s"$palabra: $count")
    }
    