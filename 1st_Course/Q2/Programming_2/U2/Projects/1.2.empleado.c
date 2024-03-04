#include"1.3.empleado.h"
#define SIZE 3
void    createWorker(worker_t worker[], int size)
{
    int i; 
      for (i = 0; i < 3; i++)
      {
        printf("insert worker ID %d: ",i + 1);
        scanf("%s", &worker[i].id);
        printf("insert worker Name %d: ",i + 1);
        scanf("%s", &worker[i].name);
        printf("insert worker salary %d: ",i + 1);
        scanf("%s", &worker[i].salary);
        printf("\n");
      }   
}

void    printWorker(worker_t worker[], int size){
    int i;
    for (i = 0; i < 3; i++)
    {
        printf("----------Cliente------------------------------------------|\n");
        printf("| id: %s |\n", worker[i].id);
        printf("| Name: %s |\n", worker[i].name);
        printf("| Salary: %s |\n", worker[i].salary);
        printf("-----------------------------------------------------------|\n");
    }
}