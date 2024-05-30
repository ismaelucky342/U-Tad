#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
    char date[11];
    int hour; 
    float speed; 
} DataRecord;


void readFromBinaryFile(const char *filename, int recordIndex);
int countLines(FILE *file);
void readData(FILE *file, DataRecord *records, int numRecords);
void saveToBinaryFile(const char *filename, DataRecord *records, int numRecords);

int main() 
{
    const char *inputFilename = "data.txt";
    const char *outputFilename = "data.bin";
    FILE *file = fopen(inputFilename, "r");
    if (file == NULL) {
        perror("Error al abrir el archivo de texto");
        return 1;
    }

    // Contar el número de líneas en el archivo de texto
    int numRecords = countLines(file) - 1; // Restar 1 por la línea de encabezado

    // Declarar el array de estructuras
    DataRecord *records = (DataRecord *)malloc(numRecords * sizeof(DataRecord));
    //null
    if (records == NULL) {
        perror("Error al asignar memoria");
        fclose(file);
        return 1;
    }

    // Leer los datos del archivo de texto y guardarlos en el array de estructuras
    readData(file, records, numRecords);
    fclose(file);

    // Guardar los datos en un archivo binario
    saveToBinaryFile(outputFilename, records, numRecords);

    // Leer un registro específico del archivo binario y mostrarlo
    int recordIndex = 0; // Cambia esto para leer un registro diferente
    readFromBinaryFile(outputFilename, recordIndex);

    free(records);
    return 0;
}

int countLines(FILE *file) {
    int lines = 0; 
    char ch; 
    while (!feof(file)) {
        ch = fgetc(file);
        if (ch == '\n')
            lines++; 
    }
    rewind(file); 
    return lines; 
}

void readData(FILE *file, DataRecord *records, int numRecords) {
    char line[256]; 
    fgets(line, sizeof(line), file); // Leer la línea de encabezado

    for (int i = 0; i < numRecords; i++) {
        fgets(line, sizeof(line), file);
        sscanf(line, "%[^,],%d,%f", records[i].date, &records[i].hour, &records[i].speed);
    }
}

void saveToBinaryFile(const char *filename, DataRecord *records, int numRecords) {
    FILE *file = fopen(filename, "wb");
    if (file == NULL) {
        perror("Error al abrir el archivo binario");
        exit(1);
    }
    fwrite(records, sizeof(DataRecord), numRecords, file);
    fclose(file);
}

void readFromBinaryFile(const char *filename, int recordIndex) {
    FILE *file = fopen(filename, "rb");
    if (file == NULL) {
        perror("Error al abrir el archivo binario");
        exit(1);
    }
    DataRecord record;
    fseek(file, recordIndex * sizeof(DataRecord), SEEK_SET);
    fread(&record, sizeof(DataRecord), 1, file);
    fclose(file);

    printf("Fecha: %s, Hora: %d, Velocidad: %.2f\n", record.date, record.hour, record.speed);
}