/*

### **Ejercicio 3 (2 puntos)**

Vamos a construir un diseño basado en el **patrón Strategy** para seleccionar diferentes formas de calcular si un número es primo. Las estrategias pueden incluir:

- División simple
- Criba de Eratóstenes (simulada)
- Verificación probabilística (simulada)

Los componentes deben ser:

- **PrimalityStrategy** (interface)
- **SimpleDivisionStrategy**, **SieveStrategy**, **ProbabilisticStrategy** (implementaciones)
- **PrimeChecker**: clase cliente que usa la estrategia

### Se pide:

- Dibujar el **diagrama UML** del patrón Strategy con los componentes anteriores.
- Indicar claramente el tipo de relación entre cada clase (herencia, composición, etc.).

---*/


import java.util.List;
import java.util.ArrayList;

public interface PrimalityStrategy {
	boolean isPrime(int number);
}

public class SimpleDivisionStrategy implements PrimalityStrategy {
	@Override
	public boolean isPrime(int number) {
		if (number <= 1) return false;
		for (int i = 2; i <= Math.sqrt(number); i++) {
			if (number % i == 0) return false;
		}
		return true;
	}
}

public class SieveStrategy implements PrimalityStrategy {
	@Override
	public boolean isPrime(int number) {
		if (number <= 1) return false;
		boolean[] isPrime = new boolean[number + 1];
		for (int i = 2; i <= number; i++) isPrime[i] = true;
		for (int i = 2; i * i <= number; i++) {
			if (isPrime[i]) {
				for (int j = i * i; j <= number; j += i) {
					isPrime[j] = false;
				}
			}
		}
		return isPrime[number];
	}
}

public class ProbabilisticStrategy implements PrimalityStrategy {
	@Override
	public boolean isPrime(int number) {
		if (number <= 1) return false;
		if (number <= 3) return true;
		if (number % 2 == 0 || number % 3 == 0) return false;
		for (int i = 5; i * i <= number; i += 6) {
			if (number % i == 0 || number % (i + 2) == 0) return false;
		}
		return true;
	}
}

public class PrimeChecker {
	private PrimalityStrategy strategy;

	public PrimeChecker(PrimalityStrategy strategy) {
		this.strategy = strategy;
	}

	public boolean check(int number) {
		return strategy.isPrime(number);
	}
}

public class Main {
	public static void main(String[] args) {
		List<PrimeChecker> checkers = new ArrayList<>();
		checkers.add(new PrimeChecker(new SimpleDivisionStrategy()));
		checkers.add(new PrimeChecker(new SieveStrategy()));
		checkers.add(new PrimeChecker(new ProbabilisticStrategy()));

		int numberToCheck = 29; // Example number

		for (PrimeChecker checker : checkers) {
			System.out.println("Is " + numberToCheck + " prime? " + checker.check(numberToCheck));
		}
	}
}