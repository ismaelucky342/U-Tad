/*
Singleton ingenuo (hilo único)
Es muy fácil implementar un Singleton descuidado. Tan solo necesitas esconder el constructor e implementar un método de creación estático.

*/

public class Singleton {
	private static Singleton instance;
	public String value;

	// Constructor privado para evitar instanciación externa
	// Este constructor es privado para que no se pueda crear una instancia de Singleton desde fuera de la clase.
	// Esto asegura que la única forma de obtener una instancia de Singleton sea a través
	private Singleton() {
		value = "Singleton Instance";
	}

	// Método público estático para obtener la instancia
	// Este método proporciona un punto de acceso global a la instancia única de Singleton.
	// Si la instancia aún no ha sido creada, se crea una nueva instancia.
	// Si ya existe una instancia, simplemente se devuelve esa instancia.
	// Esto garantiza que solo haya una instancia de Singleton en todo el sistema.
	public static Singleton getInstance() {
		if (instance == null) {
			instance = new Singleton();
		}
		return instance;
	}


}

public class Main {
	public static void main(String[] args) {
		// Obtener la instancia del Singleton
		Singleton singleton = Singleton.getInstance();
		System.out.println(singleton.value); // Imprime: Singleton Instance

		// Intentar obtener otra instancia del Singleton
		Singleton anotherSingleton = Singleton.getInstance();
		System.out.println(anotherSingleton.value); // Imprime: Singleton Instance

		// Verificar que ambas referencias apuntan al mismo objeto
		System.out.println(singleton == anotherSingleton); // Imprime: true
	}
}