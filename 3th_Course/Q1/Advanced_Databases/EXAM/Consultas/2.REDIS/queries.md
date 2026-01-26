Ejercicio 1: Conectar y set/get de claves

Enunciado:
Guardar un valor simple y recuperarlo.

SET nombre "ismael"
GET nombre



Ejercicio 2: Contador de visitas por página

Enunciado:
Contar cuántas veces se visita cada página del sitio web.

HINCRBY visitas:pagina "/inicio" 1
HINCRBY visitas:pagina "/contacto" 1 
HGET visitas:pagina "/inicio"
HGETALL visitas:pagina



Ejercicio 3: Últimos mensajes de chat

Enunciado:
Guardar los últimos 10 mensajes de un chat de grupo.

LPUSH chat:grupo1 "Hola!"
LPUSH chat:grupo1 "Bienvenidos"
LTRIM chat:grupo1 0 9 
LRANGE chat:grupo1 0 -1



Ejercicio 4: Usuarios únicos conectados hoy

Enunciado:
Guardar los usuarios únicos que se conectan cada día.

SADD usuarios:hoy "Ismael"
SADD usuarios:hoy "Ana"
SADD usuarios:hoy "Ismael" <- ignorado no se duplica
SCARD usuarios:hoy <- devuelve la cantidad de usuarios únicos
SMEMBERS usuarios:hoy 



Ejercicio 5: Sesión de usuario con expiración

Enunciado:
Guardar la sesión de un usuario que caduca en 30 minutos.

SETEX session:12345 "Ismael" 1800
GET session:12345



Ejercicio 6: Rate limit por usuario

Enunciado
Limitar a 100 peticiones por minuto por usuario.

INCR rate:user:42



Ejercicio 7: Sesión de usuario

Enunciado
Guardar datos de sesión y que caduquen en 30 minutos.

HSET session:abc123 nombre "Ismael" rol "admin"
EXPIRE session:abc123 1800



Ejercicio 8: Usuarios online ahora mismo 

Enunciado 
Saber qué usuarios están conectados, sin duplicados.

SADD users:online "Ismael"
SADD users:online "Ana"
SREM users:online "Ismael" <- lo elimina
SMEMBERS users:online 



Ejercicio 9: Contador por categoría

Enunciado
Contar eventos por tipo.

HINCRBY eventos login 1 
HINCRBY eventos logout 1
HGETALL eventos 



Ejercicio 10: Mensajes recientes por usuario

Enunciado
Guardar los últimos 5 mensajes enviados por un usuario.

LPUSH user:42:messages "hola"
LPUSH user:42:messages "adios"
LTRIM user:42:messages 0 4