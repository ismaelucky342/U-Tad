#ifndef USER_H
#define USER_H

typedef struct User {
    char Name[20];
    char apellido[20];
    int UserID;
    int age;
    char correo[30];
    int telefono;
}User;

User create_user(const char* name, const char* apellido, int userID, int age, const char* correo, int telefono);
void print_user(User user);

#endif 
