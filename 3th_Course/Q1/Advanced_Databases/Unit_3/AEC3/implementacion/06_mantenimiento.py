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

# 1. Cola de mantenimiento rutinario (FIFO)
r.rpush("queue:mantenimiento:rutinario", "V001", "V005", "V007", "V012")
cola_rutinario = r.lrange("queue:mantenimiento:rutinario", 0, -1)
pendientes_rutinario = r.llen("queue:mantenimiento:rutinario")
siguiente_rutinario = r.lpop("queue:mantenimiento:rutinario")
proximos3 = r.lrange("queue:mantenimiento:rutinario", 0, 2)
print("\n=== MANTENIMIENTO RUTINARIO (FIFO) ===")
print("Cola actual:", cola_rutinario)
print("Pendientes:", pendientes_rutinario)
print("Siguiente:", siguiente_rutinario)
print("Próximos 3:", proximos3)

# 2. Cola de mantenimiento urgente (LIFO)
r.lpush("queue:mantenimiento:urgente", "V023", "V019")
urgente = r.lpop("queue:mantenimiento:urgente")
cola_urgente = r.lrange("queue:mantenimiento:urgente", 0, -1)
print("\n=== MANTENIMIENTO URGENTE (LIFO) ===")
print("Atendido urgente:", urgente)
print("Cola urgente actual:", cola_urgente)

# 3. Múltiples colas por tipo de servicio
r.rpush("queue:revisiones", "V008", "V015", "V022")
r.rpush("queue:reparaciones", "V011", "V017")
r.rpush("queue:limpieza", "V003", "V009", "V014", "V020")
r.rpush("queue:neumaticos", "V006", "V018")
r.lpop("queue:revisiones")
r.lpop("queue:reparaciones")
r.lpop("queue:limpieza")
print("\n=== COLAS POR TIPO DE SERVICIO ===")
print("Revisiones:", r.lrange("queue:revisiones", 0, -1))
print("Reparaciones:", r.lrange("queue:reparaciones", 0, -1))
print("Limpieza:", r.lrange("queue:limpieza", 0, -1))
print("Neumáticos:", r.lrange("queue:neumaticos", 0, -1))

# 4. Información detallada de mantenimiento (hashes)
r.hset("mantenimiento:V001", mapping={
    "vehiculo_id":"V001", "tipo":"revision_programada", "fecha_entrada":"2025-11-20T09:00:00", "km_actuales":45150,
    "descripcion":"Revisión 45.000 km", "prioridad":"normal", "mecanico_asignado":"Juan Pérez", "estado":"en_proceso", "coste_estimado":350.00
})
r.hset("mantenimiento:V023", mapping={
    "vehiculo_id":"V023", "tipo":"averia", "fecha_entrada":"2025-11-20T14:30:00", "km_actuales":67890,
    "descripcion":"Motor hace ruido extraño", "prioridad":"urgente", "mecanico_asignado":"Laura Gómez", "estado":"diagnostico", "coste_estimado":0
})
r.hset("mantenimiento:V008", mapping={
    "vehiculo_id":"V008", "tipo":"ITV", "fecha_entrada":"2025-11-20T08:00:00", "km_actuales":32000,
    "descripcion":"ITV anual", "prioridad":"normal", "mecanico_asignado":"Carlos Ruiz", "estado":"pendiente", "coste_estimado":45.00
})
info_v001 = r.hgetall("mantenimiento:V001")
r.hset("mantenimiento:V001", mapping={
    "estado":"completado", "fecha_salida":"2025-11-20T16:30:00", "coste_real":385.50, "observaciones":"Todo OK. Cambiados filtros y aceite"
})
print("\n=== INFO DETALLADA DE MANTENIMIENTO ===")
print("V001:", info_v001)
print("V023:", r.hgetall("mantenimiento:V023"))
print("V008:", r.hgetall("mantenimiento:V008"))

# 5. Historial de mantenimientos (lists)
r.lpush("historial:V001:mantenimientos", '{"fecha":"2025-11-20","tipo":"revision","km":45150,"coste":385.50}')
r.lpush("historial:V001:mantenimientos", '{"fecha":"2025-09-15","tipo":"reparacion","km":42300,"coste":567.80}')
r.lpush("historial:V001:mantenimientos", '{"fecha":"2025-07-10","tipo":"revision","km":40000,"coste":320.00}')
ultimos5 = r.lrange("historial:V001:mantenimientos", 0, 4)
mas_reciente = r.lindex("historial:V001:mantenimientos", 0)
total_historial = r.llen("historial:V001:mantenimientos")
r.ltrim("historial:V001:mantenimientos", 0, 19)
print("\n=== HISTORIAL DE MANTENIMIENTOS ===")
print("Últimos 5:", ultimos5)
print("Más reciente:", mas_reciente)
print("Total historial:", total_historial)

# 6. Vehículos en mantenimiento activo (set)
r.sadd("vehiculos:en_mantenimiento", "V001", "V008", "V023")
en_mant_v001 = r.sismember("vehiculos:en_mantenimiento", "V001")
en_mant_v002 = r.sismember("vehiculos:en_mantenimiento", "V002")
todos_en_mant = r.smembers("vehiculos:en_mantenimiento")
cuantos_en_mant = r.scard("vehiculos:en_mantenimiento")
r.srem("vehiculos:en_mantenimiento", "V001")
print("\n=== VEHÍCULOS EN MANTENIMIENTO ACTIVO ===")
print("V001 en mantenimiento:", en_mant_v001)
print("V002 en mantenimiento:", en_mant_v002)
print("Todos en mantenimiento:", todos_en_mant)
print("Cuántos en mantenimiento:", cuantos_en_mant)

# 7. Contador de días en mantenimiento
r.hset("stats:mantenimiento:dias", mapping={"V001":3, "V008":1, "V023":5, "V011":2, "V017":4})
dias_mant = r.hgetall("stats:mantenimiento:dias")
r.hincrby("stats:mantenimiento:dias", "V023", 1)
print("\n=== DÍAS EN MANTENIMIENTO ===")
print("Días por vehículo:", dias_mant)

# 8. Costes de mantenimiento
r.hset("stats:mantenimiento:costes", mapping={"V001":1250.50, "V008":890.30, "V023":2567.80})
r.hincrbyfloat("stats:mantenimiento:costes", "V001", 385.50)
r.set("stats:mantenimiento:coste_mes:2025-11", 0)
r.incrbyfloat("stats:mantenimiento:coste_mes:2025-11", 385.50)
r.incrbyfloat("stats:mantenimiento:coste_mes:2025-11", 567.80)
print("\n=== COSTES DE MANTENIMIENTO ===")
print("Costes por vehículo:", r.hgetall("stats:mantenimiento:costes"))
print("Coste mes 2025-11:", r.get("stats:mantenimiento:coste_mes:2025-11"))

# 9. Alertas de mantenimiento preventivo
r.zadd("alert:proxima_revision", {"V001":46000, "V008":33000, "V012":51000, "V015":48000})
pasados_limite = r.zrangebyscore("alert:proxima_revision", 50000, "+inf", withscores=True)
proximos_2000 = r.zrangebyscore("alert:proxima_revision", 45000, 47000, withscores=True)
r.zadd("alert:proxima_revision", {"V001":50000})
print("\n=== ALERTAS DE MANTENIMIENTO PREVENTIVO ===")
print(">50.000 km:", pasados_limite)
print("Próximos a revisión (45-47k):", proximos_2000)

# 10. Priorización de mantenimiento
r.zadd("queue:mantenimiento:priorizado", {"V023":10, "V008":5, "V001":3, "V011":8, "V017":2})
mas_urgente = r.zrevrange("queue:mantenimiento:priorizado", 0, 0)
r.zpopmax("queue:mantenimiento:priorizado")
todos_priorizados = r.zrevrange("queue:mantenimiento:priorizado", 0, -1, withscores=True)
print("\n=== PRIORIZACIÓN DE MANTENIMIENTO ===")
print("Más urgente:", mas_urgente)
print("Todos priorizados:", todos_priorizados)
