package Mario_Kart;

public class Item {
    private String nombre;
    private String efecto;
    private int duracion;

    public Item(String nombre, String efecto, int duracion) {
        this.nombre = nombre;
        this.efecto = efecto;
        this.duracion = duracion;
    }

    public void aplicarEfecto(Personaje personaje) {
        System.out.println(personaje.getNombre() + " usa " + nombre + "!");
        switch (efecto) {
            case "velocidad":
                personaje.getKart().aumentarVelocidadMaxima(30, duracion);
                break;
            case "inmunidad":
                personaje.setInmunidad(true, duracion);
                break;
            case "miniturbo":
                personaje.getKart().aplicarMiniturbo();
                break;
        }
    }

    public String getNombre() {
        return nombre;
    }

    public String getEfecto() {
        return efecto;
    }

    public int getDuracion() {
        return duracion;
    }
}