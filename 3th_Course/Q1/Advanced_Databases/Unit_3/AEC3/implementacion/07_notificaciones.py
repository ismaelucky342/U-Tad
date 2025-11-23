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

# 1. Canales básicos de notificación
r.publish("notifications:drivers", "Nuevo servicio asignado: V001 → Madrid Centro")
r.publish("notifications:drivers", "Recuerda revisar el combustible antes de salir")
print("\n=== NOTIFICACIONES A CONDUCTORES ===")
print("Mensajes enviados a canal drivers.")

# 2. Notificaciones a administradores
r.publish("notifications:admins", "ALERTA: Vehículo V023 requiere mantenimiento urgente")
r.publish("notifications:admins", "INFO: Reserva R045 completada - Cliente muy satisfecho")
r.publish("notifications:admins", "CRÍTICO: Solo quedan 5 vehículos disponibles en Madrid")
print("\n=== NOTIFICACIONES A ADMINISTRADORES ===")
print("Mensajes enviados a canal admins.")

# 3. Notificaciones a clientes específicos
r.publish("notifications:client:C123", "Tu reserva R001 ha sido confirmada. Vehículo: Mercedes Sprinter")
r.publish("notifications:client:C123", "Recordatorio: Tu reserva empieza en 1 hora. Ubicación: Madrid Centro")
r.publish("notifications:client:C123", "Tu vehículo está listo para recoger. Puesto: P-15")
print("\n=== NOTIFICACIONES A CLIENTES ===")
print("Mensajes enviados a cliente C123.")

# 4. Notificaciones por tipo de evento
r.publish("events:reservas:nueva", '{"reserva_id":"R045","vehiculo":"V001","cliente":"C123","precio":89.50}')
r.publish("events:reservas:completada", '{"reserva_id":"R001","vehiculo":"V001","cliente":"C123","rating":5}')
r.publish("events:reservas:cancelada", '{"reserva_id":"R023","vehiculo":"V005","razon":"Cliente enfermo"}')
print("\n=== NOTIFICACIONES POR EVENTO ===")
print("Mensajes enviados a eventos de reservas.")

# 5. Notificaciones de mantenimiento
r.publish("notifications:taller", "Vehículo V001 entrando a mantenimiento - Revisión 45.000 km")
r.publish("notifications:taller", "Vehículo V023 - URGENTE: Motor hace ruido extraño")
r.publish("notifications:taller", "Vehículo V008 listo para salir del taller")
print("\n=== NOTIFICACIONES DE TALLER ===")
print("Mensajes enviados a canal taller.")

# 6. Alertas de vehículos en tiempo real
r.publish("tracking:vehicles", '{"vehiculo":"V001","lat":40.4168,"lon":-3.7038,"velocidad":45,"timestamp":"2025-11-20T10:15:00"}')
r.publish("tracking:vehicles", '{"vehiculo":"V001","lat":40.4200,"lon":-3.7100,"velocidad":50,"timestamp":"2025-11-20T10:20:00"}')
print("\n=== ALERTAS DE VEHÍCULOS EN TIEMPO REAL ===")
print("Mensajes enviados a tracking:vehicles.")

# 7. Patrones (wildcard) con psubscribe (solo ejemplo de publish)
r.publish("notifications:client:C123", "Mensaje para C123")
r.publish("notifications:client:C456", "Mensaje para C456")
print("\n=== NOTIFICACIONES POR PATRÓN (WILDCARD) ===")
print("Mensajes enviados a clientes C123 y C456.")

# 8. Notificaciones por ciudad
r.publish("notifications:city:madrid", "ALERTA: Tráfico intenso en M-30")
r.publish("notifications:city:madrid", "INFO: Nueva zona de carga disponible en Chamartín")
r.publish("notifications:city:barcelona", "ALERTA: Manifestación en Diagonal - Evitar zona")
print("\n=== NOTIFICACIONES POR CIUDAD ===")
print("Mensajes enviados a Madrid y Barcelona.")

# 9. Sistema de broadcast (a todos)
r.publish("notifications:broadcast", "MANTENIMIENTO: El sistema estará en mantenimiento de 02:00 a 04:00")
r.publish("notifications:broadcast", "OFERTA: 20% descuento en reservas de fin de semana")
r.publish("notifications:broadcast", "NUEVO: Ahora disponibles vehículos eléctricos en Valencia")
print("\n=== BROADCAST GENERAL ===")
print("Mensajes enviados a todos los usuarios.")

# 10. Notificaciones de emergencia
r.publish("alerts:emergency", "EMERGENCIA: Vehículo V023 reporta accidente en A-2 km 45")
r.publish("alerts:emergency", "URGENTE: Cliente C789 no responde - Reserva R067 activa")
print("\n=== NOTIFICACIONES DE EMERGENCIA ===")
print("Mensajes enviados a canal de alertas de emergencia.")
