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
print("\n=== TRANSACCIÓN: CREAR RESERVA ===")
print("Reserva R100:", r.hgetall("reserva:R100"))

# 2. Cancelar transacción (DISCARD)
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("reserva:R101", mapping={"vehiculo_id":"V002", "cliente_id":"C456", "precio":145.00})
    pipe.decr("stats:vehiculos:disponibles")
    pipe.incr("stats:reservas:activas")
    pipe.discard()
print("\n=== TRANSACCIÓN CANCELADA (DISCARD) ===")
print("Reserva R101 existe:", r.exists("reserva:R101"))

# 3. Transacción: completar reserva
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("reserva:R001", mapping={"estado":"completada", "fecha_fin":"2025-11-20T18:00:00"})
    pipe.incr("stats:vehiculos:disponibles")
    pipe.decr("stats:reservas:activas")
    pipe.hincrby("vehiculo:V001", "km_actuales", 150)
    pipe.delete("bloqueo:vehiculo:V001")
    pipe.execute()
print("\n=== TRANSACCIÓN: COMPLETAR RESERVA ===")
print("Reserva R001:", r.hgetall("reserva:R001"))

# 4. Transacción: vehículo a mantenimiento
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("vehiculo:V005", mapping={"estado":"mantenimiento", "ubicacion":"Madrid Taller"})
    pipe.decr("stats:vehiculos:disponibles")
    pipe.incr("stats:vehiculos:mantenimiento")
    pipe.rpush("queue:mantenimiento:rutinario", "V005")
    pipe.sadd("vehiculos:en_mantenimiento", "V005")
    pipe.execute()
print("\n=== TRANSACCIÓN: VEHÍCULO A MANTENIMIENTO ===")
print("Vehículo V005:", r.hgetall("vehiculo:V005"))

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
print("\n=== TRANSACCIÓN CON WATCH ===")
print("Reserva R102:", r.hgetall("reserva:R102"))

# 6. Transacción: actualizar múltiples métricas
with r.pipeline() as pipe:
    pipe.multi()
    pipe.incr("stats:reservas:dia:2025-11-20")
    pipe.incr("stats:reservas:mes:2025-11")
    pipe.incr("stats:reservas:total_historico")
    pipe.hincrby("stats:ciudad:madrid", "reservas_hoy", 1)
    pipe.hincrby("stats:tipo:furgoneta", "reservas_mes", 1)
    pipe.execute()
print("\n=== TRANSACCIÓN: ACTUALIZAR MÉTRICAS ===")
print("Reservas hoy:", r.get("stats:reservas:dia:2025-11-20"))
print("Reservas mes:", r.get("stats:reservas:mes:2025-11"))
print("Total histórico:", r.get("stats:reservas:total_historico"))

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
print("\n=== TRANSACCIÓN: CAMBIO DE ESTADO COMPLEJO ===")
print("Vehículo V005:", r.hgetall("vehiculo:V005"))

# 8. Pipelining (optimización de red)
with r.pipeline() as pipe:
    pipe.set("key1", "value1")
    pipe.set("key2", "value2")
    pipe.set("key3", "value3")
    pipe.incr("counter")
    pipe.get("key1")
    pipe.execute()
print("\n=== PIPELINING ===")
print("key1:", r.get("key1"))
print("key2:", r.get("key2"))
print("key3:", r.get("key3"))
print("counter:", r.get("counter"))

# 9. Combinación: pipeline + transacción
with r.pipeline() as pipe:
    pipe.multi()
    pipe.hset("reserva:R103", mapping={"vehiculo_id":"V002", "cliente_id":"C789", "precio":145.00})
    pipe.decr("stats:vehiculos:disponibles")
    pipe.incr("stats:reservas:activas")
    pipe.execute()
print("\n=== PIPELINE + TRANSACCIÓN ===")
print("Reserva R103:", r.hgetall("reserva:R103"))

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
print("\n=== TRANSACCIÓN: TRANSFERENCIA DE PUNTOS ===")
print("Puntos C123:", r.get("user:C123:puntos"))
print("Puntos C456:", r.get("user:C456:puntos"))
print("Última transacción:", r.lindex("transacciones:puntos", 0))

