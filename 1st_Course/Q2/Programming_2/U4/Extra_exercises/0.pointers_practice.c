#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    int array[10];
    int *pointer = NULL;
    array[0] = 5; 

    pointer = &array[0]; // same has pointer = array
    *(pointer)++; // array in possition 0 ++
    pointer++; //array possition 1
    *(pointer + 2) = 5; //array possition + 2 = array [3] = 5


    return 0; 
}