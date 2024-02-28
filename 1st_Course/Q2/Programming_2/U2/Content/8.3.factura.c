#include <stdio.h>

#include "7.2.clientes.h"
#include "7.4.inventario.h"
#include "8.2.factura.h"

void create_factura(Factura factu[],Inventario invent[], int nro_factu)
{
   
    printf("Por favor ingrese la informacion del cliente a facturar:\n");
    printf("Numero de factura : ");

    scanf("%d", &factu[nro_factu].nro_factura);
    printf("tipo de coche del cliente que tiene hoy (1 para Berlina, 2 para Compacto y 3 para Cabriolet) : ");

    scanf("%d", &factu[nro_factu].coche);
    printf("Precio del coche: ");

    scanf(" %d", &factu[nro_factu].precio);
    printf("Cantidad: ");

    scanf(" %d", &factu[nro_factu].cantidad);

    printf("Nombre del cliente: ");

    scanf(" %s", factu[nro_factu].nombre);
    printf("Apellido del cliente: ");

    scanf("%s", factu[nro_factu].apellido);
    printf("identificador del cliente: ");

    scanf("%s", factu[nro_factu].NIF);
    printf("\n");

}


void print_factura(Factura factu[],int nro_factu)
{
    char * coche;
    int Totals = factu[nro_factu].precio * factu[nro_factu].cantidad;
    
    printf("----------Factura------------------------------------------|\n");
    printf("| Numero factura: %d \n", factu[nro_factu].nro_factura);

    switch(factu[nro_factu].coche) {
        case BERLINA: coche = "Berlina"; break;
        case COMPACTO: coche = "Compacto"; break;
        case CABRIOLET: coche = "Cabriolet"; break;
    }

    printf("| Coche: %s \n", coche);
    printf("| Apellido: %s \n", factu[nro_factu].apellido);
    printf("| NIF: %s \n", factu[nro_factu].NIF);
    printf("| Precio: %d \n", factu[nro_factu].precio);
    printf("| Cantidad: %d \n", factu[nro_factu].cantidad);
    printf("| TOTAL($): %d \n", Totals);
    printf("-----------------------------------------------------------|\n");
}

