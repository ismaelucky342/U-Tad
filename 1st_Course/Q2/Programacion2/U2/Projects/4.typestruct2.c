#include <stdio.h>

typedef struct alumnos
{
    int ID;
    int Grade;
}student_t;

int main()

{
    student_t s[5];

    s[0].ID = 1;
    s[0].Grade = 81;
    s[1].ID = 2;
    s[1].Grade = 82;
    s[2].ID = 3;
    s[2].Grade = 83;
    s[3].ID = 4;
    s[3].Grade = 84;
    s[4].ID = 5;
    s[4].Grade = 85;

    printf("La nota promedio del alumno %d es %d. \n",s[0].ID,s[0].Grade);
    printf("La nota promedio del alumno %d es %d. \n",s[1].ID,s[1].Grade);
    printf("La nota promedio del alumno %d es %d. \n",s[2].ID,s[2].Grade);
    printf("La nota promedio del alumno %d es %d. \n",s[3].ID,s[3].Grade);
    printf("La nota promedio del alumno %d es %d. \n",s[4].ID,s[4].Grade);
    return 0;
}

