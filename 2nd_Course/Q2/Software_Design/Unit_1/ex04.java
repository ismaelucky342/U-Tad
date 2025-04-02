// Delegation by composition

// Class that has the behavior of eating
class Behavior {
    void eat() {
        System.out.println("The animal is eating.");
    }
}

// Dog class that delegates the responsibility of eating
class Dog {
    private Behavior behavior;

    // Delegation by composition (Dog has a Behavior)
    public Dog() {
        this.behavior = new Behavior();  // Create an instance of Behavior
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
        Dog dog = new Dog();  // The Dog has its own Behavior

        dog.bark();
        dog.eat();  // Delegation happens here
    }
}
