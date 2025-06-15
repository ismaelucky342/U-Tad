/*
### Variante 3.1 – (Ya escrita) **Decorator: Números pares**

**Enunciado:**

Queremos aplicar el patrón **Decorator** para obtener el siguiente número **par** a partir del anterior. Se pide un diseño que permita construir decoradores sucesivos que devuelvan el siguiente número par a partir del anterior decorado.

**Componentes requeridos:**

- `NumberComponent`
- `BaseNumberComponent`
- `DecoratorNumberComponent`
- `EvenNumberComponent`

**Tarea:**

Dibuja el **diagrama UML** de este diseño indicando el tipo de relación entre clases.
*/

interface NumberComponent {
	int getValue();
	String getDescription();

}

class BaseNumberComponent implements NumberComponent {
	private int value;

	public BaseNumberComponent(int value) {
		this.value = value;
	}

	@Override
	public int getValue() {
		return value;
	}

	@Override
	public String getDescription() {
		return "Base number: " + value;
	}
}

class DecoratorNumberComponent implements NumberComponent {
	protected NumberComponent component;

	public DecoratorNumberComponent(NumberComponent component) {
		this.component = component;
	}

	@Override
	public int getValue() {
		return component.getValue();
	}

	@Override
	public String getDescription() {
		return component.getDescription();
	}
}

class EvenNumberComponent extends DecoratorNumberComponent {

	public EvenNumberComponent(NumberComponent component) {
		super(component);
	}

	@Override
	public int getValue() {
		int value = component.getValue();
		return (value % 2 == 0) ? value : value + 1; // Return next even number
	}

	@Override
	public String getDescription() {
		return "Even number: " + getValue();
	}
}

public class Main {
	public static void main(String[] args) {

		NumberComponent baseNumber = new BaseNumberComponent(5);
		System.out.println(baseNumber.getDescription()); 

		NumberComponent evenNumber = new EvenNumberComponent(baseNumber);
		System.out.println(evenNumber.getDescription()); 

		NumberComponent nextEvenNumber = new EvenNumberComponent(evenNumber);
		System.out.println(nextEvenNumber.getDescription());
	}
}


