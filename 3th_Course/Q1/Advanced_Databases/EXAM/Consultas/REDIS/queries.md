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