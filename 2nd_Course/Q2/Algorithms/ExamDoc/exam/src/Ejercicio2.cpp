#include "../includes/lib2.hpp"

/*
* ListaEnlazada
 * @param
 * Constructor por parámetros. ListaEnlazada()
 * Destructor.
 * Nodo* getNodo(int posición)
 * Licencia getValor(int pos)
 * void setValor(int pos, Licencia val)
 * int getN()
 * void insertar(int pos, Licencia val)
 * void eliminar(int pos)
 * int buscar(Licencia val)
 * void imprimir() Provista en la plantilla
 * */
class ListaEnlazada
{
	Nodo *lista;

	int n;

	Nodo * getNodo (int posicion)
	{
		if (posicion < 0 || posicion >= n) {
			return nullptr;
		}

		Nodo *actual = lista;
		for (int i = 0; i < posicion; i++) {
			actual = actual->siguienteNodo;
		}
		return actual;
	}

public:

	ListaEnlazada()
	{
		lista = nullptr;
		n = 0;
	}

	Licencia getValor(int posicion)
	{
		Nodo *nodo = getNodo(posicion);
		if (nodo != nullptr) {
			return nodo->elemento;
		} else {
			throw std::out_of_range("ERROR:Posición fuera de rango");
		}
	}


	void setValor(int posicion, Licencia nuevoValor)
	{
		Nodo *nodo = getNodo(posicion);
		if (nodo != nullptr) {
			nodo->elemento = nuevoValor;
		} else {
			throw std::out_of_range("ERROR:Posición fuera de rango");
		}
	}

	int getN()
	{
		return n;
	}

	void insertar (int posicion, Licencia nuevoValor)
	{
		if (posicion < 0 || posicion > n) {
			throw std::out_of_range("ERROR:Posición fuera de rango");
		}

		Nodo *nuevoNodo = new Nodo;
		nuevoNodo->elemento = nuevoValor;

		if (posicion == 0) {
			nuevoNodo->siguienteNodo = lista;
			lista = nuevoNodo;
		} else {
			Nodo *anterior = getNodo(posicion - 1);
			nuevoNodo->siguienteNodo = anterior->siguienteNodo;
			anterior->siguienteNodo = nuevoNodo;
		}

		n++;
	}

	void eliminar (int posicion)
	{
		if (posicion < 0 || posicion >= n) {
			throw std::out_of_range("ERROR:Posición fuera de rango");
		}

		Nodo *nodoAEliminar;

		if (posicion == 0) {
			nodoAEliminar = lista;
			lista = lista->siguienteNodo;
		} else {
			Nodo *anterior = getNodo(posicion - 1);
			nodoAEliminar = anterior->siguienteNodo;
			anterior->siguienteNodo = nodoAEliminar->siguienteNodo;
		}

		delete nodoAEliminar;
		n--;
	}

	int buscar(Licencia elementoABuscar)
	{
		Nodo *actual = lista;
		int posicion = 0;

		while (actual != nullptr) {
			if (actual->elemento.codigo == elementoABuscar.codigo) {
				return posicion;
			}
			actual = actual->siguienteNodo;
			posicion++;
		}

		return -1;
	}
	
	void imprimir()
	{
		Nodo *actual = lista;
		while (actual != nullptr) {
			std::cout << "Codigo: " << actual->elemento.codigo 
					  << ", Herramienta: " << actual->elemento.herramienta << std::endl;
			actual = actual->siguienteNodo;
		}
	}
	
	~ListaEnlazada()
	{
		Nodo *actual = lista;
		while (actual != nullptr) {
			Nodo *siguiente = actual->siguienteNodo;
			delete actual;
			actual = siguiente;
		}
	}
};

/*
* Licencias
 * @param
 * int capacidad
 * int n
 * ListaEnlazada *tabla
 * Constructor por parámetros. Licencias(int capacidad)
 * int obtenerPosición(long codigo).
 * Nota: La función hash estará basada en el resto de la división entre capacidad
 * void insertarLicencia(long codigo, string herramienta).
 * void eliminarLicencia(long codigo). Siempre se va a considerar que la herramienta SI existe
 * void imprimirTabla() (propocionada en la plantilla)
 * */
class Licencias
{

	protected:

		int capacidad; 
		int n; 

		ListaEnlazada *tabla; 
	public:

		Licencias(int capacidad)
		{
			this->capacidad = capacidad;
			this->n = 0;
			tabla = new ListaEnlazada[capacidad];
		}

		int obtenerPosicion (long codigo)
		{
			int posicion = codigo % capacidad;
			return posicion;
		}

		void insertarLicencia (long codigo, string herramienta)
		{
			if (n >= capacidad) {
				std::cout << RED << "ERROR: Tabla llena, no se puede insertar." << RESET << std::endl;
				return;
			}

			int posicion = obtenerPosicion(codigo);
			Licencia nuevaLicencia = {codigo, herramienta};

			if (tabla[posicion].buscar(nuevaLicencia) != -1) {
				std::cout << RED << "ERROR: Licencia ya existe en la tabla." << RESET << std::endl;
				return;
			}

			tabla[posicion].insertar(tabla[posicion].getN(), nuevaLicencia);
			n++;
		}

		void eliminarLicencia (long codigo)
		{
			int posicion = obtenerPosicion(codigo);
			Licencia licenciaAEliminar = {codigo, ""};

			int indice = tabla[posicion].buscar(licenciaAEliminar);
			if (indice != -1) {
				tabla[posicion].eliminar(indice);
				n--;
				std::cout << GREEN << "Licencia eliminada correctamente." << RESET << std::endl;
			} else {
				std::cout << RED << "ERROR: Licencia no encontrada." << RESET << std::endl;
			}
		}

		void imprimir()
		{
			for (int i = 0; i < capacidad; i++) {
				std::cout << "Posición " << i << ": ";
				tabla[i].imprimir();
			}
		}

};


/*
* Main Comandos a implementar 
 * A: añadir a la tabla 
 * E: eliminar una herramienta
 * I: imprimir la tabla 
 * S: salir del programa
 * Prompt generado personalizado
 * Validaciones en caso de no insertar nada
 * Control de espacios y tabulaciones en la entrada de argumentos
 * 
 * */
int main () 
{
	int capacidad;
	std::cout << BLUE << "---BIENVENIDO A ADAL.SA---" << RESET << std::endl;
	std::cout << BLUE << "Porfavor, introduce la capacidad de la tabla: " << RESET << std::endl;
	std::cin >> capacidad;

	Licencias licencias(capacidad);
	char comando;
	long codigo;
	std::string herramienta;

	while (true) {
		std::cout << GREEN <<  "Introduce un comando(A: añadir, E: eliminar, I: imprimir, S: salir): " << RESET;
		std::cin >> comando;

		switch (comando) {
			case 'A':
				std::cout << GREEN <<  "Codigo de licencia: "<< RESET;
				std::cin >> codigo;
				std::cout << GREEN <<  "Nombre de la herramienta: "<< RESET;
				std::cin >> herramienta;
				licencias.insertarLicencia(codigo, herramienta);
				break;
			case 'E':
				std::cout  << GREEN << "Codigo de licencia a eliminar: "<< RESET;
				std::cin >> codigo;
				licencias.eliminarLicencia(codigo);
				break;
			case 'I':
				licencias.imprimir();
				break;
			case 'S':
				return 0;
			default:
				std::cout << RED << "ERROR: Comando no reconocido." << RESET << std::endl;
		}
	}
}
