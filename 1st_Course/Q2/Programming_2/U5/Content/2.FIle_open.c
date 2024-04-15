#include <stdio.h>
#include <stdlib.h>

void main(){

      FILE *fd; //file descriptor
      fd = fopen("prueba.txt","r"); //intentamos abrirlo en modo lectura

      if (fd==NULL) //Comprobar si ha habido errores 
            printf("Error, el archivo no existe\n");
      else 
             printf("Error, el archivo existe\n");

}