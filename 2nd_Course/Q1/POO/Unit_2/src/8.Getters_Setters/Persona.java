public class Persona {
    private String nombre;
    public Persona(String nombre) {
        this.nombre = nombre; // Uso de 'this' para referenciar el atributo nombre
    }
    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}