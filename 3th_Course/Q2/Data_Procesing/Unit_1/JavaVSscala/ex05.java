// agrupación avanzada: medias/promedios: mapValues: groupMapReduce posible: trabajar con objetos + agregación

import java.util.*;
import java.util.stream.*;

class Producto {
    String nombre;
    String categoria;
    double precio;

    Producto(String nombre, String categoria, double precio) {
        this.nombre = nombre;
        this.categoria = categoria;
        this.precio = precio;
    }

    public String getNombre() {
        return nombre;
    }

    public String getCategoria() {
        return categoria;
    }

    public double getPrecio() {
        return precio;
    }

    @Override
    public String toString() {
        return nombre + " - " + precio;
    }
}

public class Main {

    public static void main(String[] args) {

        List<Producto> productos = Arrays.asList(
                new Producto("Portatil", "Tecnologia", 1200),
                new Producto("Raton", "Tecnologia", 25),
                new Producto("Silla", "Hogar", 150),
                new Producto("Mesa", "Hogar", 300),
                new Producto("Monitor", "Tecnologia", 400)
        );

        Map<String, Double> resultado =
                productos.stream()
                        .collect(Collectors.groupingBy(
                                Producto::getCategoria,
                                Collectors.averagingDouble(Producto::getPrecio)
                        ));

        resultado.forEach((categoria, media) ->
                System.out.println(categoria + ": " + media)
        );
    }
}