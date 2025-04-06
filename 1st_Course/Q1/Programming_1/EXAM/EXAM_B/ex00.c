#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NUM_PREMIOS 12
#define NUM_TERMINACIONES 10

int leernumero(int premios[], int elementos);
int calcularTerminacion(int* terminaciones,int premios[], int elementos);
int maxnum(int premios[], int elementos);
int terminacionP(int* terminaciones, int elementos);

int main()
{
	int i, j;
	int numpremios[NUM_PREMIOS];
	int terminaciones[NUM_TERMINACIONES];
	int maxnum = 0;

	printf("Ingrese los numeros premiados en los ultimos 12 años: \n");
	leernumero(numpremios, NUM_PREMIOS);

	printf("los numeros almacenados son: \n");
	for(i = 0; i < NUM_PREMIOS; i++)
	{
		printf("numero %d: %d \n", i+1, numpremios[i]);
	}
	return 0;
}

int leernumero(int premios[], int elementos)
{
	int aux;
	for (int i = 0; i < elementos; i++)
	{
		printf("Introduzca valor %d: \n", i + 1);
		aux = 0;
		while (aux != 1 || premios[i] >= 90000 || premios[i] <= 0)
		{
			aux = scanf("%d", &premios[i]); 
			while (getchar() != '\n'); // Limpiar el buffer de entrada
			
			if(premios[i] > 90000 || premios[i] <= 0)
			{
				printf("Introduzca un valor correcto en el rango de 1 a 90000\n");
			}
			else if (aux != 1)
			{
				printf("Valor no valido\n");
			}
		}
	}
	return 0;
}

int calcularTerminacion(int* terminaciones,int premios[], int elementos)
{
	int aux; 

	for (int i = 0; i < NUM_PREMIOS; i++)
	{
		aux = premios[i] % 10; 
		terminaciones[aux]++; 
	}
	return 0; 
}

int maxnum(int premios[], int elementos)
{
	int max; 

	max = premios[0]; 
	for(int i = 0; i < elementos; i++)
	{
		if(premios[i] > max)
			max = premios[i]; 
	}
	return max; 
}

int terminacionP(int* terminaciones, int elementos)
{
	int pop, elm; 

	elm = terminaciones[0]; 
	for(int i = 0; i < elementos; i++)
	{
		if (terminaciones[i] > elm)
		{
			elm = terminaciones[i]; 
			pop = i; 
		}
	}
	return pop; 
}
