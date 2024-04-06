#ifndef BOOKS_H
#define BOOKS_H

typedef struct Books {
    char title[50];
    float price;
    char autor[20];
    int ISBN;
    int stock;
}Books;

Books create_book(const char* title, float price, const char* autor, int ISBN, int stock);
void print_book(Books book);

#endif 
