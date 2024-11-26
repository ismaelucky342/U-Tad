package astralis;

public class Nave {
    private String tipo;              // Tipo de nave (por ejemplo, "Destructor", "Cazador", etc.)
    private int poderDeAtaque;        // El poder de ataque de la nave
    private String counter;           // El tipo de nave contra la que esta nave es efectiva (counter)

    // Constructor
    public Nave(String tipo, int poderDeAtaque, String counter) {
        this.tipo = tipo;                    // Establece el tipo de nave
        this.poderDeAtaque = poderDeAtaque;  // Establece el poder de ataque
        this.counter = counter;              // Establece el counter (la nave contra la que es efectiva)
    }

    // Métodos getters
    public String getTipo() {
        return tipo;
    }

    public int getPoderDeAtaque() {
        return poderDeAtaque;
    }

    public String getCounter() {
        return counter;
    }

    // Método para establecer el poder de ataque de la nave
    public void setPoderDeAtaque(int poderDeAtaque) {
        this.poderDeAtaque = poderDeAtaque;
    }

    // Método para mostrar los detalles de la nave
    public void mostrarDetalles() {
        System.out.println("Tipo de nave: " + tipo);
        System.out.println("Poder de ataque: " + poderDeAtaque);
        System.out.println("Counter: " + counter);
    }
}
