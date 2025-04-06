#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char frase[1000]; // Declare an array to store each line of the file
    int i = 0;
    FILE *filePointer;
    filePointer = fopen("quijote_3.txt","r");

    // Read the first line and print it.
    fgets(frase, 1000, filePointer);
    printf("First line only: %s \n", frase);

    // Return to the beginning of the file.
    rewind(filePointer);

    // Implement a while loop until EOF.
    while (!feof(filePointer)) {
        if (fgets(frase, 1000, filePointer)) {
            printf("Line %d: %s", i+1, frase); // Print each line
            i++;
        }
    }

    fclose(filePointer);
    return 0;
}
