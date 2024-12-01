/****************************************************************************************************/
/*                                                                                                  */
/*                            ██╗   ██╗   ████████╗ █████╗ ██████╗                                  */
/*                            ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗                                 */
/*                            ██║   ██║█████╗██║   ███████║██║  ██║                                 */
/*                            ██║   ██║╚════╝██║   ██╔══██║██║  ██║                                 */
/*                            ╚██████╔╝      ██║   ██║  ██║██████╔╝                                 */
/*                             ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝                                  */
/*                                                                                                  */
/*                              ismael.hernandez@live.u-tad.com                                     */
/*                                                                                                  */
/****************************************************************************************************/


#include "cache.h"
#include "utils.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void resolver_cache_tamano_memoria()
{
    int tam_memoria, tam_cache, tam_bloque;

    printf("Ingrese el tamaño de la memoria (en bytes): ");
    tam_memoria = leer_potencia_dos();
    printf("Ingrese el tamaño de la caché (en bytes): ");
    tam_cache = leer_potencia_dos();
    printf("Ingrese el tamaño del bloque (en bytes): ");
    tam_bloque = leer_potencia_dos();

    int num_lineas = tam_cache / tam_bloque;
    int bits_bloque = log2(tam_bloque);
    int bits_linea = log2(num_lineas);
    int bits_etiqueta = log2(tam_memoria) - (bits_bloque + bits_linea);

    printf("\nEstructura de la dirección:\n");
    printf("Bits de etiqueta: %d\n", bits_etiqueta);
    printf("Bits de línea: %d\n", bits_linea);
    printf("Bits de bloque: %d\n", bits_bloque);
}

void resolver_cache_hexadecimal()
{
    int tam_cache, tam_bloque;

    printf("Ingrese el tamaño de la caché (en bytes): ");
    tam_cache = leer_potencia_dos();
    printf("Ingrese el tamaño del bloque (en bytes): ");
    tam_bloque = leer_potencia_dos();

    int num_lineas = tam_cache / tam_bloque;
    int bits_bloque = log2(tam_bloque);
    int bits_linea = log2(num_lineas);

    printf("Ingrese una dirección en hexadecimal (sin 0x): ");
    unsigned int direccion_hex = leer_hexadecimal();

    int linea = (direccion_hex / tam_bloque) % num_lineas;
    int etiqueta = direccion_hex / (num_lineas * tam_bloque);

    printf("\nDescomposición de la dirección:\n");
    printf("Etiqueta: %d\n", etiqueta);
    printf("Línea: %d\n", linea);
    printf("Desplazamiento: %d\n", direccion_hex % tam_bloque);
}

void mostrar_ejemplos()
{
    printf("\n--- Ejemplo 1: Correspondencia directa ---\n");
    printf("Memoria: 64KB, Caché: 4KB, Bloque: 64B\n");
    printf("Resultado: Etiqueta: 9 bits, Línea: 6 bits, Bloque: 6 bits\n");

    printf("\n--- Ejemplo 2: Correspondencia asociativa ---\n");
    printf("Memoria: 32KB, Caché: 8KB, Bloque: 32B, Conjuntos: 4\n");
    printf("Resultado: Etiqueta: 10 bits, Conjunto: 4 bits, Bloque: 5 bits\n");
}

void mostrar_teoria()
{
    printf("\n--- Teoría de modos de correspondencia ---\n");
    printf("1. Directa: Cada bloque de memoria mapea a una única línea de caché.\n");
    printf("2. Asociativa: Un bloque puede estar en cualquier línea de caché.\n");
    printf("3. Asociativa por conjuntos: La memoria se divide en conjuntos, y un bloque puede estar en cualquier línea de su conjunto.\n");
}
