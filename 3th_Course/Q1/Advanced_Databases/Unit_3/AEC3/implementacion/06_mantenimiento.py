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

# 2. Cola de mantenimiento urgente (LIFO)
r.lpush("queue:mantenimiento:urgente", "V023", "V019")
urgente = r.lpop("queue:mantenimiento:urgente")
cola_urgente = r.lrange("queue:mantenimiento:urgente", 0, -1)

# 3. Múltiples colas por tipo de servicio
r.rpush("queue:revisiones", "V008", "V015", "V022")
r.rpush("queue:reparaciones", "V011", "V017")
r.rpush("queue:limpieza", "V003", "V009", "V014", "V020")
r.rpush("queue:neumaticos", "V006", "V018")
r.lpop("queue:revisiones")
r.lpop("queue:reparaciones")
r.lpop("queue:limpieza")

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

# 5. Historial de mantenimientos (lists)
r.lpush("historial:V001:mantenimientos", '{"fecha":"2025-11-20","tipo":"revision","km":45150,"coste":385.50}')
r.lpush("historial:V001:mantenimientos", '{"fecha":"2025-09-15","tipo":"reparacion","km":42300,"coste":567.80}')
r.lpush("historial:V001:mantenimientos", '{"fecha":"2025-07-10","tipo":"revision","km":40000,"coste":320.00}')
ultimos5 = r.lrange("historial:V001:mantenimientos", 0, 4)
mas_reciente = r.lindex("historial:V001:mantenimientos", 0)
total_historial = r.llen("historial:V001:mantenimientos")
r.ltrim("historial:V001:mantenimientos", 0, 19)

# 6. Vehículos en mantenimiento activo (set)
r.sadd("vehiculos:en_mantenimiento", "V001", "V008", "V023")
en_mant_v001 = r.sismember("vehiculos:en_mantenimiento", "V001")
en_mant_v002 = r.sismember("vehiculos:en_mantenimiento", "V002")
todos_en_mant = r.smembers("vehiculos:en_mantenimiento")
cuantos_en_mant = r.scard("vehiculos:en_mantenimiento")
r.srem("vehiculos:en_mantenimiento", "V001")

# 7. Contador de días en mantenimiento
r.hset("stats:mantenimiento:dias", mapping={"V001":3, "V008":1, "V023":5, "V011":2, "V017":4})
dias_mant = r.hgetall("stats:mantenimiento:dias")
r.hincrby("stats:mantenimiento:dias", "V023", 1)

# 8. Costes de mantenimiento
r.hset("stats:mantenimiento:costes", mapping={"V001":1250.50, "V008":890.30, "V023":2567.80})
r.hincrbyfloat("stats:mantenimiento:costes", "V001", 385.50)
r.set("stats:mantenimiento:coste_mes:2025-11", 0)
r.incrbyfloat("stats:mantenimiento:coste_mes:2025-11", 385.50)
r.incrbyfloat("stats:mantenimiento:coste_mes:2025-11", 567.80)

# 9. Alertas de mantenimiento preventivo
r.zadd("alert:proxima_revision", {"V001":46000, "V008":33000, "V012":51000, "V015":48000})
pasados_limite = r.zrangebyscore("alert:proxima_revision", 50000, "+inf", withscores=True)
proximos_2000 = r.zrangebyscore("alert:proxima_revision", 45000, 47000, withscores=True)
r.zadd("alert:proxima_revision", {"V001":50000})

# 10. Priorización de mantenimiento
r.zadd("queue:mantenimiento:priorizado", {"V023":10, "V008":5, "V001":3, "V011":8, "V017":2})
mas_urgente = r.zrevrange("queue:mantenimiento:priorizado", 0, 0)
r.zpopmax("queue:mantenimiento:priorizado")
todos_priorizados = r.zrevrange("queue:mantenimiento:priorizado", 0, -1, withscores=True)

# 11. Bloqueo de vehículos en mantenimiento
r.set("bloqueo:vehiculo:V001:mantenimiento", "true", ex=86400)
bloqueo = r.get("bloqueo:vehiculo:V001:mantenimiento")
r.delete("bloqueo:vehiculo:V001:mantenimiento")

# 12. Mecánicos y sus colas de trabajo
r.rpush("mecanico:juanperez:cola", "V001", "V015", "V022")
r.rpush("mecanico:lauragomez:cola", "V023", "V011")
r.rpush("mecanico:carlosruiz:cola", "V008")
r.lpop("mecanico:juanperez:cola")
carga_juan = r.llen("mecanico:juanperez:cola")
carga_laura = r.llen("mecanico:lauragomez:cola")
carga_carlos = r.llen("mecanico:carlosruiz:cola")
r.rpoplpush("mecanico:lauragomez:cola", "mecanico:carlosruiz:cola")

# 13. Tiempo estimado de completación
r.hset("tiempo:estimado:mantenimiento", mapping={
    "revision":4, "reparacion":8, "ITV":2, "limpieza":3, "neumaticos":1.5, "diagnostico":2
})
tiempo_revision = r.hget("tiempo:estimado:mantenimiento", "revision")

# 14. Estadísticas de eficiencia
r.hset("stats:tiempo_promedio:mantenimiento", mapping={"revision":4.2, "reparacion":9.5, "ITV":1.8, "limpieza":2.9})
r.hset("stats:mantenimientos:completados", mapping={"revision":234, "reparacion":89, "ITV":156, "limpieza":203})
r.hincrby("stats:mantenimientos:completados", "revision", 1)
r.hincrbyfloat("stats:tiempo_promedio:mantenimiento", "revision", 0.1)

# 15. Notificaciones de mantenimiento
r.rpush("notifications:mantenimiento:pendientes", "V001:completado", "V023:diagnostico", "V008:en_proceso")
r.lpop("notifications:mantenimiento:pendientes")
r.sadd("notifications:mantenimiento:enviadas", "V001:completado")

# 16. Piezas y repuestos necesarios
r.rpush("mantenimiento:V001:piezas", "filtro_aceite", "aceite_5w30:5L", "filtro_aire", "pastillas_freno")
r.rpush("mantenimiento:V023:piezas", "correa_distribucion", "bomba_agua", "rodamiento")
piezas_v001 = r.lrange("mantenimiento:V001:piezas", 0, -1)
r.lrem("mantenimiento:V001:piezas", 1, "filtro_aceite")

# 17. Calendario de mantenimientos programados
r.zadd("calendario:mantenimiento", {"V001":1732147200, "V008":1732233600, "V015":1732320000, "V022":1732406400})
mantenimientos_semana = r.zrangebyscore("calendario:mantenimiento", 1732060800, 1732665600, withscores=True)
mantenimientos_hoy = r.zrangebyscore("calendario:mantenimiento", 1732147200, 1732233599)
atrasados = r.zrangebyscore("calendario:mantenimiento", 0, 1732012800)

# 18. Transfer entre colas
r.lrem("queue:mantenimiento:rutinario", 1, "V007")
r.lpush("queue:mantenimiento:urgente", "V007")
r.rpoplpush("queue:mantenimiento:rutinario", "queue:mantenimiento:urgente")

# 19. Cola bloqueante (para workers)
# r.blpop("queue:mantenimiento:rutinario", 0)  # Espera indefinidamente
# r.blpop("queue:mantenimiento:rutinario", 30) # Espera máximo 30 segundos
r.rpush("queue:mantenimiento:rutinario", "V025")

# 20. Orden de entrada (timestamp)
r.zadd("registro:entrada:mantenimiento", {"V001":1732099200, "V008":1732102800, "V023":1732106400})
orden_entrada = r.zrange("registro:entrada:mantenimiento", 0, -1, withscores=True)
mas_24h = r.zrangebyscore("registro:entrada:mantenimiento", 0, 1732012800)

# 21. Cleanup: datos temporales
r.delete("mantenimiento:V001")
r.delete("mantenimiento:V001:piezas")
r.srem("vehiculos:en_mantenimiento", "V001")
r.delete("bloqueo:vehiculo:V001:mantenimiento")
r.lpush("historial:V001:mantenimientos", '{"fecha":"2025-11-20","tipo":"revision","coste":385.50}')
