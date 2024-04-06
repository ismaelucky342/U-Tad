#ifndef ORDERS_H
#define ORDERS_H

#include "user.h"
#include "books.h"

struct ShippingStatus {
    int StatusCode;
    char description[100];
};

typedef struct Orders {
    User user;
    Books books;
    int N_orders;
    float total;
    struct ShippingStatus Status;
}Orders;

Orders create_order(User user, Books book, int N_orders, float total, int statusCode, const char* statusDescription);
void print_order(Orders order);

#endif 
