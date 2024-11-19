public class Coche {
    String marca;
    int velocidad;

    public Coche(String marca) {
        this.marca = marca;
        this.velocidad = 0;
    }

    public void acelerar() {
        velocidad += 10;
        System.out.println("El coche " + marca + " está a " + velocidad + " km/h.");
    }

    public static void main(String[] args) {
        Coche miCoche = new Coche("Toyota");
        miCoche.acelerar();
    }
}
