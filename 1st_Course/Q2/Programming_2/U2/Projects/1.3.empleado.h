#ifndef EMPLEADO_H
#define EMPLEADO_H

#include<stdio.h>
#include<stdlib.h>

typedef struct Worker{
    char  id[4];
    char name[20];
    char salary[5];
}worker_t;

void    createWorker(worker_t empleado[], int size);
void    printWorker(worker_t empleado[], int size);

#endif