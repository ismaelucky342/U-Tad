// El patrón State permite a un objeto cambiar su comportamiento
// en función de su estado interno. En este ejemplo, se
// implementa un sistema de gestión de pedidos que cambia
// su comportamiento según el estado del pedido (por ejemplo,
// "Pendiente", "En preparación", "Entregado"). El patrón
// State permite encapsular el comportamiento específico de
// cada estado en clases separadas, lo que facilita la
// extensión y el mantenimiento del código.

// en pocas palabras, el patrón State permite a un objeto
// cambiar su comportamiento cuando cambia su estado interno.

public interface State {
	void OrdenarPedido();
	void PrepararPedido();
	void EntregarPedido();
	void CancelarPedido();
}

// Clase concreta que representa el estado "Pendiente"
class PendienteState implements State {
	private Pedido pedido;

	public PendienteState(Pedido pedido) {
		this.pedido = pedido;
	}

	@Override
	public void OrdenarPedido() {
		System.out.println("El pedido ya está en estado pendiente.");
	}

	@Override
	public void PrepararPedido() {
		System.out.println("Preparando el pedido...");
		pedido.setState(new PreparandoState(pedido));
	}

	@Override
	public void EntregarPedido() {
		System.out.println("No se puede entregar un pedido pendiente.");
	}

	@Override
	public void CancelarPedido() {
		System.out.println("Cancelando el pedido...");
		pedido.setState(new CanceladoState(pedido));
	}
}

// Clase concreta que representa el estado "Preparando"
class PreparandoState implements State {
	private Pedido pedido;

	public PreparandoState(Pedido pedido) {
		this.pedido = pedido;
	}

	@Override
	public void OrdenarPedido() {
		System.out.println("El pedido ya está en preparación.");
	}

	@Override
	public void PrepararPedido() {
		System.out.println("El pedido ya está en preparación.");
	}

	@Override
	public void EntregarPedido() {
		System.out.println("Entregando el pedido...");
		pedido.setState(new EntregadoState(pedido));
	}

	@Override
	public void CancelarPedido() {
		System.out.println("Cancelando el pedido...");
		pedido.setState(new CanceladoState(pedido));
	}
}

// Clase concreta que representa el estado "Entregado"
class EntregadoState implements State {
	private Pedido pedido;

	public EntregadoState(Pedido pedido) {
		this.pedido = pedido;
	}

	@Override
	public void OrdenarPedido() {
		System.out.println("El pedido ya ha sido entregado.");
	}

	@Override
	public void PrepararPedido() {
		System.out.println("El pedido ya ha sido entregado.");
	}

	@Override
	public void EntregarPedido() {
		System.out.println("El pedido ya ha sido entregado.");
	}

	@Override
	public void CancelarPedido() {
		System.out.println("No se puede cancelar un pedido entregado.");
	}
}

// Clase concreta que representa el estado "Cancelado"
class CanceladoState implements State {
	private Pedido pedido;

	public CanceladoState(Pedido pedido) {
		this.pedido = pedido;
	}

	@Override
	public void OrdenarPedido() {
		System.out.println("El pedido ha sido cancelado.");
	}

	@Override
	public void PrepararPedido() {
		System.out.println("El pedido ha sido cancelado.");
	}

	@Override
	public void EntregarPedido() {
		System.out.println("El pedido ha sido cancelado.");
	}

	@Override
	public void CancelarPedido() {
		System.out.println("El pedido ya ha sido cancelado.");
	}
}

// Clase que representa el pedido
class Pedido {
	private State state;

	public Pedido() {
		state = new PendienteState(this);
	}

	public void setState(State state) {
		this.state = state;
	}

	public void OrdenarPedido() {
		state.OrdenarPedido();
	}

	public void PrepararPedido() {
		state.PrepararPedido();
	}

	public void EntregarPedido() {
		state.EntregarPedido();
	}

	public void CancelarPedido() {
		state.CancelarPedido();
	}
}

// Clase principal para probar el patrón State
public class Main {
	public static void main(String[] args) {
		Pedido pedido = new Pedido();

		pedido.OrdenarPedido(); // Estado: Pendiente
		pedido.PrepararPedido(); // Estado: Preparando
		pedido.EntregarPedido(); // Estado: Entregado
		pedido.CancelarPedido(); // Estado: Cancelado
	}
}
