/*
El siguiente algoritmo, implementado en el método main de la clase CalculaArea, 
calcula el área de un círculo o un cuadrado, formas geométricas cuya área solo 
depende de un parámetro, radio y lado respectivamente. Identificaremos los componentes 
necesarios para generar una nueva versión aplicando el patrón Strategy.
*/

import java.util.Scanner;

//interfaz estrategia Area 
public interface AreaStrategy {

	public Double calculaArea(Double parametro);

}

//algoritmo estrategia concreta para circulos
public class CircleAreaStrategy implements AreaStrategy {

	public Double calculaArea(Double parametro) {

		return Math.PI * Math.pow(parametro, 2);

	}

}

//algoritmo estrategia concreta para cuadrados
public class SquareAreaStrategy implements AreaStrategy {

	public Double calculaArea(Double parametro) {

		return Math.pow(parametro, 2);

	}

}

public class ContextAreaStrategy {

	// 1. Interface común como componente privado

	private AreaStrategy areaStrategy;

	// 2. La estrategia debe establecerse como parámetro de constructor

	public ContextAreaStrategy(AreaStrategy areaStrategy) {

		super();
		this.areaStrategy = areaStrategy;

	}

	public AreaStrategy getAreaStrategy() {

		return areaStrategy;

	}

	// 3. La estrategia debe ser intercambiable

	public void setAreaStrategy(AreaStrategy areaStrategy) {

		this.areaStrategy = areaStrategy;

	}

	public Double calculaArea(Double parametro) {

		// 4. Delegación por composición (agregación)

		return this.areaStrategy.calculaArea(parametro);

	}

}

public class AreaStrategyTest {

	public static void main(String[] args) {

		ContextAreaStrategy contextAreaStrategy

				= new ContextAreaStrategy(new SquareAreaStrategy());

		StringBuilder figureMessage

				= new StringBuilder("The area of ");

		Double optionValue = 0.0;

		Scanner sc = new Scanner(System.in);

		System.out.println("Choose selection of area to calculate:");

		System.out.println("1.Square 2.Circle");

		int n = sc.nextInt();

		switch (n) {

			case 1:

				System.out.println("Type the square side (cm) :");

				optionValue = sc.nextDouble();

				figureMessage.append("square is ");

				figureMessage.append(contextAreaStrategy.calculaArea(optionValue) + "     cm(s)");

				System.out.println(figureMessage);

				break;

			case 2:

				System.out.println("Type the circle radius (cm):");

				optionValue = sc.nextDouble();

				contextAreaStrategy.setAreaStrategy(new CircleAreaStrategy());

				figureMessage.append("circle is ");

				figureMessage.append(contextAreaStrategy.calculaArea(optionValue) +
						" cm(s)");
				System.out.println(figureMessage);
				break;
			default:
				figureMessage.append(" figure is not available");
				System.out.println(figureMessage);
		}
		sc.close();
	}
}
