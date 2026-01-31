// Servidor TCP minimo
#include <iostream>
#include <netinet/in.h>
#include <unistd.h>

int main(){
    int server_fd = socket(AF_INET, SOCK_STREAM, 0); // Crear socket para IPv4 y TCP

    sockaddr_in addr{}; // Configurar dirección del servidor
    addr.sin_family = AF_INET; // IPv4
    addr.sin_port = htons(8080); // Puerto 8080
    addr.sin_addr.s_addr = INADDR_ANY; // Escuchar en todas las interfaces

    bind(server_fd, (sockaddr*)&addr, sizeof(addr)); // Asociar socket a la dirección
    listen(server_fd, 1); // Escuchar conexiones entrantes

    std::cout << "Servidor esperando...\n"; // Mensaje de espera

    int client_fd = accept(server_fd, nullptr, nullptr); // Aceptar una conexión entrante

    int x;
    read(client_fd, &x, sizeof(x)); // Leer un entero enviado por el cliente

    int result = x * 2; // Procesar el entero (multiplicarlo por 2)

    write(client_fd, &result, sizeof(result)); // Enviar el resultado de vuelta al cliente

    close(client_fd);
    close(server_fd); // Cerrar sockets
}