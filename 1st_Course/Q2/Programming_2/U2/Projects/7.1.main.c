#include <stdio.h>
#include "7.2.clientes.h"
#include "7.4.inventario.h"
 
#define SIZE 3
#define CARS 3

int main(){
    Cliente c[SIZE];
    Inventario v[CARS];

        create_cliente(c,SIZE);

        print_cliente(c,SIZE);
        create_inventario(v,CARS);

        print_inventario(v,CARS);
    return 0;
}