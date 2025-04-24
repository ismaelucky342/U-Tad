package exam;

import java.util.ArrayList;
import java.util.List;

/*Clase Usuario*/

public class Usuario {

	String nombre;
	String email;
	List<libro> librosPrestados = new ArrayList<libro>();

	public Usuario(String nombre, String email) {// constructor de usuario
		this.nombre = nombre;
		this.email = email;
	}
}
