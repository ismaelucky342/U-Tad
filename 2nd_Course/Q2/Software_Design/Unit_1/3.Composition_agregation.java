// Class that represents a Heart (Composition)
class Heart {
    void beat() {
        System.out.println("The heart is beating.");
    }
}

// Dog class that has a Heart (Composition)
class Dog {
    private Heart heart;

    public Dog() {
        // The Heart is an integral part of a Dog
        heart = new Heart();
    }

    void bark() {
        System.out.println("The dog is barking.");
    }

    void beat() {
        heart.beat();  // Delegate the beating action to the Heart
    }
}

// Owner class that has a Dog (Aggregation)
class Owner {
    private Dog dog;

    public Owner(Dog dog) {
        this.dog = dog;  // The owner has a Dog but does not create it
    }

    void walk() {
        System.out.println("The owner is walking the dog.");
        dog.bark();  // The owner can make the dog bark
    }
}

public class Main {
    public static void main(String[] args) {
        // Create a Dog
        Dog dog = new Dog();
        
        // Create an Owner and assign a Dog to them
        Owner owner = new Owner(dog);
        
        // The dog can bark and its heart can beat
        dog.bark();
        dog.beat();
        
        // The owner can walk the dog
        owner.walk();
    }
}
