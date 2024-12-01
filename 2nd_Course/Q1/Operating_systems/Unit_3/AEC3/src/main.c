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

void mostrar_menu()
{
    printf("\n--- Menú Principal ---\n");
    printf("1. Tipo de problema de caché 1 (Correspondencia directa)\n");
    printf("2. Tipo de problema de caché 2 (Correspondencia asociativa)\n");
    printf("3. Ejemplos prácticos\n");
    printf("4. Explicación teórica\n");
    printf("5. Salir\n");
    printf("Seleccione una opción: ");
}

int main()
{
    int opcion;
    do
    {
        mostrar_menu();
        opcion = leer_entero();
        switch (opcion)
        {
        case 1:
            printf("\n--- Problema de caché tipo 1 (Correspondencia directa) ---\n");
            resolver_cache_directa();
            break;
        case 2:
            printf("\n--- Problema de caché tipo 2 (Correspondencia asociativa) ---\n");
            resolver_cache_asociativa();
            break;
        case 3:
            printf("\n--- Ejemplos prácticos ---\n");
            mostrar_ejemplos();
            break;
        case 4:
            printf("\n--- Explicación teórica ---\n");
            mostrar_teoria();
            break;
        case 5:
            printf("\nSaliendo del programa...\n");
            break;
        default:
            printf("Opción no válida. Intente de nuevo.\n");
        }
    } while (opcion != 5);
    return 0;
}
