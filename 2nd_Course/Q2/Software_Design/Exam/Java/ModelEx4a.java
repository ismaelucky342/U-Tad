/*
**Ejercicio 3 (2 Puntos)**
Se ha decidido que el patrón Decorator es el patrón que nos va a permitir conocer el siguiente primo (el primero) a partir del anterior, es decir el proceso de decoración sobre un número permite encontrar el primer primo mayor que el número decorado. El diseño debe tener los siguientes componentes: `NumberComponent`, `BaseNumberComponent`, `DecoratorNumberComponent` y `PrimeNumberComponent` cumpliendo los siguientes requisitos:

- A todo objeto que se 'comporta' como un `NumberComponent`, se le puede pedir su valor en `base decimal` (es un `numérico` largo) `getValorDecimal()` y su descripción (es un `String`) `getDescripcion()`.
- `BaseNumberComponent` representa la clase base del patrón que permite recibir un número largo en su constructor, pero expone dos constructores, el constructor sin parámetros asigna al atributo `valorDecimal` el valor 2 por defecto, ya que 2 se considera que es el primer primo.
- `DecoratorNumberComponent` es una interface que caracteriza a los decoradores.
- `PrimeNumberComponent` es el decorador, si permite especialización posterior que representa un `número primo`, recibe un objeto común al diseño, solo existe un único constructor y encuentra el valor numérico corresponde al siguiente primo mayor que el objeto decorado. El primo encontrado se guarda en el atributo `primerPrimo` de tipo `numérico` largo que es asignado en el constructor principal.

**Ejercicio 4 (4 Puntos)**
Una vez obtenido el diseño del patrón Decorator del ejercicio anterior, vamos a generar y completar el código correspondiente.

Se pide:

- **4.1 Escribe el código completo de la clase `BaseNumberComponent` según los requisitos del diseño (1.5 Puntos)**
    - 4.1.1 Declaración de la clase
    - 4.1.2 Atributos
    - 4.1.3 Constructores
    - 4.1.4 Declaración y cuerpo del método `toString()`
    - 4.1.5 Declaración y cuerpo de `getValorDecimal`
    - 4.1.6 Declaración y cuerpo de `getDescripcion`
- **4.2 Completa el código de la clase `PrimeNumberComponent` en los apartados indicados como //TODO (2.5 Puntos)**
    - 4.2.1 Declaración de la clase
    - 4.2.2 Atributos
    - 4.2.3 Constructor y cuerpo de `getPrimeNumberComponent`
    - 4.2.4 Declaración y cuerpo de `getValorDecimal`
    - 4.2.5 Declaración y cuerpo de `getDescripcion`
- **4.3 Completa el código que se encontraría en el método `main` de la clase `PrimeNumberDecorator`,**
el objetivo es conseguir la lista de los 12 primeros números primos. El último primo de la lista debe
ser el que se obtenga después de la decoración.
    - 4.3.1 Instanciación del objeto `decimoSegundoPrimo`
    - 4.3.2 Decoración hasta encontrar el `decimoSegundoPrimo`

Java
*/

public class BaseNumberComponent implements NumberComponent {
	private long valorDecimal;

	// Constructor sin parámetros, asigna el valor 2 por defecto
	public BaseNumberComponent() {
		this.valorDecimal = 2;
	}

	// Constructor que recibe un número largo
	public BaseNumberComponent(long valorDecimal) {
		this.valorDecimal = valorDecimal;
	}

	@Override
	public String toString() {
		return "BaseNumberComponent{" +
				"valorDecimal=" + valorDecimal +
				'}';
	}

	@Override
	public long getValorDecimal() {
		return valorDecimal;
	}

	@Override
	public String getDescripcion() {
		return "Número base: " + valorDecimal;
	}
}

public class PrimeNumberComponent implements DecoratorNumberComponent {
	private long primerPrimo;

	// Constructor que recibe un objeto NumberComponent
	public PrimeNumberComponent(NumberComponent component) {
		this.primerPrimo = findNextPrime(component.getValorDecimal());
	}

	// Método para encontrar el siguiente número primo mayor que el valor dado
	private long findNextPrime(long number) {
		long next = number + 1;
		while (!isPrime(next)) {
			next++;
		}
		return next;
	}

	// Método para verificar si un número es primo
	private boolean isPrime(long num) {
		if (num <= 1) return false;
		for (long i = 2; i <= Math.sqrt(num); i++) {
			if (num % i == 0) return false;
		}
		return true;
	}

	@Override
	public long getValorDecimal() {
		return primerPrimo;
	}

	@Override
	public String getDescripcion() {
		return "Siguiente primo: " + primerPrimo;
	}
}

public class PrimeNumberDecorator {
	public static void main(String[] args) {
		// 4.3.1 Instanciación del objeto decimoSegundoPrimo
		NumberComponent decimoSegundoPrimo = new BaseNumberComponent();

		// 4.3.2 Decoración hasta encontrar el decimoSegundoPrimo
		for (int i = 0; i < 12; i++) {
			decimoSegundoPrimo = new PrimeNumberComponent(decimoSegundoPrimo);
			System.out.println(decimoSegundoPrimo.getDescripcion());
		}
	}
}

