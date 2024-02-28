#include <stdio.h>

union iden{
    char DNI[9];
    char NIE[9];
    char pasaporte[10];
};

struct direccion{
    char calle[50];
    int numero;
    int cp;
    char provincia[25];
};

struct usuario{

    char nombre[10];
    char apellido[10];
    union iden id;

    int edad;
       float altura;
       struct direccion dire;
};

 

int main(){

    struct usuario user = { "Maxi" , "Fernandez" , "123456789" , 44 , 1.77 , 
                                { "Paseo de la Castellana" , 200 , 28004 , "Madrid" } };

    printf("[ %s , %s , %s , %d , %f , %s , %d , %d , %s ] \n",user.nombre,
             user.apellido, user.id.DNI, user.edad, user.altura, user.dire.calle, user.dire.numero, user.dire.cp, user.dire.provincia);
    return 0;

}



