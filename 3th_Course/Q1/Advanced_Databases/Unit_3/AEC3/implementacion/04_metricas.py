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

# 1. Contadores globales operativos
r.set("stats:flota:total_vehiculos", 50)
r.set("stats:flota:vehiculos_disponibles", 38)
r.set("stats:flota:vehiculos_en_uso", 10)
r.set("stats:flota:vehiculos_mantenimiento", 2)
r.set("stats:reservas:total_historico", 1547)
r.set("stats:reservas:activas", 10)
r.set("stats:reservas:hoy", 8)
r.set("stats:reservas:mes_actual", 234)
r.set("stats:clientes:registrados", 892)
r.set("stats:clientes:activos_hoy", 45)
r.set("stats:conductores:totales", 28)
r.set("stats:conductores:en_turno", 12)

# 2. Operaciones sobre contadores
r.decr("stats:flota:vehiculos_disponibles")
r.incr("stats:flota:vehiculos_en_uso")
r.incr("stats:reservas:activas")
r.incr("stats:reservas:hoy")
r.incr("stats:reservas:mes_actual")
r.incr("stats:flota:vehiculos_disponibles")
r.decr("stats:flota:vehiculos_en_uso")
r.decr("stats:reservas:activas")
r.decr("stats:flota:vehiculos_disponibles")
r.incr("stats:flota:vehiculos_mantenimiento")
r.incr("stats:flota:vehiculos_disponibles")
r.decr("stats:flota:vehiculos_mantenimiento")

# 3. Contadores de kilómetros
r.set("stats:km:total_historico", 2500000)
r.set("stats:km:hoy", 3450)
r.set("stats:km:mes:2025-11", 45680)
r.incrby("stats:km:hoy", 120)
r.incrby("stats:km:mes:2025-11", 120)
r.incrby("stats:km:total_historico", 120)
km_hoy = r.get("stats:km:hoy")

# 4. Contadores de ingresos (float)
r.set("stats:ingresos:2025-11-20", 0)
r.incrbyfloat("stats:ingresos:2025-11-20", 89.50)
r.incrbyfloat("stats:ingresos:2025-11-20", 145.00)
r.incrbyfloat("stats:ingresos:2025-11-20", 75.50)
ingresos_dia = r.get("stats:ingresos:2025-11-20")
r.set("stats:ingresos:2025-11", 45678.90)
r.incrbyfloat("stats:ingresos:2025-11", 89.50)
r.set("stats:ingresos:2025", 456789.45)
r.incrbyfloat("stats:ingresos:2025", 89.50)

# 5. Métricas por tipo de vehículo (hashes)
r.hset("stats:tipo:furgoneta", mapping={"total":25, "disponibles":18, "en_uso":5, "mantenimiento":2, "reservas_mes":145, "ingresos_mes":12890.50})
r.hset("stats:tipo:autobus", mapping={"total":15, "disponibles":12, "en_uso":2, "mantenimiento":1, "reservas_mes":67, "ingresos_mes":8934.00})
r.hset("stats:tipo:van", mapping={"total":10, "disponibles":8, "en_uso":3, "mantenimiento":0, "reservas_mes":89, "ingresos_mes":6234.75})
r.hincrby("stats:tipo:furgoneta", "en_uso", 1)
r.hincrby("stats:tipo:furgoneta", "disponibles", -1)
r.hincrby("stats:tipo:furgoneta", "reservas_mes", 1)
r.hincrbyfloat("stats:tipo:furgoneta", "ingresos_mes", 89.50)
furgoneta_metrics = r.hgetall("stats:tipo:furgoneta")
furgoneta_disponibles = r.hget("stats:tipo:furgoneta", "disponibles")

# 6. Métricas por ubicación/ciudad (hashes)
r.hset("stats:ciudad:madrid", mapping={"vehiculos":20, "disponibles":15, "en_uso":4, "reservas_hoy":8, "ingresos_hoy":678.50})
r.hset("stats:ciudad:barcelona", mapping={"vehiculos":15, "disponibles":10, "en_uso":4, "reservas_hoy":6, "ingresos_hoy":523.00})
r.hset("stats:ciudad:valencia", mapping={"vehiculos":10, "disponibles":8, "en_uso":2, "reservas_hoy":3, "ingresos_hoy":245.75})
r.hset("stats:ciudad:sevilla", mapping={"vehiculos":5, "disponibles":5, "en_uso":0, "reservas_hoy":0, "ingresos_hoy":0})
r.hincrby("stats:ciudad:madrid", "en_uso", 1)
r.hincrby("stats:ciudad:madrid", "disponibles", -1)
r.hincrby("stats:ciudad:madrid", "reservas_hoy", 1)
r.hincrbyfloat("stats:ciudad:madrid", "ingresos_hoy", 89.50)
ingresos_madrid = r.hget("stats:ciudad:madrid", "ingresos_hoy")
ingresos_barcelona = r.hget("stats:ciudad:barcelona", "ingresos_hoy")

# 7. Ranking de vehículos más rentables (sorted set)
r.zadd("ranking:vehiculos:ingresos", {"V001":4567.50, "V002":3892.00, "V003":5234.75, "V004":2890.30, "V005":6123.90})
top5_rentables = r.zrevrange("ranking:vehiculos:ingresos", 0, 4, withscores=True)
pos_v003 = r.zrevrank("ranking:vehiculos:ingresos", "V003")
r.zincrby("ranking:vehiculos:ingresos", 89.50, "V001")
vehiculos_4000 = r.zrangebyscore("ranking:vehiculos:ingresos", 4000, "+inf", withscores=True)

# 8. Ranking de vehículos más populares (sorted set)
r.zadd("ranking:vehiculos:popularidad", {"V001":45, "V002":38, "V003":52, "V004":31, "V005":41})
top10_populares = r.zrevrange("ranking:vehiculos:popularidad", 0, 9, withscores=True)
r.zincrby("ranking:vehiculos:popularidad", 1, "V001")
menos_populares = r.zrange("ranking:vehiculos:popularidad", 0, 4, withscores=True)

# 9. Ranking de clientes por gasto (sorted set)
r.zadd("ranking:clientes:gasto", {"C123":1234.50, "C456":2567.80, "C789":892.30, "C012":3456.90, "C345":567.25})
top10_clientes = r.zrevrange("ranking:clientes:gasto", 0, 9, withscores=True)
r.zincrby("ranking:clientes:gasto", 89.50, "C123")
clientes_vip = r.zrangebyscore("ranking:clientes:gasto", 2000, "+inf", withscores=True)
clientes_1000 = r.zcount("ranking:clientes:gasto", 1000, "+inf")

# 10. Métricas de rendimiento de conductores (hashes)
r.hset("driver:stats:D456", mapping={"nombre":"Carlos Ruiz", "servicios_completados":234, "km_recorridos":12560, "rating_promedio":4.8, "incidencias":2, "horas_trabajadas":856})
r.hset("driver:stats:D789", mapping={"nombre":"Ana Torres", "servicios_completados":189, "km_recorridos":9870, "rating_promedio":4.9, "incidencias":0, "horas_trabajadas":678})
r.hincrby("driver:stats:D456", "servicios_completados", 1)
r.hincrby("driver:stats:D456", "km_recorridos", 145)
r.hincrbyfloat("driver:stats:D456", "horas_trabajadas", 3.5)
rendimiento_d456 = r.hgetall("driver:stats:D456")

# 11. Contadores por tiempo (series temporales)
r.set("stats:reservas:hora:08", 3)
r.set("stats:reservas:hora:09", 7)
r.set("stats:reservas:hora:10", 12)
r.set("stats:reservas:hora:11", 15)
r.set("stats:reservas:hora:12", 18)
r.set("stats:reservas:hora:13", 14)
r.set("stats:reservas:hora:14", 16)
r.incr("stats:reservas:hora:10")
hora_pico = r.get("stats:reservas:hora:12")
r.set("stats:reservas:dia:lunes", 45)
r.set("stats:reservas:dia:martes", 38)
r.set("stats:reservas:dia:miercoles", 42)
r.set("stats:reservas:dia:jueves", 40)
r.set("stats:reservas:dia:viernes", 58)
r.set("stats:reservas:dia:sabado", 67)
r.set("stats:reservas:dia:domingo", 52)

# 12. Contadores de eventos (strings)
r.set("events:vehiculo:averia:total", 23)
r.set("events:vehiculo:revision:total", 156)
r.set("events:reserva:cancelacion:total", 47)
r.set("events:reserva:modificacion:total", 89)
r.set("events:cliente:registro:total", 892)
r.set("events:cliente:baja:total", 34)
r.incr("events:vehiculo:averia:total")
r.incr("events:reserva:cancelacion:total")
cancelaciones = r.get("events:reserva:cancelacion:total")
reservas_total = r.get("stats:reservas:total_historico")

# 13. Métricas de tiempo de respuesta
r.set("stats:tiempo:confirmacion:suma", 0)
r.set("stats:tiempo:confirmacion:count", 0)
r.incrby("stats:tiempo:confirmacion:suma", 45)
r.incr("stats:tiempo:confirmacion:count")
tiempo_suma = r.get("stats:tiempo:confirmacion:suma")
tiempo_count = r.get("stats:tiempo:confirmacion:count")

# 14. Métricas de ocupación (porcentajes)
r.set("stats:ocupacion:capacidad_total", 50)
r.set("stats:ocupacion:en_uso_actual", 12)
r.hset("stats:ocupacion:diaria:2025-11-20", mapping={
    "hora_08": 15, "hora_10": 24, "hora_12": 38, "hora_14": 42, "hora_16": 35, "hora_18": 28, "hora_20": 18
})
mejor_hora = r.hget("stats:ocupacion:diaria:2025-11-20", "hora_14")

# 15. Métricas de calidad (ratings)
r.set("stats:rating:suma_total", 2345.6)
r.set("stats:rating:num_ratings", 512)
r.incrbyfloat("stats:rating:suma_total", 5.0)
r.incr("stats:rating:num_ratings")
r.set("stats:rating:5_estrellas", 312)
r.set("stats:rating:4_estrellas", 145)
r.set("stats:rating:3_estrellas", 42)
r.set("stats:rating:2_estrellas", 11)
r.set("stats:rating:1_estrella", 2)
r.incr("stats:rating:5_estrellas")

# 16. Alertas y umbrales
r.set("threshold:vehiculos_disponibles:min", 10)
r.set("threshold:reservas_canceladas:max", 5)
r.set("threshold:ocupacion:min", 20)
vehiculos_disp = int(r.get("stats:flota:vehiculos_disponibles") or 0)
umbral_disp = int(r.get("threshold:vehiculos_disponibles:min") or 0)
r.set("alerts:vehiculos_bajo_stock:count", 0)
r.set("alerts:alta_cancelacion:count", 0)
if vehiculos_disp < umbral_disp:
    r.incr("alerts:vehiculos_bajo_stock:count")

# 17. Dashboard en tiempo real (hash consolidado)
r.hset("dashboard:realtime", mapping={
    "vehiculos_total": 50, "vehiculos_disponibles": 38, "vehiculos_en_uso": 10, "vehiculos_mantenimiento": 2,
    "reservas_activas": 10, "reservas_hoy": 8, "clientes_online": 45, "conductores_activos": 12,
    "ingresos_hoy": 678.50, "km_hoy": 3570, "rating_promedio": 4.58, "alertas_activas": 0
})
r.hset("dashboard:realtime", mapping={"vehiculos_disponibles": 37, "vehiculos_en_uso": 11})
r.hincrbyfloat("dashboard:realtime", "ingresos_hoy", 89.50)
dashboard = r.hgetall("dashboard:realtime")
dashboard_metrics = r.hmget("dashboard:realtime", "vehiculos_disponibles", "reservas_activas", "ingresos_hoy")

# 18. Reset de contadores diarios/mensuales
r.rename("stats:reservas:hoy", "stats:reservas:historico:2025-11-20")
r.rename("stats:ingresos:2025-11-20", "stats:ingresos:historico:2025-11-20")
r.rename("stats:km:hoy", "stats:km:historico:2025-11-20")
r.set("stats:reservas:hoy", 0)
r.set("stats:ingresos:2025-11-21", 0)
r.set("stats:km:hoy", 0)
