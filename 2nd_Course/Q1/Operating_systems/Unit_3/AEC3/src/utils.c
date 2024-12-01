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
        printf("Invalid input. Please enter a hexadecimal address (without 0x): ");
        while (getchar() != '\n'); // Clear the input buffer
    }
}

void validate_int_input(int *value)
{
    while (scanf("%d", value) != 1)
    {
        printf("Invalid input. Please enter an integer: ");
        while (getchar() != '\n'); // Clear the input buffer
    }
}
