
// Modelo básico del patrón de diseño Strategy
// en Java. Este modelo es un ejemplo de cómo implementar
// implementamos un programa que decida qué estrategia usar
// en función de la entrada del usuario para un servicio de 
// entrega de comida a domicilio. El programa permite al
// usuario elegir entre diferentes estrategias de entrega
// (por ejemplo, entrega rápida, entrega estándar, etc.)
// y luego ejecuta la estrategia seleccionada.

public interface Strategy {
	void entregar();
}

// Implementación de la entrega rápida
class EntregaRapida implements Strategy {
	@Override
	public void entregar() {
		System.out.println("Entrega rápida seleccionada.");
	}
}

// Implementación de la entrega estándar
class EntregaEstandar implements Strategy {
	@Override
	public void entregar() {
		System.out.println("Entrega estándar seleccionada.");
	}
}

// Implementación de la entrega programada
class EntregaProgramada implements Strategy {
	@Override
	public void entregar() {
		System.out.println("Entrega programada seleccionada.");
	}
}

// Contexto que utiliza las estrategias
class Contexto {
	private Strategy strategy;

	public void setStrategy(Strategy strategy) {
		this.strategy = strategy;
	}

	public void ejecutarEstrategia() {
		if (strategy != null) {
			strategy.entregar();
		} else {
			System.out.println("No se ha seleccionado ninguna estrategia.");
		}
	}
}

// Clase principal para probar el patrón Strategy
public class Main {
	public static void main(String[] args) {
		Contexto contexto = new Contexto();

		// Seleccionar entrega rápida
		contexto.setStrategy(new EntregaRapida());
		contexto.ejecutarEstrategia();

		// Cambiar a entrega estándar
		contexto.setStrategy(new EntregaEstandar());
		contexto.ejecutarEstrategia();

		// Cambiar a entrega programada
		contexto.setStrategy(new EntregaProgramada());
		contexto.ejecutarEstrategia();
	}
}