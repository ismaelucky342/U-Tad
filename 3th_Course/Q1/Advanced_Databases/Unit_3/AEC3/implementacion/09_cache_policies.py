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

# 3. Estrategia de TTL para FleetHub
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

# 4. Verificar y gestionar TTL
ttl = r.ttl("session:user:abc123")
pttl = r.pttl("session:user:abc123")
r.expire("session:user:abc123", 1800)
r.persist("session:user:abc123")
ttl_vehiculo = r.ttl("vehiculo:V001")

# 5. Expiración con setex y psetex
r.setex("cache:key", 300, "valor")
r.psetex("cache:key", 300000, "valor")
r.set("cache:key", "valor", ex=300)
r.set("cache:key", "valor", px=300000)
# r.set("cache:key", "valor", exat=1732147200)
# r.set("cache:key", "valor", pxat=1732147200000)

# 6. Patrón de caché: cache-aside
cache = r.get("cache:vehiculo:V001")
if not cache:
    # Simular consulta a BD y guardar en caché
    r.set("cache:vehiculo:V001", '{"marca":"Mercedes","modelo":"Sprinter"}', ex=300)

# 7. Invalidación de caché
r.hset("vehiculo:V001", "precio_dia", 95.00)
r.delete("cache:vehiculo:V001")
r.delete("cache:busqueda:madrid:furgonetas")
r.delete("cache:busqueda:madrid:todos")

# 8. Caché con actualización proactiva
r.hset("vehiculo:V001", "precio_dia", 95.00)
r.set("cache:vehiculo:V001", '{"marca":"Mercedes","modelo":"Sprinter","precio_dia":95.00}', ex=300)

# 9. Expiración por lotes
with r.pipeline() as pipe:
    pipe.expire("session:user:abc123", 0)
    pipe.expire("session:user:def456", 0)
    pipe.expire("session:user:ghi789", 0)
    pipe.execute()
r.delete("session:user:abc123", "session:user:def456", "session:user:ghi789")

# 10. Monitoreo de memoria (solo admin)
# info_memory = r.info("memory")
# info_stats = r.info("stats")

# 11. Keys volátiles vs persistentes
r.set("config:precios:base", 50)
r.set("config:iva", 0.21)
r.hset("stats:totales", mapping={"vehiculos":50, "reservas":1547})
r.setex("session:user:abc123", 1800, "...")
r.set("cache:vehiculo:V001", "...", ex=300)

# 12. Expiración perezosa y activa (no requiere código, es automático)

# 13. Callback de expiración (keyspace notifications, solo admin)
# r.config_set("notify-keyspace-events", "Ex")
# Suscribirse: r.pubsub().psubscribe("__keyevent@0__:expired")

# 14. Estrategia de caché para diferentes datos
r.set("cache:config:ciudades", '["Madrid","Barcelona","Valencia"]', ex=86400)
r.set("cache:vehiculos:disponibles:madrid", '["V001","V004","V007"]', ex=60)
r.set("cache:ubicacion:V001", '{"lat":40.4168,"lon":-3.7038}', ex=10)
r.hset("vehiculo:V001", mapping={"matricula":"1234ABC", "marca":"Mercedes", "modelo":"Sprinter"})

# 15. Caché de consultas complejas
r.set("cache:busqueda:madrid:furgonetas:disponibles:rango_50_100", '["V001","V004","V007"]', ex=300)
existe = r.exists("cache:busqueda:madrid:furgonetas:disponibles:rango_50_100")

# 16. Caché con versiones
r.set("cache:v2:vehiculo:V001", '{"marca":"Mercedes"}', ex=300)
r.set("cache:v3:vehiculo:V001", '{"marca":"Mercedes","año":2022}', ex=300)

# 17. Warming up de caché
r.set("cache:vehiculo:V001", '{"marca":"Mercedes","modelo":"Sprinter"}', ex=3600)
r.set("cache:vehiculo:V002", '{"marca":"Iveco","modelo":"Daily"}', ex=3600)
r.set("cache:vehiculo:V003", '{"marca":"Ford","modelo":"Transit"}', ex=3600)

# 18. Gestión de memoria proactiva
# for key in r.scan_iter("cache:*"):
#     r.delete(key)
r.delete("cache:vehiculo:V001", "cache:vehiculo:V002", "cache:vehiculo:V003")
# for key in r.scan_iter("cache:busqueda:*"):
#     r.delete(key)

# 19. Análisis de hits/misses
r.set("stats:cache:hits", 0)
r.set("stats:cache:misses", 0)
if r.get("cache:vehiculo:V001"):
    r.incr("stats:cache:hits")
else:
    r.incr("stats:cache:misses")
hits = r.get("stats:cache:hits")
misses = r.get("stats:cache:misses")

# 20. Políticas personalizadas por tipo de dato
r.hset("vehiculo:V001", "matricula", "1234ABC")
r.set("cache:config:precios", "...", ex=3600)
r.set("cache:vehiculo:V001", "...", ex=300)
r.set("cache:busqueda:temporal", "...", ex=60)

# 21. Resumen de estrategia (solo admin)
# r.config_set("maxmemory-policy", "allkeys-lru")
# r.config_set("maxmemory", 2 * 1024 * 1024 * 1024)
# r.config_set("notify-keyspace-events", "Ex")
# info_memory = r.info("memory")
# info_stats = r.info("stats")
