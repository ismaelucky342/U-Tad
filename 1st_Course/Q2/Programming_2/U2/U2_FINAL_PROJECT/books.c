#include "books.h"
#include <stdio.h>
#include <string.h>

Books create_book(const char* title, float price, const char* autor, int ISBN, int stock) {
    Books newBook;
    strcpy(newBook.title, title);
    newBook.price = price;
    strcpy(newBook.autor, autor);
    newBook.ISBN = ISBN;
    newBook.stock = stock;
    return newBook;
}

void print_book(Books book) {
    printf("Título: %s\n", book.title);
    printf("Autor: %s\n", book.autor);
    printf("Precio: %.2f\n", book.price);
    printf("ISBN: %d\n", book.ISBN);
    printf("Stock disponible: %d\n", book.stock);
}
