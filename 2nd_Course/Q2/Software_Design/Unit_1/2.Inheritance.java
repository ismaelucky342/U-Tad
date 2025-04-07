// Inheritance

// Base class (superclass)
class Animal {
    void eat() {
        System.out.println("This animal is eating.");
    }
}

// Derived classes (subclasses) that inherit from Animal
class Dog extends Animal {
    void bark() {
        System.out.println("The dog is barking.");
    }
}

class Cat extends Animal {
    void meow() {
        System.out.println("The cat is meowing.");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();  // Inherited from Animal
        dog.bark(); // Method from the Dog class

        Cat cat = new Cat();
        cat.eat();   // Inherited from Animal
        cat.meow();  // Method from the Cat class
    }
}


// Composition

class Engine {
    void start() {
        System.out.println("The engine is on.");
    }
}
class Car {
    private Engine engine;

    // Constructor
    public Car() {
        this.engine = new Engine(); // Composition: the car has an engine
    }

    void startCar() {
        engine.start();
        System.out.println("The car has started.");
    }
}
class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.startCar(); // Starts the car, which in turn starts the engine
    }
}
