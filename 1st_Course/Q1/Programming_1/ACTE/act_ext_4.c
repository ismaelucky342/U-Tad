#include <stdio.h>

// Prototipos de las funciones
void leeFechaCorrecta(int *dia, int *mes, int *year);
int calculaNumMagico(int dia, int mes, int year);

// Función principal
int main() {
    int dia, mes, year;
    
    // Leer la fecha correcta
    leeFechaCorrecta(&dia, &mes, &year);
    
    // Mostrar la fecha de nacimiento
    printf("Tu fecha de Nacimiento es: %02d/%02d/%d\n", dia, mes, year);
    
    // Calcular y mostrar el número mágico
    int numMagico = calculaNumMagico(dia, mes, year);
    printf("El numero magico asociado a tu fecha de nacimiento es: %d\n", numMagico);
    
    return 0;
}

// Función que pide al usuario los datos de su fecha de nacimiento y los devuelve cuando todos sean correctos
void leeFechaCorrecta(int *dia, int *mes, int *year) {
    int dias_mes[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int valido = 0;
    
    while (!valido) {
        printf("Introduce tu Fecha de Nacimiento.\n");
        printf("Año: ");
        scanf("%d", year);
        
        if (*year <= 0) {
            printf("El año introducido no es correcto.\n");
            continue;
        }
        
        printf("Mes: ");
        scanf("%d", mes);
        
        if (*mes < 1 || *mes > 12) {
            printf("El mes introducido no es correcto.\n");
            continue;
        }
        
        printf("Dia: ");
        scanf("%d", dia);
        
        if (*dia < 1 || *dia > dias_mes[*mes - 1]) {
            printf("El dia del mes introducido no es correcto.\n");
            continue;
        }
        
        valido = 1;
    }
}

// Función que calcula el número mágico asociado a una fecha de nacimiento y lo devuelve como resultado
int calculaNumMagico(int dia, int mes, int year) {
    int suma = dia + mes + year;
    
    while (suma >= 10) {
        int nueva_suma = 0;
        
        while (suma > 0) {
            nueva_suma += suma % 10;
            suma /= 10;
        }
        
        suma = nueva_suma;
    }
    
    return suma;
}
