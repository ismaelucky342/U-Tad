/***************************************************************************************/
/*                                                                                     */
/*                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        */
/*      AEC2 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       */
/*                                         ██║   ██║█████╗██║   ███████║██║  ██║       */
/*      created:        01/03/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       */
/*      last change:    15/03/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       */
/*                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        */
/*                                                                                     */
/*       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        */
/*                                                                                     */
/*       Github:  https://github.com/ismaelucky342/                                    */
/*                                                                                     */
/***************************************************************************************/

# include "../includes/lib.hpp"

/**
 * Función recursiva que calcula el número de combinaciones de n elementos tomados de r en r.
 *
 * La fórmula es: C(n, r) = n! / (r! * (n - r)!)
 * En este caso, se usa la propiedad recursiva:
 * C(n, r) = C(n-1, r-1) + C(n-1, r)
 * 
 * @details 
 *  * - Se usa argv y argc en vez de cin para recibir argumentos desde la línea de comandos. (mas capacidad de manejo de errores)
 *  * - La función combinaciones se llama recursivamente hasta que r es 0 o r es igual a n.
 *  * - Si r es 0 o r es igual a n, la función retorna 1, ya que hay exactamente una manera de elegir 0 o n elementos de un conjunto de n elementos.
 *  * - En caso contrario, la función retorna la suma de las combinaciones de (n-1, r-1) y (n-1, r).
 *
 * Precondiciones:
 * - n debe ser un número entero no negativo.
 * - r debe ser un número entero no negativo y menor o igual que n.
 *
 * Complejidad temporal: O(r), dado que cada llamada recursiva calcula el valor de C(n, r)
 * dividiendo el problema en dos subproblemas más pequeños.
 * Complejidad espacial: O(r), debido a las llamadas recursivas.
 */
int combinaciones(int n, int r)
{
    if (r == 0 || r == n)
        return 1;
    return combinaciones(n - 1, r - 1) + combinaciones(n - 1, r);
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        dprintf(2, RED "ERROR, Usage: %s <n> <r>\n" RESET, argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    int r = atoi(argv[2]);

    if (n < 0)
    {
        dprintf(2, RED "ERROR: n must be a non-negative integer." RESET);
        return 1;
    }

    if (r < 0 || r > n)
    {
        dprintf(2, RED "ERROR: r must be a non-negative integer and less than or equal to n.\n" RESET);
        return 1;
    }
    printf("%d\n", combinaciones(n, r));

    return 0;
}
