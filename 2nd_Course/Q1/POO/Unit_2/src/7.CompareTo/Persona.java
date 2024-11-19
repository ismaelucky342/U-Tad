public class Persona implements Comparable<Persona> {
    
    private String nombre;
    public Persona(String nombre) {
        this.nombre = nombre;
    }
    @Override
    public int compareTo(Persona otraPersona) {
        return this.nombre.compareTo(otraPersona.nombre);
    }

}