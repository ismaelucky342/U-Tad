#include<stdio.h>
#include<stdlib.h>

int main()
{
    int *array; 
    int n, i; 

    printf("Insert array 1 starting space");
    scanf("%d", &n);

    array = malloc(n*sizeof(int));
    
    if (array == NULL) {
        printf("Error\n");
        return 1;
    }
   
    for (i = 0; i <= n; i++)
    {
        array[i] = i; 
    }
     printf("ARRAY 1");
    for (i = 0; i <= n; i++) {
        printf("%d \n", array[i]);
    }
    printf("Insert array 2 modified space: ");
    scanf("%d", &n);
    
    //reallocation
    array = (int*)realloc(array, n * sizeof(int));

    
    if (array == NULL) {
        printf("Error\n");
        return 1;
    }

    printf("Array 2:\n");
    for (i = 0; i <= n; i++) {
        printf("%d \n", array[i]);
    }

    free(array);

    return 0;
}