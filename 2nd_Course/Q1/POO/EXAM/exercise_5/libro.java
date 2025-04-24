package exam;

public class libro {
	
	//declaramos variable titulo, autor, isbn y disponibilidad (boolean por si o no disponible)
	String titulo;
	String autor;
	String ISBN;
	boolean disponibilidad;

	public libro(String titulo, String autor, String ISBN, boolean disponibilidad) {//constructor de libro 
		this.titulo = titulo;
		this.autor = autor;
		this.ISBN = ISBN;
		this.disponibilidad = disponibilidad;
	}
}
