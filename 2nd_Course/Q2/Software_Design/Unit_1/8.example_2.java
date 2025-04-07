/**3.a Create another version of the ElectricCar class, in this case called Car, and its UML representation, in such a way that it shows a 'has a motor' relationship but through a weak composition or aggregation. Compare the UML diagrams of this version and those of exercise 2.a.

3.b In the main method of the Car class, create an electricEngine object that will be used as a parameter value in the creation of the Car object with the brand Tesla, model Model3, and color red. Invoke the turnOn and move methods on the instantiated object. */

class Car {
	private String brand;
	private String model;
	private String color;
	private Motor engine;

	public Car(String brand, String model, String color, Motor engine) {
		this.brand = brand;
		this.model = model;
		this.color = color;
		this.engine = engine;
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
		Motor electricEngine = new Motor();
		Car car = new Car("Tesla", "Model3", "red", electricEngine);
		car.turnOn();
		car.move();
	}
}