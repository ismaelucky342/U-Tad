#include"1.3.worker.h"
#define SIZE 3

int main()
{
    worker_t c[SIZE]; 
    createWorker(c, SIZE);
    printWorker(c, SIZE);
    return 0; 
}
