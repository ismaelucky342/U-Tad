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

# 2. Notificaciones a administradores
r.publish("notifications:admins", "ALERTA: Vehículo V023 requiere mantenimiento urgente")
r.publish("notifications:admins", "INFO: Reserva R045 completada - Cliente muy satisfecho")
r.publish("notifications:admins", "CRÍTICO: Solo quedan 5 vehículos disponibles en Madrid")

# 3. Notificaciones a clientes específicos
r.publish("notifications:client:C123", "Tu reserva R001 ha sido confirmada. Vehículo: Mercedes Sprinter")
r.publish("notifications:client:C123", "Recordatorio: Tu reserva empieza en 1 hora. Ubicación: Madrid Centro")
r.publish("notifications:client:C123", "Tu vehículo está listo para recoger. Puesto: P-15")

# 4. Notificaciones por tipo de evento
r.publish("events:reservas:nueva", '{"reserva_id":"R045","vehiculo":"V001","cliente":"C123","precio":89.50}')
r.publish("events:reservas:completada", '{"reserva_id":"R001","vehiculo":"V001","cliente":"C123","rating":5}')
r.publish("events:reservas:cancelada", '{"reserva_id":"R023","vehiculo":"V005","razon":"Cliente enfermo"}')

# 5. Notificaciones de mantenimiento
r.publish("notifications:taller", "Vehículo V001 entrando a mantenimiento - Revisión 45.000 km")
r.publish("notifications:taller", "Vehículo V023 - URGENTE: Motor hace ruido extraño")
r.publish("notifications:taller", "Vehículo V008 listo para salir del taller")

# 6. Alertas de vehículos en tiempo real
r.publish("tracking:vehicles", '{"vehiculo":"V001","lat":40.4168,"lon":-3.7038,"velocidad":45,"timestamp":"2025-11-20T10:15:00"}')
r.publish("tracking:vehicles", '{"vehiculo":"V001","lat":40.4200,"lon":-3.7100,"velocidad":50,"timestamp":"2025-11-20T10:20:00"}')

# 7. Patrones (wildcard) con psubscribe (solo ejemplo de publish)
r.publish("notifications:client:C123", "Mensaje para C123")
r.publish("notifications:client:C456", "Mensaje para C456")

# 8. Notificaciones por ciudad
r.publish("notifications:city:madrid", "ALERTA: Tráfico intenso en M-30")
r.publish("notifications:city:madrid", "INFO: Nueva zona de carga disponible en Chamartín")
r.publish("notifications:city:barcelona", "ALERTA: Manifestación en Diagonal - Evitar zona")

# 9. Sistema de broadcast (a todos)
r.publish("notifications:broadcast", "MANTENIMIENTO: El sistema estará en mantenimiento de 02:00 a 04:00")
r.publish("notifications:broadcast", "OFERTA: 20% descuento en reservas de fin de semana")
r.publish("notifications:broadcast", "NUEVO: Ahora disponibles vehículos eléctricos en Valencia")

# 10. Notificaciones de emergencia
r.publish("alerts:emergency", "EMERGENCIA: Vehículo V023 reporta accidente en A-2 km 45")
r.publish("alerts:emergency", "URGENTE: Cliente C789 no responde - Reserva R067 activa")

# 11. Chat en tiempo real (soporte)
r.publish("chat:session:abc123", "Agente María: Hola, ¿en qué puedo ayudarte?")
r.publish("chat:session:abc123", "Cliente: Necesito cambiar mi reserva")
r.publish("chat:session:abc123", "Agente María: Claro, dime tu número de reserva")

# 12. Notificaciones de métricas en tiempo real
r.publish("metrics:realtime", '{"tipo":"nueva_reserva","total":235,"ingresos_dia":2456.80}')
r.publish("metrics:realtime", '{"tipo":"vehiculo_devuelto","disponibles":39}')

# 13. Logs en tiempo real
r.publish("logs:error", '{"timestamp":"2025-11-20T10:30:00","service":"reservas","error":"Connection timeout","vehiculo":"V001"}')
r.publish("logs:info", '{"timestamp":"2025-11-20T10:31:00","service":"reservas","message":"Reserva R045 creada exitosamente"}')

# 14. Eventos de integración
r.publish("integration:payment", '{"event":"payment_received","reserva":"R045","amount":89.50,"method":"card"}')
r.publish("integration:gps", '{"vehiculo":"V001","lat":40.4168,"lon":-3.7038,"timestamp":"2025-11-20T10:15:00"}')

# 15. Notificaciones segmentadas por rol
r.publish("role:driver", "Nuevas normas de seguridad vial en vigor desde hoy")
r.publish("role:admin", "Informe mensual disponible en el panel de control")
r.publish("role:vip_client", "Acceso exclusivo: Reserva anticipada de vehículos premium")

# 16. Múltiples suscripciones simultáneas (solo ejemplo de publish)
r.publish("notifications:client:C123", "Mensaje multi-canal")
r.publish("notifications:broadcast", "Mensaje multi-canal")
r.publish("events:reservas:nueva", "Mensaje multi-canal")

# 17. Verificar suscriptores activos (solo comandos redis-cli, no en python)
# r.pubsub_numsub("notifications:drivers")
# r.pubsub_channels()
# r.pubsub_channels("notifications:*")
# r.pubsub_numpat()

# 18. Desuscripción (solo comandos redis-cli, no en python)

# 19. Ejemplo completo: flujo de reserva
r.publish("events:reservas:nueva", '{"reserva_id":"R050","cliente":"C123","vehiculo":"V001"}')
r.publish("notifications:client:C123", "Tu reserva R050 está siendo procesada...")
r.publish("notifications:driver:D456", "Nuevo servicio: Reserva R050 - Vehículo V001 - Inicio: 2025-11-21 09:00")
r.publish("notifications:admins", "Nueva reserva R050 confirmada - Cliente: C123 - Ingresos: +89.50€")
r.publish("metrics:realtime", '{"evento":"nueva_reserva","total_dia":9}')

# 20. Ejemplo: tracking de vehículo en vivo
r.publish("tracking:vehicle:V001", '{"lat":40.4168,"lon":-3.7038,"velocidad":45,"gasolina":75,"timestamp":"2025-11-20T10:15:00"}')
r.publish("tracking:vehicle:V001", '{"lat":40.4200,"lon":-3.7100,"velocidad":50,"gasolina":74,"timestamp":"2025-11-20T10:15:30"}')

# 21. Patrón: notificar y almacenar
r.publish("notifications:client:C123", "Tu reserva está confirmada")
r.lpush("notifications:history:C123", '{"timestamp":"2025-11-20T10:00:00","mensaje":"Tu reserva está confirmada"}')
r.ltrim("notifications:history:C123", 0, 99)

# 22. Uso práctico: worker background
r.publish("events:reservas:nueva", '{"reserva_id":"R050","cliente":"C123","vehiculo":"V001"}')
r.publish("events:reservas:procesada", '{"reserva":"R050","estado":"email_enviado"}')
