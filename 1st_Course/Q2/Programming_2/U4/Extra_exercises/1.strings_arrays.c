#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    char string[] = "hello world"; 

    //strcpy init
    char *origin = "hello world";
    char destiny [strlen(origin)+1];

    strcpy(destiny, origin);
    printf("%s \n", string); 
    printf("Origin: %s\nDestiny: %s\n", origin, destiny);
    return 0; 
}