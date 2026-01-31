Ejercicio A: 
1. Crea una lista llamada tasks y agrega las tareas: "task1", "task2" y "task3".
2. Extrae la primera tarea de la lista y marca que ha sido completada (elimínala de la lista).
3. Obtén todas las tareas restantes en la lista.

LPUSH tasks task1 task2 task3 
RPOP tasks
LRANGE tasks 0 -1

Ejercicio B:
1. Crea un conjunto llamado online_users y agrega los usuarios: "Alice",
"Bob" y "Charlie".
2. Comprueba si el usuario "Bob" está en línea.
3. Elimina al usuario "Charlie" del conjunto y muestra todos los usuarios
restantes en línea

SADD online_users "Alice" "Bob" "Charlie"
SISMEMBER online_users "Bob"
SREM online_users "Charlie"
SMEMBERS online_users

Ejercicio C: 
Utiliza una transacción para realizar las siguientes acciones de manera atómica:
- Establece una clave balance con el valor 1000.
- Incrementa el balance en 500.
- Reduce el balance en 200.

MULT
SET balance 1000
INCRBY balance 500
DECRBY balance 200
EXEC

Ejercicio D:
1. Crea un canal llamado news_channel. Simula la suscripción de un cliente
al canal.
2. Publica un mensaje en el canal diciendo "Breaking news: Redis is
awesome!".

SUBSCRIBE news_channel
PUBLISH news_channel "Breaking news: Redis is awesome!"


Ejercicio E:
1. Crea un hash llamado user:1000 que almacene información del usuario:
- name: "Alice",
- age: 30,
- city: "New York".
2. Actualiza el campo age a 31.
3. Recupera solo el nombre y la ciudad del hash

HSET user:100 name "alice" age 30 city "New York"
HSET user:100 age 31
HMGET user:100 name city