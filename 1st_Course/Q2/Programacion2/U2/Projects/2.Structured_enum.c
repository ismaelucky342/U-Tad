#include <stdio.h>
#include <stdlib.h>

enum menu
{
    alta = 49, baja = 50, modificacion = 51, salir = 52
};

int main()
{
    int opcion = 0;
    enum menu user;
    printf(" 1- Alta de registro \n 2- Baja de registro \n 3- Modificación de registro \n 4- Salir\n");
    opcion = getchar();
    user = opcion;
     switch(user){
       case alta:
            printf("Se va a dar de alta un registro \n");
            break;
        case baja:
            printf("Se va a dar de baja un registro \n");
            break;
        case modificacion:
            printf("Se va a modificar un registro \n");
            break;
        case salir:
             printf("Fin Programa \n");
             break;
        default:
            printf("Error! Valor no permitido \n");
            break;
    }
    return 0;
}