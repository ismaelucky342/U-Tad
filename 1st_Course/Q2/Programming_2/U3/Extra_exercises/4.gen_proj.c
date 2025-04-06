#include <stdio.h>
#include <stdlib.h>

int main() {
    // Using malloc to allocate memory for an integer
    int *ptr = (int*) malloc(sizeof(int));
    if(ptr == NULL) {
        printf("Memory allocation with malloc failed.\n");
        return 1;
    }
    *ptr = 5;
    printf("Value of ptr: %d\n", *ptr);

    // Freeing the memory allocated by malloc
    free(ptr);

    // Using calloc to allocate memory for an array of integers
    int *arr = (int*) calloc(5, sizeof(int));
    if(arr == NULL) {
        printf("Memory allocation with calloc failed.\n");
        return 1;
    }

    // Assigning values to the array
    for(int i = 0; i < 5; i++) {
        arr[i] = i;
        printf("arr[%d] = %d\n", i, arr[i]);
    }

    // Freeing the memory allocated by calloc
    free(arr);

    return 0;
}
