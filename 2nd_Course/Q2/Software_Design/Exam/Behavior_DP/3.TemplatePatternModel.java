// Patron de diseño Template Method
// Este patrón define el esqueleto de un algoritmo en una
// operación, delegando algunos pasos a las subclases.
// Permite a las subclases redefinir ciertos pasos de un
// algoritmo sin cambiar la estructura del algoritmo.
// // En este ejemplo, se define una clase abstracta
// "Template" que contiene el método "templateMethod".
// Este método define el esqueleto del algoritmo y llama a
// métodos abstractos que deben ser implementados por las
// subclases. Las subclases implementan los pasos específicos
// del algoritmo.

// En pocas palabras te da una lista de pasos a seguir y
// permite a las subclases implementar los pasos específicos
// del algoritmo.

public abstract class Template {
	// Método plantilla
	public final void templateMethod() {
		step1();
		step2();
		step3();
	}

	// Paso 1
	protected abstract void step1();

	// Paso 2
	protected abstract void step2();

	// Paso 3
	protected abstract void step3();
}

// Subclase concreta que implementa los pasos específicos
// Se pueden implementar por separado siempre que se extienda el template
// y se implementen los pasos abstractos
// de la clase abstracta
class ConcreteTemplate extends Template {
	@Override
	protected void step1() {
		System.out.println("Paso 1: Implementación específica en la subclase.");
	}

	@Override
	protected void step2() {
		System.out.println("Paso 2: Implementación específica en la subclase.");
	}

	@Override
	protected void step3() {
		System.out.println("Paso 3: Implementación específica en la subclase.");
	}
}

// Clase principal para probar el patrón Template Method
public class Main {
	public static void main(String[] args) {
		Template template = new ConcreteTemplate();
		template.templateMethod();
	}
}