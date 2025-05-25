/**
 * Ejemplo del patrón de diseño Template Method en Java.
 * Este patrón define el esqueleto de un algoritmo en una clase base,
 * permitiendo que las subclases redefinan ciertos pasos del algoritmo sin cambiar su estructura.
 */

// Clase abstracta que define el método plantilla
abstract class Juego {
	// Método plantilla (template method)
	public final void jugar() {
		inicializar();
		empezarJuego();
		finalizarJuego();
	}

	// Métodos abstractos que las subclases deben implementar
	protected abstract void inicializar();
	protected abstract void empezarJuego();
	protected abstract void finalizarJuego();
}

// Subclase concreta que implementa los pasos específicos del juego de fútbol
class Futbol extends Juego {
	@Override
	protected void inicializar() {
		System.out.println("Fútbol: Inicializando el juego...");
	}

	@Override
	protected void empezarJuego() {
		System.out.println("Fútbol: ¡El juego ha comenzado!");
	}

	@Override
	protected void finalizarJuego() {
		System.out.println("Fútbol: El juego ha terminado.");
	}
}

// Subclase concreta que implementa los pasos específicos del juego de baloncesto
class Baloncesto extends Juego {
	@Override
	protected void inicializar() {
		System.out.println("Baloncesto: Inicializando el juego...");
	}

	@Override
	protected void empezarJuego() {
		System.out.println("Baloncesto: ¡El juego ha comenzado!");
	}

	@Override
	protected void finalizarJuego() {
		System.out.println("Baloncesto: El juego ha terminado.");
	}
}

// Clase principal para probar el patrón Template Method
public class TemplateModel {
	public static void main(String[] args) {
		Juego juego = new Futbol();
		juego.jugar();

		System.out.println();

		juego = new Baloncesto();
		juego.jugar();
	}
}