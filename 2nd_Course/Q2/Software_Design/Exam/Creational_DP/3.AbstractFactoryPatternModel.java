// El patron de factoría abstracta es un patrón de diseño creacional
// que proporciona una interfaz para crear familias de objetos
// relacionados sin especificar sus clases concretas. Este patrón
// es útil cuando se desea crear objetos que pertenecen a una
// misma familia o que están relacionados entre sí, pero no se
// desea acoplar el código a clases concretas.

// Su diferencia con el patrón Factory Method es que el patrón
// Factory Method se centra en la creación de un solo objeto,
// mientras que el patrón Abstract Factory se centra en la creación
// de familias de objetos relacionados. En otras palabras, el
// patrón Factory Method define una interfaz para crear un objeto,
// pero permite a las subclases decidir qué clase instanciar,
// mientras que el patrón Abstract Factory define una interfaz
// para crear un conjunto de objetos relacionados sin especificar
// sus clases concretas.

interface Animal {
	void EmitirSonido();
}

interface Juguete {
	void Jugar();
}

// Animales concretos
class Perro implements Animal {
	@Override
	public void EmitirSonido() {
		System.out.println("Guau");
	}
}

class Gato implements Animal {
	@Override
	public void EmitirSonido() {
		System.out.println("Miau");
	}
}

// Juguetes concretos

class Pelota implements Juguete {
	@Override
	public void Jugar() {
		System.out.println("Jugando con la pelota");
	}
}

class Ratón implements Juguete {
	@Override
	public void Jugar() {
		System.out.println("Jugando con el ratón");
	}
}

// Fábrica abstracta
abstract class AnimalFactory {
	public abstract Animal CrearAnimal();
	public abstract Juguete CrearJuguete();
}

// Fábrica concreta para perros

class PerroFactory extends AnimalFactory {
	@Override
	public Animal CrearAnimal() {
		return new Perro();
	}

	@Override
	public Juguete CrearJuguete() {
		return new Pelota();
	}
}

// Fábrica concreta para gatos

class GatoFactory extends AnimalFactory {
	@Override
	public Animal CrearAnimal() {
		return new Gato();
	}

	@Override
	public Juguete CrearJuguete() {
		return new Ratón();
	}
}

// Clase principal para probar el patrón Abstract Factory

public class Main {
	public static void main(String[] args) {
		// Crear una fábrica de perros
		AnimalFactory perroFactory = new PerroFactory();
		Animal perro = perroFactory.CrearAnimal();
		Juguete pelota = perroFactory.CrearJuguete();
		perro.EmitirSonido(); // Salida: Guau
		pelota.Jugar(); // Salida: Jugando con la pelota

		// Crear una fábrica de gatos
		AnimalFactory gatoFactory = new GatoFactory();
		Animal gato = gatoFactory.CrearAnimal();
		Juguete ratón = gatoFactory.CrearJuguete();
		gato.EmitirSonido(); // Salida: Miau
		ratón.Jugar(); // Salida: Jugando con el ratón
	}
}