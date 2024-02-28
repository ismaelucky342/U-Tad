#include <stdio.h>

#include "clientes.h"
#include "inventario.h"

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

void create_cliente(Cliente client[], int size){
    
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