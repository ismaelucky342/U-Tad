package exam;

import java.util.ArrayList;
import java.util.List;

public class Biblioteca {

	List<libro> libros = new ArrayList<libro>(); // array de libros 
	List<Usuario> usuarios = new ArrayList<Usuario>(); // array de usuarios 

	public void addLibro(libro l) {// metodo para registrar libro
		libros.add(l);
	}
	

	public void addUser(Usuario u) {// metodo para registrar usuario
		usuarios.add(u);
	}

	public void listarLibros() {// metodo para mostrar libros en listado
		for (libro l : libros) {
			System.out.println("Titulo: " + l.titulo + ", Autor: " + l.autor + ", ISBN: " + l.ISBN
					+ ", Disponibilidad: " + (l.disponibilidad ? "Disponible" : "No disponible"));
		}
	}

	public void listarLibrosDisponibles() {// metodo para mostrar los libros igualmente en listado pero filtrando solo los que estan disponibles 
		for (libro l : libros) {
			if (l.disponibilidad) {
				System.out.println("Titulo: " + l.titulo + ", Autor: " + l.autor + ", ISBN: " + l.ISBN);
			}
		}
	}

	public void listarLibrosPrestados() {// metodo para mostrar los libros igualmente en listado pero filtrando solo los que estan prestados a los usuarios
		for (libro l : libros) {
			if (!l.disponibilidad) {
				System.out.println("Titulo: " + l.titulo + ", Autor: " + l.autor + ", ISBN: " + l.ISBN);
			}
		}
	}

	public void buscarLibro(String titulo) {// metodo para buscar libro por titulo
		for (libro l : libros) {
			if (l.titulo.equals(titulo)) {
				System.out.println("Titulo: " + l.titulo + ", Autor: " + l.autor + ", ISBN: " + l.ISBN
						+ ", Disponibilidad: " + (l.disponibilidad ? "Disponible" : "No disponible"));
			}
		}
	}
}
