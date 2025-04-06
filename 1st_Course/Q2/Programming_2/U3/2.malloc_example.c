#include <stdio.h>
#include <stdlib.h>

int main()
{
    void *ptrVoid; 
    int a = 78, arr[20];
    float r = 283.91, *ptrFloat; 
    char name[30]; 

    ptrVoid = &a; 
    ptrVoid = arr; 
    ptrVoid = &arr[5];    
    ptrVoid = &r; 
    ptrFloat = malloc(sizeof(float));

    *ptrFloat = 456.78; 
    ptrVoid = ptrFloat; 
    ptrVoid = name; 
}