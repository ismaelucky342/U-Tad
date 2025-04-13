// el patrón adaptador permite que dos interfaces incompatibles trabajen juntas
// al envolver una de las interfaces en una clase adaptadora. Esto es útil
// cuando se desea reutilizar código existente sin modificarlo.

public interface EnchufeEuropeo {
	void conectar();
}

public class EnchufeAmericano {
	public void conectarAmericano() {
		System.out.println("Conectado al enchufe americano.");
	}
}



// Adaptador
public class AdaptadorEnchufe implements EnchufeEuropeo {
	private EnchufeAmericano enchufeAmericano;

	public AdaptadorEnchufe(EnchufeAmericano enchufeAmericano) {
		this.enchufeAmericano = enchufeAmericano;
	}

	@Override
	public void conectar() {
		enchufeAmericano.conectarAmericano();
	}
}

// Cliente
public class Main {
	public static void main(String[] args) {
		EnchufeAmericano enchufeAmericano = new EnchufeAmericano();
		EnchufeEuropeo adaptador = new AdaptadorEnchufe(enchufeAmericano);
		adaptador.conectar();
	}
}
