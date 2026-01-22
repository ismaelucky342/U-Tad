/*
 * MODELO D - EXAMEN SISTEMAS DISTRIBUIDOS U3
 * Gestor de Productos
 * 
 * PARTE 2 DEL EXAMEN - Método aplicaDescuento
 * 
 * QUE TE DAN:
 * - Esqueleto básico de la función aplicaDescuento
 * 
 * QUE TE PIDEN COMPLETAR:
 * 
 * PASOS A SEGUIR:
 * 
 * 1. VERIFICAR PUNTERO NULO
 *    - Comprobar si el puntero es NULL
 *    - Si es NULL, hacer return para salir
 * 
 * 2. MOSTRAR DATOS DEL PRODUCTO
 *    - Usar cout para mostrar el producto (con operador <<)
 * 
 * 3. APLICAR DESCUENTO DEL 10%
 *    - Obtener el precio actual con getPrecio()
 *    - Calcular el nuevo precio: precio * 0.9 (10% de descuento)
 *    - Establecer el nuevo precio con setPrecio()
 * 
 * 4. MOSTRAR PRECIO ACTUALIZADO
 *    - Mostrar por pantalla el nuevo precio
 */

#include "Producto.h"

void aplicaDescuento(Producto* producto) {
    // PASO 1: Comprobar puntero nulo
    if (producto == NULL) {
        return;
    }
    
    // PASO 2: Mostrar datos
    cout << "Producto: " << *producto << endl;
    
    // PASO 3: Aplicar descuento del 10%
    double precioActual = producto->getPrecio();
    producto->setPrecio(precioActual * 0.9);
    
    // PASO 4: Mostrar precio actualizado
    cout << "Precio con descuento: " << producto->getPrecio() << "€" << endl;
}
