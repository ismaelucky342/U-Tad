// El patron puente es un patrón de diseño estructural que
// permite separar la abstracción de su implementación, de modo que
// ambas puedan variar de forma independiente. Este patrón es útil
// cuando se desea evitar el acoplamiento entre la abstracción y la
// implementación, lo que permite cambiar la implementación sin
// afectar a la abstracción y viceversa.

// De forma práctica nos permite crear una jerarquía de clases
// que pueden variar de forma independiente, lo que facilita la
// extensión y el mantenimiento del código.

public interface Vehiculo {
	void Acelerar();
	void Frenar();
	void Arrancar();
	void Apagar();
}

// Implementador concreto 1

public class Coche implements Vehiculo {
	@Override
	public void Acelerar() {
		System.out.println("El coche está acelerando.");
	}

	@Override
	public void Frenar() {
		System.out.println("El coche está frenando.");
	}

	@Override
	public void Arrancar() {
		System.out.println("El coche ha arrancado.");
	}

	@Override
	public void Apagar() {
		System.out.println("El coche se ha apagado.");
	}
}

// Implementador concreto 2
public class Moto implements Vehiculo {
	@Override
	public void Acelerar() {
		System.out.println("La moto está acelerando.");
	}

	@Override
	public void Frenar() {
		System.out.println("La moto está frenando.");
	}

	@Override
	public void Arrancar() {
		System.out.println("La moto ha arrancado.");
	}

	@Override
	public void Apagar() {
		System.out.println("La moto se ha apagado.");
	}
}

// Abstracción
public abstract class VehiculoAbstraccion {
	protected Vehiculo vehiculo;

	public VehiculoAbstraccion(Vehiculo vehiculo) {
		this.vehiculo = vehiculo;
	}

	public abstract void Acelerar();
	public abstract void Frenar();
	public abstract void Arrancar();
	public abstract void Apagar();
}

// Abstracción refinada 1
public class CocheAbstraccion extends VehiculoAbstraccion {
	public CocheAbstraccion(Vehiculo vehiculo) {
		super(vehiculo);
	}

	@Override
	public void Acelerar() {
		vehiculo.Acelerar();
	}

	@Override
	public void Frenar() {
		vehiculo.Frenar();
	}

	@Override
	public void Arrancar() {
		vehiculo.Arrancar();
	}

	@Override
	public void Apagar() {
		vehiculo.Apagar();
	}
}

// Abstracción refinada 2

public class MotoAbstraccion extends VehiculoAbstraccion {
	public MotoAbstraccion(Vehiculo vehiculo) {
		super(vehiculo);
	}

	@Override
	public void Acelerar() {
		vehiculo.Acelerar();
	}

	@Override
	public void Frenar() {
		vehiculo.Frenar();
	}

	@Override
	public void Arrancar() {
		vehiculo.Arrancar();
	}

	@Override
	public void Apagar() {
		vehiculo.Apagar();
	}
}

// Main para probar el patrón Bridge
public class Main {
	public static void main(String[] args) {
		Vehiculo coche = new Coche();
		VehiculoAbstraccion cocheAbstraccion = new CocheAbstraccion(coche);
		cocheAbstraccion.Arrancar();
		cocheAbstraccion.Acelerar();
		cocheAbstraccion.Frenar();
		cocheAbstraccion.Apagar();

		Vehiculo moto = new Moto();
		VehiculoAbstraccion motoAbstraccion = new MotoAbstraccion(moto);
		motoAbstraccion.Arrancar();
		motoAbstraccion.Acelerar();
		motoAbstraccion.Frenar();
		motoAbstraccion.Apagar();
	}
}
