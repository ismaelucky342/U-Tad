#include <stdio.h>
#include "7.2.clientes.h"
#include "7.4.inventario.h"
#include "8.2.factura.h"

#define SIZE 3
#define CARS 3
#define FACT 2

 int main(){

    Cliente c[SIZE];
    Inventario v[CARS];
    Factura f[FACT];

    create_cliente(c,SIZE);
    print_cliente(c,SIZE);
    create_inventario(v,CARS);
    print_inventario(v,CARS);
    create_factura(f,v,1);
    print_factura(f,1);

 return 0;
}