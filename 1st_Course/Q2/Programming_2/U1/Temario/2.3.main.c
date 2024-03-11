#include "2.2.Lib.h"
#define MAX 5


/*MAIN FUNCTION: */

int		main()
{
	float matriz[MAX][MAX]; 
	float array[5] = {0.0};
	
	printf("Introduce los parametros de la matriz: \n");
	fillMatrix(matriz);
	
	printf("La matriz ingresada es: \n");
	printMatrix(matriz);
	sum(matriz,array);
	
	printf("el sumatorio de filas es: \n");
	Array(array);
	
	return 0; 
}
