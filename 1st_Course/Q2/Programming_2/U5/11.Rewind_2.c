#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *filePointer; // All standard input/output functions use this pointer to access file information
    char character;

    filePointer = fopen("origin.txt", "r");  // Opening the file for reading
    if (filePointer == NULL) {               // Checking if the file opened successfully
        printf("Unable to open the file.\n");
        exit(1);
    }

    printf("File content:\n");
    character = getc(filePointer);  // Reading characters from the file
    while (!feof(filePointer)) {     // Checking for end of file
        printf("%c", character);
        character = getc(filePointer);
    }

    if (fclose(filePointer) != 0)  // Closing the file
        printf("Error in closing the file.\n");
    return 0;
}
