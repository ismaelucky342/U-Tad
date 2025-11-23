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

# Algunas de las consultas las he hecho en admin por lo que están comentadas para github
# 1. Configuración de memoria (solo funciona si tienes permisos de admin)
# r.config_set("maxmemory", 2 * 1024 * 1024 * 1024)
# r.config_set("maxmemory-policy", "allkeys-lru")

# 2. Políticas de desalojo disponibles (comentadas, solo admin)
# r.config_set("maxmemory-policy", "noeviction")
# r.config_set("maxmemory-policy", "allkeys-lru")
# r.config_set("maxmemory-policy", "allkeys-lfu")
# r.config_set("maxmemory-policy", "allkeys-random")
# r.config_set("maxmemory-policy", "volatile-lru")
# r.config_set("maxmemory-policy", "volatile-lfu")
# r.config_set("maxmemory-policy", "volatile-ttl")
# r.config_set("maxmemory-policy", "volatile-random")

# 3. Estrategia de TTL
r.setex("session:user:abc123", 1800, '{"user_id":"C123","tipo":"cliente"}')
r.setex("session:driver:xyz789", 28800, '{"user_id":"D456","vehiculo":"V001"}')
r.setex("session:admin:mno345", 3600, '{"user_id":"A789","tipo":"admin"}')
r.set("cache:vehiculo:V001", '{"marca":"Mercedes","modelo":"Sprinter"}', ex=300)
r.setex("prereserva:PR001", 900, '{"vehiculo":"V001","cliente":"C123"}')
r.hset("reserva:R001", mapping={"vehiculo_id":"V001", "cliente_id":"C123"})
r.expire("reserva:R001", 259200)
r.setex("reset:token:abc789", 3600, '{"email":"juan@email.com"}')
r.set("bloqueo:vehiculo:V001", "R001", ex=259200)
r.set("login:attempts:juan@email.com", 0, ex=900)
r.set("stats:reservas:dia:2025-11-20", 15, ex=604800)
r.set("cache:busqueda:madrid:furgonetas", '["V001","V004","V007"]', ex=600)
print("\n=== ESTRATEGIA DE TTL Y CACHÉ ===")
print("TTL session:user:abc123:", r.ttl("session:user:abc123"))
print("Cache vehículo V001:", r.get("cache:vehiculo:V001"))

# 4. Verificar y gestionar TTL
ttl = r.ttl("session:user:abc123")
pttl = r.pttl("session:user:abc123")
r.expire("session:user:abc123", 1800)
r.persist("session:user:abc123")
ttl_vehiculo = r.ttl("vehiculo:V001")
print("\n=== VERIFICACIÓN Y GESTIÓN DE TTL ===")
print("TTL session:user:abc123:", ttl)
print("PTTL session:user:abc123:", pttl)
print("TTL vehiculo:V001:", ttl_vehiculo)

# 5. Expiración con setex y psetex
r.setex("cache:key", 300, "valor")
r.psetex("cache:key", 300000, "valor")
r.set("cache:key", "valor", ex=300)
r.set("cache:key", "valor", px=300000)
# r.set("cache:key", "valor", exat=1732147200)
# r.set("cache:key", "valor", pxat=1732147200000)
print("\n=== EXPIRACIÓN CON SETEX/PSSETEX ===")
print("TTL cache:key:", r.ttl("cache:key"))

# 6. Patrón de caché: cache-aside
cache = r.get("cache:vehiculo:V001")
if not cache:
    # Simular consulta a BD y guardar en caché
    r.set("cache:vehiculo:V001", '{"marca":"Mercedes","modelo":"Sprinter"}', ex=300)
print("\n=== PATRÓN CACHE-ASIDE ===")
print("Cache vehículo V001:", r.get("cache:vehiculo:V001"))

# 7. Invalidación de caché
r.hset("vehiculo:V001", "precio_dia", 95.00)
r.delete("cache:vehiculo:V001")
r.delete("cache:busqueda:madrid:furgonetas")
r.delete("cache:busqueda:madrid:todos")
print("\n=== INVALIDACIÓN DE CACHÉ ===")
print("Cache vehículo V001 tras delete:", r.get("cache:vehiculo:V001"))

# 8. Caché con actualización proactiva
r.hset("vehiculo:V001", "precio_dia", 95.00)
r.set("cache:vehiculo:V001", '{"marca":"Mercedes","modelo":"Sprinter","precio_dia":95.00}', ex=300)
print("\n=== CACHÉ CON ACTUALIZACIÓN PROACTIVA ===")
print("Cache vehículo V001 actualizado:", r.get("cache:vehiculo:V001"))

# 9. Expiración por lotes
with r.pipeline() as pipe:
    pipe.expire("session:user:abc123", 0)
    pipe.expire("session:user:def456", 0)
    pipe.expire("session:user:ghi789", 0)
    pipe.execute()
r.delete("session:user:abc123", "session:user:def456", "session:user:ghi789")
print("\n=== EXPIRACIÓN POR LOTES ===")
print("session:user:abc123 existe:", r.exists("session:user:abc123"))
print("session:user:def456 existe:", r.exists("session:user:def456"))
print("session:user:ghi789 existe:", r.exists("session:user:ghi789"))

# 10. Monitoreo de memoria (solo admin)
# info_memory = r.info("memory")
# info_stats = r.info("stats")
