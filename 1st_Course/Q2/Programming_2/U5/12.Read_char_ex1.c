#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char *phrase;
    char c;
    int i = 0;
    FILE *filePointer;
    filePointer = fopen("quijote.txt","r");

    // Read the first character and print it.
    c = getc(filePointer);
    printf("First character: %c \n", c);

    // Return to the beginning of the file.
    rewind(filePointer);

    // Implement a while loop until EOF.
    while (!feof(filePointer)) {
        c = getc(filePointer);
        *(phrase + i) = c;
        i++;
    }

    printf("%s", phrase);
    fclose(filePointer);
    return 0;
}
