/*
### ✅ Variante 3.2 – **Strategy: Ordenamiento de números**

**Enunciado:**

Queremos aplicar el patrón **Strategy** para permitir cambiar el algoritmo de ordenación de una lista de números. Se pueden usar diferentes estrategias como orden ascendente, descendente, o por cercanía al cero.

**Componentes requeridos:**

- `SorterContext`: tiene una lista de números y una estrategia de ordenación.
- `SortingStrategy`: interfaz con el método `ordenar(List<Long>)`.
- `OrdenAscendenteStrategy`, `OrdenDescendenteStrategy`, `CercanoACeroStrategy`: implementaciones concretas.

**Tarea:**

Dibuja el **diagrama UML** de este diseño, incluyendo clases, interfaces y relaciones (agregación, implementación, etc.).

### **Ejercicio 4 (4 Puntos)** – *Versión Strategy*

Una vez obtenido el diseño del patrón Strategy del ejercicio anterior, vamos a generar y completar el código correspondiente.

Se pide:

---

### ✅ **4.1 Escribe el código completo de la clase `SorterContext` según los requisitos del diseño (1.5 Puntos)**

- **4.1.1 Declaración de la clase**
- **4.1.2 Atributos:**
    - Lista de números `List<Long>` llamada `numeros`
    - Objeto `estrategia` de tipo `SortingStrategy`
- **4.1.3 Constructores**
    - Constructor que recibe la lista de números y una estrategia
- **4.1.4 Método `ordenarNumeros()` que aplique la estrategia actual**
- **4.1.5 Método `setEstrategia()` para cambiar la estrategia**
- **4.1.6 Método `toString()` para imprimir la lista ordenada**

---

### ✅ **4.2 Completa el código de la clase `CercanoACeroStrategy` en los apartados indicados como `//TODO` (2.5 Puntos)**

- **4.2.1 Declaración de la clase**
- **4.2.2 Implementación de la interfaz `SortingStrategy`**
- **4.2.3 Implementación del método `ordenar(List<Long> numeros)`**
    - Ordena los números por valor absoluto creciente (más cercanos a 0 primero)
    - En caso de empate, mantiene el orden relativo

---

### ✅ **4.3 Completa el método `main` de una clase `StrategyDemo`**

El objetivo es probar las diferentes estrategias de ordenamiento (`ascendente`, `descendente`, `cercano a cero`) con la misma lista de números.

- **4.3.1 Instanciación de una lista `List<Long>` con algunos enteros positivos y negativos**
- **4.3.2 Crear un `SorterContext` con estrategia ascendente**
- **4.3.3 Ordenar e imprimir**
- **4.3.4 Cambiar la estrategia a descendente y volver a ordenar**
- **4.3.5 Cambiar la estrategia a `CercanoACeroStrategy` y ordenar nuevamente**
*/

public class SorterContext {
	private List<Long> numeros;
	private SortingStrategy estrategia;

	public SorterContext(List<Long> numeros, SortingStrategy estrategia) {
		this.numeros = numeros;
		this.estrategia = estrategia;
	}

	public void getEstrategia(SortingStrategy estrategia) {
		this.estrategia = estrategia;
	}

	public void setEstrategia(SortingStrategy estrategia) {
		this.estrategia = estrategia;
	}

	public void ordenarNumeros() {
		if (estrategia != null) {
			estrategia.ordenar(numeros);
		}
	}
}

public class CercanoACeroStrategy implements SortingStrategy {
	@Override
	public void ordenar(List<Long> numeros) {
		numeros.sort((a, b) -> {
			int cmp = Long.compare(Math.abs(a), Math.abs(b));
			if (cmp == 0) {
				return Long.compare(a, b); // Mantiene el orden relativo en caso de empate
			}
			return cmp;
		});
	}
}

public class StrategyDemo {
	public static void main(String[] args) {
		List<Long> numeros = Arrays.asList(3L, -1L, 2L, -5L, 4L, -2L, 0L, 1L);

		// Estrategia Ascendente
		SorterContext context = new SorterContext(numeros, new OrdenAscendenteStrategy());
		context.ordenarNumeros();
		System.out.println("Orden Ascendente: " + context);

		// Cambiar a Estrategia Descendente
		context.setEstrategia(new OrdenDescendenteStrategy());
		context.ordenarNumeros();
		System.out.println("Orden Descendente: " + context);

		// Cambiar a Estrategia Cercano a Cero
		context.setEstrategia(new CercanoACeroStrategy());
		context.ordenarNumeros();
		System.out.println("Cercano a Cero: " + context);
	}
}