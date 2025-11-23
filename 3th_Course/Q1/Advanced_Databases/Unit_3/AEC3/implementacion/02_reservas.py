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
print("\n=== CREACIÓN DE RESERVAS ===")
for rid in ["R001", "R002", "R003"]:
    print(f"Reserva {rid}: {r.hgetall(f'reserva:{rid}')}")

# 2. Consultas de reservas
detalles_r001 = r.hgetall("reserva:R001")
info_basica_r001 = r.hmget("reserva:R001", "cliente_nombre", "vehiculo_id", "fecha_inicio", "fecha_fin", "estado")
estado_r001 = r.hget("reserva:R001", "estado")
ttl_r001 = r.ttl("reserva:R001")
print("\n=== CONSULTAS ===")
print("Detalles R001:", detalles_r001)
print("Info básica R001:", info_basica_r001)
print("Estado R001:", estado_r001)
print("TTL R001:", ttl_r001)

# 3. Actualización de estado de reservas
r.hset("reserva:R001", mapping={"estado": "activa", "hora_recogida": "2025-11-20T09:30:00"})
r.hset("reserva:R001", mapping={"estado": "completada", "hora_devolucion": "2025-11-23T18:45:00", "km_recorridos": 450})
r.hset("reserva:R003", mapping={"ubicacion_actual": "Albacete", "ultima_actualizacion": "2025-11-21T14:20:00"})
r.hset("reserva:R002", mapping={"estado": "cancelada", "motivo_cancelacion": "Cliente enfermo", "fecha_cancelacion": "2025-11-20T16:00:00"})
print("\n=== ACTUALIZACIONES ===")
print("R001 tras actualización:", r.hgetall("reserva:R001"))
print("R002 tras actualización:", r.hgetall("reserva:R002"))
print("R003 tras actualización:", r.hgetall("reserva:R003"))

# 4. Índice de reservas por cliente
r.sadd("cliente:C123:reservas", "R001")
r.sadd("cliente:C456:reservas", "R002")
r.sadd("cliente:C789:reservas", "R003")
reservas_c123 = r.smembers("cliente:C123:reservas")
r.srem("cliente:C123:reservas", "R001")
print("\n=== ÍNDICE POR CLIENTE ===")
print("Reservas de C123 antes de borrar:", reservas_c123)
print("Reservas de C123 después de borrar:", r.smembers("cliente:C123:reservas"))

# 5. Índice de reservas por vehículo
r.sadd("vehiculo:V001:reservas", "R001")
r.sadd("vehiculo:V002:reservas", "R002")
r.sadd("vehiculo:V003:reservas", "R003")
reservas_v001 = r.smembers("vehiculo:V001:reservas")
num_reservas_v001 = r.scard("vehiculo:V001:reservas")
print("\n=== ÍNDICE POR VEHÍCULO ===")
print("Reservas de V001:", reservas_v001)
print("Nº reservas V001:", num_reservas_v001)

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
print("\n=== CONTADORES ===")
print("Total:", r.get("stats:reservas:total"))
print("Activas:", r.get("stats:reservas:activas"))
print("Completadas:", r.get("stats:reservas:completadas"))
print("Canceladas:", r.get("stats:reservas:canceladas"))
print("Reservas día 2025-11-20:", r.get("stats:reservas:dia:2025-11-20"))
print("Reservas mes 2025-11:", r.get("stats:reservas:mes:2025-11"))

# 7. Lista de reservas pendientes de confirmación
r.lpush("cola:reservas:pendientes", "R004", "R005", "R006")
r.rpop("cola:reservas:pendientes")
pendientes = r.lrange("cola:reservas:pendientes", 0, -1)
num_pendientes = r.llen("cola:reservas:pendientes")
print("\n=== COLA DE RESERVAS PENDIENTES ===")
print("Pendientes:", pendientes)
print("Nº pendientes:", num_pendientes)

# 8. Reservas con extensión de tiempo
r.hset("reserva:R001", mapping={"fecha_fin": "2025-11-25", "dias": 5, "precio_total": 447.50, "extension": "true"})
r.expire("reserva:R001", 432000)
nuevo_ttl_r001 = r.ttl("reserva:R001")
print("\n=== EXTENSIÓN DE RESERVA ===")
print("R001 tras extensión:", r.hgetall("reserva:R001"))
print("Nuevo TTL R001:", nuevo_ttl_r001)

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
print("\n=== PRE-RESERVAS ===")
print("Pre-reserva PR001:", prereserva)
print("Reserva R010:", r.hgetall("reserva:R010"))

# 10. Historial de reservas completadas
r.hset("historial:R001", mapping={
    "vehiculo_id": "V001", "cliente_id": "C123", "fecha_inicio": "2025-11-20", "fecha_fin": "2025-11-23",
    "precio_total": 268.50, "estado": "completada", "rating_cliente": 5, "comentario": "Excelente servicio"
})
r.sadd("historial:cliente:C123", "R001", "R007", "R015")
historial_c123 = r.smembers("historial:cliente:C123")
print("\n=== HISTORIAL DE RESERVAS ===")
print("Historial de C123:", historial_c123)
print("Historial R001:", r.hgetall("historial:R001"))
