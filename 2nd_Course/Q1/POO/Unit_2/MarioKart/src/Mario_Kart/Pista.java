package Mario_Kart;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Pista {
    private String nombre;
    private int longitud;
    private TipoPista tipo;
    private List<Obstaculo> obstaculos;
    private List<Item> items;
    private Map<Integer, String> puntosClave;

    public Pista(String nombre, int longitud, TipoPista tipo) {
        this.nombre = nombre;
        this.longitud = longitud;
        this.tipo = tipo;
        this.obstaculos = new ArrayList<>();
        this.items = new ArrayList<>();
        this.puntosClave = new HashMap<>();
        inicializarPuntosClave();
    }

    private void inicializarPuntosClave() {
        puntosClave.put(longitud / 4, "¡Primera curva!");
        puntosClave.put(longitud / 2, "¡Media carrera!");
        puntosClave.put(longitud * 3 / 4, "¡Última recta!");
    }

    public void agregarObstaculo(Obstaculo obstaculo) {
        obstaculos.add(obstaculo);
    }

    public void agregarItem(Item item) {
        items.add(item);
    }

    public String checkPuntoClave(int posicion) {
        return puntosClave.getOrDefault(posicion, null);
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public int getLongitud() {
        return longitud;
    }

    public List<Obstaculo> getObstaculos() {
        return obstaculos;
    }

    public List<Item> getItems() {
        return items;
    }

    public double getFactorDificultad() {
        return tipo.getFactorDificultad();
    }
}
