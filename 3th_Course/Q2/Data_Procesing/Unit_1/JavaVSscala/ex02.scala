// ex02 traducido a scala
/*
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
*/
val nombres = List("Ana", "Luis", "Alberto", "Lucia", "Andres", "Maria", "Alicia")

val filtrados = nombres.filter(nombre => nombre.length > 4)

val mayusculas = filtrados.map(nombre => nombre.toUpperCase)

val ordenados = mayusculas.sorted

val resultado = ordenados.groupBy(nombre => nombre.charAt(0))

resultado.foreach(par => {
  val letra = par._1
  val lista = par._2

  println(letra + " -> " + lista)
})

// En version de estilo scala puro

val resultadoPuro = nombres
  .filter(_.length > 4)
  .map(_.toUpperCase)
  .sorted
  .groupBy(_.head)

resultadoPuro.foreach { case (letra, lista) =>
  println(s"$letra -> $lista")
}