# AEC3 - Comunicación RPC

## Objetivos

La práctica consiste en distribuir un objeto `FileManager` (que originalmente era monousuario) en un sistema cliente-servidor usando RPC. El cliente mantiene la misma interfaz de usuario (`main_fm.cpp`), pero ahora conecta remotamente a servidores que manejan instancias del `FileManager`. Para la máxima nota, añadí un Broker que registra servidores y balancea conexiones de clientes, permitiendo múltiples servidores en diferentes máquinas (ideal para AWS).

## Mi solución: Arquitectura y distribución

He organizado el código de manera profesional: los headers en `includes/` y los sources en `src/`. Esto evita el caos y facilita la compilación.

### Estructura de archivos:
- **`includes/`**: Headers (.h)
  - `clientManager.h`: Maneja las peticiones RPC en el servidor.
  - `filemanager.h`: Interfaz del FileManager (no modificada, como pide la práctica).
  - `utils.h`: Utilidades de red (serialización, conexiones).
- **`src/`**: Implementaciones (.cpp) y librería
  - `broker.cpp`: El Broker para registro y balanceo.
  - `client.cpp`: Vacío, no lo toqué (el cliente real usa `main_fm.cpp`).
  - `clientManager.cpp`: Implementa el RPC en el servidor.
  - `fileManagerRemoto.cpp`: Implementación remota del FileManager para el cliente.
  - `libFileManager.a`: Librería original del FileManager (enlazada en servidor).
  - `main_fm.cpp`: Interfaz de usuario (no modificada).
  - `server.cpp`: Servidor que acepta conexiones y lanza hilos.
  - `utils.cpp`: Implementación de utilidades de red.

### Cómo funciona mi implementación:
1. **Cliente**: Al crear un `FileManager`, conecta al Broker (puerto 8080) para pedir un servidor. Una vez asignado, conecta directamente al servidor y envía RPC (CREATE, LIST, READ, WRITE, DESTROY). Usa `fileManagerRemoto.cpp` para empaquetar/desempaquetar mensajes.
2. **Servidor**: Se registra con el Broker al iniciar. Acepta conexiones de clientes, crea hilos para cada uno, y maneja instancias de `FileManager` usando `clientManager.cpp`.
3. **Broker**: Escucha en puerto 8080. Servidores se registran enviando su IP y puerto. Clientes piden un servidor, y el Broker da el menos cargado (basado en conexiones activas).

Mensajes RPC: Uso `pack`/`unpack` de `utils.h` para serializar strings, ints y vectores. Comandos como "CREATE" + path, "LIST" + id, etc.

## Compilación y ejecución

Usa CMake. En la raíz del proyecto:

```bash
mkdir build
cd build
cmake ..
make
```

Esto genera: `broker`, `server`, `client`, `fileManager` (original para pruebas).

### Pruebas locales (sin Broker):
1. `./server` (puerto 8081 por defecto).
2. En otra terminal: `./client` (conecta directo, pero modifiqué para usar Broker; si falla, ajusta IPs).

### Para máxima puntuación en AWS (3 máquinas):
1. **Máquina Broker**: `./broker` (puerto 8080, IP pública).
2. **Máquinas Servidor** (2 instancias): `./server <puerto>` (ej. 8081, 8082). Se registran automáticamente con Broker.
3. **Máquina Cliente** (o cualquier): `./client`. Pide servidor al Broker, conecta y opera (lls, upload, download).

Cambia las constantes en código si necesitas IPs específicas (ej. en `fileManagerRemoto.cpp`: BROKER_HOST).

## Lo que implementé para brillar:
- **RPC completo**: Todos los métodos del FileManager (listFiles, readFile, writeFile) via red.
- **Broker con balanceo**: Registra servidores, asigna el menos cargado.
- **Hilos**: Servidor maneja múltiples clientes concurrentes.
- **Documentación**: Comentarios `/** @param */` en funciones clave.
- **Manejo de errores**: Conexiones fallidas, etc.
- **Sin modificar lo prohibido**: `main_fm.cpp`, `filemanager.h`, `libFileManager.a` intactos.




![alt text](image.png)