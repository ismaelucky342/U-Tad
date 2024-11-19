package Mario_Kart;

public class Obstaculo {
    private String nombre;
    private String efecto;

    public Obstaculo(String nombre, String efecto) {
        this.nombre = nombre;
        this.efecto = efecto;
    }

    public void aplicarEfecto(Kart kart) {
        System.out.println("¡" + kart.getNombre() + " ha chocado con " + nombre + "!");
        if (efecto.equals("chocar")) {
            kart.chocar();
        } else if (efecto.equals("ralentizar")) {
            kart.frenar();
        }
    }

    public String getNombre() {
        return nombre;
    }

    public String getEfecto() {
        return efecto;
    }
}