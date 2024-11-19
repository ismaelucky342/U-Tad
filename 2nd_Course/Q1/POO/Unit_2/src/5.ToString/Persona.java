public class Persona {
	private String nombre;

	public Persona(String nombre) {
		this.nombre = nombre;
	}

	@Override
	public String toString() {
		return "Persona{nombre='" + nombre + "'}";
	}

	public static void main(String[] args) {
		Persona persona = new Persona("John Doe");
		System.out.println(persona.toString());
	}
}