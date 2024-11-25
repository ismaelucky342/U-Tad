package Zoo;
import java.util.ArrayList;

public class zoologico {
    private ArrayList<Animal> animales;

    public zoologico() {
        animales = new ArrayList<>();
    }

    public void agregarAnimal(Animal animal) {
        animales.add(animal);
    }

    public void mostrarAnimales() {
        for (Animal animal : animales) {
            animal.mostrarDetalles();
            animal.comer();
            animal.dormir();
            animal.hacerSonido();
            System.out.println();
        }
    }
}
