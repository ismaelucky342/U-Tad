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

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "utils.h"

int leer_entero()
{
    int valor;
    if (scanf("%d", &valor) != 1)
    {
        printf("Entrada inválida. Saliendo...\n");
        exit(EXIT_FAILURE);
    }
    return valor;
}

int leer_potencia_dos()
{
    int valor = leer_entero();
    if ((valor & (valor - 1)) != 0)
    {
        printf("Error: El valor ingresado no es una potencia de 2. Intente de nuevo.\n");
        exit(EXIT_FAILURE);
    }
    return valor;
}
