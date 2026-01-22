/*
 * MODELO B - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Gestor de Libros
 * 
 * PARTE 2 DEL EXAMEN - Método procesaLibro
 * 
 * QUE TE DAN:
 * - Esqueleto básico de la función procesaLibro
 * 
 * QUE TE PIDEN COMPLETAR:
 * 
 * PASOS A SEGUIR:
 * 
 * 1. VERIFICAR PUNTERO NULO
 *    - Comprobar si el puntero es NULL
 *    - Si es NULL, hacer return para salir
 * 
 * 2. MOSTRAR DATOS DEL LIBRO
 *    - Usar cout para mostrar el libro (con operador <<)
 * 
 * 3. AÑADIR 50 PÁGINAS
 *    - Obtener el número de páginas actual con getNumPaginas()
 *    - Sumar 50 páginas
 *    - Establecer el nuevo número con setNumPaginas()
 * 
 * 4. MOSTRAR PÁGINAS ACTUALIZADAS
 *    - Mostrar por pantalla el nuevo número de páginas
 */

#include "Libro.h"

void procesaLibro(Libro* libro) {
    // PASO 1: Comprobar puntero nulo
    if (libro == NULL) {
        return;
    }
    
    // PASO 2: Mostrar datos
    cout << "Libro: " << *libro << endl;
    
    // PASO 3: Añadir 50 páginas
    int paginasActuales = libro->getNumPaginas();
    libro->setNumPaginas(paginasActuales + 50);
    
    // PASO 4: Mostrar páginas actualizadas
    cout << "Páginas actualizadas: " << libro->getNumPaginas() << endl;
}
