#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int child; 
    if((child == fork()) > 0)
    {
        fprintf(stdout, "Parent process\n");
    }
    else if(child == 0)
    {
        fprintf(stdout, "Child process\n");
    }
    else
    {
        fprintf(stderr, "Fork failed\n");
        return 1;
    }
    return 0; 
}
