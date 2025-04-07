/*
Statement
1.a  Write the code for a class, Engine, and its representation in UML class diagram, which represents an engine. It will have an attribute, type, of type String. As a behavior of the class, add a method turnOn() that prints a message 'type' + ' engine turned on!' to the console.

1.b In the main method of the Engine class, create an instance of an 'electric' engine and invoke the turnOn() method.

1.c Add a parameterless constructor by creating a constant value that will be used as the default value, "N/A", in case this constructor is invoked.

1.d Redefine the toString() method of the Engine class in such a way that, when invoked on an object, it displays the class of the object and the value of the type attribute. */

public class Engine {
	private String type;

	public Engine() {
		this.type = "N/A";
	}

	public Engine(String type) {
		this.type = type;
	}

	public void turnOn() {
		System.out.println(type + " engine turned on!");
	}

	@Override
	public String toString() {
		return "Engine: " + type;
	}

	public static void main(String[] args) {
		Engine electricEngine = new Engine("electric");
		electricEngine.turnOn();
	}
}