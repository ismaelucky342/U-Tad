// Producto abstracto
interface Product {
    void use();
}

// Producto concreto
class ConcreteProductA implements Product {
    public void use() {
        System.out.println("Usando Producto A");
    }
}

// Creador abstracto (Factoría)
abstract class Creator {
    abstract Product factoryMethod();
}

// Fábrica concreta
class ConcreteCreatorA extends Creator {
    public Product factoryMethod() {
        return new ConcreteProductA();
    }
}

// Uso del patrón
public class FactoryMethodExample {
    public static void main(String[] args) {
        Creator creator = new ConcreteCreatorA();
        Product product = creator.factoryMethod();
        product.use(); // Salida: "Usando Producto A"
    }
}
