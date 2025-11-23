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
import time

r = redis.Redis(decode_responses=True)

# 1. Creación de reservas (hashes + expiración)
r.hset("reserva:R001", mapping={
    "vehiculo_id": "V001", "cliente_id": "C123", "cliente_nombre": "Juan García", "cliente_email": "juan@email.com",
    "fecha_inicio": "2025-11-20", "fecha_fin": "2025-11-23", "dias": 3, "precio_total": 268.50, "estado": "confirmada",
    "ubicacion_recogida": "Madrid Centro", "ubicacion_entrega": "Madrid Centro", "tipo_reserva": "mudanza"
})
r.expire("reserva:R001", 259200)
r.hset("reserva:R002", mapping={
    "vehiculo_id": "V002", "cliente_id": "C456", "cliente_nombre": "María López", "cliente_email": "maria@email.com",
    "fecha_inicio": "2025-11-21", "fecha_fin": "2025-11-21", "dias": 1, "precio_total": 145.00, "estado": "confirmada",
    "ubicacion_recogida": "Barcelona", "ubicacion_entrega": "Barcelona", "tipo_reserva": "excursion"
})
r.expire("reserva:R002", 86400)
r.hset("reserva:R003", mapping={
    "vehiculo_id": "V003", "cliente_id": "C789", "cliente_nombre": "Tech Solutions SL", "cliente_email": "info@techsol.com",
    "fecha_inicio": "2025-11-20", "fecha_fin": "2025-11-25", "dias": 5, "precio_total": 375.00, "estado": "activa",
    "ubicacion_recogida": "Valencia", "ubicacion_entrega": "Valencia", "tipo_reserva": "corporativa"
})
r.expire("reserva:R003", 432000)

# 2. Consultas de reservas
detalles_r001 = r.hgetall("reserva:R001")
info_basica_r001 = r.hmget("reserva:R001", "cliente_nombre", "vehiculo_id", "fecha_inicio", "fecha_fin", "estado")
estado_r001 = r.hget("reserva:R001", "estado")
ttl_r001 = r.ttl("reserva:R001")

# 3. Actualización de estado de reservas
r.hset("reserva:R001", mapping={"estado": "activa", "hora_recogida": "2025-11-20T09:30:00"})
r.hset("reserva:R001", mapping={"estado": "completada", "hora_devolucion": "2025-11-23T18:45:00", "km_recorridos": 450})
r.hset("reserva:R003", mapping={"ubicacion_actual": "Albacete", "ultima_actualizacion": "2025-11-21T14:20:00"})
r.hset("reserva:R002", mapping={"estado": "cancelada", "motivo_cancelacion": "Cliente enfermo", "fecha_cancelacion": "2025-11-20T16:00:00"})

# 4. Índice de reservas por cliente
r.sadd("cliente:C123:reservas", "R001")
r.sadd("cliente:C456:reservas", "R002")
r.sadd("cliente:C789:reservas", "R003")
reservas_c123 = r.smembers("cliente:C123:reservas")
r.srem("cliente:C123:reservas", "R001")

# 5. Índice de reservas por vehículo
r.sadd("vehiculo:V001:reservas", "R001")
r.sadd("vehiculo:V002:reservas", "R002")
r.sadd("vehiculo:V003:reservas", "R003")
reservas_v001 = r.smembers("vehiculo:V001:reservas")
num_reservas_v001 = r.scard("vehiculo:V001:reservas")

# 6. Contadores de reservas (strings)
r.set("stats:reservas:total", 3)
r.set("stats:reservas:activas", 2)
r.set("stats:reservas:completadas", 0)
r.set("stats:reservas:canceladas", 1)
r.set("stats:reservas:dia:2025-11-20", 3)
r.incr("stats:reservas:dia:2025-11-20")
r.get("stats:reservas:dia:2025-11-20")
r.set("stats:reservas:mes:2025-11", 15)
r.incr("stats:reservas:mes:2025-11")
r.incr("stats:reservas:total")
r.incr("stats:reservas:activas")
r.incr("stats:reservas:dia:2025-11-20")
r.decr("stats:reservas:activas")
r.incr("stats:reservas:completadas")

# 7. Lista de reservas pendientes de confirmación
r.lpush("cola:reservas:pendientes", "R004", "R005", "R006")
r.rpop("cola:reservas:pendientes")
pendientes = r.lrange("cola:reservas:pendientes", 0, -1)
num_pendientes = r.llen("cola:reservas:pendientes")

# 8. Reservas con extensión de tiempo
r.hset("reserva:R001", mapping={"fecha_fin": "2025-11-25", "dias": 5, "precio_total": 447.50, "extension": "true"})
r.expire("reserva:R001", 432000)
nuevo_ttl_r001 = r.ttl("reserva:R001")

# 9. Sistema de pre-reservas
r.hset("prereserva:PR001", mapping={
    "vehiculo_id": "V001", "cliente_id": "C999", "fecha_inicio": "2025-11-25", "fecha_fin": "2025-11-27",
    "precio_estimado": 179.00, "estado": "pendiente_pago"
})
r.expire("prereserva:PR001", 900)
prereserva = r.hgetall("prereserva:PR001")
r.hset("reserva:R010", mapping={
    "vehiculo_id": "V001", "cliente_id": "C999", "fecha_inicio": "2025-11-25", "fecha_fin": "2025-11-27",
    "dias": 2, "precio_total": 179.00, "estado": "confirmada"
})
r.expire("reserva:R010", 172800)
r.delete("prereserva:PR001")

# 10. Bloqueo de disponibilidad
r.set("bloqueo:vehiculo:V001", "R001", ex=259200)
existe_bloqueo = r.exists("bloqueo:vehiculo:V001")
bloqueo_valor = r.get("bloqueo:vehiculo:V001")
r.delete("bloqueo:vehiculo:V001")

# 11. Historial de reservas completadas
r.hset("historial:R001", mapping={
    "vehiculo_id": "V001", "cliente_id": "C123", "fecha_inicio": "2025-11-20", "fecha_fin": "2025-11-23",
    "precio_total": 268.50, "estado": "completada", "rating_cliente": 5, "comentario": "Excelente servicio"
})
r.sadd("historial:cliente:C123", "R001", "R007", "R015")
historial_c123 = r.smembers("historial:cliente:C123")

# 12. Reservas urgentes (priority queue)
r.zadd("cola:reservas:urgentes", {"R008": 1732099200, "R009": 1732102800, "R010": 1732106400})
urgente = r.zrange("cola:reservas:urgentes", 0, 0, withscores=True)
r.zpopmin("cola:reservas:urgentes")
urgentes_restantes = r.zrange("cola:reservas:urgentes", 0, -1, withscores=True)

# 13. Ingresos por reservas
r.set("stats:ingresos:2025-11-20", 0)
r.incrbyfloat("stats:ingresos:2025-11-20", 268.50)
r.incrbyfloat("stats:ingresos:2025-11-20", 145.00)
r.incrbyfloat("stats:ingresos:2025-11-20", 375.00)
total_dia = r.get("stats:ingresos:2025-11-20")
r.set("stats:ingresos:2025-11", 15234.75)
r.incrbyfloat("stats:ingresos:2025-11", 268.50)
r.set("stats:ingresos:2025", 142567.80)
r.incrbyfloat("stats:ingresos:2025", 268.50)

# 14. Notificaciones de reserva
r.sadd("notificaciones:R001", "confirmacion_enviada", "recordatorio_24h", "recordatorio_1h")
notificacion_enviada = r.sismember("notificaciones:R001", "confirmacion_enviada")
notificaciones_r001 = r.smembers("notificaciones:R001")

# 15. Gestión de expiración avanzada
mget_reservas = r.mget("reserva:R001", "reserva:R002", "reserva:R003")
r.persist("reserva:R001")
r.expire("reserva:R001", 86400)
ttl_r001_final = r.ttl("reserva:R001")
ttl_r999 = r.ttl("reserva:R999")
