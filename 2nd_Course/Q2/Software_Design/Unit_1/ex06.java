/*
Statement
2.a Create a class ElectricCar, and its UML representation, with attributes brand, model, and color (all of type String) that shows a 'has a motor' relationship, using the class from exercise 1. The class has a constructor with three parameters: brand, model, and color.

2.b The ElectricCar class has two behavioral methods: turnOn, which delegates the service, and move, which prints a message to the console formed by concatenating the values of brand, model, and color with the text 'moving...'.

2.c Implement the toString() method of the ElectricCar class and use it in the message of the move method.

2.d In the main method of the ElectricCar class, create an object of the ElectricCar class with the brand Tesla, model Model3, and color red. Invoke the turnOn and move methods on the instantiated object.

2.e Compare the composition solution from section 2.a in which the object is created directly in the attribute declaration itself.
*/

class ElectricCar {
	private String brand;
	private String model;
	private String color;
	private Motor engine;

	public ElectricCar(String brand, String model, String color) {
		this.brand = brand;
		this.model = model;
		this.color = color;
		this.engine = new Motor();
	}

	public void turnOn() {
		engine.turnOn();
	}

	public void move() {
		System.out.println(toString() + " moving...");
	}

	@Override
	public String toString() {
		return brand + " " + model + " " + color;
	}

	public static void main(String[] args) {
		ElectricCar car = new ElectricCar("Tesla", "Model3", "red");
		car.turnOn();
		car.move();
	}
}

class Motor {
	public void turnOn() {
		System.out.println("Engine turned on");
	}
}
