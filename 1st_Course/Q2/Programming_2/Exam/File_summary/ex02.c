#include <stdio.h>
#include <ctype.h>

int main() {
    FILE *file = fopen("texto.txt", "r");
    if (file == NULL) {
        printf("No se pudo abrir el archivo\n");
        return 1;
    }

    int ch;
    int inWord = 0;
    int wordCount = 0;

    while ((ch = fgetc(file)) != EOF) {
        if (isspace(ch)) {
            if (inWord) {
                inWord = 0;
            }
        } else {
            if (!inWord) {
                inWord = 1;
                wordCount++;
            }
        }
    }

    fclose(file);
    printf("Número de palabras: %d\n", wordCount);
    return 0;
}
