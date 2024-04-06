#include "User.h"
#include <stdio.h>
#include <string.h>

User create_user(const char* name, const char* apellido, int userID, int age, const char* correo, int telefono) {
    User newUser;
    strcpy(newUser.Name, name);
    strcpy(newUser.apellido, apellido);
    newUser.UserID = userID;
    newUser.age = age;
    strcpy(newUser.correo, correo);
    newUser.telefono = telefono;
    return newUser;
}

void print_user(User user) {
    printf("Nombre: %s %s\n", user.Name, user.apellido);
    printf("ID de usuario: %d\n", user.UserID);
    printf("Edad: %d\n", user.age);
    printf("Correo electrónico: %s\n", user.correo);
    printf("Teléfono: %d\n", user.telefono);
}
