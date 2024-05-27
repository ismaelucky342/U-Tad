#include<stdio.h> 
#include<stdlib.h>

int main()
{
    int n; 
    //user
    printf("Insert number of elements: \n"); 
    scanf("%d", &n); 

    int *numbers = (int *)malloc(n*(sizeof(int))); 
    if (numbers == NULL){
        printf("memory allocation failed"); 
        return 1; 
    }

    printf("insert %d numbers", n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &numbers[i]); 
    }
    int sum = 0; 

    for (int i = 0; i < n; i++)
    {
        sum += numbers[i]; 
    }
    printf("the sum is: %d", sum); 
    free(numbers); 

    return 0; 
}