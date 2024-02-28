#include <stdio.h>

typedef struct alumnos
{
    int ID;
    int Grade;
}student_t;

int main()
{
    student_t a1, a2;
    a1.ID = 1;
    a1.Grade = 85;
    a2.ID = 2;
    a2.Grade = 74;
    printf("La nota promedio del alumno %d es %d. \n",a1.ID,a1.Grade);
    printf("La nota promedio del alumno %d es %d. \n",a2.ID,a2.Grade);
    return 0;
}