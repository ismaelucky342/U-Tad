#include<stdio.h>
#include<stdlib.h>

int main()
{
    printf("how many elements you need to stack");
    int len; 
    scanf("%d", &len);

    float* values = (float *) malloc(len*sizeof(float));// MEMORY ALLOCATION 
    int i; 

    for(i = 0; i<len; i++){
        values[i] = 5; 
    }
    printf("all ok"); 
    return 0;
}
