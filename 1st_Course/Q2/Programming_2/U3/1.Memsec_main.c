#include <stdio.h>
#include <stdlib.h>

int c;  // Global variable
int d;  // Global variable

void main(int argc, char** argv) {
    int a;  // Local variable
    int b;  // Local variable
    int *ptr = (int*)malloc(sizeof(int) * 1000);  // Dynamically allocated memory

    printf("global 1   :%p \n", &c);            // Print address of global variable c
    printf("global 2   :%p \n", &d);            // Print address of global variable d
    printf("cabecera 1 :%p \n", &argc);         // Print address of function parameter argc
    printf("cabecera 2 :%p \n", &argv);         // Print address of function parameter argv
    printf("local 1    :%p \n", &a);            // Print address of local variable a
    printf("local 2    :%p \n", &b);            // Print address of local variable b
    printf("malloc     :%p \n", ptr);           // Print address of dynamically allocated memory

    // Remember to free the dynamically allocated memory to avoid memory leaks
    free(ptr);
}
