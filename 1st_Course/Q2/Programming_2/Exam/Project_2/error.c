#include "library.h"

int     error(int err)
{
    if(err != 2 )
    {   
        printf("Error you need to insert 2 args");
        return 1; 
    }
}