package Zoo;

public class Main {
    public Main(final String[] args) {
        zoologico zoologico = new zoologico();

        // Crear hábitats
        Animal.Habitat habitatTerrestre = new Mamifero("Animal", 0, 0, null, "Corto").new Habitat("Terrestre", 200.5);
        Animal.Habitat habitatAcuatico = new Mamifero("Animal", 0, 0, null, "Corto").new Habitat("Acuático", 1000.0);
        Animal.Habitat habitatAereo = new Mamifero("Animal", 0, 0, null, "Corto").new Habitat("Aéreo", 300.0);

        // Crear animales
        Mamifero mamifero = new Mamifero("León", 5, 190.5, habitatTerrestre, "Corto");
        Ave ave = new Ave("Águila", 3, 5.0, habitatAereo, true);
        reptil reptil = new reptil("Serpiente", 2, 3.5, habitatAcuatico, "Escamas lisas");

        // Agregar animales al zoológico
        zoologico.agregarAnimal(mamifero);
        zoologico.agregarAnimal(ave);
        zoologico.agregarAnimal(reptil);

        // Mostrar animales
        zoologico.mostrarAnimales();
    }
}
