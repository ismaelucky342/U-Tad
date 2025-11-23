#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      Competición - ABDB                                ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        19/11/2025  -  05:00:00           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    23/11/2025  -  11:34:43           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================# 

import redis

r = redis.Redis(decode_responses=True)

# 1. Sesiones de usuarios (strings)
r.setex("session:user:abc123def456", 1800, '{"user_id":"C123","tipo":"cliente","nombre":"Juan García","email":"juan@email.com","login":"2025-11-20T10:00:00","ultima_actividad":"2025-11-20T10:15:00","permisos":["ver_vehiculos","hacer_reservas","ver_historial"]}')
r.setex("session:driver:xyz789ghi012", 7200, '{"user_id":"D456","tipo":"conductor","nombre":"Carlos Ruiz","vehiculo_asignado":"V001","estado":"activo","login":"2025-11-20T08:00:00","ubicacion":"Madrid Centro"}')
r.setex("session:admin:mno345pqr678", 3600, '{"user_id":"A789","tipo":"admin","nombre":"Laura Martín","nivel":"super_admin","login":"2025-11-20T09:00:00","ip":"192.168.1.100"}')

# 2. Verificación y validación de sesiones
session_data = r.get("session:user:abc123def456")
ttl = r.ttl("session:user:abc123def456")
r.setex("session:user:abc123def456", 1800, '{"user_id":"C123",...,"ultima_actividad":"2025-11-20T10:30:00"}')
r.expire("session:user:abc123def456", 1800)

# 3. Logout / cierre de sesión
r.delete("session:user:abc123def456")
existe = r.exists("session:user:abc123def456")

# 4. Índice de sesiones activas por usuario
r.sadd("user:C123:sessions", "session:user:abc123def456")
r.sadd("user:C123:sessions", "session:user:mobile789xyz")
sesiones_c123 = r.smembers("user:C123:sessions")
# Cerrar todas las sesiones de un usuario
for sid in sesiones_c123:
    r.delete(sid)
r.delete("user:C123:sessions")

# 5. Contador de sesiones activas
r.set("stats:sesiones:clientes:activas", 0)
r.set("stats:sesiones:conductores:activas", 0)
r.set("stats:sesiones:admins:activas", 0)
r.incr("stats:sesiones:clientes:activas")
r.decr("stats:sesiones:clientes:activas")
r.get("stats:sesiones:clientes:activas")

# 6. Sesiones con información detallada (hashes)
r.hset("session:detail:abc123def456", mapping={
    "user_id": "C123", "tipo": "cliente", "nombre": "Juan García", "email": "juan@email.com",
    "login": "2025-11-20T10:00:00", "ultima_actividad": "2025-11-20T10:30:00", "ip": "192.168.1.50",
    "dispositivo": "Chrome/Windows", "token_version": 1
})
r.expire("session:detail:abc123def456", 1800)
r.hset("session:detail:abc123def456", "ultima_actividad", "2025-11-20T10:45:00")
r.expire("session:detail:abc123def456", 1800)
hmget = r.hmget("session:detail:abc123def456", "user_id", "tipo", "ultima_actividad")
hgetall = r.hgetall("session:detail:abc123def456")

# 7. Bloqueo de cuentas / sesiones suspendidas
r.set("user:C123:blocked", "true", ex=3600)
bloqueada = r.get("user:C123:blocked")
r.set("user:C999:blocked", "permanent")
r.delete("user:C123:blocked")

# 8. Intentos de login fallidos
r.set("login:attempts:juan@email.com", 0, ex=900)
r.incr("login:attempts:juan@email.com")
intentos = r.get("login:attempts:juan@email.com")
r.set("login:blocked:juan@email.com", "true", ex=1800)
r.delete("login:attempts:juan@email.com")

# 9. Tokens de recuperación de contraseña
r.setex("reset:token:def456abc789", 3600, '{"email":"juan@email.com","user_id":"C123","created":"2025-11-20T11:00:00"}')
reset_token = r.get("reset:token:def456abc789")
r.delete("reset:token:def456abc789")

# 10. Sesiones de conductores con estado
r.hset("driver:session:D456", mapping={
    "driver_id": "D456", "nombre": "Carlos Ruiz", "vehiculo": "V001", "estado": "en_servicio",
    "reserva_actual": "R001", "ubicacion": "Madrid Norte", "inicio_turno": "2025-11-20T08:00:00",
    "ultima_ubicacion_update": "2025-11-20T12:30:00"
})
r.expire("driver:session:D456", 28800)
r.hset("driver:session:D456", mapping={"ubicacion": "Madrid Centro", "ultima_ubicacion_update": "2025-11-20T12:31:00"})
r.expire("driver:session:D456", 28800)
r.hset("driver:session:D456", "estado", "en_pausa")
r.delete("driver:session:D456")

# 11. Lista de usuarios conectados en tiempo real
r.zadd("usuarios:online", {"C123": 1732099200, "C456": 1732099260, "D789": 1732099320})
r.zadd("usuarios:online", {"C123": 1732099400})
usuarios_5min = r.zrangebyscore("usuarios:online", 1732099100, "+inf")
r.zremrangebyscore("usuarios:online", "-inf", 1732099100)

# 12. Sesiones persistentes "recuérdame"
r.setex("session:remember:long456token", 2592000, '{"user_id":"C123","tipo":"cliente","created":"2025-11-20"}')
token_persistente = r.get("session:remember:long456token")
r.delete("session:remember:long456token")

# 13. Auditoría de sesiones
r.lpush("audit:logins:C123", '{"timestamp":"2025-11-20T10:00:00","ip":"192.168.1.50","dispositivo":"Chrome","resultado":"exitoso"}')
r.ltrim("audit:logins:C123", 0, 49)
historial_logins = r.lrange("audit:logins:C123", 0, 9)

# 14. Cambio de versión de token (invalidación masiva)
r.set("user:C123:token_version", 1)
r.hset("session:detail:abc123", mapping={"user_id": "C123", "token_version": 1})
r.expire("session:detail:abc123", 1800)
r.incr("user:C123:token_version")
version_sesion = r.hget("session:detail:abc123", "token_version")
version_usuario = r.get("user:C123:token_version")

# 15. Estadísticas de sesiones
r.set("stats:logins:2025-11-20", 0)
r.incr("stats:logins:2025-11-20")
r.set("stats:peak:concurrent:2025-11-20", 0)
# Simulación de actualización de pico concurrente
actual = int(r.get("stats:sesiones:clientes:activas") or 0)
pico = int(r.get("stats:peak:concurrent:2025-11-20") or 0)
if actual > pico:
    r.set("stats:peak:concurrent:2025-11-20", actual)
r.set("stats:duracion:sesiones:total", 0)
r.set("stats:duracion:sesiones:count", 0)
r.incrby("stats:duracion:sesiones:total", 1845)
r.incr("stats:duracion:sesiones:count")
total_duracion = int(r.get("stats:duracion:sesiones:total") or 0)
num_sesiones = int(r.get("stats:duracion:sesiones:count") or 1)
promedio = total_duracion / num_sesiones

# 16. Sesiones con datos de geolocalización
r.hset("session:geo:D456", mapping={
    "driver_id": "D456", "lat": 40.4168, "lon": -3.7038, "precision": 50, "timestamp": "2025-11-20T12:45:00"
})
r.expire("session:geo:D456", 300)
r.hset("session:geo:D456", mapping={"lat": 40.4200, "lon": -3.7100, "timestamp": "2025-11-20T12:50:00"})
r.expire("session:geo:D456", 300)
