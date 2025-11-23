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

# 1. Ranking por popularidad (más reservados)
r.zadd("ranking:vehiculos:reservas_total", {
    "V001":156, "V002":143, "V003":189, "V004":98, "V005":167, "V006":134, "V007":201, "V008":112, "V009":145, "V010":178
})
top5_reservados = r.zrevrange("ranking:vehiculos:reservas_total", 0, 4, withscores=True)
pos_v004 = r.zrevrank("ranking:vehiculos:reservas_total", "V004")
r.zincrby("ranking:vehiculos:reservas_total", 1, "V004")
score_v004 = r.zscore("ranking:vehiculos:reservas_total", "V004")

# 2. Ranking por ingresos generados
r.zadd("ranking:vehiculos:ingresos", {
    "V001":23456.80, "V002":19872.50, "V003":28934.25, "V004":15678.90, "V005":24567.30
})
top3_ingresos = r.zrevrange("ranking:vehiculos:ingresos", 0, 2, withscores=True)
r.zincrby("ranking:vehiculos:ingresos", 125.50, "V004")
vehiculos_20k_30k = r.zrangebyscore("ranking:vehiculos:ingresos", 20000, 30000, withscores=True)
vehiculos_25k = r.zrangebyscore("ranking:vehiculos:ingresos", 25000, "+inf", withscores=True)
count_20k = r.zcount("ranking:vehiculos:ingresos", 20000, "+inf")

# 3. Ranking por rating/valoración
r.zadd("ranking:vehiculos:rating", {
    "V001":4.8, "V002":4.9, "V003":4.6, "V004":4.3, "V005":4.7, "V006":4.95, "V007":4.4, "V008":4.85
})
top5_rating = r.zrevrange("ranking:vehiculos:rating", 0, 4, withscores=True)
peor_valorados = r.zrange("ranking:vehiculos:rating", 0, 2, withscores=True)
rating_sup_45 = r.zrangebyscore("ranking:vehiculos:rating", 4.5, 5.0, withscores=True)
r.zadd("ranking:vehiculos:rating", {"V004":4.85})

# 4. Ranking por disponibilidad (días activos)
r.zadd("ranking:vehiculos:disponibilidad", {
    "V001":28, "V002":25, "V003":30, "V004":22, "V005":27, "V006":29, "V007":24
})
mas_disponibles = r.zrevrange("ranking:vehiculos:disponibilidad", 0, 4, withscores=True)
poco_disponibles = r.zrange("ranking:vehiculos:disponibilidad", 0, 2, withscores=True)

# 5. Ranking de clientes por fidelidad
r.zadd("ranking:clientes:reservas", {
    "C123":23, "C456":45, "C789":12, "C012":67, "C345":34, "C678":89, "C901":19
})
top10_fieles = r.zrevrange("ranking:clientes:reservas", 0, 9, withscores=True)
r.zincrby("ranking:clientes:reservas", 1, "C123")
clientes_vip = r.zrangebyscore("ranking:clientes:reservas", 50, "+inf", withscores=True)
nuevos_clientes = r.zrangebyscore("ranking:clientes:reservas", 0, 5, withscores=True)

# 6. Ranking de clientes por gasto total
r.zadd("ranking:clientes:gasto", {
    "C123":2456.90, "C456":5678.50, "C789":1234.75, "C012":8901.20, "C345":3456.80
})
top10_gasto = r.zrevrange("ranking:clientes:gasto", 0, 9, withscores=True)
r.zincrby("ranking:clientes:gasto", 189.50, "C123")
clientes_gold = r.zrangebyscore("ranking:clientes:gasto", 5000, "+inf", withscores=True)
clientes_platinum = r.zrangebyscore("ranking:clientes:gasto", 10000, "+inf", withscores=True)

# 7. Ranking de conductores por eficiencia
r.zadd("ranking:conductores:eficiencia", {
    "D456":12.5, "D789":11.8, "D012":13.2, "D345":10.9, "D678":12.9
})
mas_eficientes = r.zrevrange("ranking:conductores:eficiencia", 0, 4, withscores=True)
baja_eficiencia = r.zrange("ranking:conductores:eficiencia", 0, 2, withscores=True)

# 8. Ranking de conductores por valoración
r.zadd("ranking:conductores:rating", {
    "D456":4.9, "D789":4.7, "D012":4.95, "D345":4.6, "D678":4.85
})
mejores_conductores = r.zrevrange("ranking:conductores:rating", 0, 4, withscores=True)
conductores_bajo_47 = r.zrangebyscore("ranking:conductores:rating", 0, 4.7, withscores=True)

# 9. Ranking temporal: más reservados hoy
r.zadd("ranking:hoy:vehiculos:reservas", {
    "V001":3, "V002":5, "V003":2, "V004":4, "V005":6, "V006":1
})
populares_hoy = r.zrevrange("ranking:hoy:vehiculos:reservas", 0, 4, withscores=True)
r.zincrby("ranking:hoy:vehiculos:reservas", 1, "V003")
r.rename("ranking:hoy:vehiculos:reservas", "ranking:historico:2025-11-20:vehiculos:reservas")
r.zadd("ranking:hoy:vehiculos:reservas", {"V001":0, "V002":0, "V003":0})

# 10. Ranking por tiempo de respuesta
r.zadd("ranking:soporte:tiempo_respuesta", {
    "agente001":45, "agente002":38, "agente003":52, "agente004":41, "agente005":67
})
agentes_rapidos = r.zrange("ranking:soporte:tiempo_respuesta", 0, 4, withscores=True)
agentes_lentos = r.zrevrange("ranking:soporte:tiempo_respuesta", 0, 2, withscores=True)
r.zadd("ranking:soporte:tiempo_respuesta", {"agente001":40})

# 11. Ranking de ciudades por actividad
r.zadd("ranking:ciudades:reservas", {
    "Madrid":234, "Barcelona":189, "Valencia":156, "Sevilla":98, "Bilbao":123, "Málaga":87
})
top5_ciudades = r.zrevrange("ranking:ciudades:reservas", 0, 4, withscores=True)
ciudades_bajas = r.zrangebyscore("ranking:ciudades:reservas", 0, 100, withscores=True)
r.zincrby("ranking:ciudades:reservas", 1, "Sevilla")

# 12. Ranking por antigüedad de registro
r.zadd("ranking:clientes:antiguedad", {
    "C123":1609459200, "C456":1612137600, "C789":1614556800, "C012":1625097600
})
antiguos = r.zrange("ranking:clientes:antiguedad", 0, 9, withscores=True)
registrados_despues = r.zrangebyscore("ranking:clientes:antiguedad", 1620000000, "+inf", withscores=True)

# 13. Ranking combinado: score personalizado
r.zadd("ranking:vehiculos:score_total", {
    "V001":166.26, "V002":154.32, "V003":178.45, "V004":132.67
})
mejores_score = r.zrevrange("ranking:vehiculos:score_total", 0, 9, withscores=True)

# 14. Operaciones de rango avanzadas
r.zrevrange("ranking:vehiculos:ingresos", 5, 10, withscores=True)
r.zrange("ranking:vehiculos:ingresos", 0, -1, withscores=True)
total_vehiculos = r.zcard("ranking:vehiculos:ingresos")
r.zrem("ranking:vehiculos:ingresos", "V004")
r.zremrangebyscore("ranking:vehiculos:ingresos", 0, 10000)

# 15. Intersección de rankings
top10_pop = r.zrevrange("ranking:vehiculos:reservas_total", 0, 9)
top10_ing = r.zrevrange("ranking:vehiculos:ingresos", 0, 9)
r.zinterstore("ranking:vehiculos:combinado", ["ranking:vehiculos:reservas_total", "ranking:vehiculos:ingresos"], aggregate="SUM", weights=[1, 0.01])
r.zrevrange("ranking:vehiculos:combinado", 0, 9, withscores=True)

# 16. Unión de rankings
r.zadd("ranking:mes_pasado:reservas", {"V001":45, "V002":38, "V003":52})
r.zadd("ranking:mes_actual:reservas", {"V001":42, "V002":50, "V003":39})
r.zunionstore("ranking:total:dos_meses", ["ranking:mes_pasado:reservas", "ranking:mes_actual:reservas"])
r.zrevrange("ranking:total:dos_meses", 0, -1, withscores=True)

# 17. Ranking con límite temporal (TTL)
r.zadd("ranking:semana:vehiculos:reservas", {"V001":12, "V002":15, "V003":9})
r.expire("ranking:semana:vehiculos:reservas", 604800)

# 18. Ranking por incrementos fraccionarios
r.zadd("ranking:rating:dinamico", {"V001":4.5})
r.zincrby("ranking:rating:dinamico", 0.045, "V001")

# 19. Búsquedas por prefijo (lexicográfico)
r.zadd("ranking:vehiculos:alfabetico", {
    "Mercedes-Sprinter-V001":0, "Ford-Transit-V003":0, "Iveco-Daily-V002":0, "Renault-Master-V004":0
})
vehiculos_m = r.zrangebylex("ranking:vehiculos:alfabetico", "[M", "[N")
vehiculos_mercedes = r.zrangebylex("ranking:vehiculos:alfabetico", "[Mercedes", "[Mercedez")

# 20. Ranking con paginación
pagina1 = r.zrevrange("ranking:vehiculos:ingresos", 0, 9, withscores=True)
pagina2 = r.zrevrange("ranking:vehiculos:ingresos", 10, 19, withscores=True)
pagina3 = r.zrevrange("ranking:vehiculos:ingresos", 20, 29, withscores=True)
# Para página N, tamaño 10:
# start = (N - 1) * 10
# end = N * 10 - 1

# 21. Ranking de tendencias (velocidad de crecimiento)
r.zadd("ranking:tendencias:crecimiento", {
    "V001":4.0, "V002":2.1, "V003":5.0, "V004":1.5
})
tendencia_alza = r.zrevrange("ranking:tendencias:crecimiento", 0, 4, withscores=True)
crecimiento_3 = r.zrangebyscore("ranking:tendencias:crecimiento", 3.0, "+inf", withscores=True)
