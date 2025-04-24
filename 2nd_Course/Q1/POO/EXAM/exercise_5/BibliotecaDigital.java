package exam;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
 * Desarrolla un programa para gestionar una biblioteca digital. El sistema debe permitir registrar usuarios, gestionar libros y realizar préstamos de libros.



Funcionalidades requeridas:







Detalles importantes:

Cada funcionalidad debe gestionar posibles errores usando excepciones, como:
                  Intentar prestar un libro que ya está prestado.

                  Intentar devolver un libro que no está en préstamo.

                  Registrar un usuario con un email ya existente.



Implementar validaciones para entrada de datos (p.ej., no aceptar un título de libro vacío).







/*Gestión de libros:
               Añadir libros con atributos: título, autor, ISBN y disponibilidad (prestado o no).

               Listar todos los libros disponibles y los que están actualmente prestados.

               Buscar libros por título o autor.
Gestión de libros:
               Añadir libros con atributos: título, autor, ISBN y disponibilidad (prestado o no).

               Listar todos los libros disponibles y los que están actualmente prestados.

               Buscar libros por título o autor.



Gestión de usuarios:
                Registrar usuarios con atributos: nombre, email y una lista de libros actualmente prestados.



Préstamos:
                Permitir que un usuario registrado pueda tomar prestado un libro disponible.

                Devolver un libro prestado.

                Restringir el número máximo de libros que un usuario puede tener en préstamo (por ejemplo, 3).



Almacenamiento:
                Guardar la lista de libros y usuarios en archivos separados.

                Cargar los datos al iniciar la aplicación.



Ejemplo de menú de la aplicación:

=== Menú principal ===

1. Gestionar libros

2. Gestionar usuarios

3. Realizar préstamo

4. Devolver libro

5. Guardar y salir Seleccione una opción:*/


/*programa principal*/


/*clase libro*/

public class BibliotecaDigital {

	public static void main(String[] args) {

        Biblioteca biblioteca = new Biblioteca();

        libro libro1 = new libro("El Señor de los Anillos", "J.R.R. Tolkien", "123456", true);
        libro libro2 = new libro("Cien años de soledad", "Gabriel García Márquez", "654321", true);
        libro libro3 = new libro("Don Quijote de la Mancha", "Miguel de Cervantes", "987654", false);

        biblioteca.addLibro(libro1);
        biblioteca.addLibro(libro2);
        biblioteca.addLibro(libro3);

        Usuario usuario1 = new Usuario("Alice", " [email protected]"); 
        Usuario usuario2 = new Usuario("Bob", " [email protected]");
        Usuario usuario3 = new Usuario("Charlie", " [email protected]");
        
        biblioteca.addUser(usuario1);
        biblioteca.addUser(usuario2);
        biblioteca.addUser(usuario3);
        
        int opcion = 0;
        
        
        while (opcion != 5) {
        	
        	System.out.println("=== Menú principal ===");
        	System.out.println("1. Gestionar libros");
        	System.out.println("2. Gestionar usuarios");
        	System.out.println("3. Realizar préstamo");
        	System.out.println("4. Devolver libro");
        	System.out.println("5. Guardar y salir");
        	System.out.println("Seleccione una opción:");
        	
        	//leo la opcion
        	Scanner sc = new Scanner(System.in);
        	opcion = sc.nextInt();
        	
        	//opcion 1
        	
        	if (opcion == 1) {
        		System.out.println("=== Menú de libros ===");
        		System.out.println("1. Añadir libro");
        		System.out.println("2. Listar libros");
        		System.out.println("3. Listar libros disponibles");
        		System.out.println("4. Listar libros prestados");
        		System.out.println("5. Buscar libro");
        		System.out.println("Seleccione una opción:");
        		
        		int opcionLibros = sc.nextInt();
        		
        		if (opcionLibros == 1) {
        			System.out.println("Introduzca el titulo del libro:");
        			String titulo = sc.next();
        			System.out.println("Introduzca el autor del libro:");
        			String autor = sc.next();
        			System.out.println("Introduzca el ISBN del libro:");
        			String ISBN = sc.next();
        			System.out.println("Introduzca la disponibilidad del libro (true/false):");
        			boolean disponibilidad = sc.nextBoolean();
        			
        			libro l = new libro(titulo, autor, ISBN, disponibilidad);
        			biblioteca.addLibro(l);
        		}
        		
        		if (opcionLibros == 2) {
        			biblioteca.listarLibros();
        		}
        		
        		if (opcionLibros == 3) {
        			biblioteca.listarLibrosDisponibles();
        		}
        		
        		if (opcionLibros == 4) {
        			biblioteca.listarLibrosPrestados();
        		}
        		
        		if (opcionLibros == 5) {
        			System.out.println("Introduzca el titulo del libro:");
        			String titulo = sc.next();
        			biblioteca.buscarLibro(titulo);
        		}
        		
        	}
        	//opcion 2
			if (opcion == 2) {
				System.out.println("=== Menú de usuarios ===");
				System.out.println("1. Registrar usuario");
				System.out.println("2. Listar usuarios");
				System.out.println("Seleccione una opción:");

				int opcionUsuarios = sc.nextInt();

				if (opcionUsuarios == 1) {
					System.out.println("Introduzca el nombre del usuario:");
					String nombre = sc.next();
					System.out.println("Introduzca el email del usuario:");
					String email = sc.next();

					Usuario u = new Usuario(nombre, email);
					biblioteca.addUser(u);
				}

				if (opcionUsuarios == 2) {
					for (Usuario u : biblioteca.usuarios) {
						System.out.println("Nombre: " + u.nombre + ", Email: " + u.email);
					}
				}
			}
			//opcion 3
			if (opcion == 3) {
				System.out.println("=== Menú de préstamos ===");
				System.out.println("Introduzca el email del usuario:");
				String email = sc.next();
				System.out.println("Introduzca el titulo del libro:");
				String titulo = sc.next();

				Usuario u = null;
				for (Usuario usuario : biblioteca.usuarios) {
					if (usuario.email.equals(email)) {
						u = usuario;
					}
				}

				libro l = null;
				for (libro libro : biblioteca.libros) {
					if (libro.titulo.equals(titulo)) {
						l = libro;
					}
				}

				if (u != null && l != null && l.disponibilidad) {
					l.disponibilidad = false;
					u.librosPrestados.add(l);
				} else {
					System.out.println("No se ha podido realizar el préstamo porque el libro no está disponible");
				}
			}
				
				//opcion 4
				if (opcion == 4) {
					System.out.println("=== Menú de devolución ===");
					System.out.println("Introduzca el email del usuario:");
					String email = sc.next();
					System.out.println("Introduzca el titulo del libro:");
					String titulo = sc.next();

					Usuario u = null;
					for (Usuario usuario : biblioteca.usuarios) {
						if (usuario.email.equals(email)) {
							u = usuario;
						}
					}

					libro l = null;
					for (libro libro : biblioteca.libros) {
						if (libro.titulo.equals(titulo)) {
							l = libro;
						}
					}

					if (u != null && l != null && !l.disponibilidad) {
						l.disponibilidad = true;
						u.librosPrestados.remove(l);
					} else {
						System.out.println("No se ha podido realizar la devolución porque el libro no está prestado");
					}
				}

				// opcion 5
				if (opcion == 5) {
					// guardar datos
					try {
						File file = new File("libros.txt");
						file.createNewFile();
					} catch (IOException e) {
						e.printStackTrace();
					}

					try {
						File file = new File("usuarios.txt");
						file.createNewFile();
					} catch (IOException e) {
						e.printStackTrace();
					}

					// salir
					System.out.println("Saliendo de la aplicación...");
					System.exit(0);
					
			}
				if (opcion != 5) {
					System.out.println("Seleccione una opción:");
				}
        }								
     }
}

	



