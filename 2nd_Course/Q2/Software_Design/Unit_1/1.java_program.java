public class Car {
    // Attributes (state)
    private String brand;
    private String model;
    private boolean isRunning;

    // Constructor
    public Car(String brand, String model) {
        this.brand = brand;
        this.model = model;
        this.isRunning = false; // Default state: the car is stopped
    }
    // Methods (behavior)

    // Start the car
    public void start() {
        if (!isRunning) {
            isRunning = true;
            System.out.println("The car has started.");
        } else {
            System.out.println("The car is already running.");
        }
    }

    // Stop the car
    public void stop() {
        if (isRunning) {
            isRunning = false;
            System.out.println("The car has stopped.");
        } else {
            System.out.println("The car is already stopped.");
        }
    }

    // Display the car's state
    public void displayState() {
        System.out.println("Car brand: " + brand);
        System.out.println("Car model: " + model);
        System.out.println("Is the car running? " + (isRunning ? "Yes" : "No"));
    }

    // Main method for execution
    public static void main(String[] args) {
        Car myCar = new Car("Toyota", "Corolla");

        // Display initial state
        myCar.displayState();

        // Start the car
        myCar.start();

        // Display state after starting
        myCar.displayState();

        // Stop the car
        myCar.stop();

        // Display state after stopping
        myCar.displayState();
    }
}