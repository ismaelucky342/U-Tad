// El patron decorador es un patron de diseño estructural que 
// permite añadir nuevas funcionalidades a un objeto existente 
// sin modificar su estructura.
// Se utiliza para extender la funcionalidad de las clases de forma
// dinámica y flexible.
// En este ejemplo, se implementa un sistema de notificaciones
// donde se pueden añadir diferentes tipos de notificaciones
// (SMS, Email) a un objeto Notificador.

// Interfaz base
interface Notificador {
	void enviar(String mensaje);
}

// Implementación concreta
class NotificadorBasico implements Notificador {
	@Override
	public void enviar(String mensaje) {
		System.out.println("Notificación básica: " + mensaje);
	}
}

// Decorador abstracto
abstract class NotificadorDecorador implements Notificador {
	protected Notificador envoltorio;

	public NotificadorDecorador(Notificador envoltorio) {
		this.envoltorio = envoltorio;
	}

	@Override
	public void enviar(String mensaje) {
		envoltorio.enviar(mensaje);
	}
}

// Decorador concreto: SMS
class NotificadorSMS extends NotificadorDecorador {
	public NotificadorSMS(Notificador envoltorio) {
		super(envoltorio);
	}

	@Override
	public void enviar(String mensaje) {
		super.enviar(mensaje);
		enviarSMS(mensaje);
	}

	private void enviarSMS(String mensaje) {
		System.out.println("Enviando SMS: " + mensaje);
	}
}



// Decorador concreto: Email
class NotificadorEmail extends NotificadorDecorador {
	public NotificadorEmail(Notificador envoltorio) {
		super(envoltorio);
	}

	@Override
	public void enviar(String mensaje) {
		super.enviar(mensaje);
		enviarEmail(mensaje);
	}

	private void enviarEmail(String mensaje) {
		System.out.println("Enviando Email: " + mensaje);
	}
}

// Ejemplo de uso
class Main {
	public static void main(String[] args) {
		Notificador notificador = new NotificadorBasico();
		notificador = new NotificadorSMS(notificador);
		notificador = new NotificadorEmail(notificador);

		notificador.enviar("¡Examen de patrones de diseño!");
	}
}