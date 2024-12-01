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

void validate_hex_input(unsigned int *address)
{
    while (scanf("%x", address) != 1)
    {
        printf("Entrada no válida. Ingrese una dirección en hexadecimal (sin 0x): ");
        while (getchar() != '\n'); // Limpiar el buffer de entrada
    }
}

void validate_int_input(int *value)
{
    while (scanf("%d", value) != 1)
    {
        printf("Entrada no válida. Ingrese un número entero: ");
        while (getchar() != '\n'); // Limpiar el buffer de entrada
    }
}
