// El patron Singleton es un patrón de diseño creacional que
// restringe la instanciación de una clase a un único objeto.
// Esto es útil cuando exactamente un objeto debe coordinar
// acciones a través del sistema. El patrón Singleton es
// comúnmente utilizado para gestionar recursos compartidos,
// como conexiones a bases de datos o configuraciones globales.

// En este ejemplo, implementaremos un modelo básico del
// patrón Singleton en Java. Tendremos una clase Singleton
// que garantiza que solo haya una instancia de sí misma
// y proporciona un punto de acceso global a esa instancia.

public class Singleton {
	// Instancia privada estática de la clase Singleton
	private static Singleton instance;

	// Constructor privado para evitar instanciación externa
	private Singleton() {
		// Inicialización del singleton
	}

	// Método público estático para obtener la instancia
	public static Singleton getInstance() {
		if (instance == null) {
			instance = new Singleton();
		}
		return instance;
	}

	// Método de ejemplo
	public void doSomething() {
		System.out.println("Haciendo algo con el singleton.");
	}
}

// // Main para probar el patrón Singleton
public class Main {
	public static void main(String[] args) {
		// Obtener la instancia del singleton
		Singleton singleton = Singleton.getInstance();
		singleton.doSomething();

		// Verificar que ambas referencias apuntan al mismo objeto
		Singleton anotherSingleton = Singleton.getInstance();
		System.out.println("¿Son las mismas instancias? " + (singleton == anotherSingleton));
	}
}