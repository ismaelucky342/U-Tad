#include "library.h"

enum models{
    Sport = 1, Coupe = 2, Supersport = 3
};

typedef struct{
    char *name;
    enum models; 
    int  id; 
}Cars;

int main(int argc, char *argv[])
{
    int err = argc;
    error(err); 

    int number_cars = atoi(argv[1]); 
    Cars *cars  = malloc(number_cars*sizeof(Cars)); 

    if (cars = NULL)
    {
        printf("NULL");
        return 1; 
    }

    

    return 0; 
}