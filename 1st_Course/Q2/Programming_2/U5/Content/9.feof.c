#include <stdio.h>

void main () {
   FILE *fichDesc;
   char Caracter;

   fichDesc = fopen("file.txt","r");

   if(fichDesc == NULL) {
      printf("Error in opening file");
   }else{
      Caracter = fgetc(fichDesc);
      while(!feof(fichDesc)){
         printf("%c", Caracter);
         Caracter = fgetc(fichDesc);
      }
   }
    fclose(fichDesc);
}