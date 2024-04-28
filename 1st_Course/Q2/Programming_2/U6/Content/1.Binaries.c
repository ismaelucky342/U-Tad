#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum calle_t{
     AVENIDA = 1, CALLE = 2 , PASEO = 3 , BOULEVARD = 4 , PLAZA = 5 
}calle_t;

typedef struct direccion{
    calle_t tipo_calle;
    char nombre_calle[50];
    int num_calle;
    int cod_postal;
    char provincia[20];
}direccion_t;

int main(){
    // creamos la estructura y asignamos valores...
    direccion_t dir = { 1,"Main Street",200,28000,"Madrid" };

    // imprimimos el contenido por stdout...
    printf("La direccion es: %d, %s %d CP%d %s \n",dir.tipo_calle, dir.nombre_calle, dir.num_calle, dir.cod_postal, dir.provincia);

    // escribimos el contenido a un fichero de texto
     FILE * f_texto;
     f_texto = fopen("estructura_texto.csv","w");
    fprintf(f_texto,"%d,%s,%d,%d,%s\n",dir.tipo_calle, dir.nombre_calle, dir.num_calle, dir.cod_postal, dir.provincia);

    // escribimos el contenido a un fichero binario
     FILE * f_binario;
     f_binario = fopen("estructura_binario.bin","wb");
    fwrite(&dir,sizeof(direccion_t),1,f_binario);
    fclose(f_texto);
    fclose(f_binario);
    return 0;
}