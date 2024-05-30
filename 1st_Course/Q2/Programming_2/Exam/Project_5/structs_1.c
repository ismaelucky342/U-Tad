#include <stdio.h>
#include <string.h>

#define MAX_USUARIOS 3
#define MAX_LIBROS 3
#define MAX_PEDIDOS 3

//structs 
typedef struct {
    char nombre[50];
    char apellido[50];
    int id;
    char email[100];
    char telefono[20];
} Usuario;

typedef struct {
    char titulo[100];
    char autor[50];
    char ISBN[20];
    float precio;
    int stock;
} Libro;

typedef struct {
    int id_usuario;
    int ISBN_libro;
    int cantidad;
    float total;
    char estado[20];
} Pedido;

//Prototype area
Usuario crearUsuario(char nombre[], char apellido[], int id, char email[], char telefono[]);
Libro crearLibro(char titulo[], char autor[], char ISBN[], float precio, int stock);
Pedido crearPedido(int id_usuario, int ISBN_libro, int cantidad, float total, char estado[]);
void imprimirUsuario(Usuario usuario);
void imprimirLibro(Libro libro);
void imprimirPedido(Pedido pedido);

int main() {
//users 
    Usuario usuarios[MAX_USUARIOS] = {
        crearUsuario("Juan", "Perez", 1, "juan@example.com", "123-456-7890"),
        crearUsuario("Maria", "Garcia", 2, "maria@example.com", "987-654-3210"),
        crearUsuario("Carlos", "Lopez", 3, "carlos@example.com", "555-555-5555")
    };
    //books

    Libro libros[MAX_LIBROS] = {
        crearLibro("El misterio del tesoro desaparecido", "Geronimo Stilton", "9788499082478", 15.99, 10),
        crearLibro("Harry Potter y la piedra filosofal", "J.K. Rowling", "9788498382676", 12.50, 15),
        crearLibro("Los Juegos del Hambre", "Suzanne Collins", "9788427202139", 9.75, 20)
    };
    //orders
    Pedido pedidos[MAX_PEDIDOS] = {
        crearPedido(usuarios[0].id, libros[0].ISBN, 2, 31.98, "Enviado"),
        crearPedido(usuarios[1].id, libros[1].ISBN, 1, 12.50, "En proceso"),
        crearPedido(usuarios[2].id, libros[2].ISBN, 3, 29.25, "Pendiente")
    };

    //disUsers
    printf("=== Usuarios ===\n");
    for (int i = 0; i < MAX_USUARIOS; i++) {
        imprimirUsuario(usuarios[i]);
    }

    // ImpresiÃ³n de libros
    printf("\n=== Libros ===\n");
    for (int i = 0; i < MAX_LIBROS; i++) {
        imprimirLibro(libros[i]);
    }

    // ImpresiÃ³n de pedidos
    printf("\n=== Pedidos ===\n");
    for (int i = 0; i < MAX_PEDIDOS; i++) {
        imprimirPedido(pedidos[i]);
    }

    return 0;
}

// ImplementaciÃ³n de funciones

// FunciÃ³n para crear un usuario
Usuario crearUsuario(char nombre[], char apellido[], int id, char email[], char telefono[]) {
    Usuario usuario;
    strcpy(usuario.nombre, nombre);
    strcpy(usuario.apellido, apellido);
    usuario.id = id;
    strcpy(usuario.email, email);
    strcpy(usuario.telefono, telefono);
    return usuario;
}

// FunciÃ³n para crear un libro
Libro crearLibro(char titulo[], char autor[], char ISBN[], float precio, int stock) {
    Libro libro;
    strcpy(libro.titulo, titulo);
    strcpy(libro.autor, autor);
    strcpy(libro.ISBN, ISBN);
    libro.precio = precio;
    libro.stock = stock;
    return libro;
}

// FunciÃ³n para crear un pedido
Pedido crearPedido(int id_usuario, int ISBN_libro, int cantidad, float total, char estado[]) {
    Pedido pedido;
    pedido.id_usuario = id_usuario;
    pedido.ISBN_libro = ISBN_libro;
    pedido.cantidad = cantidad;
    pedido.total = total;
    strcpy(pedido.estado, estado);
    return pedido;
}

// FunciÃ³n para imprimir un usuario
void imprimirUsuario(Usuario usuario) {
    printf("Nombre: %s %s\n", usuario.nombre, usuario.apellido);
    printf("ID: %d\n", usuario.id);
    printf("Email: %s\n", usuario.email);
    printf("TelÃ©fono: %s\n", usuario.telefono);
    printf("\n");
}

// FunciÃ³n para imprimir un libro
void imprimirLibro(Libro libro) {
    printf("TÃ­tulo: %s\n", libro.titulo);
    printf("Autor: %s\n", libro.autor);
    printf("ISBN: %s\n", libro.ISBN);
    printf("Precio: %.2f\n", libro.precio);
    printf("Stock: %d\n", libro.stock);
    printf("\n");
}

// FunciÃ³n para imprimir un pedido
void imprimirPedido(Pedido pedido) {
    printf("ID Usuario: %d\n", pedido.id_usuario);
    printf("ISBN Libro: %d\n", pedido.ISBN_libro);
    printf("Cantidad: %d\n", pedido.cantidad);
    printf("Total: %.2f\n", pedido.total);
    printf("Estado: %s\n", pedido.estado);
    printf("\n");
}