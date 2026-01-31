/*
 * MODELO C - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Gestor de Estudiantes
 * 
 * PARTE 2 DEL EXAMEN - Método procesaEstudiante
 * 
 * QUE TE DAN:
 * - Esqueleto básico de la función procesaEstudiante
 * 
 * QUE TE PIDEN COMPLETAR:
 * 
 * PASOS A SEGUIR:
 * 
 * 1. VERIFICAR PUNTERO NULO
 *    - Comprobar si el puntero es NULL
 *    - Si es NULL, hacer return para salir
 * 
 * 2. MOSTRAR DATOS DEL ESTUDIANTE
 *    - Usar cout para mostrar el estudiante (con operador <<)
 * 
 * 3. ACTUALIZAR NOTA MEDIA
 *    - Obtener la nota actual con getNotaMedia()
 *    - Sumar 0.5 puntos a la nota
 *    - Establecer la nueva nota con setNotaMedia()
 * 
 * 4. MOSTRAR NOTA ACTUALIZADA
 *    - Mostrar por pantalla la nueva nota
 */

#include "Estudiante.h"

void procesaEstudiante(Estudiante* estudiante) {
    // PASO 1: Comprobar puntero nulo
    if (estudiante == NULL) {
        return;
    }
    
    // PASO 2: Mostrar datos
    cout << "Estudiante: " << *estudiante << endl;
    
    // PASO 3: Actualizar nota media (sumar 0.5 puntos)
    float notaActual = estudiante->getNotaMedia();
    estudiante->setNotaMedia(notaActual + 0.5);
    
    // PASO 4: Mostrar nota actualizada
    cout << "Nueva nota: " << estudiante->getNotaMedia() << endl;
}
