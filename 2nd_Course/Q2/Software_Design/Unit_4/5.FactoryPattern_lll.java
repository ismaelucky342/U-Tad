// interface

interface Pizza{
    void prepare();
}

class PizzaItalian implements Pizza{
    @Override
    public void prepare() {
        System.out.println("Preparing Italian Pizza!");
    }
}

class PizzaMexican implements Pizza{
    @Override
    public void prepare() {
        System.out.println("Preparing Mexican Pizza!");
    }
}

// Factory
abstract class Pizzeria {
    public void ordenarPizza() {
        Pizza pizza = crearPizza(); // Factory Method
        pizza.preparar();
    }
    public abstract Pizza crearPizza();
}

// Concrete Factory Classes

class PizzeriaItaliana extends Pizzeria {
    @Override
    public Pizza crearPizza() {
        return new PizzaItalian();
    }
}

class PizzeriaMexicana extends Pizzeria {
    @Override
    public Pizza crearPizza() {
        return new PizzaMexican();
    }
}

// Main class to demonstrate the Factory Pattern

public class Main {
    public static void main(String[] args) {
        Pizzeria pizzeriaItaliana = new PizzeriaItaliana();
        pizzeriaItaliana.ordenarPizza(); // Output: Preparing Italian Pizza!

        Pizzeria pizzeriaMexicana = new PizzeriaMexicana();
        pizzeriaMexicana.ordenarPizza(); // Output: Preparing Mexican Pizza!
    }
}
