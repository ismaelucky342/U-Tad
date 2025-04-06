#include <stdio.h>

struct Address {
    char street[50];
    int number;
    int postalCode;
    char province[25];
};

struct User {
    char firstName[10];
    char lastName[10];
    char identification[9];
    int age;
    float height;
    struct Address address;
};

int main() {
    // Initialize the structure and assign values
    struct User user = { "Maxi" , "Fernandez" , "123456789" , 44 , 1.77 , { "Paseo de la Castellana" , 200 , 28004 , "Madrid" } }; 

    // Print the structure as if it were a record in a database (although the last 4 values come from a structure within a structure)
    printf("[ %s , %s , %s , %d , %f , %s , %d , %d , %s ] \n",
           user.firstName, user.lastName, user.identification, user.age, user.height,
           user.address.street, user.address.number, user.address.postalCode, user.address.province);

    return 0;
}
