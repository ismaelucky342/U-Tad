public class Persona {
    // ATRIBUTOS: representan el estado del objeto
    private String nombre;
    private int edad;

    // CONSTRUCTOR: inicializa los atributos
    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // GETTERS: devuelven los valores de los atributos
    public String getNombre() { return nombre; }
    public int getEdad() { return edad; }

    // SETTERS: permiten modificar los valores de los atributos
    public void setNombre(String nuevoNombre) { this.nombre = nuevoNombre; }
    public void setEdad(int nuevaEdad) { this.edad = nuevaEdad; }

    // MÉTODO normal
    public void saludar() {
        System.out.println("Hola, me llamo " + nombre + " y tengo " + edad + " años.");
    }
}

// Clase principal para probar la clase Persona
public class Main {
	public static void main(String[] args) {
		// Crear un objeto Persona
		Persona persona = new Persona("Juan", 30);
		
		// Usar los métodos de la clase Persona
		persona.saludar();
		
		// Modificar los atributos usando setters
		persona.setNombre("Pedro");
		persona.setEdad(25);
		
		// Volver a saludar con los nuevos valores
		persona.saludar();
	}
}
