#ifndef CLIENTES
#define CLIENTES

typedef enum coche_t
{
    BERLINA = 1, COMPACTO = 2 , CABRIOLET = 3
}Coche;

typedef struct cliente_t
{
    char nombre[30];
    char apellido[40];
    char NIF[9];
    Coche coche;
} Cliente;

void create_cliente(Cliente client[], int size);
void print_cliente(Cliente client[], int size);

#endif // CLIENTES