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

int main() {
    int choice;

    while (1) {
        printf("Menu:\n");
        printf("1. Cache problem type 1\n");
        printf("2. Cache problem type 2\n");
        printf("3. Exit\n");
        printf("Choose an option: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                cache_problem_1();
                break;
            case 2:
                cache_problem_2();
                break;
            case 3:
                printf("Saliendo...\n");
                exit(0);
            default:
                printf("Opción no válida. Inténtelo de nuevo.\n");
        }
    }

    return 0;
}
