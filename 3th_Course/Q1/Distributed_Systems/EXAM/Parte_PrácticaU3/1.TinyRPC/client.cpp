// client.cpp
#include <iostream>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int sock = socket(AF_INET, SOCK_STREAM, 0); // Crear socket para IPv4 y TCP

    sockaddr_in addr{}; // Configurar dirección del servidor
    addr.sin_family = AF_INET; // IPv4
    addr.sin_port = htons(8080); // Puerto 8080
    inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr); // Dirección IP del servidor

    connect(sock, (sockaddr*)&addr, sizeof(addr)); // Conectar al servidor

    int x = 21;
    write(sock, &x, sizeof(x)); // Enviar un entero al servidor

    int result;
    read(sock, &result, sizeof(result)); // Leer el resultado enviado por el servidor

    std::cout << "Resultado: " << result << std::endl; // Mostrar el resultado

    close(sock); // Cerrar el socket
}
