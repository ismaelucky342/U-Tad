// Delegation by injection

// Class that has the behavior of eating
class Behavior {
    void eat() {
        System.out.println("The animal is eating.");
    }
}

// Dog class that delegates the responsibility of eating
class Dog {
    private Behavior behavior;

    // Delegation by injection through the constructor
    public Dog(Behavior behavior) {
        this.behavior = behavior;
    }

    void bark() {
        System.out.println("The dog is barking.");
    }

    void eat() {
        behavior.eat();  // Delegation of eating to the behavior object
    }
}

public class Main {
    public static void main(String[] args) {
        // Create a behavior and inject it into the dog
        Behavior behavior = new Behavior();
        Dog dog = new Dog(behavior);

        dog.bark();
        dog.eat();  // Delegation happens here
    }
}
