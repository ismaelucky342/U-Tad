package Zoo;

public abstract class Animal {
    private String nombre;
    private int edad;
    private double peso;
    private Habitat habitat;

    // Constructor
    public Animal(String nombre, int edad, double peso, Habitat habitat) {
        this.nombre = nombre;
        this.edad = edad;
        this.peso = peso;
        this.habitat = habitat;
    }

    // Métodos abstractos
    public abstract void comer();
    public abstract void dormir();
    public abstract void hacerSonido();

    // Método concreto para mostrar detalles
    public void mostrarDetalles() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Peso: " + peso + " kg");
        habitat.mostrarDetalles();
    }

    // Clase interna Habitat
    public class Habitat {
        private String tipoDeHabitat;
        private double tamaño;

        public Habitat(String tipoDeHabitat, double tamaño) {
            this.tipoDeHabitat = tipoDeHabitat;
            this.tamaño = tamaño;
        }

        public void mostrarDetalles() {
            System.out.println("Tipo de hábitat: " + tipoDeHabitat);
            System.out.println("Tamaño del hábitat: " + tamaño + " m²");
        }
    }
}

