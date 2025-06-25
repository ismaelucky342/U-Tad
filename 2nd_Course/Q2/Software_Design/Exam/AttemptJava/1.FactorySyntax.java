/**
 *Producción de elementos GUI multiplataforma
En este ejemplo, Buttons (Botones) juega el papel de producto y los diálogos actúan como creadores.

Los distintos tipos de diálogos requieren sus propios tipos de elementos. Por eso creamos una subclase para cada tipo de diálogo y sobrescribimos sus métodos fábrica.

Ahora, cada tipo de diálogo instanciará clases de botón. El diálogo base trabaja con productos utilizando su interfaz común, por eso su código sigue siendo funcional tras todos los cambios.
 */

// metodo de factoría 

public interface Button {
	void onClick();
	void render();
}

public class HtmlButton implements Button {

	// Método 1 
	@Override
	public void onClick() {
		System.out.println("HTML Button clicked!");
	}

	// Método 2
	@Override
	public void render() {
		System.out.println("<button>HTML Button</button>");
	}
}

public class WindowsButton implements Button {

	// Método 1
	@Override
	public void onClick() {
		System.out.println("Windows Button clicked!");
	}

	// Método 2
	@Override
	public void render() {
		System.out.println("[Windows Button]");
	}
}

abstract class Dialog {
	// Método fábrica
	public abstract Button createButton();

	// Método para mostrar el diálogo
	public void render() {
		Button button = createButton();
		button.render();
		button.onClick();
	}
}

// fabrica concreta html
public class HtmlDialog extends Dialog {

	// Implementación del método fábrica para crear un botón HTML
	@Override
	public Button createButton() {
		return new HtmlButton();
	}
}

// fabrica concreta windows
public class WindowsDialog extends Dialog {

	// Implementación del método fábrica para crear un botón de Windows
	@Override
	public Button createButton() {
		return new WindowsButton();
	}
}

public class Main {
	public static void main(String[] args) {
		// Crear un diálogo HTML
		Dialog htmlDialog = new HtmlDialog();
		htmlDialog.render();

		System.out.println();

		// Crear un diálogo de Windows
		Dialog windowsDialog = new WindowsDialog();
		windowsDialog.render();
	}
}