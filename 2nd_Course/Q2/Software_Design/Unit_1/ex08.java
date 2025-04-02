/**
 * 4.a By means of specialization/inheritance, create the class HerencyElectricCar based on the Car class from exercise 3. The constructor of the HerencyElectricCar class will only contain the brand, model, and color parameters.
 * 
 * 4.b In the main method of the HerencyElectricCar class, create an object of type Car that will be instantiated through an object of HerencyElectricCar, corresponding to a vehicle of the brand Tesla, model Model3, and color red.
 */

class HerencyElectricCar extends Car {
	public HerencyElectricCar(String brand, String model, String color) {
		super(brand, model, color, new Motor());
	}

	public static void main(String[] args) {
		HerencyElectricCar car = new HerencyElectricCar("Tesla", "Model3", "red");
		car.turnOn();
		car.move();
	}
}

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
}

class Motor {
	public void turnOn() {
		System.out.println("Engine turned on");
	}
}

