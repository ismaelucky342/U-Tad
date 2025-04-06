#include "2.2.Lib.h"  // Include necessary header file (assuming it contains required declarations)

#define MAX 5  // Define the constant MAX with a value of 5

// Function to calculate the sum of each row in the matrix and store it in an array
void sum(float matriz[MAX][MAX], float array[5])
{
    for(int i = 0; i < MAX; i++){
        for(int j = 0; j < MAX; j++){
            array[i] += matriz[i][j];
        }
    }
}

// Function to fill a 2D matrix with user input
void fillMatrix(float matriz[MAX][MAX])
{
    for(int i = 0; i < MAX; i++){
        for(int j = 0; j < MAX; j++){
            printf("introduce el elemento %d, %d: \n", i, j);
            scanf("%f", &matriz[i][j]);
        }
    }
}

// Function to print the elements of a 1D array
void Array(float array[5])
{
    for(int i = 0; i < 5; i++){
        printf("%2f  ", array[i]);
    }
}

// Function to print the elements of a 2D matrix
void printMatrix(float matriz[MAX][MAX])
{
    for(int i = 0; i < MAX; i++){
        for(int j = 0; j < MAX; j++){
            printf("%f  ", matriz[i][j]);
        }
        printf("\n");
    }
}

// Function to clean the input buffer
int cleanBuffer()
{
    while(getchar() != '\n');
}
