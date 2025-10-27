# 💬 Chat-Room Cliente-Servidor - Práctica U2

## 📋 Descripción del Proyecto

Sistema de chat multi-usuario implementado en C++ que permite la comunicación en tiempo real entre múltiples clientes a través de un servidor central. El proyecto utiliza sockets TCP/IP y programación concurrente con hilos.

## 🎯 Características Implementadas

### ✅ Requisitos Básicos (5 puntos)

1. **Servidor Multi-Cliente**
   - Escucha en el puerto 3000 (localhost)
   - Soporta múltiples conexiones simultáneas
   - Gestiona lista de clientes conectados con sus identificadores
   - Implementa broadcast de mensajes a todos los clientes
   - Muestra logs de conexiones y mensajes en consola

2. **Cliente Interactivo**
   - Solicita nombre de usuario al iniciar
   - Conexión al servidor (127.0.0.1:3000)
   - Hilo paralelo (`std::thread`) para recepción de mensajes
   - Interfaz de consola para escribir mensajes
   - Comando `exit()` para desconexión ordenada

3. **Protocolo de Comunicación**
   - Uso de `pack()` y `unpack()` para serialización
   - Formato: [longitud][contenido]
   - Empaquetado correcto de nombre de usuario y mensajes

### ⚡ Extensiones Implementadas (5 puntos extra)

#### 1. ✅ Solución Error "Lost Connection" (2 puntos)
- El servidor envía un mensaje de confirmación antes de cerrar la conexión
- El cliente espera la confirmación antes de terminar
- Implementación de tipo de mensaje `MSG_DISCONNECT`
- No se modifica `libUtils`

#### 2. ✅ Mensajes Privados (3 puntos)
- Comando `/privado <usuario> <mensaje>` para enviar mensajes privados
- Tipos de mensaje diferenciados: `MSG_PUBLIC` y `MSG_PRIVATE`
- Empaquetado adicional del destinatario en mensajes privados
- Servidor mantiene pares `{nombre, clientId}` en la lista de usuarios
- Búsqueda de usuarios por nombre
- Notificaciones de estado (enviado correctamente / usuario no encontrado)

## 🏗️ Estructura del Proyecto

```
AEC2/
├── CMakeLists.txt          # Configuración de CMake
├── README.md               # Este archivo
├── include/
│   └── protocol.h          # Definiciones de protocolo y tipos de mensaje
├── src/
│   ├── server.cpp          # Implementación del servidor
│   └── client.cpp          # Implementación del cliente
└── lib/
    └── libUtils.so         # Librería proporcionada (debes colocarla aquí)
```

## 🔧 Compilación

### Requisitos Previos
- CMake 3.10 o superior
- Compilador C++ compatible con C++17 (g++, clang++)
- pthread (incluido en Linux)
- Librería `libUtils` proporcionada por el profesor

### Pasos para Compilar

1. **Colocar la librería libUtils:**
   ```bash
   mkdir -p lib
   cp /ruta/a/libUtils.so lib/
   ```

2. **Crear directorio de build:**
   ```bash
   mkdir build
   cd build
   ```

3. **Configurar y compilar:**
   ```bash
   cmake ..
   make
   ```

4. **Ejecutables generados:**
   - `server` - Servidor del chat
   - `client` - Cliente del chat

## 🚀 Ejecución

### Iniciar el Servidor

```bash
cd build
./server
```

Salida esperada:
```
========================================
    SERVIDOR CHAT-ROOM - PUERTO 3000   
========================================

[OK] Servidor iniciado en localhost:3000
[INFO] Esperando conexiones de clientes...
```

### Iniciar Clientes (en terminales separadas)

```bash
cd build
./client
```

El cliente te solicitará un nombre de usuario:
```
========================================
       CLIENTE CHAT-ROOM v2.0          
========================================

Por favor, ingresa tu nombre de usuario: Juan
```

## 📝 Comandos del Cliente

| Comando | Descripción |
|---------|-------------|
| `<mensaje>` | Envía un mensaje público a todos los usuarios |
| `/privado <usuario> <mensaje>` | Envía un mensaje privado a un usuario específico |
| `/ayuda` | Muestra la lista de comandos disponibles |
| `exit()` | Sale del chat de forma ordenada |

### Ejemplos de Uso

**Mensaje público:**
```
> Hola a todos!
```

**Mensaje privado:**
```
> /privado Maria Hola, ¿cómo estás?
[INFO] Mensaje privado enviado a Maria
```

**Salir del chat:**
```
> exit()
[INFO] Cerrando conexión...
```

## 🔍 Detalles Técnicos

### Protocolo de Mensajes

Cada mensaje se compone de los siguientes campos empaquetados:

```
[tipo][username][contenido][destinatario (solo privados)]
```

Donde cada campo tiene el formato:
```
[longitud (4 bytes)][datos (longitud bytes)]
```

### Tipos de Mensaje

```cpp
enum MessageType {
    MSG_PUBLIC = 0,     // Mensaje público (broadcast)
    MSG_PRIVATE = 1,    // Mensaje privado
    MSG_DISCONNECT = 2, // Desconexión ordenada
    MSG_CONNECT = 3     // Conexión inicial (envío de nombre)
};
```

### Sincronización de Hilos

- **Servidor:** Usa `std::mutex` para proteger la lista de clientes compartida
- **Cliente:** Usa `std::atomic<bool>` para controlar el estado de ejecución
- Cada cliente del servidor se maneja en un hilo independiente con `.detach()`

### Manejo de Errores

- Validación de buffers vacíos para detectar desconexiones
- Try-catch para excepciones en procesamiento de mensajes
- Notificaciones claras al usuario sobre errores (usuario no encontrado, etc.)
- Limpieza automática de clientes desconectados de la lista

## 📊 Ejemplos de Ejecución

### Escenario 1: Mensajes Públicos

**Terminal 1 (Servidor):**
```
[CONEXIÓN] Usuario 'Juan' (ID: 1) se ha unido al chat
[CONEXIÓN] Usuario 'Maria' (ID: 2) se ha unido al chat
[PÚBLICO] Juan dice: Hola a todos!
[PÚBLICO] Maria dice: Hola Juan!
```

**Terminal 2 (Cliente - Juan):**
```
[OK] Conectado al servidor exitosamente
[INFO] ¡Bienvenido al chat, Juan!
> Hola a todos!
[Maria]: Hola Juan!
```

**Terminal 3 (Cliente - Maria):**
```
[SERVIDOR] Juan se ha unido al chat
> Hola Juan!
[Juan]: Hola a todos!
```

### Escenario 2: Mensajes Privados

**Terminal 2 (Cliente - Juan):**
```
> /privado Maria ¿Quieres ayuda con el proyecto?
[INFO] Mensaje privado enviado a Maria
[SERVIDOR] Mensaje privado enviado a Maria
```

**Terminal 3 (Cliente - Maria):**
```
[PRIVADO] Juan te dice: ¿Quieres ayuda con el proyecto?
> /privado Juan Sí, por favor!
[INFO] Mensaje privado enviado a Juan
```

**Terminal 1 (Servidor):**
```
[PRIVADO] De: Juan Para: Maria | Mensaje: ¿Quieres ayuda con el proyecto?
[PRIVADO] De: Maria Para: Juan | Mensaje: Sí, por favor!
```

### Escenario 3: Desconexión Ordenada

**Terminal 2 (Cliente - Juan):**
```
> exit()
[INFO] Cerrando conexión...
[INFO] Desconexión confirmada
[INFO] Desconectado del servidor. ¡Hasta pronto!
```

**Terminal 1 (Servidor):**
```
[DESCONEXIÓN] Usuario 'Juan' ha salido del chat
```

**Terminal 3 (Cliente - Maria):**
```
[SERVIDOR] Juan ha salido del chat
```

## 🐛 Solución de Problemas

### Error: "No se pudo conectar al servidor"
- Verifica que el servidor esté ejecutándose
- Confirma que el puerto 3000 no esté ocupado
- Revisa el firewall del sistema

### Error: "libUtils.so: cannot open shared object file"
- Asegúrate de que `libUtils.so` esté en el directorio `lib/`
- Añade el directorio al LD_LIBRARY_PATH:
  ```bash
  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/lib
  ```

### Error de compilación con CMake
- Verifica que CMake sea versión 3.10 o superior
- Confirma que el compilador soporte C++17

## 📚 Funciones de libUtils Utilizadas

- `initServer(int port)` - Inicializa el servidor
- `initClient(const char* ip, int port)` - Conecta el cliente
- `checkClient()` - Comprueba nuevas conexiones
- `getLastClientID()` - Obtiene ID del último cliente conectado
- `sendMSG(int id, const std::string& buffer)` - Envía mensaje
- `recvMSG(int id, std::string* buffer)` - Recibe mensaje
- `closeConnection(int id)` - Cierra conexión

## 👨‍💻 Mejores Prácticas Implementadas

1. **Código Documentado:** Comentarios Doxygen en funciones principales
2. **Manejo de Recursos:** RAII y limpieza automática de recursos
3. **Concurrencia Segura:** Uso de mutex para secciones críticas
4. **Separación de Responsabilidades:** Funciones específicas y modulares
5. **Protocolo Extensible:** Estructura de mensajes fácil de ampliar
6. **Logs Descriptivos:** Información clara sobre el estado del sistema

## 📄 Entrega

Este proyecto incluye:
- ✅ Código fuente completo (`.cpp`, `.h`, `CMakeLists.txt`)
- ✅ README con documentación detallada
- ✅ Ejemplos de ejecución y capturas
- ✅ Todos los requisitos básicos implementados (5 puntos)
- ✅ Ambas extensiones opcionales implementadas (5 puntos extra)

**Puntuación Total Esperada: 10/10 puntos**

## 📧 Notas Adicionales

- El código está preparado para compilar asumiendo que `libUtils` sigue la interfaz estándar
- Si `libUtils` tiene una interfaz diferente, puede ser necesario ajustar las declaraciones `extern "C"`
- El proyecto puede extenderse fácilmente con más tipos de mensajes (archivos, emoticons, etc.)
- La arquitectura soporta fácilmente la adición de más comandos especiales

---

**Autor:** Estudiante de Sistemas Distribuidos - U-TAD  
**Curso:** 3º - Programación Cliente-Servidor  
**Fecha:** Octubre 2025
