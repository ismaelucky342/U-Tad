/*implementar una clase llamada ListaEnlazadaOrdenada que gestione una lista enlazada simple de enteros ordenados de forma ascendente. Aquí tienes un resumen de los requisitos y el ejemplo de uso:

Requisitos de la clase ListaEnlazadaOrdenada:
Debe incluir al menos los siguientes métodos públicos:

insertar(int valor)

Inserta el valor en la posición correspondiente para mantener el orden ascendente.

borrar(int valor)

Elimina el primer nodo que contenga ese valor (si existe).

buscar(int valor)

Devuelve true si el valor está en la lista, false en caso contrario.

imprimir()

Muestra la lista por pantalla.*/

#include <iostream>

class ListaEnlazadaOrdenada {
private:

    struct Nodo {
        int valor;
        Nodo* siguiente;
        Nodo(int v) : valor(v), siguiente(nullptr) {}
    };

    Nodo* cabeza;

public:
    ListaEnlazadaOrdenada() : cabeza(nullptr) {}

    ~ListaEnlazadaOrdenada() {
        while (cabeza) {
            Nodo* temp = cabeza;
            cabeza = cabeza->siguiente;
            delete temp;
        }
    }

    void insertar(int valor) {
        Nodo* nuevo = new Nodo(valor);
        if (!cabeza || valor < cabeza->valor) {
            nuevo->siguiente = cabeza;
            cabeza = nuevo;
            return;
        }

        Nodo* actual = cabeza;
        while (actual->siguiente && actual->siguiente->valor < valor) {
            actual = actual->siguiente;
        }

        nuevo->siguiente = actual->siguiente;
        actual->siguiente = nuevo;
    }

    void borrar(int valor) {
        if (!cabeza) return;

        if (cabeza->valor == valor) {
            Nodo* temp = cabeza;
            cabeza = cabeza->siguiente;
            delete temp;
            return;
        }

        Nodo* actual = cabeza;
        while (actual->siguiente && actual->siguiente->valor != valor) {
            actual = actual->siguiente;
        }

        if (actual->siguiente) {
            Nodo* temp = actual->siguiente;
            actual->siguiente = actual->siguiente->siguiente;
            delete temp;
        }
    }

    bool buscar(int valor) {
        Nodo* actual = cabeza;
        while (actual) {
            if (actual->valor == valor) return true;
            if (actual->valor > valor) break;
            actual = actual->siguiente;
        }
        return false;
    }

    void imprimir() {
        std::cout << "[";
        Nodo* actual = cabeza;
        while (actual) {
            std::cout << actual->valor;
            if (actual->siguiente) std::cout << ", ";
            actual = actual->siguiente;
        }
        std::cout << "]\n";
    }
};
