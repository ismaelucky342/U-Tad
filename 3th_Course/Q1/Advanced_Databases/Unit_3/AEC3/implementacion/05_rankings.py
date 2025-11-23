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
print("\n=== RANKING POPULARIDAD (RESERVAS) ===")
print("Top 5 reservados:", top5_reservados)
print("Posición V004:", pos_v004)
print("Score V004 tras incremento:", score_v004)

# 2. Ranking por ingresos generados
r.zadd("ranking:vehiculos:ingresos", {
    "V001":23456.80, "V002":19872.50, "V003":28934.25, "V004":15678.90, "V005":24567.30
})
top3_ingresos = r.zrevrange("ranking:vehiculos:ingresos", 0, 2, withscores=True)
r.zincrby("ranking:vehiculos:ingresos", 125.50, "V004")
vehiculos_20k_30k = r.zrangebyscore("ranking:vehiculos:ingresos", 20000, 30000, withscores=True)
vehiculos_25k = r.zrangebyscore("ranking:vehiculos:ingresos", 25000, "+inf", withscores=True)
count_20k = r.zcount("ranking:vehiculos:ingresos", 20000, "+inf")
print("\n=== RANKING INGRESOS ===")
print("Top 3 ingresos:", top3_ingresos)
print(">=20k y <=30k:", vehiculos_20k_30k)
print(">=25k:", vehiculos_25k)
print("Nº >=20k:", count_20k)

# 3. Ranking por rating/valoración
r.zadd("ranking:vehiculos:rating", {
    "V001":4.8, "V002":4.9, "V003":4.6, "V004":4.3, "V005":4.7, "V006":4.95, "V007":4.4, "V008":4.85
})
top5_rating = r.zrevrange("ranking:vehiculos:rating", 0, 4, withscores=True)
peor_valorados = r.zrange("ranking:vehiculos:rating", 0, 2, withscores=True)
rating_sup_45 = r.zrangebyscore("ranking:vehiculos:rating", 4.5, 5.0, withscores=True)
r.zadd("ranking:vehiculos:rating", {"V004":4.85})
print("\n=== RANKING RATING ===")
print("Top 5 rating:", top5_rating)
print("Peor valorados:", peor_valorados)
print("Rating >4.5:", rating_sup_45)

# 4. Ranking por disponibilidad (días activos)
r.zadd("ranking:vehiculos:disponibilidad", {
    "V001":28, "V002":25, "V003":30, "V004":22, "V005":27, "V006":29, "V007":24
})
mas_disponibles = r.zrevrange("ranking:vehiculos:disponibilidad", 0, 4, withscores=True)
poco_disponibles = r.zrange("ranking:vehiculos:disponibilidad", 0, 2, withscores=True)
print("\n=== RANKING DISPONIBILIDAD ===")
print("Más disponibles:", mas_disponibles)
print("Menos disponibles:", poco_disponibles)

# 5. Ranking de clientes por fidelidad
r.zadd("ranking:clientes:reservas", {
    "C123":23, "C456":45, "C789":12, "C012":67, "C345":34, "C678":89, "C901":19
})
top10_fieles = r.zrevrange("ranking:clientes:reservas", 0, 9, withscores=True)
r.zincrby("ranking:clientes:reservas", 1, "C123")
clientes_vip = r.zrangebyscore("ranking:clientes:reservas", 50, "+inf", withscores=True)
nuevos_clientes = r.zrangebyscore("ranking:clientes:reservas", 0, 5, withscores=True)
print("\n=== RANKING CLIENTES FIELES ===")
print("Top 10 fieles:", top10_fieles)
print("VIPs (>50 reservas):", clientes_vip)
print("Nuevos clientes (<=5):", nuevos_clientes)

# 6. Ranking de clientes por gasto total
r.zadd("ranking:clientes:gasto", {
    "C123":2456.90, "C456":5678.50, "C789":1234.75, "C012":8901.20, "C345":3456.80
})
top10_gasto = r.zrevrange("ranking:clientes:gasto", 0, 9, withscores=True)
r.zincrby("ranking:clientes:gasto", 189.50, "C123")
clientes_gold = r.zrangebyscore("ranking:clientes:gasto", 5000, "+inf", withscores=True)
clientes_platinum = r.zrangebyscore("ranking:clientes:gasto", 10000, "+inf", withscores=True)
print("\n=== RANKING CLIENTES POR GASTO ===")
print("Top 10 gasto:", top10_gasto)
print("Gold (>5000):", clientes_gold)
print("Platinum (>10000):", clientes_platinum)

# 7. Ranking de conductores por eficiencia
r.zadd("ranking:conductores:eficiencia", {
    "D456":12.5, "D789":11.8, "D012":13.2, "D345":10.9, "D678":12.9
})
mas_eficientes = r.zrevrange("ranking:conductores:eficiencia", 0, 4, withscores=True)
baja_eficiencia = r.zrange("ranking:conductores:eficiencia", 0, 2, withscores=True)
print("\n=== RANKING CONDUCTORES EFICIENCIA ===")
print("Más eficientes:", mas_eficientes)
print("Menos eficientes:", baja_eficiencia)

# 8. Ranking de conductores por valoración
r.zadd("ranking:conductores:rating", {
    "D456":4.9, "D789":4.7, "D012":4.95, "D345":4.6, "D678":4.85
})
mejores_conductores = r.zrevrange("ranking:conductores:rating", 0, 4, withscores=True)
conductores_bajo_47 = r.zrangebyscore("ranking:conductores:rating", 0, 4.7, withscores=True)
print("\n=== RANKING CONDUCTORES VALORACIÓN ===")
print("Mejores conductores:", mejores_conductores)
print("Bajo 4.7:", conductores_bajo_47)

# 9. Ranking temporal: más reservados hoy
r.zadd("ranking:hoy:vehiculos:reservas", {
    "V001":3, "V002":5, "V003":2, "V004":4, "V005":6, "V006":1
})
populares_hoy = r.zrevrange("ranking:hoy:vehiculos:reservas", 0, 4, withscores=True)
r.zincrby("ranking:hoy:vehiculos:reservas", 1, "V003")
r.rename("ranking:hoy:vehiculos:reservas", "ranking:historico:2025-11-20:vehiculos:reservas")
r.zadd("ranking:hoy:vehiculos:reservas", {"V001":0, "V002":0, "V003":0})
print("\n=== RANKING HOY (TEMPORAL) ===")
print("Populares hoy:", populares_hoy)

# 10. Ranking por tiempo de respuesta
r.zadd("ranking:soporte:tiempo_respuesta", {
    "agente001":45, "agente002":38, "agente003":52, "agente004":41, "agente005":67
})
agentes_rapidos = r.zrange("ranking:soporte:tiempo_respuesta", 0, 4, withscores=True)
agentes_lentos = r.zrevrange("ranking:soporte:tiempo_respuesta", 0, 2, withscores=True)
r.zadd("ranking:soporte:tiempo_respuesta", {"agente001":40})
print("\n=== RANKING SOPORTE (TIEMPO RESPUESTA) ===")
print("Agentes rápidos:", agentes_rapidos)
print("Agentes lentos:", agentes_lentos)

