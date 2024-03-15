#include <stdio.h>

struct User {
    char firstName[10];
    char lastName[10];
    char identification[9];
    int age;
    float height;
    char address[100];
};

int main() {

    // Initialize the structure and assign values
    struct User user = { "Maxi" , "Fernandez" , "123456789" , 44 , 1.77 , "Paseo de la Castellana 200, 28004, Madrid" };

    // Print the structure as if it were a record in a database
    printf("[ %s , %s , %s , %d , %f , %s ] \n", user.firstName, user.lastName, user.identification, user.age, user.height, user.address);

    return 0;
}
