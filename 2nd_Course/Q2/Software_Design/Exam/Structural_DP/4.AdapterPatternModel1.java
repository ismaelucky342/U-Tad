/*### Variante 3.3 – **Adapter: Conversión de unidades**

**Enunciado:**

Tenemos una clase `SensorTemperaturaFahrenheit` que devuelve temperaturas en Fahrenheit con el método `leerF()`. Queremos usarla como si fuera un `SensorTemperaturaCelsius` con el método `leerC()`.

**Componentes requeridos:**

- `SensorTemperaturaCelsius` (interfaz esperada).
- `SensorTemperaturaFahrenheit` (clase existente).
- `TemperaturaAdapter`: adapta Fahrenheit a Celsius.

**Tarea:**

Dibuja el **diagrama UML** del patrón Adapter aplicado a este caso, indicando los tipos de relaciones.
*/

public interface SensorTemperaturaCelsius {
	double leerC();
}

public class SensorTemperaturaFahrenheit
{
	public double leerF() {
		// Simula la lectura de temperatura en Fahrenheit
		return 98.6; // Por ejemplo, 98.6°F
	}
}

public class TemperaturaAdapter implements SensorTemperaturaCelsius {
	private SensorTemperaturaFahrenheit sensorFahrenheit;

	public TemperaturaAdapter(SensorTemperaturaFahrenheit sensorFahrenheit) {
		this.sensorFahrenheit = sensorFahrenheit;
	}

	@Override
	public double leerC() {
		// Convertir Fahrenheit a Celsius
		double fahrenheit = sensorFahrenheit.leerF();
		return (fahrenheit - 32) * 5.0 / 9.0;
	}
}

public class Main {
	public static void main(String[] args) {
		// Crear un sensor de temperatura en Fahrenheit
		SensorTemperaturaFahrenheit sensorF = new SensorTemperaturaFahrenheit();
		
		// Adaptar el sensor de Fahrenheit a Celsius
		SensorTemperaturaCelsius sensorC = new TemperaturaAdapter(sensorF);
		
		// Leer la temperatura en Celsius
		double temperaturaC = sensorC.leerC();
		System.out.println("Temperatura en Celsius: " + temperaturaC);
	}
}