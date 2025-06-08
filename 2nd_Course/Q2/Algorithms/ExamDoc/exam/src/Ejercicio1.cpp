#include "../includes/lib.hpp"

using namespace std;

/*
 * Clase Producto
 * Atributos:
 * - nombre
 * - precio
 * */
class Producto
{
public:
	string nombre;
	float precio;

	Producto(const string &n, float p) : nombre(n), precio(p) {}
};

/*
 * Algoritmo de Ordenación de Producto
 * Método Quickshort
 *
 * */

void ordenarProductos(vector<pair<string, float>> &productos)
{
	sort(productos.begin(), productos.end(), [](const pair<string, float> &a, const pair<string, float> &b)
		 { return a.second < b.second; });
}
/*
 * Método para ingresar productos
 * Se solicita Nombre y precio
 * En caso de no ingresar nada tanto en nombre como en precio
 * Se devuelve mensaje de error y se le vuevle a solicitar de nuevo
 * */
void ingresarProductos(vector<pair<string, float>> &productos, int n)
{
	for (int i = 0; i < n; ++i)
	{
		string nombre;
		float precio;
		cout << "Producto " << i + 1 << ":" << endl;
		cout << "Nombre: ";
		getline(cin, nombre);
		if (nombre.empty())
		{
			cout << RED << "El nombre del producto no puede estar vacío. Inténtalo de nuevo." RESET << endl;
			--i;
			continue;
		}
		cout << "Precio: ";
		cin >> precio;
		cin.ignore();
		productos.emplace_back(nombre, precio);
	}
}

/*
 * Algorimto para buscar y mostrar producto
 *
 * */
void mostrarProductos(const vector<pair<string, float>> &productos)
{
	cout << BLUE << "--- Lista de productos ordenada por precio ---" RESET << endl;
	for (size_t i = 0; i < productos.size(); ++i)
	{
		cout << GREEN << i + 1 << ". " << productos[i].first << " - $" << productos[i].second << RESET << endl;
	}
}

/*
 * Main
 * Entrada de Usuario, se le solicita al usuario el numero de productos que va a introducir
 * Se protege la entrada con una validación que contempla números negativos
 * Devuelve error y ignora lo ingresado
 *
 * */
int main()
{
	int n;
	cout << GREEN "--- Bienvenido, Introduce el número de productos: ---" RESET << endl;
	cin >> n;
	cin.ignore();
	while (n <= 0)
	{
		cout << RED << "Por favor, introduce un número válido de productos: " RESET;
		cin >> n;
		cin.ignore();
	}

	vector<pair<string, float>> productos;

	ingresarProductos(productos, n);
	ordenarProductos(productos);
	mostrarProductos(productos);

	return 0;
}
