# AEC2 - SISTEMAS DISTRIBUIDOS

## Desarrollo y objetivos

Este es mi implementación de un sistema de chat en tiempo real usando sockets TCP/IP en C++. Básicamente, construí un servidor que puede manejar varios clientes conectándose al mismo tiempo y hablando entre ellos, ya sea en un chat grupal o enviándose mensajes privados.Sistema de chat en tiempo real implementado en C++ utilizando sockets TCP/IP. El proyecto permite que múltiples usuarios se conecten simultáneamente a un servidor central y se comuniquen entre ellos mediante mensajes públicos o privados.

Lo que más me costó fue entender cómo hacer que los hilos no se pisaran unos a otros cuando varios clientes intentan hacer cosas al mismo tiempo. He desarrollado este sistema desde las plantillas proporcionadas, completando las funciones de serialización (pack/unpack) y la lógica de comunicación tanto en el cliente como en el servidor. El mayor desafío fue coordinar los hilos de recepción y envío sin que se bloqueasen mutuamente.


## Estructura del Proyecto

``````

AEC2/AEC2/

├── CMakeLists.txt           
├── README.md             
├── include/├── include/
│   └── protocol.h          # Definición del protocolo
├── src/├── src/
│   ├── server.cpp          # El servidor      
│   └── client.cpp          # El cliente
└── lib/
    └── libUtils.so         # Librería de sockets que nos dieron

``````



## Desarrollo de los Componentes

### protocol.h

Aquí definí la librería común que usan cliente y servidor para entenderse. Básicamente:Defino la estructura del protocolo de comunicación que comparten cliente y servidor, así como todas los includes:

- Un enum MessageType con los 4 tipos de mensaje que puede haber (público, privado, conectar, desconectar)- **MessageType**: Enum con 4 tipos de mensaje (PUBLIC, PRIVATE, DISCONNECT, CONNECT)

- Una estructura Message que agrupa todo lo que lleva un mensaje (tipo, quien lo manda, el contenido, y si es privado, a quién va)- **Message**: Estructura que encapsula tipo, usuario, contenido y destinatario (para privados)

### server.cpp

**Acepta conexiones**: Se queda escuchando en el puerto 3000 esperando clientes. Cuando llega uno, crea un hilo nuevo solo para él. Así puede atender a varios a la vez sin que uno bloquee a los demás.

**Guarda los usuarios**: Mantiene una lista con todos los clientes conectados. Guarda su ID (que da el socket) y su nombre de usuario. Esta lista está protegida con un mutex porque varios hilos la tocan a la vez.

**Reenvía mensajes públicos**: Cuando alguien manda un mensaje público, el servidor lo reenvía a todos MENOS al que lo envió (para no verlo duplicado).

**Gestiona mensajes privados**: Tiene una función findClientByUsername() que busca en la lista al destinatario. Si lo encuentra, solo le envía el mensaje a ese cliente. Si no, le dice al remitente que ese usuario no existe.

**Cierra conexiones bien**: Cuando alguien escribe exit(), no solo cierra la conexión sin más. Primero avisa a todos, luego le manda un "ok" al que se va, y después cierra todo limpiamente. Así no hay errores de "lost connection".

La función handleClient() es donde pasa todo el trafico: recibe mensajes sin parar, los desempaqueta, y hace lo que toque según el tipo.La función handleClient() es el corazón: recibe mensajes en bucle, los desempaqueta campo por campo, y según el tipo ejecuta la acción correspondiente.


### client.cpp

Esta es la interfaz con la que interactúa el usuario. Lo interesante aquí:El cliente gestiona la interacción con el usuario y la comunicación con el servidor:

**Dos hilos trabajando juntos**:**Arquitectura de dos hilos**: 

- El hilo principal está pendiente de lo que escribes y lo envía- Hilo principal: captura entrada del usuario y envía mensajes

- Otro hilo (receiveMessages) está escuchando lo que llega del servidor- Hilo receptor (receiveMessages): recibe mensajes del servidor en segundo plano

¿Por qué dos hilos? Porque recvMSG() se queda esperando hasta que llegue algo. Si lo hiciera todo en un hilo, mientras esperas mensajes no podrías escribir.

**Coordinación con atomic**: Uso std::atomic<bool> isRunning para que ambos hilos sepan cuándo tienen que parar. Cuando uno detecta que hay que cerrar (porque escribiste exit() o se cayó la conexión), pone isRunning = false y el otro lo ve y también termina.

**Comandos especiales**: Implementé processCommand() que detecta /privado y /ayuda. Para mensajes privados, parsea el input, extrae destinatario y mensaje, y construye un Message de tipo MSG_PRIVATE.

**Serialización**: Las funciones pack() y unpack() son clave. Pack mete 4 bytes al principio diciendo cuánto mide lo que viene después. Unpack lee esos 4 bytes, ya sabe cuántos bytes tiene que leer, y los extrae. Sin esto, no sabríamos dónde empieza y termina cada dato.### CMakeLists.txt



Configuración de compilación:

- Define dos ejecutables independientes (server y client)

La configuración para compilar. Nada del otro mundo:- Enlaza con libUtils y pthread (necesaria para std::thread)

- Crea dos ejecutables (server y client)- Establece C++17 como estándar (requerido para algunas características)

- Los enlaza con libUtils (para los sockets) y pthread (para los hilos)



## Formato:

Cada mensaje va con este formato:```

[tipo][username][contenido][destinatario (solo en MSG_PRIVATE)]

``````

[tipo][usuario][contenido][destinatario (solo en privados)]

```Donde cada campo se empaqueta como: `[4 bytes longitud][N bytes datos]`



Cada campo se empaqueta así: `[4 bytes con la longitud][los datos]`**Flujo de conexión**:

1. Cliente se conecta con initClient()

**Cuando te conectas**:2. Cliente envía MSG_CONNECT con su username

1. Cliente llama a initClient()3. Servidor registra el par {clientId, username}

2. Manda MSG_CONNECT con tu nombre4. Servidor notifica a todos: "X se ha unido al chat"

3. Servidor te añade a su lista

4. Avisa a todos que te uniste**Flujo de mensaje público**:

1. Usuario escribe mensaje y pulsa Enter

**Mensaje público**:2. Cliente empaqueta MSG_PUBLIC con username y contenido

1. Escribes algo y das Enter3. Servidor recibe, desempaqueta, y hace broadcast a todos menos al remitente

2. Cliente hace pack de MSG_PUBLIC con tu nombre y texto

3. Servidor lo recibe y hace broadcast a todos menos a ti**Flujo de mensaje privado**:

1. Usuario escribe: `/privado Maria Hola`

**Mensaje privado**:2. Cliente parsea, extrae destinatario y mensaje

1. Escribes: `/privado Maria Hola`3. Empaqueta MSG_PRIVATE con campo adicional recipient

2. Cliente separa el nombre y el mensaje4. Servidor busca clientId de "Maria"

3. Empaqueta MSG_PRIVATE con un campo extra (destinatario)5. Si existe, reenvía solo a ella. Si no, notifica error al remitente

4. Servidor busca a "Maria"

5. Si existe, se lo manda solo a ella. Si no, te avisa del error**Flujo de desconexión**:

1. Usuario escribe `exit()`

**Cuando te vas**:2. Cliente envía MSG_DISCONNECT

1. Escribes `exit()`3. Servidor notifica a todos, envía confirmación, cierra conexión

2. Cliente manda MSG_DISCONNECT4. Cliente recibe confirmación, cierra limpiamente sin errores

3. Servidor avisa a todos, te manda "ok", y cierra

4. Recibes el ok y cierras limpiamente sin errores## Compilacion y Ejecucion



## Compilar y Ejecutar



### Compilar```bash

# Colocar libUtils.so en lib/

```bashmkdir -p lib

# Poner libUtils.so en lib/cp /ruta/a/libUtils.so lib/

mkdir -p lib

cp /ruta/a/libUtils.so lib/# Configurar path (si es necesario)

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/lib

# Si hace falta, configurar la ruta

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/lib# Crear directorio de build

mkdir build && cd build

# Compilar

mkdir build && cd build# Configurar y compilar

cmake ..cmake ..

make -j$(nproc)make

```

### Test 1: Varios Clientes Conectándose

## Pruebas Realizadas

**Qué probé**: Que el servidor acepta y registra bien a varios clientes a la vez.

### Test 1: Conexión de Múltiples Clientes

**Cómo**: Arranqué el servidor y conecté 3 clientes (Juan, Maria, Pedro).

**Descripción**: Verificar que el servidor acepta y registra correctamente varios clientes conectándose simultáneamente.

**Qué debería pasar**: Cada uno ve cuando los otros se conectan. El servidor muestra los logs con IDs y nombres.

**Procedimiento**: Iniciar el servidor y conectar 3 clientes con nombres diferentes (Juan, Maria, Pedro).

*(Captura aquí)*

**Resultado esperado**: Cada cliente recibe notificaciones de cuando los otros se conectan. El servidor muestra logs con los IDs y nombres de usuario.

---

*(Insertar captura aquí)*

### Test 2: Mensajes Públicos

---

**Qué probé**: Que los mensajes llegan a todos menos al que los mandó.

### Test 2: Mensajes Públicos (Broadcast)

**Cómo**: Un cliente manda un mensaje y miro si aparece en los otros.

**Descripción**: Comprobar que los mensajes públicos llegan a todos los clientes excepto al remitente.

**Qué debería pasar**: Todos lo ven con formato `[Usuario]: mensaje` excepto quien lo escribió.

**Procedimiento**: Un cliente envía un mensaje. Verificar que aparece en las terminales de los otros clientes pero no en la propia.

*(Captura aquí)*

**Resultado esperado**: Todos los clientes (excepto el remitente) ven el mensaje con formato `[Usuario]: mensaje`.

---

*(Insertar captura aquí)*

### Test 3: Mensajes Privados

---

**Qué probé**: Que los privados solo los ve el destinatario.

### Test 3: Mensajes Privados

**Cómo**: Juan escribe `/privado Maria Hola`. Verifico que solo Maria lo recibe.

**Descripción**: Verificar la funcionalidad de mensajes privados entre usuarios específicos.

**Qué debería pasar**: Maria ve `[PRIVADO] Juan te dice: Hola`. Juan ve confirmación. Pedro no ve nada.

**Procedimiento**: Cliente Juan envía `/privado Maria Hola Maria`. Verificar que solo Maria lo recibe.

*(Captura aquí)*

**Resultado esperado**: Maria ve `[PRIVADO] Juan te dice: Hola Maria`. Juan recibe confirmación. Pedro no ve nada.

---

*(Insertar captura aquí)*

### Test 4: Usuario que No Existe

---

**Qué probé**: Qué pasa si mandas un privado a alguien que no está.

### Test 4: Usuario No Encontrado

**Cómo**: Escribí `/privado NoExisto Hola`.

**Descripción**: Probar el manejo de errores cuando se intenta enviar mensaje privado a usuario inexistente.

**Qué debería pasar**: El cliente recibe: "Error: Usuario 'NoExisto' no encontrado".

**Procedimiento**: Enviar `/privado UsuarioInexistente Hola`.

*(Captura aquí)*

**Resultado esperado**: Cliente recibe mensaje del servidor: "Error: Usuario 'UsuarioInexistente' no encontrado".

---

*(Insertar captura aquí)*

### Test 5: Desconexión Normal

---

**Qué probé**: Que no salte "lost connection" al salir con exit().

### Test 5: Desconexión Ordenada

**Cómo**: Un cliente escribe `exit()`.

**Descripción**: Verificar que no aparecen errores de "lost connection" al desconectarse correctamente.

**Qué debería pasar**: Cliente dice "Desconexión confirmada" y termina bien. Servidor y otros ven "X ha salido del chat".

**Procedimiento**: Un cliente escribe `exit()` y presiona Enter.

*(Captura aquí)*

**Resultado esperado**: Cliente muestra "Desconexión confirmada" y termina limpiamente. Servidor y otros clientes reciben notificación "X ha salido del chat".

---

*(Insertar captura aquí)*

### Test 6: Cerrar de Golpe

---

**Qué probé**: Qué pasa si cierras la terminal con Ctrl+C.

### Test 6: Desconexión Abrupta

**Cómo**: Cierro la terminal de un cliente bruscamente.

**Descripción**: Comprobar que el servidor maneja correctamente cuando un cliente cierra la terminal sin usar exit().

**Qué debería pasar**: Servidor detecta que se cayó, lo borra de la lista, avisa a los demás.

**Procedimiento**: Cerrar terminal de un cliente con Ctrl+C.

*(Captura aquí)*

**Resultado esperado**: Servidor detecta conexión perdida, elimina al cliente de la lista, notifica a los demás usuarios.

---

*(Insertar captura aquí)*

## Lo Que Aprendí

---

**Sockets y TCP**: Ahora entiendo por qué necesitas serialización. TCP es un chorro continuo de bytes sin separadores. Si no pones [longitud][datos], no sabes dónde termina cada mensaje.

## Lo Que He Aprendido

**Programación con hilos**: Me quedó claro la diferencia entre hacer todo secuencial (bloqueante) vs hacer cosas en paralelo. El cliente necesita dos hilos porque si recvMSG() te bloquea el programa, no puedes escribir mientras esperas. Con dos hilos, uno espera mensajes y otro captura tu input.

**Sockets y comunicación en red**: Entendí cómo TCP funciona como un stream continuo de bytes y por qué necesitamos serialización. Sin el formato [longitud][datos], sería imposible saber dónde termina un mensaje y empieza el siguiente.

**Sincronización**: Aprendí que sin mutex en el servidor, dos hilos pueden intentar modificar la lista de clientes a la vez y liarla. También que std::atomic es perfecto para banderas simples como isRunning.

**Programación con hilos**: La diferencia entre bloquear el programa entero vs ejecutar tareas en paralelo. El cliente necesita dos hilos porque recibir mensajes (recvMSG) es bloqueante - si lo hiciéramos en el mismo hilo que captura input del usuario, no podríamos escribir mientras esperamos mensajes.

**Diseñar protocolos**: Vi lo importante que es pensar bien el formato desde el principio. Como definí los tipos de mensaje con un enum y una estructura extensible, añadir mensajes privados fue bastante fácil. Solo tuve que meter un nuevo tipo y un campo extra.

**Sincronización**: Por qué necesitamos mutex en el servidor. Sin él, dos hilos podrían intentar modificar la lista de clientes simultáneamente y corromper los datos. También aprendí sobre std::atomic para variables compartidas simples.

**Manejo de errores**: Ahora siempre valido los buffers (pueden estar vacíos si se cae la conexión), uso try-catch para cosas que pueden petar (como std::stoi), y pongo mensajes de error útiles para el usuario.

**Diseño de protocolos**: La importancia de definir un formato claro y extensible. Añadir mensajes privados fue fácil porque solo necesité un nuevo valor en el enum y un campo extra en la estructura.

**Debugging distribuido**: Debuggear esto fue más chungo que debuggear un programa normal porque el estado está repartido entre varios procesos. Los logs del servidor me salvaron la vida para entender qué pasaba.

**Manejo de errores**: Validar siempre los buffers (pueden estar vacíos si se pierde la conexión), usar try-catch para operaciones que pueden fallar (std::stoi), y proporcionar mensajes de error útiles al usuario.

---

**Debugging de sistemas distribuidos**: Es más complejo que debuggear un programa secuencial porque el estado está repartido entre varios procesos. Los logs detallados en el servidor fueron cruciales para entender qué pasaba.

**Autor**: Ismael Hernandez Clemente  

**Asignatura**: Sistemas Distribuidos - U-TAD  ---

**Fecha**: Noviembre 2025

**Autor**: Ismael Hernandez Clemente  
**Asignatura**: Sistemas Distribuidos - U-TAD  
**Fecha**: Noviembre 2025

### Requisitos Base (5 puntos)

**Servidor Multi-Cliente**

El servidor escucha en el puerto 3000 de localhost y está diseñado para gestionar múltiples clientes de forma concurrente. Cada vez que un nuevo cliente se conecta, se crea un hilo independiente (detached) para manejar su comunicación, permitiendo así que el servidor procese múltiples conexiones simultáneas sin bloqueos.

La lista de clientes conectados se mantiene como una estructura compartida (std::list<ClientInfo>) protegida por un mutex para garantizar operaciones thread-safe. Cada cliente se registra con su identificador de socket y su nombre de usuario, permitiendo tanto la búsqueda por nombre como el reenvío selectivo de mensajes.

El servidor implementa un sistema de broadcast que reenvía los mensajes públicos a todos los clientes conectados excepto al remitente. Además, mantiene logs detallados en consola que registran conexiones, desconexiones y mensajes intercambiados, facilitando el seguimiento del estado del sistema.

**Cliente Interactivo**

El cliente solicita el nombre de usuario al iniciar y establece una conexión TCP/IP con el servidor en 127.0.0.1:3000. Una vez conectado, se inicia un hilo paralelo dedicado exclusivamente a la recepción de mensajes del servidor, permitiendo que el hilo principal se dedique a capturar la entrada del usuario sin bloqueos.

Esta arquitectura de dos hilos permite una experiencia de usuario fluida: mientras el usuario escribe un mensaje, puede recibir y visualizar mensajes de otros usuarios en tiempo real. El cliente utiliza una variable atómica (std::atomic<bool>) para coordinar el estado de ejecución entre ambos hilos de forma segura.

El comando exit() permite una desconexión ordenada: se envía un mensaje de tipo MSG_DISCONNECT al servidor, se espera la confirmación, y luego se cierra la conexión limpiamente.

**Protocolo de Comunicación**

El protocolo implementado utiliza serialización personalizada mediante las funciones pack() y unpack(). Cada campo de datos se empaqueta con el formato [longitud (4 bytes)][contenido (longitud bytes)], donde la longitud es un entero que indica cuántos bytes ocupa el contenido.

Este enfoque resuelve el problema de la delimitación de mensajes en streams TCP: al conocer de antemano la longitud de cada campo, el receptor puede extraer exactamente la cantidad correcta de bytes sin ambigüedad, incluso si los mensajes llegan fragmentados o concatenados.

### Mejoras y Soluciones (Bonificaciones - 5 puntos)

**Solución al Error "Lost Connection" (2 puntos)**

El problema del "lost connection" ocurre cuando el cliente cierra abruptamente la conexión sin dar tiempo al servidor a procesar la desconexión de forma ordenada, generando mensajes de error confusos en la consola.

La solución implementada introduce un mensaje de control de desconexión (MSG_DISCONNECT). Cuando el usuario escribe exit(), el cliente no cierra inmediatamente la conexión, sino que:

1. Envía un mensaje de tipo MSG_DISCONNECT al servidor
2. El servidor procesa este mensaje, notifica a los demás usuarios, y envía una confirmación de desconexión al cliente
3. El cliente recibe esta confirmación en su hilo receptor, establece la bandera isRunning a false de forma controlada
4. Finalmente, ambos extremos cierran la conexión de forma ordenada

Este handshake de cierre asegura que no queden mensajes pendientes en los buffers y que ambas partes estén sincronizadas sobre el estado de la conexión. El servidor no intenta enviar más datos a un cliente que ya se desconectó, y el cliente no muestra errores de conexión perdida cuando la desconexión es intencional.

**Mensajes Privados (3 puntos)**

La implementación de mensajes privados requirió extender el protocolo original para soportar diferentes tipos de comunicación. Se introduce un campo de tipo de mensaje al inicio de cada paquete, que puede ser:

- MSG_PUBLIC (0): Mensaje público para todos
- MSG_PRIVATE (1): Mensaje privado a un usuario específico
- MSG_DISCONNECT (2): Señal de desconexión
- MSG_CONNECT (3): Mensaje inicial de conexión con el nombre de usuario

Para los mensajes privados, el protocolo se extiende añadiendo un campo adicional de destinatario:

[tipo][username][contenido][destinatario]

El cliente implementa el comando /privado <usuario> <mensaje> que parsea la entrada del usuario, extrae el destinatario y el mensaje, y construye un paquete MSG_PRIVATE correctamente formateado.

En el servidor, la lista de clientes se transformó de una simple lista de enteros (client IDs) a una lista de estructuras ClientInfo que almacenan pares {clientId, username}. Esto permite la búsqueda eficiente de usuarios por nombre mediante std::find_if con un lambda.

Cuando el servidor recibe un mensaje privado:

1. Desempaqueta el tipo de mensaje y reconoce que es privado
2. Extrae el nombre del remitente, el contenido y el destinatario
3. Busca el clientId del destinatario en la lista de usuarios conectados
4. Si lo encuentra, reenvía el mensaje solo a ese cliente
5. Envía una confirmación al remitente indicando el estado de la operación
6. Si no lo encuentra, notifica al remitente que el usuario no existe

Esta arquitectura es extensible: añadir nuevos tipos de mensaje solo requiere agregar un nuevo valor al enum MessageType y extender la lógica de procesamiento en los switches de cliente y servidor.

## Estructura del Proyecto

El proyecto se organiza en una estructura clara que separa las responsabilidades:

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

**protocol.h**: Define la estructura del protocolo de comunicación. Contiene el enum MessageType con los cuatro tipos de mensaje soportados y la estructura Message que encapsula todos los campos necesarios para la comunicación. Esta separación permite que tanto cliente como servidor compartan las mismas definiciones sin duplicar código.

**server.cpp**: Implementa toda la lógica del servidor. Incluye la función main que inicializa el socket del servidor y entra en un bucle infinito de aceptación de clientes, la función handleClient que se ejecuta en un hilo independiente para cada cliente conectado, y funciones auxiliares para broadcast, búsqueda de usuarios y envío de mensajes. La gestión de la lista compartida de clientes se realiza con operaciones protegidas por mutex.

**client.cpp**: Implementa la lógica del cliente. La función main gestiona el bucle de envío de mensajes y la entrada del usuario, mientras que la función receiveMessages se ejecuta en un hilo paralelo para la recepción continua de mensajes del servidor. También incluye funciones para parsear comandos especiales como /privado y /ayuda.

**CMakeLists.txt**: Configura la compilación del proyecto. Define dos ejecutables independientes (server y client), enlaza con libUtils y pthread, y establece el estándar C++17 requerido para las características modernas utilizadas (structured bindings, auto en lambdas, etc.).

## Protocolo y Comunicacion

La comunicación entre cliente y servidor sigue un protocolo binario personalizado basado en serialización con longitud prefijada. Este diseño resuelve el problema fundamental de TCP: dado que es un stream continuo de bytes sin delimitadores naturales, necesitamos una forma de saber dónde termina un campo y comienza el siguiente.

### Funciones de Serialización

**pack(const std::string& data)**

Toma una cadena de texto y la convierte en un formato transmisible que incluye metadatos sobre su longitud:

1. Calcula la longitud de la cadena en bytes
2. Crea un nuevo string que comienza con esa longitud como un entero de 4 bytes
3. Concatena los datos originales después de la longitud
4. Retorna el paquete completo

Este formato garantiza que el receptor pueda extraer exactamente los bytes correctos sin leer de más o quedarse corto.

**unpack(const std::string& data)**

Realiza el proceso inverso:

1. Lee los primeros 4 bytes como un entero que indica la longitud del contenido
2. Extrae exactamente esa cantidad de bytes como el contenido
3. Retorna el contenido deserializado como string

Incluye validaciones para evitar accesos fuera de rango si el buffer está incompleto.

### Formato de Mensajes

Todos los mensajes siguen una estructura jerárquica de campos empaquetados:

**Mensaje de Conexión (MSG_CONNECT)**
```
[tipo=3][username][contenido=""]
```

Se envía una sola vez al inicio de la conexión para registrar el nombre de usuario en el servidor.

**Mensaje Público (MSG_PUBLIC)**
```
[tipo=0][username][contenido]
```

El servidor lo recibe de un cliente y lo reenvía a todos los demás clientes conectados (broadcast).

**Mensaje Privado (MSG_PRIVATE)**
```
[tipo=1][username][contenido][destinatario]
```

Incluye un campo adicional con el nombre del destinatario. El servidor lo recibe, busca al destinatario en su lista de usuarios, y lo reenvía solo a ese cliente específico.

**Mensaje de Desconexión (MSG_DISCONNECT)**
```
[tipo=2][username][contenido]
```

Señal de cierre ordenado. El servidor lo procesa, notifica a los demás usuarios, envía confirmación al cliente, y luego cierra la conexión.

### Flujo de Comunicación

**Inicialización del Cliente**

1. El cliente llama a initClient() de libUtils
2. Una vez conectado, empaqueta y envía un mensaje MSG_CONNECT con su nombre de usuario
3. El servidor recibe este mensaje, extrae el nombre, y registra el par {clientId, username} en su lista
4. El servidor notifica a todos los demás clientes que un nuevo usuario se ha unido

**Envío de Mensaje Público**

1. El usuario escribe un mensaje y presiona Enter
2. El cliente crea una estructura Message con tipo MSG_PUBLIC
3. Llama a sendMessage() que empaqueta todos los campos y los envía via sendMSG()
4. El servidor recibe el buffer, lo desempaqueta campo por campo
5. Crea un nuevo Message y llama a broadcastMessage()
6. Itera sobre todos los clientes conectados (excepto el remitente) y reenvía el mensaje

**Envío de Mensaje Privado**

1. El usuario escribe /privado <destinatario> <mensaje>
2. El cliente parsea la entrada, extrae destinatario y mensaje
3. Crea un Message con tipo MSG_PRIVATE y el campo recipient poblado
4. El servidor recibe y desempaqueta, incluyendo el campo adicional de destinatario
5. Busca el clientId del destinatario con findClientByUsername()
6. Envía el mensaje solo a ese cliente
7. Envía confirmación o error al remitente

**Desconexión Ordenada**

1. El usuario escribe exit()
2. El cliente envía MSG_DISCONNECT
3. El servidor procesa, notifica a otros usuarios, y envía MSG_DISCONNECT de vuelta
4. El hilo receptor del cliente detecta MSG_DISCONNECT, establece isRunning = false
5. El bucle principal del cliente termina
6. Se hace join del hilo receptor
7. Se cierra la conexión con closeConnection()

## Instrucciones de Compilacion y Uso

### Requisitos Previos

- CMake version 3.10 o superior
- Compilador C++ compatible con el estándar C++17 (se recomienda g++ o clang++)
- Biblioteca pthread (incluida por defecto en sistemas Linux)
- Librería libUtils proporcionada por el profesor

### Pasos para Compilar

**1. Preparar la librería libUtils**

Primero, asegurarse de que la librería esté en el directorio correcto:

```bash
mkdir -p lib
cp /ruta/a/libUtils.so lib/
```

Si la librería no está en el PATH del sistema, será necesario configurar LD_LIBRARY_PATH:

```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(pwd)/lib
```

**2. Crear el directorio de compilación**

CMake utiliza compilaciones fuera del árbol de fuentes (out-of-tree builds) para mantener limpio el código fuente:

```bash
mkdir build
cd build
```

**3. Configurar el proyecto**

CMake generará los Makefiles necesarios analizando el CMakeLists.txt:

```bash
cmake ..
```

Esto detectará automáticamente el compilador, verificará las dependencias, y configurará los flags de compilación.

**4. Compilar los ejecutables**

```bash
make
```

Si la compilación es exitosa, se generarán dos ejecutables en el directorio build:

- server: Ejecutable del servidor
- client: Ejecutable del cliente

Para compilaciones más rápidas en sistemas multi-core:

```bash
make -j$(nproc)
```

### Ejecución del Sistema

**Iniciar el Servidor**

En una terminal, desde el directorio build:

```bash
./server
```

El servidor mostrará un mensaje indicando que está escuchando:

```
========================================
    SERVIDOR CHAT-ROOM - PUERTO 3000   
========================================

[OK] Servidor iniciado en localhost:3000
[INFO] Esperando conexiones de clientes...
```

El servidor quedará bloqueado esperando conexiones. No requiere entrada del usuario; toda la actividad se registra automáticamente en logs.

**Iniciar Clientes**

Abrir una o más terminales adicionales (tantas como clientes se desee simular). En cada una, desde el directorio build:

```bash
./client
```

Cada cliente solicitará un nombre de usuario:

```
========================================
       CLIENTE CHAT-ROOM v2.0          
========================================

Por favor, ingresa tu nombre de usuario: Juan
```

Tras ingresar el nombre y presionar Enter, el cliente se conectará al servidor y estará listo para enviar mensajes.

### Comandos Disponibles

El cliente acepta los siguientes comandos:

**Mensaje Público**

Simplemente escribir el texto y presionar Enter. El mensaje se enviará a todos los usuarios conectados:

```
> Hola a todos desde el cliente de Juan
```

**Mensaje Privado**

Utilizar el comando /privado seguido del nombre del destinatario y el mensaje:

```
> /privado Maria Hola Maria, esto es privado
[INFO] Mensaje privado enviado a Maria
```

El servidor buscará al usuario Maria y reenviará el mensaje solo a ella. Si Maria no está conectada, se mostrará un error.

**Ayuda**

Mostrar la lista de comandos disponibles:

```
> /ayuda
```

**Salir del Chat**

Para desconectarse de forma ordenada:

```
> exit()
[INFO] Cerrando conexión...
[INFO] Desconectado del servidor. ¡Hasta pronto!
```

Esto enviará la señal de desconexión al servidor, esperará confirmación, y cerrará limpiamente la conexión.

## Ejemplos de Ejecución

### Escenario: Conversación Pública entre Tres Usuarios

**Terminal 1 - Servidor**

```
[CONEXIÓN] Usuario 'Juan' (ID: 1) se ha unido al chat
[CONEXIÓN] Usuario 'Maria' (ID: 2) se ha unido al chat
[CONEXIÓN] Usuario 'Pedro' (ID: 3) se ha unido al chat
[PÚBLICO] Juan dice: Hola a todos!
[PÚBLICO] Maria dice: Hola Juan, cómo estás?
[PÚBLICO] Pedro dice: Hola equipo!
```

**Terminal 2 - Cliente Juan**

```
[OK] Conectado al servidor exitosamente
[INFO] ¡Bienvenido al chat, Juan!
> Hola a todos!
[SERVIDOR] Maria se ha unido al chat
[SERVIDOR] Pedro se ha unido al chat
[Maria]: Hola Juan, cómo estás?
[Pedro]: Hola equipo!
```

**Terminal 3 - Cliente Maria**

```
[SERVIDOR] Juan se ha unido al chat
> Hola Juan, cómo estás?
[Juan]: Hola a todos!
[SERVIDOR] Pedro se ha unido al chat
[Pedro]: Hola equipo!
```

**Terminal 4 - Cliente Pedro**

```
[SERVIDOR] Juan se ha unido al chat
[SERVIDOR] Maria se ha unido al chat
> Hola equipo!
[Juan]: Hola a todos!
[Maria]: Hola Juan, cómo estás?
```

### Escenario: Mensajes Privados

**Terminal 2 - Cliente Juan**

```
> /privado Maria Oye Maria, tenemos que revisar el código del servidor
[INFO] Mensaje privado enviado a Maria
[SERVIDOR] Mensaje privado enviado a Maria
```

**Terminal 3 - Cliente Maria**

```
[PRIVADO] Juan te dice: Oye Maria, tenemos que revisar el código del servidor
> /privado Juan Claro, lo veo ahora y te comento
[INFO] Mensaje privado enviado a Juan
```

**Terminal 1 - Servidor**

```
[PRIVADO] De: Juan Para: Maria | Mensaje: Oye Maria, tenemos que revisar el código del servidor
[PRIVADO] De: Maria Para: Juan | Mensaje: Claro, lo veo ahora y te comento
```

Observar que Pedro (Terminal 4) no ve estos mensajes privados; solo ven la conversación Juan y Maria.

### Escenario: Desconexión Ordenada

**Terminal 2 - Cliente Juan**

```
> exit()
[INFO] Cerrando conexión...
[INFO] Desconexión confirmada
[INFO] Desconectado del servidor. ¡Hasta pronto!
```

**Terminal 1 - Servidor**

```
[DESCONEXIÓN] Usuario 'Juan' ha salido del chat
```

**Terminal 3 - Cliente Maria**

```
[SERVIDOR] Juan ha salido del chat
```

Maria y Pedro reciben la notificación de que Juan abandonó el chat, pero no ven ningún error de conexión perdida.

