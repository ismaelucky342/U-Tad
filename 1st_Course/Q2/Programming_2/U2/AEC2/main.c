#include <stdio.h>
#include "User.h"
#include "books.h"
#include "orders.h"

int main() {
    // Crear 3 usuarios
    User users[3];
   for (int i = 0; i < 3; i++) {
        printf("Ingrese el nombre del usuario %d: ", i + 1);
        scanf("%s", users[i].Name);
        printf("Ingrese el apellido del usuario %d: ", i + 1);
        scanf("%s", users[i].apellido);
        printf("Ingrese el ID de usuario %d: ", i + 1);
        scanf("%d", &users[i].UserID);
        printf("Ingrese la edad del usuario %d: ", i + 1);
        scanf("%d", &users[i].age);
        
        // Verificar el correo electrónico
        do {
            printf("Ingrese el correo electrónico del usuario %d: ", i + 1);
            scanf("%s", users[i].correo);
            if (strchr(users[i].correo, '@') == NULL) {
                printf("Error: El correo electrónico debe contener el símbolo '@'. Intente nuevamente.\n");
            }
        } while (strchr(users[i].correo, '@') == NULL);
        
        printf("Ingrese el número de teléfono del usuario %d: ", i + 1);
        scanf("%d", &users[i].telefono);

        // Verificar el número de teléfono
        if (users[i].telefono < 100000000 || users[i].telefono > 999999999) {
            printf("Error: El número de teléfono debe tener 9 dígitos.\n");
            // Reiniciar el bucle para volver a solicitar los datos del usuario
            i--;
        }
    }

    // Crear 3 libros
    Books books[3];
    for (int i = 0; i < 3; i++) {
        printf("\nIngrese el título del libro %d: ", i + 1);
        scanf("%s", books[i].title);
        printf("Ingrese el autor del libro %d: ", i + 1);
        scanf("%s", books[i].autor);
        printf("Ingrese el precio del libro %d: ", i + 1);
        scanf("%f", &books[i].price);
        printf("Ingrese el ISBN del libro %d: ", i + 1);
        scanf("%d", &books[i].ISBN);
        printf("Ingrese el stock disponible del libro %d: ", i + 1);
        scanf("%d", &books[i].stock);
    }

    // Crear 3 pedidos
    Orders orders[3];
    for (int i = 0; i < 3; i++) {
        orders[i].user = users[i];
        orders[i].books = books[i];
        printf("\nIngrese la cantidad de pedidos para el pedido %d: ", i + 1);
        scanf("%d", &orders[i].N_orders);
        printf("Ingrese el total del pedido %d: ", i + 1);
        scanf("%f", &orders[i].total);
        printf("Ingrese el código de estado de envío para el pedido %d: ", i + 1);
        scanf("%d", &orders[i].Status.StatusCode);
        printf("Ingrese la descripción del estado de envío para el pedido %d: ", i + 1);
        scanf("%s", orders[i].Status.description);
    }

    // Imprimir detalles de los pedidos
    for (int i = 0; i < 3; i++) {
        printf("\nDetalles del pedido %d:\n", i + 1);
        printf("Usuario:\n");
        print_user(orders[i].user);
        printf("Libro:\n");
        print_book(orders[i].books);
        printf("Cantidad de pedidos: %d\n", orders[i].N_orders);
        printf("Total del pedido: %.2f\n", orders[i].total);
        printf("Estado de envío (Código %d): %s\n", orders[i].Status.StatusCode, orders[i].Status.description);
    }

    return 0;
}
