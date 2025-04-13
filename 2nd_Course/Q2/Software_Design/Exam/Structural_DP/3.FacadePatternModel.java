// El patron de fachada es un patrón de diseño estructural
// que proporciona una interfaz simplificada a un conjunto de
// interfaces en un subsistema. Este patrón es útil cuando
// se desea ocultar la complejidad de un sistema y proporcionar
// una interfaz más fácil de usar. La fachada actúa como un
// intermediario entre el cliente y el subsistema, lo que
// permite al cliente interactuar con el subsistema sin tener
// que preocuparse por su complejidad interna.

// O lo que es lo mismo, el patrón de fachada define una
// interfaz de alto nivel que hace que el subsistema sea
// más fácil de usar. Esto es especialmente útil cuando
// el subsistema es complejo o tiene muchas clases y
// métodos. Al proporcionar una interfaz simplificada,
// la fachada oculta la complejidad del subsistema y
// facilita su uso por parte del cliente.

class SistemaDeAudio {
	public void encender() {
		System.out.println("Sistema de audio encendido.");
	}


	public void apagar() {
		System.out.println("Sistema de audio apagado.");
	}

	public void reproducir(String cancion) {
		System.out.println("Reproduciendo: " + cancion);
	}
}


class SistemaDeIluminacion {
	public void encender() {
		System.out.println("Sistema de iluminación encendido.");
	}

	public void apagar() {
		System.out.println("Sistema de iluminación apagado.");
	}

	public void ajustarBrillo(int nivel) {
		System.out.println("Ajustando brillo a: " + nivel);
	}
}

class SistemaDeClimatizacion {
	public void encender() {
		System.out.println("Sistema de climatización encendido.");
	}

	public void apagar() {
		System.out.println("Sistema de climatización apagado.");
	}

	public void ajustarTemperatura(int temperatura) {
		System.out.println("Ajustando temperatura a: " + temperatura + "°C");
	}
}

class SistemaDeFachada {
	private SistemaDeAudio audio;
	private SistemaDeIluminacion iluminacion;
	private SistemaDeClimatizacion climatizacion;

	public SistemaDeFachada() {
		audio = new SistemaDeAudio();
		iluminacion = new SistemaDeIluminacion();
		climatizacion = new SistemaDeClimatizacion();
	}

	public void encenderTodo() {
		audio.encender();
		iluminacion.encender();
		climatizacion.encender();
	}

	public void apagarTodo() {
		audio.apagar();
		iluminacion.apagar();
		climatizacion.apagar();
	}
}

public class Main {
	public static void main(String[] args) {
		SistemaDeFachada sistema = new SistemaDeFachada();

		sistema.encenderTodo();
		sistema.apagarTodo();
	}
}