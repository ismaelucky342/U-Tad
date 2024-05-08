#include<stdio.h>
#include<stdlib.h>

void printVector(int v[], int N);

int main()
{
    int N = 10; 
    int *p; 
    p = (int *)malloc(N*sizeof(int));
    /*memory allocation failed test: 
    malloc(-1) to force NULL*/
    if (p == NULL) {
        printf("Memory allocation failed.\n");
        return 1; // Terminates the program indicating failure
    }
    printf("vector with malloc is: ");
    printVector(p, N); 

    int *q; 
    q = (int *)calloc(N, sizeof(int));
    if (q == NULL) {
        printf("Memory allocation failed.\n");
        free(p); // Freeing previously allocated memory before terminating
        return 1; // Terminates the program indicating failure
    }
    printf("vector with calloc is: "); 
    printVector(q, N);

    // Freeing the dynamically allocated memory
    free(p);
    free(q);
    
    return 0; // Indicates successful completion of the program
}

void printVector(int v[], int N)
{
    int i; 
    for(i = 0; i < N; i++) // Fixed the typo: changed ',' to ';'
    {
        printf("%d \n", v[i]);
    }
}
