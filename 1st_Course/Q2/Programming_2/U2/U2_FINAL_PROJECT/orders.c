#include "orders.h"
#include <stdio.h>
#include <string.h>

Orders create_order(User user, Books book, int N_orders, float total, int statusCode, const char* statusDescription) {
    Orders newOrder;
    newOrder.user = user;
    newOrder.books = book;
    newOrder.N_orders = N_orders;
    newOrder.total = total;
    newOrder.Status.StatusCode = statusCode;
    strcpy(newOrder.Status.description, statusDescription);
    return newOrder;
}

void print_order(Orders order) {
    printf("Detalles del pedido:\n");
    printf("Usuario:\n");
    print_user(order.user);
    printf("Libro:\n");
    print_book(order.books);
    printf("Cantidad de pedidos: %d\n", order.N_orders);
    printf("Total: %.2f\n", order.total);
    printf("Estado de envío (Código %d): %s\n", order.Status.StatusCode, order.Status.description);
}
