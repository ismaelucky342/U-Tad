
abstract class Beverage {
    // Método plantilla
    public final void prepareRecipe() {
        boilWater();
        brew();
        pourInCup();
        addCondiments();
    }

    void boilWater() {
        System.out.println("Hirviendo agua");
    }

    void pourInCup() {
        System.out.println("Sirviendo en taza");
    }

    // Métodos abstractos que definen los pasos variables
    abstract void brew();
    abstract void addCondiments();
}

class Coffee extends Beverage {
    @Override
    void brew() {
        System.out.println("Filtrando el café");
    }

    @Override
    void addCondiments() {
        System.out.println("Agregando azúcar y leche");
    }
}

public class Main {
    public static void main(String[] args) {
        Beverage myCoffee = new Coffee();
        myCoffee.prepareRecipe();
    }
}
