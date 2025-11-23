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

# 1. Transacción básica: crear reserva
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("reserva:R100", mapping={"vehiculo_id":"V001", "cliente_id":"C123", "precio":89.50, "estado":"confirmada"})
    pipe.decr("stats:vehiculos:disponibles")
    pipe.incr("stats:reservas:activas")
    pipe.zincrby("ranking:vehiculos:popularidad", 1, "V001")
    pipe.incrbyfloat("stats:ingresos:2025-11-20", 89.50)
    result = pipe.execute()

# 2. Cancelar transacción (DISCARD)
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("reserva:R101", mapping={"vehiculo_id":"V002", "cliente_id":"C456", "precio":145.00})
    pipe.decr("stats:vehiculos:disponibles")
    pipe.incr("stats:reservas:activas")
    pipe.discard()

# 3. Transacción: completar reserva
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("reserva:R001", mapping={"estado":"completada", "fecha_fin":"2025-11-20T18:00:00"})
    pipe.incr("stats:vehiculos:disponibles")
    pipe.decr("stats:reservas:activas")
    pipe.hincrby("vehiculo:V001", "km_actuales", 150)
    pipe.delete("bloqueo:vehiculo:V001")
    pipe.execute()

# 4. Transacción: vehículo a mantenimiento
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("vehiculo:V005", mapping={"estado":"mantenimiento", "ubicacion":"Madrid Taller"})
    pipe.decr("stats:vehiculos:disponibles")
    pipe.incr("stats:vehiculos:mantenimiento")
    pipe.rpush("queue:mantenimiento:rutinario", "V005")
    pipe.sadd("vehiculos:en_mantenimiento", "V005")
    pipe.execute()

# 5. Transacción con WATCH (optimistic locking)
with r.pipeline() as pipe:
    while True:
        try:
            pipe.watch("vehiculo:V001")
            # estado = r.hget("vehiculo:V001", "estado")
            # if estado != "disponible":
            #     pipe.unwatch()
            #     break
            pipe.multi()
            pipe.hset("reserva:R102", mapping={"vehiculo_id":"V001", "cliente_id":"C123", "estado":"confirmada"})
            pipe.hset("vehiculo:V001", "estado", "en_uso")
            pipe.decr("stats:vehiculos:disponibles")
            result = pipe.execute()
            break
        except redis.WatchError:
            continue

# 6. Transacción: actualizar múltiples métricas
with r.pipeline() as pipe:
    pipe.multi()
    pipe.incr("stats:reservas:dia:2025-11-20")
    pipe.incr("stats:reservas:mes:2025-11")
    pipe.incr("stats:reservas:total_historico")
    pipe.hincrby("stats:ciudad:madrid", "reservas_hoy", 1)
    pipe.hincrby("stats:tipo:furgoneta", "reservas_mes", 1)
    pipe.execute()

# 7. Transacción: cambio de estado complejo
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("vehiculo:V005", mapping={"estado":"disponible", "ubicacion":"Madrid Centro"})
    pipe.incr("stats:vehiculos:disponibles")
    pipe.decr("stats:vehiculos:mantenimiento")
    pipe.lpop("queue:mantenimiento:rutinario")
    pipe.srem("vehiculos:en_mantenimiento", "V005")
    pipe.delete("mantenimiento:V005")
    pipe.lpush("historial:V005:mantenimientos", '{"fecha":"2025-11-20","tipo":"revision","coste":385.50}')
    pipe.execute()

# 8. Pipelining (optimización de red)
with r.pipeline() as pipe:
    pipe.set("key1", "value1")
    pipe.set("key2", "value2")
    pipe.set("key3", "value3")
    pipe.incr("counter")
    pipe.get("key1")
    pipe.execute()

# 9. Combinación: pipeline + transacción
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("reserva:R103", mapping={"vehiculo_id":"V002", "cliente_id":"C789", "precio":145.00})
    pipe.decr("stats:vehiculos:disponibles")
    pipe.incr("stats:reservas:activas")
    pipe.execute()

# 10. Transacción: transferencia de puntos/créditos
with r.pipeline() as pipe:
    while True:
        try:
            pipe.watch("user:C123:puntos", "user:C456:puntos")
            # puntos = int(r.get("user:C123:puntos") or 0)
            # if puntos < 50:
            #     pipe.unwatch()
            #     break
            pipe.multi()
            pipe.decrby("user:C123:puntos", 50)
            pipe.incrby("user:C456:puntos", 50)
            pipe.lpush("transacciones:puntos", '{"de":"C123","a":"C456","cantidad":50,"fecha":"2025-11-20"}')
            pipe.execute()
            break
        except redis.WatchError:
            continue

# 11. Transacción: crear sesión y actualizar contadores
with r.pipeline() as pipe:
    pipe.multi()
    pipe.setex("session:user:xyz789", 1800, '{"user_id":"C123","login":"2025-11-20T10:00:00"}')
    pipe.sadd("user:C123:sessions", "session:user:xyz789")
    pipe.incr("stats:sesiones:clientes:activas")
    pipe.incr("stats:logins:2025-11-20")
    pipe.lpush("audit:logins:C123", '{"timestamp":"2025-11-20T10:00:00","ip":"192.168.1.50"}')
    pipe.execute()

# 12. Transacción: cancelar reserva con reembolso
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("reserva:R050", mapping={"estado":"cancelada", "motivo":"Cliente cambió planes"})
    pipe.incr("stats:vehiculos:disponibles")
    pipe.decr("stats:reservas:activas")
    pipe.incr("stats:reservas:canceladas")
    pipe.hset("vehiculo:V003", "estado", "disponible")
    pipe.delete("bloqueo:vehiculo:V003")
    pipe.incrbyfloat("user:C123:credito", 89.50)
    pipe.execute()

# 13. WATCH múltiples claves
with r.pipeline() as pipe:
    while True:
        try:
            pipe.watch("vehiculo:V001", "stats:vehiculos:disponibles", "reserva:R104")
            pipe.multi()
            # ... operaciones
            pipe.execute()
            break
        except redis.WatchError:
            continue

# 14. Patrón: retry con WATCH (ver ejemplo en comentario)
# while True:
#     with r.pipeline() as pipe:
#         try:
#             pipe.watch("vehiculo:V001")
#             estado = r.hget("vehiculo:V001", "estado")
#             if estado != "disponible":
#                 pipe.unwatch()
#                 break
#             pipe.multi()
#             pipe.hset("reserva:R105", ...)
#             pipe.hset("vehiculo:V001", "estado", "en_uso")
#             pipe.execute()
#             break
#         except redis.WatchError:
#             continue

# 15. Transacción: actualizar ranking múltiple
with r.pipeline() as pipe:
    pipe.multi()
    pipe.zincrby("ranking:vehiculos:reservas_total", 1, "V001")
    pipe.zincrby("ranking:vehiculos:ingresos", 89.50, "V001")
    pipe.zadd("ranking:vehiculos:ultima_actividad", {"V001":1732099200})
    pipe.zincrby("ranking:clientes:reservas", 1, "C123")
    pipe.zincrby("ranking:clientes:gasto", 89.50, "C123")
    pipe.execute()

# 16. Transacción: batch update de múltiples vehículos
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("vehiculo:V001", "precio_dia", 95.00)
    pipe.hset("vehiculo:V002", "precio_dia", 150.00)
    pipe.hset("vehiculo:V003", "precio_dia", 80.00)
    pipe.hset("vehiculo:V004", "precio_dia", 85.00)
    pipe.hset("vehiculo:V005", "precio_dia", 190.00)
    pipe.execute()

# 17. Errores en transacciones (comentado, para referencia)
# with r.pipeline() as pipe:
#     pipe.multi()
#     pipe.set("key", "value")
#     pipe.set("key")  # ERROR: falta el valor
#     pipe.incr("counter")
#     pipe.execute()
# with r.pipeline() as pipe:
#     pipe.multi()
#     pipe.set("key", "value")
#     pipe.incr("key")  # ERROR: key no es un número
#     pipe.set("otro", "valor")
#     pipe.execute()

# 18. Transacción: limpieza de datos temporales
with r.pipeline() as pipe:
    pipe.multi()
    pipe.delete("session:user:abc123")
    pipe.delete("prereserva:PR001")
    pipe.delete("cache:vehiculo:V001")
    pipe.srem("user:C123:sessions", "session:user:abc123")
    pipe.decr("stats:sesiones:clientes:activas")
    pipe.execute()

# 19. Pipelining: consultas masivas
with r.pipeline() as pipe:
    for vid in ["V001", "V002", "V003", "V004", "V005", "V006", "V007", "V008", "V009", "V010"]:
        pipe.hgetall(f"vehiculo:{vid}")
    vehiculos_info = pipe.execute()

# 20. Transacción: operación idempotente
with r.pipeline() as pipe:
    while True:
        try:
            pipe.watch("reserva:R106")
            # exists = r.exists("reserva:R106")
            pipe.multi()
            pipe.hset("reserva:R106", mapping={"vehiculo_id":"V001", "cliente_id":"C123", "precio":89.50})
            # ... más operaciones
            pipe.execute()
            break
        except redis.WatchError:
            continue

# 21. Transacción compleja: flujo completo de reserva
with r.pipeline() as pipe:
    while True:
        try:
            pipe.watch("vehiculo:V001", "stats:vehiculos:disponibles")
            # ...verificaciones...
            # estado = r.hget("vehiculo:V001", "estado")
            pipe.multi()
            pipe.hset("reserva:R200", mapping={
                "vehiculo_id":"V001", "cliente_id":"C123", "fecha_inicio":"2025-11-21", "fecha_fin":"2025-11-23",
                "precio":268.50, "estado":"confirmada"
            })
            pipe.expire("reserva:R200", 259200)
            pipe.hset("vehiculo:V001", "estado", "en_uso")
            pipe.decr("stats:vehiculos:disponibles")
            pipe.incr("stats:vehiculos:en_uso")
            pipe.incr("stats:reservas:activas")
            pipe.incr("stats:reservas:dia:2025-11-20")
            pipe.incr("stats:reservas:mes:2025-11")
            pipe.sadd("vehiculo:V001:reservas", "R200")
            pipe.sadd("cliente:C123:reservas", "R200")
            pipe.set("bloqueo:vehiculo:V001", "R200", ex=259200)
            pipe.zincrby("ranking:vehiculos:popularidad", 1, "V001")
            pipe.zincrby("ranking:vehiculos:ingresos", 268.50, "V001")
            pipe.zincrby("ranking:clientes:reservas", 1, "C123")
            pipe.zincrby("ranking:clientes:gasto", 268.50, "C123")
            pipe.incrbyfloat("stats:ingresos:2025-11-20", 268.50)
            pipe.incrbyfloat("stats:ingresos:2025-11", 268.50)
            pipe.lpush("events:reservas:log", '{"reserva":"R200","cliente":"C123","vehiculo":"V001","timestamp":"2025-11-20T10:30:00"}')
            pipe.ltrim("events:reservas:log", 0, 999)
            pipe.execute()
            break
        except redis.WatchError:
            continue
