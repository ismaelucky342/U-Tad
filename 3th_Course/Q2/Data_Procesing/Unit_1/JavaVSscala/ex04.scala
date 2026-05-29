// Version ex04 en scala puro 

/*
import java.util.*;
import java.util.stream.*;

class Alumno {
    String nombre;
    double nota;

    Alumno(String nombre, double nota) {
        this.nombre = nombre;
        this.nota = nota;
    }

    public String getNombre() {
        return nombre;
    }

    public double getNota() {
        return nota;
    }

    @Override
    public String toString() {
        return nombre + " (" + nota + ")";
    }
}

public class Main {

    public static void main(String[] args) {

        List<Alumno> alumnos = Arrays.asList(
                new Alumno("Ana", 7.5),
                new Alumno("Luis", 4.0),
                new Alumno("Marta", 8.2),
                new Alumno("Carlos", 6.8),
                new Alumno("Lucia", 9.1)
        );

        List<String> resultado =
                alumnos.stream()
                        .filter(a -> a.getNota() >= 5)
                        .sorted(Comparator.comparing(Alumno::getNota).reversed())
                        .map(a -> a.getNombre().toUpperCase())
                        .collect(Collectors.toList());

        resultado.forEach(System.out::println);
    }
}
*/

case class Alumno(nombre: String, nota: Double)

val alumnos = List(
  Alumno("Ana", 7.5),
  Alumno("Luis", 4.0),
  Alumno("Marta", 8.2),
  Alumno("Carlos", 6.8),
  Alumno("Lucia", 9.1)
)

val resultado = alumnos
  .filter(_.nota >= 5)
  .sortBy(-_.nota)
  .map(_.nombre.toUpperCase)
resultado.foreach(println)

