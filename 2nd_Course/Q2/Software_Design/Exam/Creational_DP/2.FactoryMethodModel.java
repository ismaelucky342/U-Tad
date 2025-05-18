// El patron de Fabrica es un patron de diseño creacional 
// que proporciona una interfaz para crear objetos en una superclase,
// pero permite a las subclases alterar el tipo de objetos que se crean.
// Este patrón es útil cuando no se conoce de antemano qué tipo de objeto
// se va a crear o cuando se desea delegar la creación de objetos a subclases específicas.

// En pocas palabras, el patrón Factory Method define una interfaz para crear un objeto,
// pero permite a las subclases decidir qué clase instanciar.

interface Animal {
	void EmitirSonido();
}

// Clase concreta que implementa la interfaz Animal
class Perro implements Animal {
	@Override
	public void EmitirSonido() {
		System.out.println("Guau");
	}
}

// Clase concreta que implementa la interfaz Animal
class Gato implements Animal {
	@Override
	public void EmitirSonido() {
		System.out.println("Miau");
	}
}

// Clase abstracta que define el método de fábrica
abstract class AnimalFactory {
	public abstract Animal CrearAnimal();
}

// Clase concreta que implementa el método de fábrica para crear un perro
class PerroFactory extends AnimalFactory {
	@Override
	public Animal CrearAnimal() {
		return new Perro();
	}
}

// Clase concreta que implementa el método de fábrica para crear un gato
class GatoFactory extends AnimalFactory {
	@Override
	public Animal CrearAnimal() {
		return new Gato();
	}
}

// Clase principal para probar el patrón Factory Method
public class Main {
	public static void main(String[] args) {
		// Crear una fábrica de perros
		AnimalFactory perroFactory = new PerroFactory();
		Animal perro = perroFactory.CrearAnimal();
		perro.EmitirSonido(); // Salida: Guau

		// Crear una fábrica de gatos
		AnimalFactory gatoFactory = new GatoFactory();
		Animal gato = gatoFactory.CrearAnimal();
		gato.EmitirSonido(); // Salida: Miau
	}
}