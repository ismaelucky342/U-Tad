/*
### Variante 3.2 – **Strategy: Ordenamiento de números**

**Enunciado:**

Queremos aplicar el patrón **Strategy** para permitir cambiar el algoritmo de ordenación de una lista de números. Se pueden usar diferentes estrategias como orden ascendente, descendente, o por cercanía al cero.

**Componentes requeridos:**

- `SorterContext`: tiene una lista de números y una estrategia de ordenación.
- `SortingStrategy`: interfaz con el método `ordenar(List<Long>)`.
- `OrdenAscendenteStrategy`, `OrdenDescendenteStrategy`, `CercanoACeroStrategy`: implementaciones concretas.

**Tarea:**

Dibuja el **diagrama UML** de este diseño, incluyendo clases, interfaces y relaciones (agregación, implementación, etc.).
*/

public interface SortingStrategy {
	List<Long> ordenar(List<Long> numeros);
}

public class OrdenAscendenteStrategy implements SortingStrategy {
	@Override
	public List<Long> ordenar(List<Long> numeros) {
		return numeros.stream().sorted().toList();
	}
}

public class OrdenDescendenteStrategy implements SortingStrategy {
	@Override
	public List<Long> ordenar(List<Long> numeros) {
		return numeros.stream().sorted(Comparator.reverseOrder()).toList();
	}
}

public class CercanoACeroStrategy implements SortingStrategy {
	@Override
	public List<Long> ordenar(List<Long> numeros) {
		return numeros.stream()
			.sorted(Comparator.comparingLong(Math::abs))
			.toList();
	}
}

public class SorterContext {
	private List<Long> numeros;
	private SortingStrategy strategy;

	public SorterContext(List<Long> numeros, SortingStrategy strategy) {
		this.numeros = numeros;
		this.strategy = strategy;
	}

	public List<Long> ordenar() {
		return strategy.ordenar(numeros);
	}
	public void setStrategy(SortingStrategy strategy) {
		this.strategy = strategy;
	}
	public List<Long> getNumeros() {
		return numeros;
	}
	public void setNumeros(List<Long> numeros) {
		this.numeros = numeros;
	}
	public SortingStrategy getStrategy() {
		return strategy;
	}
}

public class Main {
	public static void main(String[] args) {
		List<Long> numeros = List.of(5L, 3L, -2L, 8L, 1L);
		
		SorterContext context = new SorterContext(numeros, new OrdenAscendenteStrategy());
		System.out.println("Orden Ascendente: " + context.ordenar());
		
		context.setStrategy(new OrdenDescendenteStrategy());
		System.out.println("Orden Descendente: " + context.ordenar());
		
		context.setStrategy(new CercanoACeroStrategy());
		System.out.println("Cercano a Cero: " + context.ordenar());
	}
}
