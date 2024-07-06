/*Implemente un programa en C que simule el análisis de temperaturas registradas en los últimos 30 días en una ciudad. El programa debe realizar las siguientes tareas:

Leer 30 temperaturas: El usuario debe introducir 30 números enteros que representen las temperaturas registradas en los últimos 30 días.

Mostrar las temperaturas registradas: Una vez leídas las temperaturas, el programa debe mostrarlas al usuario.

Calcular las frecuencias de las temperaturas: El programa debe calcular la cantidad de veces que se repiten las temperaturas enteras dentro del rango de -10 a 50 grados Celsius.

Mostrar las frecuencias: Mostrar la cantidad de veces que se repite cada temperatura dentro del rango mencionado.

Determinar la temperatura más frecuente: Identificar cuál es la temperatura que aparece más frecuentemente entre las temperaturas registradas.

Determinar la temperatura más alta: Encontrar la temperatura más alta registrada en los últimos 30 días.*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NUM_DIAS 30
#define TEMP_MAX 50
#define TEMP_MIN -10

void leeTemperaturas(int temperaturas[], int num_dias);
void calculaFrecuencias(int *frecuencias, int *temperaturas, int num_dias);
int temperaturaMasFrecuente(int frecuencias[], int temp_min, int temp_max);
int temperaturaMasAlta(int temperaturas[], int num_dias);

int main(int argc, char** argv)
{
    int i;
    int temperaturas[NUM_DIAS];
    int tempMasAlta = 0;
    int frecuencias[TEMP_MAX - TEMP_MIN + 1] = {0};

    printf("Introduce 30 temperaturas entre %d y %d. Estas deben ser las registradas en los últimos 30 días\n", TEMP_MIN, TEMP_MAX);
    leeTemperaturas(temperaturas, NUM_DIAS);

    printf("\n==> Las temperaturas registradas en los últimos 30 días son:\n");
    
    for (i = 0; i < NUM_DIAS; i++)
    {
        printf("%d ", temperaturas[i]);
    }
    printf("\n");

    calculaFrecuencias(frecuencias, temperaturas, NUM_DIAS);

    for (i = TEMP_MIN; i <= TEMP_MAX; i++)
    {
        if (frecuencias[i - TEMP_MIN] > 0) {
            printf("Temperaturas de %d grados: %d\n", i, frecuencias[i - TEMP_MIN]);
        }
    }

    int tempFrecuente = temperaturaMasFrecuente(frecuencias, TEMP_MIN, TEMP_MAX);
    printf("==> La temperatura más frecuente en estos días ha sido de: %d grados\n", tempFrecuente);

    tempMasAlta = temperaturaMasAlta(temperaturas, NUM_DIAS);
    printf("\n==> La temperatura más alta registrada en estos días ha sido de: %d grados\n", tempMasAlta);

    return 0;
}


void leeTemperaturas(int temperaturas[], int num_dias)
{
    int res;

    for (int i = 0; i < num_dias; i++)
    {
        printf("Introduce la temperatura %d: ", i + 1);
        res = 0;

        // Verificar si la entrada es válida y está dentro del rango
        while (res != 1 || temperaturas[i] < TEMP_MIN || temperaturas[i] > TEMP_MAX)
        {
            res = scanf("%d", &temperaturas[i]);
            while (getchar() != '\n'); 
            if (res != 1) {
                printf("El dato no es válido. Inténtalo de nuevo.\n");
            } else if (temperaturas[i] < TEMP_MIN || temperaturas[i] > TEMP_MAX) {
                printf("Incorrecto, temperatura no válida. Debe estar entre %d y %d.\n", TEMP_MIN, TEMP_MAX);
            }
            // Pedir nuevamente la temperatura
        }
    }
}

void calculaFrecuencias(int frecuencias[], int temperaturas[], int num_dias)
{
    for (int i = 0; i < num_dias; i++)
    {
        frecuencias[temperaturas[i] - TEMP_MIN]++;
    }
}

int temperaturaMasFrecuente(int frecuencias[], int temp_min, int temp_max)
{
    int maxFrecuencia = frecuencias[0];
    int tempFrecuente = temp_min;

    for (int i = 1; i <= (temp_max - temp_min); i++)
    {
        if (frecuencias[i] > maxFrecuencia)
        {
            maxFrecuencia = frecuencias[i];
            tempFrecuente = i + temp_min;
        }
    }
    return tempFrecuente;
}

int temperaturaMasAlta(int temperaturas[], int num_dias)
{
    int maximo = temperaturas[0];

    for (int i = 1; i < num_dias; i++)
    {
        if (temperaturas[i] > maximo)
        {
            maximo = temperaturas[i];
        }
    }
    return maximo;
}
