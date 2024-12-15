package Mario_Kart;

public enum TipoPista {
    HIERBA("Circuito Verde", 0.8),
    DESIERTO("Desierto Seco", 1.0),
    HIELO("Pista Helada", 1.2),
    ARCOIRIS("Senda Arcoíris", 1.5);

    private final String nombre;
    private final double factorDificultad;

    TipoPista(String nombre, double factorDificultad) {
        this.nombre = nombre;
        this.factorDificultad = factorDificultad;
    }

    public String getNombre() {
        return nombre;
    }

    public double getFactorDificultad() {
        return factorDificultad;
    }
}