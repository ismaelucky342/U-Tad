/*
Encajar piezas cuadradas en agujeros redondos
Este sencillo ejemplo muestra el modo en que un Adapter puede hacer que objetos incompatibles trabajen juntos.
*/

public class RoundHole {
	// Atributo que representa el radio del agujero redondo
	// Este atributo almacena el tamaño del agujero redondo, que es la distancia desde
	// su centro hasta el borde del agujero.
	private double radius;

	// Constructor que recibe el radio del agujero redondo
	// Este constructor inicializa el radio del agujero redondo.
	// El radio es la distancia desde el centro del agujero hasta su borde.
	public RoundHole(double radius) {
		this.radius = radius;
	}

	// Método que devuelve el radio del agujero redondo
	// Este método permite obtener el tamaño del agujero redondo.
	// El radio es la distancia desde el centro del agujero hasta su borde.
	public double getRadius() {
		return radius;
	}

	// Método que verifica si una pieza redonda (RoundPeg) cabe en el agujero
	// Este método toma un objeto RoundPeg como argumento y verifica si su radio es menor o
	// igual al radio del agujero redondo. Si es así, la pieza cabe en
	public boolean fits(RoundPeg peg) {
		return this.radius >= peg.getRadius();
	}
}

public class RoundPeg {
	// Atributo que representa el radio de la pieza redonda
	// Este atributo almacena el tamaño de la pieza redonda, que es la distancia desde
	// su centro hasta el borde de la pieza.
	private double radius;

	// Constructor que recibe el radio de la pieza redonda
	// Este constructor inicializa el radio de la pieza redonda.
	// El radio es la distancia desde el centro de la pieza hasta su borde.
	public RoundPeg(double radius) {
		this.radius = radius;
	}

	// Método que devuelve el radio de la pieza redonda
	// Este método permite obtener el tamaño de la pieza redonda.
	public double getRadius() {
		return radius;
	}
}

public class SquarePeg {
	// Atributo que representa el tamaño de la pieza cuadrada
	// Este atributo almacena el tamaño de la pieza cuadrada, que es la longitud de uno de sus lados.
	private double width;

	// Constructor que recibe el tamaño de la pieza cuadrada
	// Este constructor inicializa el tamaño de la pieza cuadrada.
	public SquarePeg(double width) {
		this.width = width;
	}

	// Método que devuelve el tamaño de la pieza cuadrada
	// Este método permite obtener el tamaño de la pieza cuadrada.
	public double getWidth() {
		return width;
	}
}

public class SquarePegAdapter extends RoundPeg {
	// Atributo que representa la pieza cuadrada adaptada
	// Este atributo almacena la pieza cuadrada que se está adaptando para que funcione con el agujero redondo.
	private SquarePeg squarePeg;

	// Constructor que recibe una pieza cuadrada y calcula su radio equivalente
	// Este constructor inicializa la pieza cuadrada y calcula su radio equivalente.
	public SquarePegAdapter(SquarePeg squarePeg) {
		// El radio de la pieza cuadrada adaptada se calcula como el radio de un círculo inscrito en el cuadrado.
		super(squarePeg.getWidth() * Math.sqrt(2) / 2);
		this.squarePeg = squarePeg;
	}

	// Método que devuelve el ancho de la pieza cuadrada adaptada
	// Este método permite obtener el tamaño de la pieza cuadrada adaptada.
	public double getWidth() {
		return squarePeg.getWidth();
	}
}

public class Main {
	public static void main(String[] args) {
		// Crear un agujero redondo con un radio de 5
		RoundHole hole = new RoundHole(5);

		// Crear una pieza redonda con un radio de 4
		RoundPeg roundPeg = new RoundPeg(4);
		System.out.println("Round peg fits: " + hole.fits(roundPeg)); // Debería ser true

		// Crear una pieza cuadrada con un ancho de 6
		SquarePeg squarePeg = new SquarePeg(6);
		SquarePegAdapter squarePegAdapter = new SquarePegAdapter(squarePeg);
		System.out.println("Square peg fits: " + hole.fits(squarePegAdapter)); // Debería ser false
	}
}