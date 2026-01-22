/*
 * MODELO A - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Gestor de Clientes
 * 
 * PARTE 2 DEL EXAMEN - Método atiendeCliente
 * 
 * QUE TE DAN:
 * - Esqueleto básico de la función atiendeCliente
 * 
 * QUE TE PIDEN COMPLETAR:
 * 
 * PASOS A SEGUIR:
 * 
 * 1. VERIFICAR PUNTERO NULO
 *    - Comprobar si el puntero es NULL
 *    - Si es NULL, hacer return para salir
 * 
 * 2. MOSTRAR DATOS DE LA PERSONA
 *    - Usar cout para mostrar la persona (con operador <<)
 * 
 * 3. ACTUALIZAR EDAD
 *    - Obtener la edad actual con getEdad()
 *    - Sumar 1 a la edad
 *    - Establecer la nueva edad con setEdad()
 * 
 * 4. MOSTRAR EDAD ACTUALIZADA
 *    - Mostrar por pantalla la nueva edad
 */

#include "Persona.h"

void atiendeCliente(Persona* cliente) {
    // PASO 1: Comprobar puntero nulo
    if (cliente == NULL) {
        return;
    }
    
    // PASO 2: Mostrar datos
    cout << "Cliente: " << *cliente << endl;
    
    // PASO 3: Actualizar edad (sumar 1)
    int edadActual = cliente->getEdad();
    cliente->setEdad(edadActual + 1);
    
    // PASO 4: Mostrar edad actualizada
    cout << "Nueva edad: " << cliente->getEdad() << endl;
}
