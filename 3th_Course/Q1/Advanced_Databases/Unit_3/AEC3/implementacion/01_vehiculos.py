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

# 1. Registro de vehículos (hashes)
vehiculos = [
    ("V001", {"matricula":"1234ABC", "marca":"Mercedes", "modelo":"Sprinter", "tipo":"furgoneta", "capacidad":12, "estado":"disponible", "ubicacion":"Madrid Centro", "km_actuales":45000, "año":2022, "precio_dia":89.50, "rating":4.7}),
    ("V002", {"matricula":"5678DEF", "marca":"Iveco", "modelo":"Daily", "tipo":"autobus", "capacidad":25, "estado":"disponible", "ubicacion":"Barcelona", "km_actuales":32000, "año":2023, "precio_dia":145.00, "rating":4.9}),
    ("V003", {"matricula":"9012GHI", "marca":"Ford", "modelo":"Transit", "tipo":"van", "capacidad":8, "estado":"en_uso", "ubicacion":"Valencia", "km_actuales":28500, "año":2021, "precio_dia":75.00, "rating":4.5}),
    ("V004", {"matricula":"3456JKL", "marca":"Renault", "modelo":"Master", "tipo":"furgoneta", "capacidad":14, "estado":"disponible", "ubicacion":"Sevilla", "km_actuales":52000, "año":2020, "precio_dia":82.00, "rating":4.3}),
    ("V005", {"matricula":"7890MNO", "marca":"MAN", "modelo":"Lion's City", "tipo":"autobus", "capacidad":40, "estado":"mantenimiento", "ubicacion":"Madrid Taller", "km_actuales":85000, "año":2019, "precio_dia":180.00, "rating":4.6}),
]
for vid, attrs in vehiculos:
    r.hset(f"vehiculo:{vid}", mapping=attrs)

# 2. Consultas de vehículos
info_v001 = r.hgetall("vehiculo:V001")
campos_v001 = r.hmget("vehiculo:V001", "marca", "modelo", "precio_dia", "estado", "ubicacion")
estado_v001 = r.hget("vehiculo:V001", "estado")
existe_v001 = r.hexists("vehiculo:V001", "matricula")

# 3. Actualización de vehículos
r.hset("vehiculo:V001", "ubicacion", "Madrid Norte")
r.hset("vehiculo:V003", mapping={"km_actuales":28750, "estado":"disponible", "ubicacion":"Valencia Centro"})
r.hset("vehiculo:V001", mapping={"estado":"mantenimiento", "ubicacion":"Madrid Taller"})
r.hset("vehiculo:V001", "rating", 4.8)

# 4. Contador de vehículos por estado (strings)
r.set("stats:vehiculos:total", 5)
r.set("stats:vehiculos:disponibles", 3)
r.set("stats:vehiculos:en_uso", 1)
r.set("stats:vehiculos:mantenimiento", 1)
r.decr("stats:vehiculos:disponibles")
r.incr("stats:vehiculos:en_uso")
r.decr("stats:vehiculos:en_uso")
r.incr("stats:vehiculos:disponibles")
disponibles = r.get("stats:vehiculos:disponibles")
total = r.get("stats:vehiculos:total")

# 5. Búsqueda por tipo (sets)
r.sadd("vehiculos:tipo:furgoneta", "V001", "V004")
r.sadd("vehiculos:tipo:autobus", "V002", "V005")
r.sadd("vehiculos:tipo:van", "V003")
furgonetas = r.smembers("vehiculos:tipo:furgoneta")
es_furgoneta = r.sismember("vehiculos:tipo:furgoneta", "V001")
num_furgonetas = r.scard("vehiculos:tipo:furgoneta")

# 6. Índice de disponibilidad por ciudad
r.sadd("vehiculos:disponibles:madrid", "V001")
r.sadd("vehiculos:disponibles:barcelona", "V002")
r.sadd("vehiculos:disponibles:valencia", "V003")
r.sadd("vehiculos:disponibles:sevilla", "V004")
disponibles_madrid = r.smembers("vehiculos:disponibles:madrid")
r.sadd("vehiculos:estado:disponible", "V001", "V002", "V004")
furgonetas_disponibles = r.sinter("vehiculos:tipo:furgoneta", "vehiculos:estado:disponible")

# 7. Caché de vehículos más consultados
r.set("cache:vehiculo:V001", '{"id":"V001","marca":"Mercedes","modelo":"Sprinter","precio_dia":89.50,"disponible":true}', ex=300)
cache_v001 = r.get("cache:vehiculo:V001")
ttl_v001 = r.ttl("cache:vehiculo:V001")
r.persist("cache:vehiculo:V001")
r.expire("cache:vehiculo:V001", 600)

# 8. Operaciones útiles adicionales
r.hincrby("vehiculo:V001", "km_actuales", 150)
r.hincrbyfloat("vehiculo:V001", "precio_dia", 5.50)
campos = r.hkeys("vehiculo:V001")
valores = r.hvals("vehiculo:V001")
num_campos = r.hlen("vehiculo:V001")
r.hdel("vehiculo:V001", "campo_temporal")

# 9. Información de vehículo extendida
r.hset("vehiculo:V001:detalles", mapping={
    "color": "blanco",
    "matriculacion": "2022-03-15",
    "seguro": "Seguro123",
    "revision_proxima": "2025-12-01",
    "propietario": "FleetHub Madrid",
    "contacto_taller": "+34600123456"
})
detalles_v001 = r.hgetall("vehiculo:V001:detalles")

# 10. Patrón de búsqueda y listado
todos_vehiculos = r.keys("vehiculo:V*")
info_basica = [r.hmget(f"vehiculo:{vid[-4:]}", "matricula", "marca", "modelo", "estado", "ubicacion") for vid in ["V001", "V002", "V003"]]
