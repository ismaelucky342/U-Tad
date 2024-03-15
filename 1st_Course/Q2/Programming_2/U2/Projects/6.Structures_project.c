#include <stdio.h>
#define SIZE 3

/*STRUCT AREA*/
typedef enum coche_t{
    BERLINA = 1, COMPACTO = 2 , CABRIOLET = 3
}Coche;

typedef struct cliente_t{
    char nombre[30];
    char apellido[40];
    char NIF[9];
    Coche coche;
} Cliente;

/*PROTOTPE AREA*/
void create_cliente(Cliente client[], int size);
void print_cliente(Cliente client[], int size);

 
/*MAIN AREA*/
int main(){

    Cliente c[SIZE];
    create_cliente(c,SIZE);
    print_cliente(c,SIZE);

    return 0;
}

 

void create_cliente(Cliente client[], int size)
{
    printf("Por favor ingrese la informacion del cliente:\n");
    
    for(int i = 0; i < size; i++){
        printf("Nombre del cliente: ");
        scanf(" %s", client[i].nombre);
        printf("Apellido del cliente: ");
        scanf("%s", client[i].apellido);
        printf("identificador del cliente: ");
        scanf("%s", client[i].NIF);
        printf("tipo de coche del cliente que tiene hoy (1 para Berlina, 2 para Compacto y 3 para Cabriolet) : ");
        scanf("%d", &client[i].coche);
        printf("\n");
    }
}

void print_cliente(Cliente client[], int size){

    char * coche;
    for(int i = 0; i < size; i++){

        printf("----------Cliente------------------------------------------|\n");
        printf("| Nombre: %-40s |\n", client[i].nombre);
        printf("| Apellido: %-40s |\n", client[i].apellido);
        printf("| NIF: %-40s |\n", client[i].NIF);

        switch(client[i].coche) {
            case BERLINA: coche = "Berlina"; break;
            case COMPACTO: coche = "Compacto"; break;
            case CABRIOLET: coche = "Cabriolet"; break;
        }

        printf("| Coche: %-40s |\n", coche);
        printf("-----------------------------------------------------------|\n");
    }
}