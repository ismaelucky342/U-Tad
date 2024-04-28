#include <stdio.h>
#include <stdlib.h>
#include <string.h>

size_t getFileSize(FILE* file);

int main(){
    char* strInFile=NULL;

    size_t strLength=0;
     FILE* file=NULL;
     file=fopen("filename.txt","r+");
     strLength=getFileSize(file);
     strInFile=(char*)malloc(sizeof(char)*(strLength+1));
    fread(strInFile,strLength,1,file);
    strInFile[strLength]='\0';
    fclose(file);
    printf("Tamanio del fichero: %zu bytes...\n",strLength);
    return 0;

}

 

size_t getFileSize(FILE* file){
    size_t size=0;
    size_t posOrigin=0;
     posOrigin = ftell(file);
    fseek(file, 0L, SEEK_END);
     size = ftell(file);
    fseek(file,posOrigin, SEEK_END);
    return size;
}