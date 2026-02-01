#include "persona.h"
#include "protocolo.h"
#include <sys/socket.h>
#include <string.h>
#include <unistd.h>
#include <iostream>
#include <vector>

void PersonaRemota::setEdad(int edad) {
    // 1. Definir buffer y variables
    
    // 2. Empaquetar: ID operación + Argumentos
    
    // 3. Enviar mensaje
    
    // 4. Recibir ACK (Bloqueante)
    
    // 5. Comprobar confirmación
}

int PersonaRemota::getEdad() {
    // 1. Definir buffer y variables
    
    // 2. Empaquetar: ID operación
    
    // 3. Enviar mensaje
    
    // 4. Recibir respuesta
    
    // 5. Desempaquetar: ACK + Datos
    
    // 6. Retornar valor o lanzar error
    return -1; 
}

void PersonaRemota::setNombre(std::string nombre) {
    // 1. Definir buffer
    
    // 2. Empaquetar: ID + Tamaño String + Datos String
    
    // 3. Enviar
    
    // 4. Recibir ACK
}

std::string PersonaRemota::getNombre() {
    // 1. Empaquetar ID
    
    // 2. Enviar
    
    // 3. Recibir Buffer
    
    // 4. Desempaquetar: ACK + Tamaño + Datos
    
    // 5. Retornar string reconstruida
    return "";
}
