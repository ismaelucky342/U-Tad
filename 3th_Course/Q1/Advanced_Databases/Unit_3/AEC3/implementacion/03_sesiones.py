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
r.setex("session:user:abc123def456", 1800, '{"user_id":"C123","tipo":"cliente","nombre":"Juan García","email":"juan@email.com","login":"2025-11-20T10:00:00","ultima_actividad":"2025-11-20T10:15:00","permisos":["ver_vehiculos","hacer_reservas","ver_historial"]}')
r.setex("session:driver:xyz789ghi012", 7200, '{"user_id":"D456","tipo":"conductor","nombre":"Carlos Ruiz","vehiculo_asignado":"V001","estado":"activo","login":"2025-11-20T08:00:00","ubicacion":"Madrid Centro"}')
r.setex("session:admin:mno345pqr678", 3600, '{"user_id":"A789","tipo":"admin","nombre":"Laura Martín","nivel":"super_admin","login":"2025-11-20T09:00:00","ip":"192.168.1.100"}')
print("\n=== CREACIÓN DE SESIONES (STRINGS) ===")
print("Session user:", r.get("session:user:abc123def456"))
print("Session driver:", r.get("session:driver:xyz789ghi012"))
print("Session admin:", r.get("session:admin:mno345pqr678"))

# 2. Verificación y validación de sesiones
session_data = r.get("session:user:abc123def456")
ttl = r.ttl("session:user:abc123def456")
r.setex("session:user:abc123def456", 1800, '{"user_id":"C123",...,"ultima_actividad":"2025-11-20T10:30:00"}')
r.expire("session:user:abc123def456", 1800)
print("\n=== VERIFICACIÓN Y TTL ===")
print("Session data:", session_data)
print("TTL session user:", ttl)

# 3. Logout / cierre de sesión
r.delete("session:user:abc123def456")
existe = r.exists("session:user:abc123def456")
print("\n=== LOGOUT / CIERRE DE SESIÓN ===")
print("¿Existe session:user:abc123def456?:", existe)

# 4. Índice de sesiones activas por usuario
r.sadd("user:C123:sessions", "session:user:abc123def456")
r.sadd("user:C123:sessions", "session:user:mobile789xyz")
sesiones_c123 = r.smembers("user:C123:sessions")
# Cerrar todas las sesiones de un usuario
for sid in sesiones_c123:
    r.delete(sid)
r.delete("user:C123:sessions")
print("\n=== ÍNDICE DE SESIONES POR USUARIO ===")
print("Sesiones activas de C123:", sesiones_c123)

# 5. Contador de sesiones activas
r.set("stats:sesiones:clientes:activas", 0)
r.set("stats:sesiones:conductores:activas", 0)
r.set("stats:sesiones:admins:activas", 0)
r.incr("stats:sesiones:clientes:activas")
r.decr("stats:sesiones:clientes:activas")
r.get("stats:sesiones:clientes:activas")
print("\n=== CONTADOR DE SESIONES ACTIVAS ===")
print("Clientes activas:", r.get("stats:sesiones:clientes:activas"))
print("Conductores activas:", r.get("stats:sesiones:conductores:activas"))
print("Admins activas:", r.get("stats:sesiones:admins:activas"))

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
print("\n=== SESIONES DETALLADAS (HASHES) ===")
print("Campos clave:", hmget)
print("Todos los campos:", hgetall)

# 7. Bloqueo de cuentas / sesiones suspendidas
r.set("user:C123:blocked", "true", ex=3600)
bloqueada = r.get("user:C123:blocked")
r.set("user:C999:blocked", "permanent")
r.delete("user:C123:blocked")
print("\n=== BLOQUEO DE CUENTAS ===")
print("¿C123 bloqueada temporal?:", bloqueada)
print("¿C999 bloqueada permanente?:", r.get("user:C999:blocked"))

# 8. Intentos de login fallidos
r.set("login:attempts:juan@email.com", 0, ex=900)
r.incr("login:attempts:juan@email.com")
intentos = r.get("login:attempts:juan@email.com")
r.set("login:blocked:juan@email.com", "true", ex=1800)
r.delete("login:attempts:juan@email.com")
print("\n=== INTENTOS DE LOGIN Y BLOQUEO ===")
print("Intentos de login juan@email.com:", intentos)
print("¿Login bloqueado?:", r.get("login:blocked:juan@email.com"))

# 9. Tokens de recuperación de contraseña
r.setex("reset:token:def456abc789", 3600, '{"email":"juan@email.com","user_id":"C123","created":"2025-11-20T11:00:00"}')
reset_token = r.get("reset:token:def456abc789")
print("\n=== TOKEN DE RECUPERACIÓN ===")
print("Reset token:", reset_token)
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
print("\n=== SESIÓN DE CONDUCTOR ===")
print("Driver session D456:", r.hgetall("driver:session:D456"))
r.delete("driver:session:D456")